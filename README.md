# Awesome Gaussian Splatting [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of latest research papers, projects and resources related to Gaussian Splatting. Content is automatically updated daily.

> Last Update: 2025-10-16 00:51:24

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

- [3DGS Surveys](#3dgs-surveys) (9 papers) - Survey papers and benchmarks about 3D Gaussian Splatting
- [Acceleration](#acceleration) (112 papers) - Papers about speeding up rendering or training
- [Applications](#applications) (475 papers) - Papers about specific applications
- [Avatar Generation](#avatar-generation) (168 papers) - Papers about human avatar generation
- [Dynamic Scene](#dynamic-scene) (193 papers) - Papers about dynamic scene reconstruction and rendering
- [Few-shot](#few-shot) (41 papers) - Papers about few-shot or sparse view reconstruction
- [Geometry Reconstruction](#geometry-reconstruction) (167 papers) - Papers about 3D geometry reconstruction
- [Large Scene](#large-scene) (39 papers) - Papers about large-scale scene reconstruction
- [Model Compression](#model-compression) (195 papers) - Papers about model compression and optimization
- [Quality Enhancement](#quality-enhancement) (91 papers) - Papers focusing on improving rendering quality
- [Ray Tracing](#ray-tracing) (10 papers) - Papers about ray tracing and ray casting in Gaussian Splatting
- [Relighting](#relighting) (59 papers) - Papers about relighting and illumination effects in Gaussian Splatting
- [SLAM](#slam) (70 papers) - Papers about SLAM using Gaussian Splatting
- [Scene Understanding](#scene-understanding) (106 papers) - Papers about scene understanding and semantic analysis



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
  Keywords: lightweight, human, understanding, ar, nerf, survey, gaussian splatting, efficient  
- **[From Fields to Splats: A Cross-Domain Survey of Real-Time Neural Scene
  Representations](https://arxiv.org/abs/2509.23555v1)**  
  Authors: Javed Ahmad, Penggang Gao, Donatien Delehelle, Mennuti Canio, Nikhil Deshpande, Jesús Ortiz, Darwin G. Caldwell, Yonas Teodros Tefera  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.23555v1.pdf)  
  Keywords: neural rendering, 3d gaussian, understanding, fast, nerf, slam, ar, survey, gaussian splatting, efficient  
- **[A Survey on 3D Gaussian Splatting Applications: Segmentation, Editing,
  and Generation](https://arxiv.org/abs/2508.09977v2)**  
  Authors: Shuting He, Peilin Ji, Yitong Yang, Changshuo Wang, Jiayi Ji, Yinglin Wang, Henghui Ding  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.09977v2.pdf)  
  Keywords: semantic, 3d gaussian, segmentation, compact, understanding, ar, nerf, lighting, survey, high-fidelity, gaussian splatting  
- **[A Study of the Framework and Real-World Applications of Language
  Embedding for 3D Scene Understanding](https://arxiv.org/abs/2508.05064v2)**  
  Authors: Mahmoud Chick Zaouali, Todd Charter, Yehor Karpichev, Brandon Haworth, Homayoun Najjaran  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.05064v2.pdf)  
  Keywords: semantic, 3d gaussian, understanding, ar, nerf, robotics, survey, gaussian splatting, efficient  
- **[Radiance Fields in XR: A Survey on How Radiance Fields are Envisioned
  and Addressed for XR Research](https://arxiv.org/abs/2508.04326v2)**  
  Authors: Ke Li, Mana Masuda, Susanne Schmidt, Shohei Mori  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.04326v2.pdf)  
  Keywords: 3d gaussian, human, ar, nerf, robotics, survey, gaussian splatting  
- **[Sparse-View 3D Reconstruction: Recent Advances and Open Challenges](https://arxiv.org/abs/2507.16406v1)**  
  Authors: Tanveer Younis, Zhanglin Cheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.16406v1.pdf)  
  Keywords: vr, sparse-view, motion, 3d gaussian, ar, nerf, robotics, survey, gaussian splatting, geometry, 3d reconstruction  
- **[Advances in Feed-Forward 3D Reconstruction and View Synthesis: A Survey](https://arxiv.org/abs/2507.14501v3)**  
  Authors: Jiahui Zhang, Yuelei Li, Anpei Chen, Muyu Xu, Kunhao Liu, Jianyuan Wang, Xiao-Xiao Long, Hanxue Liang, Zexiang Xu, Hao Su, Christian Theobalt, Christian Rupprecht, Andrea Vedaldi, Kaichen Zhou, Paul Pu Liang, Shijian Lu, Fangneng Zhan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.14501v3.pdf)  
  Keywords: vr, 3d gaussian, human, ar, fast, nerf, slam, robotics, lighting, survey, gaussian splatting, dynamic, 3d reconstruction  
- **[3D Gaussian Splatting for Fine-Detailed Surface Reconstruction in
  Large-Scale Scene](https://arxiv.org/abs/2506.17636v1)**  
  Authors: Shihan Chen, Zhaojin Li, Zeyu Chen, Qingsong Yan, Gaoyang Shen, Ran Duan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.17636v1.pdf)  
  Keywords: autonomous driving, 3d gaussian, ar, nerf, efficient, survey, high-fidelity, gaussian splatting, outdoor, face, dynamic  
- **[R3eVision: A Survey on Robust Rendering, Restoration, and Enhancement
  for 3D Low-Level Vision](https://arxiv.org/abs/2506.16262v2)**  
  Authors: Weeyoung Kwon, Jeahun Sung, Minkyu Jeon, Chanho Eom, Jihyong Oh  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.16262v2.pdf)  
  Keywords: vr, autonomous driving, neural rendering, 3d gaussian, ar, nerf, robotics, survey, high-fidelity, gaussian splatting, 3d reconstruction  

### Acceleration

*Showing the latest 50 out of 112 papers*

- **[Phys2Real: Fusing VLM Priors with Interactive Online Adaptation for
  Uncertainty-Aware Sim-to-Real Manipulation](https://arxiv.org/abs/2510.11689v1)**  
  Authors: Maggie Wang, Stephen Tian, Aiden Swann, Ola Shorinwa, Jiajun Wu, Mac Schwager  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.11689v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://phys2real.github.io/)  
  Keywords: 3d gaussian, ar, fast, high-fidelity, gaussian splatting, dynamic  
- **[P-4DGS: Predictive 4D Gaussian Splatting with 90$\times$ Compression](https://arxiv.org/abs/2510.10030v1)**  
  Authors: Henan Wang, Hanxin Zhu, Xinliang Gong, Tianyu He, Xin Li, Zhibo Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.10030v1.pdf)  
  Keywords: 3d gaussian, compact, 4d, fast, ar, compression, gaussian splatting, dynamic, real-time rendering  
- **[LTGS: Long-Term Gaussian Scene Chronology From Sparse View Updates](https://arxiv.org/abs/2510.09881v1)**  
  Authors: Minkwan Kim, Seungmin Lee, Junho Kim, Young Min Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.09881v1.pdf)  
  Keywords: sparse-view, ar, fast, gaussian splatting, efficient, face, sparse view, few-shot  
- **[FLOWING: Implicit Neural Flows for Structure-Preserving Morphing](https://arxiv.org/abs/2510.09537v1)**  
  Authors: Arthur Bizzi, Matias Grynberg, Vitor Matias, Daniel Perazzo, João Paulo Lima, Luiz Velho, Nuno Gonçalves, João Pereira, Guilherme Schardong, Tiago Novello  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.09537v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](http://schardong.github.io/flowing.)  
  Keywords: ar, fast, face, gaussian splatting, deformation  
- **[ComGS: Efficient 3D Object-Scene Composition via Surface Octahedral
  Probes](https://arxiv.org/abs/2510.07729v1)**  
  Authors: Jian Gao, Mengqi Yuan, Yifei Zeng, Chang Zeng, Zhihao Li, Zhenyu Chen, Weichao Qiu, Xiao-Xiao Long, Hao Zhu, Xun Cao, Yao Yao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.07729v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://nju-3dv.github.io/projects/ComGS/.)  
  Keywords: relightable, ray tracing, light transport, ar, lighting, shadow, gaussian splatting, efficient, face, real-time rendering  
- **[Capture and Interact: Rapid 3D Object Acquisition and Rendering with
  Gaussian Splatting in Unity](https://arxiv.org/abs/2510.06802v1)**  
  Authors: Islomjon Shukhratov, Sergey Gorinsky  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.06802v1.pdf)  
  Keywords: 3d gaussian, ar, gaussian splatting, 3d reconstruction, real-time rendering  
- **[RTGS: Real-Time 3D Gaussian Splatting SLAM via Multi-Level Redundancy
  Reduction](https://arxiv.org/abs/2510.06644v2)**  
  Authors: Leshu Li, Jiayin Qin, Jie Peng, Zishen Wan, Huaizhi Qu, Ye Han, Pingqing Zheng, Hongsen Zhang, Yu Cao, Tianlong Chen, Yang Katie Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.06644v2.pdf)  
  Keywords: 3d gaussian, head, ar, slam, mapping, acceleration, gaussian splatting, dynamic, localization  
- **[ArchitectHead: Continuous Level of Detail Control for 3D Gaussian Head
  Avatars](https://arxiv.org/abs/2510.05488v1)**  
  Authors: Peizhi Yan, Rabab Ward, Qiang Tang, Shan Du  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.05488v1.pdf)  
  Keywords: lightweight, 3d gaussian, head, avatar, ar, gaussian splatting, efficient, dynamic, real-time rendering  
- **[Optimized Minimal 4D Gaussian Splatting](https://arxiv.org/abs/2510.03857v1)**  
  Authors: Minseo Lee, Byeonghyeon Lee, Lucas Yunkyu Lee, Eunsoo Lee, Sangmin Kim, Seunghyeon Song, Joo Chan Lee, Jong Hwan Ko, Jaesik Park, Eunbyung Park  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.03857v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://minshirley.github.io/OMG4/.)  
  Keywords: motion, head, compact, 4d, ar, high-fidelity, compression, gaussian splatting, face, dynamic, real-time rendering  
- **[FSFSplatter: Build Surface and Novel Views with Sparse-Views within 2min](https://arxiv.org/abs/2510.02691v2)**  
  Authors: Yibin Zhao, Yihan Pan, Jun Nan, Liwei Chen, Jianjun Yi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.02691v2.pdf)  
  Keywords: sparse-view, head, ar, fast, gaussian splatting, face, geometry  

### Applications

*Showing the latest 50 out of 475 papers*

- **[Uncertainty Matters in Dynamic Gaussian Splatting for Monocular 4D
  Reconstruction](https://arxiv.org/abs/2510.12768v1)**  
  Authors: Fengzhi Guo, Chih-Chuan Hsu, Sihao Ding, Cheng Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.12768v1.pdf)  
  Keywords: motion, 4d, ar, gaussian splatting, efficient, dynamic, geometry  
- **[BSGS: Bi-stage 3D Gaussian Splatting for Camera Motion Deblurring](https://arxiv.org/abs/2510.12493v1)**  
  Authors: An Zhao, Piaopiao Yu, Zhe Zhu, Mingqiang Wei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.12493v1.pdf)  
  Keywords: motion, 3d gaussian, ar, gaussian splatting, dynamic  
- **[Hybrid Gaussian Splatting for Novel Urban View Synthesis](https://arxiv.org/abs/2510.12308v1)**  
  Authors: Mohamed Omran, Farhad Zanjani, Davide Abati, Jens Petersen, Amirhossein Habibian  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.12308v1.pdf)  
  Keywords: gaussian splatting, ar, 3d reconstruction  
- **[PAGS: Priority-Adaptive Gaussian Splatting for Dynamic Driving Scenes](https://arxiv.org/abs/2510.12282v1)**  
  Authors: Ying A, Wenzhang Sun, Chang Zeng, Chunfeng Wang, Hao Li, Jianxun Cui  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.12282v1.pdf)  
  Keywords: semantic, autonomous driving, ar, gaussian splatting, face, dynamic, 3d reconstruction, urban scene  
- **[UniGS: Unified Geometry-Aware Gaussian Splatting for Multimodal
  Rendering](https://arxiv.org/abs/2510.12174v1)**  
  Authors: Yusen Xie, Zhenmin Huang, Jianhao Jiao, Dimitrios Kanoulas, Jun Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.12174v1.pdf)  
  Keywords: semantic, 3d gaussian, ar, high-fidelity, gaussian splatting, face, geometry, 3d reconstruction  
- **[GS-Verse: Mesh-based Gaussian Splatting for Physics-aware Interaction in
  Virtual Reality](https://arxiv.org/abs/2510.11878v1)**  
  Authors: Anastasiya Pechko, Piotr Borycki, Joanna Waczyńska, Daniel Barczyk, Agata Szymańska, Sławomir Tadeja, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.11878v1.pdf)  
  Keywords: vr, ar, face, gaussian splatting, efficient, deformation  
- **[Ev4DGS: Novel-view Rendering of Non-Rigid Objects from Monocular Event
  Streams](https://arxiv.org/abs/2510.11717v1)**  
  Authors: Takuya Nakabayashi, Navami Kairanda, Hideo Saito, Vladislav Golyanik  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.11717v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://4dqv.mpi-inf.mpg.de/Ev4DGS/.)  
  Keywords: 3d gaussian, 4d, ar, gaussian splatting, efficient, deformation  
- **[Phys2Real: Fusing VLM Priors with Interactive Online Adaptation for
  Uncertainty-Aware Sim-to-Real Manipulation](https://arxiv.org/abs/2510.11689v1)**  
  Authors: Maggie Wang, Stephen Tian, Aiden Swann, Ola Shorinwa, Jiajun Wu, Mac Schwager  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.11689v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://phys2real.github.io/)  
  Keywords: 3d gaussian, ar, fast, high-fidelity, gaussian splatting, dynamic  
- **[VA-GS: Enhancing the Geometric Representation of Gaussian Splatting via
  View Alignment](https://arxiv.org/abs/2510.11473v1)**  
  Authors: Qing Li, Huifang Feng, Xun Gong, Yu-Shen Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.11473v1.pdf)  
  Keywords: 3d gaussian, ar, lighting, illumination, gaussian splatting, efficient, face, geometry  
- **[MaterialRefGS: Reflective Gaussian Splatting with Multi-view Consistent
  Material Inference](https://arxiv.org/abs/2510.11387v1)**  
  Authors: Wenyuan Zhang, Jimin Tang, Weiqi Zhang, Yi Fang, Yu-Shen Liu, Zhizhong Han  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.11387v1.pdf)  
  Keywords: ray tracing, ar, reflection, illumination, gaussian splatting, geometry  

### Avatar Generation

*Showing the latest 50 out of 168 papers*

- **[PAGS: Priority-Adaptive Gaussian Splatting for Dynamic Driving Scenes](https://arxiv.org/abs/2510.12282v1)**  
  Authors: Ying A, Wenzhang Sun, Chang Zeng, Chunfeng Wang, Hao Li, Jianxun Cui  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.12282v1.pdf)  
  Keywords: semantic, autonomous driving, ar, gaussian splatting, face, dynamic, 3d reconstruction, urban scene  
- **[UniGS: Unified Geometry-Aware Gaussian Splatting for Multimodal
  Rendering](https://arxiv.org/abs/2510.12174v1)**  
  Authors: Yusen Xie, Zhenmin Huang, Jianhao Jiao, Dimitrios Kanoulas, Jun Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.12174v1.pdf)  
  Keywords: semantic, 3d gaussian, ar, high-fidelity, gaussian splatting, face, geometry, 3d reconstruction  
- **[GS-Verse: Mesh-based Gaussian Splatting for Physics-aware Interaction in
  Virtual Reality](https://arxiv.org/abs/2510.11878v1)**  
  Authors: Anastasiya Pechko, Piotr Borycki, Joanna Waczyńska, Daniel Barczyk, Agata Szymańska, Sławomir Tadeja, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.11878v1.pdf)  
  Keywords: vr, ar, face, gaussian splatting, efficient, deformation  
- **[VA-GS: Enhancing the Geometric Representation of Gaussian Splatting via
  View Alignment](https://arxiv.org/abs/2510.11473v1)**  
  Authors: Qing Li, Huifang Feng, Xun Gong, Yu-Shen Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.11473v1.pdf)  
  Keywords: 3d gaussian, ar, lighting, illumination, gaussian splatting, efficient, face, geometry  
- **[Towards Efficient 3D Gaussian Human Avatar Compression: A Prior-Guided
  Framework](https://arxiv.org/abs/2510.10492v1)**  
  Authors: Shanzhi Yin, Bolin Chen, Xinju Wu, Ru-Ling Liao, Jie Chen, Shiqi Wang, Yan Ye  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.10492v1.pdf)  
  Keywords: 3d gaussian, avatar, compact, human, ar, body, compression, gaussian splatting, efficient, dynamic  
- **[CLoD-GS: Continuous Level-of-Detail via 3D Gaussian Splatting](https://arxiv.org/abs/2510.09997v1)**  
  Authors: Zhigang Cheng, Mingchao Sun, Yu Liu, Zengye Ge, Luyang Tang, Mu Xu, Yangyan Li, Peng Pan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.09997v1.pdf)  
  Keywords: 3d gaussian, head, ar, high-fidelity, gaussian splatting, dynamic  
- **[LTGS: Long-Term Gaussian Scene Chronology From Sparse View Updates](https://arxiv.org/abs/2510.09881v1)**  
  Authors: Minkwan Kim, Seungmin Lee, Junho Kim, Young Min Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.09881v1.pdf)  
  Keywords: sparse-view, ar, fast, gaussian splatting, efficient, face, sparse view, few-shot  
- **[Vision Language Models: A Survey of 26K Papers](https://arxiv.org/abs/2510.09586v1)**  
  Authors: Fengming Lin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.09586v1.pdf)  
  Keywords: lightweight, human, understanding, ar, nerf, survey, gaussian splatting, efficient  
- **[FLOWING: Implicit Neural Flows for Structure-Preserving Morphing](https://arxiv.org/abs/2510.09537v1)**  
  Authors: Arthur Bizzi, Matias Grynberg, Vitor Matias, Daniel Perazzo, João Paulo Lima, Luiz Velho, Nuno Gonçalves, João Pereira, Guilherme Schardong, Tiago Novello  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.09537v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](http://schardong.github.io/flowing.)  
  Keywords: ar, fast, face, gaussian splatting, deformation  
- **[Visibility-Aware Densification for 3D Gaussian Splatting in Dynamic
  Urban Scenes](https://arxiv.org/abs/2510.09364v1)**  
  Authors: Yikang Zhang, Rui Fan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.09364v1.pdf)  
  Keywords: 3d gaussian, ar, high-fidelity, gaussian splatting, face, dynamic, geometry, urban scene  

### Dynamic Scene

*Showing the latest 50 out of 193 papers*

- **[Uncertainty Matters in Dynamic Gaussian Splatting for Monocular 4D
  Reconstruction](https://arxiv.org/abs/2510.12768v1)**  
  Authors: Fengzhi Guo, Chih-Chuan Hsu, Sihao Ding, Cheng Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.12768v1.pdf)  
  Keywords: motion, 4d, ar, gaussian splatting, efficient, dynamic, geometry  
- **[BSGS: Bi-stage 3D Gaussian Splatting for Camera Motion Deblurring](https://arxiv.org/abs/2510.12493v1)**  
  Authors: An Zhao, Piaopiao Yu, Zhe Zhu, Mingqiang Wei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.12493v1.pdf)  
  Keywords: motion, 3d gaussian, ar, gaussian splatting, dynamic  
- **[PAGS: Priority-Adaptive Gaussian Splatting for Dynamic Driving Scenes](https://arxiv.org/abs/2510.12282v1)**  
  Authors: Ying A, Wenzhang Sun, Chang Zeng, Chunfeng Wang, Hao Li, Jianxun Cui  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.12282v1.pdf)  
  Keywords: semantic, autonomous driving, ar, gaussian splatting, face, dynamic, 3d reconstruction, urban scene  
- **[GS-Verse: Mesh-based Gaussian Splatting for Physics-aware Interaction in
  Virtual Reality](https://arxiv.org/abs/2510.11878v1)**  
  Authors: Anastasiya Pechko, Piotr Borycki, Joanna Waczyńska, Daniel Barczyk, Agata Szymańska, Sławomir Tadeja, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.11878v1.pdf)  
  Keywords: vr, ar, face, gaussian splatting, efficient, deformation  
- **[Ev4DGS: Novel-view Rendering of Non-Rigid Objects from Monocular Event
  Streams](https://arxiv.org/abs/2510.11717v1)**  
  Authors: Takuya Nakabayashi, Navami Kairanda, Hideo Saito, Vladislav Golyanik  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.11717v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://4dqv.mpi-inf.mpg.de/Ev4DGS/.)  
  Keywords: 3d gaussian, 4d, ar, gaussian splatting, efficient, deformation  
- **[Phys2Real: Fusing VLM Priors with Interactive Online Adaptation for
  Uncertainty-Aware Sim-to-Real Manipulation](https://arxiv.org/abs/2510.11689v1)**  
  Authors: Maggie Wang, Stephen Tian, Aiden Swann, Ola Shorinwa, Jiajun Wu, Mac Schwager  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.11689v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://phys2real.github.io/)  
  Keywords: 3d gaussian, ar, fast, high-fidelity, gaussian splatting, dynamic  
- **[Dynamic Gaussian Splatting from Defocused and Motion-blurred Monocular
  Videos](https://arxiv.org/abs/2510.10691v1)**  
  Authors: Xuankai Zhang, Junjin Xiao, Qing Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.10691v1.pdf)  
  Keywords: gaussian splatting, ar, dynamic, motion  
- **[Towards Efficient 3D Gaussian Human Avatar Compression: A Prior-Guided
  Framework](https://arxiv.org/abs/2510.10492v1)**  
  Authors: Shanzhi Yin, Bolin Chen, Xinju Wu, Ru-Ling Liao, Jie Chen, Shiqi Wang, Yan Ye  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.10492v1.pdf)  
  Keywords: 3d gaussian, avatar, compact, human, ar, body, compression, gaussian splatting, efficient, dynamic  
- **[Color3D: Controllable and Consistent 3D Colorization with Personalized
  Colorizer](https://arxiv.org/abs/2510.10152v1)**  
  Authors: Yecong Wan, Mingwen Shao, Renlong Wu, Wangmeng Zuo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.10152v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://yecongwan.github.io/Color3D/.)  
  Keywords: gaussian splatting, ar, dynamic, mapping  
- **[P-4DGS: Predictive 4D Gaussian Splatting with 90$\times$ Compression](https://arxiv.org/abs/2510.10030v1)**  
  Authors: Henan Wang, Hanxin Zhu, Xinliang Gong, Tianyu He, Xin Li, Zhibo Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.10030v1.pdf)  
  Keywords: 3d gaussian, compact, 4d, fast, ar, compression, gaussian splatting, dynamic, real-time rendering  

### Few-shot

- **[Opacity-Gradient Driven Density Control for Compact and Efficient
  Few-Shot 3D Gaussian Splatting](https://arxiv.org/abs/2510.10257v1)**  
  Authors: Abdelrhman Elrawy, Emad A. Mohammed  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.10257v1.pdf)  
  Keywords: lightweight, 3d gaussian, compact, ar, nerf, gaussian splatting, efficient, few-shot  
- **[Gesplat: Robust Pose-Free 3D Reconstruction via Geometry-Guided Gaussian
  Splatting](https://arxiv.org/abs/2510.10097v1)**  
  Authors: Jiahui Lu, Haihong Xiao, Xueyan Zhao, Wenxiong Kang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.10097v1.pdf)  
  Keywords: sparse-view, 3d gaussian, ar, nerf, gaussian splatting, geometry, 3d reconstruction  
- **[LTGS: Long-Term Gaussian Scene Chronology From Sparse View Updates](https://arxiv.org/abs/2510.09881v1)**  
  Authors: Minkwan Kim, Seungmin Lee, Junho Kim, Young Min Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.09881v1.pdf)  
  Keywords: sparse-view, ar, fast, gaussian splatting, efficient, face, sparse view, few-shot  
- **[D$^2$GS: Depth-and-Density Guided Gaussian Splatting for Stable and
  Accurate Sparse-View Reconstruction](https://arxiv.org/abs/2510.08566v1)**  
  Authors: Meixi Song, Xin Lin, Dizhe Zhang, Haodong Li, Xiangtai Li, Bo Du, Lu Qi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.08566v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://insta360-research-team.github.io/DDGS-website/.)  
  Keywords: sparse-view, 3d gaussian, ar, high-fidelity, gaussian splatting, sparse view  
- **[FSFSplatter: Build Surface and Novel Views with Sparse-Views within 2min](https://arxiv.org/abs/2510.02691v2)**  
  Authors: Yibin Zhao, Yihan Pan, Jun Nan, Liwei Chen, Jianjun Yi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.02691v2.pdf)  
  Keywords: sparse-view, head, ar, fast, gaussian splatting, face, geometry  
- **[HART: Human Aligned Reconstruction Transformer](https://arxiv.org/abs/2509.26621v1)**  
  Authors: Xiyi Chen, Shaofei Wang, Marko Mihajlovic, Taewon Kang, Sergey Prokudin, Ming Lin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.26621v1.pdf)  
  Keywords: sparse-view, ar, body, human, geometry  
- **[GaussianLens: Localized High-Resolution Reconstruction via On-Demand
  Gaussian Densification](https://arxiv.org/abs/2509.25603v1)**  
  Authors: Yijia Weng, Zhicheng Wang, Songyou Peng, Saining Xie, Howard Zhou, Leonidas J. Guibas  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.25603v1.pdf)  
  Keywords: 3d gaussian, human, ar, fast, gaussian splatting, sparse view  
- **[HBSplat: Robust Sparse-View Gaussian Reconstruction with Hybrid-Loss
  Guided Depth and Bidirectional Warping](https://arxiv.org/abs/2509.24893v3)**  
  Authors: Yu Ma, Guoliang Wei, Haihong Xiao, Yue Cheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.24893v3.pdf)  
  Keywords: sparse-view, 3d gaussian, ar, high-fidelity, gaussian splatting, sparse view, 3d reconstruction  
- **[OracleGS: Grounding Generative Priors for Sparse-View Gaussian Splatting](https://arxiv.org/abs/2509.23258v2)**  
  Authors: Atakan Topaloglu, Kunyi Li, Michael Niemeyer, Nassir Navab, A. Murat Tekalp, Federico Tombari  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.23258v2.pdf)  
  Keywords: sparse-view, 3d gaussian, ar, nerf, gaussian splatting, sparse view  
- **[WaveletGaussian: Wavelet-domain Diffusion for Sparse-view 3D Gaussian
  Object Reconstruction](https://arxiv.org/abs/2509.19073v1)**  
  Authors: Hung Nguyen, Runfa Li, An Le, Truong Nguyen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.19073v1.pdf)  
  Keywords: lightweight, sparse-view, 3d gaussian, ar, nerf, gaussian splatting, efficient  

### Geometry Reconstruction

*Showing the latest 50 out of 167 papers*

- **[Uncertainty Matters in Dynamic Gaussian Splatting for Monocular 4D
  Reconstruction](https://arxiv.org/abs/2510.12768v1)**  
  Authors: Fengzhi Guo, Chih-Chuan Hsu, Sihao Ding, Cheng Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.12768v1.pdf)  
  Keywords: motion, 4d, ar, gaussian splatting, efficient, dynamic, geometry  
- **[Hybrid Gaussian Splatting for Novel Urban View Synthesis](https://arxiv.org/abs/2510.12308v1)**  
  Authors: Mohamed Omran, Farhad Zanjani, Davide Abati, Jens Petersen, Amirhossein Habibian  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.12308v1.pdf)  
  Keywords: gaussian splatting, ar, 3d reconstruction  
- **[PAGS: Priority-Adaptive Gaussian Splatting for Dynamic Driving Scenes](https://arxiv.org/abs/2510.12282v1)**  
  Authors: Ying A, Wenzhang Sun, Chang Zeng, Chunfeng Wang, Hao Li, Jianxun Cui  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.12282v1.pdf)  
  Keywords: semantic, autonomous driving, ar, gaussian splatting, face, dynamic, 3d reconstruction, urban scene  
- **[UniGS: Unified Geometry-Aware Gaussian Splatting for Multimodal
  Rendering](https://arxiv.org/abs/2510.12174v1)**  
  Authors: Yusen Xie, Zhenmin Huang, Jianhao Jiao, Dimitrios Kanoulas, Jun Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.12174v1.pdf)  
  Keywords: semantic, 3d gaussian, ar, high-fidelity, gaussian splatting, face, geometry, 3d reconstruction  
- **[VA-GS: Enhancing the Geometric Representation of Gaussian Splatting via
  View Alignment](https://arxiv.org/abs/2510.11473v1)**  
  Authors: Qing Li, Huifang Feng, Xun Gong, Yu-Shen Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.11473v1.pdf)  
  Keywords: 3d gaussian, ar, lighting, illumination, gaussian splatting, efficient, face, geometry  
- **[MaterialRefGS: Reflective Gaussian Splatting with Multi-view Consistent
  Material Inference](https://arxiv.org/abs/2510.11387v1)**  
  Authors: Wenyuan Zhang, Jimin Tang, Weiqi Zhang, Yi Fang, Yu-Shen Liu, Zhizhong Han  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.11387v1.pdf)  
  Keywords: ray tracing, ar, reflection, illumination, gaussian splatting, geometry  
- **[Gesplat: Robust Pose-Free 3D Reconstruction via Geometry-Guided Gaussian
  Splatting](https://arxiv.org/abs/2510.10097v1)**  
  Authors: Jiahui Lu, Haihong Xiao, Xueyan Zhao, Wenxiong Kang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.10097v1.pdf)  
  Keywords: sparse-view, 3d gaussian, ar, nerf, gaussian splatting, geometry, 3d reconstruction  
- **[Visibility-Aware Densification for 3D Gaussian Splatting in Dynamic
  Urban Scenes](https://arxiv.org/abs/2510.09364v1)**  
  Authors: Yikang Zhang, Rui Fan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.09364v1.pdf)  
  Keywords: 3d gaussian, ar, high-fidelity, gaussian splatting, face, dynamic, geometry, urban scene  
- **[Splat the Net: Radiance Fields with Splattable Neural Primitives](https://arxiv.org/abs/2510.08491v1)**  
  Authors: Xilong Zhou, Bao-Huy Nguyen, Loïc Magne, Vladislav Golyanik, Thomas Leimkühler, Christian Theobalt  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.08491v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://vcai.mpi-inf.mpg.de/projects/SplatNet/.)  
  Keywords: 3d gaussian, ar, gaussian splatting, efficient, geometry, ray marching  
- **[Efficient Label Refinement for Face Parsing Under Extreme Poses Using 3D
  Gaussian Splatting](https://arxiv.org/abs/2510.08096v1)**  
  Authors: Ankit Gahlawat, Anirban Mukherjee, Dinesh Babu Jayagopi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.08096v1.pdf)  
  Keywords: 3d gaussian, head, segmentation, human, ar, gaussian splatting, efficient, face, geometry  

### Large Scene

- **[PAGS: Priority-Adaptive Gaussian Splatting for Dynamic Driving Scenes](https://arxiv.org/abs/2510.12282v1)**  
  Authors: Ying A, Wenzhang Sun, Chang Zeng, Chunfeng Wang, Hao Li, Jianxun Cui  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.12282v1.pdf)  
  Keywords: semantic, autonomous driving, ar, gaussian splatting, face, dynamic, 3d reconstruction, urban scene  
- **[Two-Stage Gaussian Splatting Optimization for Outdoor Scene
  Reconstruction](https://arxiv.org/abs/2510.09489v1)**  
  Authors: Deborah Pintani, Ariel Caputo, Noah Lewis, Marc Stamminger, Fabio Pellacini, Andrea Giachetti  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.09489v1.pdf)  
  Keywords: motion, ar, illumination, gaussian splatting, outdoor  
- **[Visibility-Aware Densification for 3D Gaussian Splatting in Dynamic
  Urban Scenes](https://arxiv.org/abs/2510.09364v1)**  
  Authors: Yikang Zhang, Rui Fan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.09364v1.pdf)  
  Keywords: 3d gaussian, ar, high-fidelity, gaussian splatting, face, dynamic, geometry, urban scene  
- **[LOBE-GS: Load-Balanced and Efficient 3D Gaussian Splatting for
  Large-Scale Scene Reconstruction](https://arxiv.org/abs/2510.01767v1)**  
  Authors: Sheng-Hsiang Hung, Ting-Yu Yen, Wei-Fang Sun, Simon See, Shih-Hsuan Hung, Hung-Kuo Chu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.01767v1.pdf)  
  Keywords: lightweight, 3d gaussian, head, ar, fast, efficient, high-fidelity, gaussian splatting, outdoor  
- **[LVT: Large-Scale Scene Reconstruction via Local View Transformers](https://arxiv.org/abs/2509.25001v1)**  
  Authors: Tooba Imtiaz, Lucy Chai, Kathryn Heal, Xuan Luo, Jungyeon Park, Jennifer Dy, John Flynn  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.25001v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://toobaimt.github.io/lvt/.)  
  Keywords: ar, large scene, 3d gaussian  
- **[Aerial-Ground Image Feature Matching via 3D Gaussian Splatting-based
  Intermediate View Rendering](https://arxiv.org/abs/2509.19898v1)**  
  Authors: Jiangxue Yu, Hui Wang, San Jiang, Xing Zhang, Dejin Zhang, Qingquan Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.19898v1.pdf)  
  Keywords: large scene, motion, 3d gaussian, ar, gaussian splatting  
- **[FGGS-LiDAR: Ultra-Fast, GPU-Accelerated Simulation from General 3DGS
  Models to LiDAR](https://arxiv.org/abs/2509.17390v1)**  
  Authors: Junzhe Wu, Yufei Jia, Yiyi Yan, Zhixing Chen, Tiao Tan, Zifan Wang, Guangyu Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.17390v1.pdf)  
  Keywords: autonomous driving, 3d gaussian, ar, fast, robotics, high-fidelity, gaussian splatting, outdoor  
- **[ROSGS: Relightable Outdoor Scenes With Gaussian Splatting](https://arxiv.org/abs/2509.11275v1)**  
  Authors: Lianjun Liao, Chunhui Zhang, Tong Wu, Henglei Lv, Bailin Deng, Lin Gao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.11275v1.pdf)  
  Keywords: relightable, relighting, 3d gaussian, head, compact, ar, nerf, efficient, efficient rendering, lighting, illumination, gaussian splatting, outdoor, geometry  
- **[VIM-GS: Visual-Inertial Monocular Gaussian Splatting via Object-level
  Guidance in Large Scenes](https://arxiv.org/abs/2509.06685v3)**  
  Authors: Shengkai Zhang, Yuhe Liu, Guanjun Wu, Jianhua He, Xinggang Wang, Mozi Chen, Kezhong Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.06685v3.pdf)  
  Keywords: large scene, motion, ar, gaussian splatting, dynamic  
- **[3DOF+Quantization: 3DGS quantization for large scenes with limited
  Degrees of Freedom](https://arxiv.org/abs/2509.06400v1)**  
  Authors: Matthieu Gendrin, Stéphane Pateux, Théo Ladune  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.06400v1.pdf)  
  Keywords: gaussian splatting, ar, large scene, 3d gaussian  

### Model Compression

*Showing the latest 50 out of 195 papers*

- **[Uncertainty Matters in Dynamic Gaussian Splatting for Monocular 4D
  Reconstruction](https://arxiv.org/abs/2510.12768v1)**  
  Authors: Fengzhi Guo, Chih-Chuan Hsu, Sihao Ding, Cheng Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.12768v1.pdf)  
  Keywords: motion, 4d, ar, gaussian splatting, efficient, dynamic, geometry  
- **[GS-Verse: Mesh-based Gaussian Splatting for Physics-aware Interaction in
  Virtual Reality](https://arxiv.org/abs/2510.11878v1)**  
  Authors: Anastasiya Pechko, Piotr Borycki, Joanna Waczyńska, Daniel Barczyk, Agata Szymańska, Sławomir Tadeja, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.11878v1.pdf)  
  Keywords: vr, ar, face, gaussian splatting, efficient, deformation  
- **[Ev4DGS: Novel-view Rendering of Non-Rigid Objects from Monocular Event
  Streams](https://arxiv.org/abs/2510.11717v1)**  
  Authors: Takuya Nakabayashi, Navami Kairanda, Hideo Saito, Vladislav Golyanik  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.11717v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://4dqv.mpi-inf.mpg.de/Ev4DGS/.)  
  Keywords: 3d gaussian, 4d, ar, gaussian splatting, efficient, deformation  
- **[VA-GS: Enhancing the Geometric Representation of Gaussian Splatting via
  View Alignment](https://arxiv.org/abs/2510.11473v1)**  
  Authors: Qing Li, Huifang Feng, Xun Gong, Yu-Shen Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.11473v1.pdf)  
  Keywords: 3d gaussian, ar, lighting, illumination, gaussian splatting, efficient, face, geometry  
- **[Towards Efficient 3D Gaussian Human Avatar Compression: A Prior-Guided
  Framework](https://arxiv.org/abs/2510.10492v1)**  
  Authors: Shanzhi Yin, Bolin Chen, Xinju Wu, Ru-Ling Liao, Jie Chen, Shiqi Wang, Yan Ye  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.10492v1.pdf)  
  Keywords: 3d gaussian, avatar, compact, human, ar, body, compression, gaussian splatting, efficient, dynamic  
- **[Opacity-Gradient Driven Density Control for Compact and Efficient
  Few-Shot 3D Gaussian Splatting](https://arxiv.org/abs/2510.10257v1)**  
  Authors: Abdelrhman Elrawy, Emad A. Mohammed  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.10257v1.pdf)  
  Keywords: lightweight, 3d gaussian, compact, ar, nerf, gaussian splatting, efficient, few-shot  
- **[P-4DGS: Predictive 4D Gaussian Splatting with 90$\times$ Compression](https://arxiv.org/abs/2510.10030v1)**  
  Authors: Henan Wang, Hanxin Zhu, Xinliang Gong, Tianyu He, Xin Li, Zhibo Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.10030v1.pdf)  
  Keywords: 3d gaussian, compact, 4d, fast, ar, compression, gaussian splatting, dynamic, real-time rendering  
- **[VG-Mapping: Variation-Aware 3D Gaussians for Online Semi-static Scene
  Mapping](https://arxiv.org/abs/2510.09962v1)**  
  Authors: Yicheng He, Jingwen Yu, Guangcheng Chen, Hong Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.09962v1.pdf)  
  Keywords: 3d gaussian, ar, mapping, gaussian splatting, efficient, localization  
- **[LTGS: Long-Term Gaussian Scene Chronology From Sparse View Updates](https://arxiv.org/abs/2510.09881v1)**  
  Authors: Minkwan Kim, Seungmin Lee, Junho Kim, Young Min Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.09881v1.pdf)  
  Keywords: sparse-view, ar, fast, gaussian splatting, efficient, face, sparse view, few-shot  
- **[Vision Language Models: A Survey of 26K Papers](https://arxiv.org/abs/2510.09586v1)**  
  Authors: Fengming Lin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.09586v1.pdf)  
  Keywords: lightweight, human, understanding, ar, nerf, survey, gaussian splatting, efficient  

### Quality Enhancement

*Showing the latest 50 out of 91 papers*

- **[UniGS: Unified Geometry-Aware Gaussian Splatting for Multimodal
  Rendering](https://arxiv.org/abs/2510.12174v1)**  
  Authors: Yusen Xie, Zhenmin Huang, Jianhao Jiao, Dimitrios Kanoulas, Jun Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.12174v1.pdf)  
  Keywords: semantic, 3d gaussian, ar, high-fidelity, gaussian splatting, face, geometry, 3d reconstruction  
- **[Phys2Real: Fusing VLM Priors with Interactive Online Adaptation for
  Uncertainty-Aware Sim-to-Real Manipulation](https://arxiv.org/abs/2510.11689v1)**  
  Authors: Maggie Wang, Stephen Tian, Aiden Swann, Ola Shorinwa, Jiajun Wu, Mac Schwager  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.11689v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://phys2real.github.io/)  
  Keywords: 3d gaussian, ar, fast, high-fidelity, gaussian splatting, dynamic  
- **[High-Fidelity Simulated Data Generation for Real-World Zero-Shot Robotic
  Manipulation Learning with Gaussian Splatting](https://arxiv.org/abs/2510.10637v1)**  
  Authors: Haoyu Zhao, Cheng Zeng, Linghao Zhuang, Yaxi Zhao, Shengke Xue, Hao Wang, Xingyue Zhao, Zhongyu Li, Kehan Li, Siteng Huang, Mingxiu Chen, Xin Li, Deli Zhao, Hua Zou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.10637v1.pdf)  
  Keywords: gaussian splatting, high-fidelity, ar, 3d gaussian  
- **[CLoD-GS: Continuous Level-of-Detail via 3D Gaussian Splatting](https://arxiv.org/abs/2510.09997v1)**  
  Authors: Zhigang Cheng, Mingchao Sun, Yu Liu, Zengye Ge, Luyang Tang, Mu Xu, Yangyan Li, Peng Pan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.09997v1.pdf)  
  Keywords: 3d gaussian, head, ar, high-fidelity, gaussian splatting, dynamic  
- **[Visibility-Aware Densification for 3D Gaussian Splatting in Dynamic
  Urban Scenes](https://arxiv.org/abs/2510.09364v1)**  
  Authors: Yikang Zhang, Rui Fan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.09364v1.pdf)  
  Keywords: 3d gaussian, ar, high-fidelity, gaussian splatting, face, dynamic, geometry, urban scene  
- **[D$^2$GS: Depth-and-Density Guided Gaussian Splatting for Stable and
  Accurate Sparse-View Reconstruction](https://arxiv.org/abs/2510.08566v1)**  
  Authors: Meixi Song, Xin Lin, Dizhe Zhang, Haodong Li, Xiangtai Li, Bo Du, Lu Qi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.08566v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://insta360-research-team.github.io/DDGS-website/.)  
  Keywords: sparse-view, 3d gaussian, ar, high-fidelity, gaussian splatting, sparse view  
- **[CVD-STORM: Cross-View Video Diffusion with Spatial-Temporal
  Reconstruction Model for Autonomous Driving](https://arxiv.org/abs/2510.07944v1)**  
  Authors: Tianrui Zhang, Yichen Liu, Zilin Guo, Yuxin Guo, Jingcheng Ni, Chenjing Ding, Dan Xu, Lewei Lu, Zehuan Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.07944v1.pdf)  
  Keywords: autonomous driving, understanding, 4d, ar, high-fidelity, gaussian splatting, dynamic  
- **[PrismGS: Physically-Grounded Anti-Aliasing for High-Fidelity Large-Scale
  3D Gaussian Splatting](https://arxiv.org/abs/2510.07830v1)**  
  Authors: Houqiang Zhong, Zhenglong Wu, Sihua Fu, Zihan Zheng, Xin Jin, Xiaoyun Zhang, Li Song, Qiang Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.07830v1.pdf)  
  Keywords: 3d gaussian, compact, ar, high-fidelity, gaussian splatting, face, geometry  
- **[Generating Surface for Text-to-3D using 2D Gaussian Splatting](https://arxiv.org/abs/2510.06967v1)**  
  Authors: Huanning Dong, Fan Li, Ping Kuang, Jianwen Min  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.06967v1.pdf)  
  Keywords: gaussian splatting, face, geometry, high-fidelity  
- **[Optimized Minimal 4D Gaussian Splatting](https://arxiv.org/abs/2510.03857v1)**  
  Authors: Minseo Lee, Byeonghyeon Lee, Lucas Yunkyu Lee, Eunsoo Lee, Sangmin Kim, Seunghyeon Song, Joo Chan Lee, Jong Hwan Ko, Jaesik Park, Eunbyung Park  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.03857v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://minshirley.github.io/OMG4/.)  
  Keywords: motion, head, compact, 4d, ar, high-fidelity, compression, gaussian splatting, face, dynamic, real-time rendering  

### Ray Tracing

- **[MaterialRefGS: Reflective Gaussian Splatting with Multi-view Consistent
  Material Inference](https://arxiv.org/abs/2510.11387v1)**  
  Authors: Wenyuan Zhang, Jimin Tang, Weiqi Zhang, Yi Fang, Yu-Shen Liu, Zhizhong Han  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.11387v1.pdf)  
  Keywords: ray tracing, ar, reflection, illumination, gaussian splatting, geometry  
- **[Splat the Net: Radiance Fields with Splattable Neural Primitives](https://arxiv.org/abs/2510.08491v1)**  
  Authors: Xilong Zhou, Bao-Huy Nguyen, Loïc Magne, Vladislav Golyanik, Thomas Leimkühler, Christian Theobalt  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.08491v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://vcai.mpi-inf.mpg.de/projects/SplatNet/.)  
  Keywords: 3d gaussian, ar, gaussian splatting, efficient, geometry, ray marching  
- **[ComGS: Efficient 3D Object-Scene Composition via Surface Octahedral
  Probes](https://arxiv.org/abs/2510.07729v1)**  
  Authors: Jian Gao, Mengqi Yuan, Yifei Zeng, Chang Zeng, Zhihao Li, Zhenyu Chen, Weichao Qiu, Xiao-Xiao Long, Hao Zhu, Xun Cao, Yao Yao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.07729v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://nju-3dv.github.io/projects/ComGS/.)  
  Keywords: relightable, ray tracing, light transport, ar, lighting, shadow, gaussian splatting, efficient, face, real-time rendering  
- **[Differentiable Light Transport with Gaussian Surfels via Adapted
  Radiosity for Efficient Relighting and Geometry Reconstruction](https://arxiv.org/abs/2509.18497v2)**  
  Authors: Kaiwen Jiang, Jia-Mu Sun, Zilu Li, Dan Wang, Tzu-Mao Li, Ravi Ramamoorthi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.18497v2.pdf)  
  Keywords: light transport, global illumination, relighting, ar, lighting, illumination, reflection, gaussian splatting, efficient, geometry  
- **[Every Camera Effect, Every Time, All at Once: 4D Gaussian Ray Tracing
  for Physics-based Camera Effect Data Generation](https://arxiv.org/abs/2509.10759v1)**  
  Authors: Yi-Ruei Liu, You-Zhe Xie, Yu-Hsiang Hsu, I-Sheng Fang, Yu-Lun Liu, Jun-Cheng Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.10759v1.pdf)  
  Keywords: ray tracing, 4d, fast, ar, gaussian splatting, dynamic  
- **[GOGS: High-Fidelity Geometry and Relighting for Glossy Objects via
  Gaussian Surfels](https://arxiv.org/abs/2508.14563v1)**  
  Authors: Xingyuan Yang, Min Wei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2508.14563v1.pdf)  
  Keywords: ray tracing, relighting, 3d gaussian, ar, nerf, lighting, high-fidelity, illumination, gaussian splatting, reflection, face, geometry  
- **[GaRe: Relightable 3D Gaussian Splatting for Outdoor Scenes from
  Unconstrained Photo Collections](https://arxiv.org/abs/2507.20512v1)**  
  Authors: Haiyang Bai, Jiaqi Zhu, Songru Jiang, Wei Huang, Tao Lu, Yuanqi Li, Jie Guo, Runze Fu, Yanwen Guo, Lijun Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.20512v1.pdf)  
  Keywords: relightable, global illumination, 3d gaussian, relighting, ar, lighting, shadow, illumination, gaussian splatting, outdoor, face, dynamic  
- **[GSCache: Real-Time Radiance Caching for Volume Path Tracing using 3D
  Gaussian Splatting](https://arxiv.org/abs/2507.19718v2)**  
  Authors: David Bauer, Qi Wu, Hamid Gadirov, Kwan-Liu Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.19718v2.pdf)  
  Keywords: path tracing, 3d gaussian, ar, lighting, gaussian splatting, face, dynamic  
- **[Gaussian Splatting with Discretized SDF for Relightable Assets](https://arxiv.org/abs/2507.15629v1)**  
  Authors: Zuo-Liang Zhu, Jian Yang, Beibei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2507.15629v1.pdf)  
  Keywords: relightable, relighting, 3d gaussian, ar, efficient rendering, lighting, gaussian splatting, efficient, face, geometry, ray marching  
- **[RaRa Clipper: A Clipper for Gaussian Splatting Based on Ray Tracer and
  Rasterizer](https://arxiv.org/abs/2506.20202v1)**  
  Authors: Da Li, Donggang Jia, Yousef Rajeh, Dominik Engel, Ivan Viola  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2506.20202v1.pdf)  
  Keywords: ray tracing, ar, high-fidelity, gaussian splatting, efficient, real-time rendering  

### Relighting

*Showing the latest 50 out of 59 papers*

- **[VA-GS: Enhancing the Geometric Representation of Gaussian Splatting via
  View Alignment](https://arxiv.org/abs/2510.11473v1)**  
  Authors: Qing Li, Huifang Feng, Xun Gong, Yu-Shen Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.11473v1.pdf)  
  Keywords: 3d gaussian, ar, lighting, illumination, gaussian splatting, efficient, face, geometry  
- **[MaterialRefGS: Reflective Gaussian Splatting with Multi-view Consistent
  Material Inference](https://arxiv.org/abs/2510.11387v1)**  
  Authors: Wenyuan Zhang, Jimin Tang, Weiqi Zhang, Yi Fang, Yu-Shen Liu, Zhizhong Han  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.11387v1.pdf)  
  Keywords: ray tracing, ar, reflection, illumination, gaussian splatting, geometry  
- **[Two-Stage Gaussian Splatting Optimization for Outdoor Scene
  Reconstruction](https://arxiv.org/abs/2510.09489v1)**  
  Authors: Deborah Pintani, Ariel Caputo, Noah Lewis, Marc Stamminger, Fabio Pellacini, Andrea Giachetti  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.09489v1.pdf)  
  Keywords: motion, ar, illumination, gaussian splatting, outdoor  
- **[ComGS: Efficient 3D Object-Scene Composition via Surface Octahedral
  Probes](https://arxiv.org/abs/2510.07729v1)**  
  Authors: Jian Gao, Mengqi Yuan, Yifei Zeng, Chang Zeng, Zhihao Li, Zhenyu Chen, Weichao Qiu, Xiao-Xiao Long, Hao Zhu, Xun Cao, Yao Yao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.07729v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://nju-3dv.github.io/projects/ComGS/.)  
  Keywords: relightable, ray tracing, light transport, ar, lighting, shadow, gaussian splatting, efficient, face, real-time rendering  
- **[Spec-Gloss Surfels and Normal-Diffuse Priors for Relightable Glossy
  Objects](https://arxiv.org/abs/2510.02069v1)**  
  Authors: Georgios Kouros, Minye Wu, Tinne Tuytelaars  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.02069v1.pdf)  
  Keywords: relightable, relighting, neural rendering, ar, lighting, illumination, reflection, gaussian splatting, face, dynamic, geometry  
- **[MPMAvatar: Learning 3D Gaussian Avatars with Accurate and Robust
  Physics-Based Dynamics](https://arxiv.org/abs/2510.01619v1)**  
  Authors: Changmin Lee, Jihyun Lee, Tae-Kyun Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.01619v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://KAISTChangmin.github.io/MPMAvatar/)  
  Keywords: 3d gaussian, avatar, human, ar, animation, shadow, body, high-fidelity, gaussian splatting, deformation, dynamic  
- **[Universal Beta Splatting](https://arxiv.org/abs/2510.03312v1)**  
  Authors: Rong Liu, Zhongpai Gao, Benjamin Planche, Meida Chen, Van Nguyen Nguyen, Meng Zheng, Anwesa Choudhuri, Terrence Chen, Yue Wang, Andrew Feng, Ziyan Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.03312v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://rongliu-leo.github.io/universal-beta-splatting/.)  
  Keywords: light transport, 3d gaussian, ar, gaussian splatting, face, dynamic, real-time rendering  
- **[Large Material Gaussian Model for Relightable 3D Generation](https://arxiv.org/abs/2509.22112v1)**  
  Authors: Jingrui Ye, Lingting Zhu, Runze Zhang, Zeyu Hu, Yingda Yin, Lanjiong Li, Lequan Yu, Qingmin Liao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.22112v1.pdf)  
  Keywords: relightable, relighting, 3d gaussian, ar, lighting, gaussian splatting, efficient, dynamic  
- **[Dynamic Novel View Synthesis in High Dynamic Range](https://arxiv.org/abs/2509.21853v2)**  
  Authors: Kaixuan Zhang, Zhipeng Xiong, Minxian Li, Mingwu Ren, Jiankang Deng, Xiatian Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.21853v2.pdf)  
  Keywords: 4d, ar, mapping, lighting, gaussian splatting, dynamic  
- **[Seeing Through Reflections: Advancing 3D Scene Reconstruction in
  Mirror-Containing Environments with Gaussian Splatting](https://arxiv.org/abs/2509.18956v1)**  
  Authors: Zijing Guo, Yunyang Zhao, Lin Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.18956v1.pdf)  
  Keywords: 3d gaussian, ar, nerf, mapping, reflection, gaussian splatting, face, geometry, 3d reconstruction  

### SLAM

*Showing the latest 50 out of 70 papers*

- **[Color3D: Controllable and Consistent 3D Colorization with Personalized
  Colorizer](https://arxiv.org/abs/2510.10152v1)**  
  Authors: Yecong Wan, Mingwen Shao, Renlong Wu, Wangmeng Zuo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.10152v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://yecongwan.github.io/Color3D/.)  
  Keywords: gaussian splatting, ar, dynamic, mapping  
- **[VG-Mapping: Variation-Aware 3D Gaussians for Online Semi-static Scene
  Mapping](https://arxiv.org/abs/2510.09962v1)**  
  Authors: Yicheng He, Jingwen Yu, Guangcheng Chen, Hong Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.09962v1.pdf)  
  Keywords: 3d gaussian, ar, mapping, gaussian splatting, efficient, localization  
- **[SCas4D: Structural Cascaded Optimization for Boosting Persistent 4D
  Novel View Synthesis](https://arxiv.org/abs/2510.06694v1)**  
  Authors: Jipeng Lyu, Jiahua Dong, Yu-Xiong Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.06694v1.pdf)  
  Keywords: 3d gaussian, segmentation, 4d, ar, tracking, gaussian splatting, deformation, dynamic  
- **[RTGS: Real-Time 3D Gaussian Splatting SLAM via Multi-Level Redundancy
  Reduction](https://arxiv.org/abs/2510.06644v2)**  
  Authors: Leshu Li, Jiayin Qin, Jie Peng, Zishen Wan, Huaizhi Qu, Ye Han, Pingqing Zheng, Hongsen Zhang, Yu Cao, Tianlong Chen, Yang Katie Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.06644v2.pdf)  
  Keywords: 3d gaussian, head, ar, slam, mapping, acceleration, gaussian splatting, dynamic, localization  
- **[Geometry Meets Vision: Revisiting Pretrained Semantics in Distilled
  Fields](https://arxiv.org/abs/2510.03104v1)**  
  Authors: Zhiting Mei, Ola Shorinwa, Anirudha Majumdar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.03104v1.pdf)  
  Keywords: semantic, ar, gaussian splatting, geometry, localization  
- **[GaussianMorphing: Mesh-Guided 3D Gaussians for Semantic-Aware Object
  Morphing](https://arxiv.org/abs/2510.02034v1)**  
  Authors: Mengtian Li, Yunshu Bai, Yimin Chu, Yijun Shen, Zhongmei Li, Weifeng Ge, Zhifeng Xie, Chaofeng Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.02034v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://baiyunshu.github.io/GAUSSIANMORPHING.github.io/)  
  Keywords: semantic, 3d gaussian, ar, mapping, high-fidelity, gaussian splatting, deformation, geometry  
- **[GreenhouseSplat: A Dataset of Photorealistic Greenhouse Simulations for
  Mobile Robotics](https://arxiv.org/abs/2510.01848v1)**  
  Authors: Diram Tabaa, Gianni Di Caro  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.01848v1.pdf)  
  Keywords: gaussian splatting, ar, localization, robotics  
- **[From Fields to Splats: A Cross-Domain Survey of Real-Time Neural Scene
  Representations](https://arxiv.org/abs/2509.23555v1)**  
  Authors: Javed Ahmad, Penggang Gao, Donatien Delehelle, Mennuti Canio, Nikhil Deshpande, Jesús Ortiz, Darwin G. Caldwell, Yonas Teodros Tefera  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.23555v1.pdf)  
  Keywords: neural rendering, 3d gaussian, understanding, fast, nerf, slam, ar, survey, gaussian splatting, efficient  
- **[Learning Unified Representation of 3D Gaussian Splatting](https://arxiv.org/abs/2509.22917v1)**  
  Authors: Yuelin Xin, Yuheng Liu, Xiaohui Xie, Xinke Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.22917v1.pdf)  
  Keywords: 3d gaussian, ar, mapping, gaussian splatting, efficient, 3d reconstruction  
- **[Dynamic Novel View Synthesis in High Dynamic Range](https://arxiv.org/abs/2509.21853v2)**  
  Authors: Kaixuan Zhang, Zhipeng Xiong, Minxian Li, Mingwu Ren, Jiankang Deng, Xiatian Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.21853v2.pdf)  
  Keywords: 4d, ar, mapping, lighting, gaussian splatting, dynamic  

### Scene Understanding

*Showing the latest 50 out of 106 papers*

- **[PAGS: Priority-Adaptive Gaussian Splatting for Dynamic Driving Scenes](https://arxiv.org/abs/2510.12282v1)**  
  Authors: Ying A, Wenzhang Sun, Chang Zeng, Chunfeng Wang, Hao Li, Jianxun Cui  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.12282v1.pdf)  
  Keywords: semantic, autonomous driving, ar, gaussian splatting, face, dynamic, 3d reconstruction, urban scene  
- **[UniGS: Unified Geometry-Aware Gaussian Splatting for Multimodal
  Rendering](https://arxiv.org/abs/2510.12174v1)**  
  Authors: Yusen Xie, Zhenmin Huang, Jianhao Jiao, Dimitrios Kanoulas, Jun Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.12174v1.pdf)  
  Keywords: semantic, 3d gaussian, ar, high-fidelity, gaussian splatting, face, geometry, 3d reconstruction  
- **[Vision Language Models: A Survey of 26K Papers](https://arxiv.org/abs/2510.09586v1)**  
  Authors: Fengming Lin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.09586v1.pdf)  
  Keywords: lightweight, human, understanding, ar, nerf, survey, gaussian splatting, efficient  
- **[Efficient Label Refinement for Face Parsing Under Extreme Poses Using 3D
  Gaussian Splatting](https://arxiv.org/abs/2510.08096v1)**  
  Authors: Ankit Gahlawat, Anirban Mukherjee, Dinesh Babu Jayagopi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.08096v1.pdf)  
  Keywords: 3d gaussian, head, segmentation, human, ar, gaussian splatting, efficient, face, geometry  
- **[CVD-STORM: Cross-View Video Diffusion with Spatial-Temporal
  Reconstruction Model for Autonomous Driving](https://arxiv.org/abs/2510.07944v1)**  
  Authors: Tianrui Zhang, Yichen Liu, Zilin Guo, Yuxin Guo, Jingcheng Ni, Chenjing Ding, Dan Xu, Lewei Lu, Zehuan Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.07944v1.pdf)  
  Keywords: autonomous driving, understanding, 4d, ar, high-fidelity, gaussian splatting, dynamic  
- **[SCas4D: Structural Cascaded Optimization for Boosting Persistent 4D
  Novel View Synthesis](https://arxiv.org/abs/2510.06694v1)**  
  Authors: Jipeng Lyu, Jiahua Dong, Yu-Xiong Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.06694v1.pdf)  
  Keywords: 3d gaussian, segmentation, 4d, ar, tracking, gaussian splatting, deformation, dynamic  
- **[Geometry Meets Vision: Revisiting Pretrained Semantics in Distilled
  Fields](https://arxiv.org/abs/2510.03104v1)**  
  Authors: Zhiting Mei, Ola Shorinwa, Anirudha Majumdar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.03104v1.pdf)  
  Keywords: semantic, ar, gaussian splatting, geometry, localization  
- **[GaussianMorphing: Mesh-Guided 3D Gaussians for Semantic-Aware Object
  Morphing](https://arxiv.org/abs/2510.02034v1)**  
  Authors: Mengtian Li, Yunshu Bai, Yimin Chu, Yijun Shen, Zhongmei Li, Weifeng Ge, Zhifeng Xie, Chaofeng Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.02034v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://baiyunshu.github.io/GAUSSIANMORPHING.github.io/)  
  Keywords: semantic, 3d gaussian, ar, mapping, high-fidelity, gaussian splatting, deformation, geometry  
- **[4DGS-Craft: Consistent and Interactive 4D Gaussian Splatting Editing](https://arxiv.org/abs/2510.01991v1)**  
  Authors: Lei Liu, Can Wang, Zhenghao Chen, Dong Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.01991v1.pdf)  
  Keywords: understanding, 4d, ar, gaussian splatting, face, geometry  
- **[CrashSplat: 2D to 3D Vehicle Damage Segmentation in Gaussian Splatting](https://arxiv.org/abs/2509.23947v1)**  
  Authors: Dragoş-Andrei Chileban, Andrei-Ştefan Bulzan, Cosmin Cernǎzanu-Glǎvan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.23947v1.pdf)  
  Keywords: motion, 3d gaussian, segmentation, ar, fast, gaussian splatting, 3d reconstruction  



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