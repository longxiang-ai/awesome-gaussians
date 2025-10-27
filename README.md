# Awesome Gaussian Splatting [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of latest research papers, projects and resources related to Gaussian Splatting. Content is automatically updated daily.

> Last Update: 2025-10-27 00:56:56

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

- [3DGS Surveys](#3dgs-surveys) (23 papers) - Survey papers and benchmarks about 3D Gaussian Splatting
- [Acceleration](#acceleration) (260 papers) - Papers about speeding up rendering or training
- [Applications](#applications) (995 papers) - Papers about specific applications
- [Avatar Generation](#avatar-generation) (342 papers) - Papers about human avatar generation
- [Dynamic Scene](#dynamic-scene) (392 papers) - Papers about dynamic scene reconstruction and rendering
- [Few-shot](#few-shot) (71 papers) - Papers about few-shot or sparse view reconstruction
- [Geometry Reconstruction](#geometry-reconstruction) (322 papers) - Papers about 3D geometry reconstruction
- [Large Scene](#large-scene) (73 papers) - Papers about large-scale scene reconstruction
- [Model Compression](#model-compression) (407 papers) - Papers about model compression and optimization
- [Quality Enhancement](#quality-enhancement) (175 papers) - Papers focusing on improving rendering quality
- [Ray Tracing](#ray-tracing) (19 papers) - Papers about ray tracing and ray casting in Gaussian Splatting
- [Relighting](#relighting) (124 papers) - Papers about relighting and illumination effects in Gaussian Splatting
- [SLAM](#slam) (148 papers) - Papers about SLAM using Gaussian Splatting
- [Scene Understanding](#scene-understanding) (202 papers) - Papers about scene understanding and semantic analysis



## Table of Contents

- [Categorized Papers](#categorized-papers)
- [Classic Papers](#classic-papers)
- [Open Source Projects](#open-source-projects)
- [Applications](#applications)
- [Tutorials & Blogs](#tutorials--blogs)





## Categorized Papers

### 3DGS Surveys

- **[Advances in 4D Representation: Geometry, Motion, and Interaction](https://arxiv.org/abs/2510.19255v1)**  
  Authors: Mingrui Zhao, Sauradip Nag, Kai Wang, Aditya Vora, Guangda Ji, Peter Chun, Ali Mahdavi-Amiri, Hao Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.19255v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://mingrui-zhao.github.io/4DRep-GMI/)  
  Keywords: fast, gaussian splatting, motion, ar, 3d gaussian, nerf, survey, geometry, 4d  
- **[From Volume Rendering to 3D Gaussian Splatting: Theory and Applications](https://arxiv.org/abs/2510.18101v1)**  
  Authors: Vitor Pereira Matias, Daniel Perazzo, Vinicius Silva, Alberto Raposo, Luiz Velho, Afonso Paiva, Tiago Novello  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.18101v1.pdf)  
  Keywords: lighting, face, gaussian splatting, ar, efficient rendering, animation, 3d reconstruction, 3d gaussian, efficient, survey, real-time rendering, avatar  
- **[Vision Language Models: A Survey of 26K Papers](https://arxiv.org/abs/2510.09586v1)**  
  Authors: Fengming Lin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.09586v1.pdf)  
  Keywords: lightweight, gaussian splatting, understanding, ar, efficient, nerf, survey, human  
- **[From Fields to Splats: A Cross-Domain Survey of Real-Time Neural Scene
  Representations](https://arxiv.org/abs/2509.23555v1)**  
  Authors: Javed Ahmad, Penggang Gao, Donatien Delehelle, Mennuti Canio, Nikhil Deshpande, Jesús Ortiz, Darwin G. Caldwell, Yonas Teodros Tefera  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.23555v1.pdf)  
  Keywords: fast, gaussian splatting, understanding, ar, neural rendering, efficient, 3d gaussian, nerf, survey, slam  
- **[A Survey on 3D Gaussian Splatting Applications: Segmentation, Editing,
  and Generation](https://arxiv.org/abs/2508.09977v2)**  
  Authors: Shuting He, Peilin Ji, Yitong Yang, Changshuo Wang, Jiayi Ji, Yinglin Wang, Henghui Ding  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.09977v2.pdf)  
  Keywords: lighting, gaussian splatting, understanding, ar, semantic, compact, segmentation, 3d gaussian, nerf, survey, high-fidelity  
- **[A Study of the Framework and Real-World Applications of Language
  Embedding for 3D Scene Understanding](https://arxiv.org/abs/2508.05064v2)**  
  Authors: Mahmoud Chick Zaouali, Todd Charter, Yehor Karpichev, Brandon Haworth, Homayoun Najjaran  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.05064v2.pdf)  
  Keywords: gaussian splatting, understanding, ar, semantic, robotics, efficient, 3d gaussian, nerf, survey  
- **[Radiance Fields in XR: A Survey on How Radiance Fields are Envisioned
  and Addressed for XR Research](https://arxiv.org/abs/2508.04326v2)**  
  Authors: Ke Li, Mana Masuda, Susanne Schmidt, Shohei Mori  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.04326v2.pdf)  
  Keywords: gaussian splatting, ar, robotics, 3d gaussian, nerf, survey, human  
- **[Sparse-View 3D Reconstruction: Recent Advances and Open Challenges](https://arxiv.org/abs/2507.16406v1)**  
  Authors: Tanveer Younis, Zhanglin Cheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.16406v1.pdf)  
  Keywords: gaussian splatting, motion, ar, vr, robotics, 3d reconstruction, 3d gaussian, nerf, sparse-view, survey, geometry  
- **[Advances in Feed-Forward 3D Reconstruction and View Synthesis: A Survey](https://arxiv.org/abs/2507.14501v3)**  
  Authors: Jiahui Zhang, Yuelei Li, Anpei Chen, Muyu Xu, Kunhao Liu, Jianyuan Wang, Xiao-Xiao Long, Hanxue Liang, Zexiang Xu, Hao Su, Christian Theobalt, Christian Rupprecht, Andrea Vedaldi, Kaichen Zhou, Paul Pu Liang, Shijian Lu, Fangneng Zhan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.14501v3.pdf)  
  Keywords: lighting, fast, dynamic, gaussian splatting, ar, vr, robotics, 3d reconstruction, 3d gaussian, nerf, survey, slam, human  
- **[3D Gaussian Splatting for Fine-Detailed Surface Reconstruction in
  Large-Scale Scene](https://arxiv.org/abs/2506.17636v1)**  
  Authors: Shihan Chen, Zhaojin Li, Zeyu Chen, Qingsong Yan, Gaoyang Shen, Ran Duan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.17636v1.pdf)  
  Keywords: outdoor, dynamic, gaussian splatting, face, ar, autonomous driving, efficient, 3d gaussian, nerf, survey, high-fidelity  

### Acceleration

*Showing the latest 50 out of 260 papers*

- **[Advances in 4D Representation: Geometry, Motion, and Interaction](https://arxiv.org/abs/2510.19255v1)**  
  Authors: Mingrui Zhao, Sauradip Nag, Kai Wang, Aditya Vora, Guangda Ji, Peter Chun, Ali Mahdavi-Amiri, Hao Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.19255v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://mingrui-zhao.github.io/4DRep-GMI/)  
  Keywords: fast, gaussian splatting, motion, ar, 3d gaussian, nerf, survey, geometry, 4d  
- **[From Volume Rendering to 3D Gaussian Splatting: Theory and Applications](https://arxiv.org/abs/2510.18101v1)**  
  Authors: Vitor Pereira Matias, Daniel Perazzo, Vinicius Silva, Alberto Raposo, Luiz Velho, Afonso Paiva, Tiago Novello  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.18101v1.pdf)  
  Keywords: lighting, face, gaussian splatting, ar, efficient rendering, animation, 3d reconstruction, 3d gaussian, efficient, survey, real-time rendering, avatar  
- **[HGC-Avatar: Hierarchical Gaussian Compression for Streamable Dynamic 3D
  Avatars](https://arxiv.org/abs/2510.16463v1)**  
  Authors: Haocheng Tang, Ruoke Yan, Xinhui Yin, Qi Zhang, Xinfeng Zhang, Siwei Ma, Wen Gao, Chuanmin Jia  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.16463v1.pdf)  
  Keywords: compression, dynamic, gaussian splatting, motion, ar, semantic, compact, efficient, 3d gaussian, fast, avatar, human  
- **[Proactive Scene Decomposition and Reconstruction](https://arxiv.org/abs/2510.16272v1)**  
  Authors: Baicheng Li, Zike Yan, Dong Wu, Hongbin Zha  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.16272v1.pdf)  
  Keywords: dynamic, gaussian splatting, ar, efficient rendering, efficient, human  
- **[Phys2Real: Fusing VLM Priors with Interactive Online Adaptation for
  Uncertainty-Aware Sim-to-Real Manipulation](https://arxiv.org/abs/2510.11689v1)**  
  Authors: Maggie Wang, Stephen Tian, Aiden Swann, Ola Shorinwa, Jiajun Wu, Mac Schwager  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.11689v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://phys2real.github.io/)  
  Keywords: dynamic, gaussian splatting, ar, 3d gaussian, fast, high-fidelity  
- **[P-4DGS: Predictive 4D Gaussian Splatting with 90$\times$ Compression](https://arxiv.org/abs/2510.10030v1)**  
  Authors: Henan Wang, Hanxin Zhu, Xinliang Gong, Tianyu He, Xin Li, Zhibo Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.10030v1.pdf)  
  Keywords: compression, dynamic, gaussian splatting, ar, compact, 3d gaussian, fast, real-time rendering, 4d  
- **[LTGS: Long-Term Gaussian Scene Chronology From Sparse View Updates](https://arxiv.org/abs/2510.09881v1)**  
  Authors: Minkwan Kim, Seungmin Lee, Junho Kim, Young Min Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.09881v1.pdf)  
  Keywords: sparse view, face, gaussian splatting, ar, efficient, sparse-view, fast, few-shot  
- **[FLOWING: Implicit Neural Flows for Structure-Preserving Morphing](https://arxiv.org/abs/2510.09537v1)**  
  Authors: Arthur Bizzi, Matias Grynberg, Vitor Matias, Daniel Perazzo, João Paulo Lima, Luiz Velho, Nuno Gonçalves, João Pereira, Guilherme Schardong, Tiago Novello  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.09537v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](http://schardong.github.io/flowing.)  
  Keywords: deformation, face, gaussian splatting, ar, fast  
- **[ComGS: Efficient 3D Object-Scene Composition via Surface Octahedral
  Probes](https://arxiv.org/abs/2510.07729v1)**  
  Authors: Jian Gao, Mengqi Yuan, Yifei Zeng, Chang Zeng, Zhihao Li, Zhenyu Chen, Weichao Qiu, Xiao-Xiao Long, Hao Zhu, Xun Cao, Yao Yao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.07729v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://nju-3dv.github.io/projects/ComGS/.)  
  Keywords: relightable, lighting, light transport, ray tracing, gaussian splatting, shadow, face, ar, efficient, real-time rendering  
- **[Capture and Interact: Rapid 3D Object Acquisition and Rendering with
  Gaussian Splatting in Unity](https://arxiv.org/abs/2510.06802v1)**  
  Authors: Islomjon Shukhratov, Sergey Gorinsky  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.06802v1.pdf)  
  Keywords: gaussian splatting, ar, 3d reconstruction, 3d gaussian, real-time rendering  

### Applications

*Showing the latest 50 out of 995 papers*

- **[GSWorld: Closed-Loop Photo-Realistic Simulation Suite for Robotic
  Manipulation](https://arxiv.org/abs/2510.20813v1)**  
  Authors: Guangqi Jiang, Haoran Chang, Ri-Zhao Qiu, Yutong Liang, Mazeyu Ji, Jiyue Zhu, Zhao Dong, Xueyan Zou, Xiaolong Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.20813v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://3dgsworld.github.io/.)  
  Keywords: robotics, gaussian splatting, ar, 3d gaussian  
- **[Dino-Diffusion Modular Designs Bridge the Cross-Domain Gap in Autonomous
  Parking](https://arxiv.org/abs/2510.20335v1)**  
  Authors: Zixuan Wu, Hengyuan Zhang, Ting-Hsuan Chen, Yuliang Guo, David Paz, Xinyu Huang, Liu Ren  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.20335v1.pdf)  
  Keywords: lighting, gaussian splatting, ar, motion, 3d gaussian  
- **[COS3D: Collaborative Open-Vocabulary 3D Segmentation](https://arxiv.org/abs/2510.20238v1)**  
  Authors: Runsong Zhu, Ka-Hei Hui, Zhengzhe Liu, Qianyi Wu, Weiliang Tang, Shi Qiu, Pheng-Ann Heng, Chi-Wing Fu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.20238v1.pdf)  
  Keywords: mapping, understanding, ar, segmentation, robotics, efficient  
- **[Extreme Views: 3DGS Filter for Novel View Synthesis from
  Out-of-Distribution Camera Poses](https://arxiv.org/abs/2510.20027v1)**  
  Authors: Damian Bowness, Charalambos Poullis  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.20027v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://damian-bowness.github.io/EV3DGS)  
  Keywords: gaussian splatting, ar, 3d reconstruction, 3d gaussian, nerf, geometry  
- **[Advances in 4D Representation: Geometry, Motion, and Interaction](https://arxiv.org/abs/2510.19255v1)**  
  Authors: Mingrui Zhao, Sauradip Nag, Kai Wang, Aditya Vora, Guangda Ji, Peter Chun, Ali Mahdavi-Amiri, Hao Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.19255v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://mingrui-zhao.github.io/4DRep-GMI/)  
  Keywords: fast, gaussian splatting, motion, ar, 3d gaussian, nerf, survey, geometry, 4d  
- **[MoE-GS: Mixture of Experts for Dynamic Gaussian Splatting](https://arxiv.org/abs/2510.19210v1)**  
  Authors: In-Hwan Jin, Hyeongju Mun, Joonsoo Kim, Kugjin Yun, Kyeongbo Kong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.19210v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://anonymous.4open.science/w/MoE-GS-68BA/.)  
  Keywords: lightweight, dynamic, gaussian splatting, ar, 3d gaussian  
- **[GRASPLAT: Enabling dexterous grasping through novel view synthesis](https://arxiv.org/abs/2510.19200v1)**  
  Authors: Matteo Bortolon, Nuno Ferreira Duarte, Plinio Moreno, Fabio Poiesi, José Santos-Victor, Alessio Del Bue  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.19200v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://mbortolon97.github.io/grasplat/)  
  Keywords: face, gaussian splatting, ar, 3d gaussian, high-fidelity  
- **[Moving Light Adaptive Colonoscopy Reconstruction via
  Illumination-Attenuation-Aware 3D Gaussian Splatting](https://arxiv.org/abs/2510.18739v1)**  
  Authors: Hao Wang, Ying Zhou, Haoyu Zhao, Rui Wang, Qiang Hu, Xing Zhang, Qiang Li, Zhiwei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.18739v1.pdf)  
  Keywords: tracking, dynamic, gaussian splatting, ar, 3d reconstruction, 3d gaussian, illumination, geometry  
- **[Re-Activating Frozen Primitives for 3D Gaussian Splatting](https://arxiv.org/abs/2510.19653v1)**  
  Authors: Yuxin Cheng, Binxiao Huang, Wenyong Zhou, Taiqiang Wu, Zhengwu Liu, Graziano Chesi, Ngai Wong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.19653v1.pdf)  
  Keywords: gaussian splatting, ar, 3d gaussian  
- **[Mono4DGS-HDR: High Dynamic Range 4D Gaussian Splatting from
  Alternating-exposure Monocular Videos](https://arxiv.org/abs/2510.18489v1)**  
  Authors: Jinfeng Liu, Lingtong Kong, Mi Zhou, Jinwen Chen, Dan Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.18489v1.pdf)  
  Keywords: dynamic, gaussian splatting, ar, 4d  

### Avatar Generation

*Showing the latest 50 out of 342 papers*

- **[GRASPLAT: Enabling dexterous grasping through novel view synthesis](https://arxiv.org/abs/2510.19200v1)**  
  Authors: Matteo Bortolon, Nuno Ferreira Duarte, Plinio Moreno, Fabio Poiesi, José Santos-Victor, Alessio Del Bue  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.19200v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://mbortolon97.github.io/grasplat/)  
  Keywords: face, gaussian splatting, ar, 3d gaussian, high-fidelity  
- **[From Volume Rendering to 3D Gaussian Splatting: Theory and Applications](https://arxiv.org/abs/2510.18101v1)**  
  Authors: Vitor Pereira Matias, Daniel Perazzo, Vinicius Silva, Alberto Raposo, Luiz Velho, Afonso Paiva, Tiago Novello  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.18101v1.pdf)  
  Keywords: lighting, face, gaussian splatting, ar, efficient rendering, animation, 3d reconstruction, 3d gaussian, efficient, survey, real-time rendering, avatar  
- **[GSPlane: Concise and Accurate Planar Reconstruction via Structured
  Representation](https://arxiv.org/abs/2510.17095v1)**  
  Authors: Ruitong Gan, Junran Peng, Yang Liu, Chuanchen Luo, Qing Li, Zhaoxiang Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.17095v1.pdf)  
  Keywords: face, gaussian splatting, dynamic, ar, segmentation, geometry  
- **[2DGS-R: Revisiting the Normal Consistency Regularization in 2D Gaussian
  Splatting](https://arxiv.org/abs/2510.16837v1)**  
  Authors: Haofan Ren, Qingsong Yan, Ming Lu, Rongfeng Lu, Zunjie Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.16837v1.pdf)  
  Keywords: head, lighting, face, gaussian splatting, ar, 3d gaussian, high-fidelity  
- **[HGC-Avatar: Hierarchical Gaussian Compression for Streamable Dynamic 3D
  Avatars](https://arxiv.org/abs/2510.16463v1)**  
  Authors: Haocheng Tang, Ruoke Yan, Xinhui Yin, Qi Zhang, Xinfeng Zhang, Siwei Ma, Wen Gao, Chuanmin Jia  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.16463v1.pdf)  
  Keywords: compression, dynamic, gaussian splatting, motion, ar, semantic, compact, efficient, 3d gaussian, fast, avatar, human  
- **[REALM: An MLLM-Agent Framework for Open World 3D Reasoning Segmentation
  and Editing on Gaussian Splatting](https://arxiv.org/abs/2510.16410v1)**  
  Authors: Changyue Shi, Minghao Chen, Yiping Mao, Chuxiao Yang, Xinyuan Hu, Jiajun Ding, Zhou Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.16410v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://ChangyueShi.github.io/REALM.)  
  Keywords: understanding, gaussian splatting, ar, localization, segmentation, robotics, 3d gaussian, human  
- **[Proactive Scene Decomposition and Reconstruction](https://arxiv.org/abs/2510.16272v1)**  
  Authors: Baicheng Li, Zike Yan, Dong Wu, Hongbin Zha  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.16272v1.pdf)  
  Keywords: dynamic, gaussian splatting, ar, efficient rendering, efficient, human  
- **[Leveraging Learned Image Prior for 3D Gaussian Compression](https://arxiv.org/abs/2510.14705v1)**  
  Authors: Seungjoo Shin, Jaesik Park, Sunghyun Cho  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.14705v1.pdf)  
  Keywords: head, compression, gaussian splatting, ar, compact, 3d gaussian  
- **[InsideOut: Integrated RGB-Radiative Gaussian Splatting for Comprehensive
  3D Object Representation](https://arxiv.org/abs/2510.17864v1)**  
  Authors: Jungmin Lee, Seonghyuk Hong, Juyong Lee, Jaeyoon Lee, Jongwon Choi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.17864v1.pdf)  
  Keywords: face, gaussian splatting, ar, 3d gaussian, medical, high-fidelity  
- **[Capture, Canonicalize, Splat: Zero-Shot 3D Gaussian Avatars from
  Unstructured Phone Images](https://arxiv.org/abs/2510.14081v2)**  
  Authors: Emanuel Garbin, Guy Adam, Oded Krams, Zohar Barzelay, Eran Guendelman, Michael Schwarz, Matteo Presutto, Moran Vatelmacher, Yigal Shenkman, Eli Peker, Itai Druker, Uri Patish, Yoav Blum, Max Bluvstein, Junxuan Li, Rawal Khirodkar, Shunsuke Saito  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.14081v2.pdf)  
  Keywords: face, gaussian splatting, ar, body, 3d gaussian, avatar, high-fidelity  

### Dynamic Scene

*Showing the latest 50 out of 392 papers*

- **[Dino-Diffusion Modular Designs Bridge the Cross-Domain Gap in Autonomous
  Parking](https://arxiv.org/abs/2510.20335v1)**  
  Authors: Zixuan Wu, Hengyuan Zhang, Ting-Hsuan Chen, Yuliang Guo, David Paz, Xinyu Huang, Liu Ren  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.20335v1.pdf)  
  Keywords: lighting, gaussian splatting, ar, motion, 3d gaussian  
- **[Advances in 4D Representation: Geometry, Motion, and Interaction](https://arxiv.org/abs/2510.19255v1)**  
  Authors: Mingrui Zhao, Sauradip Nag, Kai Wang, Aditya Vora, Guangda Ji, Peter Chun, Ali Mahdavi-Amiri, Hao Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.19255v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://mingrui-zhao.github.io/4DRep-GMI/)  
  Keywords: fast, gaussian splatting, motion, ar, 3d gaussian, nerf, survey, geometry, 4d  
- **[MoE-GS: Mixture of Experts for Dynamic Gaussian Splatting](https://arxiv.org/abs/2510.19210v1)**  
  Authors: In-Hwan Jin, Hyeongju Mun, Joonsoo Kim, Kugjin Yun, Kyeongbo Kong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.19210v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://anonymous.4open.science/w/MoE-GS-68BA/.)  
  Keywords: lightweight, dynamic, gaussian splatting, ar, 3d gaussian  
- **[Moving Light Adaptive Colonoscopy Reconstruction via
  Illumination-Attenuation-Aware 3D Gaussian Splatting](https://arxiv.org/abs/2510.18739v1)**  
  Authors: Hao Wang, Ying Zhou, Haoyu Zhao, Rui Wang, Qiang Hu, Xing Zhang, Qiang Li, Zhiwei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.18739v1.pdf)  
  Keywords: tracking, dynamic, gaussian splatting, ar, 3d reconstruction, 3d gaussian, illumination, geometry  
- **[Mono4DGS-HDR: High Dynamic Range 4D Gaussian Splatting from
  Alternating-exposure Monocular Videos](https://arxiv.org/abs/2510.18489v1)**  
  Authors: Jinfeng Liu, Lingtong Kong, Mi Zhou, Jinwen Chen, Dan Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.18489v1.pdf)  
  Keywords: dynamic, gaussian splatting, ar, 4d  
- **[From Volume Rendering to 3D Gaussian Splatting: Theory and Applications](https://arxiv.org/abs/2510.18101v1)**  
  Authors: Vitor Pereira Matias, Daniel Perazzo, Vinicius Silva, Alberto Raposo, Luiz Velho, Afonso Paiva, Tiago Novello  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.18101v1.pdf)  
  Keywords: lighting, face, gaussian splatting, ar, efficient rendering, animation, 3d reconstruction, 3d gaussian, efficient, survey, real-time rendering, avatar  
- **[Initialize to Generalize: A Stronger Initialization Pipeline for
  Sparse-View 3DGS](https://arxiv.org/abs/2510.17479v1)**  
  Authors: Feng Zhou, Wenkai Guo, Pu Cao, Zhicheng Zhang, Jianqin Yin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.17479v1.pdf)  
  Keywords: sparse view, gaussian splatting, motion, ar, 3d gaussian, nerf, sparse-view  
- **[GSPlane: Concise and Accurate Planar Reconstruction via Structured
  Representation](https://arxiv.org/abs/2510.17095v1)**  
  Authors: Ruitong Gan, Junran Peng, Yang Liu, Chuanchen Luo, Qing Li, Zhaoxiang Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.17095v1.pdf)  
  Keywords: face, gaussian splatting, dynamic, ar, segmentation, geometry  
- **[HGC-Avatar: Hierarchical Gaussian Compression for Streamable Dynamic 3D
  Avatars](https://arxiv.org/abs/2510.16463v1)**  
  Authors: Haocheng Tang, Ruoke Yan, Xinhui Yin, Qi Zhang, Xinfeng Zhang, Siwei Ma, Wen Gao, Chuanmin Jia  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.16463v1.pdf)  
  Keywords: compression, dynamic, gaussian splatting, motion, ar, semantic, compact, efficient, 3d gaussian, fast, avatar, human  
- **[Proactive Scene Decomposition and Reconstruction](https://arxiv.org/abs/2510.16272v1)**  
  Authors: Baicheng Li, Zike Yan, Dong Wu, Hongbin Zha  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.16272v1.pdf)  
  Keywords: dynamic, gaussian splatting, ar, efficient rendering, efficient, human  

### Few-shot

*Showing the latest 50 out of 71 papers*

- **[Initialize to Generalize: A Stronger Initialization Pipeline for
  Sparse-View 3DGS](https://arxiv.org/abs/2510.17479v1)**  
  Authors: Feng Zhou, Wenkai Guo, Pu Cao, Zhicheng Zhang, Jianqin Yin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.17479v1.pdf)  
  Keywords: sparse view, gaussian splatting, motion, ar, 3d gaussian, nerf, sparse-view  
- **[Opacity-Gradient Driven Density Control for Compact and Efficient
  Few-Shot 3D Gaussian Splatting](https://arxiv.org/abs/2510.10257v1)**  
  Authors: Abdelrhman Elrawy, Emad A. Mohammed  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.10257v1.pdf)  
  Keywords: lightweight, gaussian splatting, ar, compact, efficient, 3d gaussian, nerf, few-shot  
- **[Gesplat: Robust Pose-Free 3D Reconstruction via Geometry-Guided Gaussian
  Splatting](https://arxiv.org/abs/2510.10097v1)**  
  Authors: Jiahui Lu, Haihong Xiao, Xueyan Zhao, Wenxiong Kang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.10097v1.pdf)  
  Keywords: gaussian splatting, ar, 3d reconstruction, 3d gaussian, nerf, sparse-view, geometry  
- **[LTGS: Long-Term Gaussian Scene Chronology From Sparse View Updates](https://arxiv.org/abs/2510.09881v1)**  
  Authors: Minkwan Kim, Seungmin Lee, Junho Kim, Young Min Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.09881v1.pdf)  
  Keywords: sparse view, face, gaussian splatting, ar, efficient, sparse-view, fast, few-shot  
- **[D$^2$GS: Depth-and-Density Guided Gaussian Splatting for Stable and
  Accurate Sparse-View Reconstruction](https://arxiv.org/abs/2510.08566v1)**  
  Authors: Meixi Song, Xin Lin, Dizhe Zhang, Haodong Li, Xiangtai Li, Bo Du, Lu Qi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.08566v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://insta360-research-team.github.io/DDGS-website/.)  
  Keywords: sparse view, gaussian splatting, ar, 3d gaussian, sparse-view, high-fidelity  
- **[FSFSplatter: Build Surface and Novel Views with Sparse-Views within 2min](https://arxiv.org/abs/2510.02691v2)**  
  Authors: Yibin Zhao, Yihan Pan, Jun Nan, Liwei Chen, Jianjun Yi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.02691v2.pdf)  
  Keywords: head, face, gaussian splatting, ar, sparse-view, fast, geometry  
- **[HART: Human Aligned Reconstruction Transformer](https://arxiv.org/abs/2509.26621v1)**  
  Authors: Xiyi Chen, Shaofei Wang, Marko Mihajlovic, Taewon Kang, Sergey Prokudin, Ming Lin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.26621v1.pdf)  
  Keywords: ar, body, sparse-view, geometry, human  
- **[GaussianLens: Localized High-Resolution Reconstruction via On-Demand
  Gaussian Densification](https://arxiv.org/abs/2509.25603v1)**  
  Authors: Yijia Weng, Zhicheng Wang, Songyou Peng, Saining Xie, Howard Zhou, Leonidas J. Guibas  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.25603v1.pdf)  
  Keywords: sparse view, gaussian splatting, ar, 3d gaussian, fast, human  
- **[HBSplat: Robust Sparse-View Gaussian Reconstruction with Hybrid-Loss
  Guided Depth and Bidirectional Warping](https://arxiv.org/abs/2509.24893v3)**  
  Authors: Yu Ma, Guoliang Wei, Haihong Xiao, Yue Cheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.24893v3.pdf)  
  Keywords: sparse view, gaussian splatting, ar, 3d reconstruction, 3d gaussian, sparse-view, high-fidelity  
- **[OracleGS: Grounding Generative Priors for Sparse-View Gaussian Splatting](https://arxiv.org/abs/2509.23258v2)**  
  Authors: Atakan Topaloglu, Kunyi Li, Michael Niemeyer, Nassir Navab, A. Murat Tekalp, Federico Tombari  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.23258v2.pdf)  
  Keywords: sparse view, gaussian splatting, ar, 3d gaussian, sparse-view, nerf  

### Geometry Reconstruction

*Showing the latest 50 out of 322 papers*

- **[Extreme Views: 3DGS Filter for Novel View Synthesis from
  Out-of-Distribution Camera Poses](https://arxiv.org/abs/2510.20027v1)**  
  Authors: Damian Bowness, Charalambos Poullis  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.20027v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://damian-bowness.github.io/EV3DGS)  
  Keywords: gaussian splatting, ar, 3d reconstruction, 3d gaussian, nerf, geometry  
- **[Advances in 4D Representation: Geometry, Motion, and Interaction](https://arxiv.org/abs/2510.19255v1)**  
  Authors: Mingrui Zhao, Sauradip Nag, Kai Wang, Aditya Vora, Guangda Ji, Peter Chun, Ali Mahdavi-Amiri, Hao Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.19255v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://mingrui-zhao.github.io/4DRep-GMI/)  
  Keywords: fast, gaussian splatting, motion, ar, 3d gaussian, nerf, survey, geometry, 4d  
- **[Moving Light Adaptive Colonoscopy Reconstruction via
  Illumination-Attenuation-Aware 3D Gaussian Splatting](https://arxiv.org/abs/2510.18739v1)**  
  Authors: Hao Wang, Ying Zhou, Haoyu Zhao, Rui Wang, Qiang Hu, Xing Zhang, Qiang Li, Zhiwei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.18739v1.pdf)  
  Keywords: tracking, dynamic, gaussian splatting, ar, 3d reconstruction, 3d gaussian, illumination, geometry  
- **[From Volume Rendering to 3D Gaussian Splatting: Theory and Applications](https://arxiv.org/abs/2510.18101v1)**  
  Authors: Vitor Pereira Matias, Daniel Perazzo, Vinicius Silva, Alberto Raposo, Luiz Velho, Afonso Paiva, Tiago Novello  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.18101v1.pdf)  
  Keywords: lighting, face, gaussian splatting, ar, efficient rendering, animation, 3d reconstruction, 3d gaussian, efficient, survey, real-time rendering, avatar  
- **[HouseTour: A Virtual Real Estate A(I)gent](https://arxiv.org/abs/2510.18054v1)**  
  Authors: Ata Çelen, Marc Pollefeys, Daniel Barath, Iro Armeni  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.18054v1.pdf)  
  Keywords: ar, gaussian splatting, 3d reconstruction, 3d gaussian  
- **[GSPlane: Concise and Accurate Planar Reconstruction via Structured
  Representation](https://arxiv.org/abs/2510.17095v1)**  
  Authors: Ruitong Gan, Junran Peng, Yang Liu, Chuanchen Luo, Qing Li, Zhaoxiang Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.17095v1.pdf)  
  Keywords: face, gaussian splatting, dynamic, ar, segmentation, geometry  
- **[SaLon3R: Structure-aware Long-term Generalizable 3D Reconstruction from
  Unposed Images](https://arxiv.org/abs/2510.15072v1)**  
  Authors: Jiaxin Guo, Tongfan Guan, Wenzhen Dong, Wenzhao Zheng, Wenting Wang, Yue Wang, Yeung Yam, Yun-Hui Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.15072v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://wrld.github.io/SaLon3R/.)  
  Keywords: ar, gaussian splatting, compact, 3d reconstruction, 3d gaussian  
- **[BalanceGS: Algorithm-System Co-design for Efficient 3D Gaussian
  Splatting Training on GPU](https://arxiv.org/abs/2510.14564v1)**  
  Authors: Junyi Wu, Jiaming Xu, Jinhao Li, Yongkang Zhou, Jiayi Pan, Xingyang Li, Guohao Dai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.14564v1.pdf)  
  Keywords: mapping, dynamic, gaussian splatting, ar, 3d reconstruction, 3d gaussian, efficient  
- **[GauSSmart: Enhanced 3D Reconstruction through 2D Foundation Models and
  Geometric Filtering](https://arxiv.org/abs/2510.14270v1)**  
  Authors: Alexander Valverde, Brian Xu, Yuyin Zhou, Meng Xu, Hongyun Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.14270v1.pdf)  
  Keywords: lighting, gaussian splatting, ar, semantic, segmentation, 3d reconstruction, 3d gaussian, nerf  
- **[VIST3A: Text-to-3D by Stitching a Multi-view Reconstruction Network to a
  Video Generator](https://arxiv.org/abs/2510.13454v1)**  
  Authors: Hyojun Go, Dominik Narnhofer, Goutam Bhat, Prune Truong, Federico Tombari, Konrad Schindler  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.13454v1.pdf)  
  Keywords: geometry, ar, 3d reconstruction, human  

### Large Scene

*Showing the latest 50 out of 73 papers*

- **[Leveraging 2D Priors and SDF Guidance for Dynamic Urban Scene Rendering](https://arxiv.org/abs/2510.13381v1)**  
  Authors: Siddharth Tourani, Jayaram Reddy, Akash Kumbar, Satyajit Tourani, Nishant Goyal, Madhava Krishna, N. Dinesh Reddy, Muhammad Haris Khan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.13381v1.pdf)  
  Keywords: urban scene, deformation, dynamic, gaussian splatting, motion, ar, segmentation, 3d gaussian, tracking  
- **[PAGS: Priority-Adaptive Gaussian Splatting for Dynamic Driving Scenes](https://arxiv.org/abs/2510.12282v1)**  
  Authors: Ying A, Wenzhang Sun, Chang Zeng, Chunfeng Wang, Hao Li, Jianxun Cui  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.12282v1.pdf)  
  Keywords: urban scene, face, dynamic, gaussian splatting, ar, semantic, autonomous driving, 3d reconstruction  
- **[Two-Stage Gaussian Splatting Optimization for Outdoor Scene
  Reconstruction](https://arxiv.org/abs/2510.09489v1)**  
  Authors: Deborah Pintani, Ariel Caputo, Noah Lewis, Marc Stamminger, Fabio Pellacini, Andrea Giachetti  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.09489v1.pdf)  
  Keywords: outdoor, gaussian splatting, ar, motion, illumination  
- **[Visibility-Aware Densification for 3D Gaussian Splatting in Dynamic
  Urban Scenes](https://arxiv.org/abs/2510.09364v1)**  
  Authors: Yikang Zhang, Rui Fan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.09364v1.pdf)  
  Keywords: urban scene, dynamic, gaussian splatting, face, ar, 3d gaussian, geometry, high-fidelity  
- **[LOBE-GS: Load-Balanced and Efficient 3D Gaussian Splatting for
  Large-Scale Scene Reconstruction](https://arxiv.org/abs/2510.01767v1)**  
  Authors: Sheng-Hsiang Hung, Ting-Yu Yen, Wei-Fang Sun, Simon See, Shih-Hsuan Hung, Hung-Kuo Chu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.01767v1.pdf)  
  Keywords: head, outdoor, lightweight, gaussian splatting, ar, efficient, 3d gaussian, fast, high-fidelity  
- **[LVT: Large-Scale Scene Reconstruction via Local View Transformers](https://arxiv.org/abs/2509.25001v1)**  
  Authors: Tooba Imtiaz, Lucy Chai, Kathryn Heal, Xuan Luo, Jungyeon Park, Jennifer Dy, John Flynn  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.25001v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://toobaimt.github.io/lvt/.)  
  Keywords: ar, 3d gaussian, large scene  
- **[Aerial-Ground Image Feature Matching via 3D Gaussian Splatting-based
  Intermediate View Rendering](https://arxiv.org/abs/2509.19898v1)**  
  Authors: Jiangxue Yu, Hui Wang, San Jiang, Xing Zhang, Dejin Zhang, Qingquan Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.19898v1.pdf)  
  Keywords: gaussian splatting, ar, motion, large scene, 3d gaussian  
- **[FGGS-LiDAR: Ultra-Fast, GPU-Accelerated Simulation from General 3DGS
  Models to LiDAR](https://arxiv.org/abs/2509.17390v1)**  
  Authors: Junzhe Wu, Yufei Jia, Yiyi Yan, Zhixing Chen, Tiao Tan, Zifan Wang, Guangyu Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.17390v1.pdf)  
  Keywords: outdoor, gaussian splatting, ar, robotics, autonomous driving, 3d gaussian, fast, high-fidelity  
- **[ROSGS: Relightable Outdoor Scenes With Gaussian Splatting](https://arxiv.org/abs/2509.11275v1)**  
  Authors: Lianjun Liao, Chunhui Zhang, Tong Wu, Henglei Lv, Bailin Deng, Lin Gao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.11275v1.pdf)  
  Keywords: relightable, head, lighting, outdoor, gaussian splatting, ar, efficient rendering, compact, efficient, 3d gaussian, nerf, illumination, geometry, relighting  
- **[VIM-GS: Visual-Inertial Monocular Gaussian Splatting via Object-level
  Guidance in Large Scenes](https://arxiv.org/abs/2509.06685v3)**  
  Authors: Shengkai Zhang, Yuhe Liu, Guanjun Wu, Jianhua He, Xinggang Wang, Mozi Chen, Kezhong Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.06685v3.pdf)  
  Keywords: dynamic, gaussian splatting, ar, large scene, motion  

### Model Compression

*Showing the latest 50 out of 407 papers*

- **[COS3D: Collaborative Open-Vocabulary 3D Segmentation](https://arxiv.org/abs/2510.20238v1)**  
  Authors: Runsong Zhu, Ka-Hei Hui, Zhengzhe Liu, Qianyi Wu, Weiliang Tang, Shi Qiu, Pheng-Ann Heng, Chi-Wing Fu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.20238v1.pdf)  
  Keywords: mapping, understanding, ar, segmentation, robotics, efficient  
- **[MoE-GS: Mixture of Experts for Dynamic Gaussian Splatting](https://arxiv.org/abs/2510.19210v1)**  
  Authors: In-Hwan Jin, Hyeongju Mun, Joonsoo Kim, Kugjin Yun, Kyeongbo Kong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.19210v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://anonymous.4open.science/w/MoE-GS-68BA/.)  
  Keywords: lightweight, dynamic, gaussian splatting, ar, 3d gaussian  
- **[From Volume Rendering to 3D Gaussian Splatting: Theory and Applications](https://arxiv.org/abs/2510.18101v1)**  
  Authors: Vitor Pereira Matias, Daniel Perazzo, Vinicius Silva, Alberto Raposo, Luiz Velho, Afonso Paiva, Tiago Novello  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.18101v1.pdf)  
  Keywords: lighting, face, gaussian splatting, ar, efficient rendering, animation, 3d reconstruction, 3d gaussian, efficient, survey, real-time rendering, avatar  
- **[HGC-Avatar: Hierarchical Gaussian Compression for Streamable Dynamic 3D
  Avatars](https://arxiv.org/abs/2510.16463v1)**  
  Authors: Haocheng Tang, Ruoke Yan, Xinhui Yin, Qi Zhang, Xinfeng Zhang, Siwei Ma, Wen Gao, Chuanmin Jia  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.16463v1.pdf)  
  Keywords: compression, dynamic, gaussian splatting, motion, ar, semantic, compact, efficient, 3d gaussian, fast, avatar, human  
- **[Proactive Scene Decomposition and Reconstruction](https://arxiv.org/abs/2510.16272v1)**  
  Authors: Baicheng Li, Zike Yan, Dong Wu, Hongbin Zha  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.16272v1.pdf)  
  Keywords: dynamic, gaussian splatting, ar, efficient rendering, efficient, human  
- **[SaLon3R: Structure-aware Long-term Generalizable 3D Reconstruction from
  Unposed Images](https://arxiv.org/abs/2510.15072v1)**  
  Authors: Jiaxin Guo, Tongfan Guan, Wenzhen Dong, Wenzhao Zheng, Wenting Wang, Yue Wang, Yeung Yam, Yun-Hui Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.15072v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://wrld.github.io/SaLon3R/.)  
  Keywords: ar, gaussian splatting, compact, 3d reconstruction, 3d gaussian  
- **[Leveraging Learned Image Prior for 3D Gaussian Compression](https://arxiv.org/abs/2510.14705v1)**  
  Authors: Seungjoo Shin, Jaesik Park, Sunghyun Cho  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.14705v1.pdf)  
  Keywords: head, compression, gaussian splatting, ar, compact, 3d gaussian  
- **[BalanceGS: Algorithm-System Co-design for Efficient 3D Gaussian
  Splatting Training on GPU](https://arxiv.org/abs/2510.14564v1)**  
  Authors: Junyi Wu, Jiaming Xu, Jinhao Li, Yongkang Zhou, Jiayi Pan, Xingyang Li, Guohao Dai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.14564v1.pdf)  
  Keywords: mapping, dynamic, gaussian splatting, ar, 3d reconstruction, 3d gaussian, efficient  
- **[Virtually Being: Customizing Camera-Controllable Video Diffusion Models
  with Multi-View Performance Captures](https://arxiv.org/abs/2510.14179v1)**  
  Authors: Yuancheng Xu, Wenqi Xian, Li Ma, Julien Philip, Ahmet Levent Taşel, Yiwei Zhao, Ryan Burgert, Mingming He, Oliver Hermann, Oliver Pilarski, Rahul Garg, Paul Debevec, Ning Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.14179v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://eyeline-labs.github.io/Virtually-Being.)  
  Keywords: lighting, gaussian splatting, motion, ar, efficient, relighting, 4d  
- **[Instant Skinned Gaussian Avatars for Web, Mobile and VR Applications](https://arxiv.org/abs/2510.13978v2)**  
  Authors: Naruya Kondo, Yuto Asano, Yoichi Ochiai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.13978v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://gaussian-vrm.github.io/)  
  Keywords: lightweight, dynamic, gaussian splatting, ar, vr, efficient, avatar  

### Quality Enhancement

*Showing the latest 50 out of 175 papers*

- **[GRASPLAT: Enabling dexterous grasping through novel view synthesis](https://arxiv.org/abs/2510.19200v1)**  
  Authors: Matteo Bortolon, Nuno Ferreira Duarte, Plinio Moreno, Fabio Poiesi, José Santos-Victor, Alessio Del Bue  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.19200v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://mbortolon97.github.io/grasplat/)  
  Keywords: face, gaussian splatting, ar, 3d gaussian, high-fidelity  
- **[2DGS-R: Revisiting the Normal Consistency Regularization in 2D Gaussian
  Splatting](https://arxiv.org/abs/2510.16837v1)**  
  Authors: Haofan Ren, Qingsong Yan, Ming Lu, Rongfeng Lu, Zunjie Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.16837v1.pdf)  
  Keywords: head, lighting, face, gaussian splatting, ar, 3d gaussian, high-fidelity  
- **[GaussGym: An open-source real-to-sim framework for learning locomotion
  from pixels](https://arxiv.org/abs/2510.15352v1)**  
  Authors: Alejandro Escontrela, Justin Kerr, Arthur Allshire, Jonas Frey, Rocky Duan, Carmelo Sferrazza, Pieter Abbeel  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.15352v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://escontrela.me/gauss_gym/.)  
  Keywords: gaussian splatting, motion, ar, semantic, robotics, 3d gaussian, high-fidelity  
- **[InsideOut: Integrated RGB-Radiative Gaussian Splatting for Comprehensive
  3D Object Representation](https://arxiv.org/abs/2510.17864v1)**  
  Authors: Jungmin Lee, Seonghyuk Hong, Juyong Lee, Jaeyoon Lee, Jongwon Choi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.17864v1.pdf)  
  Keywords: face, gaussian splatting, ar, 3d gaussian, medical, high-fidelity  
- **[Capture, Canonicalize, Splat: Zero-Shot 3D Gaussian Avatars from
  Unstructured Phone Images](https://arxiv.org/abs/2510.14081v2)**  
  Authors: Emanuel Garbin, Guy Adam, Oded Krams, Zohar Barzelay, Eran Guendelman, Michael Schwarz, Matteo Presutto, Moran Vatelmacher, Yigal Shenkman, Eli Peker, Itai Druker, Uri Patish, Yoav Blum, Max Bluvstein, Junxuan Li, Rawal Khirodkar, Shunsuke Saito  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.14081v2.pdf)  
  Keywords: face, gaussian splatting, ar, body, 3d gaussian, avatar, high-fidelity  
- **[UniGS: Unified Geometry-Aware Gaussian Splatting for Multimodal
  Rendering](https://arxiv.org/abs/2510.12174v1)**  
  Authors: Yusen Xie, Zhenmin Huang, Jianhao Jiao, Dimitrios Kanoulas, Jun Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.12174v1.pdf)  
  Keywords: face, gaussian splatting, ar, semantic, 3d reconstruction, 3d gaussian, geometry, high-fidelity  
- **[Phys2Real: Fusing VLM Priors with Interactive Online Adaptation for
  Uncertainty-Aware Sim-to-Real Manipulation](https://arxiv.org/abs/2510.11689v1)**  
  Authors: Maggie Wang, Stephen Tian, Aiden Swann, Ola Shorinwa, Jiajun Wu, Mac Schwager  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.11689v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://phys2real.github.io/)  
  Keywords: dynamic, gaussian splatting, ar, 3d gaussian, fast, high-fidelity  
- **[High-Fidelity Simulated Data Generation for Real-World Zero-Shot Robotic
  Manipulation Learning with Gaussian Splatting](https://arxiv.org/abs/2510.10637v1)**  
  Authors: Haoyu Zhao, Cheng Zeng, Linghao Zhuang, Yaxi Zhao, Shengke Xue, Hao Wang, Xingyue Zhao, Zhongyu Li, Kehan Li, Siteng Huang, Mingxiu Chen, Xin Li, Deli Zhao, Hua Zou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.10637v1.pdf)  
  Keywords: ar, gaussian splatting, high-fidelity, 3d gaussian  
- **[CLoD-GS: Continuous Level-of-Detail via 3D Gaussian Splatting](https://arxiv.org/abs/2510.09997v1)**  
  Authors: Zhigang Cheng, Mingchao Sun, Yu Liu, Zengye Ge, Luyang Tang, Mu Xu, Yangyan Li, Peng Pan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.09997v1.pdf)  
  Keywords: head, dynamic, gaussian splatting, ar, 3d gaussian, high-fidelity  
- **[Visibility-Aware Densification for 3D Gaussian Splatting in Dynamic
  Urban Scenes](https://arxiv.org/abs/2510.09364v1)**  
  Authors: Yikang Zhang, Rui Fan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.09364v1.pdf)  
  Keywords: urban scene, dynamic, gaussian splatting, face, ar, 3d gaussian, geometry, high-fidelity  

### Ray Tracing

- **[MaterialRefGS: Reflective Gaussian Splatting with Multi-view Consistent
  Material Inference](https://arxiv.org/abs/2510.11387v2)**  
  Authors: Wenyuan Zhang, Jimin Tang, Weiqi Zhang, Yi Fang, Yu-Shen Liu, Zhizhong Han  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.11387v2.pdf)  
  Keywords: ray tracing, gaussian splatting, ar, reflection, illumination, geometry  
- **[Splat the Net: Radiance Fields with Splattable Neural Primitives](https://arxiv.org/abs/2510.08491v1)**  
  Authors: Xilong Zhou, Bao-Huy Nguyen, Loïc Magne, Vladislav Golyanik, Thomas Leimkühler, Christian Theobalt  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.08491v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://vcai.mpi-inf.mpg.de/projects/SplatNet/.)  
  Keywords: gaussian splatting, ar, efficient, 3d gaussian, ray marching, geometry  
- **[ComGS: Efficient 3D Object-Scene Composition via Surface Octahedral
  Probes](https://arxiv.org/abs/2510.07729v1)**  
  Authors: Jian Gao, Mengqi Yuan, Yifei Zeng, Chang Zeng, Zhihao Li, Zhenyu Chen, Weichao Qiu, Xiao-Xiao Long, Hao Zhu, Xun Cao, Yao Yao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.07729v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://nju-3dv.github.io/projects/ComGS/.)  
  Keywords: relightable, lighting, light transport, ray tracing, gaussian splatting, shadow, face, ar, efficient, real-time rendering  
- **[Differentiable Light Transport with Gaussian Surfels via Adapted
  Radiosity for Efficient Relighting and Geometry Reconstruction](https://arxiv.org/abs/2509.18497v2)**  
  Authors: Kaiwen Jiang, Jia-Mu Sun, Zilu Li, Dan Wang, Tzu-Mao Li, Ravi Ramamoorthi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.18497v2.pdf)  
  Keywords: lighting, light transport, gaussian splatting, ar, global illumination, reflection, efficient, illumination, geometry, relighting  
- **[Every Camera Effect, Every Time, All at Once: 4D Gaussian Ray Tracing
  for Physics-based Camera Effect Data Generation](https://arxiv.org/abs/2509.10759v2)**  
  Authors: Yi-Ruei Liu, You-Zhe Xie, Yu-Hsiang Hsu, I-Sheng Fang, Yu-Lun Liu, Jun-Cheng Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.10759v2.pdf)  
  Keywords: ray tracing, gaussian splatting, dynamic, ar, fast, 4d  
- **[GOGS: High-Fidelity Geometry and Relighting for Glossy Objects via
  Gaussian Surfels](https://arxiv.org/abs/2508.14563v1)**  
  Authors: Xingyuan Yang, Min Wei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.14563v1.pdf)  
  Keywords: lighting, ray tracing, gaussian splatting, face, ar, reflection, 3d gaussian, nerf, illumination, geometry, high-fidelity, relighting  
- **[GaRe: Relightable 3D Gaussian Splatting for Outdoor Scenes from
  Unconstrained Photo Collections](https://arxiv.org/abs/2507.20512v1)**  
  Authors: Haiyang Bai, Jiaqi Zhu, Songru Jiang, Wei Huang, Tao Lu, Yuanqi Li, Jie Guo, Runze Fu, Yanwen Guo, Lijun Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.20512v1.pdf)  
  Keywords: relightable, lighting, outdoor, dynamic, gaussian splatting, shadow, face, global illumination, ar, 3d gaussian, illumination, relighting  
- **[GSCache: Real-Time Radiance Caching for Volume Path Tracing using 3D
  Gaussian Splatting](https://arxiv.org/abs/2507.19718v2)**  
  Authors: David Bauer, Qi Wu, Hamid Gadirov, Kwan-Liu Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.19718v2.pdf)  
  Keywords: lighting, dynamic, gaussian splatting, face, ar, path tracing, 3d gaussian  
- **[Gaussian Splatting with Discretized SDF for Relightable Assets](https://arxiv.org/abs/2507.15629v1)**  
  Authors: Zuo-Liang Zhu, Jian Yang, Beibei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.15629v1.pdf)  
  Keywords: relightable, lighting, face, gaussian splatting, ar, efficient rendering, efficient, 3d gaussian, ray marching, geometry, relighting  
- **[RaRa Clipper: A Clipper for Gaussian Splatting Based on Ray Tracer and
  Rasterizer](https://arxiv.org/abs/2506.20202v1)**  
  Authors: Da Li, Donggang Jia, Yousef Rajeh, Dominik Engel, Ivan Viola  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.20202v1.pdf)  
  Keywords: ray tracing, gaussian splatting, ar, efficient, real-time rendering, high-fidelity  

### Relighting

*Showing the latest 50 out of 124 papers*

- **[Dino-Diffusion Modular Designs Bridge the Cross-Domain Gap in Autonomous
  Parking](https://arxiv.org/abs/2510.20335v1)**  
  Authors: Zixuan Wu, Hengyuan Zhang, Ting-Hsuan Chen, Yuliang Guo, David Paz, Xinyu Huang, Liu Ren  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.20335v1.pdf)  
  Keywords: lighting, gaussian splatting, ar, motion, 3d gaussian  
- **[Moving Light Adaptive Colonoscopy Reconstruction via
  Illumination-Attenuation-Aware 3D Gaussian Splatting](https://arxiv.org/abs/2510.18739v1)**  
  Authors: Hao Wang, Ying Zhou, Haoyu Zhao, Rui Wang, Qiang Hu, Xing Zhang, Qiang Li, Zhiwei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.18739v1.pdf)  
  Keywords: tracking, dynamic, gaussian splatting, ar, 3d reconstruction, 3d gaussian, illumination, geometry  
- **[From Volume Rendering to 3D Gaussian Splatting: Theory and Applications](https://arxiv.org/abs/2510.18101v1)**  
  Authors: Vitor Pereira Matias, Daniel Perazzo, Vinicius Silva, Alberto Raposo, Luiz Velho, Afonso Paiva, Tiago Novello  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.18101v1.pdf)  
  Keywords: lighting, face, gaussian splatting, ar, efficient rendering, animation, 3d reconstruction, 3d gaussian, efficient, survey, real-time rendering, avatar  
- **[2DGS-R: Revisiting the Normal Consistency Regularization in 2D Gaussian
  Splatting](https://arxiv.org/abs/2510.16837v1)**  
  Authors: Haofan Ren, Qingsong Yan, Ming Lu, Rongfeng Lu, Zunjie Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.16837v1.pdf)  
  Keywords: head, lighting, face, gaussian splatting, ar, 3d gaussian, high-fidelity  
- **[GauSSmart: Enhanced 3D Reconstruction through 2D Foundation Models and
  Geometric Filtering](https://arxiv.org/abs/2510.14270v1)**  
  Authors: Alexander Valverde, Brian Xu, Yuyin Zhou, Meng Xu, Hongyun Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.14270v1.pdf)  
  Keywords: lighting, gaussian splatting, ar, semantic, segmentation, 3d reconstruction, 3d gaussian, nerf  
- **[Virtually Being: Customizing Camera-Controllable Video Diffusion Models
  with Multi-View Performance Captures](https://arxiv.org/abs/2510.14179v1)**  
  Authors: Yuancheng Xu, Wenqi Xian, Li Ma, Julien Philip, Ahmet Levent Taşel, Yiwei Zhao, Ryan Burgert, Mingming He, Oliver Hermann, Oliver Pilarski, Rahul Garg, Paul Debevec, Ning Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.14179v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://eyeline-labs.github.io/Virtually-Being.)  
  Keywords: lighting, gaussian splatting, motion, ar, efficient, relighting, 4d  
- **[VA-GS: Enhancing the Geometric Representation of Gaussian Splatting via
  View Alignment](https://arxiv.org/abs/2510.11473v1)**  
  Authors: Qing Li, Huifang Feng, Xun Gong, Yu-Shen Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.11473v1.pdf)  
  Keywords: lighting, face, gaussian splatting, ar, efficient, 3d gaussian, illumination, geometry  
- **[MaterialRefGS: Reflective Gaussian Splatting with Multi-view Consistent
  Material Inference](https://arxiv.org/abs/2510.11387v2)**  
  Authors: Wenyuan Zhang, Jimin Tang, Weiqi Zhang, Yi Fang, Yu-Shen Liu, Zhizhong Han  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.11387v2.pdf)  
  Keywords: ray tracing, gaussian splatting, ar, reflection, illumination, geometry  
- **[Two-Stage Gaussian Splatting Optimization for Outdoor Scene
  Reconstruction](https://arxiv.org/abs/2510.09489v1)**  
  Authors: Deborah Pintani, Ariel Caputo, Noah Lewis, Marc Stamminger, Fabio Pellacini, Andrea Giachetti  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.09489v1.pdf)  
  Keywords: outdoor, gaussian splatting, ar, motion, illumination  
- **[ComGS: Efficient 3D Object-Scene Composition via Surface Octahedral
  Probes](https://arxiv.org/abs/2510.07729v1)**  
  Authors: Jian Gao, Mengqi Yuan, Yifei Zeng, Chang Zeng, Zhihao Li, Zhenyu Chen, Weichao Qiu, Xiao-Xiao Long, Hao Zhu, Xun Cao, Yao Yao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.07729v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://nju-3dv.github.io/projects/ComGS/.)  
  Keywords: relightable, lighting, light transport, ray tracing, gaussian splatting, shadow, face, ar, efficient, real-time rendering  

### SLAM

*Showing the latest 50 out of 148 papers*

- **[COS3D: Collaborative Open-Vocabulary 3D Segmentation](https://arxiv.org/abs/2510.20238v1)**  
  Authors: Runsong Zhu, Ka-Hei Hui, Zhengzhe Liu, Qianyi Wu, Weiliang Tang, Shi Qiu, Pheng-Ann Heng, Chi-Wing Fu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.20238v1.pdf)  
  Keywords: mapping, understanding, ar, segmentation, robotics, efficient  
- **[Moving Light Adaptive Colonoscopy Reconstruction via
  Illumination-Attenuation-Aware 3D Gaussian Splatting](https://arxiv.org/abs/2510.18739v1)**  
  Authors: Hao Wang, Ying Zhou, Haoyu Zhao, Rui Wang, Qiang Hu, Xing Zhang, Qiang Li, Zhiwei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.18739v1.pdf)  
  Keywords: tracking, dynamic, gaussian splatting, ar, 3d reconstruction, 3d gaussian, illumination, geometry  
- **[REALM: An MLLM-Agent Framework for Open World 3D Reasoning Segmentation
  and Editing on Gaussian Splatting](https://arxiv.org/abs/2510.16410v1)**  
  Authors: Changyue Shi, Minghao Chen, Yiping Mao, Chuxiao Yang, Xinyuan Hu, Jiajun Ding, Zhou Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.16410v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://ChangyueShi.github.io/REALM.)  
  Keywords: understanding, gaussian splatting, ar, localization, segmentation, robotics, 3d gaussian, human  
- **[BalanceGS: Algorithm-System Co-design for Efficient 3D Gaussian
  Splatting Training on GPU](https://arxiv.org/abs/2510.14564v1)**  
  Authors: Junyi Wu, Jiaming Xu, Jinhao Li, Yongkang Zhou, Jiayi Pan, Xingyang Li, Guohao Dai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.14564v1.pdf)  
  Keywords: mapping, dynamic, gaussian splatting, ar, 3d reconstruction, 3d gaussian, efficient  
- **[Leveraging 2D Priors and SDF Guidance for Dynamic Urban Scene Rendering](https://arxiv.org/abs/2510.13381v1)**  
  Authors: Siddharth Tourani, Jayaram Reddy, Akash Kumbar, Satyajit Tourani, Nishant Goyal, Madhava Krishna, N. Dinesh Reddy, Muhammad Haris Khan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.13381v1.pdf)  
  Keywords: urban scene, deformation, dynamic, gaussian splatting, motion, ar, segmentation, 3d gaussian, tracking  
- **[Color3D: Controllable and Consistent 3D Colorization with Personalized
  Colorizer](https://arxiv.org/abs/2510.10152v1)**  
  Authors: Yecong Wan, Mingwen Shao, Renlong Wu, Wangmeng Zuo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.10152v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://yecongwan.github.io/Color3D/.)  
  Keywords: dynamic, gaussian splatting, ar, mapping  
- **[VG-Mapping: Variation-Aware 3D Gaussians for Online Semi-static Scene
  Mapping](https://arxiv.org/abs/2510.09962v1)**  
  Authors: Yicheng He, Jingwen Yu, Guangcheng Chen, Hong Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.09962v1.pdf)  
  Keywords: mapping, gaussian splatting, ar, localization, efficient, 3d gaussian  
- **[SCas4D: Structural Cascaded Optimization for Boosting Persistent 4D
  Novel View Synthesis](https://arxiv.org/abs/2510.06694v1)**  
  Authors: Jipeng Lyu, Jiahua Dong, Yu-Xiong Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.06694v1.pdf)  
  Keywords: deformation, dynamic, gaussian splatting, ar, segmentation, 3d gaussian, tracking, 4d  
- **[RTGS: Real-Time 3D Gaussian Splatting SLAM via Multi-Level Redundancy
  Reduction](https://arxiv.org/abs/2510.06644v2)**  
  Authors: Leshu Li, Jiayin Qin, Jie Peng, Zishen Wan, Huaizhi Qu, Ye Han, Pingqing Zheng, Hongsen Zhang, Yu Cao, Tianlong Chen, Yang Katie Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.06644v2.pdf)  
  Keywords: head, mapping, acceleration, gaussian splatting, dynamic, ar, localization, 3d gaussian, slam  
- **[Geometry Meets Vision: Revisiting Pretrained Semantics in Distilled
  Fields](https://arxiv.org/abs/2510.03104v1)**  
  Authors: Zhiting Mei, Ola Shorinwa, Anirudha Majumdar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.03104v1.pdf)  
  Keywords: gaussian splatting, ar, semantic, localization, geometry  

### Scene Understanding

*Showing the latest 50 out of 202 papers*

- **[COS3D: Collaborative Open-Vocabulary 3D Segmentation](https://arxiv.org/abs/2510.20238v1)**  
  Authors: Runsong Zhu, Ka-Hei Hui, Zhengzhe Liu, Qianyi Wu, Weiliang Tang, Shi Qiu, Pheng-Ann Heng, Chi-Wing Fu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.20238v1.pdf)  
  Keywords: mapping, understanding, ar, segmentation, robotics, efficient  
- **[OpenInsGaussian: Open-vocabulary Instance Gaussian Segmentation with
  Context-aware Cross-view Fusion](https://arxiv.org/abs/2510.18253v1)**  
  Authors: Tianyu Huang, Runnan Chen, Dongting Hu, Fengming Huang, Mingming Gong, Tongliang Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.18253v1.pdf)  
  Keywords: gaussian splatting, understanding, ar, semantic, segmentation, robotics, autonomous driving, 3d gaussian  
- **[GSPlane: Concise and Accurate Planar Reconstruction via Structured
  Representation](https://arxiv.org/abs/2510.17095v1)**  
  Authors: Ruitong Gan, Junran Peng, Yang Liu, Chuanchen Luo, Qing Li, Zhaoxiang Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.17095v1.pdf)  
  Keywords: face, gaussian splatting, dynamic, ar, segmentation, geometry  
- **[HGC-Avatar: Hierarchical Gaussian Compression for Streamable Dynamic 3D
  Avatars](https://arxiv.org/abs/2510.16463v1)**  
  Authors: Haocheng Tang, Ruoke Yan, Xinhui Yin, Qi Zhang, Xinfeng Zhang, Siwei Ma, Wen Gao, Chuanmin Jia  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.16463v1.pdf)  
  Keywords: compression, dynamic, gaussian splatting, motion, ar, semantic, compact, efficient, 3d gaussian, fast, avatar, human  
- **[REALM: An MLLM-Agent Framework for Open World 3D Reasoning Segmentation
  and Editing on Gaussian Splatting](https://arxiv.org/abs/2510.16410v1)**  
  Authors: Changyue Shi, Minghao Chen, Yiping Mao, Chuxiao Yang, Xinyuan Hu, Jiajun Ding, Zhou Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.16410v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://ChangyueShi.github.io/REALM.)  
  Keywords: understanding, gaussian splatting, ar, localization, segmentation, robotics, 3d gaussian, human  
- **[GaussGym: An open-source real-to-sim framework for learning locomotion
  from pixels](https://arxiv.org/abs/2510.15352v1)**  
  Authors: Alejandro Escontrela, Justin Kerr, Arthur Allshire, Jonas Frey, Rocky Duan, Carmelo Sferrazza, Pieter Abbeel  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.15352v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://escontrela.me/gauss_gym/.)  
  Keywords: gaussian splatting, motion, ar, semantic, robotics, 3d gaussian, high-fidelity  
- **[GauSSmart: Enhanced 3D Reconstruction through 2D Foundation Models and
  Geometric Filtering](https://arxiv.org/abs/2510.14270v1)**  
  Authors: Alexander Valverde, Brian Xu, Yuyin Zhou, Meng Xu, Hongyun Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.14270v1.pdf)  
  Keywords: lighting, gaussian splatting, ar, semantic, segmentation, 3d reconstruction, 3d gaussian, nerf  
- **[Leveraging 2D Priors and SDF Guidance for Dynamic Urban Scene Rendering](https://arxiv.org/abs/2510.13381v1)**  
  Authors: Siddharth Tourani, Jayaram Reddy, Akash Kumbar, Satyajit Tourani, Nishant Goyal, Madhava Krishna, N. Dinesh Reddy, Muhammad Haris Khan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.13381v1.pdf)  
  Keywords: urban scene, deformation, dynamic, gaussian splatting, motion, ar, segmentation, 3d gaussian, tracking  
- **[PAGS: Priority-Adaptive Gaussian Splatting for Dynamic Driving Scenes](https://arxiv.org/abs/2510.12282v1)**  
  Authors: Ying A, Wenzhang Sun, Chang Zeng, Chunfeng Wang, Hao Li, Jianxun Cui  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.12282v1.pdf)  
  Keywords: urban scene, face, dynamic, gaussian splatting, ar, semantic, autonomous driving, 3d reconstruction  
- **[UniGS: Unified Geometry-Aware Gaussian Splatting for Multimodal
  Rendering](https://arxiv.org/abs/2510.12174v1)**  
  Authors: Yusen Xie, Zhenmin Huang, Jianhao Jiao, Dimitrios Kanoulas, Jun Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.12174v1.pdf)  
  Keywords: face, gaussian splatting, ar, semantic, 3d reconstruction, 3d gaussian, geometry, high-fidelity  



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