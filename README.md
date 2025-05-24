# Awesome Gaussian Splatting [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of latest research papers, projects and resources related to Gaussian Splatting. Content is automatically updated daily.

> Last Update: 2025-05-24 00:52:36

## Categories

- [3DGS Surveys](#3dgs-surveys) (34 papers) - Survey papers and benchmarks about 3D Gaussian Splatting
- [Acceleration](#acceleration) (510 papers) - Papers about speeding up rendering or training
- [Applications](#applications) (1791 papers) - Papers about specific applications
- [Avatar Generation](#avatar-generation) (604 papers) - Papers about human avatar generation
- [Dynamic Scene](#dynamic-scene) (678 papers) - Papers about dynamic scene reconstruction and rendering
- [Few-shot](#few-shot) (128 papers) - Papers about few-shot or sparse view reconstruction
- [Geometry Reconstruction](#geometry-reconstruction) (581 papers) - Papers about 3D geometry reconstruction
- [Large Scene](#large-scene) (101 papers) - Papers about large-scale scene reconstruction
- [Model Compression](#model-compression) (682 papers) - Papers about model compression and optimization
- [Quality Enhancement](#quality-enhancement) (287 papers) - Papers focusing on improving rendering quality
- [Ray Tracing](#ray-tracing) (40 papers) - Papers about ray tracing and ray casting in Gaussian Splatting
- [Relighting](#relighting) (201 papers) - Papers about relighting and illumination effects in Gaussian Splatting
- [SLAM](#slam) (267 papers) - Papers about SLAM using Gaussian Splatting
- [Scene Understanding](#scene-understanding) (321 papers) - Papers about scene understanding and semantic analysis



## Table of Contents

- [Categorized Papers](#categorized-papers)
- [Classic Papers](#classic-papers)
- [Open Source Projects](#open-source-projects)
- [Applications](#applications)
- [Tutorials & Blogs](#tutorials--blogs)





## Categorized Papers

### 3DGS Surveys

- **[Is Semantic SLAM Ready for Embedded Systems ? A Comparative Survey](https://arxiv.org/abs/2505.12384v1)**  
  Authors: Calvin Galagain, Martyna Poreba, François Goulette  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.12384v1.pdf)  
  Keywords: efficient, nerf, survey, 3d gaussian, ar, segmentation, localization, gaussian splatting, semantic, slam, mapping  
- **[Advances in Radiance Field for Dynamic Scene: From Neural Field to Gaussian Field](https://arxiv.org/abs/2505.10049v2)**  
  Authors: Jinlong Fan, Xuepu Zeng, Jing Zhang, Mingming Gong, Yuxiang Yang, Dacheng Tao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.10049v2.pdf)  
  Keywords: survey, 3d gaussian, motion, ar, body, gaussian splatting, 4d, understanding, dynamic  
- **[A Survey of 3D Reconstruction with Event Cameras: From Event-based Geometry to Neural 3D Rendering](https://arxiv.org/abs/2505.08438v1)**  
  Authors: Chuanzhi Xu, Haoxian Zhou, Langyi Chen, Haodong Chen, Ying Zhou, Vera Chung, Qiang Qu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.08438v1.pdf)  
  Keywords: 3d reconstruction, survey, 3d gaussian, motion, ar, neural rendering, gaussian splatting, geometry, dynamic  
- **[UltraGauss: Ultrafast Gaussian Reconstruction of 3D Ultrasound Volumes](https://arxiv.org/abs/2505.05643v1)**  
  Authors: Mark C. Eid, Ana I. L. Namburete, João F. Henriques  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.05643v1.pdf)  
  Keywords: 3d reconstruction, efficient, survey, ar, gaussian splatting, fast  
- **[3D Scene Generation: A Survey](https://arxiv.org/abs/2505.05474v1)**  
  Authors: Beichen Wen, Haozhe Xie, Zhaoxi Chen, Fangzhou Hong, Ziwei Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.05474v1.pdf) | [![GitHub](https://img.shields.io/github/stars/hzxie/Awesome-3D-Scene-Generation?style=social)](https://github.com/hzxie/Awesome-3D-Scene-Generation)  
  Keywords: nerf, survey, 3d gaussian, autonomous driving, ar, semantic, robotics  
- **[Visual enhancement and 3D representation for underwater scenes: a review](https://arxiv.org/abs/2505.01869v1)**  
  Authors: Guoxi Huang, Haoran Wang, Brett Seymour, Evan Kovacs, John Ellerbrock, Dave Blackham, Nantheera Anantrasirichai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.01869v1.pdf)  
  Keywords: 3d reconstruction, survey, 3d gaussian, ar, lighting  
- **[A Survey on 3D Reconstruction Techniques in Plant Phenotyping: From Classical Methods to Neural Radiance Fields (NeRF), 3D Gaussian Splatting (3DGS), and Beyond](https://arxiv.org/abs/2505.00737v1)**  
  Authors: Jiajia Li, Xinda Qi, Seyed Hamidreza Nabaei, Meiqi Liu, Dong Chen, Xin Zhang, Xunyuan Yin, Zhaojian Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.00737v1.pdf) | [![GitHub](https://img.shields.io/github/stars/JiajiaLi04/3D-Reconstruction-Plants?style=social)](https://github.com/JiajiaLi04/3D-Reconstruction-Plants)  
  Keywords: 3d reconstruction, nerf, survey, outdoor, 3d gaussian, ar, sparse view, gaussian splatting, geometry, face, understanding  
- **[Digital Twin Generation from Visual Data: A Survey](https://arxiv.org/abs/2504.13159v1)**  
  Authors: Andrew Melnik, Benjamin Alt, Giang Nguyen, Artur Wilkowski, Maciej Stefańczyk, Qirui Wu, Sinan Harms, Helge Rhodin, Manolis Savva, Michael Beetz  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.13159v1.pdf) | [![GitHub](https://img.shields.io/github/stars/ndrwmlnk/awesome-digital-twins?style=social)](https://github.com/ndrwmlnk/awesome-digital-twins)  
  Keywords: survey, 3d gaussian, ar, segmentation, gaussian splatting, lighting, semantic, robotics  
- **[A Survey on Event-driven 3D Reconstruction: Development under Different Categories](https://arxiv.org/abs/2503.19753v2)**  
  Authors: Chuanzhi Xu, Haoxian Zhou, Haodong Chen, Vera Chung, Qiang Qu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.19753v2.pdf)  
  Keywords: 3d reconstruction, survey, 3d gaussian, motion, ar, gaussian splatting, lighting, fast, dynamic  
- **[Dynamic Scene Reconstruction: Recent Advance in Real-time Rendering and Streaming](https://arxiv.org/abs/2503.08166v1)**  
  Authors: Jiaxuan Zhu, Hao Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.08166v1.pdf)  
  Keywords: real-time rendering, survey, 3d gaussian, ar, gaussian splatting, dynamic  

### Acceleration

*Showing the latest 50 out of 510 papers*

- **[Hybrid 3D-4D Gaussian Splatting for Fast Dynamic Scene Representation](https://arxiv.org/abs/2505.13215v1)**  
  Authors: Seungjun Oh, Younggeun Lee, Hyejin Jeon, Eunbyung Park  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.13215v1.pdf)  
  Keywords: 3d gaussian, motion, ar, gaussian splatting, head, 4d, fast, high-fidelity, dynamic  
- **[iSegMan: Interactive Segment-and-Manipulate 3D Gaussians](https://arxiv.org/abs/2505.11934v1)**  
  Authors: Yian Zhao, Wanshi Xu, Ruochong Zheng, Pengchong Qiao, Chang Liu, Jie Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.11934v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://zhao-yian.github.io/iSegMan.)  
  Keywords: efficient, 3d gaussian, ar, segmentation, efficient rendering  
- **[GrowSplat: Constructing Temporal Digital Twins of Plants with Gaussian Splats](https://arxiv.org/abs/2505.10923v1)**  
  Authors: Simeon Adebola, Shuangyu Xie, Chung Min Kim, Justin Kerr, Bart M. van Marrewijk, Mieke van Vlaardingen, Tim van Daalen, Robert van Loo, Jose Luis Susa Rincon, Eugen Solowjow, Rick van de Zedde, Ken Goldberg  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.10923v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://berkeleyautomation.github.io/GrowSplat/)  
  Keywords: 3d gaussian, ar, deformation, gaussian splatting, 4d, fast  
- **[EA-3DGS: Efficient and Adaptive 3D Gaussians with Highly Enhanced Quality for outdoor scenes](https://arxiv.org/abs/2505.10787v1)**  
  Authors: Jianlin Guo, Haihong Xiao, Wenxiong Kang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.10787v1.pdf)  
  Keywords: real-time rendering, efficient, nerf, outdoor, 3d gaussian, ar, gaussian splatting, geometry, face  
- **[VRSplat: Fast and Robust Gaussian Splatting for Virtual Reality](https://arxiv.org/abs/2505.10144v1)**  
  Authors: Xuechang Tu, Lukas Radl, Michael Steiner, Markus Steinberger, Bernhard Kerbl, Fernando de la Torre  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.10144v1.pdf)  
  Keywords: efficient, 3d gaussian, ar, gaussian splatting, head, face, fast, vr  
- **[FOCI: Trajectory Optimization on Gaussian Splats](https://arxiv.org/abs/2505.08510v1)**  
  Authors: Mario Gomez Andreu, Maximum Wilder-Smith, Victor Klemm, Vaishakh Patil, Jesus Tordesillas, Marco Hutter  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.08510v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://rffr.leggedrobotics.com/works/foci/)  
  Keywords: 3d reconstruction, nerf, 3d gaussian, ar, gaussian splatting, fast, robotics  
- **[GIFStream: 4D Gaussian-based Immersive Video with Feature Stream](https://arxiv.org/abs/2505.07539v1)**  
  Authors: Hao Li, Sicheng Li, Xiang Gao, Abudouaihati Batuer, Lu Yu, Yiyi Liao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.07539v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://xdimlab.github.io/GIFStream)  
  Keywords: real-time rendering, efficient, motion, deformation, ar, compression, gaussian splatting, 4d, fast  
- **[TUGS: Physics-based Compact Representation of Underwater Scenes by Tensorized Gaussian](https://arxiv.org/abs/2505.08811v1)**  
  Authors: Shijie Lian, Ziyi Zhang, Laurence Tianruo Yang and, Mengyu Ren, Debin Liu, Hua Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.08811v1.pdf)  
  Keywords: efficient, nerf, fast, ar, gaussian splatting, lightweight, face, compact  
- **[Virtualized 3D Gaussians: Flexible Cluster-based Level-of-Detail System for Real-Time Rendering of Composed Scenes](https://arxiv.org/abs/2505.06523v1)**  
  Authors: Xijie Yang, Linning Xu, Lihan Jiang, Dahua Lin, Bo Dai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.06523v1.pdf)  
  Keywords: real-time rendering, efficient, 3d gaussian, ar, gaussian splatting, dynamic  
- **[UltraGauss: Ultrafast Gaussian Reconstruction of 3D Ultrasound Volumes](https://arxiv.org/abs/2505.05643v1)**  
  Authors: Mark C. Eid, Ana I. L. Namburete, João F. Henriques  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.05643v1.pdf)  
  Keywords: 3d reconstruction, efficient, survey, ar, gaussian splatting, fast  

### Applications

*Showing the latest 50 out of 1791 papers*

- **[SHaDe: Compact and Consistent Dynamic 3D Reconstruction via Tri-Plane Deformation and Latent Diffusion](https://arxiv.org/abs/2505.16535v1)**  
  Authors: Asrar Alruwayqi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.16535v1.pdf)  
  Keywords: 3d reconstruction, efficient, sparse-view, motion, deformation, ar, gaussian splatting, head, 4d, compact, dynamic  
- **[Motion Matters: Compact Gaussian Streaming for Free-Viewpoint Video Reconstruction](https://arxiv.org/abs/2505.16533v1)**  
  Authors: Jiacong Chen, Qingyu Mao, Youneng Bao, Xiandong Meng, Fanyang Meng, Ronggang Wang, Yongsheng Liang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.16533v1.pdf)  
  Keywords: efficient, 3d gaussian, motion, ar, dynamic, gaussian splatting, head, face, compact, high-fidelity  
- **[MAGIC: Motion-Aware Generative Inference via Confidence-Guided LLM](https://arxiv.org/abs/2505.16456v1)**  
  Authors: Siwei Meng, Yawei Luo, Ping Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.16456v1.pdf)  
  Keywords: motion, ar, dynamic, 3d gaussian  
- **[RUSplatting: Robust 3D Gaussian Splatting for Sparse-View Underwater Scene Reconstruction](https://arxiv.org/abs/2505.15737v1)**  
  Authors: Zhuodong Jiang, Haoran Wang, Guoxi Huang, Brett Seymour, Nantheera Anantrasirichai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.15737v1.pdf)  
  Keywords: robotics, sparse-view, 3d gaussian, ar, gaussian splatting, high-fidelity  
- **[PlantDreamer: Achieving Realistic 3D Plant Models with Diffusion-Guided Gaussian Splatting](https://arxiv.org/abs/2505.15528v1)**  
  Authors: Zane K J Hartley, Lewis A G Stuart, Andrew P French, Michael P Pound  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.15528v1.pdf)  
  Keywords: 3d gaussian, ar, gaussian splatting, geometry, high-fidelity  
- **[EVA: Expressive Virtual Avatars from Multi-view Videos](https://arxiv.org/abs/2505.15385v1)**  
  Authors: Hendrik Junkawitsch, Guoxing Sun, Heming Zhu, Christian Theobalt, Marc Habermann  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.15385v1.pdf)  
  Keywords: 3d gaussian, motion, deformation, body, ar, neural rendering, avatar, geometry, human, tracking, face, high-fidelity  
- **[R3GS: Gaussian Splatting for Robust Reconstruction and Relocalization in Unconstrained Image Collections](https://arxiv.org/abs/2505.15294v1)**  
  Authors: Xu yan, Zhaohui Wang, Rong Wei, Jingbo Yu, Dong Li, Xiangde Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.15294v1.pdf)  
  Keywords: outdoor, ar, localization, gaussian splatting, lightweight, lighting, human, face  
- **[GS2E: Gaussian Splatting is an Effective Data Generator for Event Stream Generation](https://arxiv.org/abs/2505.15287v1)**  
  Authors: Yuchen Li, Chaoran Feng, Zhenyu Tang, Kaiyuan Deng, Wangbo Yu, Yonghong Tian, Li Yuan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.15287v1.pdf)  
  Keywords: 3d reconstruction, 3d gaussian, motion, ar, gaussian splatting, lighting, high-fidelity  
- **[X-GRM: Large Gaussian Reconstruction Model for Sparse-view X-rays to Computed Tomography](https://arxiv.org/abs/2505.15235v1)**  
  Authors: Yifan Liu, Wuyang Li, Weihao Yu, Chenxin Li, Alexandre Alahi, Max Meng, Yixuan Yuan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.15235v1.pdf) | [![GitHub](https://img.shields.io/github/stars/CUHK-AIM-Group/X-GRM?style=social)](https://github.com/CUHK-AIM-Group/X-GRM)  
  Keywords: ar, sparse-view, efficient, gaussian splatting  
- **[GT^2-GS: Geometry-aware Texture Transfer for Gaussian Splatting](https://arxiv.org/abs/2505.15208v1)**  
  Authors: Wenjie Liu, Zhongliang Liu, Junwei Shu, Changbo Wang, Yang Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.15208v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://vpx-ecnu.github.io/GT2-GS-website.)  
  Keywords: geometry, ar, human, gaussian splatting  

### Avatar Generation

*Showing the latest 50 out of 604 papers*

- **[SHaDe: Compact and Consistent Dynamic 3D Reconstruction via Tri-Plane Deformation and Latent Diffusion](https://arxiv.org/abs/2505.16535v1)**  
  Authors: Asrar Alruwayqi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.16535v1.pdf)  
  Keywords: 3d reconstruction, efficient, sparse-view, motion, deformation, ar, gaussian splatting, head, 4d, compact, dynamic  
- **[Motion Matters: Compact Gaussian Streaming for Free-Viewpoint Video Reconstruction](https://arxiv.org/abs/2505.16533v1)**  
  Authors: Jiacong Chen, Qingyu Mao, Youneng Bao, Xiandong Meng, Fanyang Meng, Ronggang Wang, Yongsheng Liang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.16533v1.pdf)  
  Keywords: efficient, 3d gaussian, motion, ar, dynamic, gaussian splatting, head, face, compact, high-fidelity  
- **[EVA: Expressive Virtual Avatars from Multi-view Videos](https://arxiv.org/abs/2505.15385v1)**  
  Authors: Hendrik Junkawitsch, Guoxing Sun, Heming Zhu, Christian Theobalt, Marc Habermann  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.15385v1.pdf)  
  Keywords: 3d gaussian, motion, deformation, body, ar, neural rendering, avatar, geometry, human, tracking, face, high-fidelity  
- **[R3GS: Gaussian Splatting for Robust Reconstruction and Relocalization in Unconstrained Image Collections](https://arxiv.org/abs/2505.15294v1)**  
  Authors: Xu yan, Zhaohui Wang, Rong Wei, Jingbo Yu, Dong Li, Xiangde Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.15294v1.pdf)  
  Keywords: outdoor, ar, localization, gaussian splatting, lightweight, lighting, human, face  
- **[GT^2-GS: Geometry-aware Texture Transfer for Gaussian Splatting](https://arxiv.org/abs/2505.15208v1)**  
  Authors: Wenjie Liu, Zhongliang Liu, Junwei Shu, Changbo Wang, Yang Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.15208v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://vpx-ecnu.github.io/GT2-GS-website.)  
  Keywords: geometry, ar, human, gaussian splatting  
- **[Hybrid 3D-4D Gaussian Splatting for Fast Dynamic Scene Representation](https://arxiv.org/abs/2505.13215v1)**  
  Authors: Seungjun Oh, Younggeun Lee, Hyejin Jeon, Eunbyung Park  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.13215v1.pdf)  
  Keywords: 3d gaussian, motion, ar, gaussian splatting, head, 4d, fast, high-fidelity, dynamic  
- **[TACOcc:Target-Adaptive Cross-Modal Fusion with Volume Rendering for 3D Semantic Occupancy](https://arxiv.org/abs/2505.12693v1)**  
  Authors: Luyao Lei, Shuo Xu, Yifan Bai, Xing Wei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.12693v1.pdf)  
  Keywords: 3d gaussian, ar, gaussian splatting, geometry, semantic, face  
- **[EA-3DGS: Efficient and Adaptive 3D Gaussians with Highly Enhanced Quality for outdoor scenes](https://arxiv.org/abs/2505.10787v1)**  
  Authors: Jianlin Guo, Haihong Xiao, Wenxiong Kang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.10787v1.pdf)  
  Keywords: real-time rendering, efficient, nerf, outdoor, 3d gaussian, ar, gaussian splatting, geometry, face  
- **[VRSplat: Fast and Robust Gaussian Splatting for Virtual Reality](https://arxiv.org/abs/2505.10144v1)**  
  Authors: Xuechang Tu, Lukas Radl, Michael Steiner, Markus Steinberger, Bernhard Kerbl, Fernando de la Torre  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.10144v1.pdf)  
  Keywords: efficient, 3d gaussian, ar, gaussian splatting, head, face, fast, vr  
- **[ToonifyGB: StyleGAN-based Gaussian Blendshapes for 3D Stylized Head Avatars](https://arxiv.org/abs/2505.10072v1)**  
  Authors: Rui-Yang Ju, Sheng-Yen Huang, Yi-Ping Hung  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.10072v1.pdf)  
  Keywords: efficient, 3d gaussian, ar, avatar, head, animation, face  

### Dynamic Scene

*Showing the latest 50 out of 678 papers*

- **[SHaDe: Compact and Consistent Dynamic 3D Reconstruction via Tri-Plane Deformation and Latent Diffusion](https://arxiv.org/abs/2505.16535v1)**  
  Authors: Asrar Alruwayqi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.16535v1.pdf)  
  Keywords: 3d reconstruction, efficient, sparse-view, motion, deformation, ar, gaussian splatting, head, 4d, compact, dynamic  
- **[Motion Matters: Compact Gaussian Streaming for Free-Viewpoint Video Reconstruction](https://arxiv.org/abs/2505.16533v1)**  
  Authors: Jiacong Chen, Qingyu Mao, Youneng Bao, Xiandong Meng, Fanyang Meng, Ronggang Wang, Yongsheng Liang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.16533v1.pdf)  
  Keywords: efficient, 3d gaussian, motion, ar, dynamic, gaussian splatting, head, face, compact, high-fidelity  
- **[MAGIC: Motion-Aware Generative Inference via Confidence-Guided LLM](https://arxiv.org/abs/2505.16456v1)**  
  Authors: Siwei Meng, Yawei Luo, Ping Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.16456v1.pdf)  
  Keywords: motion, ar, dynamic, 3d gaussian  
- **[EVA: Expressive Virtual Avatars from Multi-view Videos](https://arxiv.org/abs/2505.15385v1)**  
  Authors: Hendrik Junkawitsch, Guoxing Sun, Heming Zhu, Christian Theobalt, Marc Habermann  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.15385v1.pdf)  
  Keywords: 3d gaussian, motion, deformation, body, ar, neural rendering, avatar, geometry, human, tracking, face, high-fidelity  
- **[GS2E: Gaussian Splatting is an Effective Data Generator for Event Stream Generation](https://arxiv.org/abs/2505.15287v1)**  
  Authors: Yuchen Li, Chaoran Feng, Zhenyu Tang, Kaiyuan Deng, Wangbo Yu, Yonghong Tian, Li Yuan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.15287v1.pdf)  
  Keywords: 3d reconstruction, 3d gaussian, motion, ar, gaussian splatting, lighting, high-fidelity  
- **[Scan, Materialize, Simulate: A Generalizable Framework for Physically Grounded Robot Planning](https://arxiv.org/abs/2505.14938v1)**  
  Authors: Amine Elhafsi, Daniel Morton, Marco Pavone  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.14938v1.pdf)  
  Keywords: 3d gaussian, ar, segmentation, gaussian splatting, semantic, understanding, dynamic  
- **[MGStream: Motion-aware 3D Gaussian for Streamable Dynamic Scene Reconstruction](https://arxiv.org/abs/2505.13839v1)**  
  Authors: Zhenyu Bao, Qing Li, Guibiao Liao, Zhongyuan Zhao, Kanglin Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.13839v1.pdf) | [![GitHub](https://img.shields.io/github/stars/pcl3dv/MGStream?style=social)](https://github.com/pcl3dv/MGStream)  
  Keywords: 3d gaussian, motion, deformation, ar, gaussian splatting, dynamic  
- **[Hybrid 3D-4D Gaussian Splatting for Fast Dynamic Scene Representation](https://arxiv.org/abs/2505.13215v1)**  
  Authors: Seungjun Oh, Younggeun Lee, Hyejin Jeon, Eunbyung Park  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.13215v1.pdf)  
  Keywords: 3d gaussian, motion, ar, gaussian splatting, head, 4d, fast, high-fidelity, dynamic  
- **[MonoMobility: Zero-Shot 3D Mobility Analysis from Monocular Videos](https://arxiv.org/abs/2505.11868v1)**  
  Authors: Hongyi Zhou, Xiaogang Wang, Yulan Guo, Kai Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.11868v1.pdf)  
  Keywords: motion, ar, gaussian splatting, geometry, dynamic  
- **[GrowSplat: Constructing Temporal Digital Twins of Plants with Gaussian Splats](https://arxiv.org/abs/2505.10923v1)**  
  Authors: Simeon Adebola, Shuangyu Xie, Chung Min Kim, Justin Kerr, Bart M. van Marrewijk, Mieke van Vlaardingen, Tim van Daalen, Robert van Loo, Jose Luis Susa Rincon, Eugen Solowjow, Rick van de Zedde, Ken Goldberg  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.10923v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://berkeleyautomation.github.io/GrowSplat/)  
  Keywords: 3d gaussian, ar, deformation, gaussian splatting, 4d, fast  

### Few-shot

*Showing the latest 50 out of 128 papers*

- **[SHaDe: Compact and Consistent Dynamic 3D Reconstruction via Tri-Plane Deformation and Latent Diffusion](https://arxiv.org/abs/2505.16535v1)**  
  Authors: Asrar Alruwayqi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.16535v1.pdf)  
  Keywords: 3d reconstruction, efficient, sparse-view, motion, deformation, ar, gaussian splatting, head, 4d, compact, dynamic  
- **[RUSplatting: Robust 3D Gaussian Splatting for Sparse-View Underwater Scene Reconstruction](https://arxiv.org/abs/2505.15737v1)**  
  Authors: Zhuodong Jiang, Haoran Wang, Guoxi Huang, Brett Seymour, Nantheera Anantrasirichai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.15737v1.pdf)  
  Keywords: robotics, sparse-view, 3d gaussian, ar, gaussian splatting, high-fidelity  
- **[X-GRM: Large Gaussian Reconstruction Model for Sparse-view X-rays to Computed Tomography](https://arxiv.org/abs/2505.15235v1)**  
  Authors: Yifan Liu, Wuyang Li, Weihao Yu, Chenxin Li, Alexandre Alahi, Max Meng, Yixuan Yuan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.15235v1.pdf) | [![GitHub](https://img.shields.io/github/stars/CUHK-AIM-Group/X-GRM?style=social)](https://github.com/CUHK-AIM-Group/X-GRM)  
  Keywords: ar, sparse-view, efficient, gaussian splatting  
- **[SpatialCrafter: Unleashing the Imagination of Video Diffusion Models for Scene Reconstruction from Limited Observations](https://arxiv.org/abs/2505.11992v1)**  
  Authors: Songchun Zhang, Huiyao Xu, Sitong Guo, Zhongwei Xie, Pengwei Liu, Hujun Bao, Weiwei Xu, Changqing Zou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.11992v1.pdf)  
  Keywords: efficient, 3d gaussian, ar, sparse view, semantic  
- **[Sparfels: Fast Reconstruction from Sparse Unposed Imagery](https://arxiv.org/abs/2505.02178v1)**  
  Authors: Shubhendu Jena, Amine Ouasfi, Mae Younes, Adnane Boukhayma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.02178v1.pdf)  
  Keywords: efficient, shape reconstruction, ar, sparse view, gaussian splatting, head, geometry, face, fast  
- **[SparSplat: Fast Multi-View Reconstruction with Generalizable 2D Gaussian Splatting](https://arxiv.org/abs/2505.02175v1)**  
  Authors: Shubhendu Jena, Shishir Reddy Vutukur, Adnane Boukhayma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.02175v1.pdf)  
  Keywords: 3d reconstruction, sparse-view, 3d gaussian, shape reconstruction, ar, sparse view, gaussian splatting, geometry, face, fast  
- **[A Survey on 3D Reconstruction Techniques in Plant Phenotyping: From Classical Methods to Neural Radiance Fields (NeRF), 3D Gaussian Splatting (3DGS), and Beyond](https://arxiv.org/abs/2505.00737v1)**  
  Authors: Jiajia Li, Xinda Qi, Seyed Hamidreza Nabaei, Meiqi Liu, Dong Chen, Xin Zhang, Xunyuan Yin, Zhaojian Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.00737v1.pdf) | [![GitHub](https://img.shields.io/github/stars/JiajiaLi04/3D-Reconstruction-Plants?style=social)](https://github.com/JiajiaLi04/3D-Reconstruction-Plants)  
  Keywords: 3d reconstruction, nerf, survey, outdoor, 3d gaussian, ar, sparse view, gaussian splatting, geometry, face, understanding  
- **[Sparse2DGS: Geometry-Prioritized Gaussian Splatting for Surface Reconstruction from Sparse Views](https://arxiv.org/abs/2504.20378v1)**  
  Authors: Jiang Wu, Rui Li, Yu Zhu, Rong Guo, Jinqiu Sun, Yanning Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.20378v1.pdf)  
  Keywords: nerf, sparse-view, motion, sparse view, ar, gaussian splatting, geometry, face, fast  
- **[PIN-WM: Learning Physics-INformed World Models for Non-Prehensile Manipulation](https://arxiv.org/abs/2504.16693v2)**  
  Authors: Wenxuan Li, Hang Zhao, Zhiyuan Yu, Yu Du, Qin Zou, Ruizhen Hu, Kai Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.16693v2.pdf)  
  Keywords: efficient, few-shot, ar, body, gaussian splatting, dynamic  
- **[IXGS-Intraoperative 3D Reconstruction from Sparse, Arbitrarily Posed Real X-rays](https://arxiv.org/abs/2504.14699v1)**  
  Authors: Sascha Jecklin, Aidana Massalimova, Ruyi Zha, Lilian Calvet, Christoph J. Laux, Mazda Farshad, Philipp Fürnstahl  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.14699v1.pdf)  
  Keywords: 3d reconstruction, ar, sparse-view, gaussian splatting  

### Geometry Reconstruction

*Showing the latest 50 out of 581 papers*

- **[SHaDe: Compact and Consistent Dynamic 3D Reconstruction via Tri-Plane Deformation and Latent Diffusion](https://arxiv.org/abs/2505.16535v1)**  
  Authors: Asrar Alruwayqi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.16535v1.pdf)  
  Keywords: 3d reconstruction, efficient, sparse-view, motion, deformation, ar, gaussian splatting, head, 4d, compact, dynamic  
- **[PlantDreamer: Achieving Realistic 3D Plant Models with Diffusion-Guided Gaussian Splatting](https://arxiv.org/abs/2505.15528v1)**  
  Authors: Zane K J Hartley, Lewis A G Stuart, Andrew P French, Michael P Pound  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.15528v1.pdf)  
  Keywords: 3d gaussian, ar, gaussian splatting, geometry, high-fidelity  
- **[EVA: Expressive Virtual Avatars from Multi-view Videos](https://arxiv.org/abs/2505.15385v1)**  
  Authors: Hendrik Junkawitsch, Guoxing Sun, Heming Zhu, Christian Theobalt, Marc Habermann  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.15385v1.pdf)  
  Keywords: 3d gaussian, motion, deformation, body, ar, neural rendering, avatar, geometry, human, tracking, face, high-fidelity  
- **[GS2E: Gaussian Splatting is an Effective Data Generator for Event Stream Generation](https://arxiv.org/abs/2505.15287v1)**  
  Authors: Yuchen Li, Chaoran Feng, Zhenyu Tang, Kaiyuan Deng, Wangbo Yu, Yonghong Tian, Li Yuan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.15287v1.pdf)  
  Keywords: 3d reconstruction, 3d gaussian, motion, ar, gaussian splatting, lighting, high-fidelity  
- **[GT^2-GS: Geometry-aware Texture Transfer for Gaussian Splatting](https://arxiv.org/abs/2505.15208v1)**  
  Authors: Wenjie Liu, Zhongliang Liu, Junwei Shu, Changbo Wang, Yang Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.15208v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://vpx-ecnu.github.io/GT2-GS-website.)  
  Keywords: geometry, ar, human, gaussian splatting  
- **[MonoSplat: Generalizable 3D Gaussian Splatting from Monocular Depth Foundation Models](https://arxiv.org/abs/2505.15185v1)**  
  Authors: Yifan Liu, Keyu Fan, Weihao Yu, Chenxin Li, Hao Lu, Yixuan Yuan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.15185v1.pdf) | [![GitHub](https://img.shields.io/github/stars/CUHK-AIM-Group/MonoSplat?style=social)](https://github.com/CUHK-AIM-Group/MonoSplat)  
  Keywords: 3d gaussian, ar, gaussian splatting, geometry, lightweight, high-fidelity  
- **[Recollection from Pensieve: Novel View Synthesis via Learning from Uncalibrated Videos](https://arxiv.org/abs/2505.13440v1)**  
  Authors: Ruoyu Wang, Yi Ma, Shenghua Gao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.13440v1.pdf) | [![GitHub](https://img.shields.io/github/stars/Dwawayu/Pensieve?style=social)](https://github.com/Dwawayu/Pensieve)  
  Keywords: geometry, ar, gaussian splatting, 3d gaussian  
- **[TACOcc:Target-Adaptive Cross-Modal Fusion with Volume Rendering for 3D Semantic Occupancy](https://arxiv.org/abs/2505.12693v1)**  
  Authors: Luyao Lei, Shuo Xu, Yifan Bai, Xing Wei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.12693v1.pdf)  
  Keywords: 3d gaussian, ar, gaussian splatting, geometry, semantic, face  
- **[GTR: Gaussian Splatting Tracking and Reconstruction of Unknown Objects Based on Appearance and Geometric Complexity](https://arxiv.org/abs/2505.11905v1)**  
  Authors: Takuya Ikeda, Sergey Zakharov, Muhammad Zubair Irshad, Istvan Balazs Opra, Shun Iwase, Dian Chen, Mark Tjersland, Robert Lee, Alexandre Dilly, Rares Ambrus, Koichi Nishiwaki  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.11905v1.pdf)  
  Keywords: 3d reconstruction, 3d gaussian, ar, gaussian splatting, geometry, tracking, high-fidelity  
- **[MonoMobility: Zero-Shot 3D Mobility Analysis from Monocular Videos](https://arxiv.org/abs/2505.11868v1)**  
  Authors: Hongyi Zhou, Xiaogang Wang, Yulan Guo, Kai Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.11868v1.pdf)  
  Keywords: motion, ar, gaussian splatting, geometry, dynamic  

### Large Scene

*Showing the latest 50 out of 101 papers*

- **[R3GS: Gaussian Splatting for Robust Reconstruction and Relocalization in Unconstrained Image Collections](https://arxiv.org/abs/2505.15294v1)**  
  Authors: Xu yan, Zhaohui Wang, Rong Wei, Jingbo Yu, Dong Li, Xiangde Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.15294v1.pdf)  
  Keywords: outdoor, ar, localization, gaussian splatting, lightweight, lighting, human, face  
- **[Gaussian Splatting as a Unified Representation for Autonomy in Unstructured Environments](https://arxiv.org/abs/2505.11794v1)**  
  Authors: Dexter Ong, Yuezhan Tao, Varun Murali, Igor Spasojevic, Vijay Kumar, Pratik Chaudhari  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.11794v1.pdf)  
  Keywords: ar, semantic, outdoor, gaussian splatting  
- **[EA-3DGS: Efficient and Adaptive 3D Gaussians with Highly Enhanced Quality for outdoor scenes](https://arxiv.org/abs/2505.10787v1)**  
  Authors: Jianlin Guo, Haihong Xiao, Wenxiong Kang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.10787v1.pdf)  
  Keywords: real-time rendering, efficient, nerf, outdoor, 3d gaussian, ar, gaussian splatting, geometry, face  
- **[Consistent Quantity-Quality Control across Scenes for Deployment-Aware Gaussian Splatting](https://arxiv.org/abs/2505.10473v2)**  
  Authors: Fengdi Zhang, Hongkun Cao, Ruqi Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.10473v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://zhang-fengdi.github.io/ControlGS/)  
  Keywords: outdoor, 3d gaussian, ar, gaussian splatting, semantic, compact  
- **[Large-Scale Gaussian Splatting SLAM](https://arxiv.org/abs/2505.09915v1)**  
  Authors: Zhe Xin, Chenyang Wu, Penghui Huang, Yanyong Zhang, Yinian Mao, Guoquan Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.09915v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://lsg-slam.github.io.)  
  Keywords: nerf, outdoor, 3d gaussian, ar, gaussian splatting, recognition, tracking, slam  
- **[NavDP: Learning Sim-to-Real Navigation Diffusion Policy with Privileged Information Guidance](https://arxiv.org/abs/2505.08712v2)**  
  Authors: Wenzhe Cai, Jiaqi Peng, Yuqiang Yang, Yujian Zhang, Meng Wei, Hanqing Wang, Yilun Chen, Tai Wang, Jiangmiao Pang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.08712v2.pdf)  
  Keywords: efficient, outdoor, ar, localization, gaussian splatting, human, mapping, dynamic  
- **[SLAG: Scalable Language-Augmented Gaussian Splatting](https://arxiv.org/abs/2505.08124v1)**  
  Authors: Laszlo Szilagyi, Francis Engelmann, Jeannette Bohg  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.08124v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://slag-project.github.io/.)  
  Keywords: large scene, efficient, 3d gaussian, ar, gaussian splatting, robotics  
- **[TUM2TWIN: Introducing the Large-Scale Multimodal Urban Digital Twin Benchmark Dataset](https://arxiv.org/abs/2505.07396v2)**  
  Authors: Olaf Wysocki, Benedikt Schwab, Manoj Kumar Biswanath, Michael Greza, Qilin Zhang, Jingwei Zhu, Thomas Froech, Medhini Heeramaglore, Ihab Hijazi, Khaoula Kanna, Mathias Pechinger, Zhaiyu Chen, Yao Sun, Alejandro Rueda Segura, Ziyang Xu, Omar AbdelGafar, Mansour Mehranfar, Chandan Yeshwanth, Yueh-Cheng Liu, Hadi Yazdi, Jiapan Wang, Stefan Auer, Katharina Anders, Klaus Bogenberger, Andre Borrmann, Angela Dai, Ludwig Hoegner, Christoph Holst, Thomas H. Kolbe, Ferdinand Ludwig, Matthias Nießner, Frank Petzold, Xiao Xiang Zhu, Boris Jutzi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.07396v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://tum2t.win)  
  Keywords: nerf, outdoor, ar, segmentation, gaussian splatting, semantic, high-fidelity  
- **[A Survey on 3D Reconstruction Techniques in Plant Phenotyping: From Classical Methods to Neural Radiance Fields (NeRF), 3D Gaussian Splatting (3DGS), and Beyond](https://arxiv.org/abs/2505.00737v1)**  
  Authors: Jiajia Li, Xinda Qi, Seyed Hamidreza Nabaei, Meiqi Liu, Dong Chen, Xin Zhang, Xunyuan Yin, Zhaojian Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.00737v1.pdf) | [![GitHub](https://img.shields.io/github/stars/JiajiaLi04/3D-Reconstruction-Plants?style=social)](https://github.com/JiajiaLi04/3D-Reconstruction-Plants)  
  Keywords: 3d reconstruction, nerf, survey, outdoor, 3d gaussian, ar, sparse view, gaussian splatting, geometry, face, understanding  
- **[HUG: Hierarchical Urban Gaussian Splatting with Block-Based Reconstruction](https://arxiv.org/abs/2504.16606v1)**  
  Authors: Zhongtao Wang, Mai Su, Huishan Au, Yilong Li, Xizhe Cao, Chengwei Pan, Yisong Chen, Guoping Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.16606v1.pdf)  
  Keywords: efficient, 3d gaussian, urban scene, ar, gaussian splatting  

### Model Compression

*Showing the latest 50 out of 682 papers*

- **[SHaDe: Compact and Consistent Dynamic 3D Reconstruction via Tri-Plane Deformation and Latent Diffusion](https://arxiv.org/abs/2505.16535v1)**  
  Authors: Asrar Alruwayqi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.16535v1.pdf)  
  Keywords: 3d reconstruction, efficient, sparse-view, motion, deformation, ar, gaussian splatting, head, 4d, compact, dynamic  
- **[Motion Matters: Compact Gaussian Streaming for Free-Viewpoint Video Reconstruction](https://arxiv.org/abs/2505.16533v1)**  
  Authors: Jiacong Chen, Qingyu Mao, Youneng Bao, Xiandong Meng, Fanyang Meng, Ronggang Wang, Yongsheng Liang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.16533v1.pdf)  
  Keywords: efficient, 3d gaussian, motion, ar, dynamic, gaussian splatting, head, face, compact, high-fidelity  
- **[R3GS: Gaussian Splatting for Robust Reconstruction and Relocalization in Unconstrained Image Collections](https://arxiv.org/abs/2505.15294v1)**  
  Authors: Xu yan, Zhaohui Wang, Rong Wei, Jingbo Yu, Dong Li, Xiangde Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.15294v1.pdf)  
  Keywords: outdoor, ar, localization, gaussian splatting, lightweight, lighting, human, face  
- **[X-GRM: Large Gaussian Reconstruction Model for Sparse-view X-rays to Computed Tomography](https://arxiv.org/abs/2505.15235v1)**  
  Authors: Yifan Liu, Wuyang Li, Weihao Yu, Chenxin Li, Alexandre Alahi, Max Meng, Yixuan Yuan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.15235v1.pdf) | [![GitHub](https://img.shields.io/github/stars/CUHK-AIM-Group/X-GRM?style=social)](https://github.com/CUHK-AIM-Group/X-GRM)  
  Keywords: ar, sparse-view, efficient, gaussian splatting  
- **[MonoSplat: Generalizable 3D Gaussian Splatting from Monocular Depth Foundation Models](https://arxiv.org/abs/2505.15185v1)**  
  Authors: Yifan Liu, Keyu Fan, Weihao Yu, Chenxin Li, Hao Lu, Yixuan Yuan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.15185v1.pdf) | [![GitHub](https://img.shields.io/github/stars/CUHK-AIM-Group/MonoSplat?style=social)](https://github.com/CUHK-AIM-Group/MonoSplat)  
  Keywords: 3d gaussian, ar, gaussian splatting, geometry, lightweight, high-fidelity  
- **[Is Semantic SLAM Ready for Embedded Systems ? A Comparative Survey](https://arxiv.org/abs/2505.12384v1)**  
  Authors: Calvin Galagain, Martyna Poreba, François Goulette  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.12384v1.pdf)  
  Keywords: efficient, nerf, survey, 3d gaussian, ar, segmentation, localization, gaussian splatting, semantic, slam, mapping  
- **[SpatialCrafter: Unleashing the Imagination of Video Diffusion Models for Scene Reconstruction from Limited Observations](https://arxiv.org/abs/2505.11992v1)**  
  Authors: Songchun Zhang, Huiyao Xu, Sitong Guo, Zhongwei Xie, Pengwei Liu, Hujun Bao, Weiwei Xu, Changqing Zou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.11992v1.pdf)  
  Keywords: efficient, 3d gaussian, ar, sparse view, semantic  
- **[iSegMan: Interactive Segment-and-Manipulate 3D Gaussians](https://arxiv.org/abs/2505.11934v1)**  
  Authors: Yian Zhao, Wanshi Xu, Ruochong Zheng, Pengchong Qiao, Chang Liu, Jie Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.11934v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://zhao-yian.github.io/iSegMan.)  
  Keywords: efficient, 3d gaussian, ar, segmentation, efficient rendering  
- **[EA-3DGS: Efficient and Adaptive 3D Gaussians with Highly Enhanced Quality for outdoor scenes](https://arxiv.org/abs/2505.10787v1)**  
  Authors: Jianlin Guo, Haihong Xiao, Wenxiong Kang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.10787v1.pdf)  
  Keywords: real-time rendering, efficient, nerf, outdoor, 3d gaussian, ar, gaussian splatting, geometry, face  
- **[GaussianFormer3D: Multi-Modal Gaussian-based Semantic Occupancy Prediction with 3D Deformable Attention](https://arxiv.org/abs/2505.10685v1)**  
  Authors: Lingjun Zhao, Sizhe Wei, James Hays, Lu Gan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.10685v1.pdf)  
  Keywords: 3d gaussian, autonomous driving, ar, geometry, semantic, compact  

### Quality Enhancement

*Showing the latest 50 out of 287 papers*

- **[Motion Matters: Compact Gaussian Streaming for Free-Viewpoint Video Reconstruction](https://arxiv.org/abs/2505.16533v1)**  
  Authors: Jiacong Chen, Qingyu Mao, Youneng Bao, Xiandong Meng, Fanyang Meng, Ronggang Wang, Yongsheng Liang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.16533v1.pdf)  
  Keywords: efficient, 3d gaussian, motion, ar, dynamic, gaussian splatting, head, face, compact, high-fidelity  
- **[RUSplatting: Robust 3D Gaussian Splatting for Sparse-View Underwater Scene Reconstruction](https://arxiv.org/abs/2505.15737v1)**  
  Authors: Zhuodong Jiang, Haoran Wang, Guoxi Huang, Brett Seymour, Nantheera Anantrasirichai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.15737v1.pdf)  
  Keywords: robotics, sparse-view, 3d gaussian, ar, gaussian splatting, high-fidelity  
- **[PlantDreamer: Achieving Realistic 3D Plant Models with Diffusion-Guided Gaussian Splatting](https://arxiv.org/abs/2505.15528v1)**  
  Authors: Zane K J Hartley, Lewis A G Stuart, Andrew P French, Michael P Pound  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.15528v1.pdf)  
  Keywords: 3d gaussian, ar, gaussian splatting, geometry, high-fidelity  
- **[EVA: Expressive Virtual Avatars from Multi-view Videos](https://arxiv.org/abs/2505.15385v1)**  
  Authors: Hendrik Junkawitsch, Guoxing Sun, Heming Zhu, Christian Theobalt, Marc Habermann  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.15385v1.pdf)  
  Keywords: 3d gaussian, motion, deformation, body, ar, neural rendering, avatar, geometry, human, tracking, face, high-fidelity  
- **[GS2E: Gaussian Splatting is an Effective Data Generator for Event Stream Generation](https://arxiv.org/abs/2505.15287v1)**  
  Authors: Yuchen Li, Chaoran Feng, Zhenyu Tang, Kaiyuan Deng, Wangbo Yu, Yonghong Tian, Li Yuan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.15287v1.pdf)  
  Keywords: 3d reconstruction, 3d gaussian, motion, ar, gaussian splatting, lighting, high-fidelity  
- **[MonoSplat: Generalizable 3D Gaussian Splatting from Monocular Depth Foundation Models](https://arxiv.org/abs/2505.15185v1)**  
  Authors: Yifan Liu, Keyu Fan, Weihao Yu, Chenxin Li, Hao Lu, Yixuan Yuan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.15185v1.pdf) | [![GitHub](https://img.shields.io/github/stars/CUHK-AIM-Group/MonoSplat?style=social)](https://github.com/CUHK-AIM-Group/MonoSplat)  
  Keywords: 3d gaussian, ar, gaussian splatting, geometry, lightweight, high-fidelity  
- **[Hybrid 3D-4D Gaussian Splatting for Fast Dynamic Scene Representation](https://arxiv.org/abs/2505.13215v1)**  
  Authors: Seungjun Oh, Younggeun Lee, Hyejin Jeon, Eunbyung Park  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.13215v1.pdf)  
  Keywords: 3d gaussian, motion, ar, gaussian splatting, head, 4d, fast, high-fidelity, dynamic  
- **[GTR: Gaussian Splatting Tracking and Reconstruction of Unknown Objects Based on Appearance and Geometric Complexity](https://arxiv.org/abs/2505.11905v1)**  
  Authors: Takuya Ikeda, Sergey Zakharov, Muhammad Zubair Irshad, Istvan Balazs Opra, Shun Iwase, Dian Chen, Mark Tjersland, Robert Lee, Alexandre Dilly, Rares Ambrus, Koichi Nishiwaki  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.11905v1.pdf)  
  Keywords: 3d reconstruction, 3d gaussian, ar, gaussian splatting, geometry, tracking, high-fidelity  
- **[TUM2TWIN: Introducing the Large-Scale Multimodal Urban Digital Twin Benchmark Dataset](https://arxiv.org/abs/2505.07396v2)**  
  Authors: Olaf Wysocki, Benedikt Schwab, Manoj Kumar Biswanath, Michael Greza, Qilin Zhang, Jingwei Zhu, Thomas Froech, Medhini Heeramaglore, Ihab Hijazi, Khaoula Kanna, Mathias Pechinger, Zhaiyu Chen, Yao Sun, Alejandro Rueda Segura, Ziyang Xu, Omar AbdelGafar, Mansour Mehranfar, Chandan Yeshwanth, Yueh-Cheng Liu, Hadi Yazdi, Jiapan Wang, Stefan Auer, Katharina Anders, Klaus Bogenberger, Andre Borrmann, Angela Dai, Ludwig Hoegner, Christoph Holst, Thomas H. Kolbe, Ferdinand Ludwig, Matthias Nießner, Frank Petzold, Xiao Xiang Zhu, Boris Jutzi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.07396v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://tum2t.win)  
  Keywords: nerf, outdoor, ar, segmentation, gaussian splatting, semantic, high-fidelity  
- **[SVAD: From Single Image to 3D Avatar via Synthetic Data Generation with Video Diffusion and Data Augmentation](https://arxiv.org/abs/2505.05475v1)**  
  Authors: Yonwoo Choi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.05475v1.pdf)  
  Keywords: real-time rendering, 3d gaussian, ar, gaussian splatting, avatar, animation, human, face, high-fidelity  

### Ray Tracing

- **[DNF-Avatar: Distilling Neural Fields for Real-time Animatable Avatar Relighting](https://arxiv.org/abs/2504.10486v1)**  
  Authors: Zeren Jiang, Shaofei Wang, Siyu Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.10486v1.pdf)  
  Keywords: shadow, relightable, relighting, ar, gaussian splatting, avatar, geometry, lighting, human, fast, ray tracing  
- **[Stochastic Ray Tracing of 3D Transparent Gaussians](https://arxiv.org/abs/2504.06598v2)**  
  Authors: Xin Sun, Iliyan Georgiev, Yun Fei, Miloš Hašan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.06598v2.pdf)  
  Keywords: relighting, efficient, 3d gaussian, ar, gaussian splatting, acceleration, lighting, ray tracing, efficient rendering  
- **[3D Gaussian Particle Approximation of VDB Datasets: A Study for Scientific Visualization](https://arxiv.org/abs/2504.04857v2)**  
  Authors: Isha Sharma, Dieter Schmalstieg  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.04857v2.pdf)  
  Keywords: efficient, ray marching, 3d gaussian, ar, gaussian splatting, acceleration, animation, compact, dynamic  
- **[3D Gaussian Inverse Rendering with Approximated Global Illumination](https://arxiv.org/abs/2504.01358v1)**  
  Authors: Zirui Wu, Jianteng Chen, Laijian Li, Shaoteng Wu, Zhikai Zhu, Kang Xu, Martin R. Oswald, Jie Song  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.01358v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://wuzirui.github.io/gs-ssr.)  
  Keywords: real-time rendering, efficient, global illumination, 3d gaussian, ar, gaussian splatting, lighting, face, ray tracing, illumination  
- **[Real-time Global Illumination for Dynamic 3D Gaussian Scenes](https://arxiv.org/abs/2503.17897v1)**  
  Authors: Chenxiao Hu, Meng Gai, Guoping Wang, Sheng Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.17897v1.pdf)  
  Keywords: real-time rendering, global illumination, 3d gaussian, light transport, lighting, face, fast, dynamic, illumination  
- **[REdiSplats: Ray Tracing for Editable Gaussian Splatting](https://arxiv.org/abs/2503.12284v1)**  
  Authors: Krzysztof Byrski, Grzegorz Wilczyński, Weronika Smolak-Dyżewska, Piotr Borycki, Dawid Baran, Sławomir Tadeja, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.12284v1.pdf)  
  Keywords: shadow, 3d gaussian, ar, neural rendering, gaussian splatting, reflection, fast, ray tracing  
- **[BEAM: Bridging Physically-based Rendering and Gaussian Modeling for Relightable Volumetric Video](https://arxiv.org/abs/2502.08297v1)**  
  Authors: Yu Hong, Yize Wu, Zhehao Shen, Chengcheng Guo, Yuheng Jiang, Yingliang Zhang, Jingyi Yu, Lan Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.08297v1.pdf)  
  Keywords: real-time rendering, relightable, efficient, ar, geometry, lighting, tracking, 4d, face, dynamic, ray tracing  
- **[MeshSplats: Mesh-Based Rendering with Gaussian Splatting Initialization](https://arxiv.org/abs/2502.07754v1)**  
  Authors: Rafał Tobiasz, Grzegorz Wilczyński, Marcin Mazur, Sławomir Tadeja, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.07754v1.pdf)  
  Keywords: shadow, gaussian splatting, reflection, lighting, face, ray tracing  
- **[Scalable 3D Gaussian Splatting-Based RF Signal Spatial Propagation Modeling](https://arxiv.org/abs/2502.01826v1)**  
  Authors: Kang Yang, Gaofeng Dong, Sijie Ji, Wan Du, Mani Srivastava  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.01826v1.pdf)  
  Keywords: survey, 3d gaussian, ar, gaussian splatting, ray tracing  
- **[Radiant Foam: Real-Time Differentiable Ray Tracing](https://arxiv.org/abs/2502.01157v1)**  
  Authors: Shrisudhan Govindarajan, Daniel Rebain, Kwang Moo Yi, Andrea Tagliasacchi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.01157v1.pdf)  
  Keywords: efficient, light transport, ar, gaussian splatting, acceleration, reflection, ray tracing  

### Relighting

*Showing the latest 50 out of 201 papers*

- **[R3GS: Gaussian Splatting for Robust Reconstruction and Relocalization in Unconstrained Image Collections](https://arxiv.org/abs/2505.15294v1)**  
  Authors: Xu yan, Zhaohui Wang, Rong Wei, Jingbo Yu, Dong Li, Xiangde Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.15294v1.pdf)  
  Keywords: outdoor, ar, localization, gaussian splatting, lightweight, lighting, human, face  
- **[GS2E: Gaussian Splatting is an Effective Data Generator for Event Stream Generation](https://arxiv.org/abs/2505.15287v1)**  
  Authors: Yuchen Li, Chaoran Feng, Zhenyu Tang, Kaiyuan Deng, Wangbo Yu, Yonghong Tian, Li Yuan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.15287v1.pdf)  
  Keywords: 3d reconstruction, 3d gaussian, motion, ar, gaussian splatting, lighting, high-fidelity  
- **[3D Gaussian Adaptive Reconstruction for Fourier Light-Field Microscopy](https://arxiv.org/abs/2505.12875v1)**  
  Authors: Chenyu Xu, Zhouyu Jin, Chengkang Shen, Hao Zhu, Zhan Ma, Bo Xiong, You Zhou, Xun Cao, Ning Gu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.12875v1.pdf)  
  Keywords: nerf, 3d gaussian, ar, gaussian splatting, lighting  
- **[Visual enhancement and 3D representation for underwater scenes: a review](https://arxiv.org/abs/2505.01869v1)**  
  Authors: Guoxi Huang, Haoran Wang, Brett Seymour, Evan Kovacs, John Ellerbrock, Dave Blackham, Nantheera Anantrasirichai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.01869v1.pdf)  
  Keywords: 3d reconstruction, survey, 3d gaussian, ar, lighting  
- **[TransparentGS: Fast Inverse Rendering of Transparent Objects with Gaussians](https://arxiv.org/abs/2504.18768v2)**  
  Authors: Letian Huang, Dongwei Ye, Jialin Dan, Chengzhi Tao, Huiwen Liu, Kun Zhou, Bo Ren, Yuanqi Li, Yanwen Guo, Jie Guo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.18768v2.pdf)  
  Keywords: efficient, 3d gaussian, ar, gaussian splatting, reflection, fast  
- **[RGS-DR: Reflective Gaussian Surfels with Deferred Rendering for Shiny Objects](https://arxiv.org/abs/2504.18468v3)**  
  Authors: Georgios Kouros, Minye Wu, Tinne Tuytelaars  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.18468v3.pdf)  
  Keywords: relighting, nerf, 3d gaussian, ar, gaussian splatting, reflection, lighting, geometry, face  
- **[iVR-GS: Inverse Volume Rendering for Explorable Visualization via Editable 3D Gaussian Splatting](https://arxiv.org/abs/2504.17954v1)**  
  Authors: Kaiyuan Tang, Siyuan Yao, Chaoli Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.17954v1.pdf) | [![GitHub](https://img.shields.io/github/stars/TouKaienn/iVR-GS?style=social)](https://github.com/TouKaienn/iVR-GS)  
  Keywords: nerf, 3d gaussian, ar, gaussian splatting, lighting, fast, mapping, vr  
- **[StyleMe3D: Stylization with Disentangled Priors by Multiple Encoders on 3D Gaussians](https://arxiv.org/abs/2504.15281v1)**  
  Authors: Cailin Zhuang, Yaoqi Hu, Xuanyang Zhang, Wei Cheng, Jiacheng Bao, Shengqi Liu, Yiying Yang, Xianfang Zeng, Gang Yu, Ming Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.15281v1.pdf)  
  Keywords: real-time rendering, nerf, 3d gaussian, ar, gaussian splatting, human, lighting, semantic, quality enhancement, dynamic  
- **[Immersive Teleoperation Framework for Locomanipulation Tasks](https://arxiv.org/abs/2504.15229v1)**  
  Authors: Takuya Boehringer, Jonathan Embley-Riches, Karim Hammoud, Valerio Modugno, Dimitrios Kanoulas  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.15229v1.pdf)  
  Keywords: ar, gaussian splatting, lighting, face, fast, vr  
- **[Metamon-GS: Enhancing Representability with Variance-Guided Densification and Light Encoding](https://arxiv.org/abs/2504.14460v1)**  
  Authors: Junyan Su, Baozhu Zhao, Xiaohan Zhang, Qi Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.14460v1.pdf)  
  Keywords: lighting, ar, gaussian splatting, 3d gaussian  

### SLAM

*Showing the latest 50 out of 267 papers*

- **[EVA: Expressive Virtual Avatars from Multi-view Videos](https://arxiv.org/abs/2505.15385v1)**  
  Authors: Hendrik Junkawitsch, Guoxing Sun, Heming Zhu, Christian Theobalt, Marc Habermann  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.15385v1.pdf)  
  Keywords: 3d gaussian, motion, deformation, body, ar, neural rendering, avatar, geometry, human, tracking, face, high-fidelity  
- **[R3GS: Gaussian Splatting for Robust Reconstruction and Relocalization in Unconstrained Image Collections](https://arxiv.org/abs/2505.15294v1)**  
  Authors: Xu yan, Zhaohui Wang, Rong Wei, Jingbo Yu, Dong Li, Xiangde Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.15294v1.pdf)  
  Keywords: outdoor, ar, localization, gaussian splatting, lightweight, lighting, human, face  
- **[Is Semantic SLAM Ready for Embedded Systems ? A Comparative Survey](https://arxiv.org/abs/2505.12384v1)**  
  Authors: Calvin Galagain, Martyna Poreba, François Goulette  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.12384v1.pdf)  
  Keywords: efficient, nerf, survey, 3d gaussian, ar, segmentation, localization, gaussian splatting, semantic, slam, mapping  
- **[GTR: Gaussian Splatting Tracking and Reconstruction of Unknown Objects Based on Appearance and Geometric Complexity](https://arxiv.org/abs/2505.11905v1)**  
  Authors: Takuya Ikeda, Sergey Zakharov, Muhammad Zubair Irshad, Istvan Balazs Opra, Shun Iwase, Dian Chen, Mark Tjersland, Robert Lee, Alexandre Dilly, Rares Ambrus, Koichi Nishiwaki  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.11905v1.pdf)  
  Keywords: 3d reconstruction, 3d gaussian, ar, gaussian splatting, geometry, tracking, high-fidelity  
- **[Large-Scale Gaussian Splatting SLAM](https://arxiv.org/abs/2505.09915v1)**  
  Authors: Zhe Xin, Chenyang Wu, Penghui Huang, Yanyong Zhang, Yinian Mao, Guoquan Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.09915v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://lsg-slam.github.io.)  
  Keywords: nerf, outdoor, 3d gaussian, ar, gaussian splatting, recognition, tracking, slam  
- **[Real2Render2Real: Scaling Robot Data Without Dynamics Simulation or Robot Hardware](https://arxiv.org/abs/2505.09601v1)**  
  Authors: Justin Yu, Letian Fu, Huang Huang, Karim El-Refai, Rares Andrei Ambrus, Richard Cheng, Muhammad Zubair Irshad, Ken Goldberg  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.09601v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://real2render2real.com)  
  Keywords: 3d gaussian, motion, ar, gaussian splatting, geometry, human, tracking, dynamic  
- **[NavDP: Learning Sim-to-Real Navigation Diffusion Policy with Privileged Information Guidance](https://arxiv.org/abs/2505.08712v2)**  
  Authors: Wenzhe Cai, Jiaqi Peng, Yuqiang Yang, Yujian Zhang, Meng Wei, Hanqing Wang, Yilun Chen, Tai Wang, Jiangmiao Pang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.08712v2.pdf)  
  Keywords: efficient, outdoor, ar, localization, gaussian splatting, human, mapping, dynamic  
- **[DLO-Splatting: Tracking Deformable Linear Objects Using 3D Gaussian Splatting](https://arxiv.org/abs/2505.08644v2)**  
  Authors: Holly Dinkel, Marcel Büsching, Alberta Longhini, Brian Coltin, Trey Smith, Danica Kragic, Mårten Björkman, Timothy Bretl  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.08644v2.pdf)  
  Keywords: 3d gaussian, ar, gaussian splatting, tracking, dynamic  
- **[Monocular Online Reconstruction with Enhanced Detail Preservation](https://arxiv.org/abs/2505.07887v2)**  
  Authors: Songyin Wu, Zhaoyang Lv, Yufeng Zhu, Duncan Frost, Zhengqin Li, Ling-Qi Yan, Carl Ren, Richard Newcombe, Zhao Dong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.07887v2.pdf)  
  Keywords: mapping, tracking, ar, 3d gaussian  
- **[Apply Hierarchical-Chain-of-Generation to Complex Attributes Text-to-3D Generation](https://arxiv.org/abs/2505.05505v1)**  
  Authors: Yiming Qin, Zhu Xu, Yang Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.05505v1.pdf) | [![GitHub](https://img.shields.io/github/stars/Wakals/GASCOL?style=social)](https://github.com/Wakals/GASCOL)  
  Keywords: ar, semantic, localization, 3d gaussian  

### Scene Understanding

*Showing the latest 50 out of 321 papers*

- **[Scan, Materialize, Simulate: A Generalizable Framework for Physically Grounded Robot Planning](https://arxiv.org/abs/2505.14938v1)**  
  Authors: Amine Elhafsi, Daniel Morton, Marco Pavone  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.14938v1.pdf)  
  Keywords: 3d gaussian, ar, segmentation, gaussian splatting, semantic, understanding, dynamic  
- **[TACOcc:Target-Adaptive Cross-Modal Fusion with Volume Rendering for 3D Semantic Occupancy](https://arxiv.org/abs/2505.12693v1)**  
  Authors: Luyao Lei, Shuo Xu, Yifan Bai, Xing Wei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.12693v1.pdf)  
  Keywords: 3d gaussian, ar, gaussian splatting, geometry, semantic, face  
- **[Is Semantic SLAM Ready for Embedded Systems ? A Comparative Survey](https://arxiv.org/abs/2505.12384v1)**  
  Authors: Calvin Galagain, Martyna Poreba, François Goulette  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.12384v1.pdf)  
  Keywords: efficient, nerf, survey, 3d gaussian, ar, segmentation, localization, gaussian splatting, semantic, slam, mapping  
- **[SpatialCrafter: Unleashing the Imagination of Video Diffusion Models for Scene Reconstruction from Limited Observations](https://arxiv.org/abs/2505.11992v1)**  
  Authors: Songchun Zhang, Huiyao Xu, Sitong Guo, Zhongwei Xie, Pengwei Liu, Hujun Bao, Weiwei Xu, Changqing Zou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.11992v1.pdf)  
  Keywords: efficient, 3d gaussian, ar, sparse view, semantic  
- **[iSegMan: Interactive Segment-and-Manipulate 3D Gaussians](https://arxiv.org/abs/2505.11934v1)**  
  Authors: Yian Zhao, Wanshi Xu, Ruochong Zheng, Pengchong Qiao, Chang Liu, Jie Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.11934v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://zhao-yian.github.io/iSegMan.)  
  Keywords: efficient, 3d gaussian, ar, segmentation, efficient rendering  
- **[Gaussian Splatting as a Unified Representation for Autonomy in Unstructured Environments](https://arxiv.org/abs/2505.11794v1)**  
  Authors: Dexter Ong, Yuezhan Tao, Varun Murali, Igor Spasojevic, Vijay Kumar, Pratik Chaudhari  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.11794v1.pdf)  
  Keywords: ar, semantic, outdoor, gaussian splatting  
- **[GaussianFormer3D: Multi-Modal Gaussian-based Semantic Occupancy Prediction with 3D Deformable Attention](https://arxiv.org/abs/2505.10685v1)**  
  Authors: Lingjun Zhao, Sizhe Wei, James Hays, Lu Gan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.10685v1.pdf)  
  Keywords: 3d gaussian, autonomous driving, ar, geometry, semantic, compact  
- **[Consistent Quantity-Quality Control across Scenes for Deployment-Aware Gaussian Splatting](https://arxiv.org/abs/2505.10473v2)**  
  Authors: Fengdi Zhang, Hongkun Cao, Ruqi Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.10473v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://zhang-fengdi.github.io/ControlGS/)  
  Keywords: outdoor, 3d gaussian, ar, gaussian splatting, semantic, compact  
- **[Advances in Radiance Field for Dynamic Scene: From Neural Field to Gaussian Field](https://arxiv.org/abs/2505.10049v2)**  
  Authors: Jinlong Fan, Xuepu Zeng, Jing Zhang, Mingming Gong, Yuxiang Yang, Dacheng Tao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.10049v2.pdf)  
  Keywords: survey, 3d gaussian, motion, ar, body, gaussian splatting, 4d, understanding, dynamic  
- **[Large-Scale Gaussian Splatting SLAM](https://arxiv.org/abs/2505.09915v1)**  
  Authors: Zhe Xin, Chenyang Wu, Penghui Huang, Yanyong Zhang, Yinian Mao, Guoquan Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.09915v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://lsg-slam.github.io.)  
  Keywords: nerf, outdoor, 3d gaussian, ar, gaussian splatting, recognition, tracking, slam  



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