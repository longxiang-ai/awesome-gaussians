# Awesome Gaussian Splatting [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of latest research papers, projects and resources related to Gaussian Splatting. Content is automatically updated daily.

> Last Update: 2025-04-22 00:52:58

## Categories

- [3DGS Surveys](#3dgs-surveys) (27 papers) - Survey papers and benchmarks about 3D Gaussian Splatting
- [Acceleration](#acceleration) (477 papers) - Papers about speeding up rendering or training
- [Applications](#applications) (1678 papers) - Papers about specific applications
- [Avatar Generation](#avatar-generation) (565 papers) - Papers about human avatar generation
- [Dynamic Scene](#dynamic-scene) (633 papers) - Papers about dynamic scene reconstruction and rendering
- [Few-shot](#few-shot) (117 papers) - Papers about few-shot or sparse view reconstruction
- [Geometry Reconstruction](#geometry-reconstruction) (543 papers) - Papers about 3D geometry reconstruction
- [Large Scene](#large-scene) (91 papers) - Papers about large-scale scene reconstruction
- [Model Compression](#model-compression) (638 papers) - Papers about model compression and optimization
- [Quality Enhancement](#quality-enhancement) (270 papers) - Papers focusing on improving rendering quality
- [Ray Tracing](#ray-tracing) (39 papers) - Papers about ray tracing and ray casting in Gaussian Splatting
- [Relighting](#relighting) (191 papers) - Papers about relighting and illumination effects in Gaussian Splatting
- [SLAM](#slam) (247 papers) - Papers about SLAM using Gaussian Splatting
- [Scene Understanding](#scene-understanding) (298 papers) - Papers about scene understanding and semantic analysis



## Table of Contents

- [Categorized Papers](#categorized-papers)
- [Classic Papers](#classic-papers)
- [Open Source Projects](#open-source-projects)
- [Applications](#applications)
- [Tutorials & Blogs](#tutorials--blogs)





## Categorized Papers

### 3DGS Surveys

- **[Digital Twin Generation from Visual Data: A Survey](https://arxiv.org/abs/2504.13159v1)**  
  Authors: Andrew Melnik, Benjamin Alt, Giang Nguyen, Artur Wilkowski, Maciej Stefańczyk, Qirui Wu, Sinan Harms, Helge Rhodin, Manolis Savva, Michael Beetz  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.13159v1.pdf) | [![GitHub](https://img.shields.io/github/stars/ndrwmlnk/awesome-digital-twins?style=social)](https://github.com/ndrwmlnk/awesome-digital-twins)  
  Keywords: lighting, gaussian splatting, semantic, survey, segmentation, ar, robotics, 3d gaussian  
- **[A Survey on Event-driven 3D Reconstruction: Development under Different Categories](https://arxiv.org/abs/2503.19753v2)**  
  Authors: Chuanzhi Xu, Haoxian Zhou, Haodong Chen, Vera Chung, Qiang Qu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.19753v2.pdf)  
  Keywords: 3d gaussian, lighting, gaussian splatting, motion, survey, 3d reconstruction, dynamic, ar, fast  
- **[Dynamic Scene Reconstruction: Recent Advance in Real-time Rendering and Streaming](https://arxiv.org/abs/2503.08166v1)**  
  Authors: Jiaxuan Zhu, Hao Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.08166v1.pdf)  
  Keywords: real-time rendering, gaussian splatting, survey, dynamic, ar, 3d gaussian  
- **[Infinite Leagues Under the Sea: Photorealistic 3D Underwater Terrain Generation by Latent Fractal Diffusion Models](https://arxiv.org/abs/2503.06784v1)**  
  Authors: Tianyi Zhang, Weiming Zhi, Joshua Mangelson, Matthew Johnson-Roberson  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.06784v1.pdf)  
  Keywords: geometry, survey, semantic, ar  
- **[Compression in 3D Gaussian Splatting: A Survey of Methods, Trends, and Future Directions](https://arxiv.org/abs/2502.19457v1)**  
  Authors: Muhammad Salman Ali, Chaoning Zhang, Marco Cagnazzo, Giuseppe Valenzise, Enzo Tartaglione, Sung-Ho Bae  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.19457v1.pdf)  
  Keywords: real-time rendering, gaussian splatting, nerf, survey, 3d reconstruction, compression, efficient, 3d gaussian, ar  
- **[Grounding Creativity in Physics: A Brief Survey of Physical Priors in AIGC](https://arxiv.org/abs/2502.07007v1)**  
  Authors: Siwei Meng, Yawei Luo, Ping Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.07007v1.pdf)  
  Keywords: lighting, 4d, gaussian splatting, motion, nerf, survey, dynamic, ar, deformation  
- **[Scalable 3D Gaussian Splatting-Based RF Signal Spatial Propagation Modeling](https://arxiv.org/abs/2502.01826v1)**  
  Authors: Kang Yang, Gaofeng Dong, Sijie Ji, Wan Du, Mani Srivastava  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.01826v1.pdf)  
  Keywords: ray tracing, gaussian splatting, survey, ar, 3d gaussian  
- **[NFL-BA: Improving Endoscopic SLAM with Near-Field Light Bundle Adjustment](https://arxiv.org/abs/2412.13176v2)**  
  Authors: Andrea Dunn Beltran, Daniel Rho, Stephen Pizer, Marc Niethammer, Roni Sengupta  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.13176v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://asdunnbe.github.io/NFL-BA/)  
  Keywords: lighting, slam, geometry, survey, mapping, tracking, face, dynamic, localization, ar, outdoor  
- **[Adversarial Attacks Using Differentiable Rendering: A Survey](https://arxiv.org/abs/2411.09749v1)**  
  Authors: Matthew Hull, Chao Zhang, Zsolt Kira, Duen Horng Chau  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.09749v1.pdf)  
  Keywords: gaussian splatting, recognition, survey, ar, illumination, 3d gaussian  
- **[Neural Fields in Robotics: A Survey](https://arxiv.org/abs/2410.20220v1)**  
  Authors: Muhammad Zubair Irshad, Mauro Comi, Yen-Chen Lin, Nick Heppert, Abhinav Valada, Rares Ambrus, Zsolt Kira, Jonathan Tremblay  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.20220v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://robonerf.github.io)  
  Keywords: high-fidelity, lighting, gaussian splatting, nerf, geometry, semantic, survey, autonomous driving, 3d reconstruction, dynamic, ar, compact, robotics  

### Acceleration

*Showing the latest 50 out of 477 papers*

- **[Volume Encoding Gaussians: Transfer Function-Agnostic 3D Gaussians for Volume Rendering](https://arxiv.org/abs/2504.13339v1)**  
  Authors: Landon Dyken, Andres Sewell, Will Usher, Steve Petruzza, Sidharth Kumar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.13339v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, motion, geometry, ar, efficient, fast  
- **[Training-Free Hierarchical Scene Understanding for Gaussian Splatting with Superpoint Graphs](https://arxiv.org/abs/2504.13153v1)**  
  Authors: Shaohui Dai, Yansong Qu, Zheyan Li, Xinyang Li, Shengchuan Zhang, Liujuan Cao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.13153v1.pdf) | [![GitHub](https://img.shields.io/github/stars/Atrovast/THGS?style=social)](https://github.com/Atrovast/THGS)  
  Keywords: 3d gaussian, gaussian splatting, understanding, geometry, semantic, segmentation, ar, compact, efficient, fast  
- **[Second-order Optimization of Gaussian Splats with Importance Sampling](https://arxiv.org/abs/2504.12905v1)**  
  Authors: Hamza Pehlivan, Andrea Boscolo Camiletto, Lin Geng Foo, Marc Habermann, Christian Theobalt  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.12905v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://vcai.mpi-inf.mpg.de/projects/LM-IS)  
  Keywords: gaussian splatting, fast, 3d gaussian, ar  
- **[EDGS: Eliminating Densification for Efficient Convergence of 3DGS](https://arxiv.org/abs/2504.13204v1)**  
  Authors: Dmytro Kotovenko, Olga Grebenkova, Björn Ommer  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.13204v1.pdf)  
  Keywords: gaussian splatting, motion, geometry, ar, efficient, 3d gaussian, acceleration  
- **[3DAffordSplat: Efficient Affordance Reasoning with 3D Gaussians](https://arxiv.org/abs/2504.11218v2)**  
  Authors: Zeming Wei, Junyi Lin, Yang Liu, Weixing Chen, Jingzhou Luo, Guanbin Li, Liang Lin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.11218v2.pdf)  
  Keywords: high-fidelity, lighting, head, real-time rendering, gaussian splatting, recognition, human, efficient, 3d gaussian, ar  
- **[3D Gabor Splatting: Reconstruction of High-frequency Surface Texture using Gabor Noise](https://arxiv.org/abs/2504.11003v1)**  
  Authors: Haato Watanabe, Kenji Tojo, Nobuyuki Umetani  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.11003v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, lightweight, face, ar, fast  
- **[DNF-Avatar: Distilling Neural Fields for Real-time Animatable Avatar Relighting](https://arxiv.org/abs/2504.10486v1)**  
  Authors: Zeren Jiang, Shaofei Wang, Siyu Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.10486v1.pdf)  
  Keywords: shadow, lighting, ray tracing, avatar, gaussian splatting, geometry, relighting, human, relightable, fast, ar  
- **[LL-Gaussian: Low-Light Scene Reconstruction and Enhancement via Gaussian Splatting for Novel View Synthesis](https://arxiv.org/abs/2504.10331v3)**  
  Authors: Hao Sun, Fenggen Yu, Huiyao Xu, Tao Zhang, Changqing Zou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.10331v3.pdf)  
  Keywords: real-time rendering, gaussian splatting, nerf, 3d reconstruction, dynamic, ar, illumination, fast, 3d gaussian  
- **[GaussVideoDreamer: 3D Scene Generation with Video Diffusion and Inconsistency-Aware Gaussian Splatting](https://arxiv.org/abs/2504.10001v3)**  
  Authors: Junlin Hao, Peiheng Wang, Haoyang Wang, Xinggong Zhang, Zongming Guo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.10001v3.pdf)  
  Keywords: 3d gaussian, gaussian splatting, geometry, ar, fast  
- **[MCBlock: Boosting Neural Radiance Field Training Speed by MCTS-based Dynamic-Resolution Ray Sampling](https://arxiv.org/abs/2504.09878v1)**  
  Authors: Yunpeng Tan, Junlin Hao, Jiangkai Wu, Liming Liu, Qingyang Li, Xinggong Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.09878v1.pdf)  
  Keywords: high-fidelity, gaussian splatting, nerf, dynamic, ar, efficient, acceleration  

### Applications

*Showing the latest 50 out of 1678 papers*

- **[SLAM&Render: A Benchmark for the Intersection Between Neural Rendering, Gaussian Splatting and SLAM](https://arxiv.org/abs/2504.13713v1)**  
  Authors: Samuel Cerezo, Gaetano Meli, Tomás Berriel Martins, Kirill Safronov, Javier Civera  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.13713v1.pdf)  
  Keywords: lighting, slam, gaussian splatting, neural rendering, nerf, mapping, localization, ar, illumination  
- **[Green Robotic Mixed Reality with Gaussian Splatting](https://arxiv.org/abs/2504.13697v1)**  
  Authors: Chenxuan Liu, He Li, Zongze Li, Shuai Wang, Wei Xu, Kejiang Ye, Derrick Wing Kwan Ng, Chengzhong Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.13697v1.pdf)  
  Keywords: gaussian splatting, ar  
- **[EG-Gaussian: Epipolar Geometry and Graph Network Enhanced 3D Gaussian Splatting](https://arxiv.org/abs/2504.13540v1)**  
  Authors: Beizhen Zhao, Yifan Zhou, Zijian Wang, Hao Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.13540v1.pdf)  
  Keywords: sparse-view, gaussian splatting, outdoor, geometry, ar, efficient, 3d gaussian  
- **[Volume Encoding Gaussians: Transfer Function-Agnostic 3D Gaussians for Volume Rendering](https://arxiv.org/abs/2504.13339v1)**  
  Authors: Landon Dyken, Andres Sewell, Will Usher, Steve Petruzza, Sidharth Kumar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.13339v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, motion, geometry, ar, efficient, fast  
- **[Novel Demonstration Generation with Gaussian Splatting Enables Robust One-Shot Manipulation](https://arxiv.org/abs/2504.13175v1)**  
  Authors: Sizhe Yang, Wenye Yu, Jia Zeng, Jun Lv, Kerui Ren, Cewu Lu, Dahua Lin, Jiangmiao Pang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.13175v1.pdf)  
  Keywords: lighting, gaussian splatting, face, ar, 3d gaussian  
- **[ODHSR: Online Dense 3D Reconstruction of Humans and Scenes from Monocular Videos](https://arxiv.org/abs/2504.13167v2)**  
  Authors: Zetong Zhang, Manuel Kaufmann, Lixin Xue, Jie Song, Martin R. Oswald  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.13167v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://eth-ait.github.io/ODHSR.)  
  Keywords: gaussian splatting, understanding, neural rendering, tracking, 3d reconstruction, human, deformation, 3d gaussian, ar, efficient  
- **[Digital Twin Generation from Visual Data: A Survey](https://arxiv.org/abs/2504.13159v1)**  
  Authors: Andrew Melnik, Benjamin Alt, Giang Nguyen, Artur Wilkowski, Maciej Stefańczyk, Qirui Wu, Sinan Harms, Helge Rhodin, Manolis Savva, Michael Beetz  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.13159v1.pdf) | [![GitHub](https://img.shields.io/github/stars/ndrwmlnk/awesome-digital-twins?style=social)](https://github.com/ndrwmlnk/awesome-digital-twins)  
  Keywords: lighting, gaussian splatting, semantic, survey, segmentation, ar, robotics, 3d gaussian  
- **[Training-Free Hierarchical Scene Understanding for Gaussian Splatting with Superpoint Graphs](https://arxiv.org/abs/2504.13153v1)**  
  Authors: Shaohui Dai, Yansong Qu, Zheyan Li, Xinyang Li, Shengchuan Zhang, Liujuan Cao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.13153v1.pdf) | [![GitHub](https://img.shields.io/github/stars/Atrovast/THGS?style=social)](https://github.com/Atrovast/THGS)  
  Keywords: 3d gaussian, gaussian splatting, understanding, geometry, semantic, segmentation, ar, compact, efficient, fast  
- **[CompGS++: Compressed Gaussian Splatting for Static and Dynamic Scene Representation](https://arxiv.org/abs/2504.13022v1)**  
  Authors: Xiangrui Liu, Xinju Wu, Shiqi Wang, Zhu Li, Sam Kwong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.13022v1.pdf)  
  Keywords: gaussian splatting, compression, dynamic, ar, compact  
- **[GSAC: Leveraging Gaussian Splatting for Photorealistic Avatar Creation with Unity Integration](https://arxiv.org/abs/2504.12999v1)**  
  Authors: Rendong Zhang, Alexandra Watkins, Nilanjan Sarkar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.12999v1.pdf)  
  Keywords: lighting, avatar, gaussian splatting, nerf, vr, face, human, efficient, 3d gaussian, ar  

### Avatar Generation

*Showing the latest 50 out of 565 papers*

- **[Novel Demonstration Generation with Gaussian Splatting Enables Robust One-Shot Manipulation](https://arxiv.org/abs/2504.13175v1)**  
  Authors: Sizhe Yang, Wenye Yu, Jia Zeng, Jun Lv, Kerui Ren, Cewu Lu, Dahua Lin, Jiangmiao Pang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.13175v1.pdf)  
  Keywords: lighting, gaussian splatting, face, ar, 3d gaussian  
- **[ODHSR: Online Dense 3D Reconstruction of Humans and Scenes from Monocular Videos](https://arxiv.org/abs/2504.13167v2)**  
  Authors: Zetong Zhang, Manuel Kaufmann, Lixin Xue, Jie Song, Martin R. Oswald  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.13167v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://eth-ait.github.io/ODHSR.)  
  Keywords: gaussian splatting, understanding, neural rendering, tracking, 3d reconstruction, human, deformation, 3d gaussian, ar, efficient  
- **[GSAC: Leveraging Gaussian Splatting for Photorealistic Avatar Creation with Unity Integration](https://arxiv.org/abs/2504.12999v1)**  
  Authors: Rendong Zhang, Alexandra Watkins, Nilanjan Sarkar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.12999v1.pdf)  
  Keywords: lighting, avatar, gaussian splatting, nerf, vr, face, human, efficient, 3d gaussian, ar  
- **[AAA-Gaussians: Anti-Aliased and Artifact-Free 3D Gaussian Rendering](https://arxiv.org/abs/2504.12811v1)**  
  Authors: Michael Steiner, Thomas Köhler, Lukas Radl, Felix Windisch, Dieter Schmalstieg, Markus Steinberger  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.12811v1.pdf)  
  Keywords: gaussian splatting, face, 3d reconstruction, ar, 3d gaussian  
- **[TSGS: Improving Gaussian Splatting for Transparent Surface Reconstruction via Normal and De-lighting Priors](https://arxiv.org/abs/2504.12799v1)**  
  Authors: Mingwei Li, Pu Pang, Hehe Fan, Hua Huang, Yi Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.12799v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://longxiang-ai.github.io/TSGS/.)  
  Keywords: lighting, gaussian splatting, geometry, face, 3d reconstruction, ar, efficient, 3d gaussian  
- **[Mind2Matter: Creating 3D Models from EEG Signals](https://arxiv.org/abs/2504.11936v2)**  
  Authors: Xia Deng, Shen Chen, Jiale Zhou, Lei Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.11936v2.pdf) | [![GitHub](https://img.shields.io/github/stars/sddwwww/Mind2Matter?style=social)](https://github.com/sddwwww/Mind2Matter)  
  Keywords: semantic, face, 3d reconstruction, ar, 3d gaussian  
- **[BEV-GS: Feed-forward Gaussian Splatting in Bird's-Eye-View for Road Reconstruction](https://arxiv.org/abs/2504.13207v1)**  
  Authors: Wenhua Wu, Tong Zhao, Chensheng Peng, Lei Yang, Yintao Wei, Zhe Liu, Hesheng Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.13207v1.pdf) | [![GitHub](https://img.shields.io/github/stars/cat-wwh/BEV-GS?style=social)](https://github.com/cat-wwh/BEV-GS)  
  Keywords: gaussian splatting, nerf, geometry, face, ar  
- **[3DAffordSplat: Efficient Affordance Reasoning with 3D Gaussians](https://arxiv.org/abs/2504.11218v2)**  
  Authors: Zeming Wei, Junyi Lin, Yang Liu, Weixing Chen, Jingzhou Luo, Guanbin Li, Liang Lin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.11218v2.pdf)  
  Keywords: high-fidelity, lighting, head, real-time rendering, gaussian splatting, recognition, human, efficient, 3d gaussian, ar  
- **[3D Gabor Splatting: Reconstruction of High-frequency Surface Texture using Gabor Noise](https://arxiv.org/abs/2504.11003v1)**  
  Authors: Haato Watanabe, Kenji Tojo, Nobuyuki Umetani  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.11003v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, lightweight, face, ar, fast  
- **[DNF-Avatar: Distilling Neural Fields for Real-time Animatable Avatar Relighting](https://arxiv.org/abs/2504.10486v1)**  
  Authors: Zeren Jiang, Shaofei Wang, Siyu Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.10486v1.pdf)  
  Keywords: shadow, lighting, ray tracing, avatar, gaussian splatting, geometry, relighting, human, relightable, fast, ar  

### Dynamic Scene

*Showing the latest 50 out of 633 papers*

- **[Volume Encoding Gaussians: Transfer Function-Agnostic 3D Gaussians for Volume Rendering](https://arxiv.org/abs/2504.13339v1)**  
  Authors: Landon Dyken, Andres Sewell, Will Usher, Steve Petruzza, Sidharth Kumar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.13339v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, motion, geometry, ar, efficient, fast  
- **[ODHSR: Online Dense 3D Reconstruction of Humans and Scenes from Monocular Videos](https://arxiv.org/abs/2504.13167v2)**  
  Authors: Zetong Zhang, Manuel Kaufmann, Lixin Xue, Jie Song, Martin R. Oswald  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.13167v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://eth-ait.github.io/ODHSR.)  
  Keywords: gaussian splatting, understanding, neural rendering, tracking, 3d reconstruction, human, deformation, 3d gaussian, ar, efficient  
- **[CompGS++: Compressed Gaussian Splatting for Static and Dynamic Scene Representation](https://arxiv.org/abs/2504.13022v1)**  
  Authors: Xiangrui Liu, Xinju Wu, Shiqi Wang, Zhu Li, Sam Kwong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.13022v1.pdf)  
  Keywords: gaussian splatting, compression, dynamic, ar, compact  
- **[CAGE-GS: High-fidelity Cage Based 3D Gaussian Splatting Deformation](https://arxiv.org/abs/2504.12800v1)**  
  Authors: Yifei Tong, Runze Tian, Xiao Han, Dingyao Liu, Fenggen Yu, Yan Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.12800v1.pdf)  
  Keywords: high-fidelity, gaussian splatting, ar, deformation, 3d gaussian  
- **[ARAP-GS: Drag-driven As-Rigid-As-Possible 3D Gaussian Splatting Editing with Diffusion Prior](https://arxiv.org/abs/2504.12788v1)**  
  Authors: Xiao Han, Runze Tian, Yifei Tong, Fenggen Yu, Dingyao Liu, Yan Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.12788v1.pdf)  
  Keywords: gaussian splatting, ar, deformation, 3d gaussian, efficient  
- **[EDGS: Eliminating Densification for Efficient Convergence of 3DGS](https://arxiv.org/abs/2504.13204v1)**  
  Authors: Dmytro Kotovenko, Olga Grebenkova, Björn Ommer  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.13204v1.pdf)  
  Keywords: gaussian splatting, motion, geometry, ar, efficient, 3d gaussian, acceleration  
- **[GaSLight: Gaussian Splats for Spatially-Varying Lighting in HDR](https://arxiv.org/abs/2504.10809v2)**  
  Authors: Christophe Bolduc, Yannick Hold-Geoffroy, Zhixin Shu, Jean-François Lalonde  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.10809v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://lvsn.github.io/gaslight/)  
  Keywords: ar, lighting, dynamic  
- **[LL-Gaussian: Low-Light Scene Reconstruction and Enhancement via Gaussian Splatting for Novel View Synthesis](https://arxiv.org/abs/2504.10331v3)**  
  Authors: Hao Sun, Fenggen Yu, Huiyao Xu, Tao Zhang, Changqing Zou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.10331v3.pdf)  
  Keywords: real-time rendering, gaussian splatting, nerf, 3d reconstruction, dynamic, ar, illumination, fast, 3d gaussian  
- **[EBAD-Gaussian: Event-driven Bundle Adjusted Deblur Gaussian Splatting](https://arxiv.org/abs/2504.10012v1)**  
  Authors: Yufei Deng, Yuanjian Wang, Rong Xiao, Chenwei Tang, Jizhe Zhou, Jiahao Fan, Deng Xiong, Jiancheng Lv, Huajin Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.10012v1.pdf)  
  Keywords: gaussian splatting, motion, dynamic, ar, 3d gaussian  
- **[MCBlock: Boosting Neural Radiance Field Training Speed by MCTS-based Dynamic-Resolution Ray Sampling](https://arxiv.org/abs/2504.09878v1)**  
  Authors: Yunpeng Tan, Junlin Hao, Jiangkai Wu, Liming Liu, Qingyang Li, Xinggong Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.09878v1.pdf)  
  Keywords: high-fidelity, gaussian splatting, nerf, dynamic, ar, efficient, acceleration  

### Few-shot

*Showing the latest 50 out of 117 papers*

- **[EG-Gaussian: Epipolar Geometry and Graph Network Enhanced 3D Gaussian Splatting](https://arxiv.org/abs/2504.13540v1)**  
  Authors: Beizhen Zhao, Yifan Zhou, Zijian Wang, Hao Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.13540v1.pdf)  
  Keywords: sparse-view, gaussian splatting, outdoor, geometry, ar, efficient, 3d gaussian  
- **[DropoutGS: Dropping Out Gaussians for Better Sparse-view Rendering](https://arxiv.org/abs/2504.09491v1)**  
  Authors: Yexing Xu, Longguang Wang, Minglin Chen, Sheng Ao, Li Li, Yulan Guo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.09491v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://xuyx55.github.io/DropoutGS/.)  
  Keywords: sparse-view, sparse view, gaussian splatting, ar, 3d gaussian  
- **[GIGA: Generalizable Sparse Image-driven Gaussian Avatars](https://arxiv.org/abs/2504.07144v1)**  
  Authors: Anton Zubekhin, Heming Zhu, Paulo Gotardo, Thabo Beeler, Marc Habermann, Christian Theobalt  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.07144v1.pdf)  
  Keywords: avatar, sparse-view, head, body, human, 3d gaussian, ar  
- **[DropGaussian: Structural Regularization for Sparse-view Gaussian Splatting](https://arxiv.org/abs/2504.00773v1)**  
  Authors: Hyunwoo Park, Gun Ryu, Wonjun Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.00773v1.pdf) | [![GitHub](https://img.shields.io/github/stars/DCVL-3D/DropGaussian?style=social)](https://github.com/DCVL-3D/DropGaussian)  
  Keywords: 3d gaussian, sparse-view, gaussian splatting, face, ar, fast  
- **[Coca-Splat: Collaborative Optimization for Camera Parameters and 3D Gaussians](https://arxiv.org/abs/2504.00639v1)**  
  Authors: Jiamin Wu, Hongyang Li, Xiaoke Jiang, Yuan Yao, Lei Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.00639v1.pdf)  
  Keywords: sparse view, 3d gaussian, ar  
- **[Distilling Multi-view Diffusion Models into 3D Generators](https://arxiv.org/abs/2504.00457v3)**  
  Authors: Hao Qin, Luyuan Chen, Ming Kong, Mengxu Lu, Qiang Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.00457v3.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://qinbaigao.github.io/DD3G_project/)  
  Keywords: sparse-view, gaussian splatting, ar, efficient, 3d gaussian  
- **[Free360: Layered Gaussian Splatting for Unbounded 360-Degree View Synthesis from Extremely Sparse and Unposed Views](https://arxiv.org/abs/2503.24382v1)**  
  Authors: Chong Bao, Xiyu Zhang, Zehao Yu, Jiale Shi, Guofeng Zhang, Songyou Peng, Zhaopeng Cui  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.24382v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://zju3dv.github.io/free360/)  
  Keywords: sparse-view, gaussian splatting, neural rendering, geometry, face, 3d reconstruction, ar  
- **[FreeSplat++: Generalizable 3D Gaussian Splatting for Efficient Indoor Scene Reconstruction](https://arxiv.org/abs/2503.22986v1)**  
  Authors: Yunsong Wang, Tianxin Huang, Hanlin Chen, Gim Hee Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.22986v1.pdf)  
  Keywords: sparse view, gaussian splatting, ar, efficient, 3d gaussian  
- **[CoMapGS: Covisibility Map-based Gaussian Splatting for Sparse Novel View Synthesis](https://arxiv.org/abs/2503.20998v1)**  
  Authors: Youngkyoon Jang, Eduardo Pérez-Pellitero  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.20998v1.pdf)  
  Keywords: gaussian splatting, ar, few-shot, nerf  
- **[SparseGS-W: Sparse-View 3D Gaussian Splatting in the Wild with Generative Priors](https://arxiv.org/abs/2503.19452v1)**  
  Authors: Yiqing Li, Xuan Wang, Jiawei Wu, Yikun Ma, Zhi Jin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.19452v1.pdf)  
  Keywords: 3d gaussian, sparse-view, gaussian splatting, ar, illumination, outdoor  

### Geometry Reconstruction

*Showing the latest 50 out of 543 papers*

- **[EG-Gaussian: Epipolar Geometry and Graph Network Enhanced 3D Gaussian Splatting](https://arxiv.org/abs/2504.13540v1)**  
  Authors: Beizhen Zhao, Yifan Zhou, Zijian Wang, Hao Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.13540v1.pdf)  
  Keywords: sparse-view, gaussian splatting, outdoor, geometry, ar, efficient, 3d gaussian  
- **[Volume Encoding Gaussians: Transfer Function-Agnostic 3D Gaussians for Volume Rendering](https://arxiv.org/abs/2504.13339v1)**  
  Authors: Landon Dyken, Andres Sewell, Will Usher, Steve Petruzza, Sidharth Kumar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.13339v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, motion, geometry, ar, efficient, fast  
- **[ODHSR: Online Dense 3D Reconstruction of Humans and Scenes from Monocular Videos](https://arxiv.org/abs/2504.13167v2)**  
  Authors: Zetong Zhang, Manuel Kaufmann, Lixin Xue, Jie Song, Martin R. Oswald  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.13167v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://eth-ait.github.io/ODHSR.)  
  Keywords: gaussian splatting, understanding, neural rendering, tracking, 3d reconstruction, human, deformation, 3d gaussian, ar, efficient  
- **[Training-Free Hierarchical Scene Understanding for Gaussian Splatting with Superpoint Graphs](https://arxiv.org/abs/2504.13153v1)**  
  Authors: Shaohui Dai, Yansong Qu, Zheyan Li, Xinyang Li, Shengchuan Zhang, Liujuan Cao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.13153v1.pdf) | [![GitHub](https://img.shields.io/github/stars/Atrovast/THGS?style=social)](https://github.com/Atrovast/THGS)  
  Keywords: 3d gaussian, gaussian splatting, understanding, geometry, semantic, segmentation, ar, compact, efficient, fast  
- **[AAA-Gaussians: Anti-Aliased and Artifact-Free 3D Gaussian Rendering](https://arxiv.org/abs/2504.12811v1)**  
  Authors: Michael Steiner, Thomas Köhler, Lukas Radl, Felix Windisch, Dieter Schmalstieg, Markus Steinberger  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.12811v1.pdf)  
  Keywords: gaussian splatting, face, 3d reconstruction, ar, 3d gaussian  
- **[TSGS: Improving Gaussian Splatting for Transparent Surface Reconstruction via Normal and De-lighting Priors](https://arxiv.org/abs/2504.12799v1)**  
  Authors: Mingwei Li, Pu Pang, Hehe Fan, Hua Huang, Yi Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.12799v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://longxiang-ai.github.io/TSGS/.)  
  Keywords: lighting, gaussian splatting, geometry, face, 3d reconstruction, ar, efficient, 3d gaussian  
- **[Mind2Matter: Creating 3D Models from EEG Signals](https://arxiv.org/abs/2504.11936v2)**  
  Authors: Xia Deng, Shen Chen, Jiale Zhou, Lei Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.11936v2.pdf) | [![GitHub](https://img.shields.io/github/stars/sddwwww/Mind2Matter?style=social)](https://github.com/sddwwww/Mind2Matter)  
  Keywords: semantic, face, 3d reconstruction, ar, 3d gaussian  
- **[BEV-GS: Feed-forward Gaussian Splatting in Bird's-Eye-View for Road Reconstruction](https://arxiv.org/abs/2504.13207v1)**  
  Authors: Wenhua Wu, Tong Zhao, Chensheng Peng, Lei Yang, Yintao Wei, Zhe Liu, Hesheng Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.13207v1.pdf) | [![GitHub](https://img.shields.io/github/stars/cat-wwh/BEV-GS?style=social)](https://github.com/cat-wwh/BEV-GS)  
  Keywords: gaussian splatting, nerf, geometry, face, ar  
- **[EDGS: Eliminating Densification for Efficient Convergence of 3DGS](https://arxiv.org/abs/2504.13204v1)**  
  Authors: Dmytro Kotovenko, Olga Grebenkova, Björn Ommer  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.13204v1.pdf)  
  Keywords: gaussian splatting, motion, geometry, ar, efficient, 3d gaussian, acceleration  
- **[Easy3D: A Simple Yet Effective Method for 3D Interactive Segmentation](https://arxiv.org/abs/2504.11024v1)**  
  Authors: Andrea Simonelli, Norman Müller, Peter Kontschieder  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.11024v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://simonelli-andrea.github.io/easy3d.)  
  Keywords: gaussian splatting, lightweight, segmentation, 3d reconstruction, ar, efficient  

### Large Scene

*Showing the latest 50 out of 91 papers*

- **[EG-Gaussian: Epipolar Geometry and Graph Network Enhanced 3D Gaussian Splatting](https://arxiv.org/abs/2504.13540v1)**  
  Authors: Beizhen Zhao, Yifan Zhou, Zijian Wang, Hao Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.13540v1.pdf)  
  Keywords: sparse-view, gaussian splatting, outdoor, geometry, ar, efficient, 3d gaussian  
- **[You Need a Transition Plane: Bridging Continuous Panoramic 3D Reconstruction with Perspective Gaussian Splatting](https://arxiv.org/abs/2504.09062v1)**  
  Authors: Zhijie Shen, Chunyu Lin, Shujuan Huang, Lang Nie, Kang Liao, Yao Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.09062v1.pdf) | [![GitHub](https://img.shields.io/github/stars/zhijieshen-bjtu/TPGS?style=social)](https://github.com/zhijieshen-bjtu/TPGS)  
  Keywords: 3d gaussian, gaussian splatting, face, 3d reconstruction, ar, outdoor  
- **[FIORD: A Fisheye Indoor-Outdoor Dataset with LIDAR Ground Truth for 3D Scene Reconstruction and Benchmarking](https://arxiv.org/abs/2504.01732v2)**  
  Authors: Ulas Gunes, Matias Turkulainen, Xuqian Ren, Arno Solin, Juho Kannala, Esa Rahtu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.01732v2.pdf)  
  Keywords: gaussian splatting, motion, nerf, reflection, ar, outdoor  
- **[UnIRe: Unsupervised Instance Decomposition for Dynamic Urban Scene Reconstruction](https://arxiv.org/abs/2504.00763v1)**  
  Authors: Yunxuan Mao, Rong Xiong, Yue Wang, Yiyi Liao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.00763v1.pdf)  
  Keywords: urban scene, 4d, gaussian splatting, autonomous driving, dynamic, ar, 3d gaussian  
- **[RainyGS: Efficient Rain Synthesis with Physically-Based Gaussian Splatting](https://arxiv.org/abs/2503.21442v2)**  
  Authors: Qiyu Dai, Xingyu Ni, Qianfan Shen, Wenzheng Chen, Baoquan Chen, Mengyu Chu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.21442v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://pku-vcl-geometry.github.io/RainyGS/)  
  Keywords: high-fidelity, gaussian splatting, outdoor, nerf, geometry, reflection, dynamic, ar, efficient, fast  
- **[StyledStreets: Multi-style Street Simulator with Spatial and Temporal Consistency](https://arxiv.org/abs/2503.21104v1)**  
  Authors: Yuyin Chen, Yida Wang, Xueyang Zhang, Kun Zhan, Peng Jia, Yifei Zhan, Xianpeng Lang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.21104v1.pdf)  
  Keywords: urban scene, gaussian splatting, motion, geometry, dynamic, ar  
- **[EVolSplat: Efficient Volume-based Gaussian Splatting for Urban View Synthesis](https://arxiv.org/abs/2503.20168v1)**  
  Authors: Sheng Miao, Jiaxin Huang, Dongfeng Bai, Xu Yan, Hongyu Zhou, Yue Wang, Bingbing Liu, Andreas Geiger, Yiyi Liao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.20168v1.pdf)  
  Keywords: 3d gaussian, urban scene, real-time rendering, gaussian splatting, nerf, autonomous driving, ar, efficient, fast  
- **[SparseGS-W: Sparse-View 3D Gaussian Splatting in the Wild with Generative Priors](https://arxiv.org/abs/2503.19452v1)**  
  Authors: Yiqing Li, Xuan Wang, Jiawei Wu, Yikun Ma, Zhi Jin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.19452v1.pdf)  
  Keywords: 3d gaussian, sparse-view, gaussian splatting, ar, illumination, outdoor  
- **[From Sparse to Dense: Camera Relocalization with Scene-Specific Detector from Feature Gaussian Splatting](https://arxiv.org/abs/2503.19358v1)**  
  Authors: Zhiwei Huang, Hailin Yu, Yichun Shentu, Jin Yuan, Guofeng Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.19358v1.pdf)  
  Keywords: gaussian splatting, localization, ar, efficient, outdoor  
- **[HoGS: Unified Near and Far Object Reconstruction via Homogeneous Gaussian Splatting](https://arxiv.org/abs/2503.19232v1)**  
  Authors: Xinpeng Liu, Zeyi Huang, Fumio Okura, Yasuyuki Matsushita  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.19232v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://kh129.github.io/hogs/.)  
  Keywords: 3d gaussian, real-time rendering, gaussian splatting, outdoor, geometry, ar, efficient, fast  

### Model Compression

*Showing the latest 50 out of 638 papers*

- **[EG-Gaussian: Epipolar Geometry and Graph Network Enhanced 3D Gaussian Splatting](https://arxiv.org/abs/2504.13540v1)**  
  Authors: Beizhen Zhao, Yifan Zhou, Zijian Wang, Hao Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.13540v1.pdf)  
  Keywords: sparse-view, gaussian splatting, outdoor, geometry, ar, efficient, 3d gaussian  
- **[Volume Encoding Gaussians: Transfer Function-Agnostic 3D Gaussians for Volume Rendering](https://arxiv.org/abs/2504.13339v1)**  
  Authors: Landon Dyken, Andres Sewell, Will Usher, Steve Petruzza, Sidharth Kumar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.13339v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, motion, geometry, ar, efficient, fast  
- **[ODHSR: Online Dense 3D Reconstruction of Humans and Scenes from Monocular Videos](https://arxiv.org/abs/2504.13167v2)**  
  Authors: Zetong Zhang, Manuel Kaufmann, Lixin Xue, Jie Song, Martin R. Oswald  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.13167v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://eth-ait.github.io/ODHSR.)  
  Keywords: gaussian splatting, understanding, neural rendering, tracking, 3d reconstruction, human, deformation, 3d gaussian, ar, efficient  
- **[Training-Free Hierarchical Scene Understanding for Gaussian Splatting with Superpoint Graphs](https://arxiv.org/abs/2504.13153v1)**  
  Authors: Shaohui Dai, Yansong Qu, Zheyan Li, Xinyang Li, Shengchuan Zhang, Liujuan Cao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.13153v1.pdf) | [![GitHub](https://img.shields.io/github/stars/Atrovast/THGS?style=social)](https://github.com/Atrovast/THGS)  
  Keywords: 3d gaussian, gaussian splatting, understanding, geometry, semantic, segmentation, ar, compact, efficient, fast  
- **[CompGS++: Compressed Gaussian Splatting for Static and Dynamic Scene Representation](https://arxiv.org/abs/2504.13022v1)**  
  Authors: Xiangrui Liu, Xinju Wu, Shiqi Wang, Zhu Li, Sam Kwong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.13022v1.pdf)  
  Keywords: gaussian splatting, compression, dynamic, ar, compact  
- **[GSAC: Leveraging Gaussian Splatting for Photorealistic Avatar Creation with Unity Integration](https://arxiv.org/abs/2504.12999v1)**  
  Authors: Rendong Zhang, Alexandra Watkins, Nilanjan Sarkar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.12999v1.pdf)  
  Keywords: lighting, avatar, gaussian splatting, nerf, vr, face, human, efficient, 3d gaussian, ar  
- **[TSGS: Improving Gaussian Splatting for Transparent Surface Reconstruction via Normal and De-lighting Priors](https://arxiv.org/abs/2504.12799v1)**  
  Authors: Mingwei Li, Pu Pang, Hehe Fan, Hua Huang, Yi Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.12799v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://longxiang-ai.github.io/TSGS/.)  
  Keywords: lighting, gaussian splatting, geometry, face, 3d reconstruction, ar, efficient, 3d gaussian  
- **[ARAP-GS: Drag-driven As-Rigid-As-Possible 3D Gaussian Splatting Editing with Diffusion Prior](https://arxiv.org/abs/2504.12788v1)**  
  Authors: Xiao Han, Runze Tian, Yifei Tong, Fenggen Yu, Dingyao Liu, Yan Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.12788v1.pdf)  
  Keywords: gaussian splatting, ar, deformation, 3d gaussian, efficient  
- **[CAGS: Open-Vocabulary 3D Scene Understanding with Context-Aware Gaussian Splatting](https://arxiv.org/abs/2504.11893v1)**  
  Authors: Wei Sun, Yanzhao Zhou, Jianbin Jiao, Yuan Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.11893v1.pdf)  
  Keywords: gaussian splatting, understanding, segmentation, ar, robotics, efficient, 3d gaussian  
- **[EDGS: Eliminating Densification for Efficient Convergence of 3DGS](https://arxiv.org/abs/2504.13204v1)**  
  Authors: Dmytro Kotovenko, Olga Grebenkova, Björn Ommer  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.13204v1.pdf)  
  Keywords: gaussian splatting, motion, geometry, ar, efficient, 3d gaussian, acceleration  

### Quality Enhancement

*Showing the latest 50 out of 270 papers*

- **[CAGE-GS: High-fidelity Cage Based 3D Gaussian Splatting Deformation](https://arxiv.org/abs/2504.12800v1)**  
  Authors: Yifei Tong, Runze Tian, Xiao Han, Dingyao Liu, Fenggen Yu, Yan Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.12800v1.pdf)  
  Keywords: high-fidelity, gaussian splatting, ar, deformation, 3d gaussian  
- **[3DAffordSplat: Efficient Affordance Reasoning with 3D Gaussians](https://arxiv.org/abs/2504.11218v2)**  
  Authors: Zeming Wei, Junyi Lin, Yang Liu, Weixing Chen, Jingzhou Luo, Guanbin Li, Liang Lin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.11218v2.pdf)  
  Keywords: high-fidelity, lighting, head, real-time rendering, gaussian splatting, recognition, human, efficient, 3d gaussian, ar  
- **[MCBlock: Boosting Neural Radiance Field Training Speed by MCTS-based Dynamic-Resolution Ray Sampling](https://arxiv.org/abs/2504.09878v1)**  
  Authors: Yunpeng Tan, Junlin Hao, Jiangkai Wu, Liming Liu, Qingyang Li, Xinggong Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.09878v1.pdf)  
  Keywords: high-fidelity, gaussian splatting, nerf, dynamic, ar, efficient, acceleration  
- **[TextSplat: Text-Guided Semantic Fusion for Generalizable Gaussian Splatting](https://arxiv.org/abs/2504.09588v1)**  
  Authors: Zhicong Wu, Hongbin Xu, Gang Xu, Ping Nie, Zhixin Yan, Jinkai Zheng, Liangqiong Qu, Ming Li, Liqiang Nie  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.09588v1.pdf)  
  Keywords: high-fidelity, gaussian splatting, understanding, semantic, segmentation, 3d reconstruction, ar, 3d gaussian  
- **[A Constrained Optimization Approach for Gaussian Splatting from Coarsely-posed Images and Noisy Lidar Point Clouds](https://arxiv.org/abs/2504.09129v1)**  
  Authors: Jizong Peng, Tze Ho Elden Tse, Kai Xu, Wenchao Gao, Angela Yao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.09129v1.pdf)  
  Keywords: high-fidelity, gaussian splatting, motion, geometry, 3d reconstruction, ar, 3d gaussian  
- **[ContrastiveGaussian: High-Fidelity 3D Generation with Contrastive Learning and Gaussian Splatting](https://arxiv.org/abs/2504.08100v1)**  
  Authors: Junbang Liu, Enpei Huang, Dongxing Mao, Hui Zhang, Xinyuan Song, Yongxin Ni  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.08100v1.pdf)  
  Keywords: gaussian splatting, high-fidelity, ar  
- **[InteractAvatar: Modeling Hand-Face Interaction in Photorealistic Avatars with Deformable Gaussians](https://arxiv.org/abs/2504.07949v1)**  
  Authors: Kefan Chen, Sergiu Oprea, Justin Theiss, Sreyas Mohan, Srinath Sridhar, Aayush Prakash  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.07949v1.pdf)  
  Keywords: shadow, high-fidelity, avatar, head, body, gaussian splatting, geometry, vr, face, dynamic, human, 3d gaussian, ar  
- **[L3GS: Layered 3D Gaussian Splats for Efficient 3D Scene Delivery](https://arxiv.org/abs/2504.05517v1)**  
  Authors: Yi-Zhen Tsai, Xuechen Zhang, Zheng Li, Jiasi Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.05517v1.pdf)  
  Keywords: head, high quality, efficient rendering, ar, efficient, 3d gaussian  
- **[Embracing Dynamics: Dynamics-aware 4D Gaussian Splatting SLAM](https://arxiv.org/abs/2504.04844v1)**  
  Authors: Zhicong Sun, Jacqueline Lo, Jinxing Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.04844v1.pdf)  
  Keywords: high-fidelity, slam, 4d, gaussian splatting, mapping, tracking, dynamic, localization, ar, 3d gaussian  
- **[UAVTwin: Neural Digital Twins for UAVs using Gaussian Splatting](https://arxiv.org/abs/2504.02158v1)**  
  Authors: Jaehoon Choi, Dongki Jung, Yonghan Lee, Sungmin Eum, Dinesh Manocha, Heesung Kwon  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.02158v1.pdf)  
  Keywords: high quality, high-fidelity, gaussian splatting, neural rendering, motion, dynamic, human, 3d gaussian, ar  

### Ray Tracing

- **[DNF-Avatar: Distilling Neural Fields for Real-time Animatable Avatar Relighting](https://arxiv.org/abs/2504.10486v1)**  
  Authors: Zeren Jiang, Shaofei Wang, Siyu Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.10486v1.pdf)  
  Keywords: shadow, lighting, ray tracing, avatar, gaussian splatting, geometry, relighting, human, relightable, fast, ar  
- **[Stochastic Ray Tracing of 3D Transparent Gaussians](https://arxiv.org/abs/2504.06598v2)**  
  Authors: Xin Sun, Iliyan Georgiev, Yun Fei, Miloš Hašan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.06598v2.pdf)  
  Keywords: lighting, ray tracing, gaussian splatting, efficient rendering, relighting, ar, efficient, 3d gaussian, acceleration  
- **[3D Gaussian Particle Approximation of VDB Datasets: A Study for Scientific Visualization](https://arxiv.org/abs/2504.04857v2)**  
  Authors: Isha Sharma, Dieter Schmalstieg  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.04857v2.pdf)  
  Keywords: gaussian splatting, ray marching, animation, dynamic, ar, compact, efficient, 3d gaussian, acceleration  
- **[3D Gaussian Inverse Rendering with Approximated Global Illumination](https://arxiv.org/abs/2504.01358v1)**  
  Authors: Zirui Wu, Jianteng Chen, Laijian Li, Shaoteng Wu, Zhikai Zhu, Kang Xu, Martin R. Oswald, Jie Song  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.01358v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://wuzirui.github.io/gs-ssr.)  
  Keywords: global illumination, lighting, ray tracing, real-time rendering, gaussian splatting, face, ar, illumination, efficient, 3d gaussian  
- **[Real-time Global Illumination for Dynamic 3D Gaussian Scenes](https://arxiv.org/abs/2503.17897v1)**  
  Authors: Chenxiao Hu, Meng Gai, Guoping Wang, Sheng Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.17897v1.pdf)  
  Keywords: global illumination, 3d gaussian, lighting, real-time rendering, light transport, face, dynamic, illumination, fast  
- **[REdiSplats: Ray Tracing for Editable Gaussian Splatting](https://arxiv.org/abs/2503.12284v1)**  
  Authors: Krzysztof Byrski, Grzegorz Wilczyński, Weronika Smolak-Dyżewska, Piotr Borycki, Dawid Baran, Sławomir Tadeja, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.12284v1.pdf)  
  Keywords: shadow, ray tracing, gaussian splatting, neural rendering, reflection, ar, fast, 3d gaussian  
- **[BEAM: Bridging Physically-based Rendering and Gaussian Modeling for Relightable Volumetric Video](https://arxiv.org/abs/2502.08297v1)**  
  Authors: Yu Hong, Yize Wu, Zhehao Shen, Chengcheng Guo, Yuheng Jiang, Yingliang Zhang, Jingyi Yu, Lan Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.08297v1.pdf)  
  Keywords: lighting, ray tracing, 4d, real-time rendering, geometry, tracking, face, dynamic, ar, relightable, efficient  
- **[MeshSplats: Mesh-Based Rendering with Gaussian Splatting Initialization](https://arxiv.org/abs/2502.07754v1)**  
  Authors: Rafał Tobiasz, Grzegorz Wilczyński, Marcin Mazur, Sławomir Tadeja, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.07754v1.pdf)  
  Keywords: shadow, lighting, ray tracing, gaussian splatting, face, reflection  
- **[Scalable 3D Gaussian Splatting-Based RF Signal Spatial Propagation Modeling](https://arxiv.org/abs/2502.01826v1)**  
  Authors: Kang Yang, Gaofeng Dong, Sijie Ji, Wan Du, Mani Srivastava  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.01826v1.pdf)  
  Keywords: ray tracing, gaussian splatting, survey, ar, 3d gaussian  
- **[Radiant Foam: Real-Time Differentiable Ray Tracing](https://arxiv.org/abs/2502.01157v1)**  
  Authors: Shrisudhan Govindarajan, Daniel Rebain, Kwang Moo Yi, Andrea Tagliasacchi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.01157v1.pdf)  
  Keywords: ray tracing, gaussian splatting, light transport, reflection, ar, efficient, acceleration  

### Relighting

*Showing the latest 50 out of 191 papers*

- **[SLAM&Render: A Benchmark for the Intersection Between Neural Rendering, Gaussian Splatting and SLAM](https://arxiv.org/abs/2504.13713v1)**  
  Authors: Samuel Cerezo, Gaetano Meli, Tomás Berriel Martins, Kirill Safronov, Javier Civera  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.13713v1.pdf)  
  Keywords: lighting, slam, gaussian splatting, neural rendering, nerf, mapping, localization, ar, illumination  
- **[Novel Demonstration Generation with Gaussian Splatting Enables Robust One-Shot Manipulation](https://arxiv.org/abs/2504.13175v1)**  
  Authors: Sizhe Yang, Wenye Yu, Jia Zeng, Jun Lv, Kerui Ren, Cewu Lu, Dahua Lin, Jiangmiao Pang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.13175v1.pdf)  
  Keywords: lighting, gaussian splatting, face, ar, 3d gaussian  
- **[Digital Twin Generation from Visual Data: A Survey](https://arxiv.org/abs/2504.13159v1)**  
  Authors: Andrew Melnik, Benjamin Alt, Giang Nguyen, Artur Wilkowski, Maciej Stefańczyk, Qirui Wu, Sinan Harms, Helge Rhodin, Manolis Savva, Michael Beetz  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.13159v1.pdf) | [![GitHub](https://img.shields.io/github/stars/ndrwmlnk/awesome-digital-twins?style=social)](https://github.com/ndrwmlnk/awesome-digital-twins)  
  Keywords: lighting, gaussian splatting, semantic, survey, segmentation, ar, robotics, 3d gaussian  
- **[GSAC: Leveraging Gaussian Splatting for Photorealistic Avatar Creation with Unity Integration](https://arxiv.org/abs/2504.12999v1)**  
  Authors: Rendong Zhang, Alexandra Watkins, Nilanjan Sarkar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.12999v1.pdf)  
  Keywords: lighting, avatar, gaussian splatting, nerf, vr, face, human, efficient, 3d gaussian, ar  
- **[TSGS: Improving Gaussian Splatting for Transparent Surface Reconstruction via Normal and De-lighting Priors](https://arxiv.org/abs/2504.12799v1)**  
  Authors: Mingwei Li, Pu Pang, Hehe Fan, Hua Huang, Yi Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.12799v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://longxiang-ai.github.io/TSGS/.)  
  Keywords: lighting, gaussian splatting, geometry, face, 3d reconstruction, ar, efficient, 3d gaussian  
- **[3DAffordSplat: Efficient Affordance Reasoning with 3D Gaussians](https://arxiv.org/abs/2504.11218v2)**  
  Authors: Zeming Wei, Junyi Lin, Yang Liu, Weixing Chen, Jingzhou Luo, Guanbin Li, Liang Lin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.11218v2.pdf)  
  Keywords: high-fidelity, lighting, head, real-time rendering, gaussian splatting, recognition, human, efficient, 3d gaussian, ar  
- **[GaSLight: Gaussian Splats for Spatially-Varying Lighting in HDR](https://arxiv.org/abs/2504.10809v2)**  
  Authors: Christophe Bolduc, Yannick Hold-Geoffroy, Zhixin Shu, Jean-François Lalonde  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.10809v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://lvsn.github.io/gaslight/)  
  Keywords: ar, lighting, dynamic  
- **[DNF-Avatar: Distilling Neural Fields for Real-time Animatable Avatar Relighting](https://arxiv.org/abs/2504.10486v1)**  
  Authors: Zeren Jiang, Shaofei Wang, Siyu Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.10486v1.pdf)  
  Keywords: shadow, lighting, ray tracing, avatar, gaussian splatting, geometry, relighting, human, relightable, fast, ar  
- **[LL-Gaussian: Low-Light Scene Reconstruction and Enhancement via Gaussian Splatting for Novel View Synthesis](https://arxiv.org/abs/2504.10331v3)**  
  Authors: Hao Sun, Fenggen Yu, Huiyao Xu, Tao Zhang, Changqing Zou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.10331v3.pdf)  
  Keywords: real-time rendering, gaussian splatting, nerf, 3d reconstruction, dynamic, ar, illumination, fast, 3d gaussian  
- **[Cut-and-Splat: Leveraging Gaussian Splatting for Synthetic Data Generation](https://arxiv.org/abs/2504.08473v1)**  
  Authors: Bram Vanherle, Brent Zoomers, Jeroen Put, Frank Van Reeth, Nick Michiels  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.08473v1.pdf)  
  Keywords: gaussian splatting, lighting, segmentation, ar  

### SLAM

*Showing the latest 50 out of 247 papers*

- **[SLAM&Render: A Benchmark for the Intersection Between Neural Rendering, Gaussian Splatting and SLAM](https://arxiv.org/abs/2504.13713v1)**  
  Authors: Samuel Cerezo, Gaetano Meli, Tomás Berriel Martins, Kirill Safronov, Javier Civera  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.13713v1.pdf)  
  Keywords: lighting, slam, gaussian splatting, neural rendering, nerf, mapping, localization, ar, illumination  
- **[ODHSR: Online Dense 3D Reconstruction of Humans and Scenes from Monocular Videos](https://arxiv.org/abs/2504.13167v2)**  
  Authors: Zetong Zhang, Manuel Kaufmann, Lixin Xue, Jie Song, Martin R. Oswald  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.13167v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://eth-ait.github.io/ODHSR.)  
  Keywords: gaussian splatting, understanding, neural rendering, tracking, 3d reconstruction, human, deformation, 3d gaussian, ar, efficient  
- **[SIGMAN:Scaling 3D Human Gaussian Generation with Millions of Assets](https://arxiv.org/abs/2504.06982v1)**  
  Authors: Yuhang Yang, Fengqi Liu, Yixing Lu, Qin Zhao, Pingyu Wu, Wei Zhai, Ran Yi, Yang Cao, Lizhuang Ma, Zheng-Jun Zha, Junting Dong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.06982v1.pdf)  
  Keywords: mapping, human, deformation, 3d gaussian, ar  
- **[Embracing Dynamics: Dynamics-aware 4D Gaussian Splatting SLAM](https://arxiv.org/abs/2504.04844v1)**  
  Authors: Zhicong Sun, Jacqueline Lo, Jinxing Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.04844v1.pdf)  
  Keywords: high-fidelity, slam, 4d, gaussian splatting, mapping, tracking, dynamic, localization, ar, 3d gaussian  
- **[WildGS-SLAM: Monocular Gaussian Splatting SLAM in Dynamic Environments](https://arxiv.org/abs/2504.03886v1)**  
  Authors: Jianhao Zheng, Zihan Zhu, Valentin Bieri, Marc Pollefeys, Songyou Peng, Iro Armeni  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.03886v1.pdf)  
  Keywords: slam, gaussian splatting, mapping, tracking, dynamic, ar, efficient  
- **[MonoGS++: Fast and Accurate Monocular RGB Gaussian SLAM](https://arxiv.org/abs/2504.02437v1)**  
  Authors: Renwu Li, Wenjing Ke, Dong Li, Lu Tian, Emad Barsoum  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.02437v1.pdf)  
  Keywords: 3d gaussian, slam, gaussian splatting, mapping, tracking, face, dynamic, localization, ar, fast  
- **[Luminance-GS: Adapting 3D Gaussian Splatting to Challenging Lighting Conditions with View-Adaptive Curve Adjustment](https://arxiv.org/abs/2504.01503v1)**  
  Authors: Ziteng Cui, Xuangeng Chu, Tatsuya Harada  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.01503v1.pdf)  
  Keywords: lighting, real-time rendering, gaussian splatting, nerf, mapping, ar, 3d gaussian  
- **[Visual Acoustic Fields](https://arxiv.org/abs/2503.24270v2)**  
  Authors: Yuelei Li, Hyunjin Kim, Fangneng Zhan, Ri-Zhao Qiu, Mazeyu Ji, Xiaojun Shan, Xueyan Zou, Paul Liang, Hanspeter Pfister, Xiaolong Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.24270v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://yuelei0428.github.io/projects/Visual-Acoustic-Fields/.)  
  Keywords: gaussian splatting, localization, human, 3d gaussian, ar  
- **[ReasonGrounder: LVLM-Guided Hierarchical Feature Splatting for Open-Vocabulary 3D Visual Grounding and Reasoning](https://arxiv.org/abs/2503.23297v1)**  
  Authors: Zhenyang Liu, Yikai Wang, Sixiao Zheng, Tongying Pan, Longfei Liang, Yanwei Fu, Xiangyang Xue  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.23297v1.pdf)  
  Keywords: gaussian splatting, understanding, semantic, segmentation, localization, ar, robotics, 3d gaussian  
- **[VizFlyt: Perception-centric Pedagogical Framework For Autonomous Aerial Robots](https://arxiv.org/abs/2503.22876v2)**  
  Authors: Kushagra Srivastava, Rutwik Kulkarni, Manoj Velmurugan, Nitin J. Sanket  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.22876v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://pear.wpi.edu/research/vizflyt.html)  
  Keywords: gaussian splatting, localization, ar, robotics, efficient, 3d gaussian  

### Scene Understanding

*Showing the latest 50 out of 298 papers*

- **[ODHSR: Online Dense 3D Reconstruction of Humans and Scenes from Monocular Videos](https://arxiv.org/abs/2504.13167v2)**  
  Authors: Zetong Zhang, Manuel Kaufmann, Lixin Xue, Jie Song, Martin R. Oswald  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.13167v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://eth-ait.github.io/ODHSR.)  
  Keywords: gaussian splatting, understanding, neural rendering, tracking, 3d reconstruction, human, deformation, 3d gaussian, ar, efficient  
- **[Digital Twin Generation from Visual Data: A Survey](https://arxiv.org/abs/2504.13159v1)**  
  Authors: Andrew Melnik, Benjamin Alt, Giang Nguyen, Artur Wilkowski, Maciej Stefańczyk, Qirui Wu, Sinan Harms, Helge Rhodin, Manolis Savva, Michael Beetz  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.13159v1.pdf) | [![GitHub](https://img.shields.io/github/stars/ndrwmlnk/awesome-digital-twins?style=social)](https://github.com/ndrwmlnk/awesome-digital-twins)  
  Keywords: lighting, gaussian splatting, semantic, survey, segmentation, ar, robotics, 3d gaussian  
- **[Training-Free Hierarchical Scene Understanding for Gaussian Splatting with Superpoint Graphs](https://arxiv.org/abs/2504.13153v1)**  
  Authors: Shaohui Dai, Yansong Qu, Zheyan Li, Xinyang Li, Shengchuan Zhang, Liujuan Cao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.13153v1.pdf) | [![GitHub](https://img.shields.io/github/stars/Atrovast/THGS?style=social)](https://github.com/Atrovast/THGS)  
  Keywords: 3d gaussian, gaussian splatting, understanding, geometry, semantic, segmentation, ar, compact, efficient, fast  
- **[Mind2Matter: Creating 3D Models from EEG Signals](https://arxiv.org/abs/2504.11936v2)**  
  Authors: Xia Deng, Shen Chen, Jiale Zhou, Lei Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.11936v2.pdf) | [![GitHub](https://img.shields.io/github/stars/sddwwww/Mind2Matter?style=social)](https://github.com/sddwwww/Mind2Matter)  
  Keywords: semantic, face, 3d reconstruction, ar, 3d gaussian  
- **[CAGS: Open-Vocabulary 3D Scene Understanding with Context-Aware Gaussian Splatting](https://arxiv.org/abs/2504.11893v1)**  
  Authors: Wei Sun, Yanzhao Zhou, Jianbin Jiao, Yuan Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.11893v1.pdf)  
  Keywords: gaussian splatting, understanding, segmentation, ar, robotics, efficient, 3d gaussian  
- **[3DAffordSplat: Efficient Affordance Reasoning with 3D Gaussians](https://arxiv.org/abs/2504.11218v2)**  
  Authors: Zeming Wei, Junyi Lin, Yang Liu, Weixing Chen, Jingzhou Luo, Guanbin Li, Liang Lin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.11218v2.pdf)  
  Keywords: high-fidelity, lighting, head, real-time rendering, gaussian splatting, recognition, human, efficient, 3d gaussian, ar  
- **[Easy3D: A Simple Yet Effective Method for 3D Interactive Segmentation](https://arxiv.org/abs/2504.11024v1)**  
  Authors: Andrea Simonelli, Norman Müller, Peter Kontschieder  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.11024v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://simonelli-andrea.github.io/easy3d.)  
  Keywords: gaussian splatting, lightweight, segmentation, 3d reconstruction, ar, efficient  
- **[TextSplat: Text-Guided Semantic Fusion for Generalizable Gaussian Splatting](https://arxiv.org/abs/2504.09588v1)**  
  Authors: Zhicong Wu, Hongbin Xu, Gang Xu, Ping Nie, Zhixin Yan, Jinkai Zheng, Liangqiong Qu, Ming Li, Liqiang Nie  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.09588v1.pdf)  
  Keywords: high-fidelity, gaussian splatting, understanding, semantic, segmentation, 3d reconstruction, ar, 3d gaussian  
- **[FMLGS: Fast Multilevel Language Embedded Gaussians for Part-level Interactive Agents](https://arxiv.org/abs/2504.08581v1)**  
  Authors: Xin Tan, Yuzhou Ji, He Zhu, Yuan Xie  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.08581v1.pdf)  
  Keywords: 3d gaussian, gaussian splatting, understanding, semantic, face, ar, efficient, fast  
- **[Cut-and-Splat: Leveraging Gaussian Splatting for Synthetic Data Generation](https://arxiv.org/abs/2504.08473v1)**  
  Authors: Bram Vanherle, Brent Zoomers, Jeroen Put, Frank Van Reeth, Nick Michiels  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.08473v1.pdf)  
  Keywords: gaussian splatting, lighting, segmentation, ar  



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