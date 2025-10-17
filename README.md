# Awesome Gaussian Splatting [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of latest research papers, projects and resources related to Gaussian Splatting. Content is automatically updated daily.

> Last Update: 2025-10-17 00:51:13

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

- [3DGS Surveys](#3dgs-surveys) (21 papers) - Survey papers and benchmarks about 3D Gaussian Splatting
- [Acceleration](#acceleration) (262 papers) - Papers about speeding up rendering or training
- [Applications](#applications) (995 papers) - Papers about specific applications
- [Avatar Generation](#avatar-generation) (340 papers) - Papers about human avatar generation
- [Dynamic Scene](#dynamic-scene) (389 papers) - Papers about dynamic scene reconstruction and rendering
- [Few-shot](#few-shot) (73 papers) - Papers about few-shot or sparse view reconstruction
- [Geometry Reconstruction](#geometry-reconstruction) (324 papers) - Papers about 3D geometry reconstruction
- [Large Scene](#large-scene) (75 papers) - Papers about large-scale scene reconstruction
- [Model Compression](#model-compression) (413 papers) - Papers about model compression and optimization
- [Quality Enhancement](#quality-enhancement) (172 papers) - Papers focusing on improving rendering quality
- [Ray Tracing](#ray-tracing) (19 papers) - Papers about ray tracing and ray casting in Gaussian Splatting
- [Relighting](#relighting) (120 papers) - Papers about relighting and illumination effects in Gaussian Splatting
- [SLAM](#slam) (151 papers) - Papers about SLAM using Gaussian Splatting
- [Scene Understanding](#scene-understanding) (198 papers) - Papers about scene understanding and semantic analysis



## Table of Contents

- [Categorized Papers](#categorized-papers)
- [Classic Papers](#classic-papers)
- [Open Source Projects](#open-source-projects)
- [Applications](#applications)
- [Tutorials & Blogs](#tutorials--blogs)





## Categorized Papers

### 3DGS Surveys

- **[Vision Language Models: A Survey of 26K Papers](https://arxiv.org/abs/2510.09586v1)**  
  Authors: Fengming Lin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.09586v1.pdf)  
  Keywords: nerf, understanding, human, lightweight, survey, ar, efficient, gaussian splatting  
- **[From Fields to Splats: A Cross-Domain Survey of Real-Time Neural Scene
  Representations](https://arxiv.org/abs/2509.23555v1)**  
  Authors: Javed Ahmad, Penggang Gao, Donatien Delehelle, Mennuti Canio, Nikhil Deshpande, Jesús Ortiz, Darwin G. Caldwell, Yonas Teodros Tefera  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.23555v1.pdf)  
  Keywords: neural rendering, nerf, understanding, slam, fast, survey, ar, efficient, gaussian splatting, 3d gaussian  
- **[A Survey on 3D Gaussian Splatting Applications: Segmentation, Editing,
  and Generation](https://arxiv.org/abs/2508.09977v2)**  
  Authors: Shuting He, Peilin Ji, Yitong Yang, Changshuo Wang, Jiayi Ji, Yinglin Wang, Henghui Ding  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.09977v2.pdf)  
  Keywords: nerf, segmentation, high-fidelity, understanding, compact, lighting, survey, semantic, ar, gaussian splatting, 3d gaussian  
- **[A Study of the Framework and Real-World Applications of Language
  Embedding for 3D Scene Understanding](https://arxiv.org/abs/2508.05064v2)**  
  Authors: Mahmoud Chick Zaouali, Todd Charter, Yehor Karpichev, Brandon Haworth, Homayoun Najjaran  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.05064v2.pdf)  
  Keywords: nerf, understanding, robotics, survey, semantic, efficient, gaussian splatting, 3d gaussian, ar  
- **[Radiance Fields in XR: A Survey on How Radiance Fields are Envisioned
  and Addressed for XR Research](https://arxiv.org/abs/2508.04326v2)**  
  Authors: Ke Li, Mana Masuda, Susanne Schmidt, Shohei Mori  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.04326v2.pdf)  
  Keywords: nerf, human, robotics, survey, ar, gaussian splatting, 3d gaussian  
- **[Sparse-View 3D Reconstruction: Recent Advances and Open Challenges](https://arxiv.org/abs/2507.16406v1)**  
  Authors: Tanveer Younis, Zhanglin Cheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.16406v1.pdf)  
  Keywords: nerf, 3d reconstruction, geometry, vr, motion, robotics, survey, ar, gaussian splatting, 3d gaussian, sparse-view  
- **[Advances in Feed-Forward 3D Reconstruction and View Synthesis: A Survey](https://arxiv.org/abs/2507.14501v3)**  
  Authors: Jiahui Zhang, Yuelei Li, Anpei Chen, Muyu Xu, Kunhao Liu, Jianyuan Wang, Xiao-Xiao Long, Hanxue Liang, Zexiang Xu, Hao Su, Christian Theobalt, Christian Rupprecht, Andrea Vedaldi, Kaichen Zhou, Paul Pu Liang, Shijian Lu, Fangneng Zhan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.14501v3.pdf)  
  Keywords: nerf, 3d reconstruction, slam, human, vr, lighting, fast, robotics, dynamic, survey, ar, gaussian splatting, 3d gaussian  
- **[3D Gaussian Splatting for Fine-Detailed Surface Reconstruction in
  Large-Scale Scene](https://arxiv.org/abs/2506.17636v1)**  
  Authors: Shihan Chen, Zhaojin Li, Zeyu Chen, Qingsong Yan, Gaoyang Shen, Ran Duan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.17636v1.pdf)  
  Keywords: face, nerf, high-fidelity, dynamic, survey, ar, efficient, gaussian splatting, 3d gaussian, outdoor, autonomous driving  
- **[R3eVision: A Survey on Robust Rendering, Restoration, and Enhancement
  for 3D Low-Level Vision](https://arxiv.org/abs/2506.16262v2)**  
  Authors: Weeyoung Kwon, Jeahun Sung, Minkyu Jeon, Chanho Eom, Jihyong Oh  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.16262v2.pdf)  
  Keywords: neural rendering, nerf, high-fidelity, 3d reconstruction, vr, robotics, survey, ar, gaussian splatting, 3d gaussian, autonomous driving  
- **[From Flight to Insight: Semantic 3D Reconstruction for Aerial Inspection
  via Gaussian Splatting and Language-Guided Segmentation](https://arxiv.org/abs/2505.17402v1)**  
  Authors: Mahmoud Chick Zaouali, Todd Charter, Homayoun Najjaran  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.17402v1.pdf)  
  Keywords: neural rendering, segmentation, high-fidelity, 3d reconstruction, understanding, survey, semantic, efficient, gaussian splatting, 3d gaussian, ar, outdoor  

### Acceleration

*Showing the latest 50 out of 262 papers*

- **[Phys2Real: Fusing VLM Priors with Interactive Online Adaptation for
  Uncertainty-Aware Sim-to-Real Manipulation](https://arxiv.org/abs/2510.11689v1)**  
  Authors: Maggie Wang, Stephen Tian, Aiden Swann, Ola Shorinwa, Jiajun Wu, Mac Schwager  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.11689v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://phys2real.github.io/)  
  Keywords: high-fidelity, fast, dynamic, ar, gaussian splatting, 3d gaussian  
- **[P-4DGS: Predictive 4D Gaussian Splatting with 90$\times$ Compression](https://arxiv.org/abs/2510.10030v1)**  
  Authors: Henan Wang, Hanxin Zhu, Xinliang Gong, Tianyu He, Xin Li, Zhibo Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.10030v1.pdf)  
  Keywords: compression, compact, fast, dynamic, ar, gaussian splatting, 3d gaussian, real-time rendering, 4d  
- **[LTGS: Long-Term Gaussian Scene Chronology From Sparse View Updates](https://arxiv.org/abs/2510.09881v1)**  
  Authors: Minkwan Kim, Seungmin Lee, Junho Kim, Young Min Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.09881v1.pdf)  
  Keywords: face, few-shot, fast, sparse view, ar, efficient, gaussian splatting, sparse-view  
- **[FLOWING: Implicit Neural Flows for Structure-Preserving Morphing](https://arxiv.org/abs/2510.09537v1)**  
  Authors: Arthur Bizzi, Matias Grynberg, Vitor Matias, Daniel Perazzo, João Paulo Lima, Luiz Velho, Nuno Gonçalves, João Pereira, Guilherme Schardong, Tiago Novello  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.09537v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](http://schardong.github.io/flowing.)  
  Keywords: face, deformation, fast, ar, gaussian splatting  
- **[ComGS: Efficient 3D Object-Scene Composition via Surface Octahedral
  Probes](https://arxiv.org/abs/2510.07729v1)**  
  Authors: Jian Gao, Mengqi Yuan, Yifei Zeng, Chang Zeng, Zhihao Li, Zhenyu Chen, Weichao Qiu, Xiao-Xiao Long, Hao Zhu, Xun Cao, Yao Yao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.07729v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://nju-3dv.github.io/projects/ComGS/.)  
  Keywords: face, light transport, ray tracing, lighting, relightable, ar, efficient, gaussian splatting, real-time rendering, shadow  
- **[Capture and Interact: Rapid 3D Object Acquisition and Rendering with
  Gaussian Splatting in Unity](https://arxiv.org/abs/2510.06802v1)**  
  Authors: Islomjon Shukhratov, Sergey Gorinsky  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.06802v1.pdf)  
  Keywords: 3d reconstruction, ar, gaussian splatting, 3d gaussian, real-time rendering  
- **[RTGS: Real-Time 3D Gaussian Splatting SLAM via Multi-Level Redundancy
  Reduction](https://arxiv.org/abs/2510.06644v2)**  
  Authors: Leshu Li, Jiayin Qin, Jie Peng, Zishen Wan, Huaizhi Qu, Ye Han, Pingqing Zheng, Hongsen Zhang, Yu Cao, Tianlong Chen, Yang Katie Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.06644v2.pdf)  
  Keywords: head, localization, acceleration, slam, dynamic, ar, gaussian splatting, 3d gaussian, mapping  
- **[ArchitectHead: Continuous Level of Detail Control for 3D Gaussian Head
  Avatars](https://arxiv.org/abs/2510.05488v1)**  
  Authors: Peizhi Yan, Rabab Ward, Qiang Tang, Shan Du  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.05488v1.pdf)  
  Keywords: avatar, head, lightweight, dynamic, ar, efficient, gaussian splatting, 3d gaussian, real-time rendering  
- **[Optimized Minimal 4D Gaussian Splatting](https://arxiv.org/abs/2510.03857v1)**  
  Authors: Minseo Lee, Byeonghyeon Lee, Lucas Yunkyu Lee, Eunsoo Lee, Sangmin Kim, Seunghyeon Song, Joo Chan Lee, Jong Hwan Ko, Jaesik Park, Eunbyung Park  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.03857v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://minshirley.github.io/OMG4/.)  
  Keywords: face, high-fidelity, head, compression, compact, motion, dynamic, ar, gaussian splatting, real-time rendering, 4d  
- **[FSFSplatter: Build Surface and Novel Views with Sparse-Views within 2min](https://arxiv.org/abs/2510.02691v2)**  
  Authors: Yibin Zhao, Yihan Pan, Jun Nan, Liwei Chen, Jianjun Yi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.02691v2.pdf)  
  Keywords: face, head, geometry, fast, ar, gaussian splatting, sparse-view  

### Applications

*Showing the latest 50 out of 995 papers*

- **[VIST3A: Text-to-3D by Stitching a Multi-view Reconstruction Network to a
  Video Generator](https://arxiv.org/abs/2510.13454v1)**  
  Authors: Hyojun Go, Dominik Narnhofer, Goutam Bhat, Prune Truong, Federico Tombari, Konrad Schindler  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.13454v1.pdf)  
  Keywords: 3d reconstruction, geometry, human, ar  
- **[Leveraging 2D Priors and SDF Guidance for Dynamic Urban Scene Rendering](https://arxiv.org/abs/2510.13381v1)**  
  Authors: Siddharth Tourani, Jayaram Reddy, Akash Kumbar, Satyajit Tourani, Nishant Goyal, Madhava Krishna, N. Dinesh Reddy, Muhammad Haris Khan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.13381v1.pdf)  
  Keywords: segmentation, tracking, deformation, urban scene, motion, dynamic, ar, gaussian splatting, 3d gaussian  
- **[STT-GS: Sample-Then-Transmit Edge Gaussian Splatting with Joint Client
  Selection and Power Control](https://arxiv.org/abs/2510.13186v1)**  
  Authors: Zhen Li, Xibin Jin, Guoliang Li, Shuai Wang, Miaowen Wen, Huseyin Arslan, Derrick Wing Kwan Ng, Chengzhong Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.13186v1.pdf)  
  Keywords: efficient, gaussian splatting, ar, head  
- **[Uncertainty Matters in Dynamic Gaussian Splatting for Monocular 4D
  Reconstruction](https://arxiv.org/abs/2510.12768v1)**  
  Authors: Fengzhi Guo, Chih-Chuan Hsu, Sihao Ding, Cheng Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.12768v1.pdf)  
  Keywords: geometry, motion, dynamic, ar, efficient, gaussian splatting, 4d  
- **[BSGS: Bi-stage 3D Gaussian Splatting for Camera Motion Deblurring](https://arxiv.org/abs/2510.12493v1)**  
  Authors: An Zhao, Piaopiao Yu, Zhe Zhu, Mingqiang Wei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.12493v1.pdf)  
  Keywords: motion, dynamic, ar, gaussian splatting, 3d gaussian  
- **[Hybrid Gaussian Splatting for Novel Urban View Synthesis](https://arxiv.org/abs/2510.12308v1)**  
  Authors: Mohamed Omran, Farhad Zanjani, Davide Abati, Jens Petersen, Amirhossein Habibian  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.12308v1.pdf)  
  Keywords: 3d reconstruction, gaussian splatting, ar  
- **[PAGS: Priority-Adaptive Gaussian Splatting for Dynamic Driving Scenes](https://arxiv.org/abs/2510.12282v1)**  
  Authors: Ying A, Wenzhang Sun, Chang Zeng, Chunfeng Wang, Hao Li, Jianxun Cui  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.12282v1.pdf)  
  Keywords: face, 3d reconstruction, urban scene, dynamic, ar, semantic, gaussian splatting, autonomous driving  
- **[UniGS: Unified Geometry-Aware Gaussian Splatting for Multimodal
  Rendering](https://arxiv.org/abs/2510.12174v1)**  
  Authors: Yusen Xie, Zhenmin Huang, Jianhao Jiao, Dimitrios Kanoulas, Jun Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.12174v1.pdf)  
  Keywords: face, high-fidelity, 3d reconstruction, geometry, ar, semantic, gaussian splatting, 3d gaussian  
- **[GS-Verse: Mesh-based Gaussian Splatting for Physics-aware Interaction in
  Virtual Reality](https://arxiv.org/abs/2510.11878v1)**  
  Authors: Anastasiya Pechko, Piotr Borycki, Joanna Waczyńska, Daniel Barczyk, Agata Szymańska, Sławomir Tadeja, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.11878v1.pdf)  
  Keywords: face, deformation, vr, ar, efficient, gaussian splatting  
- **[Ev4DGS: Novel-view Rendering of Non-Rigid Objects from Monocular Event
  Streams](https://arxiv.org/abs/2510.11717v1)**  
  Authors: Takuya Nakabayashi, Navami Kairanda, Hideo Saito, Vladislav Golyanik  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.11717v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://4dqv.mpi-inf.mpg.de/Ev4DGS/.)  
  Keywords: deformation, ar, efficient, gaussian splatting, 3d gaussian, 4d  

### Avatar Generation

*Showing the latest 50 out of 340 papers*

- **[VIST3A: Text-to-3D by Stitching a Multi-view Reconstruction Network to a
  Video Generator](https://arxiv.org/abs/2510.13454v1)**  
  Authors: Hyojun Go, Dominik Narnhofer, Goutam Bhat, Prune Truong, Federico Tombari, Konrad Schindler  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.13454v1.pdf)  
  Keywords: 3d reconstruction, geometry, human, ar  
- **[STT-GS: Sample-Then-Transmit Edge Gaussian Splatting with Joint Client
  Selection and Power Control](https://arxiv.org/abs/2510.13186v1)**  
  Authors: Zhen Li, Xibin Jin, Guoliang Li, Shuai Wang, Miaowen Wen, Huseyin Arslan, Derrick Wing Kwan Ng, Chengzhong Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.13186v1.pdf)  
  Keywords: efficient, gaussian splatting, ar, head  
- **[PAGS: Priority-Adaptive Gaussian Splatting for Dynamic Driving Scenes](https://arxiv.org/abs/2510.12282v1)**  
  Authors: Ying A, Wenzhang Sun, Chang Zeng, Chunfeng Wang, Hao Li, Jianxun Cui  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.12282v1.pdf)  
  Keywords: face, 3d reconstruction, urban scene, dynamic, ar, semantic, gaussian splatting, autonomous driving  
- **[UniGS: Unified Geometry-Aware Gaussian Splatting for Multimodal
  Rendering](https://arxiv.org/abs/2510.12174v1)**  
  Authors: Yusen Xie, Zhenmin Huang, Jianhao Jiao, Dimitrios Kanoulas, Jun Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.12174v1.pdf)  
  Keywords: face, high-fidelity, 3d reconstruction, geometry, ar, semantic, gaussian splatting, 3d gaussian  
- **[GS-Verse: Mesh-based Gaussian Splatting for Physics-aware Interaction in
  Virtual Reality](https://arxiv.org/abs/2510.11878v1)**  
  Authors: Anastasiya Pechko, Piotr Borycki, Joanna Waczyńska, Daniel Barczyk, Agata Szymańska, Sławomir Tadeja, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.11878v1.pdf)  
  Keywords: face, deformation, vr, ar, efficient, gaussian splatting  
- **[VA-GS: Enhancing the Geometric Representation of Gaussian Splatting via
  View Alignment](https://arxiv.org/abs/2510.11473v1)**  
  Authors: Qing Li, Huifang Feng, Xun Gong, Yu-Shen Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.11473v1.pdf)  
  Keywords: face, illumination, geometry, lighting, ar, efficient, gaussian splatting, 3d gaussian  
- **[Towards Efficient 3D Gaussian Human Avatar Compression: A Prior-Guided
  Framework](https://arxiv.org/abs/2510.10492v1)**  
  Authors: Shanzhi Yin, Bolin Chen, Xinju Wu, Ru-Ling Liao, Jie Chen, Shiqi Wang, Yan Ye  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.10492v1.pdf)  
  Keywords: avatar, human, compact, compression, body, dynamic, ar, efficient, gaussian splatting, 3d gaussian  
- **[CLoD-GS: Continuous Level-of-Detail via 3D Gaussian Splatting](https://arxiv.org/abs/2510.09997v1)**  
  Authors: Zhigang Cheng, Mingchao Sun, Yu Liu, Zengye Ge, Luyang Tang, Mu Xu, Yangyan Li, Peng Pan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.09997v1.pdf)  
  Keywords: head, high-fidelity, dynamic, ar, gaussian splatting, 3d gaussian  
- **[LTGS: Long-Term Gaussian Scene Chronology From Sparse View Updates](https://arxiv.org/abs/2510.09881v1)**  
  Authors: Minkwan Kim, Seungmin Lee, Junho Kim, Young Min Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.09881v1.pdf)  
  Keywords: face, few-shot, fast, sparse view, ar, efficient, gaussian splatting, sparse-view  
- **[Vision Language Models: A Survey of 26K Papers](https://arxiv.org/abs/2510.09586v1)**  
  Authors: Fengming Lin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.09586v1.pdf)  
  Keywords: nerf, understanding, human, lightweight, survey, ar, efficient, gaussian splatting  

### Dynamic Scene

*Showing the latest 50 out of 389 papers*

- **[Leveraging 2D Priors and SDF Guidance for Dynamic Urban Scene Rendering](https://arxiv.org/abs/2510.13381v1)**  
  Authors: Siddharth Tourani, Jayaram Reddy, Akash Kumbar, Satyajit Tourani, Nishant Goyal, Madhava Krishna, N. Dinesh Reddy, Muhammad Haris Khan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.13381v1.pdf)  
  Keywords: segmentation, tracking, deformation, urban scene, motion, dynamic, ar, gaussian splatting, 3d gaussian  
- **[Uncertainty Matters in Dynamic Gaussian Splatting for Monocular 4D
  Reconstruction](https://arxiv.org/abs/2510.12768v1)**  
  Authors: Fengzhi Guo, Chih-Chuan Hsu, Sihao Ding, Cheng Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.12768v1.pdf)  
  Keywords: geometry, motion, dynamic, ar, efficient, gaussian splatting, 4d  
- **[BSGS: Bi-stage 3D Gaussian Splatting for Camera Motion Deblurring](https://arxiv.org/abs/2510.12493v1)**  
  Authors: An Zhao, Piaopiao Yu, Zhe Zhu, Mingqiang Wei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.12493v1.pdf)  
  Keywords: motion, dynamic, ar, gaussian splatting, 3d gaussian  
- **[PAGS: Priority-Adaptive Gaussian Splatting for Dynamic Driving Scenes](https://arxiv.org/abs/2510.12282v1)**  
  Authors: Ying A, Wenzhang Sun, Chang Zeng, Chunfeng Wang, Hao Li, Jianxun Cui  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.12282v1.pdf)  
  Keywords: face, 3d reconstruction, urban scene, dynamic, ar, semantic, gaussian splatting, autonomous driving  
- **[GS-Verse: Mesh-based Gaussian Splatting for Physics-aware Interaction in
  Virtual Reality](https://arxiv.org/abs/2510.11878v1)**  
  Authors: Anastasiya Pechko, Piotr Borycki, Joanna Waczyńska, Daniel Barczyk, Agata Szymańska, Sławomir Tadeja, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.11878v1.pdf)  
  Keywords: face, deformation, vr, ar, efficient, gaussian splatting  
- **[Ev4DGS: Novel-view Rendering of Non-Rigid Objects from Monocular Event
  Streams](https://arxiv.org/abs/2510.11717v1)**  
  Authors: Takuya Nakabayashi, Navami Kairanda, Hideo Saito, Vladislav Golyanik  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.11717v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://4dqv.mpi-inf.mpg.de/Ev4DGS/.)  
  Keywords: deformation, ar, efficient, gaussian splatting, 3d gaussian, 4d  
- **[Phys2Real: Fusing VLM Priors with Interactive Online Adaptation for
  Uncertainty-Aware Sim-to-Real Manipulation](https://arxiv.org/abs/2510.11689v1)**  
  Authors: Maggie Wang, Stephen Tian, Aiden Swann, Ola Shorinwa, Jiajun Wu, Mac Schwager  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.11689v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://phys2real.github.io/)  
  Keywords: high-fidelity, fast, dynamic, ar, gaussian splatting, 3d gaussian  
- **[Dynamic Gaussian Splatting from Defocused and Motion-blurred Monocular
  Videos](https://arxiv.org/abs/2510.10691v1)**  
  Authors: Xuankai Zhang, Junjin Xiao, Qing Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.10691v1.pdf)  
  Keywords: motion, gaussian splatting, dynamic, ar  
- **[Towards Efficient 3D Gaussian Human Avatar Compression: A Prior-Guided
  Framework](https://arxiv.org/abs/2510.10492v1)**  
  Authors: Shanzhi Yin, Bolin Chen, Xinju Wu, Ru-Ling Liao, Jie Chen, Shiqi Wang, Yan Ye  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.10492v1.pdf)  
  Keywords: avatar, human, compact, compression, body, dynamic, ar, efficient, gaussian splatting, 3d gaussian  
- **[Color3D: Controllable and Consistent 3D Colorization with Personalized
  Colorizer](https://arxiv.org/abs/2510.10152v1)**  
  Authors: Yecong Wan, Mingwen Shao, Renlong Wu, Wangmeng Zuo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.10152v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://yecongwan.github.io/Color3D/.)  
  Keywords: gaussian splatting, mapping, dynamic, ar  

### Few-shot

*Showing the latest 50 out of 73 papers*

- **[Opacity-Gradient Driven Density Control for Compact and Efficient
  Few-Shot 3D Gaussian Splatting](https://arxiv.org/abs/2510.10257v1)**  
  Authors: Abdelrhman Elrawy, Emad A. Mohammed  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.10257v1.pdf)  
  Keywords: nerf, few-shot, compact, lightweight, ar, efficient, gaussian splatting, 3d gaussian  
- **[Gesplat: Robust Pose-Free 3D Reconstruction via Geometry-Guided Gaussian
  Splatting](https://arxiv.org/abs/2510.10097v1)**  
  Authors: Jiahui Lu, Haihong Xiao, Xueyan Zhao, Wenxiong Kang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.10097v1.pdf)  
  Keywords: nerf, 3d reconstruction, geometry, ar, gaussian splatting, 3d gaussian, sparse-view  
- **[LTGS: Long-Term Gaussian Scene Chronology From Sparse View Updates](https://arxiv.org/abs/2510.09881v1)**  
  Authors: Minkwan Kim, Seungmin Lee, Junho Kim, Young Min Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.09881v1.pdf)  
  Keywords: face, few-shot, fast, sparse view, ar, efficient, gaussian splatting, sparse-view  
- **[D$^2$GS: Depth-and-Density Guided Gaussian Splatting for Stable and
  Accurate Sparse-View Reconstruction](https://arxiv.org/abs/2510.08566v1)**  
  Authors: Meixi Song, Xin Lin, Dizhe Zhang, Haodong Li, Xiangtai Li, Bo Du, Lu Qi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.08566v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://insta360-research-team.github.io/DDGS-website/.)  
  Keywords: high-fidelity, sparse view, ar, gaussian splatting, 3d gaussian, sparse-view  
- **[FSFSplatter: Build Surface and Novel Views with Sparse-Views within 2min](https://arxiv.org/abs/2510.02691v2)**  
  Authors: Yibin Zhao, Yihan Pan, Jun Nan, Liwei Chen, Jianjun Yi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.02691v2.pdf)  
  Keywords: face, head, geometry, fast, ar, gaussian splatting, sparse-view  
- **[HART: Human Aligned Reconstruction Transformer](https://arxiv.org/abs/2509.26621v1)**  
  Authors: Xiyi Chen, Shaofei Wang, Marko Mihajlovic, Taewon Kang, Sergey Prokudin, Ming Lin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.26621v1.pdf)  
  Keywords: geometry, human, body, ar, sparse-view  
- **[GaussianLens: Localized High-Resolution Reconstruction via On-Demand
  Gaussian Densification](https://arxiv.org/abs/2509.25603v1)**  
  Authors: Yijia Weng, Zhicheng Wang, Songyou Peng, Saining Xie, Howard Zhou, Leonidas J. Guibas  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.25603v1.pdf)  
  Keywords: human, fast, sparse view, ar, gaussian splatting, 3d gaussian  
- **[HBSplat: Robust Sparse-View Gaussian Reconstruction with Hybrid-Loss
  Guided Depth and Bidirectional Warping](https://arxiv.org/abs/2509.24893v3)**  
  Authors: Yu Ma, Guoliang Wei, Haihong Xiao, Yue Cheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.24893v3.pdf)  
  Keywords: high-fidelity, 3d reconstruction, sparse view, ar, gaussian splatting, 3d gaussian, sparse-view  
- **[OracleGS: Grounding Generative Priors for Sparse-View Gaussian Splatting](https://arxiv.org/abs/2509.23258v2)**  
  Authors: Atakan Topaloglu, Kunyi Li, Michael Niemeyer, Nassir Navab, A. Murat Tekalp, Federico Tombari  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.23258v2.pdf)  
  Keywords: nerf, sparse view, ar, gaussian splatting, 3d gaussian, sparse-view  
- **[WaveletGaussian: Wavelet-domain Diffusion for Sparse-view 3D Gaussian
  Object Reconstruction](https://arxiv.org/abs/2509.19073v1)**  
  Authors: Hung Nguyen, Runfa Li, An Le, Truong Nguyen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.19073v1.pdf)  
  Keywords: nerf, lightweight, ar, efficient, gaussian splatting, 3d gaussian, sparse-view  

### Geometry Reconstruction

*Showing the latest 50 out of 324 papers*

- **[VIST3A: Text-to-3D by Stitching a Multi-view Reconstruction Network to a
  Video Generator](https://arxiv.org/abs/2510.13454v1)**  
  Authors: Hyojun Go, Dominik Narnhofer, Goutam Bhat, Prune Truong, Federico Tombari, Konrad Schindler  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.13454v1.pdf)  
  Keywords: 3d reconstruction, geometry, human, ar  
- **[Uncertainty Matters in Dynamic Gaussian Splatting for Monocular 4D
  Reconstruction](https://arxiv.org/abs/2510.12768v1)**  
  Authors: Fengzhi Guo, Chih-Chuan Hsu, Sihao Ding, Cheng Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.12768v1.pdf)  
  Keywords: geometry, motion, dynamic, ar, efficient, gaussian splatting, 4d  
- **[Hybrid Gaussian Splatting for Novel Urban View Synthesis](https://arxiv.org/abs/2510.12308v1)**  
  Authors: Mohamed Omran, Farhad Zanjani, Davide Abati, Jens Petersen, Amirhossein Habibian  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.12308v1.pdf)  
  Keywords: 3d reconstruction, gaussian splatting, ar  
- **[PAGS: Priority-Adaptive Gaussian Splatting for Dynamic Driving Scenes](https://arxiv.org/abs/2510.12282v1)**  
  Authors: Ying A, Wenzhang Sun, Chang Zeng, Chunfeng Wang, Hao Li, Jianxun Cui  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.12282v1.pdf)  
  Keywords: face, 3d reconstruction, urban scene, dynamic, ar, semantic, gaussian splatting, autonomous driving  
- **[UniGS: Unified Geometry-Aware Gaussian Splatting for Multimodal
  Rendering](https://arxiv.org/abs/2510.12174v1)**  
  Authors: Yusen Xie, Zhenmin Huang, Jianhao Jiao, Dimitrios Kanoulas, Jun Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.12174v1.pdf)  
  Keywords: face, high-fidelity, 3d reconstruction, geometry, ar, semantic, gaussian splatting, 3d gaussian  
- **[VA-GS: Enhancing the Geometric Representation of Gaussian Splatting via
  View Alignment](https://arxiv.org/abs/2510.11473v1)**  
  Authors: Qing Li, Huifang Feng, Xun Gong, Yu-Shen Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.11473v1.pdf)  
  Keywords: face, illumination, geometry, lighting, ar, efficient, gaussian splatting, 3d gaussian  
- **[MaterialRefGS: Reflective Gaussian Splatting with Multi-view Consistent
  Material Inference](https://arxiv.org/abs/2510.11387v1)**  
  Authors: Wenyuan Zhang, Jimin Tang, Weiqi Zhang, Yi Fang, Yu-Shen Liu, Zhizhong Han  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.11387v1.pdf)  
  Keywords: geometry, reflection, ray tracing, ar, gaussian splatting, illumination  
- **[Gesplat: Robust Pose-Free 3D Reconstruction via Geometry-Guided Gaussian
  Splatting](https://arxiv.org/abs/2510.10097v1)**  
  Authors: Jiahui Lu, Haihong Xiao, Xueyan Zhao, Wenxiong Kang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.10097v1.pdf)  
  Keywords: nerf, 3d reconstruction, geometry, ar, gaussian splatting, 3d gaussian, sparse-view  
- **[Visibility-Aware Densification for 3D Gaussian Splatting in Dynamic
  Urban Scenes](https://arxiv.org/abs/2510.09364v1)**  
  Authors: Yikang Zhang, Rui Fan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.09364v1.pdf)  
  Keywords: face, high-fidelity, geometry, urban scene, dynamic, ar, gaussian splatting, 3d gaussian  
- **[Splat the Net: Radiance Fields with Splattable Neural Primitives](https://arxiv.org/abs/2510.08491v1)**  
  Authors: Xilong Zhou, Bao-Huy Nguyen, Loïc Magne, Vladislav Golyanik, Thomas Leimkühler, Christian Theobalt  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.08491v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://vcai.mpi-inf.mpg.de/projects/SplatNet/.)  
  Keywords: ray marching, geometry, ar, efficient, gaussian splatting, 3d gaussian  

### Large Scene

*Showing the latest 50 out of 75 papers*

- **[Leveraging 2D Priors and SDF Guidance for Dynamic Urban Scene Rendering](https://arxiv.org/abs/2510.13381v1)**  
  Authors: Siddharth Tourani, Jayaram Reddy, Akash Kumbar, Satyajit Tourani, Nishant Goyal, Madhava Krishna, N. Dinesh Reddy, Muhammad Haris Khan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.13381v1.pdf)  
  Keywords: segmentation, tracking, deformation, urban scene, motion, dynamic, ar, gaussian splatting, 3d gaussian  
- **[PAGS: Priority-Adaptive Gaussian Splatting for Dynamic Driving Scenes](https://arxiv.org/abs/2510.12282v1)**  
  Authors: Ying A, Wenzhang Sun, Chang Zeng, Chunfeng Wang, Hao Li, Jianxun Cui  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.12282v1.pdf)  
  Keywords: face, 3d reconstruction, urban scene, dynamic, ar, semantic, gaussian splatting, autonomous driving  
- **[Two-Stage Gaussian Splatting Optimization for Outdoor Scene
  Reconstruction](https://arxiv.org/abs/2510.09489v1)**  
  Authors: Deborah Pintani, Ariel Caputo, Noah Lewis, Marc Stamminger, Fabio Pellacini, Andrea Giachetti  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.09489v1.pdf)  
  Keywords: motion, ar, gaussian splatting, illumination, outdoor  
- **[Visibility-Aware Densification for 3D Gaussian Splatting in Dynamic
  Urban Scenes](https://arxiv.org/abs/2510.09364v1)**  
  Authors: Yikang Zhang, Rui Fan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.09364v1.pdf)  
  Keywords: face, high-fidelity, geometry, urban scene, dynamic, ar, gaussian splatting, 3d gaussian  
- **[LOBE-GS: Load-Balanced and Efficient 3D Gaussian Splatting for
  Large-Scale Scene Reconstruction](https://arxiv.org/abs/2510.01767v1)**  
  Authors: Sheng-Hsiang Hung, Ting-Yu Yen, Wei-Fang Sun, Simon See, Shih-Hsuan Hung, Hung-Kuo Chu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.01767v1.pdf)  
  Keywords: high-fidelity, head, lightweight, fast, ar, efficient, gaussian splatting, 3d gaussian, outdoor  
- **[LVT: Large-Scale Scene Reconstruction via Local View Transformers](https://arxiv.org/abs/2509.25001v1)**  
  Authors: Tooba Imtiaz, Lucy Chai, Kathryn Heal, Xuan Luo, Jungyeon Park, Jennifer Dy, John Flynn  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.25001v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://toobaimt.github.io/lvt/.)  
  Keywords: 3d gaussian, large scene, ar  
- **[Aerial-Ground Image Feature Matching via 3D Gaussian Splatting-based
  Intermediate View Rendering](https://arxiv.org/abs/2509.19898v1)**  
  Authors: Jiangxue Yu, Hui Wang, San Jiang, Xing Zhang, Dejin Zhang, Qingquan Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.19898v1.pdf)  
  Keywords: motion, ar, gaussian splatting, 3d gaussian, large scene  
- **[FGGS-LiDAR: Ultra-Fast, GPU-Accelerated Simulation from General 3DGS
  Models to LiDAR](https://arxiv.org/abs/2509.17390v1)**  
  Authors: Junzhe Wu, Yufei Jia, Yiyi Yan, Zhixing Chen, Tiao Tan, Zifan Wang, Guangyu Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.17390v1.pdf)  
  Keywords: high-fidelity, fast, robotics, ar, gaussian splatting, 3d gaussian, outdoor, autonomous driving  
- **[ROSGS: Relightable Outdoor Scenes With Gaussian Splatting](https://arxiv.org/abs/2509.11275v1)**  
  Authors: Lianjun Liao, Chunhui Zhang, Tong Wu, Henglei Lv, Bailin Deng, Lin Gao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.11275v1.pdf)  
  Keywords: nerf, illumination, head, geometry, compact, efficient rendering, lighting, relighting, relightable, ar, efficient, gaussian splatting, 3d gaussian, outdoor  
- **[VIM-GS: Visual-Inertial Monocular Gaussian Splatting via Object-level
  Guidance in Large Scenes](https://arxiv.org/abs/2509.06685v3)**  
  Authors: Shengkai Zhang, Yuhe Liu, Guanjun Wu, Jianhua He, Xinggang Wang, Mozi Chen, Kezhong Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.06685v3.pdf)  
  Keywords: motion, dynamic, ar, gaussian splatting, large scene  

### Model Compression

*Showing the latest 50 out of 413 papers*

- **[STT-GS: Sample-Then-Transmit Edge Gaussian Splatting with Joint Client
  Selection and Power Control](https://arxiv.org/abs/2510.13186v1)**  
  Authors: Zhen Li, Xibin Jin, Guoliang Li, Shuai Wang, Miaowen Wen, Huseyin Arslan, Derrick Wing Kwan Ng, Chengzhong Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.13186v1.pdf)  
  Keywords: efficient, gaussian splatting, ar, head  
- **[Uncertainty Matters in Dynamic Gaussian Splatting for Monocular 4D
  Reconstruction](https://arxiv.org/abs/2510.12768v1)**  
  Authors: Fengzhi Guo, Chih-Chuan Hsu, Sihao Ding, Cheng Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.12768v1.pdf)  
  Keywords: geometry, motion, dynamic, ar, efficient, gaussian splatting, 4d  
- **[GS-Verse: Mesh-based Gaussian Splatting for Physics-aware Interaction in
  Virtual Reality](https://arxiv.org/abs/2510.11878v1)**  
  Authors: Anastasiya Pechko, Piotr Borycki, Joanna Waczyńska, Daniel Barczyk, Agata Szymańska, Sławomir Tadeja, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.11878v1.pdf)  
  Keywords: face, deformation, vr, ar, efficient, gaussian splatting  
- **[Ev4DGS: Novel-view Rendering of Non-Rigid Objects from Monocular Event
  Streams](https://arxiv.org/abs/2510.11717v1)**  
  Authors: Takuya Nakabayashi, Navami Kairanda, Hideo Saito, Vladislav Golyanik  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.11717v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://4dqv.mpi-inf.mpg.de/Ev4DGS/.)  
  Keywords: deformation, ar, efficient, gaussian splatting, 3d gaussian, 4d  
- **[VA-GS: Enhancing the Geometric Representation of Gaussian Splatting via
  View Alignment](https://arxiv.org/abs/2510.11473v1)**  
  Authors: Qing Li, Huifang Feng, Xun Gong, Yu-Shen Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.11473v1.pdf)  
  Keywords: face, illumination, geometry, lighting, ar, efficient, gaussian splatting, 3d gaussian  
- **[Towards Efficient 3D Gaussian Human Avatar Compression: A Prior-Guided
  Framework](https://arxiv.org/abs/2510.10492v1)**  
  Authors: Shanzhi Yin, Bolin Chen, Xinju Wu, Ru-Ling Liao, Jie Chen, Shiqi Wang, Yan Ye  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.10492v1.pdf)  
  Keywords: avatar, human, compact, compression, body, dynamic, ar, efficient, gaussian splatting, 3d gaussian  
- **[Opacity-Gradient Driven Density Control for Compact and Efficient
  Few-Shot 3D Gaussian Splatting](https://arxiv.org/abs/2510.10257v1)**  
  Authors: Abdelrhman Elrawy, Emad A. Mohammed  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.10257v1.pdf)  
  Keywords: nerf, few-shot, compact, lightweight, ar, efficient, gaussian splatting, 3d gaussian  
- **[P-4DGS: Predictive 4D Gaussian Splatting with 90$\times$ Compression](https://arxiv.org/abs/2510.10030v1)**  
  Authors: Henan Wang, Hanxin Zhu, Xinliang Gong, Tianyu He, Xin Li, Zhibo Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.10030v1.pdf)  
  Keywords: compression, compact, fast, dynamic, ar, gaussian splatting, 3d gaussian, real-time rendering, 4d  
- **[VG-Mapping: Variation-Aware 3D Gaussians for Online Semi-static Scene
  Mapping](https://arxiv.org/abs/2510.09962v1)**  
  Authors: Yicheng He, Jingwen Yu, Guangcheng Chen, Hong Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.09962v1.pdf)  
  Keywords: localization, ar, efficient, gaussian splatting, 3d gaussian, mapping  
- **[LTGS: Long-Term Gaussian Scene Chronology From Sparse View Updates](https://arxiv.org/abs/2510.09881v1)**  
  Authors: Minkwan Kim, Seungmin Lee, Junho Kim, Young Min Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.09881v1.pdf)  
  Keywords: face, few-shot, fast, sparse view, ar, efficient, gaussian splatting, sparse-view  

### Quality Enhancement

*Showing the latest 50 out of 172 papers*

- **[UniGS: Unified Geometry-Aware Gaussian Splatting for Multimodal
  Rendering](https://arxiv.org/abs/2510.12174v1)**  
  Authors: Yusen Xie, Zhenmin Huang, Jianhao Jiao, Dimitrios Kanoulas, Jun Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.12174v1.pdf)  
  Keywords: face, high-fidelity, 3d reconstruction, geometry, ar, semantic, gaussian splatting, 3d gaussian  
- **[Phys2Real: Fusing VLM Priors with Interactive Online Adaptation for
  Uncertainty-Aware Sim-to-Real Manipulation](https://arxiv.org/abs/2510.11689v1)**  
  Authors: Maggie Wang, Stephen Tian, Aiden Swann, Ola Shorinwa, Jiajun Wu, Mac Schwager  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.11689v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://phys2real.github.io/)  
  Keywords: high-fidelity, fast, dynamic, ar, gaussian splatting, 3d gaussian  
- **[High-Fidelity Simulated Data Generation for Real-World Zero-Shot Robotic
  Manipulation Learning with Gaussian Splatting](https://arxiv.org/abs/2510.10637v1)**  
  Authors: Haoyu Zhao, Cheng Zeng, Linghao Zhuang, Yaxi Zhao, Shengke Xue, Hao Wang, Xingyue Zhao, Zhongyu Li, Kehan Li, Siteng Huang, Mingxiu Chen, Xin Li, Deli Zhao, Hua Zou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.10637v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, ar, high-fidelity  
- **[CLoD-GS: Continuous Level-of-Detail via 3D Gaussian Splatting](https://arxiv.org/abs/2510.09997v1)**  
  Authors: Zhigang Cheng, Mingchao Sun, Yu Liu, Zengye Ge, Luyang Tang, Mu Xu, Yangyan Li, Peng Pan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.09997v1.pdf)  
  Keywords: head, high-fidelity, dynamic, ar, gaussian splatting, 3d gaussian  
- **[Visibility-Aware Densification for 3D Gaussian Splatting in Dynamic
  Urban Scenes](https://arxiv.org/abs/2510.09364v1)**  
  Authors: Yikang Zhang, Rui Fan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.09364v1.pdf)  
  Keywords: face, high-fidelity, geometry, urban scene, dynamic, ar, gaussian splatting, 3d gaussian  
- **[D$^2$GS: Depth-and-Density Guided Gaussian Splatting for Stable and
  Accurate Sparse-View Reconstruction](https://arxiv.org/abs/2510.08566v1)**  
  Authors: Meixi Song, Xin Lin, Dizhe Zhang, Haodong Li, Xiangtai Li, Bo Du, Lu Qi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.08566v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://insta360-research-team.github.io/DDGS-website/.)  
  Keywords: high-fidelity, sparse view, ar, gaussian splatting, 3d gaussian, sparse-view  
- **[CVD-STORM: Cross-View Video Diffusion with Spatial-Temporal
  Reconstruction Model for Autonomous Driving](https://arxiv.org/abs/2510.07944v2)**  
  Authors: Tianrui Zhang, Yichen Liu, Zilin Guo, Yuxin Guo, Jingcheng Ni, Chenjing Ding, Dan Xu, Lewei Lu, Zehuan Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.07944v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://sensetime-fvg.github.io/CVD-STORM.)  
  Keywords: high-fidelity, understanding, dynamic, ar, gaussian splatting, 4d, autonomous driving  
- **[PrismGS: Physically-Grounded Anti-Aliasing for High-Fidelity Large-Scale
  3D Gaussian Splatting](https://arxiv.org/abs/2510.07830v1)**  
  Authors: Houqiang Zhong, Zhenglong Wu, Sihua Fu, Zihan Zheng, Xin Jin, Xiaoyun Zhang, Li Song, Qiang Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.07830v1.pdf)  
  Keywords: face, high-fidelity, geometry, compact, ar, gaussian splatting, 3d gaussian  
- **[Generating Surface for Text-to-3D using 2D Gaussian Splatting](https://arxiv.org/abs/2510.06967v1)**  
  Authors: Huanning Dong, Fan Li, Ping Kuang, Jianwen Min  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.06967v1.pdf)  
  Keywords: face, gaussian splatting, geometry, high-fidelity  
- **[Optimized Minimal 4D Gaussian Splatting](https://arxiv.org/abs/2510.03857v1)**  
  Authors: Minseo Lee, Byeonghyeon Lee, Lucas Yunkyu Lee, Eunsoo Lee, Sangmin Kim, Seunghyeon Song, Joo Chan Lee, Jong Hwan Ko, Jaesik Park, Eunbyung Park  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.03857v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://minshirley.github.io/OMG4/.)  
  Keywords: face, high-fidelity, head, compression, compact, motion, dynamic, ar, gaussian splatting, real-time rendering, 4d  

### Ray Tracing

- **[MaterialRefGS: Reflective Gaussian Splatting with Multi-view Consistent
  Material Inference](https://arxiv.org/abs/2510.11387v1)**  
  Authors: Wenyuan Zhang, Jimin Tang, Weiqi Zhang, Yi Fang, Yu-Shen Liu, Zhizhong Han  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.11387v1.pdf)  
  Keywords: geometry, reflection, ray tracing, ar, gaussian splatting, illumination  
- **[Splat the Net: Radiance Fields with Splattable Neural Primitives](https://arxiv.org/abs/2510.08491v1)**  
  Authors: Xilong Zhou, Bao-Huy Nguyen, Loïc Magne, Vladislav Golyanik, Thomas Leimkühler, Christian Theobalt  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.08491v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://vcai.mpi-inf.mpg.de/projects/SplatNet/.)  
  Keywords: ray marching, geometry, ar, efficient, gaussian splatting, 3d gaussian  
- **[ComGS: Efficient 3D Object-Scene Composition via Surface Octahedral
  Probes](https://arxiv.org/abs/2510.07729v1)**  
  Authors: Jian Gao, Mengqi Yuan, Yifei Zeng, Chang Zeng, Zhihao Li, Zhenyu Chen, Weichao Qiu, Xiao-Xiao Long, Hao Zhu, Xun Cao, Yao Yao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.07729v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://nju-3dv.github.io/projects/ComGS/.)  
  Keywords: face, light transport, ray tracing, lighting, relightable, ar, efficient, gaussian splatting, real-time rendering, shadow  
- **[Differentiable Light Transport with Gaussian Surfels via Adapted
  Radiosity for Efficient Relighting and Geometry Reconstruction](https://arxiv.org/abs/2509.18497v2)**  
  Authors: Kaiwen Jiang, Jia-Mu Sun, Zilu Li, Dan Wang, Tzu-Mao Li, Ravi Ramamoorthi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.18497v2.pdf)  
  Keywords: light transport, geometry, reflection, lighting, relighting, global illumination, ar, efficient, gaussian splatting, illumination  
- **[Every Camera Effect, Every Time, All at Once: 4D Gaussian Ray Tracing
  for Physics-based Camera Effect Data Generation](https://arxiv.org/abs/2509.10759v1)**  
  Authors: Yi-Ruei Liu, You-Zhe Xie, Yu-Hsiang Hsu, I-Sheng Fang, Yu-Lun Liu, Jun-Cheng Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.10759v1.pdf)  
  Keywords: ray tracing, fast, dynamic, ar, gaussian splatting, 4d  
- **[GOGS: High-Fidelity Geometry and Relighting for Glossy Objects via
  Gaussian Surfels](https://arxiv.org/abs/2508.14563v1)**  
  Authors: Xingyuan Yang, Min Wei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.14563v1.pdf)  
  Keywords: face, nerf, illumination, high-fidelity, geometry, reflection, ray tracing, lighting, relighting, ar, gaussian splatting, 3d gaussian  
- **[GaRe: Relightable 3D Gaussian Splatting for Outdoor Scenes from
  Unconstrained Photo Collections](https://arxiv.org/abs/2507.20512v1)**  
  Authors: Haiyang Bai, Jiaqi Zhu, Songru Jiang, Wei Huang, Tao Lu, Yuanqi Li, Jie Guo, Runze Fu, Yanwen Guo, Lijun Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.20512v1.pdf)  
  Keywords: face, illumination, lighting, relighting, relightable, dynamic, global illumination, ar, gaussian splatting, 3d gaussian, outdoor, shadow  
- **[GSCache: Real-Time Radiance Caching for Volume Path Tracing using 3D
  Gaussian Splatting](https://arxiv.org/abs/2507.19718v2)**  
  Authors: David Bauer, Qi Wu, Hamid Gadirov, Kwan-Liu Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.19718v2.pdf)  
  Keywords: face, path tracing, lighting, dynamic, ar, gaussian splatting, 3d gaussian  
- **[Gaussian Splatting with Discretized SDF for Relightable Assets](https://arxiv.org/abs/2507.15629v1)**  
  Authors: Zuo-Liang Zhu, Jian Yang, Beibei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.15629v1.pdf)  
  Keywords: face, ray marching, geometry, efficient rendering, lighting, relighting, relightable, ar, efficient, gaussian splatting, 3d gaussian  
- **[RaRa Clipper: A Clipper for Gaussian Splatting Based on Ray Tracer and
  Rasterizer](https://arxiv.org/abs/2506.20202v1)**  
  Authors: Da Li, Donggang Jia, Yousef Rajeh, Dominik Engel, Ivan Viola  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.20202v1.pdf)  
  Keywords: high-fidelity, ray tracing, ar, efficient, gaussian splatting, real-time rendering  

### Relighting

*Showing the latest 50 out of 120 papers*

- **[VA-GS: Enhancing the Geometric Representation of Gaussian Splatting via
  View Alignment](https://arxiv.org/abs/2510.11473v1)**  
  Authors: Qing Li, Huifang Feng, Xun Gong, Yu-Shen Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.11473v1.pdf)  
  Keywords: face, illumination, geometry, lighting, ar, efficient, gaussian splatting, 3d gaussian  
- **[MaterialRefGS: Reflective Gaussian Splatting with Multi-view Consistent
  Material Inference](https://arxiv.org/abs/2510.11387v1)**  
  Authors: Wenyuan Zhang, Jimin Tang, Weiqi Zhang, Yi Fang, Yu-Shen Liu, Zhizhong Han  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.11387v1.pdf)  
  Keywords: geometry, reflection, ray tracing, ar, gaussian splatting, illumination  
- **[Two-Stage Gaussian Splatting Optimization for Outdoor Scene
  Reconstruction](https://arxiv.org/abs/2510.09489v1)**  
  Authors: Deborah Pintani, Ariel Caputo, Noah Lewis, Marc Stamminger, Fabio Pellacini, Andrea Giachetti  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.09489v1.pdf)  
  Keywords: motion, ar, gaussian splatting, illumination, outdoor  
- **[ComGS: Efficient 3D Object-Scene Composition via Surface Octahedral
  Probes](https://arxiv.org/abs/2510.07729v1)**  
  Authors: Jian Gao, Mengqi Yuan, Yifei Zeng, Chang Zeng, Zhihao Li, Zhenyu Chen, Weichao Qiu, Xiao-Xiao Long, Hao Zhu, Xun Cao, Yao Yao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.07729v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://nju-3dv.github.io/projects/ComGS/.)  
  Keywords: face, light transport, ray tracing, lighting, relightable, ar, efficient, gaussian splatting, real-time rendering, shadow  
- **[Spec-Gloss Surfels and Normal-Diffuse Priors for Relightable Glossy
  Objects](https://arxiv.org/abs/2510.02069v1)**  
  Authors: Georgios Kouros, Minye Wu, Tinne Tuytelaars  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.02069v1.pdf)  
  Keywords: neural rendering, face, geometry, reflection, lighting, relighting, relightable, dynamic, ar, gaussian splatting, illumination  
- **[MPMAvatar: Learning 3D Gaussian Avatars with Accurate and Robust
  Physics-Based Dynamics](https://arxiv.org/abs/2510.01619v1)**  
  Authors: Changmin Lee, Jihyun Lee, Tae-Kyun Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.01619v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://KAISTChangmin.github.io/MPMAvatar/)  
  Keywords: high-fidelity, deformation, avatar, human, animation, body, dynamic, ar, gaussian splatting, 3d gaussian, shadow  
- **[Universal Beta Splatting](https://arxiv.org/abs/2510.03312v1)**  
  Authors: Rong Liu, Zhongpai Gao, Benjamin Planche, Meida Chen, Van Nguyen Nguyen, Meng Zheng, Anwesa Choudhuri, Terrence Chen, Yue Wang, Andrew Feng, Ziyan Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.03312v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://rongliu-leo.github.io/universal-beta-splatting/.)  
  Keywords: face, light transport, dynamic, ar, gaussian splatting, 3d gaussian, real-time rendering  
- **[Large Material Gaussian Model for Relightable 3D Generation](https://arxiv.org/abs/2509.22112v1)**  
  Authors: Jingrui Ye, Lingting Zhu, Runze Zhang, Zeyu Hu, Yingda Yin, Lanjiong Li, Lequan Yu, Qingmin Liao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.22112v1.pdf)  
  Keywords: lighting, relighting, relightable, dynamic, ar, efficient, gaussian splatting, 3d gaussian  
- **[Dynamic Novel View Synthesis in High Dynamic Range](https://arxiv.org/abs/2509.21853v2)**  
  Authors: Kaixuan Zhang, Zhipeng Xiong, Minxian Li, Mingwu Ren, Jiankang Deng, Xiatian Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.21853v2.pdf)  
  Keywords: lighting, dynamic, ar, gaussian splatting, mapping, 4d  
- **[Seeing Through Reflections: Advancing 3D Scene Reconstruction in
  Mirror-Containing Environments with Gaussian Splatting](https://arxiv.org/abs/2509.18956v1)**  
  Authors: Zijing Guo, Yunyang Zhao, Lin Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.18956v1.pdf)  
  Keywords: face, nerf, 3d reconstruction, geometry, reflection, ar, gaussian splatting, 3d gaussian, mapping  

### SLAM

*Showing the latest 50 out of 151 papers*

- **[Leveraging 2D Priors and SDF Guidance for Dynamic Urban Scene Rendering](https://arxiv.org/abs/2510.13381v1)**  
  Authors: Siddharth Tourani, Jayaram Reddy, Akash Kumbar, Satyajit Tourani, Nishant Goyal, Madhava Krishna, N. Dinesh Reddy, Muhammad Haris Khan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.13381v1.pdf)  
  Keywords: segmentation, tracking, deformation, urban scene, motion, dynamic, ar, gaussian splatting, 3d gaussian  
- **[Color3D: Controllable and Consistent 3D Colorization with Personalized
  Colorizer](https://arxiv.org/abs/2510.10152v1)**  
  Authors: Yecong Wan, Mingwen Shao, Renlong Wu, Wangmeng Zuo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.10152v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://yecongwan.github.io/Color3D/.)  
  Keywords: gaussian splatting, mapping, dynamic, ar  
- **[VG-Mapping: Variation-Aware 3D Gaussians for Online Semi-static Scene
  Mapping](https://arxiv.org/abs/2510.09962v1)**  
  Authors: Yicheng He, Jingwen Yu, Guangcheng Chen, Hong Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.09962v1.pdf)  
  Keywords: localization, ar, efficient, gaussian splatting, 3d gaussian, mapping  
- **[SCas4D: Structural Cascaded Optimization for Boosting Persistent 4D
  Novel View Synthesis](https://arxiv.org/abs/2510.06694v1)**  
  Authors: Jipeng Lyu, Jiahua Dong, Yu-Xiong Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.06694v1.pdf)  
  Keywords: segmentation, tracking, deformation, dynamic, ar, gaussian splatting, 3d gaussian, 4d  
- **[RTGS: Real-Time 3D Gaussian Splatting SLAM via Multi-Level Redundancy
  Reduction](https://arxiv.org/abs/2510.06644v2)**  
  Authors: Leshu Li, Jiayin Qin, Jie Peng, Zishen Wan, Huaizhi Qu, Ye Han, Pingqing Zheng, Hongsen Zhang, Yu Cao, Tianlong Chen, Yang Katie Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.06644v2.pdf)  
  Keywords: head, localization, acceleration, slam, dynamic, ar, gaussian splatting, 3d gaussian, mapping  
- **[Geometry Meets Vision: Revisiting Pretrained Semantics in Distilled
  Fields](https://arxiv.org/abs/2510.03104v1)**  
  Authors: Zhiting Mei, Ola Shorinwa, Anirudha Majumdar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.03104v1.pdf)  
  Keywords: localization, geometry, ar, semantic, gaussian splatting  
- **[GaussianMorphing: Mesh-Guided 3D Gaussians for Semantic-Aware Object
  Morphing](https://arxiv.org/abs/2510.02034v1)**  
  Authors: Mengtian Li, Yunshu Bai, Yimin Chu, Yijun Shen, Zhongmei Li, Weifeng Ge, Zhifeng Xie, Chaofeng Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.02034v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://baiyunshu.github.io/GAUSSIANMORPHING.github.io/)  
  Keywords: high-fidelity, deformation, geometry, ar, semantic, gaussian splatting, 3d gaussian, mapping  
- **[GreenhouseSplat: A Dataset of Photorealistic Greenhouse Simulations for
  Mobile Robotics](https://arxiv.org/abs/2510.01848v1)**  
  Authors: Diram Tabaa, Gianni Di Caro  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.01848v1.pdf)  
  Keywords: localization, gaussian splatting, ar, robotics  
- **[From Fields to Splats: A Cross-Domain Survey of Real-Time Neural Scene
  Representations](https://arxiv.org/abs/2509.23555v1)**  
  Authors: Javed Ahmad, Penggang Gao, Donatien Delehelle, Mennuti Canio, Nikhil Deshpande, Jesús Ortiz, Darwin G. Caldwell, Yonas Teodros Tefera  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.23555v1.pdf)  
  Keywords: neural rendering, nerf, understanding, slam, fast, survey, ar, efficient, gaussian splatting, 3d gaussian  
- **[Learning Unified Representation of 3D Gaussian Splatting](https://arxiv.org/abs/2509.22917v1)**  
  Authors: Yuelin Xin, Yuheng Liu, Xiaohui Xie, Xinke Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.22917v1.pdf)  
  Keywords: 3d reconstruction, ar, efficient, gaussian splatting, 3d gaussian, mapping  

### Scene Understanding

*Showing the latest 50 out of 198 papers*

- **[Leveraging 2D Priors and SDF Guidance for Dynamic Urban Scene Rendering](https://arxiv.org/abs/2510.13381v1)**  
  Authors: Siddharth Tourani, Jayaram Reddy, Akash Kumbar, Satyajit Tourani, Nishant Goyal, Madhava Krishna, N. Dinesh Reddy, Muhammad Haris Khan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.13381v1.pdf)  
  Keywords: segmentation, tracking, deformation, urban scene, motion, dynamic, ar, gaussian splatting, 3d gaussian  
- **[PAGS: Priority-Adaptive Gaussian Splatting for Dynamic Driving Scenes](https://arxiv.org/abs/2510.12282v1)**  
  Authors: Ying A, Wenzhang Sun, Chang Zeng, Chunfeng Wang, Hao Li, Jianxun Cui  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.12282v1.pdf)  
  Keywords: face, 3d reconstruction, urban scene, dynamic, ar, semantic, gaussian splatting, autonomous driving  
- **[UniGS: Unified Geometry-Aware Gaussian Splatting for Multimodal
  Rendering](https://arxiv.org/abs/2510.12174v1)**  
  Authors: Yusen Xie, Zhenmin Huang, Jianhao Jiao, Dimitrios Kanoulas, Jun Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.12174v1.pdf)  
  Keywords: face, high-fidelity, 3d reconstruction, geometry, ar, semantic, gaussian splatting, 3d gaussian  
- **[Vision Language Models: A Survey of 26K Papers](https://arxiv.org/abs/2510.09586v1)**  
  Authors: Fengming Lin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.09586v1.pdf)  
  Keywords: nerf, understanding, human, lightweight, survey, ar, efficient, gaussian splatting  
- **[Efficient Label Refinement for Face Parsing Under Extreme Poses Using 3D
  Gaussian Splatting](https://arxiv.org/abs/2510.08096v1)**  
  Authors: Ankit Gahlawat, Anirban Mukherjee, Dinesh Babu Jayagopi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.08096v1.pdf)  
  Keywords: face, segmentation, head, geometry, human, ar, efficient, gaussian splatting, 3d gaussian  
- **[CVD-STORM: Cross-View Video Diffusion with Spatial-Temporal
  Reconstruction Model for Autonomous Driving](https://arxiv.org/abs/2510.07944v2)**  
  Authors: Tianrui Zhang, Yichen Liu, Zilin Guo, Yuxin Guo, Jingcheng Ni, Chenjing Ding, Dan Xu, Lewei Lu, Zehuan Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.07944v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://sensetime-fvg.github.io/CVD-STORM.)  
  Keywords: high-fidelity, understanding, dynamic, ar, gaussian splatting, 4d, autonomous driving  
- **[SCas4D: Structural Cascaded Optimization for Boosting Persistent 4D
  Novel View Synthesis](https://arxiv.org/abs/2510.06694v1)**  
  Authors: Jipeng Lyu, Jiahua Dong, Yu-Xiong Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.06694v1.pdf)  
  Keywords: segmentation, tracking, deformation, dynamic, ar, gaussian splatting, 3d gaussian, 4d  
- **[Geometry Meets Vision: Revisiting Pretrained Semantics in Distilled
  Fields](https://arxiv.org/abs/2510.03104v1)**  
  Authors: Zhiting Mei, Ola Shorinwa, Anirudha Majumdar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.03104v1.pdf)  
  Keywords: localization, geometry, ar, semantic, gaussian splatting  
- **[GaussianMorphing: Mesh-Guided 3D Gaussians for Semantic-Aware Object
  Morphing](https://arxiv.org/abs/2510.02034v1)**  
  Authors: Mengtian Li, Yunshu Bai, Yimin Chu, Yijun Shen, Zhongmei Li, Weifeng Ge, Zhifeng Xie, Chaofeng Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.02034v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://baiyunshu.github.io/GAUSSIANMORPHING.github.io/)  
  Keywords: high-fidelity, deformation, geometry, ar, semantic, gaussian splatting, 3d gaussian, mapping  
- **[4DGS-Craft: Consistent and Interactive 4D Gaussian Splatting Editing](https://arxiv.org/abs/2510.01991v1)**  
  Authors: Lei Liu, Can Wang, Zhenghao Chen, Dong Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.01991v1.pdf)  
  Keywords: face, understanding, geometry, ar, gaussian splatting, 4d  



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