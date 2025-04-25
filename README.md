# Awesome Gaussian Splatting [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of latest research papers, projects and resources related to Gaussian Splatting. Content is automatically updated daily.

> Last Update: 2025-04-25 00:54:16

## Categories

- [3DGS Surveys](#3dgs-surveys) (27 papers) - Survey papers and benchmarks about 3D Gaussian Splatting
- [Acceleration](#acceleration) (481 papers) - Papers about speeding up rendering or training
- [Applications](#applications) (1694 papers) - Papers about specific applications
- [Avatar Generation](#avatar-generation) (572 papers) - Papers about human avatar generation
- [Dynamic Scene](#dynamic-scene) (639 papers) - Papers about dynamic scene reconstruction and rendering
- [Few-shot](#few-shot) (120 papers) - Papers about few-shot or sparse view reconstruction
- [Geometry Reconstruction](#geometry-reconstruction) (548 papers) - Papers about 3D geometry reconstruction
- [Large Scene](#large-scene) (92 papers) - Papers about large-scale scene reconstruction
- [Model Compression](#model-compression) (644 papers) - Papers about model compression and optimization
- [Quality Enhancement](#quality-enhancement) (271 papers) - Papers focusing on improving rendering quality
- [Ray Tracing](#ray-tracing) (39 papers) - Papers about ray tracing and ray casting in Gaussian Splatting
- [Relighting](#relighting) (194 papers) - Papers about relighting and illumination effects in Gaussian Splatting
- [SLAM](#slam) (249 papers) - Papers about SLAM using Gaussian Splatting
- [Scene Understanding](#scene-understanding) (303 papers) - Papers about scene understanding and semantic analysis



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
  Keywords: segmentation, ar, gaussian splatting, survey, 3d gaussian, lighting, robotics, semantic  
- **[A Survey on Event-driven 3D Reconstruction: Development under Different Categories](https://arxiv.org/abs/2503.19753v2)**  
  Authors: Chuanzhi Xu, Haoxian Zhou, Haodong Chen, Vera Chung, Qiang Qu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.19753v2.pdf)  
  Keywords: fast, ar, 3d reconstruction, gaussian splatting, survey, 3d gaussian, lighting, dynamic, motion  
- **[Dynamic Scene Reconstruction: Recent Advance in Real-time Rendering and Streaming](https://arxiv.org/abs/2503.08166v1)**  
  Authors: Jiaxuan Zhu, Hao Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.08166v1.pdf)  
  Keywords: ar, real-time rendering, gaussian splatting, survey, 3d gaussian, dynamic  
- **[Infinite Leagues Under the Sea: Photorealistic 3D Underwater Terrain Generation by Latent Fractal Diffusion Models](https://arxiv.org/abs/2503.06784v1)**  
  Authors: Tianyi Zhang, Weiming Zhi, Joshua Mangelson, Matthew Johnson-Roberson  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.06784v1.pdf)  
  Keywords: ar, geometry, survey, semantic  
- **[Compression in 3D Gaussian Splatting: A Survey of Methods, Trends, and Future Directions](https://arxiv.org/abs/2502.19457v1)**  
  Authors: Muhammad Salman Ali, Chaoning Zhang, Marco Cagnazzo, Giuseppe Valenzise, Enzo Tartaglione, Sung-Ho Bae  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.19457v1.pdf)  
  Keywords: efficient, nerf, compression, ar, real-time rendering, 3d reconstruction, gaussian splatting, 3d gaussian, survey  
- **[Grounding Creativity in Physics: A Brief Survey of Physical Priors in AIGC](https://arxiv.org/abs/2502.07007v1)**  
  Authors: Siwei Meng, Yawei Luo, Ping Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.07007v1.pdf)  
  Keywords: nerf, ar, gaussian splatting, survey, lighting, 4d, deformation, dynamic, motion  
- **[Scalable 3D Gaussian Splatting-Based RF Signal Spatial Propagation Modeling](https://arxiv.org/abs/2502.01826v1)**  
  Authors: Kang Yang, Gaofeng Dong, Sijie Ji, Wan Du, Mani Srivastava  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.01826v1.pdf)  
  Keywords: ar, gaussian splatting, survey, ray tracing, 3d gaussian  
- **[NFL-BA: Improving Endoscopic SLAM with Near-Field Light Bundle Adjustment](https://arxiv.org/abs/2412.13176v2)**  
  Authors: Andrea Dunn Beltran, Daniel Rho, Stephen Pizer, Marc Niethammer, Roni Sengupta  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.13176v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://asdunnbe.github.io/NFL-BA/)  
  Keywords: mapping, outdoor, localization, ar, tracking, survey, lighting, face, slam, dynamic, geometry  
- **[Adversarial Attacks Using Differentiable Rendering: A Survey](https://arxiv.org/abs/2411.09749v1)**  
  Authors: Matthew Hull, Chao Zhang, Zsolt Kira, Duen Horng Chau  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.09749v1.pdf)  
  Keywords: recognition, ar, gaussian splatting, survey, 3d gaussian, illumination  
- **[Neural Fields in Robotics: A Survey](https://arxiv.org/abs/2410.20220v1)**  
  Authors: Muhammad Zubair Irshad, Mauro Comi, Yen-Chen Lin, Nick Heppert, Abhinav Valada, Rares Ambrus, Zsolt Kira, Jonathan Tremblay  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.20220v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://robonerf.github.io)  
  Keywords: geometry, nerf, compact, ar, 3d reconstruction, gaussian splatting, survey, lighting, dynamic, autonomous driving, robotics, high-fidelity, semantic  

### Acceleration

*Showing the latest 50 out of 481 papers*

- **[StyleMe3D: Stylization with Disentangled Priors by Multiple Encoders on 3D Gaussians](https://arxiv.org/abs/2504.15281v1)**  
  Authors: Cailin Zhuang, Yaoqi Hu, Xuanyang Zhang, Wei Cheng, Jiacheng Bao, Shengqi Liu, Yiying Yang, Xianfang Zeng, Gang Yu, Ming Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.15281v1.pdf)  
  Keywords: nerf, ar, real-time rendering, gaussian splatting, 3d gaussian, lighting, human, dynamic, quality enhancement, semantic  
- **[Immersive Teleoperation Framework for Locomanipulation Tasks](https://arxiv.org/abs/2504.15229v1)**  
  Authors: Takuya Boehringer, Jonathan Embley-Riches, Karim Hammoud, Valerio Modugno, Dimitrios Kanoulas  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.15229v1.pdf)  
  Keywords: vr, fast, ar, gaussian splatting, lighting, face  
- **[3D Gaussian Head Avatars with Expressive Dynamic Appearances by Compact Tensorial Representations](https://arxiv.org/abs/2504.14967v1)**  
  Authors: Yating Wang, Xuan Wang, Ran Yi, Yanbo Fan, Jichen Hu, Jingcheng Zhu, Lizhuang Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.14967v1.pdf)  
  Keywords: compact, ar, real-time rendering, lightweight, avatar, 3d gaussian, dynamic, face, head  
- **[Volume Encoding Gaussians: Transfer Function-Agnostic 3D Gaussians for Volume Rendering](https://arxiv.org/abs/2504.13339v1)**  
  Authors: Landon Dyken, Andres Sewell, Will Usher, Steve Petruzza, Sidharth Kumar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.13339v1.pdf)  
  Keywords: efficient, fast, ar, gaussian splatting, 3d gaussian, geometry, motion  
- **[Training-Free Hierarchical Scene Understanding for Gaussian Splatting with Superpoint Graphs](https://arxiv.org/abs/2504.13153v1)**  
  Authors: Shaohui Dai, Yansong Qu, Zheyan Li, Xinyang Li, Shengchuan Zhang, Liujuan Cao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.13153v1.pdf) | [![GitHub](https://img.shields.io/github/stars/Atrovast/THGS?style=social)](https://github.com/Atrovast/THGS)  
  Keywords: efficient, understanding, fast, compact, segmentation, ar, gaussian splatting, 3d gaussian, geometry, semantic  
- **[Second-order Optimization of Gaussian Splats with Importance Sampling](https://arxiv.org/abs/2504.12905v1)**  
  Authors: Hamza Pehlivan, Andrea Boscolo Camiletto, Lin Geng Foo, Marc Habermann, Christian Theobalt  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.12905v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://vcai.mpi-inf.mpg.de/projects/LM-IS)  
  Keywords: ar, gaussian splatting, fast, 3d gaussian  
- **[EDGS: Eliminating Densification for Efficient Convergence of 3DGS](https://arxiv.org/abs/2504.13204v1)**  
  Authors: Dmytro Kotovenko, Olga Grebenkova, Björn Ommer  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.13204v1.pdf)  
  Keywords: efficient, acceleration, ar, gaussian splatting, 3d gaussian, geometry, motion  
- **[3DAffordSplat: Efficient Affordance Reasoning with 3D Gaussians](https://arxiv.org/abs/2504.11218v2)**  
  Authors: Zeming Wei, Junyi Lin, Yang Liu, Weixing Chen, Jingzhou Luo, Guanbin Li, Liang Lin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.11218v2.pdf)  
  Keywords: efficient, recognition, ar, real-time rendering, gaussian splatting, 3d gaussian, lighting, human, high-fidelity, head  
- **[3D Gabor Splatting: Reconstruction of High-frequency Surface Texture using Gabor Noise](https://arxiv.org/abs/2504.11003v1)**  
  Authors: Haato Watanabe, Kenji Tojo, Nobuyuki Umetani  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.11003v1.pdf)  
  Keywords: fast, ar, lightweight, gaussian splatting, 3d gaussian, face  
- **[DNF-Avatar: Distilling Neural Fields for Real-time Animatable Avatar Relighting](https://arxiv.org/abs/2504.10486v1)**  
  Authors: Zeren Jiang, Shaofei Wang, Siyu Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.10486v1.pdf)  
  Keywords: fast, shadow, relightable, avatar, gaussian splatting, ar, ray tracing, lighting, relighting, human, geometry  

### Applications

*Showing the latest 50 out of 1694 papers*

- **[Gaussian Splatting is an Effective Data Generator for 3D Object Detection](https://arxiv.org/abs/2504.16740v1)**  
  Authors: Farhad G. Zanjani, Davide Abati, Auke Wiggers, Dimitris Kalatzis, Jens Petersen, Hong Cai, Amirhossein Habibian  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.16740v1.pdf)  
  Keywords: efficient, ar, 3d reconstruction, gaussian splatting, autonomous driving  
- **[PIN-WM: Learning Physics-INformed World Models for Non-Prehensile Manipulation](https://arxiv.org/abs/2504.16693v1)**  
  Authors: Wenxuan Li, Hang Zhao, Zhiyuan Yu, Yu Du, Qin Zou, Ruizhen Hu, Kai Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.16693v1.pdf)  
  Keywords: efficient, few-shot, ar, gaussian splatting, body, dynamic  
- **[HUG: Hierarchical Urban Gaussian Splatting with Block-Based Reconstruction](https://arxiv.org/abs/2504.16606v1)**  
  Authors: Zhongtao Wang, Mai Su, Huishan Au, Yilong Li, Xizhe Cao, Chengwei Pan, Yisong Chen, Guoping Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.16606v1.pdf)  
  Keywords: efficient, urban scene, ar, gaussian splatting, 3d gaussian  
- **[ToF-Splatting: Dense SLAM using Sparse Time-of-Flight Depth and Multi-Frame Integration](https://arxiv.org/abs/2504.16545v1)**  
  Authors: Andrea Conti, Matteo Poggi, Valerio Cambareri, Martin R. Oswald, Stefano Mattoccia  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.16545v1.pdf)  
  Keywords: efficient, mapping, vr, ar, gaussian splatting, tracking, 3d gaussian, slam, geometry  
- **[Text-based Animatable 3D Avatars with Morphable Model Alignment](https://arxiv.org/abs/2504.15835v1)**  
  Authors: Yiqian Wu, Malte Prinzler, Xiaogang Jin, Siyu Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.15835v1.pdf)  
  Keywords: ar, animation, avatar, dynamic, semantic, geometry, head  
- **[StyleMe3D: Stylization with Disentangled Priors by Multiple Encoders on 3D Gaussians](https://arxiv.org/abs/2504.15281v1)**  
  Authors: Cailin Zhuang, Yaoqi Hu, Xuanyang Zhang, Wei Cheng, Jiacheng Bao, Shengqi Liu, Yiying Yang, Xianfang Zeng, Gang Yu, Ming Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.15281v1.pdf)  
  Keywords: nerf, ar, real-time rendering, gaussian splatting, 3d gaussian, lighting, human, dynamic, quality enhancement, semantic  
- **[Immersive Teleoperation Framework for Locomanipulation Tasks](https://arxiv.org/abs/2504.15229v1)**  
  Authors: Takuya Boehringer, Jonathan Embley-Riches, Karim Hammoud, Valerio Modugno, Dimitrios Kanoulas  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.15229v1.pdf)  
  Keywords: vr, fast, ar, gaussian splatting, lighting, face  
- **[MoBGS: Motion Deblurring Dynamic 3D Gaussian Splatting for Blurry Monocular Video](https://arxiv.org/abs/2504.15122v1)**  
  Authors: Minh-Quan Viet Bui, Jongmin Park, Juan Luis Gonzalez Bello, Jaeho Moon, Jihyong Oh, Munchurl Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.15122v1.pdf)  
  Keywords: ar, gaussian splatting, 3d gaussian, 4d, dynamic, motion  
- **[3D Gaussian Head Avatars with Expressive Dynamic Appearances by Compact Tensorial Representations](https://arxiv.org/abs/2504.14967v1)**  
  Authors: Yating Wang, Xuan Wang, Ran Yi, Yanbo Fan, Jichen Hu, Jingcheng Zhu, Lizhuang Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.14967v1.pdf)  
  Keywords: compact, ar, real-time rendering, lightweight, avatar, 3d gaussian, dynamic, face, head  
- **[IXGS-Intraoperative 3D Reconstruction from Sparse, Arbitrarily Posed Real X-rays](https://arxiv.org/abs/2504.14699v1)**  
  Authors: Sascha Jecklin, Aidana Massalimova, Ruyi Zha, Lilian Calvet, Christoph J. Laux, Mazda Farshad, Philipp Fürnstahl  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.14699v1.pdf)  
  Keywords: ar, 3d reconstruction, gaussian splatting, sparse-view  

### Avatar Generation

*Showing the latest 50 out of 572 papers*

- **[PIN-WM: Learning Physics-INformed World Models for Non-Prehensile Manipulation](https://arxiv.org/abs/2504.16693v1)**  
  Authors: Wenxuan Li, Hang Zhao, Zhiyuan Yu, Yu Du, Qin Zou, Ruizhen Hu, Kai Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.16693v1.pdf)  
  Keywords: efficient, few-shot, ar, gaussian splatting, body, dynamic  
- **[Text-based Animatable 3D Avatars with Morphable Model Alignment](https://arxiv.org/abs/2504.15835v1)**  
  Authors: Yiqian Wu, Malte Prinzler, Xiaogang Jin, Siyu Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.15835v1.pdf)  
  Keywords: ar, animation, avatar, dynamic, semantic, geometry, head  
- **[StyleMe3D: Stylization with Disentangled Priors by Multiple Encoders on 3D Gaussians](https://arxiv.org/abs/2504.15281v1)**  
  Authors: Cailin Zhuang, Yaoqi Hu, Xuanyang Zhang, Wei Cheng, Jiacheng Bao, Shengqi Liu, Yiying Yang, Xianfang Zeng, Gang Yu, Ming Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.15281v1.pdf)  
  Keywords: nerf, ar, real-time rendering, gaussian splatting, 3d gaussian, lighting, human, dynamic, quality enhancement, semantic  
- **[Immersive Teleoperation Framework for Locomanipulation Tasks](https://arxiv.org/abs/2504.15229v1)**  
  Authors: Takuya Boehringer, Jonathan Embley-Riches, Karim Hammoud, Valerio Modugno, Dimitrios Kanoulas  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.15229v1.pdf)  
  Keywords: vr, fast, ar, gaussian splatting, lighting, face  
- **[3D Gaussian Head Avatars with Expressive Dynamic Appearances by Compact Tensorial Representations](https://arxiv.org/abs/2504.14967v1)**  
  Authors: Yating Wang, Xuan Wang, Ran Yi, Yanbo Fan, Jichen Hu, Jingcheng Zhu, Lizhuang Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.14967v1.pdf)  
  Keywords: compact, ar, real-time rendering, lightweight, avatar, 3d gaussian, dynamic, face, head  
- **[SEGA: Drivable 3D Gaussian Head Avatar from a Single Image](https://arxiv.org/abs/2504.14373v2)**  
  Authors: Chen Guo, Zhuo Su, Jian Wang, Shuang Li, Xu Chang, Zhaohu Li, Yang Zhao, Guidong Wang, Ruqi Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.14373v2.pdf)  
  Keywords: efficient, ar, animation, neural rendering, gaussian splatting, avatar, 3d gaussian, human, dynamic, head  
- **[Novel Demonstration Generation with Gaussian Splatting Enables Robust One-Shot Manipulation](https://arxiv.org/abs/2504.13175v1)**  
  Authors: Sizhe Yang, Wenye Yu, Jia Zeng, Jun Lv, Kerui Ren, Cewu Lu, Dahua Lin, Jiangmiao Pang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.13175v1.pdf)  
  Keywords: ar, gaussian splatting, 3d gaussian, lighting, face  
- **[ODHSR: Online Dense 3D Reconstruction of Humans and Scenes from Monocular Videos](https://arxiv.org/abs/2504.13167v2)**  
  Authors: Zetong Zhang, Manuel Kaufmann, Lixin Xue, Jie Song, Martin R. Oswald  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.13167v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://eth-ait.github.io/ODHSR.)  
  Keywords: efficient, understanding, ar, neural rendering, 3d reconstruction, gaussian splatting, 3d gaussian, tracking, human, deformation  
- **[GSAC: Leveraging Gaussian Splatting for Photorealistic Avatar Creation with Unity Integration](https://arxiv.org/abs/2504.12999v1)**  
  Authors: Rendong Zhang, Alexandra Watkins, Nilanjan Sarkar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.12999v1.pdf)  
  Keywords: efficient, vr, nerf, ar, avatar, gaussian splatting, 3d gaussian, lighting, human, face  
- **[AAA-Gaussians: Anti-Aliased and Artifact-Free 3D Gaussian Rendering](https://arxiv.org/abs/2504.12811v1)**  
  Authors: Michael Steiner, Thomas Köhler, Lukas Radl, Felix Windisch, Dieter Schmalstieg, Markus Steinberger  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.12811v1.pdf)  
  Keywords: ar, 3d reconstruction, gaussian splatting, 3d gaussian, face  

### Dynamic Scene

*Showing the latest 50 out of 639 papers*

- **[PIN-WM: Learning Physics-INformed World Models for Non-Prehensile Manipulation](https://arxiv.org/abs/2504.16693v1)**  
  Authors: Wenxuan Li, Hang Zhao, Zhiyuan Yu, Yu Du, Qin Zou, Ruizhen Hu, Kai Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.16693v1.pdf)  
  Keywords: efficient, few-shot, ar, gaussian splatting, body, dynamic  
- **[Text-based Animatable 3D Avatars with Morphable Model Alignment](https://arxiv.org/abs/2504.15835v1)**  
  Authors: Yiqian Wu, Malte Prinzler, Xiaogang Jin, Siyu Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.15835v1.pdf)  
  Keywords: ar, animation, avatar, dynamic, semantic, geometry, head  
- **[StyleMe3D: Stylization with Disentangled Priors by Multiple Encoders on 3D Gaussians](https://arxiv.org/abs/2504.15281v1)**  
  Authors: Cailin Zhuang, Yaoqi Hu, Xuanyang Zhang, Wei Cheng, Jiacheng Bao, Shengqi Liu, Yiying Yang, Xianfang Zeng, Gang Yu, Ming Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.15281v1.pdf)  
  Keywords: nerf, ar, real-time rendering, gaussian splatting, 3d gaussian, lighting, human, dynamic, quality enhancement, semantic  
- **[MoBGS: Motion Deblurring Dynamic 3D Gaussian Splatting for Blurry Monocular Video](https://arxiv.org/abs/2504.15122v1)**  
  Authors: Minh-Quan Viet Bui, Jongmin Park, Juan Luis Gonzalez Bello, Jaeho Moon, Jihyong Oh, Munchurl Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.15122v1.pdf)  
  Keywords: ar, gaussian splatting, 3d gaussian, 4d, dynamic, motion  
- **[3D Gaussian Head Avatars with Expressive Dynamic Appearances by Compact Tensorial Representations](https://arxiv.org/abs/2504.14967v1)**  
  Authors: Yating Wang, Xuan Wang, Ran Yi, Yanbo Fan, Jichen Hu, Jingcheng Zhu, Lizhuang Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.14967v1.pdf)  
  Keywords: compact, ar, real-time rendering, lightweight, avatar, 3d gaussian, dynamic, face, head  
- **[SEGA: Drivable 3D Gaussian Head Avatar from a Single Image](https://arxiv.org/abs/2504.14373v2)**  
  Authors: Chen Guo, Zhuo Su, Jian Wang, Shuang Li, Xu Chang, Zhaohu Li, Yang Zhao, Guidong Wang, Ruqi Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.14373v2.pdf)  
  Keywords: efficient, ar, animation, neural rendering, gaussian splatting, avatar, 3d gaussian, human, dynamic, head  
- **[Volume Encoding Gaussians: Transfer Function-Agnostic 3D Gaussians for Volume Rendering](https://arxiv.org/abs/2504.13339v1)**  
  Authors: Landon Dyken, Andres Sewell, Will Usher, Steve Petruzza, Sidharth Kumar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.13339v1.pdf)  
  Keywords: efficient, fast, ar, gaussian splatting, 3d gaussian, geometry, motion  
- **[ODHSR: Online Dense 3D Reconstruction of Humans and Scenes from Monocular Videos](https://arxiv.org/abs/2504.13167v2)**  
  Authors: Zetong Zhang, Manuel Kaufmann, Lixin Xue, Jie Song, Martin R. Oswald  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.13167v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://eth-ait.github.io/ODHSR.)  
  Keywords: efficient, understanding, ar, neural rendering, 3d reconstruction, gaussian splatting, 3d gaussian, tracking, human, deformation  
- **[CompGS++: Compressed Gaussian Splatting for Static and Dynamic Scene Representation](https://arxiv.org/abs/2504.13022v1)**  
  Authors: Xiangrui Liu, Xinju Wu, Shiqi Wang, Zhu Li, Sam Kwong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.13022v1.pdf)  
  Keywords: compact, compression, ar, gaussian splatting, dynamic  
- **[CAGE-GS: High-fidelity Cage Based 3D Gaussian Splatting Deformation](https://arxiv.org/abs/2504.12800v1)**  
  Authors: Yifei Tong, Runze Tian, Xiao Han, Dingyao Liu, Fenggen Yu, Yan Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.12800v1.pdf)  
  Keywords: ar, gaussian splatting, 3d gaussian, deformation, high-fidelity  

### Few-shot

*Showing the latest 50 out of 120 papers*

- **[PIN-WM: Learning Physics-INformed World Models for Non-Prehensile Manipulation](https://arxiv.org/abs/2504.16693v1)**  
  Authors: Wenxuan Li, Hang Zhao, Zhiyuan Yu, Yu Du, Qin Zou, Ruizhen Hu, Kai Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.16693v1.pdf)  
  Keywords: efficient, few-shot, ar, gaussian splatting, body, dynamic  
- **[IXGS-Intraoperative 3D Reconstruction from Sparse, Arbitrarily Posed Real X-rays](https://arxiv.org/abs/2504.14699v1)**  
  Authors: Sascha Jecklin, Aidana Massalimova, Ruyi Zha, Lilian Calvet, Christoph J. Laux, Mazda Farshad, Philipp Fürnstahl  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.14699v1.pdf)  
  Keywords: ar, 3d reconstruction, gaussian splatting, sparse-view  
- **[VGNC: Reducing the Overfitting of Sparse-view 3DGS via Validation-guided Gaussian Number Control](https://arxiv.org/abs/2504.14548v1)**  
  Authors: Lifeng Lin, Rongfeng Lu, Quan Chen, Haofan Ren, Ming Lu, Yaoqi Sun, Chenggang Yan, Anke Xue  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.14548v1.pdf)  
  Keywords: sparse-view, ar, 3d reconstruction, gaussian splatting, 3d gaussian  
- **[EG-Gaussian: Epipolar Geometry and Graph Network Enhanced 3D Gaussian Splatting](https://arxiv.org/abs/2504.13540v1)**  
  Authors: Beizhen Zhao, Yifan Zhou, Zijian Wang, Hao Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.13540v1.pdf)  
  Keywords: efficient, outdoor, sparse-view, ar, gaussian splatting, 3d gaussian, geometry  
- **[DropoutGS: Dropping Out Gaussians for Better Sparse-view Rendering](https://arxiv.org/abs/2504.09491v1)**  
  Authors: Yexing Xu, Longguang Wang, Minglin Chen, Sheng Ao, Li Li, Yulan Guo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.09491v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://xuyx55.github.io/DropoutGS/.)  
  Keywords: sparse-view, ar, gaussian splatting, sparse view, 3d gaussian  
- **[GIGA: Generalizable Sparse Image-driven Gaussian Avatars](https://arxiv.org/abs/2504.07144v1)**  
  Authors: Anton Zubekhin, Heming Zhu, Paulo Gotardo, Thabo Beeler, Marc Habermann, Christian Theobalt  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.07144v1.pdf)  
  Keywords: sparse-view, ar, avatar, 3d gaussian, body, human, head  
- **[DropGaussian: Structural Regularization for Sparse-view Gaussian Splatting](https://arxiv.org/abs/2504.00773v1)**  
  Authors: Hyunwoo Park, Gun Ryu, Wonjun Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.00773v1.pdf) | [![GitHub](https://img.shields.io/github/stars/DCVL-3D/DropGaussian?style=social)](https://github.com/DCVL-3D/DropGaussian)  
  Keywords: fast, sparse-view, ar, gaussian splatting, 3d gaussian, face  
- **[Coca-Splat: Collaborative Optimization for Camera Parameters and 3D Gaussians](https://arxiv.org/abs/2504.00639v1)**  
  Authors: Jiamin Wu, Hongyang Li, Xiaoke Jiang, Yuan Yao, Lei Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.00639v1.pdf)  
  Keywords: ar, sparse view, 3d gaussian  
- **[Distilling Multi-view Diffusion Models into 3D Generators](https://arxiv.org/abs/2504.00457v3)**  
  Authors: Hao Qin, Luyuan Chen, Ming Kong, Mengxu Lu, Qiang Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.00457v3.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://qinbaigao.github.io/DD3G_project/)  
  Keywords: efficient, sparse-view, ar, gaussian splatting, 3d gaussian  
- **[Free360: Layered Gaussian Splatting for Unbounded 360-Degree View Synthesis from Extremely Sparse and Unposed Views](https://arxiv.org/abs/2503.24382v1)**  
  Authors: Chong Bao, Xiyu Zhang, Zehao Yu, Jiale Shi, Guofeng Zhang, Songyou Peng, Zhaopeng Cui  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.24382v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://zju3dv.github.io/free360/)  
  Keywords: sparse-view, ar, neural rendering, 3d reconstruction, gaussian splatting, face, geometry  

### Geometry Reconstruction

*Showing the latest 50 out of 548 papers*

- **[Gaussian Splatting is an Effective Data Generator for 3D Object Detection](https://arxiv.org/abs/2504.16740v1)**  
  Authors: Farhad G. Zanjani, Davide Abati, Auke Wiggers, Dimitris Kalatzis, Jens Petersen, Hong Cai, Amirhossein Habibian  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.16740v1.pdf)  
  Keywords: efficient, ar, 3d reconstruction, gaussian splatting, autonomous driving  
- **[ToF-Splatting: Dense SLAM using Sparse Time-of-Flight Depth and Multi-Frame Integration](https://arxiv.org/abs/2504.16545v1)**  
  Authors: Andrea Conti, Matteo Poggi, Valerio Cambareri, Martin R. Oswald, Stefano Mattoccia  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.16545v1.pdf)  
  Keywords: efficient, mapping, vr, ar, gaussian splatting, tracking, 3d gaussian, slam, geometry  
- **[Text-based Animatable 3D Avatars with Morphable Model Alignment](https://arxiv.org/abs/2504.15835v1)**  
  Authors: Yiqian Wu, Malte Prinzler, Xiaogang Jin, Siyu Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.15835v1.pdf)  
  Keywords: ar, animation, avatar, dynamic, semantic, geometry, head  
- **[IXGS-Intraoperative 3D Reconstruction from Sparse, Arbitrarily Posed Real X-rays](https://arxiv.org/abs/2504.14699v1)**  
  Authors: Sascha Jecklin, Aidana Massalimova, Ruyi Zha, Lilian Calvet, Christoph J. Laux, Mazda Farshad, Philipp Fürnstahl  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.14699v1.pdf)  
  Keywords: ar, 3d reconstruction, gaussian splatting, sparse-view  
- **[RoboOcc: Enhancing the Geometric and Semantic Scene Understanding for Robots](https://arxiv.org/abs/2504.14604v1)**  
  Authors: Zhang Zhang, Qiang Zhang, Wei Cui, Shuai Shi, Yijie Guo, Gang Han, Wen Zhao, Hengle Ren, Renjing Xu, Jian Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.14604v1.pdf)  
  Keywords: understanding, ar, 3d gaussian, geometry, semantic  
- **[VGNC: Reducing the Overfitting of Sparse-view 3DGS via Validation-guided Gaussian Number Control](https://arxiv.org/abs/2504.14548v1)**  
  Authors: Lifeng Lin, Rongfeng Lu, Quan Chen, Haofan Ren, Ming Lu, Yaoqi Sun, Chenggang Yan, Anke Xue  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.14548v1.pdf)  
  Keywords: sparse-view, ar, 3d reconstruction, gaussian splatting, 3d gaussian  
- **[EG-Gaussian: Epipolar Geometry and Graph Network Enhanced 3D Gaussian Splatting](https://arxiv.org/abs/2504.13540v1)**  
  Authors: Beizhen Zhao, Yifan Zhou, Zijian Wang, Hao Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.13540v1.pdf)  
  Keywords: efficient, outdoor, sparse-view, ar, gaussian splatting, 3d gaussian, geometry  
- **[Volume Encoding Gaussians: Transfer Function-Agnostic 3D Gaussians for Volume Rendering](https://arxiv.org/abs/2504.13339v1)**  
  Authors: Landon Dyken, Andres Sewell, Will Usher, Steve Petruzza, Sidharth Kumar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.13339v1.pdf)  
  Keywords: efficient, fast, ar, gaussian splatting, 3d gaussian, geometry, motion  
- **[ODHSR: Online Dense 3D Reconstruction of Humans and Scenes from Monocular Videos](https://arxiv.org/abs/2504.13167v2)**  
  Authors: Zetong Zhang, Manuel Kaufmann, Lixin Xue, Jie Song, Martin R. Oswald  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.13167v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://eth-ait.github.io/ODHSR.)  
  Keywords: efficient, understanding, ar, neural rendering, 3d reconstruction, gaussian splatting, 3d gaussian, tracking, human, deformation  
- **[Training-Free Hierarchical Scene Understanding for Gaussian Splatting with Superpoint Graphs](https://arxiv.org/abs/2504.13153v1)**  
  Authors: Shaohui Dai, Yansong Qu, Zheyan Li, Xinyang Li, Shengchuan Zhang, Liujuan Cao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.13153v1.pdf) | [![GitHub](https://img.shields.io/github/stars/Atrovast/THGS?style=social)](https://github.com/Atrovast/THGS)  
  Keywords: efficient, understanding, fast, compact, segmentation, ar, gaussian splatting, 3d gaussian, geometry, semantic  

### Large Scene

*Showing the latest 50 out of 92 papers*

- **[HUG: Hierarchical Urban Gaussian Splatting with Block-Based Reconstruction](https://arxiv.org/abs/2504.16606v1)**  
  Authors: Zhongtao Wang, Mai Su, Huishan Au, Yilong Li, Xizhe Cao, Chengwei Pan, Yisong Chen, Guoping Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.16606v1.pdf)  
  Keywords: efficient, urban scene, ar, gaussian splatting, 3d gaussian  
- **[EG-Gaussian: Epipolar Geometry and Graph Network Enhanced 3D Gaussian Splatting](https://arxiv.org/abs/2504.13540v1)**  
  Authors: Beizhen Zhao, Yifan Zhou, Zijian Wang, Hao Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.13540v1.pdf)  
  Keywords: efficient, outdoor, sparse-view, ar, gaussian splatting, 3d gaussian, geometry  
- **[You Need a Transition Plane: Bridging Continuous Panoramic 3D Reconstruction with Perspective Gaussian Splatting](https://arxiv.org/abs/2504.09062v1)**  
  Authors: Zhijie Shen, Chunyu Lin, Shujuan Huang, Lang Nie, Kang Liao, Yao Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.09062v1.pdf) | [![GitHub](https://img.shields.io/github/stars/zhijieshen-bjtu/TPGS?style=social)](https://github.com/zhijieshen-bjtu/TPGS)  
  Keywords: outdoor, ar, 3d reconstruction, gaussian splatting, 3d gaussian, face  
- **[FIORD: A Fisheye Indoor-Outdoor Dataset with LIDAR Ground Truth for 3D Scene Reconstruction and Benchmarking](https://arxiv.org/abs/2504.01732v2)**  
  Authors: Ulas Gunes, Matias Turkulainen, Xuqian Ren, Arno Solin, Juho Kannala, Esa Rahtu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.01732v2.pdf)  
  Keywords: nerf, outdoor, reflection, ar, gaussian splatting, motion  
- **[UnIRe: Unsupervised Instance Decomposition for Dynamic Urban Scene Reconstruction](https://arxiv.org/abs/2504.00763v1)**  
  Authors: Yunxuan Mao, Rong Xiong, Yue Wang, Yiyi Liao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.00763v1.pdf)  
  Keywords: urban scene, ar, gaussian splatting, 3d gaussian, 4d, dynamic, autonomous driving  
- **[RainyGS: Efficient Rain Synthesis with Physically-Based Gaussian Splatting](https://arxiv.org/abs/2503.21442v2)**  
  Authors: Qiyu Dai, Xingyu Ni, Qianfan Shen, Wenzheng Chen, Baoquan Chen, Mengyu Chu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.21442v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://pku-vcl-geometry.github.io/RainyGS/)  
  Keywords: efficient, geometry, nerf, reflection, fast, outdoor, ar, gaussian splatting, dynamic, high-fidelity  
- **[StyledStreets: Multi-style Street Simulator with Spatial and Temporal Consistency](https://arxiv.org/abs/2503.21104v1)**  
  Authors: Yuyin Chen, Yida Wang, Xueyang Zhang, Kun Zhan, Peng Jia, Yifei Zhan, Xianpeng Lang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.21104v1.pdf)  
  Keywords: urban scene, ar, gaussian splatting, dynamic, geometry, motion  
- **[EVolSplat: Efficient Volume-based Gaussian Splatting for Urban View Synthesis](https://arxiv.org/abs/2503.20168v1)**  
  Authors: Sheng Miao, Jiaxin Huang, Dongfeng Bai, Xu Yan, Hongyu Zhou, Yue Wang, Bingbing Liu, Andreas Geiger, Yiyi Liao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.20168v1.pdf)  
  Keywords: efficient, urban scene, nerf, fast, ar, real-time rendering, gaussian splatting, 3d gaussian, autonomous driving  
- **[SparseGS-W: Sparse-View 3D Gaussian Splatting in the Wild with Generative Priors](https://arxiv.org/abs/2503.19452v1)**  
  Authors: Yiqing Li, Xuan Wang, Jiawei Wu, Yikun Ma, Zhi Jin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.19452v1.pdf)  
  Keywords: outdoor, sparse-view, ar, gaussian splatting, 3d gaussian, illumination  
- **[From Sparse to Dense: Camera Relocalization with Scene-Specific Detector from Feature Gaussian Splatting](https://arxiv.org/abs/2503.19358v1)**  
  Authors: Zhiwei Huang, Hailin Yu, Yichun Shentu, Jin Yuan, Guofeng Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.19358v1.pdf)  
  Keywords: efficient, outdoor, localization, ar, gaussian splatting  

### Model Compression

*Showing the latest 50 out of 644 papers*

- **[Gaussian Splatting is an Effective Data Generator for 3D Object Detection](https://arxiv.org/abs/2504.16740v1)**  
  Authors: Farhad G. Zanjani, Davide Abati, Auke Wiggers, Dimitris Kalatzis, Jens Petersen, Hong Cai, Amirhossein Habibian  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.16740v1.pdf)  
  Keywords: efficient, ar, 3d reconstruction, gaussian splatting, autonomous driving  
- **[PIN-WM: Learning Physics-INformed World Models for Non-Prehensile Manipulation](https://arxiv.org/abs/2504.16693v1)**  
  Authors: Wenxuan Li, Hang Zhao, Zhiyuan Yu, Yu Du, Qin Zou, Ruizhen Hu, Kai Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.16693v1.pdf)  
  Keywords: efficient, few-shot, ar, gaussian splatting, body, dynamic  
- **[HUG: Hierarchical Urban Gaussian Splatting with Block-Based Reconstruction](https://arxiv.org/abs/2504.16606v1)**  
  Authors: Zhongtao Wang, Mai Su, Huishan Au, Yilong Li, Xizhe Cao, Chengwei Pan, Yisong Chen, Guoping Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.16606v1.pdf)  
  Keywords: efficient, urban scene, ar, gaussian splatting, 3d gaussian  
- **[ToF-Splatting: Dense SLAM using Sparse Time-of-Flight Depth and Multi-Frame Integration](https://arxiv.org/abs/2504.16545v1)**  
  Authors: Andrea Conti, Matteo Poggi, Valerio Cambareri, Martin R. Oswald, Stefano Mattoccia  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.16545v1.pdf)  
  Keywords: efficient, mapping, vr, ar, gaussian splatting, tracking, 3d gaussian, slam, geometry  
- **[3D Gaussian Head Avatars with Expressive Dynamic Appearances by Compact Tensorial Representations](https://arxiv.org/abs/2504.14967v1)**  
  Authors: Yating Wang, Xuan Wang, Ran Yi, Yanbo Fan, Jichen Hu, Jingcheng Zhu, Lizhuang Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.14967v1.pdf)  
  Keywords: compact, ar, real-time rendering, lightweight, avatar, 3d gaussian, dynamic, face, head  
- **[SEGA: Drivable 3D Gaussian Head Avatar from a Single Image](https://arxiv.org/abs/2504.14373v2)**  
  Authors: Chen Guo, Zhuo Su, Jian Wang, Shuang Li, Xu Chang, Zhaohu Li, Yang Zhao, Guidong Wang, Ruqi Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.14373v2.pdf)  
  Keywords: efficient, ar, animation, neural rendering, gaussian splatting, avatar, 3d gaussian, human, dynamic, head  
- **[EG-Gaussian: Epipolar Geometry and Graph Network Enhanced 3D Gaussian Splatting](https://arxiv.org/abs/2504.13540v1)**  
  Authors: Beizhen Zhao, Yifan Zhou, Zijian Wang, Hao Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.13540v1.pdf)  
  Keywords: efficient, outdoor, sparse-view, ar, gaussian splatting, 3d gaussian, geometry  
- **[Volume Encoding Gaussians: Transfer Function-Agnostic 3D Gaussians for Volume Rendering](https://arxiv.org/abs/2504.13339v1)**  
  Authors: Landon Dyken, Andres Sewell, Will Usher, Steve Petruzza, Sidharth Kumar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.13339v1.pdf)  
  Keywords: efficient, fast, ar, gaussian splatting, 3d gaussian, geometry, motion  
- **[ODHSR: Online Dense 3D Reconstruction of Humans and Scenes from Monocular Videos](https://arxiv.org/abs/2504.13167v2)**  
  Authors: Zetong Zhang, Manuel Kaufmann, Lixin Xue, Jie Song, Martin R. Oswald  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.13167v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://eth-ait.github.io/ODHSR.)  
  Keywords: efficient, understanding, ar, neural rendering, 3d reconstruction, gaussian splatting, 3d gaussian, tracking, human, deformation  
- **[Training-Free Hierarchical Scene Understanding for Gaussian Splatting with Superpoint Graphs](https://arxiv.org/abs/2504.13153v1)**  
  Authors: Shaohui Dai, Yansong Qu, Zheyan Li, Xinyang Li, Shengchuan Zhang, Liujuan Cao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.13153v1.pdf) | [![GitHub](https://img.shields.io/github/stars/Atrovast/THGS?style=social)](https://github.com/Atrovast/THGS)  
  Keywords: efficient, understanding, fast, compact, segmentation, ar, gaussian splatting, 3d gaussian, geometry, semantic  

### Quality Enhancement

*Showing the latest 50 out of 271 papers*

- **[StyleMe3D: Stylization with Disentangled Priors by Multiple Encoders on 3D Gaussians](https://arxiv.org/abs/2504.15281v1)**  
  Authors: Cailin Zhuang, Yaoqi Hu, Xuanyang Zhang, Wei Cheng, Jiacheng Bao, Shengqi Liu, Yiying Yang, Xianfang Zeng, Gang Yu, Ming Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.15281v1.pdf)  
  Keywords: nerf, ar, real-time rendering, gaussian splatting, 3d gaussian, lighting, human, dynamic, quality enhancement, semantic  
- **[CAGE-GS: High-fidelity Cage Based 3D Gaussian Splatting Deformation](https://arxiv.org/abs/2504.12800v1)**  
  Authors: Yifei Tong, Runze Tian, Xiao Han, Dingyao Liu, Fenggen Yu, Yan Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.12800v1.pdf)  
  Keywords: ar, gaussian splatting, 3d gaussian, deformation, high-fidelity  
- **[3DAffordSplat: Efficient Affordance Reasoning with 3D Gaussians](https://arxiv.org/abs/2504.11218v2)**  
  Authors: Zeming Wei, Junyi Lin, Yang Liu, Weixing Chen, Jingzhou Luo, Guanbin Li, Liang Lin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.11218v2.pdf)  
  Keywords: efficient, recognition, ar, real-time rendering, gaussian splatting, 3d gaussian, lighting, human, high-fidelity, head  
- **[MCBlock: Boosting Neural Radiance Field Training Speed by MCTS-based Dynamic-Resolution Ray Sampling](https://arxiv.org/abs/2504.09878v1)**  
  Authors: Yunpeng Tan, Junlin Hao, Jiangkai Wu, Liming Liu, Qingyang Li, Xinggong Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.09878v1.pdf)  
  Keywords: efficient, nerf, acceleration, ar, gaussian splatting, dynamic, high-fidelity  
- **[TextSplat: Text-Guided Semantic Fusion for Generalizable Gaussian Splatting](https://arxiv.org/abs/2504.09588v1)**  
  Authors: Zhicong Wu, Hongbin Xu, Gang Xu, Ping Nie, Zhixin Yan, Jinkai Zheng, Liangqiong Qu, Ming Li, Liqiang Nie  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.09588v1.pdf)  
  Keywords: understanding, segmentation, ar, 3d reconstruction, gaussian splatting, 3d gaussian, high-fidelity, semantic  
- **[A Constrained Optimization Approach for Gaussian Splatting from Coarsely-posed Images and Noisy Lidar Point Clouds](https://arxiv.org/abs/2504.09129v1)**  
  Authors: Jizong Peng, Tze Ho Elden Tse, Kai Xu, Wenchao Gao, Angela Yao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.09129v1.pdf)  
  Keywords: geometry, ar, 3d reconstruction, gaussian splatting, 3d gaussian, high-fidelity, motion  
- **[ContrastiveGaussian: High-Fidelity 3D Generation with Contrastive Learning and Gaussian Splatting](https://arxiv.org/abs/2504.08100v1)**  
  Authors: Junbang Liu, Enpei Huang, Dongxing Mao, Hui Zhang, Xinyuan Song, Yongxin Ni  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.08100v1.pdf)  
  Keywords: ar, high-fidelity, gaussian splatting  
- **[InteractAvatar: Modeling Hand-Face Interaction in Photorealistic Avatars with Deformable Gaussians](https://arxiv.org/abs/2504.07949v1)**  
  Authors: Kefan Chen, Sergiu Oprea, Justin Theiss, Sreyas Mohan, Srinath Sridhar, Aayush Prakash  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.07949v1.pdf)  
  Keywords: geometry, vr, shadow, ar, avatar, gaussian splatting, 3d gaussian, body, human, face, dynamic, high-fidelity, head  
- **[L3GS: Layered 3D Gaussian Splats for Efficient 3D Scene Delivery](https://arxiv.org/abs/2504.05517v1)**  
  Authors: Yi-Zhen Tsai, Xuechen Zhang, Zheng Li, Jiasi Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.05517v1.pdf)  
  Keywords: efficient, ar, 3d gaussian, high quality, efficient rendering, head  
- **[Embracing Dynamics: Dynamics-aware 4D Gaussian Splatting SLAM](https://arxiv.org/abs/2504.04844v1)**  
  Authors: Zhicong Sun, Jacqueline Lo, Jinxing Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.04844v1.pdf)  
  Keywords: mapping, localization, ar, gaussian splatting, tracking, 3d gaussian, 4d, slam, dynamic, high-fidelity  

### Ray Tracing

- **[DNF-Avatar: Distilling Neural Fields for Real-time Animatable Avatar Relighting](https://arxiv.org/abs/2504.10486v1)**  
  Authors: Zeren Jiang, Shaofei Wang, Siyu Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.10486v1.pdf)  
  Keywords: fast, shadow, relightable, avatar, gaussian splatting, ar, ray tracing, lighting, relighting, human, geometry  
- **[Stochastic Ray Tracing of 3D Transparent Gaussians](https://arxiv.org/abs/2504.06598v2)**  
  Authors: Xin Sun, Iliyan Georgiev, Yun Fei, Miloš Hašan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.06598v2.pdf)  
  Keywords: efficient, acceleration, ar, gaussian splatting, ray tracing, 3d gaussian, relighting, lighting, efficient rendering  
- **[3D Gaussian Particle Approximation of VDB Datasets: A Study for Scientific Visualization](https://arxiv.org/abs/2504.04857v2)**  
  Authors: Isha Sharma, Dieter Schmalstieg  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.04857v2.pdf)  
  Keywords: efficient, acceleration, compact, ar, animation, ray marching, gaussian splatting, 3d gaussian, dynamic  
- **[3D Gaussian Inverse Rendering with Approximated Global Illumination](https://arxiv.org/abs/2504.01358v1)**  
  Authors: Zirui Wu, Jianteng Chen, Laijian Li, Shaoteng Wu, Zhikai Zhu, Kang Xu, Martin R. Oswald, Jie Song  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.01358v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://wuzirui.github.io/gs-ssr.)  
  Keywords: efficient, global illumination, ar, real-time rendering, gaussian splatting, ray tracing, 3d gaussian, illumination, lighting, face  
- **[Real-time Global Illumination for Dynamic 3D Gaussian Scenes](https://arxiv.org/abs/2503.17897v1)**  
  Authors: Chenxiao Hu, Meng Gai, Guoping Wang, Sheng Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.17897v1.pdf)  
  Keywords: global illumination, light transport, fast, real-time rendering, 3d gaussian, lighting, illumination, dynamic, face  
- **[REdiSplats: Ray Tracing for Editable Gaussian Splatting](https://arxiv.org/abs/2503.12284v1)**  
  Authors: Krzysztof Byrski, Grzegorz Wilczyński, Weronika Smolak-Dyżewska, Piotr Borycki, Dawid Baran, Sławomir Tadeja, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.12284v1.pdf)  
  Keywords: reflection, fast, shadow, ar, neural rendering, gaussian splatting, ray tracing, 3d gaussian  
- **[BEAM: Bridging Physically-based Rendering and Gaussian Modeling for Relightable Volumetric Video](https://arxiv.org/abs/2502.08297v1)**  
  Authors: Yu Hong, Yize Wu, Zhehao Shen, Chengcheng Guo, Yuheng Jiang, Yingliang Zhang, Jingyi Yu, Lan Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.08297v1.pdf)  
  Keywords: efficient, ar, real-time rendering, relightable, tracking, ray tracing, lighting, 4d, face, dynamic, geometry  
- **[MeshSplats: Mesh-Based Rendering with Gaussian Splatting Initialization](https://arxiv.org/abs/2502.07754v1)**  
  Authors: Rafał Tobiasz, Grzegorz Wilczyński, Marcin Mazur, Sławomir Tadeja, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.07754v1.pdf)  
  Keywords: reflection, shadow, gaussian splatting, ray tracing, lighting, face  
- **[Scalable 3D Gaussian Splatting-Based RF Signal Spatial Propagation Modeling](https://arxiv.org/abs/2502.01826v1)**  
  Authors: Kang Yang, Gaofeng Dong, Sijie Ji, Wan Du, Mani Srivastava  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.01826v1.pdf)  
  Keywords: ar, gaussian splatting, survey, ray tracing, 3d gaussian  
- **[Radiant Foam: Real-Time Differentiable Ray Tracing](https://arxiv.org/abs/2502.01157v1)**  
  Authors: Shrisudhan Govindarajan, Daniel Rebain, Kwang Moo Yi, Andrea Tagliasacchi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.01157v1.pdf)  
  Keywords: efficient, reflection, light transport, acceleration, ar, gaussian splatting, ray tracing  

### Relighting

*Showing the latest 50 out of 194 papers*

- **[StyleMe3D: Stylization with Disentangled Priors by Multiple Encoders on 3D Gaussians](https://arxiv.org/abs/2504.15281v1)**  
  Authors: Cailin Zhuang, Yaoqi Hu, Xuanyang Zhang, Wei Cheng, Jiacheng Bao, Shengqi Liu, Yiying Yang, Xianfang Zeng, Gang Yu, Ming Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.15281v1.pdf)  
  Keywords: nerf, ar, real-time rendering, gaussian splatting, 3d gaussian, lighting, human, dynamic, quality enhancement, semantic  
- **[Immersive Teleoperation Framework for Locomanipulation Tasks](https://arxiv.org/abs/2504.15229v1)**  
  Authors: Takuya Boehringer, Jonathan Embley-Riches, Karim Hammoud, Valerio Modugno, Dimitrios Kanoulas  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.15229v1.pdf)  
  Keywords: vr, fast, ar, gaussian splatting, lighting, face  
- **[Metamon-GS: Enhancing Representability with Variance-Guided Densification and Light Encoding](https://arxiv.org/abs/2504.14460v1)**  
  Authors: Junyan Su, Baozhu Zhao, Xiaohan Zhang, Qi Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.14460v1.pdf)  
  Keywords: ar, gaussian splatting, 3d gaussian, lighting  
- **[SLAM&Render: A Benchmark for the Intersection Between Neural Rendering, Gaussian Splatting and SLAM](https://arxiv.org/abs/2504.13713v2)**  
  Authors: Samuel Cerezo, Gaetano Meli, Tomás Berriel Martins, Kirill Safronov, Javier Civera  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.13713v2.pdf)  
  Keywords: mapping, nerf, localization, ar, neural rendering, gaussian splatting, lighting, illumination, slam  
- **[Novel Demonstration Generation with Gaussian Splatting Enables Robust One-Shot Manipulation](https://arxiv.org/abs/2504.13175v1)**  
  Authors: Sizhe Yang, Wenye Yu, Jia Zeng, Jun Lv, Kerui Ren, Cewu Lu, Dahua Lin, Jiangmiao Pang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.13175v1.pdf)  
  Keywords: ar, gaussian splatting, 3d gaussian, lighting, face  
- **[Digital Twin Generation from Visual Data: A Survey](https://arxiv.org/abs/2504.13159v1)**  
  Authors: Andrew Melnik, Benjamin Alt, Giang Nguyen, Artur Wilkowski, Maciej Stefańczyk, Qirui Wu, Sinan Harms, Helge Rhodin, Manolis Savva, Michael Beetz  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.13159v1.pdf) | [![GitHub](https://img.shields.io/github/stars/ndrwmlnk/awesome-digital-twins?style=social)](https://github.com/ndrwmlnk/awesome-digital-twins)  
  Keywords: segmentation, ar, gaussian splatting, survey, 3d gaussian, lighting, robotics, semantic  
- **[GSAC: Leveraging Gaussian Splatting for Photorealistic Avatar Creation with Unity Integration](https://arxiv.org/abs/2504.12999v1)**  
  Authors: Rendong Zhang, Alexandra Watkins, Nilanjan Sarkar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.12999v1.pdf)  
  Keywords: efficient, vr, nerf, ar, avatar, gaussian splatting, 3d gaussian, lighting, human, face  
- **[TSGS: Improving Gaussian Splatting for Transparent Surface Reconstruction via Normal and De-lighting Priors](https://arxiv.org/abs/2504.12799v1)**  
  Authors: Mingwei Li, Pu Pang, Hehe Fan, Hua Huang, Yi Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.12799v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://longxiang-ai.github.io/TSGS/.)  
  Keywords: efficient, ar, 3d reconstruction, gaussian splatting, 3d gaussian, lighting, face, geometry  
- **[3DAffordSplat: Efficient Affordance Reasoning with 3D Gaussians](https://arxiv.org/abs/2504.11218v2)**  
  Authors: Zeming Wei, Junyi Lin, Yang Liu, Weixing Chen, Jingzhou Luo, Guanbin Li, Liang Lin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.11218v2.pdf)  
  Keywords: efficient, recognition, ar, real-time rendering, gaussian splatting, 3d gaussian, lighting, human, high-fidelity, head  
- **[GaSLight: Gaussian Splats for Spatially-Varying Lighting in HDR](https://arxiv.org/abs/2504.10809v2)**  
  Authors: Christophe Bolduc, Yannick Hold-Geoffroy, Zhixin Shu, Jean-François Lalonde  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.10809v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://lvsn.github.io/gaslight/)  
  Keywords: ar, dynamic, lighting  

### SLAM

*Showing the latest 50 out of 249 papers*

- **[ToF-Splatting: Dense SLAM using Sparse Time-of-Flight Depth and Multi-Frame Integration](https://arxiv.org/abs/2504.16545v1)**  
  Authors: Andrea Conti, Matteo Poggi, Valerio Cambareri, Martin R. Oswald, Stefano Mattoccia  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.16545v1.pdf)  
  Keywords: efficient, mapping, vr, ar, gaussian splatting, tracking, 3d gaussian, slam, geometry  
- **[NVSMask3D: Hard Visual Prompting with Camera Pose Interpolation for 3D Open Vocabulary Instance Segmentation](https://arxiv.org/abs/2504.14638v1)**  
  Authors: Junyuan Fang, Zihan Wang, Yejun Zhang, Shuzhe Wang, Iaroslav Melekhov, Juho Kannala  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.14638v1.pdf)  
  Keywords: recognition, segmentation, localization, ar, gaussian splatting, 3d gaussian  
- **[SLAM&Render: A Benchmark for the Intersection Between Neural Rendering, Gaussian Splatting and SLAM](https://arxiv.org/abs/2504.13713v2)**  
  Authors: Samuel Cerezo, Gaetano Meli, Tomás Berriel Martins, Kirill Safronov, Javier Civera  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.13713v2.pdf)  
  Keywords: mapping, nerf, localization, ar, neural rendering, gaussian splatting, lighting, illumination, slam  
- **[ODHSR: Online Dense 3D Reconstruction of Humans and Scenes from Monocular Videos](https://arxiv.org/abs/2504.13167v2)**  
  Authors: Zetong Zhang, Manuel Kaufmann, Lixin Xue, Jie Song, Martin R. Oswald  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.13167v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://eth-ait.github.io/ODHSR.)  
  Keywords: efficient, understanding, ar, neural rendering, 3d reconstruction, gaussian splatting, 3d gaussian, tracking, human, deformation  
- **[SIGMAN:Scaling 3D Human Gaussian Generation with Millions of Assets](https://arxiv.org/abs/2504.06982v1)**  
  Authors: Yuhang Yang, Fengqi Liu, Yixing Lu, Qin Zhao, Pingyu Wu, Wei Zhai, Ran Yi, Yang Cao, Lizhuang Ma, Zheng-Jun Zha, Junting Dong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.06982v1.pdf)  
  Keywords: mapping, ar, 3d gaussian, human, deformation  
- **[Embracing Dynamics: Dynamics-aware 4D Gaussian Splatting SLAM](https://arxiv.org/abs/2504.04844v1)**  
  Authors: Zhicong Sun, Jacqueline Lo, Jinxing Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.04844v1.pdf)  
  Keywords: mapping, localization, ar, gaussian splatting, tracking, 3d gaussian, 4d, slam, dynamic, high-fidelity  
- **[WildGS-SLAM: Monocular Gaussian Splatting SLAM in Dynamic Environments](https://arxiv.org/abs/2504.03886v1)**  
  Authors: Jianhao Zheng, Zihan Zhu, Valentin Bieri, Marc Pollefeys, Songyou Peng, Iro Armeni  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.03886v1.pdf)  
  Keywords: efficient, mapping, ar, tracking, gaussian splatting, slam, dynamic  
- **[MonoGS++: Fast and Accurate Monocular RGB Gaussian SLAM](https://arxiv.org/abs/2504.02437v1)**  
  Authors: Renwu Li, Wenjing Ke, Dong Li, Lu Tian, Emad Barsoum  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.02437v1.pdf)  
  Keywords: mapping, fast, localization, ar, gaussian splatting, tracking, 3d gaussian, slam, dynamic, face  
- **[Luminance-GS: Adapting 3D Gaussian Splatting to Challenging Lighting Conditions with View-Adaptive Curve Adjustment](https://arxiv.org/abs/2504.01503v2)**  
  Authors: Ziteng Cui, Xuangeng Chu, Tatsuya Harada  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.01503v2.pdf)  
  Keywords: mapping, nerf, ar, real-time rendering, gaussian splatting, 3d gaussian, lighting  
- **[Visual Acoustic Fields](https://arxiv.org/abs/2503.24270v2)**  
  Authors: Yuelei Li, Hyunjin Kim, Fangneng Zhan, Ri-Zhao Qiu, Mazeyu Ji, Xiaojun Shan, Xueyan Zou, Paul Liang, Hanspeter Pfister, Xiaolong Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.24270v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://yuelei0428.github.io/projects/Visual-Acoustic-Fields/.)  
  Keywords: localization, ar, gaussian splatting, 3d gaussian, human  

### Scene Understanding

*Showing the latest 50 out of 303 papers*

- **[Text-based Animatable 3D Avatars with Morphable Model Alignment](https://arxiv.org/abs/2504.15835v1)**  
  Authors: Yiqian Wu, Malte Prinzler, Xiaogang Jin, Siyu Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.15835v1.pdf)  
  Keywords: ar, animation, avatar, dynamic, semantic, geometry, head  
- **[StyleMe3D: Stylization with Disentangled Priors by Multiple Encoders on 3D Gaussians](https://arxiv.org/abs/2504.15281v1)**  
  Authors: Cailin Zhuang, Yaoqi Hu, Xuanyang Zhang, Wei Cheng, Jiacheng Bao, Shengqi Liu, Yiying Yang, Xianfang Zeng, Gang Yu, Ming Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.15281v1.pdf)  
  Keywords: nerf, ar, real-time rendering, gaussian splatting, 3d gaussian, lighting, human, dynamic, quality enhancement, semantic  
- **[NVSMask3D: Hard Visual Prompting with Camera Pose Interpolation for 3D Open Vocabulary Instance Segmentation](https://arxiv.org/abs/2504.14638v1)**  
  Authors: Junyuan Fang, Zihan Wang, Yejun Zhang, Shuzhe Wang, Iaroslav Melekhov, Juho Kannala  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.14638v1.pdf)  
  Keywords: recognition, segmentation, localization, ar, gaussian splatting, 3d gaussian  
- **[RoboOcc: Enhancing the Geometric and Semantic Scene Understanding for Robots](https://arxiv.org/abs/2504.14604v1)**  
  Authors: Zhang Zhang, Qiang Zhang, Wei Cui, Shuai Shi, Yijie Guo, Gang Han, Wen Zhao, Hengle Ren, Renjing Xu, Jian Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.14604v1.pdf)  
  Keywords: understanding, ar, 3d gaussian, geometry, semantic  
- **[ODHSR: Online Dense 3D Reconstruction of Humans and Scenes from Monocular Videos](https://arxiv.org/abs/2504.13167v2)**  
  Authors: Zetong Zhang, Manuel Kaufmann, Lixin Xue, Jie Song, Martin R. Oswald  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.13167v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://eth-ait.github.io/ODHSR.)  
  Keywords: efficient, understanding, ar, neural rendering, 3d reconstruction, gaussian splatting, 3d gaussian, tracking, human, deformation  
- **[Digital Twin Generation from Visual Data: A Survey](https://arxiv.org/abs/2504.13159v1)**  
  Authors: Andrew Melnik, Benjamin Alt, Giang Nguyen, Artur Wilkowski, Maciej Stefańczyk, Qirui Wu, Sinan Harms, Helge Rhodin, Manolis Savva, Michael Beetz  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.13159v1.pdf) | [![GitHub](https://img.shields.io/github/stars/ndrwmlnk/awesome-digital-twins?style=social)](https://github.com/ndrwmlnk/awesome-digital-twins)  
  Keywords: segmentation, ar, gaussian splatting, survey, 3d gaussian, lighting, robotics, semantic  
- **[Training-Free Hierarchical Scene Understanding for Gaussian Splatting with Superpoint Graphs](https://arxiv.org/abs/2504.13153v1)**  
  Authors: Shaohui Dai, Yansong Qu, Zheyan Li, Xinyang Li, Shengchuan Zhang, Liujuan Cao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.13153v1.pdf) | [![GitHub](https://img.shields.io/github/stars/Atrovast/THGS?style=social)](https://github.com/Atrovast/THGS)  
  Keywords: efficient, understanding, fast, compact, segmentation, ar, gaussian splatting, 3d gaussian, geometry, semantic  
- **[Mind2Matter: Creating 3D Models from EEG Signals](https://arxiv.org/abs/2504.11936v2)**  
  Authors: Xia Deng, Shen Chen, Jiale Zhou, Lei Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.11936v2.pdf) | [![GitHub](https://img.shields.io/github/stars/sddwwww/Mind2Matter?style=social)](https://github.com/sddwwww/Mind2Matter)  
  Keywords: ar, 3d reconstruction, 3d gaussian, face, semantic  
- **[CAGS: Open-Vocabulary 3D Scene Understanding with Context-Aware Gaussian Splatting](https://arxiv.org/abs/2504.11893v1)**  
  Authors: Wei Sun, Yanzhao Zhou, Jianbin Jiao, Yuan Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.11893v1.pdf)  
  Keywords: efficient, understanding, segmentation, ar, gaussian splatting, 3d gaussian, robotics  
- **[3DAffordSplat: Efficient Affordance Reasoning with 3D Gaussians](https://arxiv.org/abs/2504.11218v2)**  
  Authors: Zeming Wei, Junyi Lin, Yang Liu, Weixing Chen, Jingzhou Luo, Guanbin Li, Liang Lin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.11218v2.pdf)  
  Keywords: efficient, recognition, ar, real-time rendering, gaussian splatting, 3d gaussian, lighting, human, high-fidelity, head  



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