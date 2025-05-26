# Awesome Gaussian Splatting [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of latest research papers, projects and resources related to Gaussian Splatting. Content is automatically updated daily.

> Last Update: 2025-05-26 00:56:44

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
  Keywords: nerf, segmentation, gaussian splatting, ar, 3d gaussian, semantic, localization, efficient, mapping, survey, slam  
- **[Advances in Radiance Field for Dynamic Scene: From Neural Field to Gaussian Field](https://arxiv.org/abs/2505.10049v2)**  
  Authors: Jinlong Fan, Xuepu Zeng, Jing Zhang, Mingming Gong, Yuxiang Yang, Dacheng Tao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.10049v2.pdf)  
  Keywords: ar, gaussian splatting, 3d gaussian, motion, dynamic, understanding, survey, body, 4d  
- **[A Survey of 3D Reconstruction with Event Cameras: From Event-based Geometry to Neural 3D Rendering](https://arxiv.org/abs/2505.08438v1)**  
  Authors: Chuanzhi Xu, Haoxian Zhou, Langyi Chen, Haodong Chen, Ying Zhou, Vera Chung, Qiang Qu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.08438v1.pdf)  
  Keywords: ar, gaussian splatting, 3d gaussian, neural rendering, dynamic, 3d reconstruction, motion, survey, geometry  
- **[UltraGauss: Ultrafast Gaussian Reconstruction of 3D Ultrasound Volumes](https://arxiv.org/abs/2505.05643v1)**  
  Authors: Mark C. Eid, Ana I. L. Namburete, João F. Henriques  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.05643v1.pdf)  
  Keywords: ar, gaussian splatting, 3d reconstruction, efficient, fast, survey  
