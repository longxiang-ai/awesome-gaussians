# Awesome Gaussian Splatting [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of latest research papers, projects and resources related to Gaussian Splatting. Content is automatically updated daily.

> Last Update: 2025-05-03 00:52:19

## Categories

- [3DGS Surveys](#3dgs-surveys) (27 papers) - Survey papers and benchmarks about 3D Gaussian Splatting
- [Acceleration](#acceleration) (489 papers) - Papers about speeding up rendering or training
- [Applications](#applications) (1717 papers) - Papers about specific applications
- [Avatar Generation](#avatar-generation) (577 papers) - Papers about human avatar generation
- [Dynamic Scene](#dynamic-scene) (649 papers) - Papers about dynamic scene reconstruction and rendering
- [Few-shot](#few-shot) (121 papers) - Papers about few-shot or sparse view reconstruction
- [Geometry Reconstruction](#geometry-reconstruction) (557 papers) - Papers about 3D geometry reconstruction
- [Large Scene](#large-scene) (92 papers) - Papers about large-scale scene reconstruction
- [Model Compression](#model-compression) (653 papers) - Papers about model compression and optimization
- [Quality Enhancement](#quality-enhancement) (274 papers) - Papers focusing on improving rendering quality
- [Ray Tracing](#ray-tracing) (40 papers) - Papers about ray tracing and ray casting in Gaussian Splatting
- [Relighting](#relighting) (197 papers) - Papers about relighting and illumination effects in Gaussian Splatting
- [SLAM](#slam) (256 papers) - Papers about SLAM using Gaussian Splatting
- [Scene Understanding](#scene-understanding) (305 papers) - Papers about scene understanding and semantic analysis



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
  Keywords: gaussian splatting, semantic, ar, segmentation, robotics, 3d gaussian, lighting, survey  
- **[A Survey on Event-driven 3D Reconstruction: Development under Different Categories](https://arxiv.org/abs/2503.19753v2)**  
  Authors: Chuanzhi Xu, Haoxian Zhou, Haodong Chen, Vera Chung, Qiang Qu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.19753v2.pdf)  
  Keywords: fast, gaussian splatting, dynamic, ar, motion, 3d reconstruction, 3d gaussian, lighting, survey  
- **[Dynamic Scene Reconstruction: Recent Advance in Real-time Rendering and Streaming](https://arxiv.org/abs/2503.08166v1)**  
  Authors: Jiaxuan Zhu, Hao Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.08166v1.pdf)  
  Keywords: dynamic, gaussian splatting, ar, real-time rendering, 3d gaussian, survey  
- **[Infinite Leagues Under the Sea: Photorealistic 3D Underwater Terrain Generation by Latent Fractal Diffusion Models](https://arxiv.org/abs/2503.06784v1)**  
  Authors: Tianyi Zhang, Weiming Zhi, Joshua Mangelson, Matthew Johnson-Roberson  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.06784v1.pdf)  
  Keywords: semantic, ar, survey, geometry  
- **[Compression in 3D Gaussian Splatting: A Survey of Methods, Trends, and Future Directions](https://arxiv.org/abs/2502.19457v1)**  
  Authors: Muhammad Salman Ali, Chaoning Zhang, Marco Cagnazzo, Giuseppe Valenzise, Enzo Tartaglione, Sung-Ho Bae  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.19457v1.pdf)  
  Keywords: gaussian splatting, compression, nerf, ar, 3d reconstruction, real-time rendering, 3d gaussian, survey, efficient  
- **[Grounding Creativity in Physics: A Brief Survey of Physical Priors in AIGC](https://arxiv.org/abs/2502.07007v1)**  
  Authors: Siwei Meng, Yawei Luo, Ping Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.07007v1.pdf)  
  Keywords: dynamic, gaussian splatting, deformation, ar, motion, 4d, nerf, lighting, survey  
- **[Scalable 3D Gaussian Splatting-Based RF Signal Spatial Propagation Modeling](https://arxiv.org/abs/2502.01826v1)**  
  Authors: Kang Yang, Gaofeng Dong, Sijie Ji, Wan Du, Mani Srivastava  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.01826v1.pdf)  
  Keywords: gaussian splatting, ar, ray tracing, 3d gaussian, survey  
- **[NFL-BA: Improving Endoscopic SLAM with Near-Field Light Bundle Adjustment](https://arxiv.org/abs/2412.13176v2)**  
  Authors: Andrea Dunn Beltran, Daniel Rho, Stephen Pizer, Marc Niethammer, Roni Sengupta  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.13176v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://asdunnbe.github.io/NFL-BA/)  
  Keywords: dynamic, localization, ar, geometry, face, tracking, outdoor, mapping, slam, lighting, survey  
- **[Adversarial Attacks Using Differentiable Rendering: A Survey](https://arxiv.org/abs/2411.09749v1)**  
  Authors: Matthew Hull, Chao Zhang, Zsolt Kira, Duen Horng Chau  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.09749v1.pdf)  
  Keywords: gaussian splatting, illumination, ar, 3d gaussian, recognition, survey  
- **[Neural Fields in Robotics: A Survey](https://arxiv.org/abs/2410.20220v1)**  
  Authors: Muhammad Zubair Irshad, Mauro Comi, Yen-Chen Lin, Nick Heppert, Abhinav Valada, Rares Ambrus, Zsolt Kira, Jonathan Tremblay  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.20220v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://robonerf.github.io)  
  Keywords: high-fidelity, gaussian splatting, dynamic, compact, semantic, ar, geometry, 3d reconstruction, robotics, autonomous driving, nerf, lighting, survey  

### Acceleration

*Showing the latest 50 out of 489 papers*

- **[EfficientHuman: Efficient Training and Reconstruction of Moving Human using Articulated 2D Gaussian](https://arxiv.org/abs/2504.20607v1)**  
  Authors: Hao Tian, Rui Liu, Wen Shen, Yilong Hu, Zhihao Zheng, Xiaolin Qin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.20607v1.pdf)  
  Keywords: dynamic, fast, gaussian splatting, human, ar, face, body, 3d gaussian, efficient  
- **[GSFeatLoc: Visual Localization Using Feature Correspondence on 3D Gaussian Splatting](https://arxiv.org/abs/2504.20379v2)**  
  Authors: Jongwon Lee, Timothy Bretl  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.20379v2.pdf)  
  Keywords: fast, gaussian splatting, localization, ar, nerf, 3d gaussian  
- **[Sparse2DGS: Geometry-Prioritized Gaussian Splatting for Surface Reconstruction from Sparse Views](https://arxiv.org/abs/2504.20378v1)**  
  Authors: Jiang Wu, Rui Li, Yu Zhu, Rong Guo, Jinqiu Sun, Yanning Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.20378v1.pdf)  
  Keywords: fast, gaussian splatting, sparse-view, ar, sparse view, geometry, motion, face, nerf  
- **[Mesh-Learner: Texturing Mesh with Spherical Harmonics](https://arxiv.org/abs/2504.19938v1)**  
  Authors: Yunfei Wan, Jianheng Liu, Jiarong Lin, Fu Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.19938v1.pdf) | [![GitHub](https://img.shields.io/github/stars/hku-mars/Mesh-Learner?style=social)](https://github.com/hku-mars/Mesh-Learner)  
  Keywords: fast, gaussian splatting, ar, mapping, 3d reconstruction, robotics, 3d gaussian, efficient  
- **[TransparentGS: Fast Inverse Rendering of Transparent Objects with Gaussians](https://arxiv.org/abs/2504.18768v2)**  
  Authors: Letian Huang, Dongwei Ye, Jialin Dan, Chengzhi Tao, Huiwen Liu, Kun Zhou, Bo Ren, Yuanqi Li, Yanwen Guo, Jie Guo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.18768v2.pdf)  
  Keywords: fast, gaussian splatting, reflection, ar, 3d gaussian, efficient  
- **[STP4D: Spatio-Temporal-Prompt Consistent Modeling for Text-to-4D Gaussian Splatting](https://arxiv.org/abs/2504.18318v1)**  
  Authors: Yunze Deng, Haijun Xiong, Bin Feng, Xinggang Wang, Wenyu Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.18318v1.pdf)  
  Keywords: high-fidelity, gaussian splatting, deformation, ar, 4d, real-time rendering  
- **[iVR-GS: Inverse Volume Rendering for Explorable Visualization via Editable 3D Gaussian Splatting](https://arxiv.org/abs/2504.17954v1)**  
  Authors: Kaiyuan Tang, Siyuan Yao, Chaoli Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.17954v1.pdf) | [![GitHub](https://img.shields.io/github/stars/TouKaienn/iVR-GS?style=social)](https://github.com/TouKaienn/iVR-GS)  
  Keywords: fast, gaussian splatting, ar, mapping, vr, nerf, 3d gaussian, lighting  
- **[When Gaussian Meets Surfel: Ultra-fast High-fidelity Radiance Field Rendering](https://arxiv.org/abs/2504.17545v1)**  
  Authors: Keyang Ye, Tianjia Shao, Kun Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.17545v1.pdf)  
  Keywords: high-fidelity, fast, compact, ar, geometry, 3d gaussian  
- **[Visibility-Uncertainty-guided 3D Gaussian Inpainting via Scene Conceptional Learning](https://arxiv.org/abs/2504.17815v1)**  
  Authors: Mingxuan Cui, Qing Guo, Yuyi Wang, Hongkai Yu, Di Lin, Qin Zou, Ming-Ming Cheng, Xi Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.17815v1.pdf)  
  Keywords: dynamic, fast, gaussian splatting, semantic, ar, nerf, 3d gaussian, efficient  
- **[StyleMe3D: Stylization with Disentangled Priors by Multiple Encoders on 3D Gaussians](https://arxiv.org/abs/2504.15281v1)**  
  Authors: Cailin Zhuang, Yaoqi Hu, Xuanyang Zhang, Wei Cheng, Jiacheng Bao, Shengqi Liu, Yiying Yang, Xianfang Zeng, Gang Yu, Ming Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.15281v1.pdf)  
  Keywords: dynamic, gaussian splatting, human, nerf, semantic, ar, quality enhancement, real-time rendering, 3d gaussian, lighting  

### Applications

*Showing the latest 50 out of 1717 papers*

- **[Real-Time Animatable 2DGS-Avatars with Detail Enhancement from Monocular Videos](https://arxiv.org/abs/2505.00421v1)**  
  Authors: Xia Yuan, Hai Yuan, Wenyi Ge, Ying Fu, Xi Wu, Guanyu Xing  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.00421v1.pdf)  
  Keywords: dynamic, gaussian splatting, human, deformation, ar, face, animation, avatar  
- **[HoloTime: Taming Video Diffusion Models for Panoramic 4D Scene Generation](https://arxiv.org/abs/2504.21650v1)**  
  Authors: Haiyang Zhou, Wangbo Yu, Jiawen Guan, Xinhua Cheng, Yonghong Tian, Li Yuan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.21650v1.pdf)  
  Keywords: dynamic, high-fidelity, gaussian splatting, ar, 4d, vr  
- **[GaussTrap: Stealthy Poisoning Attacks on 3D Gaussian Splatting for Targeted Scene Confusion](https://arxiv.org/abs/2504.20829v1)**  
  Authors: Jiaxin Hong, Sixu Chen, Shuoyang Sun, Hongyao Yu, Hao Fang, Yuqi Tan, Bin Chen, Shuhan Qi, Jiawei Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.20829v1.pdf)  
  Keywords: ar, gaussian splatting, 3d gaussian, vr  
- **[GauSS-MI: Gaussian Splatting Shannon Mutual Information for Active 3D Reconstruction](https://arxiv.org/abs/2504.21067v1)**  
  Authors: Yuhan Xie, Yixi Cai, Yinqiang Zhang, Lei Yang, Jia Pan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.21067v1.pdf)  
  Keywords: gaussian splatting, ar, motion, 3d reconstruction, nerf, 3d gaussian, efficient  
- **[EfficientHuman: Efficient Training and Reconstruction of Moving Human using Articulated 2D Gaussian](https://arxiv.org/abs/2504.20607v1)**  
  Authors: Hao Tian, Rui Liu, Wen Shen, Yilong Hu, Zhihao Zheng, Xiaolin Qin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.20607v1.pdf)  
  Keywords: dynamic, fast, gaussian splatting, human, ar, face, body, 3d gaussian, efficient  
- **[Creating Your Editable 3D Photorealistic Avatar with Tetrahedron-constrained Gaussian Splatting](https://arxiv.org/abs/2504.20403v1)**  
  Authors: Hanxi Liu, Yifang Men, Zhouhui Lian  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.20403v1.pdf)  
  Keywords: localization, gaussian splatting, ar, geometry, avatar, 3d gaussian, vr  
- **[GSFeatLoc: Visual Localization Using Feature Correspondence on 3D Gaussian Splatting](https://arxiv.org/abs/2504.20379v2)**  
  Authors: Jongwon Lee, Timothy Bretl  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.20379v2.pdf)  
  Keywords: fast, gaussian splatting, localization, ar, nerf, 3d gaussian  
- **[Sparse2DGS: Geometry-Prioritized Gaussian Splatting for Surface Reconstruction from Sparse Views](https://arxiv.org/abs/2504.20378v1)**  
  Authors: Jiang Wu, Rui Li, Yu Zhu, Rong Guo, Jinqiu Sun, Yanning Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.20378v1.pdf)  
  Keywords: fast, gaussian splatting, sparse-view, ar, sparse view, geometry, motion, face, nerf  
- **[Mesh-Learner: Texturing Mesh with Spherical Harmonics](https://arxiv.org/abs/2504.19938v1)**  
  Authors: Yunfei Wan, Jianheng Liu, Jiarong Lin, Fu Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.19938v1.pdf) | [![GitHub](https://img.shields.io/github/stars/hku-mars/Mesh-Learner?style=social)](https://github.com/hku-mars/Mesh-Learner)  
  Keywords: fast, gaussian splatting, ar, mapping, 3d reconstruction, robotics, 3d gaussian, efficient  
- **[CE-NPBG: Connectivity Enhanced Neural Point-Based Graphics for Novel View Synthesis in Autonomous Driving Scenes](https://arxiv.org/abs/2504.19557v1)**  
  Authors: Mohammad Altillawi, Fengyi Shen, Liudi Yang, Sai Manoj Prakhya, Ziyuan Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.19557v1.pdf)  
  Keywords: gaussian splatting, ar, geometry, autonomous driving, 3d gaussian  

### Avatar Generation

*Showing the latest 50 out of 577 papers*

- **[Real-Time Animatable 2DGS-Avatars with Detail Enhancement from Monocular Videos](https://arxiv.org/abs/2505.00421v1)**  
  Authors: Xia Yuan, Hai Yuan, Wenyi Ge, Ying Fu, Xi Wu, Guanyu Xing  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.00421v1.pdf)  
  Keywords: dynamic, gaussian splatting, human, deformation, ar, face, animation, avatar  
- **[EfficientHuman: Efficient Training and Reconstruction of Moving Human using Articulated 2D Gaussian](https://arxiv.org/abs/2504.20607v1)**  
  Authors: Hao Tian, Rui Liu, Wen Shen, Yilong Hu, Zhihao Zheng, Xiaolin Qin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.20607v1.pdf)  
  Keywords: dynamic, fast, gaussian splatting, human, ar, face, body, 3d gaussian, efficient  
- **[Creating Your Editable 3D Photorealistic Avatar with Tetrahedron-constrained Gaussian Splatting](https://arxiv.org/abs/2504.20403v1)**  
  Authors: Hanxi Liu, Yifang Men, Zhouhui Lian  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.20403v1.pdf)  
  Keywords: localization, gaussian splatting, ar, geometry, avatar, 3d gaussian, vr  
- **[Sparse2DGS: Geometry-Prioritized Gaussian Splatting for Surface Reconstruction from Sparse Views](https://arxiv.org/abs/2504.20378v1)**  
  Authors: Jiang Wu, Rui Li, Yu Zhu, Rong Guo, Jinqiu Sun, Yanning Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.20378v1.pdf)  
  Keywords: fast, gaussian splatting, sparse-view, ar, sparse view, geometry, motion, face, nerf  
- **[IM-Portrait: Learning 3D-aware Video Diffusion for Photorealistic Talking Heads from Monocular Videos](https://arxiv.org/abs/2504.19165v2)**  
  Authors: Yuan Li, Ziqian Bai, Feitong Tan, Zhaopeng Cui, Sean Fanello, Yinda Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.19165v2.pdf)  
  Keywords: ar, avatar, 3d reconstruction, head, nerf, 3d gaussian, vr, efficient  
- **[RGS-DR: Reflective Gaussian Surfels with Deferred Rendering for Shiny Objects](https://arxiv.org/abs/2504.18468v2)**  
  Authors: Georgios Kouros, Minye Wu, Tinne Tuytelaars  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.18468v2.pdf)  
  Keywords: gaussian splatting, reflection, ar, geometry, face, nerf, 3d gaussian, lighting, relighting  
- **[PIN-WM: Learning Physics-INformed World Models for Non-Prehensile Manipulation](https://arxiv.org/abs/2504.16693v1)**  
  Authors: Wenxuan Li, Hang Zhao, Zhiyuan Yu, Yu Du, Qin Zou, Ruizhen Hu, Kai Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.16693v1.pdf)  
  Keywords: dynamic, gaussian splatting, few-shot, ar, body, efficient  
- **[Text-based Animatable 3D Avatars with Morphable Model Alignment](https://arxiv.org/abs/2504.15835v1)**  
  Authors: Yiqian Wu, Malte Prinzler, Xiaogang Jin, Siyu Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.15835v1.pdf)  
  Keywords: dynamic, semantic, ar, geometry, avatar, animation, head  
- **[StyleMe3D: Stylization with Disentangled Priors by Multiple Encoders on 3D Gaussians](https://arxiv.org/abs/2504.15281v1)**  
  Authors: Cailin Zhuang, Yaoqi Hu, Xuanyang Zhang, Wei Cheng, Jiacheng Bao, Shengqi Liu, Yiying Yang, Xianfang Zeng, Gang Yu, Ming Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.15281v1.pdf)  
  Keywords: dynamic, gaussian splatting, human, nerf, semantic, ar, quality enhancement, real-time rendering, 3d gaussian, lighting  
- **[Immersive Teleoperation Framework for Locomanipulation Tasks](https://arxiv.org/abs/2504.15229v1)**  
  Authors: Takuya Boehringer, Jonathan Embley-Riches, Karim Hammoud, Valerio Modugno, Dimitrios Kanoulas  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.15229v1.pdf)  
  Keywords: fast, gaussian splatting, ar, face, vr, lighting  

### Dynamic Scene

*Showing the latest 50 out of 649 papers*

- **[Real-Time Animatable 2DGS-Avatars with Detail Enhancement from Monocular Videos](https://arxiv.org/abs/2505.00421v1)**  
  Authors: Xia Yuan, Hai Yuan, Wenyi Ge, Ying Fu, Xi Wu, Guanyu Xing  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.00421v1.pdf)  
  Keywords: dynamic, gaussian splatting, human, deformation, ar, face, animation, avatar  
- **[HoloTime: Taming Video Diffusion Models for Panoramic 4D Scene Generation](https://arxiv.org/abs/2504.21650v1)**  
  Authors: Haiyang Zhou, Wangbo Yu, Jiawen Guan, Xinhua Cheng, Yonghong Tian, Li Yuan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.21650v1.pdf)  
  Keywords: dynamic, high-fidelity, gaussian splatting, ar, 4d, vr  
- **[GauSS-MI: Gaussian Splatting Shannon Mutual Information for Active 3D Reconstruction](https://arxiv.org/abs/2504.21067v1)**  
  Authors: Yuhan Xie, Yixi Cai, Yinqiang Zhang, Lei Yang, Jia Pan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.21067v1.pdf)  
  Keywords: gaussian splatting, ar, motion, 3d reconstruction, nerf, 3d gaussian, efficient  
- **[EfficientHuman: Efficient Training and Reconstruction of Moving Human using Articulated 2D Gaussian](https://arxiv.org/abs/2504.20607v1)**  
  Authors: Hao Tian, Rui Liu, Wen Shen, Yilong Hu, Zhihao Zheng, Xiaolin Qin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.20607v1.pdf)  
  Keywords: dynamic, fast, gaussian splatting, human, ar, face, body, 3d gaussian, efficient  
- **[Sparse2DGS: Geometry-Prioritized Gaussian Splatting for Surface Reconstruction from Sparse Views](https://arxiv.org/abs/2504.20378v1)**  
  Authors: Jiang Wu, Rui Li, Yu Zhu, Rong Guo, Jinqiu Sun, Yanning Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.20378v1.pdf)  
  Keywords: fast, gaussian splatting, sparse-view, ar, sparse view, geometry, motion, face, nerf  
- **[4DGS-CC: A Contextual Coding Framework for 4D Gaussian Splatting Data Compression](https://arxiv.org/abs/2504.18925v2)**  
  Authors: Zicong Chen, Zhenghao Chen, Wei Jiang, Wei Wang, Lei Liu, Dong Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.18925v2.pdf)  
  Keywords: dynamic, gaussian splatting, compression, ar, 4d, 3d gaussian  
- **[STP4D: Spatio-Temporal-Prompt Consistent Modeling for Text-to-4D Gaussian Splatting](https://arxiv.org/abs/2504.18318v1)**  
  Authors: Yunze Deng, Haijun Xiong, Bin Feng, Xinggang Wang, Wenyu Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.18318v1.pdf)  
  Keywords: high-fidelity, gaussian splatting, deformation, ar, 4d, real-time rendering  
- **[CasualHDRSplat: Robust High Dynamic Range 3D Gaussian Splatting from Casually Captured Videos](https://arxiv.org/abs/2504.17728v1)**  
  Authors: Shucheng Gong, Lingzhe Zhao, Wenpu Li, Hong Xie, Yin Zhang, Shiyu Zhao, Peidong Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.17728v1.pdf) | [![GitHub](https://img.shields.io/github/stars/WU-CVGL/CasualHDRSplat?style=social)](https://github.com/WU-CVGL/CasualHDRSplat)  
  Keywords: dynamic, gaussian splatting, ar, motion, nerf, 3d gaussian  
- **[PIN-WM: Learning Physics-INformed World Models for Non-Prehensile Manipulation](https://arxiv.org/abs/2504.16693v1)**  
  Authors: Wenxuan Li, Hang Zhao, Zhiyuan Yu, Yu Du, Qin Zou, Ruizhen Hu, Kai Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.16693v1.pdf)  
  Keywords: dynamic, gaussian splatting, few-shot, ar, body, efficient  
- **[Visibility-Uncertainty-guided 3D Gaussian Inpainting via Scene Conceptional Learning](https://arxiv.org/abs/2504.17815v1)**  
  Authors: Mingxuan Cui, Qing Guo, Yuyi Wang, Hongkai Yu, Di Lin, Qin Zou, Ming-Ming Cheng, Xi Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.17815v1.pdf)  
  Keywords: dynamic, fast, gaussian splatting, semantic, ar, nerf, 3d gaussian, efficient  

### Few-shot

*Showing the latest 50 out of 121 papers*

- **[Sparse2DGS: Geometry-Prioritized Gaussian Splatting for Surface Reconstruction from Sparse Views](https://arxiv.org/abs/2504.20378v1)**  
  Authors: Jiang Wu, Rui Li, Yu Zhu, Rong Guo, Jinqiu Sun, Yanning Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.20378v1.pdf)  
  Keywords: fast, gaussian splatting, sparse-view, ar, sparse view, geometry, motion, face, nerf  
- **[PIN-WM: Learning Physics-INformed World Models for Non-Prehensile Manipulation](https://arxiv.org/abs/2504.16693v1)**  
  Authors: Wenxuan Li, Hang Zhao, Zhiyuan Yu, Yu Du, Qin Zou, Ruizhen Hu, Kai Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.16693v1.pdf)  
  Keywords: dynamic, gaussian splatting, few-shot, ar, body, efficient  
- **[IXGS-Intraoperative 3D Reconstruction from Sparse, Arbitrarily Posed Real X-rays](https://arxiv.org/abs/2504.14699v1)**  
  Authors: Sascha Jecklin, Aidana Massalimova, Ruyi Zha, Lilian Calvet, Christoph J. Laux, Mazda Farshad, Philipp Fürnstahl  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.14699v1.pdf)  
  Keywords: ar, gaussian splatting, sparse-view, 3d reconstruction  
- **[VGNC: Reducing the Overfitting of Sparse-view 3DGS via Validation-guided Gaussian Number Control](https://arxiv.org/abs/2504.14548v1)**  
  Authors: Lifeng Lin, Rongfeng Lu, Quan Chen, Haofan Ren, Ming Lu, Yaoqi Sun, Chenggang Yan, Anke Xue  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.14548v1.pdf)  
  Keywords: gaussian splatting, sparse-view, ar, 3d reconstruction, 3d gaussian  
- **[EG-Gaussian: Epipolar Geometry and Graph Network Enhanced 3D Gaussian Splatting](https://arxiv.org/abs/2504.13540v1)**  
  Authors: Beizhen Zhao, Yifan Zhou, Zijian Wang, Hao Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.13540v1.pdf)  
  Keywords: gaussian splatting, sparse-view, ar, geometry, outdoor, 3d gaussian, efficient  
- **[DropoutGS: Dropping Out Gaussians for Better Sparse-view Rendering](https://arxiv.org/abs/2504.09491v1)**  
  Authors: Yexing Xu, Longguang Wang, Minglin Chen, Sheng Ao, Li Li, Yulan Guo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.09491v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://xuyx55.github.io/DropoutGS/.)  
  Keywords: gaussian splatting, sparse-view, ar, sparse view, 3d gaussian  
- **[GIGA: Generalizable Sparse Image-driven Gaussian Avatars](https://arxiv.org/abs/2504.07144v1)**  
  Authors: Anton Zubekhin, Heming Zhu, Paulo Gotardo, Thabo Beeler, Marc Habermann, Christian Theobalt  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.07144v1.pdf)  
  Keywords: sparse-view, human, ar, avatar, head, body, 3d gaussian  
- **[DropGaussian: Structural Regularization for Sparse-view Gaussian Splatting](https://arxiv.org/abs/2504.00773v1)**  
  Authors: Hyunwoo Park, Gun Ryu, Wonjun Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.00773v1.pdf) | [![GitHub](https://img.shields.io/github/stars/DCVL-3D/DropGaussian?style=social)](https://github.com/DCVL-3D/DropGaussian)  
  Keywords: fast, gaussian splatting, sparse-view, ar, face, 3d gaussian  
- **[Coca-Splat: Collaborative Optimization for Camera Parameters and 3D Gaussians](https://arxiv.org/abs/2504.00639v1)**  
  Authors: Jiamin Wu, Hongyang Li, Xiaoke Jiang, Yuan Yao, Lei Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.00639v1.pdf)  
  Keywords: ar, sparse view, 3d gaussian  
- **[Distilling Multi-view Diffusion Models into 3D Generators](https://arxiv.org/abs/2504.00457v3)**  
  Authors: Hao Qin, Luyuan Chen, Ming Kong, Mengxu Lu, Qiang Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.00457v3.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://qinbaigao.github.io/DD3G_project/)  
  Keywords: gaussian splatting, sparse-view, ar, 3d gaussian, efficient  

### Geometry Reconstruction

*Showing the latest 50 out of 557 papers*

- **[GauSS-MI: Gaussian Splatting Shannon Mutual Information for Active 3D Reconstruction](https://arxiv.org/abs/2504.21067v1)**  
  Authors: Yuhan Xie, Yixi Cai, Yinqiang Zhang, Lei Yang, Jia Pan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.21067v1.pdf)  
  Keywords: gaussian splatting, ar, motion, 3d reconstruction, nerf, 3d gaussian, efficient  
- **[Creating Your Editable 3D Photorealistic Avatar with Tetrahedron-constrained Gaussian Splatting](https://arxiv.org/abs/2504.20403v1)**  
  Authors: Hanxi Liu, Yifang Men, Zhouhui Lian  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.20403v1.pdf)  
  Keywords: localization, gaussian splatting, ar, geometry, avatar, 3d gaussian, vr  
- **[Sparse2DGS: Geometry-Prioritized Gaussian Splatting for Surface Reconstruction from Sparse Views](https://arxiv.org/abs/2504.20378v1)**  
  Authors: Jiang Wu, Rui Li, Yu Zhu, Rong Guo, Jinqiu Sun, Yanning Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.20378v1.pdf)  
  Keywords: fast, gaussian splatting, sparse-view, ar, sparse view, geometry, motion, face, nerf  
- **[Mesh-Learner: Texturing Mesh with Spherical Harmonics](https://arxiv.org/abs/2504.19938v1)**  
  Authors: Yunfei Wan, Jianheng Liu, Jiarong Lin, Fu Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.19938v1.pdf) | [![GitHub](https://img.shields.io/github/stars/hku-mars/Mesh-Learner?style=social)](https://github.com/hku-mars/Mesh-Learner)  
  Keywords: fast, gaussian splatting, ar, mapping, 3d reconstruction, robotics, 3d gaussian, efficient  
- **[CE-NPBG: Connectivity Enhanced Neural Point-Based Graphics for Novel View Synthesis in Autonomous Driving Scenes](https://arxiv.org/abs/2504.19557v1)**  
  Authors: Mohammad Altillawi, Fengyi Shen, Liudi Yang, Sai Manoj Prakhya, Ziyuan Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.19557v1.pdf)  
  Keywords: gaussian splatting, ar, geometry, autonomous driving, 3d gaussian  
- **[GSFF-SLAM: 3D Semantic Gaussian Splatting SLAM via Feature Field](https://arxiv.org/abs/2504.19409v1)**  
  Authors: Zuxing Lu, Xin Yuan, Shaowen Yang, Jingyu Liu, Jiawei Wang, Changyin Sun  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.19409v1.pdf)  
  Keywords: gaussian splatting, semantic, ar, segmentation, geometry, mapping, slam, 3d gaussian, tracking  
- **[IM-Portrait: Learning 3D-aware Video Diffusion for Photorealistic Talking Heads from Monocular Videos](https://arxiv.org/abs/2504.19165v2)**  
  Authors: Yuan Li, Ziqian Bai, Feitong Tan, Zhaopeng Cui, Sean Fanello, Yinda Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.19165v2.pdf)  
  Keywords: ar, avatar, 3d reconstruction, head, nerf, 3d gaussian, vr, efficient  
- **[RGS-DR: Reflective Gaussian Surfels with Deferred Rendering for Shiny Objects](https://arxiv.org/abs/2504.18468v2)**  
  Authors: Georgios Kouros, Minye Wu, Tinne Tuytelaars  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.18468v2.pdf)  
  Keywords: gaussian splatting, reflection, ar, geometry, face, nerf, 3d gaussian, lighting, relighting  
- **[PerfCam: Digital Twinning for Production Lines Using 3D Gaussian Splatting and Vision Models](https://arxiv.org/abs/2504.18165v1)**  
  Authors: Michel Gokan Khan, Renan Guarese, Fabian Johnson, Xi Vincent Wang, Anders Bergman, Benjamin Edvinsson, Mario Romero, Jérémy Vachier, Jan Kronqvist  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.18165v1.pdf)  
  Keywords: gaussian splatting, ar, mapping, 3d reconstruction, 3d gaussian, tracking  
- **[When Gaussian Meets Surfel: Ultra-fast High-fidelity Radiance Field Rendering](https://arxiv.org/abs/2504.17545v1)**  
  Authors: Keyang Ye, Tianjia Shao, Kun Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.17545v1.pdf)  
  Keywords: high-fidelity, fast, compact, ar, geometry, 3d gaussian  

### Large Scene

*Showing the latest 50 out of 92 papers*

- **[HUG: Hierarchical Urban Gaussian Splatting with Block-Based Reconstruction](https://arxiv.org/abs/2504.16606v1)**  
  Authors: Zhongtao Wang, Mai Su, Huishan Au, Yilong Li, Xizhe Cao, Chengwei Pan, Yisong Chen, Guoping Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.16606v1.pdf)  
  Keywords: gaussian splatting, urban scene, ar, 3d gaussian, efficient  
- **[EG-Gaussian: Epipolar Geometry and Graph Network Enhanced 3D Gaussian Splatting](https://arxiv.org/abs/2504.13540v1)**  
  Authors: Beizhen Zhao, Yifan Zhou, Zijian Wang, Hao Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.13540v1.pdf)  
  Keywords: gaussian splatting, sparse-view, ar, geometry, outdoor, 3d gaussian, efficient  
- **[You Need a Transition Plane: Bridging Continuous Panoramic 3D Reconstruction with Perspective Gaussian Splatting](https://arxiv.org/abs/2504.09062v1)**  
  Authors: Zhijie Shen, Chunyu Lin, Shujuan Huang, Lang Nie, Kang Liao, Yao Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.09062v1.pdf) | [![GitHub](https://img.shields.io/github/stars/zhijieshen-bjtu/TPGS?style=social)](https://github.com/zhijieshen-bjtu/TPGS)  
  Keywords: gaussian splatting, ar, face, outdoor, 3d reconstruction, 3d gaussian  
- **[FIORD: A Fisheye Indoor-Outdoor Dataset with LIDAR Ground Truth for 3D Scene Reconstruction and Benchmarking](https://arxiv.org/abs/2504.01732v2)**  
  Authors: Ulas Gunes, Matias Turkulainen, Xuqian Ren, Arno Solin, Juho Kannala, Esa Rahtu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.01732v2.pdf)  
  Keywords: gaussian splatting, reflection, ar, motion, outdoor, nerf  
- **[UnIRe: Unsupervised Instance Decomposition for Dynamic Urban Scene Reconstruction](https://arxiv.org/abs/2504.00763v1)**  
  Authors: Yunxuan Mao, Rong Xiong, Yue Wang, Yiyi Liao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.00763v1.pdf)  
  Keywords: dynamic, gaussian splatting, urban scene, ar, 4d, autonomous driving, 3d gaussian  
- **[RainyGS: Efficient Rain Synthesis with Physically-Based Gaussian Splatting](https://arxiv.org/abs/2503.21442v2)**  
  Authors: Qiyu Dai, Xingyu Ni, Qianfan Shen, Wenzheng Chen, Baoquan Chen, Mengyu Chu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.21442v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://pku-vcl-geometry.github.io/RainyGS/)  
  Keywords: high-fidelity, gaussian splatting, fast, dynamic, reflection, ar, geometry, outdoor, nerf, efficient  
- **[StyledStreets: Multi-style Street Simulator with Spatial and Temporal Consistency](https://arxiv.org/abs/2503.21104v1)**  
  Authors: Yuyin Chen, Yida Wang, Xueyang Zhang, Kun Zhan, Peng Jia, Yifei Zhan, Xianpeng Lang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.21104v1.pdf)  
  Keywords: dynamic, gaussian splatting, urban scene, ar, geometry, motion  
- **[EVolSplat: Efficient Volume-based Gaussian Splatting for Urban View Synthesis](https://arxiv.org/abs/2503.20168v1)**  
  Authors: Sheng Miao, Jiaxin Huang, Dongfeng Bai, Xu Yan, Hongyu Zhou, Yue Wang, Bingbing Liu, Andreas Geiger, Yiyi Liao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.20168v1.pdf)  
  Keywords: fast, gaussian splatting, urban scene, nerf, ar, autonomous driving, real-time rendering, 3d gaussian, efficient  
- **[SparseGS-W: Sparse-View 3D Gaussian Splatting in the Wild with Generative Priors](https://arxiv.org/abs/2503.19452v1)**  
  Authors: Yiqing Li, Xuan Wang, Jiawei Wu, Yikun Ma, Zhi Jin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.19452v1.pdf)  
  Keywords: gaussian splatting, sparse-view, illumination, ar, outdoor, 3d gaussian  
- **[From Sparse to Dense: Camera Relocalization with Scene-Specific Detector from Feature Gaussian Splatting](https://arxiv.org/abs/2503.19358v1)**  
  Authors: Zhiwei Huang, Hailin Yu, Yichun Shentu, Jin Yuan, Guofeng Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.19358v1.pdf)  
  Keywords: localization, gaussian splatting, ar, outdoor, efficient  

### Model Compression

*Showing the latest 50 out of 653 papers*

- **[GauSS-MI: Gaussian Splatting Shannon Mutual Information for Active 3D Reconstruction](https://arxiv.org/abs/2504.21067v1)**  
  Authors: Yuhan Xie, Yixi Cai, Yinqiang Zhang, Lei Yang, Jia Pan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.21067v1.pdf)  
  Keywords: gaussian splatting, ar, motion, 3d reconstruction, nerf, 3d gaussian, efficient  
- **[EfficientHuman: Efficient Training and Reconstruction of Moving Human using Articulated 2D Gaussian](https://arxiv.org/abs/2504.20607v1)**  
  Authors: Hao Tian, Rui Liu, Wen Shen, Yilong Hu, Zhihao Zheng, Xiaolin Qin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.20607v1.pdf)  
  Keywords: dynamic, fast, gaussian splatting, human, ar, face, body, 3d gaussian, efficient  
- **[Mesh-Learner: Texturing Mesh with Spherical Harmonics](https://arxiv.org/abs/2504.19938v1)**  
  Authors: Yunfei Wan, Jianheng Liu, Jiarong Lin, Fu Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.19938v1.pdf) | [![GitHub](https://img.shields.io/github/stars/hku-mars/Mesh-Learner?style=social)](https://github.com/hku-mars/Mesh-Learner)  
  Keywords: fast, gaussian splatting, ar, mapping, 3d reconstruction, robotics, 3d gaussian, efficient  
- **[IM-Portrait: Learning 3D-aware Video Diffusion for Photorealistic Talking Heads from Monocular Videos](https://arxiv.org/abs/2504.19165v2)**  
  Authors: Yuan Li, Ziqian Bai, Feitong Tan, Zhaopeng Cui, Sean Fanello, Yinda Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.19165v2.pdf)  
  Keywords: ar, avatar, 3d reconstruction, head, nerf, 3d gaussian, vr, efficient  
- **[4DGS-CC: A Contextual Coding Framework for 4D Gaussian Splatting Data Compression](https://arxiv.org/abs/2504.18925v2)**  
  Authors: Zicong Chen, Zhenghao Chen, Wei Jiang, Wei Wang, Lei Liu, Dong Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.18925v2.pdf)  
  Keywords: dynamic, gaussian splatting, compression, ar, 4d, 3d gaussian  
- **[TransparentGS: Fast Inverse Rendering of Transparent Objects with Gaussians](https://arxiv.org/abs/2504.18768v2)**  
  Authors: Letian Huang, Dongwei Ye, Jialin Dan, Chengzhi Tao, Huiwen Liu, Kun Zhou, Bo Ren, Yuanqi Li, Yanwen Guo, Jie Guo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.18768v2.pdf)  
  Keywords: fast, gaussian splatting, reflection, ar, 3d gaussian, efficient  
- **[When Gaussian Meets Surfel: Ultra-fast High-fidelity Radiance Field Rendering](https://arxiv.org/abs/2504.17545v1)**  
  Authors: Keyang Ye, Tianjia Shao, Kun Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.17545v1.pdf)  
  Keywords: high-fidelity, fast, compact, ar, geometry, 3d gaussian  
- **[Gaussian Splatting is an Effective Data Generator for 3D Object Detection](https://arxiv.org/abs/2504.16740v1)**  
  Authors: Farhad G. Zanjani, Davide Abati, Auke Wiggers, Dimitris Kalatzis, Jens Petersen, Hong Cai, Amirhossein Habibian  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.16740v1.pdf)  
  Keywords: gaussian splatting, ar, 3d reconstruction, autonomous driving, efficient  
- **[PIN-WM: Learning Physics-INformed World Models for Non-Prehensile Manipulation](https://arxiv.org/abs/2504.16693v1)**  
  Authors: Wenxuan Li, Hang Zhao, Zhiyuan Yu, Yu Du, Qin Zou, Ruizhen Hu, Kai Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.16693v1.pdf)  
  Keywords: dynamic, gaussian splatting, few-shot, ar, body, efficient  
- **[HUG: Hierarchical Urban Gaussian Splatting with Block-Based Reconstruction](https://arxiv.org/abs/2504.16606v1)**  
  Authors: Zhongtao Wang, Mai Su, Huishan Au, Yilong Li, Xizhe Cao, Chengwei Pan, Yisong Chen, Guoping Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.16606v1.pdf)  
  Keywords: gaussian splatting, urban scene, ar, 3d gaussian, efficient  

### Quality Enhancement

*Showing the latest 50 out of 274 papers*

- **[HoloTime: Taming Video Diffusion Models for Panoramic 4D Scene Generation](https://arxiv.org/abs/2504.21650v1)**  
  Authors: Haiyang Zhou, Wangbo Yu, Jiawen Guan, Xinhua Cheng, Yonghong Tian, Li Yuan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.21650v1.pdf)  
  Keywords: dynamic, high-fidelity, gaussian splatting, ar, 4d, vr  
- **[STP4D: Spatio-Temporal-Prompt Consistent Modeling for Text-to-4D Gaussian Splatting](https://arxiv.org/abs/2504.18318v1)**  
  Authors: Yunze Deng, Haijun Xiong, Bin Feng, Xinggang Wang, Wenyu Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.18318v1.pdf)  
  Keywords: high-fidelity, gaussian splatting, deformation, ar, 4d, real-time rendering  
- **[When Gaussian Meets Surfel: Ultra-fast High-fidelity Radiance Field Rendering](https://arxiv.org/abs/2504.17545v1)**  
  Authors: Keyang Ye, Tianjia Shao, Kun Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.17545v1.pdf)  
  Keywords: high-fidelity, fast, compact, ar, geometry, 3d gaussian  
- **[StyleMe3D: Stylization with Disentangled Priors by Multiple Encoders on 3D Gaussians](https://arxiv.org/abs/2504.15281v1)**  
  Authors: Cailin Zhuang, Yaoqi Hu, Xuanyang Zhang, Wei Cheng, Jiacheng Bao, Shengqi Liu, Yiying Yang, Xianfang Zeng, Gang Yu, Ming Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.15281v1.pdf)  
  Keywords: dynamic, gaussian splatting, human, nerf, semantic, ar, quality enhancement, real-time rendering, 3d gaussian, lighting  
- **[CAGE-GS: High-fidelity Cage Based 3D Gaussian Splatting Deformation](https://arxiv.org/abs/2504.12800v1)**  
  Authors: Yifei Tong, Runze Tian, Xiao Han, Dingyao Liu, Fenggen Yu, Yan Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.12800v1.pdf)  
  Keywords: high-fidelity, gaussian splatting, deformation, ar, 3d gaussian  
- **[3DAffordSplat: Efficient Affordance Reasoning with 3D Gaussians](https://arxiv.org/abs/2504.11218v2)**  
  Authors: Zeming Wei, Junyi Lin, Yang Liu, Weixing Chen, Jingzhou Luo, Guanbin Li, Liang Lin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.11218v2.pdf)  
  Keywords: high-fidelity, gaussian splatting, human, ar, head, real-time rendering, 3d gaussian, lighting, recognition, efficient  
- **[MCBlock: Boosting Neural Radiance Field Training Speed by MCTS-based Dynamic-Resolution Ray Sampling](https://arxiv.org/abs/2504.09878v1)**  
  Authors: Yunpeng Tan, Junlin Hao, Jiangkai Wu, Liming Liu, Qingyang Li, Xinggong Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.09878v1.pdf)  
  Keywords: high-fidelity, gaussian splatting, dynamic, acceleration, ar, nerf, efficient  
- **[TextSplat: Text-Guided Semantic Fusion for Generalizable Gaussian Splatting](https://arxiv.org/abs/2504.09588v1)**  
  Authors: Zhicong Wu, Hongbin Xu, Gang Xu, Ping Nie, Zhixin Yan, Jinkai Zheng, Liangqiong Qu, Ming Li, Liqiang Nie  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.09588v1.pdf)  
  Keywords: high-fidelity, gaussian splatting, semantic, ar, segmentation, 3d reconstruction, 3d gaussian, understanding  
- **[A Constrained Optimization Approach for Gaussian Splatting from Coarsely-posed Images and Noisy Lidar Point Clouds](https://arxiv.org/abs/2504.09129v1)**  
  Authors: Jizong Peng, Tze Ho Elden Tse, Kai Xu, Wenchao Gao, Angela Yao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.09129v1.pdf)  
  Keywords: high-fidelity, gaussian splatting, ar, geometry, motion, 3d reconstruction, 3d gaussian  
- **[ContrastiveGaussian: High-Fidelity 3D Generation with Contrastive Learning and Gaussian Splatting](https://arxiv.org/abs/2504.08100v1)**  
  Authors: Junbang Liu, Enpei Huang, Dongxing Mao, Hui Zhang, Xinyuan Song, Yongxin Ni  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.08100v1.pdf)  
  Keywords: high-fidelity, gaussian splatting, ar  

### Ray Tracing

- **[DNF-Avatar: Distilling Neural Fields for Real-time Animatable Avatar Relighting](https://arxiv.org/abs/2504.10486v1)**  
  Authors: Zeren Jiang, Shaofei Wang, Siyu Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.10486v1.pdf)  
  Keywords: fast, gaussian splatting, human, ar, ray tracing, geometry, avatar, lighting, relightable, relighting, shadow  
- **[Stochastic Ray Tracing of 3D Transparent Gaussians](https://arxiv.org/abs/2504.06598v2)**  
  Authors: Xin Sun, Iliyan Georgiev, Yun Fei, Miloš Hašan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.06598v2.pdf)  
  Keywords: gaussian splatting, acceleration, ar, ray tracing, efficient rendering, 3d gaussian, lighting, relighting, efficient  
- **[3D Gaussian Particle Approximation of VDB Datasets: A Study for Scientific Visualization](https://arxiv.org/abs/2504.04857v2)**  
  Authors: Isha Sharma, Dieter Schmalstieg  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.04857v2.pdf)  
  Keywords: dynamic, gaussian splatting, compact, acceleration, ar, animation, 3d gaussian, ray marching, efficient  
- **[3D Gaussian Inverse Rendering with Approximated Global Illumination](https://arxiv.org/abs/2504.01358v1)**  
  Authors: Zirui Wu, Jianteng Chen, Laijian Li, Shaoteng Wu, Zhikai Zhu, Kang Xu, Martin R. Oswald, Jie Song  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.01358v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://wuzirui.github.io/gs-ssr.)  
  Keywords: gaussian splatting, illumination, ar, ray tracing, face, real-time rendering, 3d gaussian, lighting, efficient, global illumination  
- **[Real-time Global Illumination for Dynamic 3D Gaussian Scenes](https://arxiv.org/abs/2503.17897v1)**  
  Authors: Chenxiao Hu, Meng Gai, Guoping Wang, Sheng Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.17897v1.pdf)  
  Keywords: fast, dynamic, illumination, face, real-time rendering, 3d gaussian, lighting, light transport, global illumination  
- **[REdiSplats: Ray Tracing for Editable Gaussian Splatting](https://arxiv.org/abs/2503.12284v1)**  
  Authors: Krzysztof Byrski, Grzegorz Wilczyński, Weronika Smolak-Dyżewska, Piotr Borycki, Dawid Baran, Sławomir Tadeja, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.12284v1.pdf)  
  Keywords: fast, gaussian splatting, neural rendering, reflection, ar, ray tracing, 3d gaussian, shadow  
- **[BEAM: Bridging Physically-based Rendering and Gaussian Modeling for Relightable Volumetric Video](https://arxiv.org/abs/2502.08297v1)**  
  Authors: Yu Hong, Yize Wu, Zhehao Shen, Chengcheng Guo, Yuheng Jiang, Yingliang Zhang, Jingyi Yu, Lan Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.08297v1.pdf)  
  Keywords: dynamic, ar, ray tracing, geometry, face, tracking, 4d, real-time rendering, lighting, relightable, efficient  
- **[MeshSplats: Mesh-Based Rendering with Gaussian Splatting Initialization](https://arxiv.org/abs/2502.07754v1)**  
  Authors: Rafał Tobiasz, Grzegorz Wilczyński, Marcin Mazur, Sławomir Tadeja, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.07754v1.pdf)  
  Keywords: gaussian splatting, reflection, ray tracing, face, lighting, shadow  
- **[Scalable 3D Gaussian Splatting-Based RF Signal Spatial Propagation Modeling](https://arxiv.org/abs/2502.01826v1)**  
  Authors: Kang Yang, Gaofeng Dong, Sijie Ji, Wan Du, Mani Srivastava  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.01826v1.pdf)  
  Keywords: gaussian splatting, ar, ray tracing, 3d gaussian, survey  
- **[Radiant Foam: Real-Time Differentiable Ray Tracing](https://arxiv.org/abs/2502.01157v1)**  
  Authors: Shrisudhan Govindarajan, Daniel Rebain, Kwang Moo Yi, Andrea Tagliasacchi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.01157v1.pdf)  
  Keywords: gaussian splatting, acceleration, reflection, ray tracing, ar, light transport, efficient  

### Relighting

*Showing the latest 50 out of 197 papers*

- **[TransparentGS: Fast Inverse Rendering of Transparent Objects with Gaussians](https://arxiv.org/abs/2504.18768v2)**  
  Authors: Letian Huang, Dongwei Ye, Jialin Dan, Chengzhi Tao, Huiwen Liu, Kun Zhou, Bo Ren, Yuanqi Li, Yanwen Guo, Jie Guo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.18768v2.pdf)  
  Keywords: fast, gaussian splatting, reflection, ar, 3d gaussian, efficient  
- **[RGS-DR: Reflective Gaussian Surfels with Deferred Rendering for Shiny Objects](https://arxiv.org/abs/2504.18468v2)**  
  Authors: Georgios Kouros, Minye Wu, Tinne Tuytelaars  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.18468v2.pdf)  
  Keywords: gaussian splatting, reflection, ar, geometry, face, nerf, 3d gaussian, lighting, relighting  
- **[iVR-GS: Inverse Volume Rendering for Explorable Visualization via Editable 3D Gaussian Splatting](https://arxiv.org/abs/2504.17954v1)**  
  Authors: Kaiyuan Tang, Siyuan Yao, Chaoli Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.17954v1.pdf) | [![GitHub](https://img.shields.io/github/stars/TouKaienn/iVR-GS?style=social)](https://github.com/TouKaienn/iVR-GS)  
  Keywords: fast, gaussian splatting, ar, mapping, vr, nerf, 3d gaussian, lighting  
- **[StyleMe3D: Stylization with Disentangled Priors by Multiple Encoders on 3D Gaussians](https://arxiv.org/abs/2504.15281v1)**  
  Authors: Cailin Zhuang, Yaoqi Hu, Xuanyang Zhang, Wei Cheng, Jiacheng Bao, Shengqi Liu, Yiying Yang, Xianfang Zeng, Gang Yu, Ming Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.15281v1.pdf)  
  Keywords: dynamic, gaussian splatting, human, nerf, semantic, ar, quality enhancement, real-time rendering, 3d gaussian, lighting  
- **[Immersive Teleoperation Framework for Locomanipulation Tasks](https://arxiv.org/abs/2504.15229v1)**  
  Authors: Takuya Boehringer, Jonathan Embley-Riches, Karim Hammoud, Valerio Modugno, Dimitrios Kanoulas  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.15229v1.pdf)  
  Keywords: fast, gaussian splatting, ar, face, vr, lighting  
- **[Metamon-GS: Enhancing Representability with Variance-Guided Densification and Light Encoding](https://arxiv.org/abs/2504.14460v1)**  
  Authors: Junyan Su, Baozhu Zhao, Xiaohan Zhang, Qi Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.14460v1.pdf)  
  Keywords: ar, gaussian splatting, 3d gaussian, lighting  
- **[SLAM&Render: A Benchmark for the Intersection Between Neural Rendering, Gaussian Splatting and SLAM](https://arxiv.org/abs/2504.13713v2)**  
  Authors: Samuel Cerezo, Gaetano Meli, Tomás Berriel Martins, Kirill Safronov, Javier Civera  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.13713v2.pdf)  
  Keywords: localization, gaussian splatting, neural rendering, illumination, ar, mapping, slam, nerf, lighting  
- **[Novel Demonstration Generation with Gaussian Splatting Enables Robust One-Shot Manipulation](https://arxiv.org/abs/2504.13175v1)**  
  Authors: Sizhe Yang, Wenye Yu, Jia Zeng, Jun Lv, Kerui Ren, Cewu Lu, Dahua Lin, Jiangmiao Pang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.13175v1.pdf)  
  Keywords: gaussian splatting, ar, face, 3d gaussian, lighting  
- **[Digital Twin Generation from Visual Data: A Survey](https://arxiv.org/abs/2504.13159v1)**  
  Authors: Andrew Melnik, Benjamin Alt, Giang Nguyen, Artur Wilkowski, Maciej Stefańczyk, Qirui Wu, Sinan Harms, Helge Rhodin, Manolis Savva, Michael Beetz  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.13159v1.pdf) | [![GitHub](https://img.shields.io/github/stars/ndrwmlnk/awesome-digital-twins?style=social)](https://github.com/ndrwmlnk/awesome-digital-twins)  
  Keywords: gaussian splatting, semantic, ar, segmentation, robotics, 3d gaussian, lighting, survey  
- **[GSAC: Leveraging Gaussian Splatting for Photorealistic Avatar Creation with Unity Integration](https://arxiv.org/abs/2504.12999v1)**  
  Authors: Rendong Zhang, Alexandra Watkins, Nilanjan Sarkar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.12999v1.pdf)  
  Keywords: gaussian splatting, human, ar, face, avatar, vr, nerf, 3d gaussian, lighting, efficient  

### SLAM

*Showing the latest 50 out of 256 papers*

- **[Creating Your Editable 3D Photorealistic Avatar with Tetrahedron-constrained Gaussian Splatting](https://arxiv.org/abs/2504.20403v1)**  
  Authors: Hanxi Liu, Yifang Men, Zhouhui Lian  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.20403v1.pdf)  
  Keywords: localization, gaussian splatting, ar, geometry, avatar, 3d gaussian, vr  
- **[GSFeatLoc: Visual Localization Using Feature Correspondence on 3D Gaussian Splatting](https://arxiv.org/abs/2504.20379v2)**  
  Authors: Jongwon Lee, Timothy Bretl  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.20379v2.pdf)  
  Keywords: fast, gaussian splatting, localization, ar, nerf, 3d gaussian  
- **[Mesh-Learner: Texturing Mesh with Spherical Harmonics](https://arxiv.org/abs/2504.19938v1)**  
  Authors: Yunfei Wan, Jianheng Liu, Jiarong Lin, Fu Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.19938v1.pdf) | [![GitHub](https://img.shields.io/github/stars/hku-mars/Mesh-Learner?style=social)](https://github.com/hku-mars/Mesh-Learner)  
  Keywords: fast, gaussian splatting, ar, mapping, 3d reconstruction, robotics, 3d gaussian, efficient  
- **[GSFF-SLAM: 3D Semantic Gaussian Splatting SLAM via Feature Field](https://arxiv.org/abs/2504.19409v1)**  
  Authors: Zuxing Lu, Xin Yuan, Shaowen Yang, Jingyu Liu, Jiawei Wang, Changyin Sun  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.19409v1.pdf)  
  Keywords: gaussian splatting, semantic, ar, segmentation, geometry, mapping, slam, 3d gaussian, tracking  
- **[PerfCam: Digital Twinning for Production Lines Using 3D Gaussian Splatting and Vision Models](https://arxiv.org/abs/2504.18165v1)**  
  Authors: Michel Gokan Khan, Renan Guarese, Fabian Johnson, Xi Vincent Wang, Anders Bergman, Benjamin Edvinsson, Mario Romero, Jérémy Vachier, Jan Kronqvist  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.18165v1.pdf)  
  Keywords: gaussian splatting, ar, mapping, 3d reconstruction, 3d gaussian, tracking  
- **[iVR-GS: Inverse Volume Rendering for Explorable Visualization via Editable 3D Gaussian Splatting](https://arxiv.org/abs/2504.17954v1)**  
  Authors: Kaiyuan Tang, Siyuan Yao, Chaoli Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.17954v1.pdf) | [![GitHub](https://img.shields.io/github/stars/TouKaienn/iVR-GS?style=social)](https://github.com/TouKaienn/iVR-GS)  
  Keywords: fast, gaussian splatting, ar, mapping, vr, nerf, 3d gaussian, lighting  
- **[ToF-Splatting: Dense SLAM using Sparse Time-of-Flight Depth and Multi-Frame Integration](https://arxiv.org/abs/2504.16545v1)**  
  Authors: Andrea Conti, Matteo Poggi, Valerio Cambareri, Martin R. Oswald, Stefano Mattoccia  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.16545v1.pdf)  
  Keywords: gaussian splatting, ar, geometry, mapping, vr, slam, 3d gaussian, tracking, efficient  
- **[SmallGS: Gaussian Splatting-based Camera Pose Estimation for Small-Baseline Videos](https://arxiv.org/abs/2504.17810v1)**  
  Authors: Yuxin Yao, Yan Zhang, Zhening Huang, Joan Lasenby  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.17810v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://yuxinyao620.github.io/SmallGS)  
  Keywords: dynamic, gaussian splatting, ar, motion, slam  
- **[NVSMask3D: Hard Visual Prompting with Camera Pose Interpolation for 3D Open Vocabulary Instance Segmentation](https://arxiv.org/abs/2504.14638v1)**  
  Authors: Junyuan Fang, Zihan Wang, Yejun Zhang, Shuzhe Wang, Iaroslav Melekhov, Juho Kannala  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.14638v1.pdf)  
  Keywords: localization, gaussian splatting, ar, segmentation, 3d gaussian, recognition  
- **[SLAM&Render: A Benchmark for the Intersection Between Neural Rendering, Gaussian Splatting and SLAM](https://arxiv.org/abs/2504.13713v2)**  
  Authors: Samuel Cerezo, Gaetano Meli, Tomás Berriel Martins, Kirill Safronov, Javier Civera  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.13713v2.pdf)  
  Keywords: localization, gaussian splatting, neural rendering, illumination, ar, mapping, slam, nerf, lighting  

### Scene Understanding

*Showing the latest 50 out of 305 papers*

- **[GSFF-SLAM: 3D Semantic Gaussian Splatting SLAM via Feature Field](https://arxiv.org/abs/2504.19409v1)**  
  Authors: Zuxing Lu, Xin Yuan, Shaowen Yang, Jingyu Liu, Jiawei Wang, Changyin Sun  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.19409v1.pdf)  
  Keywords: gaussian splatting, semantic, ar, segmentation, geometry, mapping, slam, 3d gaussian, tracking  
- **[Visibility-Uncertainty-guided 3D Gaussian Inpainting via Scene Conceptional Learning](https://arxiv.org/abs/2504.17815v1)**  
  Authors: Mingxuan Cui, Qing Guo, Yuyi Wang, Hongkai Yu, Di Lin, Qin Zou, Ming-Ming Cheng, Xi Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.17815v1.pdf)  
  Keywords: dynamic, fast, gaussian splatting, semantic, ar, nerf, 3d gaussian, efficient  
- **[Text-based Animatable 3D Avatars with Morphable Model Alignment](https://arxiv.org/abs/2504.15835v1)**  
  Authors: Yiqian Wu, Malte Prinzler, Xiaogang Jin, Siyu Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.15835v1.pdf)  
  Keywords: dynamic, semantic, ar, geometry, avatar, animation, head  
- **[StyleMe3D: Stylization with Disentangled Priors by Multiple Encoders on 3D Gaussians](https://arxiv.org/abs/2504.15281v1)**  
  Authors: Cailin Zhuang, Yaoqi Hu, Xuanyang Zhang, Wei Cheng, Jiacheng Bao, Shengqi Liu, Yiying Yang, Xianfang Zeng, Gang Yu, Ming Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.15281v1.pdf)  
  Keywords: dynamic, gaussian splatting, human, nerf, semantic, ar, quality enhancement, real-time rendering, 3d gaussian, lighting  
- **[NVSMask3D: Hard Visual Prompting with Camera Pose Interpolation for 3D Open Vocabulary Instance Segmentation](https://arxiv.org/abs/2504.14638v1)**  
  Authors: Junyuan Fang, Zihan Wang, Yejun Zhang, Shuzhe Wang, Iaroslav Melekhov, Juho Kannala  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.14638v1.pdf)  
  Keywords: localization, gaussian splatting, ar, segmentation, 3d gaussian, recognition  
- **[RoboOcc: Enhancing the Geometric and Semantic Scene Understanding for Robots](https://arxiv.org/abs/2504.14604v1)**  
  Authors: Zhang Zhang, Qiang Zhang, Wei Cui, Shuai Shi, Yijie Guo, Gang Han, Wen Zhao, Hengle Ren, Renjing Xu, Jian Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.14604v1.pdf)  
  Keywords: semantic, ar, geometry, 3d gaussian, understanding  
- **[ODHSR: Online Dense 3D Reconstruction of Humans and Scenes from Monocular Videos](https://arxiv.org/abs/2504.13167v2)**  
  Authors: Zetong Zhang, Manuel Kaufmann, Lixin Xue, Jie Song, Martin R. Oswald  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.13167v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://eth-ait.github.io/ODHSR.)  
  Keywords: gaussian splatting, neural rendering, human, deformation, ar, 3d reconstruction, 3d gaussian, tracking, understanding, efficient  
- **[Digital Twin Generation from Visual Data: A Survey](https://arxiv.org/abs/2504.13159v1)**  
  Authors: Andrew Melnik, Benjamin Alt, Giang Nguyen, Artur Wilkowski, Maciej Stefańczyk, Qirui Wu, Sinan Harms, Helge Rhodin, Manolis Savva, Michael Beetz  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.13159v1.pdf) | [![GitHub](https://img.shields.io/github/stars/ndrwmlnk/awesome-digital-twins?style=social)](https://github.com/ndrwmlnk/awesome-digital-twins)  
  Keywords: gaussian splatting, semantic, ar, segmentation, robotics, 3d gaussian, lighting, survey  
- **[Training-Free Hierarchical Scene Understanding for Gaussian Splatting with Superpoint Graphs](https://arxiv.org/abs/2504.13153v1)**  
  Authors: Shaohui Dai, Yansong Qu, Zheyan Li, Xinyang Li, Shengchuan Zhang, Liujuan Cao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.13153v1.pdf) | [![GitHub](https://img.shields.io/github/stars/Atrovast/THGS?style=social)](https://github.com/Atrovast/THGS)  
  Keywords: fast, gaussian splatting, compact, semantic, ar, segmentation, geometry, 3d gaussian, understanding, efficient  
- **[Mind2Matter: Creating 3D Models from EEG Signals](https://arxiv.org/abs/2504.11936v2)**  
  Authors: Xia Deng, Shen Chen, Jiale Zhou, Lei Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.11936v2.pdf) | [![GitHub](https://img.shields.io/github/stars/sddwwww/Mind2Matter?style=social)](https://github.com/sddwwww/Mind2Matter)  
  Keywords: semantic, ar, face, 3d reconstruction, 3d gaussian  



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