- **[3D Scene Generation: A Survey](https://arxiv.org/abs/2505.05474v1)**  
  Authors: Beichen Wen, Haozhe Xie, Zhaoxi Chen, Fangzhou Hong, Ziwei Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.05474v1.pdf) | [![GitHub](https://img.shields.io/github/stars/hzxie/Awesome-3D-Scene-Generation?style=social)](https://github.com/hzxie/Awesome-3D-Scene-Generation)  
  Keywords: nerf, robotics, ar, 3d gaussian, semantic, survey, autonomous driving  
- **[Visual enhancement and 3D representation for underwater scenes: a review](https://arxiv.org/abs/2505.01869v1)**  
  Authors: Guoxi Huang, Haoran Wang, Brett Seymour, Evan Kovacs, John Ellerbrock, Dave Blackham, Nantheera Anantrasirichai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.01869v1.pdf)  
  Keywords: lighting, 3d gaussian, 3d reconstruction, ar, survey  
- **[A Survey on 3D Reconstruction Techniques in Plant Phenotyping: From Classical Methods to Neural Radiance Fields (NeRF), 3D Gaussian Splatting (3DGS), and Beyond](https://arxiv.org/abs/2505.00737v1)**  
  Authors: Jiajia Li, Xinda Qi, Seyed Hamidreza Nabaei, Meiqi Liu, Dong Chen, Xin Zhang, Xunyuan Yin, Zhaojian Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.00737v1.pdf) | [![GitHub](https://img.shields.io/github/stars/JiajiaLi04/3D-Reconstruction-Plants?style=social)](https://github.com/JiajiaLi04/3D-Reconstruction-Plants)  
  Keywords: nerf, ar, gaussian splatting, face, 3d gaussian, understanding, 3d reconstruction, outdoor, survey, sparse view, geometry  
- **[Digital Twin Generation from Visual Data: A Survey](https://arxiv.org/abs/2504.13159v1)**  
  Authors: Andrew Melnik, Benjamin Alt, Giang Nguyen, Artur Wilkowski, Maciej Stefańczyk, Qirui Wu, Sinan Harms, Helge Rhodin, Manolis Savva, Michael Beetz  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.13159v1.pdf) | [![GitHub](https://img.shields.io/github/stars/ndrwmlnk/awesome-digital-twins?style=social)](https://github.com/ndrwmlnk/awesome-digital-twins)  
  Keywords: lighting, robotics, segmentation, gaussian splatting, ar, 3d gaussian, semantic, survey  
- **[A Survey on Event-driven 3D Reconstruction: Development under Different Categories](https://arxiv.org/abs/2503.19753v2)**  
  Authors: Chuanzhi Xu, Haoxian Zhou, Haodong Chen, Vera Chung, Qiang Qu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.19753v2.pdf)  
  Keywords: lighting, ar, gaussian splatting, 3d gaussian, motion, dynamic, 3d reconstruction, fast, survey  
- **[Dynamic Scene Reconstruction: Recent Advance in Real-time Rendering and Streaming](https://arxiv.org/abs/2503.08166v1)**  
  Authors: Jiaxuan Zhu, Hao Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.08166v1.pdf)  
  Keywords: ar, gaussian splatting, 3d gaussian, dynamic, survey, real-time rendering  

### Acceleration

*Showing the latest 50 out of 510 papers*

- **[Hybrid 3D-4D Gaussian Splatting for Fast Dynamic Scene Representation](https://arxiv.org/abs/2505.13215v1)**  
  Authors: Seungjun Oh, Younggeun Lee, Hyejin Jeon, Eunbyung Park  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.13215v1.pdf)  
  Keywords: high-fidelity, gaussian splatting, 3d gaussian, motion, dynamic, head, fast, ar, 4d  
- **[iSegMan: Interactive Segment-and-Manipulate 3D Gaussians](https://arxiv.org/abs/2505.11934v1)**  
  Authors: Yian Zhao, Wanshi Xu, Ruochong Zheng, Pengchong Qiao, Chang Liu, Jie Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.11934v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://zhao-yian.github.io/iSegMan.)  
  Keywords: segmentation, 3d gaussian, efficient, ar, efficient rendering  
- **[GrowSplat: Constructing Temporal Digital Twins of Plants with Gaussian Splats](https://arxiv.org/abs/2505.10923v1)**  
  Authors: Simeon Adebola, Shuangyu Xie, Chung Min Kim, Justin Kerr, Bart M. van Marrewijk, Mieke van Vlaardingen, Tim van Daalen, Robert van Loo, Jose Luis Susa Rincon, Eugen Solowjow, Rick van de Zedde, Ken Goldberg  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.10923v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://berkeleyautomation.github.io/GrowSplat/)  
  Keywords: deformation, gaussian splatting, 3d gaussian, fast, ar, 4d  
- **[EA-3DGS: Efficient and Adaptive 3D Gaussians with Highly Enhanced Quality for outdoor scenes](https://arxiv.org/abs/2505.10787v1)**  
  Authors: Jianlin Guo, Haihong Xiao, Wenxiong Kang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.10787v1.pdf)  
  Keywords: nerf, ar, gaussian splatting, face, 3d gaussian, efficient, outdoor, real-time rendering, geometry  
- **[VRSplat: Fast and Robust Gaussian Splatting for Virtual Reality](https://arxiv.org/abs/2505.10144v1)**  
  Authors: Xuechang Tu, Lukas Radl, Michael Steiner, Markus Steinberger, Bernhard Kerbl, Fernando de la Torre  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.10144v1.pdf)  
  Keywords: gaussian splatting, face, 3d gaussian, vr, head, efficient, fast, ar  
- **[FOCI: Trajectory Optimization on Gaussian Splats](https://arxiv.org/abs/2505.08510v1)**  
  Authors: Mario Gomez Andreu, Maximum Wilder-Smith, Victor Klemm, Vaishakh Patil, Jesus Tordesillas, Marco Hutter  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.08510v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://rffr.leggedrobotics.com/works/foci/)  
  Keywords: nerf, robotics, gaussian splatting, 3d gaussian, 3d reconstruction, fast, ar  
- **[GIFStream: 4D Gaussian-based Immersive Video with Feature Stream](https://arxiv.org/abs/2505.07539v1)**  
  Authors: Hao Li, Sicheng Li, Xiang Gao, Abudouaihati Batuer, Lu Yu, Yiyi Liao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.07539v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://xdimlab.github.io/GIFStream)  
  Keywords: deformation, gaussian splatting, motion, efficient, fast, ar, real-time rendering, compression, 4d  
- **[TUGS: Physics-based Compact Representation of Underwater Scenes by Tensorized Gaussian](https://arxiv.org/abs/2505.08811v1)**  
  Authors: Shijie Lian, Ziyi Zhang, Laurence Tianruo Yang and, Mengyu Ren, Debin Liu, Hua Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.08811v1.pdf)  
  Keywords: nerf, compact, gaussian splatting, face, efficient, fast, ar, lightweight  
- **[Virtualized 3D Gaussians: Flexible Cluster-based Level-of-Detail System for Real-Time Rendering of Composed Scenes](https://arxiv.org/abs/2505.06523v1)**  
  Authors: Xijie Yang, Linning Xu, Lihan Jiang, Dahua Lin, Bo Dai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.06523v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, dynamic, efficient, ar, real-time rendering  
- **[UltraGauss: Ultrafast Gaussian Reconstruction of 3D Ultrasound Volumes](https://arxiv.org/abs/2505.05643v1)**  
  Authors: Mark C. Eid, Ana I. L. Namburete, João F. Henriques  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.05643v1.pdf)  
  Keywords: ar, gaussian splatting, 3d reconstruction, efficient, fast, survey  

### Applications

*Showing the latest 50 out of 1791 papers*

- **[SHaDe: Compact and Consistent Dynamic 3D Reconstruction via Tri-Plane Deformation and Latent Diffusion](https://arxiv.org/abs/2505.16535v1)**  
  Authors: Asrar Alruwayqi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.16535v1.pdf)  
  Keywords: sparse-view, deformation, gaussian splatting, compact, motion, dynamic, 3d reconstruction, head, efficient, ar, 4d  
- **[Motion Matters: Compact Gaussian Streaming for Free-Viewpoint Video Reconstruction](https://arxiv.org/abs/2505.16533v1)**  
  Authors: Jiacong Chen, Qingyu Mao, Youneng Bao, Xiandong Meng, Fanyang Meng, Ronggang Wang, Yongsheng Liang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.16533v1.pdf)  
  Keywords: high-fidelity, compact, gaussian splatting, face, 3d gaussian, motion, dynamic, head, efficient, ar  
- **[MAGIC: Motion-Aware Generative Inference via Confidence-Guided LLM](https://arxiv.org/abs/2505.16456v1)**  
  Authors: Siwei Meng, Yawei Luo, Ping Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.16456v1.pdf)  
  Keywords: 3d gaussian, dynamic, motion, ar  
- **[RUSplatting: Robust 3D Gaussian Splatting for Sparse-View Underwater Scene Reconstruction](https://arxiv.org/abs/2505.15737v1)**  
  Authors: Zhuodong Jiang, Haoran Wang, Guoxi Huang, Brett Seymour, Nantheera Anantrasirichai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.15737v1.pdf)  
  Keywords: high-fidelity, sparse-view, robotics, gaussian splatting, 3d gaussian, ar  
- **[PlantDreamer: Achieving Realistic 3D Plant Models with Diffusion-Guided Gaussian Splatting](https://arxiv.org/abs/2505.15528v1)**  
  Authors: Zane K J Hartley, Lewis A G Stuart, Andrew P French, Michael P Pound  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.15528v1.pdf)  
  Keywords: high-fidelity, gaussian splatting, 3d gaussian, ar, geometry  
- **[EVA: Expressive Virtual Avatars from Multi-view Videos](https://arxiv.org/abs/2505.15385v1)**  
  Authors: Hendrik Junkawitsch, Guoxing Sun, Heming Zhu, Christian Theobalt, Marc Habermann  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.15385v1.pdf)  
  Keywords: high-fidelity, deformation, human, face, tracking, 3d gaussian, neural rendering, motion, avatar, ar, body, geometry  
- **[R3GS: Gaussian Splatting for Robust Reconstruction and Relocalization in Unconstrained Image Collections](https://arxiv.org/abs/2505.15294v1)**  
  Authors: Xu yan, Zhaohui Wang, Rong Wei, Jingbo Yu, Dong Li, Xiangde Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.15294v1.pdf)  
  Keywords: lighting, ar, gaussian splatting, human, face, localization, outdoor, lightweight  
- **[GS2E: Gaussian Splatting is an Effective Data Generator for Event Stream Generation](https://arxiv.org/abs/2505.15287v1)**  
  Authors: Yuchen Li, Chaoran Feng, Zhenyu Tang, Kaiyuan Deng, Wangbo Yu, Yonghong Tian, Li Yuan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.15287v1.pdf)  
  Keywords: high-fidelity, lighting, gaussian splatting, 3d gaussian, motion, 3d reconstruction, ar  
- **[X-GRM: Large Gaussian Reconstruction Model for Sparse-view X-rays to Computed Tomography](https://arxiv.org/abs/2505.15235v1)**  
  Authors: Yifan Liu, Wuyang Li, Weihao Yu, Chenxin Li, Alexandre Alahi, Max Meng, Yixuan Yuan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.15235v1.pdf) | [![GitHub](https://img.shields.io/github/stars/CUHK-AIM-Group/X-GRM?style=social)](https://github.com/CUHK-AIM-Group/X-GRM)  
  Keywords: gaussian splatting, efficient, sparse-view, ar  
- **[GT^2-GS: Geometry-aware Texture Transfer for Gaussian Splatting](https://arxiv.org/abs/2505.15208v1)**  
  Authors: Wenjie Liu, Zhongliang Liu, Junwei Shu, Changbo Wang, Yang Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.15208v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://vpx-ecnu.github.io/GT2-GS-website.)  
  Keywords: gaussian splatting, ar, human, geometry  

### Avatar Generation

*Showing the latest 50 out of 604 papers*

- **[SHaDe: Compact and Consistent Dynamic 3D Reconstruction via Tri-Plane Deformation and Latent Diffusion](https://arxiv.org/abs/2505.16535v1)**  
  Authors: Asrar Alruwayqi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.16535v1.pdf)  
  Keywords: sparse-view, deformation, gaussian splatting, compact, motion, dynamic, 3d reconstruction, head, efficient, ar, 4d  
- **[Motion Matters: Compact Gaussian Streaming for Free-Viewpoint Video Reconstruction](https://arxiv.org/abs/2505.16533v1)**  
  Authors: Jiacong Chen, Qingyu Mao, Youneng Bao, Xiandong Meng, Fanyang Meng, Ronggang Wang, Yongsheng Liang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.16533v1.pdf)  
  Keywords: high-fidelity, compact, gaussian splatting, face, 3d gaussian, motion, dynamic, head, efficient, ar  
- **[EVA: Expressive Virtual Avatars from Multi-view Videos](https://arxiv.org/abs/2505.15385v1)**  
  Authors: Hendrik Junkawitsch, Guoxing Sun, Heming Zhu, Christian Theobalt, Marc Habermann  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.15385v1.pdf)  
  Keywords: high-fidelity, deformation, human, face, tracking, 3d gaussian, neural rendering, motion, avatar, ar, body, geometry  
- **[R3GS: Gaussian Splatting for Robust Reconstruction and Relocalization in Unconstrained Image Collections](https://arxiv.org/abs/2505.15294v1)**  
  Authors: Xu yan, Zhaohui Wang, Rong Wei, Jingbo Yu, Dong Li, Xiangde Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.15294v1.pdf)  
  Keywords: lighting, ar, gaussian splatting, human, face, localization, outdoor, lightweight  
- **[GT^2-GS: Geometry-aware Texture Transfer for Gaussian Splatting](https://arxiv.org/abs/2505.15208v1)**  
  Authors: Wenjie Liu, Zhongliang Liu, Junwei Shu, Changbo Wang, Yang Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.15208v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://vpx-ecnu.github.io/GT2-GS-website.)  
  Keywords: gaussian splatting, ar, human, geometry  
- **[Hybrid 3D-4D Gaussian Splatting for Fast Dynamic Scene Representation](https://arxiv.org/abs/2505.13215v1)**  
  Authors: Seungjun Oh, Younggeun Lee, Hyejin Jeon, Eunbyung Park  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.13215v1.pdf)  
  Keywords: high-fidelity, gaussian splatting, 3d gaussian, motion, dynamic, head, fast, ar, 4d  
- **[TACOcc:Target-Adaptive Cross-Modal Fusion with Volume Rendering for 3D Semantic Occupancy](https://arxiv.org/abs/2505.12693v1)**  
  Authors: Luyao Lei, Shuo Xu, Yifan Bai, Xing Wei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.12693v1.pdf)  
  Keywords: gaussian splatting, face, 3d gaussian, semantic, ar, geometry  
- **[EA-3DGS: Efficient and Adaptive 3D Gaussians with Highly Enhanced Quality for outdoor scenes](https://arxiv.org/abs/2505.10787v1)**  
  Authors: Jianlin Guo, Haihong Xiao, Wenxiong Kang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.10787v1.pdf)  
  Keywords: nerf, ar, gaussian splatting, face, 3d gaussian, efficient, outdoor, real-time rendering, geometry  
- **[VRSplat: Fast and Robust Gaussian Splatting for Virtual Reality](https://arxiv.org/abs/2505.10144v1)**  
  Authors: Xuechang Tu, Lukas Radl, Michael Steiner, Markus Steinberger, Bernhard Kerbl, Fernando de la Torre  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.10144v1.pdf)  
  Keywords: gaussian splatting, face, 3d gaussian, vr, head, efficient, fast, ar  
- **[ToonifyGB: StyleGAN-based Gaussian Blendshapes for 3D Stylized Head Avatars](https://arxiv.org/abs/2505.10072v1)**  
  Authors: Rui-Yang Ju, Sheng-Yen Huang, Yi-Ping Hung  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.10072v1.pdf)  
  Keywords: animation, face, 3d gaussian, avatar, head, efficient, ar  

### Dynamic Scene

*Showing the latest 50 out of 678 papers*

- **[SHaDe: Compact and Consistent Dynamic 3D Reconstruction via Tri-Plane Deformation and Latent Diffusion](https://arxiv.org/abs/2505.16535v1)**  
  Authors: Asrar Alruwayqi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.16535v1.pdf)  
  Keywords: sparse-view, deformation, gaussian splatting, compact, motion, dynamic, 3d reconstruction, head, efficient, ar, 4d  
- **[Motion Matters: Compact Gaussian Streaming for Free-Viewpoint Video Reconstruction](https://arxiv.org/abs/2505.16533v1)**  
  Authors: Jiacong Chen, Qingyu Mao, Youneng Bao, Xiandong Meng, Fanyang Meng, Ronggang Wang, Yongsheng Liang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.16533v1.pdf)  
  Keywords: high-fidelity, compact, gaussian splatting, face, 3d gaussian, motion, dynamic, head, efficient, ar  
- **[MAGIC: Motion-Aware Generative Inference via Confidence-Guided LLM](https://arxiv.org/abs/2505.16456v1)**  
  Authors: Siwei Meng, Yawei Luo, Ping Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.16456v1.pdf)  
  Keywords: 3d gaussian, dynamic, motion, ar  
- **[EVA: Expressive Virtual Avatars from Multi-view Videos](https://arxiv.org/abs/2505.15385v1)**  
  Authors: Hendrik Junkawitsch, Guoxing Sun, Heming Zhu, Christian Theobalt, Marc Habermann  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.15385v1.pdf)  
  Keywords: high-fidelity, deformation, human, face, tracking, 3d gaussian, neural rendering, motion, avatar, ar, body, geometry  
- **[GS2E: Gaussian Splatting is an Effective Data Generator for Event Stream Generation](https://arxiv.org/abs/2505.15287v1)**  
  Authors: Yuchen Li, Chaoran Feng, Zhenyu Tang, Kaiyuan Deng, Wangbo Yu, Yonghong Tian, Li Yuan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.15287v1.pdf)  
  Keywords: high-fidelity, lighting, gaussian splatting, 3d gaussian, motion, 3d reconstruction, ar  
- **[Scan, Materialize, Simulate: A Generalizable Framework for Physically Grounded Robot Planning](https://arxiv.org/abs/2505.14938v1)**  
  Authors: Amine Elhafsi, Daniel Morton, Marco Pavone  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.14938v1.pdf)  
  Keywords: segmentation, gaussian splatting, 3d gaussian, semantic, dynamic, understanding, ar  
- **[MGStream: Motion-aware 3D Gaussian for Streamable Dynamic Scene Reconstruction](https://arxiv.org/abs/2505.13839v1)**  
  Authors: Zhenyu Bao, Qing Li, Guibiao Liao, Zhongyuan Zhao, Kanglin Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.13839v1.pdf) | [![GitHub](https://img.shields.io/github/stars/pcl3dv/MGStream?style=social)](https://github.com/pcl3dv/MGStream)  
  Keywords: deformation, gaussian splatting, 3d gaussian, motion, dynamic, ar  
- **[Hybrid 3D-4D Gaussian Splatting for Fast Dynamic Scene Representation](https://arxiv.org/abs/2505.13215v1)**  
  Authors: Seungjun Oh, Younggeun Lee, Hyejin Jeon, Eunbyung Park  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.13215v1.pdf)  
  Keywords: high-fidelity, gaussian splatting, 3d gaussian, motion, dynamic, head, fast, ar, 4d  
- **[MonoMobility: Zero-Shot 3D Mobility Analysis from Monocular Videos](https://arxiv.org/abs/2505.11868v1)**  
  Authors: Hongyi Zhou, Xiaogang Wang, Yulan Guo, Kai Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.11868v1.pdf)  
  Keywords: gaussian splatting, motion, dynamic, ar, geometry  
- **[GrowSplat: Constructing Temporal Digital Twins of Plants with Gaussian Splats](https://arxiv.org/abs/2505.10923v1)**  
  Authors: Simeon Adebola, Shuangyu Xie, Chung Min Kim, Justin Kerr, Bart M. van Marrewijk, Mieke van Vlaardingen, Tim van Daalen, Robert van Loo, Jose Luis Susa Rincon, Eugen Solowjow, Rick van de Zedde, Ken Goldberg  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.10923v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://berkeleyautomation.github.io/GrowSplat/)  
  Keywords: deformation, gaussian splatting, 3d gaussian, fast, ar, 4d  

### Few-shot

*Showing the latest 50 out of 128 papers*

- **[SHaDe: Compact and Consistent Dynamic 3D Reconstruction via Tri-Plane Deformation and Latent Diffusion](https://arxiv.org/abs/2505.16535v1)**  
  Authors: Asrar Alruwayqi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.16535v1.pdf)  
  Keywords: sparse-view, deformation, gaussian splatting, compact, motion, dynamic, 3d reconstruction, head, efficient, ar, 4d  
- **[RUSplatting: Robust 3D Gaussian Splatting for Sparse-View Underwater Scene Reconstruction](https://arxiv.org/abs/2505.15737v1)**  
  Authors: Zhuodong Jiang, Haoran Wang, Guoxi Huang, Brett Seymour, Nantheera Anantrasirichai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.15737v1.pdf)  
  Keywords: high-fidelity, sparse-view, robotics, gaussian splatting, 3d gaussian, ar  
- **[X-GRM: Large Gaussian Reconstruction Model for Sparse-view X-rays to Computed Tomography](https://arxiv.org/abs/2505.15235v1)**  
  Authors: Yifan Liu, Wuyang Li, Weihao Yu, Chenxin Li, Alexandre Alahi, Max Meng, Yixuan Yuan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.15235v1.pdf) | [![GitHub](https://img.shields.io/github/stars/CUHK-AIM-Group/X-GRM?style=social)](https://github.com/CUHK-AIM-Group/X-GRM)  
  Keywords: gaussian splatting, efficient, sparse-view, ar  
- **[SpatialCrafter: Unleashing the Imagination of Video Diffusion Models for Scene Reconstruction from Limited Observations](https://arxiv.org/abs/2505.11992v1)**  
  Authors: Songchun Zhang, Huiyao Xu, Sitong Guo, Zhongwei Xie, Pengwei Liu, Hujun Bao, Weiwei Xu, Changqing Zou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.11992v1.pdf)  
  Keywords: 3d gaussian, semantic, efficient, ar, sparse view  
- **[Sparfels: Fast Reconstruction from Sparse Unposed Imagery](https://arxiv.org/abs/2505.02178v1)**  
  Authors: Shubhendu Jena, Amine Ouasfi, Mae Younes, Adnane Boukhayma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.02178v1.pdf)  
  Keywords: gaussian splatting, face, head, efficient, fast, ar, shape reconstruction, sparse view, geometry  
- **[SparSplat: Fast Multi-View Reconstruction with Generalizable 2D Gaussian Splatting](https://arxiv.org/abs/2505.02175v1)**  
  Authors: Shubhendu Jena, Shishir Reddy Vutukur, Adnane Boukhayma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.02175v1.pdf)  
  Keywords: sparse-view, gaussian splatting, face, 3d gaussian, 3d reconstruction, fast, ar, shape reconstruction, sparse view, geometry  
- **[A Survey on 3D Reconstruction Techniques in Plant Phenotyping: From Classical Methods to Neural Radiance Fields (NeRF), 3D Gaussian Splatting (3DGS), and Beyond](https://arxiv.org/abs/2505.00737v1)**  
  Authors: Jiajia Li, Xinda Qi, Seyed Hamidreza Nabaei, Meiqi Liu, Dong Chen, Xin Zhang, Xunyuan Yin, Zhaojian Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.00737v1.pdf) | [![GitHub](https://img.shields.io/github/stars/JiajiaLi04/3D-Reconstruction-Plants?style=social)](https://github.com/JiajiaLi04/3D-Reconstruction-Plants)  
  Keywords: nerf, ar, gaussian splatting, face, 3d gaussian, understanding, 3d reconstruction, outdoor, survey, sparse view, geometry  
- **[Sparse2DGS: Geometry-Prioritized Gaussian Splatting for Surface Reconstruction from Sparse Views](https://arxiv.org/abs/2504.20378v1)**  
  Authors: Jiang Wu, Rui Li, Yu Zhu, Rong Guo, Jinqiu Sun, Yanning Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.20378v1.pdf)  
  Keywords: nerf, sparse-view, gaussian splatting, face, motion, fast, ar, sparse view, geometry  
- **[PIN-WM: Learning Physics-INformed World Models for Non-Prehensile Manipulation](https://arxiv.org/abs/2504.16693v2)**  
  Authors: Wenxuan Li, Hang Zhao, Zhiyuan Yu, Yu Du, Qin Zou, Ruizhen Hu, Kai Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.16693v2.pdf)  
  Keywords: gaussian splatting, dynamic, efficient, ar, few-shot, body  
- **[IXGS-Intraoperative 3D Reconstruction from Sparse, Arbitrarily Posed Real X-rays](https://arxiv.org/abs/2504.14699v1)**  
  Authors: Sascha Jecklin, Aidana Massalimova, Ruyi Zha, Lilian Calvet, Christoph J. Laux, Mazda Farshad, Philipp Fürnstahl  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.14699v1.pdf)  
  Keywords: gaussian splatting, sparse-view, 3d reconstruction, ar  

### Geometry Reconstruction

*Showing the latest 50 out of 581 papers*

- **[SHaDe: Compact and Consistent Dynamic 3D Reconstruction via Tri-Plane Deformation and Latent Diffusion](https://arxiv.org/abs/2505.16535v1)**  
  Authors: Asrar Alruwayqi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.16535v1.pdf)  
  Keywords: sparse-view, deformation, gaussian splatting, compact, motion, dynamic, 3d reconstruction, head, efficient, ar, 4d  
- **[PlantDreamer: Achieving Realistic 3D Plant Models with Diffusion-Guided Gaussian Splatting](https://arxiv.org/abs/2505.15528v1)**  
  Authors: Zane K J Hartley, Lewis A G Stuart, Andrew P French, Michael P Pound  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.15528v1.pdf)  
  Keywords: high-fidelity, gaussian splatting, 3d gaussian, ar, geometry  
- **[EVA: Expressive Virtual Avatars from Multi-view Videos](https://arxiv.org/abs/2505.15385v1)**  
  Authors: Hendrik Junkawitsch, Guoxing Sun, Heming Zhu, Christian Theobalt, Marc Habermann  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.15385v1.pdf)  
  Keywords: high-fidelity, deformation, human, face, tracking, 3d gaussian, neural rendering, motion, avatar, ar, body, geometry  
- **[GS2E: Gaussian Splatting is an Effective Data Generator for Event Stream Generation](https://arxiv.org/abs/2505.15287v1)**  
  Authors: Yuchen Li, Chaoran Feng, Zhenyu Tang, Kaiyuan Deng, Wangbo Yu, Yonghong Tian, Li Yuan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.15287v1.pdf)  
  Keywords: high-fidelity, lighting, gaussian splatting, 3d gaussian, motion, 3d reconstruction, ar  
- **[GT^2-GS: Geometry-aware Texture Transfer for Gaussian Splatting](https://arxiv.org/abs/2505.15208v1)**  
  Authors: Wenjie Liu, Zhongliang Liu, Junwei Shu, Changbo Wang, Yang Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.15208v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://vpx-ecnu.github.io/GT2-GS-website.)  
  Keywords: gaussian splatting, ar, human, geometry  
- **[MonoSplat: Generalizable 3D Gaussian Splatting from Monocular Depth Foundation Models](https://arxiv.org/abs/2505.15185v1)**  
  Authors: Yifan Liu, Keyu Fan, Weihao Yu, Chenxin Li, Hao Lu, Yixuan Yuan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.15185v1.pdf) | [![GitHub](https://img.shields.io/github/stars/CUHK-AIM-Group/MonoSplat?style=social)](https://github.com/CUHK-AIM-Group/MonoSplat)  
  Keywords: high-fidelity, gaussian splatting, 3d gaussian, ar, lightweight, geometry  
- **[Recollection from Pensieve: Novel View Synthesis via Learning from Uncalibrated Videos](https://arxiv.org/abs/2505.13440v1)**  
  Authors: Ruoyu Wang, Yi Ma, Shenghua Gao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.13440v1.pdf) | [![GitHub](https://img.shields.io/github/stars/Dwawayu/Pensieve?style=social)](https://github.com/Dwawayu/Pensieve)  
  Keywords: gaussian splatting, 3d gaussian, ar, geometry  
- **[TACOcc:Target-Adaptive Cross-Modal Fusion with Volume Rendering for 3D Semantic Occupancy](https://arxiv.org/abs/2505.12693v1)**  
  Authors: Luyao Lei, Shuo Xu, Yifan Bai, Xing Wei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.12693v1.pdf)  
  Keywords: gaussian splatting, face, 3d gaussian, semantic, ar, geometry  
- **[GTR: Gaussian Splatting Tracking and Reconstruction of Unknown Objects Based on Appearance and Geometric Complexity](https://arxiv.org/abs/2505.11905v1)**  
  Authors: Takuya Ikeda, Sergey Zakharov, Muhammad Zubair Irshad, Istvan Balazs Opra, Shun Iwase, Dian Chen, Mark Tjersland, Robert Lee, Alexandre Dilly, Rares Ambrus, Koichi Nishiwaki  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.11905v1.pdf)  
  Keywords: high-fidelity, gaussian splatting, tracking, 3d gaussian, 3d reconstruction, ar, geometry  
- **[MonoMobility: Zero-Shot 3D Mobility Analysis from Monocular Videos](https://arxiv.org/abs/2505.11868v1)**  
  Authors: Hongyi Zhou, Xiaogang Wang, Yulan Guo, Kai Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.11868v1.pdf)  
  Keywords: gaussian splatting, motion, dynamic, ar, geometry  

### Large Scene

*Showing the latest 50 out of 101 papers*

- **[R3GS: Gaussian Splatting for Robust Reconstruction and Relocalization in Unconstrained Image Collections](https://arxiv.org/abs/2505.15294v1)**  
  Authors: Xu yan, Zhaohui Wang, Rong Wei, Jingbo Yu, Dong Li, Xiangde Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.15294v1.pdf)  
  Keywords: lighting, ar, gaussian splatting, human, face, localization, outdoor, lightweight  
- **[Gaussian Splatting as a Unified Representation for Autonomy in Unstructured Environments](https://arxiv.org/abs/2505.11794v1)**  
  Authors: Dexter Ong, Yuezhan Tao, Varun Murali, Igor Spasojevic, Vijay Kumar, Pratik Chaudhari  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.11794v1.pdf)  
  Keywords: gaussian splatting, semantic, ar, outdoor  
- **[EA-3DGS: Efficient and Adaptive 3D Gaussians with Highly Enhanced Quality for outdoor scenes](https://arxiv.org/abs/2505.10787v1)**  
  Authors: Jianlin Guo, Haihong Xiao, Wenxiong Kang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.10787v1.pdf)  
  Keywords: nerf, ar, gaussian splatting, face, 3d gaussian, efficient, outdoor, real-time rendering, geometry  
- **[Consistent Quantity-Quality Control across Scenes for Deployment-Aware Gaussian Splatting](https://arxiv.org/abs/2505.10473v2)**  
  Authors: Fengdi Zhang, Hongkun Cao, Ruqi Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.10473v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://zhang-fengdi.github.io/ControlGS/)  
  Keywords: compact, gaussian splatting, ar, 3d gaussian, semantic, outdoor  
- **[Large-Scale Gaussian Splatting SLAM](https://arxiv.org/abs/2505.09915v1)**  
  Authors: Zhe Xin, Chenyang Wu, Penghui Huang, Yanyong Zhang, Yinian Mao, Guoquan Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.09915v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://lsg-slam.github.io.)  
  Keywords: nerf, ar, gaussian splatting, tracking, 3d gaussian, outdoor, recognition, slam  
- **[NavDP: Learning Sim-to-Real Navigation Diffusion Policy with Privileged Information Guidance](https://arxiv.org/abs/2505.08712v2)**  
  Authors: Wenzhe Cai, Jiaqi Peng, Yuqiang Yang, Yujian Zhang, Meng Wei, Hanqing Wang, Yilun Chen, Tai Wang, Jiangmiao Pang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.08712v2.pdf)  
  Keywords: ar, gaussian splatting, human, localization, dynamic, efficient, mapping, outdoor  
- **[SLAG: Scalable Language-Augmented Gaussian Splatting](https://arxiv.org/abs/2505.08124v1)**  
  Authors: Laszlo Szilagyi, Francis Engelmann, Jeannette Bohg  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.08124v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://slag-project.github.io/.)  
  Keywords: robotics, gaussian splatting, 3d gaussian, large scene, efficient, ar  
- **[TUM2TWIN: Introducing the Large-Scale Multimodal Urban Digital Twin Benchmark Dataset](https://arxiv.org/abs/2505.07396v2)**  
  Authors: Olaf Wysocki, Benedikt Schwab, Manoj Kumar Biswanath, Michael Greza, Qilin Zhang, Jingwei Zhu, Thomas Froech, Medhini Heeramaglore, Ihab Hijazi, Khaoula Kanna, Mathias Pechinger, Zhaiyu Chen, Yao Sun, Alejandro Rueda Segura, Ziyang Xu, Omar AbdelGafar, Mansour Mehranfar, Chandan Yeshwanth, Yueh-Cheng Liu, Hadi Yazdi, Jiapan Wang, Stefan Auer, Katharina Anders, Klaus Bogenberger, Andre Borrmann, Angela Dai, Ludwig Hoegner, Christoph Holst, Thomas H. Kolbe, Ferdinand Ludwig, Matthias Nießner, Frank Petzold, Xiao Xiang Zhu, Boris Jutzi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.07396v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://tum2t.win)  
  Keywords: nerf, high-fidelity, segmentation, gaussian splatting, ar, semantic, outdoor  
- **[A Survey on 3D Reconstruction Techniques in Plant Phenotyping: From Classical Methods to Neural Radiance Fields (NeRF), 3D Gaussian Splatting (3DGS), and Beyond](https://arxiv.org/abs/2505.00737v1)**  
  Authors: Jiajia Li, Xinda Qi, Seyed Hamidreza Nabaei, Meiqi Liu, Dong Chen, Xin Zhang, Xunyuan Yin, Zhaojian Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.00737v1.pdf) | [![GitHub](https://img.shields.io/github/stars/JiajiaLi04/3D-Reconstruction-Plants?style=social)](https://github.com/JiajiaLi04/3D-Reconstruction-Plants)  
  Keywords: nerf, ar, gaussian splatting, face, 3d gaussian, understanding, 3d reconstruction, outdoor, survey, sparse view, geometry  
- **[HUG: Hierarchical Urban Gaussian Splatting with Block-Based Reconstruction](https://arxiv.org/abs/2504.16606v1)**  
  Authors: Zhongtao Wang, Mai Su, Huishan Au, Yilong Li, Xizhe Cao, Chengwei Pan, Yisong Chen, Guoping Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.16606v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, urban scene, efficient, ar  

### Model Compression

*Showing the latest 50 out of 682 papers*

- **[SHaDe: Compact and Consistent Dynamic 3D Reconstruction via Tri-Plane Deformation and Latent Diffusion](https://arxiv.org/abs/2505.16535v1)**  
  Authors: Asrar Alruwayqi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.16535v1.pdf)  
  Keywords: sparse-view, deformation, gaussian splatting, compact, motion, dynamic, 3d reconstruction, head, efficient, ar, 4d  
- **[Motion Matters: Compact Gaussian Streaming for Free-Viewpoint Video Reconstruction](https://arxiv.org/abs/2505.16533v1)**  
  Authors: Jiacong Chen, Qingyu Mao, Youneng Bao, Xiandong Meng, Fanyang Meng, Ronggang Wang, Yongsheng Liang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.16533v1.pdf)  
  Keywords: high-fidelity, compact, gaussian splatting, face, 3d gaussian, motion, dynamic, head, efficient, ar  
- **[R3GS: Gaussian Splatting for Robust Reconstruction and Relocalization in Unconstrained Image Collections](https://arxiv.org/abs/2505.15294v1)**  
  Authors: Xu yan, Zhaohui Wang, Rong Wei, Jingbo Yu, Dong Li, Xiangde Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.15294v1.pdf)  
  Keywords: lighting, ar, gaussian splatting, human, face, localization, outdoor, lightweight  
- **[X-GRM: Large Gaussian Reconstruction Model for Sparse-view X-rays to Computed Tomography](https://arxiv.org/abs/2505.15235v1)**  
  Authors: Yifan Liu, Wuyang Li, Weihao Yu, Chenxin Li, Alexandre Alahi, Max Meng, Yixuan Yuan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.15235v1.pdf) | [![GitHub](https://img.shields.io/github/stars/CUHK-AIM-Group/X-GRM?style=social)](https://github.com/CUHK-AIM-Group/X-GRM)  
  Keywords: gaussian splatting, efficient, sparse-view, ar  
- **[MonoSplat: Generalizable 3D Gaussian Splatting from Monocular Depth Foundation Models](https://arxiv.org/abs/2505.15185v1)**  
  Authors: Yifan Liu, Keyu Fan, Weihao Yu, Chenxin Li, Hao Lu, Yixuan Yuan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.15185v1.pdf) | [![GitHub](https://img.shields.io/github/stars/CUHK-AIM-Group/MonoSplat?style=social)](https://github.com/CUHK-AIM-Group/MonoSplat)  
  Keywords: high-fidelity, gaussian splatting, 3d gaussian, ar, lightweight, geometry  
- **[Is Semantic SLAM Ready for Embedded Systems ? A Comparative Survey](https://arxiv.org/abs/2505.12384v1)**  
  Authors: Calvin Galagain, Martyna Poreba, François Goulette  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.12384v1.pdf)  
  Keywords: nerf, segmentation, gaussian splatting, ar, 3d gaussian, semantic, localization, efficient, mapping, survey, slam  
- **[SpatialCrafter: Unleashing the Imagination of Video Diffusion Models for Scene Reconstruction from Limited Observations](https://arxiv.org/abs/2505.11992v1)**  
  Authors: Songchun Zhang, Huiyao Xu, Sitong Guo, Zhongwei Xie, Pengwei Liu, Hujun Bao, Weiwei Xu, Changqing Zou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.11992v1.pdf)  
  Keywords: 3d gaussian, semantic, efficient, ar, sparse view  
- **[iSegMan: Interactive Segment-and-Manipulate 3D Gaussians](https://arxiv.org/abs/2505.11934v1)**  
  Authors: Yian Zhao, Wanshi Xu, Ruochong Zheng, Pengchong Qiao, Chang Liu, Jie Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.11934v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://zhao-yian.github.io/iSegMan.)  
  Keywords: segmentation, 3d gaussian, efficient, ar, efficient rendering  
- **[EA-3DGS: Efficient and Adaptive 3D Gaussians with Highly Enhanced Quality for outdoor scenes](https://arxiv.org/abs/2505.10787v1)**  
  Authors: Jianlin Guo, Haihong Xiao, Wenxiong Kang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.10787v1.pdf)  
  Keywords: nerf, ar, gaussian splatting, face, 3d gaussian, efficient, outdoor, real-time rendering, geometry  
- **[GaussianFormer3D: Multi-Modal Gaussian-based Semantic Occupancy Prediction with 3D Deformable Attention](https://arxiv.org/abs/2505.10685v1)**  
  Authors: Lingjun Zhao, Sizhe Wei, James Hays, Lu Gan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.10685v1.pdf)  
  Keywords: compact, 3d gaussian, semantic, ar, autonomous driving, geometry  

### Quality Enhancement

*Showing the latest 50 out of 287 papers*

- **[Motion Matters: Compact Gaussian Streaming for Free-Viewpoint Video Reconstruction](https://arxiv.org/abs/2505.16533v1)**  
  Authors: Jiacong Chen, Qingyu Mao, Youneng Bao, Xiandong Meng, Fanyang Meng, Ronggang Wang, Yongsheng Liang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.16533v1.pdf)  
  Keywords: high-fidelity, compact, gaussian splatting, face, 3d gaussian, motion, dynamic, head, efficient, ar  
- **[RUSplatting: Robust 3D Gaussian Splatting for Sparse-View Underwater Scene Reconstruction](https://arxiv.org/abs/2505.15737v1)**  
  Authors: Zhuodong Jiang, Haoran Wang, Guoxi Huang, Brett Seymour, Nantheera Anantrasirichai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.15737v1.pdf)  
  Keywords: high-fidelity, sparse-view, robotics, gaussian splatting, 3d gaussian, ar  
- **[PlantDreamer: Achieving Realistic 3D Plant Models with Diffusion-Guided Gaussian Splatting](https://arxiv.org/abs/2505.15528v1)**  
  Authors: Zane K J Hartley, Lewis A G Stuart, Andrew P French, Michael P Pound  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.15528v1.pdf)  
  Keywords: high-fidelity, gaussian splatting, 3d gaussian, ar, geometry  
- **[EVA: Expressive Virtual Avatars from Multi-view Videos](https://arxiv.org/abs/2505.15385v1)**  
  Authors: Hendrik Junkawitsch, Guoxing Sun, Heming Zhu, Christian Theobalt, Marc Habermann  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.15385v1.pdf)  
  Keywords: high-fidelity, deformation, human, face, tracking, 3d gaussian, neural rendering, motion, avatar, ar, body, geometry  
- **[GS2E: Gaussian Splatting is an Effective Data Generator for Event Stream Generation](https://arxiv.org/abs/2505.15287v1)**  
  Authors: Yuchen Li, Chaoran Feng, Zhenyu Tang, Kaiyuan Deng, Wangbo Yu, Yonghong Tian, Li Yuan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.15287v1.pdf)  
  Keywords: high-fidelity, lighting, gaussian splatting, 3d gaussian, motion, 3d reconstruction, ar  
- **[MonoSplat: Generalizable 3D Gaussian Splatting from Monocular Depth Foundation Models](https://arxiv.org/abs/2505.15185v1)**  
  Authors: Yifan Liu, Keyu Fan, Weihao Yu, Chenxin Li, Hao Lu, Yixuan Yuan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.15185v1.pdf) | [![GitHub](https://img.shields.io/github/stars/CUHK-AIM-Group/MonoSplat?style=social)](https://github.com/CUHK-AIM-Group/MonoSplat)  
  Keywords: high-fidelity, gaussian splatting, 3d gaussian, ar, lightweight, geometry  
- **[Hybrid 3D-4D Gaussian Splatting for Fast Dynamic Scene Representation](https://arxiv.org/abs/2505.13215v1)**  
  Authors: Seungjun Oh, Younggeun Lee, Hyejin Jeon, Eunbyung Park  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.13215v1.pdf)  
  Keywords: high-fidelity, gaussian splatting, 3d gaussian, motion, dynamic, head, fast, ar, 4d  
- **[GTR: Gaussian Splatting Tracking and Reconstruction of Unknown Objects Based on Appearance and Geometric Complexity](https://arxiv.org/abs/2505.11905v1)**  
  Authors: Takuya Ikeda, Sergey Zakharov, Muhammad Zubair Irshad, Istvan Balazs Opra, Shun Iwase, Dian Chen, Mark Tjersland, Robert Lee, Alexandre Dilly, Rares Ambrus, Koichi Nishiwaki  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.11905v1.pdf)  
  Keywords: high-fidelity, gaussian splatting, tracking, 3d gaussian, 3d reconstruction, ar, geometry  
- **[TUM2TWIN: Introducing the Large-Scale Multimodal Urban Digital Twin Benchmark Dataset](https://arxiv.org/abs/2505.07396v2)**  
  Authors: Olaf Wysocki, Benedikt Schwab, Manoj Kumar Biswanath, Michael Greza, Qilin Zhang, Jingwei Zhu, Thomas Froech, Medhini Heeramaglore, Ihab Hijazi, Khaoula Kanna, Mathias Pechinger, Zhaiyu Chen, Yao Sun, Alejandro Rueda Segura, Ziyang Xu, Omar AbdelGafar, Mansour Mehranfar, Chandan Yeshwanth, Yueh-Cheng Liu, Hadi Yazdi, Jiapan Wang, Stefan Auer, Katharina Anders, Klaus Bogenberger, Andre Borrmann, Angela Dai, Ludwig Hoegner, Christoph Holst, Thomas H. Kolbe, Ferdinand Ludwig, Matthias Nießner, Frank Petzold, Xiao Xiang Zhu, Boris Jutzi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.07396v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://tum2t.win)  
  Keywords: nerf, high-fidelity, segmentation, gaussian splatting, ar, semantic, outdoor  
- **[SVAD: From Single Image to 3D Avatar via Synthetic Data Generation with Video Diffusion and Data Augmentation](https://arxiv.org/abs/2505.05475v1)**  
  Authors: Yonwoo Choi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.05475v1.pdf)  
  Keywords: high-fidelity, animation, gaussian splatting, human, face, 3d gaussian, avatar, ar, real-time rendering  

### Ray Tracing

- **[DNF-Avatar: Distilling Neural Fields for Real-time Animatable Avatar Relighting](https://arxiv.org/abs/2504.10486v1)**  
  Authors: Zeren Jiang, Shaofei Wang, Siyu Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.10486v1.pdf)  
  Keywords: lighting, gaussian splatting, relighting, human, shadow, avatar, ray tracing, fast, relightable, ar, geometry  
- **[Stochastic Ray Tracing of 3D Transparent Gaussians](https://arxiv.org/abs/2504.06598v2)**  
  Authors: Xin Sun, Iliyan Georgiev, Yun Fei, Miloš Hašan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.06598v2.pdf)  
  Keywords: lighting, gaussian splatting, relighting, 3d gaussian, ray tracing, efficient, acceleration, ar, efficient rendering  
- **[3D Gaussian Particle Approximation of VDB Datasets: A Study for Scientific Visualization](https://arxiv.org/abs/2504.04857v2)**  
  Authors: Isha Sharma, Dieter Schmalstieg  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.04857v2.pdf)  
  Keywords: animation, compact, gaussian splatting, 3d gaussian, dynamic, ray marching, efficient, acceleration, ar  
- **[3D Gaussian Inverse Rendering with Approximated Global Illumination](https://arxiv.org/abs/2504.01358v1)**  
  Authors: Zirui Wu, Jianteng Chen, Laijian Li, Shaoteng Wu, Zhikai Zhu, Kang Xu, Martin R. Oswald, Jie Song  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.01358v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://wuzirui.github.io/gs-ssr.)  
  Keywords: lighting, gaussian splatting, face, 3d gaussian, illumination, ray tracing, efficient, global illumination, ar, real-time rendering  
- **[Real-time Global Illumination for Dynamic 3D Gaussian Scenes](https://arxiv.org/abs/2503.17897v1)**  
  Authors: Chenxiao Hu, Meng Gai, Guoping Wang, Sheng Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.17897v1.pdf)  
  Keywords: lighting, light transport, face, 3d gaussian, dynamic, illumination, fast, global illumination, real-time rendering  
- **[REdiSplats: Ray Tracing for Editable Gaussian Splatting](https://arxiv.org/abs/2503.12284v1)**  
  Authors: Krzysztof Byrski, Grzegorz Wilczyński, Weronika Smolak-Dyżewska, Piotr Borycki, Dawid Baran, Sławomir Tadeja, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2503.12284v1.pdf)  
  Keywords: ar, gaussian splatting, 3d gaussian, neural rendering, shadow, ray tracing, fast, reflection  
- **[BEAM: Bridging Physically-based Rendering and Gaussian Modeling for Relightable Volumetric Video](https://arxiv.org/abs/2502.08297v1)**  
  Authors: Yu Hong, Yize Wu, Zhehao Shen, Chengcheng Guo, Yuheng Jiang, Yingliang Zhang, Jingyi Yu, Lan Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.08297v1.pdf)  
  Keywords: lighting, face, tracking, dynamic, ray tracing, efficient, relightable, ar, real-time rendering, 4d, geometry  
- **[MeshSplats: Mesh-Based Rendering with Gaussian Splatting Initialization](https://arxiv.org/abs/2502.07754v1)**  
  Authors: Rafał Tobiasz, Grzegorz Wilczyński, Marcin Mazur, Sławomir Tadeja, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.07754v1.pdf)  
  Keywords: lighting, gaussian splatting, face, shadow, ray tracing, reflection  
- **[Scalable 3D Gaussian Splatting-Based RF Signal Spatial Propagation Modeling](https://arxiv.org/abs/2502.01826v1)**  
  Authors: Kang Yang, Gaofeng Dong, Sijie Ji, Wan Du, Mani Srivastava  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.01826v1.pdf)  
  Keywords: gaussian splatting, 3d gaussian, ray tracing, ar, survey  
- **[Radiant Foam: Real-Time Differentiable Ray Tracing](https://arxiv.org/abs/2502.01157v1)**  
  Authors: Shrisudhan Govindarajan, Daniel Rebain, Kwang Moo Yi, Andrea Tagliasacchi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2502.01157v1.pdf)  
  Keywords: light transport, ar, gaussian splatting, ray tracing, efficient, acceleration, reflection  

### Relighting

*Showing the latest 50 out of 201 papers*

- **[R3GS: Gaussian Splatting for Robust Reconstruction and Relocalization in Unconstrained Image Collections](https://arxiv.org/abs/2505.15294v1)**  
  Authors: Xu yan, Zhaohui Wang, Rong Wei, Jingbo Yu, Dong Li, Xiangde Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.15294v1.pdf)  
  Keywords: lighting, ar, gaussian splatting, human, face, localization, outdoor, lightweight  
- **[GS2E: Gaussian Splatting is an Effective Data Generator for Event Stream Generation](https://arxiv.org/abs/2505.15287v1)**  
  Authors: Yuchen Li, Chaoran Feng, Zhenyu Tang, Kaiyuan Deng, Wangbo Yu, Yonghong Tian, Li Yuan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.15287v1.pdf)  
  Keywords: high-fidelity, lighting, gaussian splatting, 3d gaussian, motion, 3d reconstruction, ar  
- **[3D Gaussian Adaptive Reconstruction for Fourier Light-Field Microscopy](https://arxiv.org/abs/2505.12875v1)**  
  Authors: Chenyu Xu, Zhouyu Jin, Chengkang Shen, Hao Zhu, Zhan Ma, Bo Xiong, You Zhou, Xun Cao, Ning Gu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.12875v1.pdf)  
  Keywords: nerf, lighting, gaussian splatting, 3d gaussian, ar  
- **[Visual enhancement and 3D representation for underwater scenes: a review](https://arxiv.org/abs/2505.01869v1)**  
  Authors: Guoxi Huang, Haoran Wang, Brett Seymour, Evan Kovacs, John Ellerbrock, Dave Blackham, Nantheera Anantrasirichai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.01869v1.pdf)  
  Keywords: lighting, 3d gaussian, 3d reconstruction, ar, survey  
- **[TransparentGS: Fast Inverse Rendering of Transparent Objects with Gaussians](https://arxiv.org/abs/2504.18768v2)**  
  Authors: Letian Huang, Dongwei Ye, Jialin Dan, Chengzhi Tao, Huiwen Liu, Kun Zhou, Bo Ren, Yuanqi Li, Yanwen Guo, Jie Guo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.18768v2.pdf)  
  Keywords: ar, gaussian splatting, 3d gaussian, efficient, fast, reflection  
- **[RGS-DR: Reflective Gaussian Surfels with Deferred Rendering for Shiny Objects](https://arxiv.org/abs/2504.18468v3)**  
  Authors: Georgios Kouros, Minye Wu, Tinne Tuytelaars  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.18468v3.pdf)  
  Keywords: nerf, lighting, ar, gaussian splatting, relighting, face, 3d gaussian, reflection, geometry  
- **[iVR-GS: Inverse Volume Rendering for Explorable Visualization via Editable 3D Gaussian Splatting](https://arxiv.org/abs/2504.17954v1)**  
  Authors: Kaiyuan Tang, Siyuan Yao, Chaoli Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.17954v1.pdf) | [![GitHub](https://img.shields.io/github/stars/TouKaienn/iVR-GS?style=social)](https://github.com/TouKaienn/iVR-GS)  
  Keywords: nerf, lighting, gaussian splatting, 3d gaussian, vr, mapping, fast, ar  
- **[StyleMe3D: Stylization with Disentangled Priors by Multiple Encoders on 3D Gaussians](https://arxiv.org/abs/2504.15281v1)**  
  Authors: Cailin Zhuang, Yaoqi Hu, Xuanyang Zhang, Wei Cheng, Jiacheng Bao, Shengqi Liu, Yiying Yang, Xianfang Zeng, Gang Yu, Ming Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.15281v1.pdf)  
  Keywords: nerf, lighting, gaussian splatting, human, 3d gaussian, semantic, dynamic, quality enhancement, ar, real-time rendering  
- **[Immersive Teleoperation Framework for Locomanipulation Tasks](https://arxiv.org/abs/2504.15229v1)**  
  Authors: Takuya Boehringer, Jonathan Embley-Riches, Karim Hammoud, Valerio Modugno, Dimitrios Kanoulas  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.15229v1.pdf)  
  Keywords: lighting, gaussian splatting, face, vr, fast, ar  
- **[Metamon-GS: Enhancing Representability with Variance-Guided Densification and Light Encoding](https://arxiv.org/abs/2504.14460v1)**  
  Authors: Junyan Su, Baozhu Zhao, Xiaohan Zhang, Qi Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2504.14460v1.pdf)  
  Keywords: gaussian splatting, lighting, 3d gaussian, ar  

### SLAM

*Showing the latest 50 out of 267 papers*

- **[EVA: Expressive Virtual Avatars from Multi-view Videos](https://arxiv.org/abs/2505.15385v1)**  
  Authors: Hendrik Junkawitsch, Guoxing Sun, Heming Zhu, Christian Theobalt, Marc Habermann  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.15385v1.pdf)  
  Keywords: high-fidelity, deformation, human, face, tracking, 3d gaussian, neural rendering, motion, avatar, ar, body, geometry  
- **[R3GS: Gaussian Splatting for Robust Reconstruction and Relocalization in Unconstrained Image Collections](https://arxiv.org/abs/2505.15294v1)**  
  Authors: Xu yan, Zhaohui Wang, Rong Wei, Jingbo Yu, Dong Li, Xiangde Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.15294v1.pdf)  
  Keywords: lighting, ar, gaussian splatting, human, face, localization, outdoor, lightweight  
- **[Is Semantic SLAM Ready for Embedded Systems ? A Comparative Survey](https://arxiv.org/abs/2505.12384v1)**  
  Authors: Calvin Galagain, Martyna Poreba, François Goulette  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.12384v1.pdf)  
  Keywords: nerf, segmentation, gaussian splatting, ar, 3d gaussian, semantic, localization, efficient, mapping, survey, slam  
- **[GTR: Gaussian Splatting Tracking and Reconstruction of Unknown Objects Based on Appearance and Geometric Complexity](https://arxiv.org/abs/2505.11905v1)**  
  Authors: Takuya Ikeda, Sergey Zakharov, Muhammad Zubair Irshad, Istvan Balazs Opra, Shun Iwase, Dian Chen, Mark Tjersland, Robert Lee, Alexandre Dilly, Rares Ambrus, Koichi Nishiwaki  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.11905v1.pdf)  
  Keywords: high-fidelity, gaussian splatting, tracking, 3d gaussian, 3d reconstruction, ar, geometry  
- **[Large-Scale Gaussian Splatting SLAM](https://arxiv.org/abs/2505.09915v1)**  
  Authors: Zhe Xin, Chenyang Wu, Penghui Huang, Yanyong Zhang, Yinian Mao, Guoquan Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.09915v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://lsg-slam.github.io.)  
  Keywords: nerf, ar, gaussian splatting, tracking, 3d gaussian, outdoor, recognition, slam  
- **[Real2Render2Real: Scaling Robot Data Without Dynamics Simulation or Robot Hardware](https://arxiv.org/abs/2505.09601v1)**  
  Authors: Justin Yu, Letian Fu, Huang Huang, Karim El-Refai, Rares Andrei Ambrus, Richard Cheng, Muhammad Zubair Irshad, Ken Goldberg  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.09601v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://real2render2real.com)  
  Keywords: gaussian splatting, human, tracking, 3d gaussian, motion, dynamic, ar, geometry  
- **[NavDP: Learning Sim-to-Real Navigation Diffusion Policy with Privileged Information Guidance](https://arxiv.org/abs/2505.08712v2)**  
  Authors: Wenzhe Cai, Jiaqi Peng, Yuqiang Yang, Yujian Zhang, Meng Wei, Hanqing Wang, Yilun Chen, Tai Wang, Jiangmiao Pang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.08712v2.pdf)  
  Keywords: ar, gaussian splatting, human, localization, dynamic, efficient, mapping, outdoor  
- **[DLO-Splatting: Tracking Deformable Linear Objects Using 3D Gaussian Splatting](https://arxiv.org/abs/2505.08644v2)**  
  Authors: Holly Dinkel, Marcel Büsching, Alberta Longhini, Brian Coltin, Trey Smith, Danica Kragic, Mårten Björkman, Timothy Bretl  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.08644v2.pdf)  
  Keywords: gaussian splatting, tracking, 3d gaussian, dynamic, ar  
- **[Monocular Online Reconstruction with Enhanced Detail Preservation](https://arxiv.org/abs/2505.07887v2)**  
  Authors: Songyin Wu, Zhaoyang Lv, Yufeng Zhu, Duncan Frost, Zhengqin Li, Ling-Qi Yan, Carl Ren, Richard Newcombe, Zhao Dong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.07887v2.pdf)  
  Keywords: tracking, 3d gaussian, mapping, ar  
- **[Apply Hierarchical-Chain-of-Generation to Complex Attributes Text-to-3D Generation](https://arxiv.org/abs/2505.05505v1)**  
  Authors: Yiming Qin, Zhu Xu, Yang Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.05505v1.pdf) | [![GitHub](https://img.shields.io/github/stars/Wakals/GASCOL?style=social)](https://github.com/Wakals/GASCOL)  
  Keywords: localization, 3d gaussian, semantic, ar  

### Scene Understanding

*Showing the latest 50 out of 321 papers*

- **[Scan, Materialize, Simulate: A Generalizable Framework for Physically Grounded Robot Planning](https://arxiv.org/abs/2505.14938v1)**  
  Authors: Amine Elhafsi, Daniel Morton, Marco Pavone  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.14938v1.pdf)  
  Keywords: segmentation, gaussian splatting, 3d gaussian, semantic, dynamic, understanding, ar  
- **[TACOcc:Target-Adaptive Cross-Modal Fusion with Volume Rendering for 3D Semantic Occupancy](https://arxiv.org/abs/2505.12693v1)**  
  Authors: Luyao Lei, Shuo Xu, Yifan Bai, Xing Wei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.12693v1.pdf)  
  Keywords: gaussian splatting, face, 3d gaussian, semantic, ar, geometry  
- **[Is Semantic SLAM Ready for Embedded Systems ? A Comparative Survey](https://arxiv.org/abs/2505.12384v1)**  
  Authors: Calvin Galagain, Martyna Poreba, François Goulette  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.12384v1.pdf)  
  Keywords: nerf, segmentation, gaussian splatting, ar, 3d gaussian, semantic, localization, efficient, mapping, survey, slam  
- **[SpatialCrafter: Unleashing the Imagination of Video Diffusion Models for Scene Reconstruction from Limited Observations](https://arxiv.org/abs/2505.11992v1)**  
  Authors: Songchun Zhang, Huiyao Xu, Sitong Guo, Zhongwei Xie, Pengwei Liu, Hujun Bao, Weiwei Xu, Changqing Zou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.11992v1.pdf)  
  Keywords: 3d gaussian, semantic, efficient, ar, sparse view  
- **[iSegMan: Interactive Segment-and-Manipulate 3D Gaussians](https://arxiv.org/abs/2505.11934v1)**  
  Authors: Yian Zhao, Wanshi Xu, Ruochong Zheng, Pengchong Qiao, Chang Liu, Jie Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.11934v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://zhao-yian.github.io/iSegMan.)  
  Keywords: segmentation, 3d gaussian, efficient, ar, efficient rendering  
- **[Gaussian Splatting as a Unified Representation for Autonomy in Unstructured Environments](https://arxiv.org/abs/2505.11794v1)**  
  Authors: Dexter Ong, Yuezhan Tao, Varun Murali, Igor Spasojevic, Vijay Kumar, Pratik Chaudhari  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.11794v1.pdf)  
  Keywords: gaussian splatting, semantic, ar, outdoor  
- **[GaussianFormer3D: Multi-Modal Gaussian-based Semantic Occupancy Prediction with 3D Deformable Attention](https://arxiv.org/abs/2505.10685v1)**  
  Authors: Lingjun Zhao, Sizhe Wei, James Hays, Lu Gan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.10685v1.pdf)  
  Keywords: compact, 3d gaussian, semantic, ar, autonomous driving, geometry  
- **[Consistent Quantity-Quality Control across Scenes for Deployment-Aware Gaussian Splatting](https://arxiv.org/abs/2505.10473v2)**  
  Authors: Fengdi Zhang, Hongkun Cao, Ruqi Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.10473v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://zhang-fengdi.github.io/ControlGS/)  
  Keywords: compact, gaussian splatting, ar, 3d gaussian, semantic, outdoor  
- **[Advances in Radiance Field for Dynamic Scene: From Neural Field to Gaussian Field](https://arxiv.org/abs/2505.10049v2)**  
  Authors: Jinlong Fan, Xuepu Zeng, Jing Zhang, Mingming Gong, Yuxiang Yang, Dacheng Tao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.10049v2.pdf)  
  Keywords: ar, gaussian splatting, 3d gaussian, motion, dynamic, understanding, survey, body, 4d  
- **[Large-Scale Gaussian Splatting SLAM](https://arxiv.org/abs/2505.09915v1)**  
  Authors: Zhe Xin, Chenyang Wu, Penghui Huang, Yanyong Zhang, Yinian Mao, Guoquan Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2505.09915v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://lsg-slam.github.io.)  
  Keywords: nerf, ar, gaussian splatting, tracking, 3d gaussian, outdoor, recognition, slam  



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