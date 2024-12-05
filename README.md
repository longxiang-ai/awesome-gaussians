# Awesome Gaussian Splatting [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

这个仓库收集了与 Gaussian Splatting 相关的最新研究论文、项目和资源。内容每日自动更新。

> 最后更新时间: 2024-12-05 00:51:33

## 目录

- [最新论文](#最新论文)
- [经典论文](#经典论文)
- [开源项目](#开源项目)
- [应用](#应用)
- [教程与博客](#教程与博客)

## 最新论文
> 🔄 每日更新

### 2024年12月
- **[AniGS: Animatable Gaussian Avatar from a Single Image with Inconsistent Gaussian Reconstruction](https://arxiv.org/abs/2412.02684v1)**  
  作者: Lingteng Qiu, Shenhao Zhu, Qi Zuo, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.02684v1.pdf)  
  摘要: Generating animatable human avatars from a single image is essential for various digital human modeling applications. Existing 3D reconstruction methods often struggle to capture fine details in anima...  
  关键词: gaussian splatting, real-time rendering, 3d reconstruction  
- **[Towards Rich Emotions in 3D Avatars: A Text-to-3D Avatar Generation Benchmark](https://arxiv.org/abs/2412.02508v1)**  
  作者: Haidong Xu, Meishan Zhang, Hao Ju, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.02508v1.pdf)  
  摘要: Producing emotionally dynamic 3D facial avatars with text derived from spoken words (Emo3D) has been a pivotal research topic in 3D avatar generation. While progress has been made in general-purpose 3...  
  关键词: 3d gaussian  
- **[RelayGS: Reconstructing Dynamic Scenes with Large-Scale and Complex Motions via Relay Gaussians](https://arxiv.org/abs/2412.02493v1)**  
  作者: Qiankun Gao, Yanmin Wu, Chengxiang Wen, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.02493v1.pdf) | [![Stars](https://img.shields.io/github/stars/gqk/RelayGS?style=social)](https://github.com/gqk/RelayGS)  
  摘要: Reconstructing dynamic scenes with large-scale and complex motions remains a significant challenge. Recent techniques like Neural Radiance Fields and 3D Gaussian Splatting (3DGS) have shown promise bu...  
  关键词: gaussian splatting, 3d gaussian  
- **[TimeWalker: Personalized Neural Space for Lifelong Head Avatars](https://arxiv.org/abs/2412.02421v1)**  
  作者: Dongwei Pan, Yang Li, Hongsheng Li, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.02421v1.pdf)  
  摘要: We present TimeWalker, a novel framework that models realistic, full-scale 3D head avatars of a person on lifelong scale. Unlike current human head avatar pipelines that capture identity at the moment...  
  关键词: gaussian splatting  
- **[Realistic Surgical Simulation from Monocular Videos](https://arxiv.org/abs/2412.02359v1)**  
  作者: Kailing Wang, Chen Yang, Keyang Zhao, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.02359v1.pdf)  
  摘要: This paper tackles the challenge of automatically performing realistic surgical simulations from readily available surgical videos. Recent efforts have successfully integrated physically grounded dyna...  
  关键词: 3d gaussian  
- **[GSGTrack: Gaussian Splatting-Guided Object Pose Tracking from RGB Videos](https://arxiv.org/abs/2412.02267v1)**  
  作者: Zhiyuan Chen, Fan Lu, Guo Yu, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.02267v1.pdf)  
  摘要: Tracking the 6DoF pose of unknown objects in monocular RGB video sequences is crucial for robotic manipulation. However, existing approaches typically rely on accurate depth information, which is non-...  
  关键词: gaussian splatting, 3d gaussian  
- **[Multi-robot autonomous 3D reconstruction using Gaussian splatting with Semantic guidance](https://arxiv.org/abs/2412.02249v1)**  
  作者: Jing Zeng, Qi Ye, Tianle Liu, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.02249v1.pdf)  
  摘要: Implicit neural representations and 3D Gaussian splatting (3DGS) have shown great potential for scene reconstruction. Recent studies have expanded their applications in autonomous reconstruction throu...  
  关键词: gaussian splatting, 3d gaussian, 3d reconstruction  
- **[SparseLGS: Sparse View Language Embedded Gaussian Splatting](https://arxiv.org/abs/2412.02245v1)**  
  作者: Jun Hu, Zhang Chen, Zhong Li, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.02245v1.pdf)  
  摘要: Recently, several studies have combined Gaussian Splatting to obtain scene representations with language embeddings for open-vocabulary 3D scene understanding. While these methods perform well, they e...  
  关键词: gaussian splatting  
- **[How to Use Diffusion Priors under Sparse Views?](https://arxiv.org/abs/2412.02225v1)**  
  作者: Qisen Wang, Yifan Zhao, Jiawei Ma, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.02225v1.pdf) | [![Stars](https://img.shields.io/github/stars/iCVTEAM/IPSM?style=social)](https://github.com/iCVTEAM/IPSM)  
  摘要: Novel view synthesis under sparse views has been a long-term important challenge in 3D reconstruction. Existing works mainly rely on introducing external semantic or depth priors to supervise the opti...  
  关键词: gaussian splatting, 3d gaussian, 3d reconstruction  
- **[SparseGrasp: Robotic Grasping via 3D Semantic Gaussian Splatting from Sparse Multi-View RGB Images](https://arxiv.org/abs/2412.02140v1)**  
  作者: Junqiu Yu, Xinlin Ren, Yongchong Gu, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.02140v1.pdf)  
  摘要: Language-guided robotic grasping is a rapidly advancing field where robots are instructed using human language to grasp specific objects. However, existing methods often depend on dense camera views a...  
  关键词: gaussian splatting, 3d gaussian  
- **[Gaussian Object Carver: Object-Compositional Gaussian Splatting with surfaces completion](https://arxiv.org/abs/2412.02075v1)**  
  作者: Liu Liu, Xinjie Wang, Jiaxiong Qiu, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.02075v1.pdf)  
  摘要: 3D scene reconstruction is a foundational problem in computer vision. Despite recent advancements in Neural Implicit Representations (NIR), existing methods often lack editability and compositional fl...  
  关键词: gaussian splatting, 3d gaussian  
- **[Planar Gaussian Splatting](https://arxiv.org/abs/2412.01931v1)**  
  作者: Farhad G. Zanjani, Hong Cai, Hanno Ackermann, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.01931v1.pdf)  
  摘要: This paper presents Planar Gaussian Splatting (PGS), a novel neural rendering approach to learn the 3D geometry and parse the 3D planes of a scene, directly from multiple RGB images. The PGS leverages...  
  关键词: gaussian splatting, neural rendering  
- **[HDGS: Textured 2D Gaussian Splatting for Enhanced Scene Rendering](https://arxiv.org/abs/2412.01823v1)**  
  作者: Yunzhou Song, Heguang Lin, Jiahui Lei, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.01823v1.pdf)  
  摘要: Recent advancements in neural rendering, particularly 2D Gaussian Splatting (2DGS), have shown promising results for jointly reconstructing fine appearance and geometry by leveraging 2D Gaussian surfe...  
  关键词: gaussian splatting, neural rendering  
- **[Occam's LGS: A Simple Approach for Language Gaussian Splatting](https://arxiv.org/abs/2412.01807v1)**  
  作者: Jiahuan Cheng, Jan-Nico Zaech, Luc Van Gool, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.01807v1.pdf)  
  摘要: TL;DR: Gaussian Splatting is a widely adopted approach for 3D scene representation that offers efficient, high-quality 3D reconstruction and rendering. A major reason for the success of 3DGS is its si...  
  关键词: gaussian splatting, 3d gaussian, 3d reconstruction  
- **[CTRL-D: Controllable Dynamic 3D Scene Editing with Personalized 2D Diffusion](https://arxiv.org/abs/2412.01792v1)**  
  作者: Kai He, Chin-Hsuan Wu, Igor Gilitschenski  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.01792v1.pdf)  
  摘要: Recent advances in 3D representations, such as Neural Radiance Fields and 3D Gaussian Splatting, have greatly improved realistic scene modeling and novel-view synthesis. However, achieving controllabl...  
  关键词: gaussian splatting, 3d gaussian  
- **[Horizon-GS: Unified 3D Gaussian Splatting for Large-Scale Aerial-to-Ground Scenes](https://arxiv.org/abs/2412.01745v1)**  
  作者: Lihan Jiang, Kerui Ren, Mulin Yu, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.01745v1.pdf)  
  摘要: Seamless integration of both aerial and street view images remains a significant challenge in neural scene reconstruction and rendering. Existing methods predominantly focus on single domain, limiting...  
  关键词: gaussian splatting  
- **[HUGSIM: A Real-Time, Photo-Realistic and Closed-Loop Simulator for Autonomous Driving](https://arxiv.org/abs/2412.01718v1)**  
  作者: Hongyu Zhou, Longzhong Lin, Jiabao Wang, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.01718v1.pdf)  
  摘要: In the past few decades, autonomous driving algorithms have made significant progress in perception, planning, and control. However, evaluating individual components does not fully reflect the perform...  
  关键词: gaussian splatting, 3d gaussian  
- **[Driving Scene Synthesis on Free-form Trajectories with Generative Prior](https://arxiv.org/abs/2412.01717v1)**  
  作者: Zeyu Yang, Zijie Pan, Yuankun Yang, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.01717v1.pdf)  
  摘要: Driving scene synthesis along free-form trajectories is essential for driving simulations to enable closed-loop evaluation of end-to-end driving policies. While existing methods excel at novel view sy...  
  关键词: gaussian splatting  
- **[Diffusion Models with Anisotropic Gaussian Splatting for Image Inpainting](https://arxiv.org/abs/2412.01682v2)**  
  作者: Jacob Fein-Ashley, Benjamin Fein-Ashley  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.01682v2.pdf)  
  摘要: Image inpainting is a fundamental task in computer vision, aiming to restore missing or corrupted regions in images realistically. While recent deep learning approaches have significantly advanced the...  
  关键词: gaussian splatting  
- **[3DSceneEditor: Controllable 3D Scene Editing with Gaussian Splatting](https://arxiv.org/abs/2412.01583v1)**  
  作者: Ziyang Yan, Lei Li, Yihua Shao, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.01583v1.pdf)  
  摘要: The creation of 3D scenes has traditionally been both labor-intensive and costly, requiring designers to meticulously configure 3D assets and environments. Recent advancements in generative AI, includ...  
  关键词: gaussian splatting  
- **[SfM-Free 3D Gaussian Splatting via Hierarchical Training](https://arxiv.org/abs/2412.01553v1)**  
  作者: Bo Ji, Angela Yao  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.01553v1.pdf) | [![Stars](https://img.shields.io/github/stars/jibo27/3DGS_Hierarchical_Training?style=social)](https://github.com/jibo27/3DGS_Hierarchical_Training)  
  摘要: Standard 3D Gaussian Splatting (3DGS) relies on known or pre-computed camera poses and a sparse point cloud, obtained from structure-from-motion (SfM) preprocessing, to initialize and grow 3D Gaussian...  
  关键词: gaussian splatting, 3d gaussian  
- **[GFreeDet: Exploiting Gaussian Splatting and Foundation Models for Model-free Unseen Object Detection in the BOP Challenge 2024](https://arxiv.org/abs/2412.01552v2)**  
  作者: Xingyu Liu, Yingyue Li, Chengxi Li, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.01552v2.pdf)  
  摘要: In this report, we provide the technical details of the submitted method GFreeDet, which exploits Gaussian splatting and vision Foundation models for the model-free unseen object Detection track in th...  
  关键词: gaussian splatting  
- **[6DOPE-GS: Online 6D Object Pose Estimation using Gaussian Splatting](https://arxiv.org/abs/2412.01543v1)**  
  作者: Yufeng Jin, Vignesh Prasad, Snehal Jauhri, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.01543v1.pdf)  
  摘要: Efficient and accurate object pose estimation is an essential component for modern vision systems in many applications such as Augmented Reality, autonomous driving, and robotics. While research in mo...  
  关键词: gaussian splatting  
- **[Structured 3D Latents for Scalable and Versatile 3D Generation](https://arxiv.org/abs/2412.01506v1)**  
  作者: Jianfeng Xiang, Zelong Lv, Sicheng Xu, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.01506v1.pdf)  
  摘要: We introduce a novel 3D generation method for versatile and high-quality 3D asset creation. The cornerstone is a unified Structured LATent (SLAT) representation which allows decoding to different outp...  
  关键词: 3d gaussian  
- **[ULSR-GS: Ultra Large-scale Surface Reconstruction Gaussian Splatting with Multi-View Geometric Consistency](https://arxiv.org/abs/2412.01402v1)**  
  作者: Zhuoxiao Li, Shanliang Yao, Qizhong Gao, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.01402v1.pdf)  
  摘要: While Gaussian Splatting (GS) demonstrates efficient and high-quality scene rendering and small area surface extraction ability, it falls short in handling large-scale aerial image surface extraction ...  
  关键词: gaussian splatting  
- **[RGBDS-SLAM: A RGB-D Semantic Dense SLAM Based on 3D Multi Level Pyramid Gaussian Splatting](https://arxiv.org/abs/2412.01217v1)**  
  作者: Zhenzhong Cao  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.01217v1.pdf) | [![Stars](https://img.shields.io/github/stars/zhenzhongcao/RGBDS-SLAM?style=social)](https://github.com/zhenzhongcao/RGBDS-SLAM)  
  摘要: High-quality reconstruction is crucial for dense SLAM. Recent popular approaches utilize 3D Gaussian Splatting (3D GS) techniques for RGB, depth, and semantic reconstruction of scenes. However, these ...  
  关键词: gaussian splatting, 3d gaussian  
- **[One Shot, One Talk: Whole-body Talking Avatar from a Single Image](https://arxiv.org/abs/2412.01106v1)**  
  作者: Jun Xiang, Yudong Guo, Leipeng Hu, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.01106v1.pdf)  
  摘要: Building realistic and animatable avatars still requires minutes of multi-view or monocular self-rotating videos, and most methods lack precise control over gestures and expressions. To push this boun...  
- **[Ref-GS: Directional Factorization for 2D Gaussian Splatting](https://arxiv.org/abs/2412.00905v1)**  
  作者: Youjia Zhang, Anpei Chen, Yumin Wan, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.00905v1.pdf)  
  摘要: In this paper, we introduce Ref-GS, a novel approach for directional light factorization in 2D Gaussian splatting, which enables photorealistic view-dependent appearance rendering and precise geometry...  
  关键词: gaussian splatting  
- **[DynSUP: Dynamic Gaussian Splatting from An Unposed Image Pair](https://arxiv.org/abs/2412.00851v1)**  
  作者: Weihang Li, Weirong Chen, Shenhan Qian, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.00851v1.pdf)  
  摘要: Recent advances in 3D Gaussian Splatting have shown promising results. Existing methods typically assume static scenes and/or multiple images with prior poses. Dynamics, sparse views, and unknown pose...  
  关键词: gaussian splatting, 3d gaussian  
- **[VR-Doh: Hands-on 3D Modeling in Virtual Reality](https://arxiv.org/abs/2412.00814v1)**  
  作者: Zhaofeng Luo, Zhitong Cui, Shijian Luo, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.00814v1.pdf)  
  摘要: We present VR-Doh, a hands-on 3D modeling system designed for creating and manipulating elastoplastic objects in virtual reality (VR). The system employs the Material Point Method (MPM) for simulating...  
  关键词: gaussian splatting  
- **[ChatSplat: 3D Conversational Gaussian Splatting](https://arxiv.org/abs/2412.00734v1)**  
  作者: Hanlin Chen, Fangyin Wei, Gim Hee Lee  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.00734v1.pdf)  
  摘要: Humans naturally interact with their 3D surroundings using language, and modeling 3D language fields for scene understanding and interaction has gained growing interest. This paper introduces ChatSpla...  
  关键词: 3d gaussian  
- **[FlashSLAM: Accelerated RGB-D SLAM for Real-Time 3D Scene Reconstruction with Gaussian Splatting](https://arxiv.org/abs/2412.00682v1)**  
  作者: Phu Pham, Damon Conover, Aniket Bera  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.00682v1.pdf)  
  摘要: We present FlashSLAM, a novel SLAM approach that leverages 3D Gaussian Splatting for efficient and robust 3D scene reconstruction. Existing 3DGS-based SLAM methods often fall short in sparse view sett...  
  关键词: gaussian splatting, 3d gaussian, 3d reconstruction  
- **[A Lesson in Splats: Teacher-Guided Diffusion for 3D Gaussian Splats Generation with 2D Supervision](https://arxiv.org/abs/2412.00623v1)**  
  作者: Chensheng Peng, Ido Sobol, Masayoshi Tomizuka, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.00623v1.pdf)  
  摘要: We introduce a diffusion model for Gaussian Splats, SplatDiffusion, to enable generation of three-dimensional structures from single images, addressing the ill-posed nature of lifting 2D inputs to 3D....  
  关键词: 3d gaussian  

### 2024年11月
- **[Speedy-Splat: Fast 3D Gaussian Splatting with Sparse Pixels and Sparse Primitives](https://arxiv.org/abs/2412.00578v1)**  
  作者: Alex Hanson, Allen Tu, Geng Lin, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.00578v1.pdf)  
  摘要: 3D Gaussian Splatting (3D-GS) is a recent 3D scene reconstruction technique that enables real-time rendering of novel views by modeling scenes as parametric point clouds of differentiable 3D Gaussians...  
  关键词: gaussian splatting, 3d gaussian, real-time rendering, nerf  
- **[Instant3dit: Multiview Inpainting for Fast Editing of 3D Objects](https://arxiv.org/abs/2412.00518v1)**  
  作者: Amir Barda, Matheus Gadelha, Vladimir G. Kim, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.00518v1.pdf)  
  摘要: We propose a generative technique to edit 3D shapes, represented as meshes, NeRFs, or Gaussian Splats, in approximately 3 seconds, without the need for running an SDS type of optimization. Our key ins...  
  关键词: nerf  
- **[LineGS : 3D Line Segment Representation on 3D Gaussian Splatting](https://arxiv.org/abs/2412.00477v1)**  
  作者: Chenggang Yang, Yuang Shi, Wei Tsang Ooi  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.00477v1.pdf)  
  摘要: Abstract representations of 3D scenes are essential in computer vision, supporting tasks like mapping, localization, and surface reconstruction. Line segments are commonly used to capture scene struct...  
  关键词: gaussian splatting, 3d gaussian, 3d reconstruction  
- **[GradiSeg: Gradient-Guided Gaussian Segmentation with Enhanced 3D Boundary Precision](https://arxiv.org/abs/2412.00392v1)**  
  作者: Zehao Li, Wenwei Han, Yujun Cai, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.00392v1.pdf)  
  摘要: While 3D Gaussian Splatting enables high-quality real-time rendering, existing Gaussian-based frameworks for 3D semantic segmentation still face significant challenges in boundary recognition accuracy...  
  关键词: gaussian splatting, 3d gaussian, real-time rendering  
- **[Gaussians on their Way: Wasserstein-Constrained 4D Gaussian Splatting with State-Space Modeling](https://arxiv.org/abs/2412.00333v1)**  
  作者: Junli Deng, Yihao Luo  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.00333v1.pdf)  
  摘要: Dynamic scene rendering has taken a leap forward with the rise of 4D Gaussian Splatting, but there's still one elusive challenge: how to make 3D Gaussians move through time as naturally as they would ...  
  关键词: gaussian splatting, 3d gaussian  
- **[GuardSplat: Efficient and Robust Watermarking for 3D Gaussian Splatting](https://arxiv.org/abs/2411.19895v2)**  
  作者: Zixuan Chen, Guangcong Wang, Jiahao Zhu, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.19895v2.pdf)  
  摘要: 3D Gaussian Splatting (3DGS) has recently created impressive assets for various applications. However, the copyright of these assets is not well protected as existing watermarking methods are not suit...  
  关键词: gaussian splatting, 3d gaussian  
- **[DeSplat: Decomposed Gaussian Splatting for Distractor-Free Rendering](https://arxiv.org/abs/2411.19756v1)**  
  作者: Yihao Wang, Marcus Klasson, Matias Turkulainen, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.19756v1.pdf)  
  摘要: Gaussian splatting enables fast novel view synthesis in static 3D environments. However, reconstructing real-world environments remains challenging as distractors or occluders break the multi-view con...  
  关键词: gaussian splatting, 3d reconstruction  
- **[TexGaussian: Generating High-quality PBR Material via Octree-based 3D Gaussian Splatting](https://arxiv.org/abs/2411.19654v1)**  
  作者: Bojun Xiong, Jialun Liu, Jiakui Hu, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.19654v1.pdf)  
  摘要: Physically Based Rendering (PBR) materials play a crucial role in modern graphics, enabling photorealistic rendering across diverse environment maps. Developing an effective and efficient algorithm th...  
  关键词: gaussian splatting, 3d gaussian  
- **[Tortho-Gaussian: Splatting True Digital Orthophoto Maps](https://arxiv.org/abs/2411.19594v1)**  
  作者: Xin Wang, Wendi Zhang, Hong Xie, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.19594v1.pdf)  
  摘要: True Digital Orthophoto Maps (TDOMs) are essential products for digital twins and Geographic Information Systems (GIS). Traditionally, TDOM generation involves a complex set of traditional photogramme...  
  关键词: gaussian splatting, 3d gaussian  
- **[Gaussian Splashing: Direct Volumetric Rendering Underwater](https://arxiv.org/abs/2411.19588v1)**  
  作者: Nir Mualem, Roy Amoyal, Oren Freifeld, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.19588v1.pdf)  
  摘要: In underwater images, most useful features are occluded by water. The extent of the occlusion depends on imaging geometry and can vary even across a sequence of burst images. As a result, 3D reconstru...  
  关键词: gaussian splatting, 3d gaussian, 3d reconstruction, nerf  
- **[Bootstraping Clustering of Gaussians for View-consistent 3D Scene Understanding](https://arxiv.org/abs/2411.19551v1)**  
  作者: Wenbo Zhang, Lu Zhang, Ping Hu, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.19551v1.pdf)  
  摘要: Injecting semantics into 3D Gaussian Splatting (3DGS) has recently garnered significant attention. While current approaches typically distill 3D semantic features from 2D foundational models (e.g., CL...  
  关键词: gaussian splatting, 3d gaussian  
- **[ReconDreamer: Crafting World Models for Driving Scene Reconstruction via Online Restoration](https://arxiv.org/abs/2411.19548v1)**  
  作者: Chaojun Ni, Guosheng Zhao, Xiaofeng Wang, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.19548v1.pdf)  
  摘要: Closed-loop simulation is crucial for end-to-end autonomous driving. Existing sensor simulation methods (e.g., NeRF and 3DGS) reconstruct driving scenes based on conditions that closely mirror trainin...  
  关键词: nerf  
- **[T-3DGS: Removing Transient Objects for 3D Scene Reconstruction](https://arxiv.org/abs/2412.00155v1)**  
  作者: Vadim Pryadilshchikov, Alexander Markin, Artem Komarichev, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.00155v1.pdf)  
  摘要: We propose a novel framework to remove transient objects from input videos for 3D scene reconstruction using Gaussian Splatting. Our framework consists of the following steps. In the first step, we pr...  
  关键词: gaussian splatting, 3d gaussian  
- **[GausSurf: Geometry-Guided 3D Gaussian Splatting for Surface Reconstruction](https://arxiv.org/abs/2411.19454v2)**  
  作者: Jiepeng Wang, Yuan Liu, Peng Wang, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.19454v2.pdf)  
  摘要: 3D Gaussian Splatting has achieved impressive performance in novel view synthesis with real-time rendering capabilities. However, reconstructing high-quality surfaces with fine details using 3D Gaussi...  
  关键词: gaussian splatting, 3d gaussian, real-time rendering  
- **[RF-3DGS: Wireless Channel Modeling with Radio Radiance Field and 3D Gaussian Splatting](https://arxiv.org/abs/2411.19420v1)**  
  作者: Lihao Zhang, Haijian Sun, Samuel Berweger, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.19420v1.pdf)  
  摘要: Precisely modeling radio propagation in complex environments has been a significant challenge, especially with the advent of 5G and beyond networks, where managing massive antenna arrays demands more ...  
  关键词: gaussian splatting, 3d gaussian  
- **[SAMa: Material-aware 3D Selection and Segmentation](https://arxiv.org/abs/2411.19322v1)**  
  作者: Michael Fischer, Iliyan Georgiev, Thibault Groueix, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.19322v1.pdf)  
  摘要: Decomposing 3D assets into material parts is a common task for artists and creators, yet remains a highly manual process. In this work, we introduce Select Any Material (SAMa), a material selection ap...  
  关键词: nerf  
- **[UrbanCAD: Towards Highly Controllable and Photorealistic 3D Vehicles for Urban Scene Simulation](https://arxiv.org/abs/2411.19292v1)**  
  作者: Yichong Lu, Yichi Cai, Shangzhan Zhang, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.19292v1.pdf)  
  摘要: Photorealistic 3D vehicle models with high controllability are essential for autonomous driving simulation and data augmentation. While handcrafted CAD models provide flexible controllability, free CA...  
- **[SADG: Segment Any Dynamic Gaussian Without Object Trackers](https://arxiv.org/abs/2411.19290v1)**  
  作者: Yun-Jin Li, Mariia Gladkova, Yan Xia, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.19290v1.pdf)  
  摘要: Understanding dynamic 3D scenes is fundamental for various applications, including extended reality (XR) and autonomous driving. Effectively integrating semantic information into 3D reconstruction ena...  
  关键词: gaussian splatting, 3d reconstruction  
- **[AGS-Mesh: Adaptive Gaussian Splatting and Meshing with Geometric Priors for Indoor Room Reconstruction Using Smartphones](https://arxiv.org/abs/2411.19271v1)**  
  作者: Xuqian Ren, Matias Turkulainen, Jiepeng Wang, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.19271v1.pdf)  
  摘要: Geometric priors are often used to enhance 3D reconstruction. With many smartphones featuring low-resolution depth sensors and the prevalence of off-the-shelf monocular geometry estimators, incorporat...  
  关键词: gaussian splatting, 3d reconstruction  
- **[Unleashing the Power of Data Synthesis in Visual Localization](https://arxiv.org/abs/2412.00138v1)**  
  作者: Sihang Li, Siqi Tan, Bowen Chang, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2412.00138v1.pdf)  
  摘要: Visual localization, which estimates a camera's pose within a known scene, is a long-standing challenge in vision and robotics. Recent end-to-end methods that directly regress camera poses from query ...  
  关键词: 3d gaussian  
- **[InstanceGaussian: Appearance-Semantic Joint Gaussian Representation for 3D Instance-Level Perception](https://arxiv.org/abs/2411.19235v1)**  
  作者: Haijie Li, Yanmin Wu, Jiarui Meng, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.19235v1.pdf)  
  摘要: 3D scene understanding has become an essential area of research with applications in autonomous driving, robotics, and augmented reality. Recently, 3D Gaussian Splatting (3DGS) has emerged as a powerf...  
  关键词: gaussian splatting, 3d gaussian  
- **[Gaussians-to-Life: Text-Driven Animation of 3D Gaussian Splatting Scenes](https://arxiv.org/abs/2411.19233v1)**  
  作者: Thomas Wimmer, Michael Oechsle, Michael Niemeyer, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.19233v1.pdf)  
  摘要: State-of-the-art novel view synthesis methods achieve impressive results for multi-view captures of static 3D scenes. However, the reconstructed scenes still lack "liveliness," a key component for cre...  
  关键词: gaussian splatting  
- **[SuperGaussians: Enhancing Gaussian Splatting Using Primitives with Spatially Varying Colors](https://arxiv.org/abs/2411.18966v1)**  
  作者: Rui Xu, Wenyue Chen, Jiepeng Wang, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.18966v1.pdf)  
  摘要: Gaussian Splattings demonstrate impressive results in multi-view reconstruction based on Gaussian explicit representations. However, the current Gaussian primitives only have a single view-dependent c...  
  关键词: gaussian splatting  
- **[RIGI: Rectifying Image-to-3D Generation Inconsistency via Uncertainty-aware Learning](https://arxiv.org/abs/2411.18866v1)**  
  作者: Jiacheng Wang, Zhedong Zheng, Wei Xu, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.18866v1.pdf)  
  摘要: Given a single image of a target object, image-to-3D generation aims to reconstruct its texture and geometric shape. Recent methods often utilize intermediate media, such as multi-view images or video...  
  关键词: gaussian splatting, 3d gaussian, 3d reconstruction  
- **[Textured Gaussians for Enhanced 3D Scene Appearance Modeling](https://arxiv.org/abs/2411.18625v1)**  
  作者: Brian Chao, Hung-Yu Tseng, Lorenzo Porzi, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.18625v1.pdf)  
  摘要: 3D Gaussian Splatting (3DGS) has recently emerged as a state-of-the-art 3D reconstruction and rendering technique due to its high-quality results and fast training and rendering time. However, pixels ...  
  关键词: gaussian splatting, 3d gaussian, 3d reconstruction  
- **[CAT4D: Create Anything in 4D with Multi-View Video Diffusion Models](https://arxiv.org/abs/2411.18613v1)**  
  作者: Rundi Wu, Ruiqi Gao, Ben Poole, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.18613v1.pdf)  
  摘要: We present CAT4D, a method for creating 4D (dynamic 3D) scenes from monocular video. CAT4D leverages a multi-view video diffusion model trained on a diverse combination of datasets to enable novel vie...  
  关键词: 3d gaussian  
- **[GaussianSpeech: Audio-Driven Gaussian Avatars](https://arxiv.org/abs/2411.18675v1)**  
  作者: Shivangi Aneja, Artem Sevastopolsky, Tobias Kirschstein, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.18675v1.pdf)  
  摘要: We introduce GaussianSpeech, a novel approach that synthesizes high-fidelity animation sequences of photo-realistic, personalized 3D human head avatars from spoken audio. To capture the expressive, de...  
  关键词: gaussian splatting, 3d gaussian  
- **[PhyCAGE: Physically Plausible Compositional 3D Asset Generation from a Single Image](https://arxiv.org/abs/2411.18548v1)**  
  作者: Han Yan, Mingrui Zhang, Yang Li, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.18548v1.pdf)  
  摘要: We present PhyCAGE, the first approach for physically plausible compositional 3D asset generation from a single image. Given an input image, we first generate consistent multi-view images for componen...  
  关键词: gaussian splatting, 3d gaussian  
- **[Point Cloud Unsupervised Pre-training via 3D Gaussian Splatting](https://arxiv.org/abs/2411.18667v1)**  
  作者: Hao Liu, Minglin Chen, Yanni Ma, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.18667v1.pdf)  
  摘要: Pre-training on large-scale unlabeled datasets contribute to the model achieving powerful performance on 3D vision tasks, especially when annotations are limited. However, existing rendering-based sel...  
  关键词: gaussian splatting, 3d gaussian  
- **[HEMGS: A Hybrid Entropy Model for 3D Gaussian Splatting Data Compression](https://arxiv.org/abs/2411.18473v1)**  
  作者: Lei Liu, Zhenghao Chen, Dong Xu  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.18473v1.pdf)  
  摘要: Fast progress in 3D Gaussian Splatting (3DGS) has made 3D Gaussians popular for 3D modeling and image rendering, but this creates big challenges in data storage and transmission. To obtain a highly co...  
  关键词: gaussian splatting, 3d gaussian  
- **[Neural Surface Priors for Editable Gaussian Splatting](https://arxiv.org/abs/2411.18311v1)**  
  作者: Jakub Szymkowiak, Weronika Jakubowska, Dawid Malarz, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.18311v1.pdf) | [![Stars](https://img.shields.io/github/stars/WJakubowska/NeuralSurfacePriors?style=social)](https://github.com/WJakubowska/NeuralSurfacePriors)  
  摘要: In computer graphics, there is a need to recover easily modifiable representations of 3D geometry and appearance from image data. We introduce a novel method for this task using 3D Gaussian Splatting,...  
  关键词: gaussian splatting, 3d gaussian  
- **[Make-It-Animatable: An Efficient Framework for Authoring Animation-Ready 3D Characters](https://arxiv.org/abs/2411.18197v1)**  
  作者: Zhiyang Guo, Jinxu Xiang, Kai Ma, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.18197v1.pdf)  
  摘要: 3D characters are essential to modern creative industries, but making them animatable often demands extensive manual work in tasks like rigging and skinning. Existing automatic rigging tools face seve...  
  关键词: 3d gaussian  
- **[SmileSplat: Generalizable Gaussian Splats for Unconstrained Sparse Images](https://arxiv.org/abs/2411.18072v1)**  
  作者: Yanyan Li, Yixin Fang, Federico Tombari, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.18072v1.pdf)  
  摘要: Sparse Multi-view Images can be Learned to predict explicit radiance fields via Generalizable Gaussian Splatting approaches, which can achieve wider application prospects in real-life when ground-trut...  
  关键词: gaussian splatting  
- **[GLS: Geometry-aware 3D Language Gaussian Splatting](https://arxiv.org/abs/2411.18066v1)**  
  作者: Jiaxiong Qiu, Liu Liu, Zhizhong Su, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.18066v1.pdf) | [![Stars](https://img.shields.io/github/stars/JiaxiongQ/GLS?style=social)](https://github.com/JiaxiongQ/GLS)  
  摘要: Recently, 3D Gaussian Splatting (3DGS) has achieved significant performance on indoor surface reconstruction and open-vocabulary segmentation. This paper presents GLS, a unified framework of surface r...  
  关键词: gaussian splatting, 3d gaussian  
- **[HI-SLAM2: Geometry-Aware Gaussian SLAM for Fast Monocular Scene Reconstruction](https://arxiv.org/abs/2411.17982v1)**  
  作者: Wei Zhang, Qing Cheng, David Skuddis, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.17982v1.pdf)  
  摘要: We present HI-SLAM2, a geometry-aware Gaussian SLAM system that achieves fast and accurate monocular scene reconstruction using only RGB input. Existing Neural SLAM or 3DGS-based SLAM methods often tr...  
  关键词: gaussian splatting, 3d gaussian  
- **[DROID-Splat: Combining end-to-end SLAM with 3D Gaussian Splatting](https://arxiv.org/abs/2411.17660v2)**  
  作者: Christian Homeyer, Leon Begiristain, Christoph Schnörr  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.17660v2.pdf) | [![Stars](https://img.shields.io/github/stars/ChenHoy/DROID-Splat?style=social)](https://github.com/ChenHoy/DROID-Splat)  
  摘要: Recent progress in scene synthesis makes standalone SLAM systems purely based on optimizing hyperprimitives with a Rendering objective possible. However, the tracking performance still lacks behind tr...  
  关键词: gaussian splatting, 3d gaussian  
- **[Distractor-free Generalizable 3D Gaussian Splatting](https://arxiv.org/abs/2411.17605v1)**  
  作者: Yanqi Bao, Jing Liao, Jing Huo, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.17605v1.pdf) | [![Stars](https://img.shields.io/github/stars/bbbbby-99/DGGS?style=social)](https://github.com/bbbbby-99/DGGS)  
  摘要: We present DGGS, a novel framework addressing the previously unexplored challenge of Distractor-free Generalizable 3D Gaussian Splatting (3DGS). It accomplishes two key objectives: fortifying generali...  
  关键词: gaussian splatting, 3d gaussian  
- **[DRiVE: Diffusion-based Rigging Empowers Generation of Versatile and Expressive Characters](https://arxiv.org/abs/2411.17423v1)**  
  作者: Mingze Sun, Junhao Chen, Junting Dong, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.17423v1.pdf)  
  摘要: Recent advances in generative models have enabled high-quality 3D character reconstruction from multi-modal. However, animating these generated characters remains a challenging task, especially for co...  
  关键词: 3d gaussian  
- **[SelfSplat: Pose-Free and 3D Prior-Free Generalizable 3D Gaussian Splatting](https://arxiv.org/abs/2411.17190v3)**  
  作者: Gyeongjin Kang, Jisang Yoo, Jihyeon Park, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.17190v3.pdf)  
  摘要: We propose SelfSplat, a novel 3D Gaussian Splatting model designed to perform pose-free and 3D prior-free generalizable 3D reconstruction from unposed multi-view images. These settings are inherently ...  
  关键词: gaussian splatting, 3d gaussian, 3d reconstruction  
- **[PhysMotion: Physics-Grounded Dynamics From a Single Image](https://arxiv.org/abs/2411.17189v2)**  
  作者: Xiyang Tan, Ying Jiang, Xuan Li, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.17189v2.pdf)  
  摘要: We introduce PhysMotion, a novel framework that leverages principled physics-based simulations to guide intermediate 3D representations generated from a single image and input conditions (e.g., applie...  
  关键词: 3d gaussian  
- **[4D Scaffold Gaussian Splatting for Memory Efficient Dynamic Scene Reconstruction](https://arxiv.org/abs/2411.17044v1)**  
  作者: Woong Oh Cho, In Cho, Seoha Kim, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.17044v1.pdf)  
  摘要: Existing 4D Gaussian methods for dynamic scene reconstruction offer high visual fidelity and fast rendering. However, these methods suffer from excessive memory and storage demands, which limits their...  
- **[G2SDF: Surface Reconstruction from Explicit Gaussians with Implicit SDFs](https://arxiv.org/abs/2411.16898v1)**  
  作者: Kunyi Li, Michael Niemeyer, Zeyu Chen, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.16898v1.pdf)  
  摘要: State-of-the-art novel view synthesis methods such as 3D Gaussian Splatting (3DGS) achieve remarkable visual quality. While 3DGS and its variants can be rendered efficiently using rasterization, many ...  
  关键词: gaussian splatting, 3d gaussian  
- **[PreF3R: Pose-Free Feed-Forward 3D Gaussian Splatting from Variable-length Image Sequence](https://arxiv.org/abs/2411.16877v1)**  
  作者: Zequn Chen, Jiezhi Yang, Heng Yang  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.16877v1.pdf)  
  摘要: We present PreF3R, Pose-Free Feed-forward 3D Reconstruction from an image sequence of variable length. Unlike previous approaches, PreF3R removes the need for camera calibration and reconstructs the 3...  
  关键词: 3d gaussian, 3d reconstruction  
- **[SplatAD: Real-Time Lidar and Camera Rendering with 3D Gaussian Splatting for Autonomous Driving](https://arxiv.org/abs/2411.16816v2)**  
  作者: Georg Hess, Carl Lindström, Maryam Fatemi, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.16816v2.pdf)  
  摘要: Ensuring the safety of autonomous robots, such as self-driving vehicles, requires extensive testing across diverse driving scenarios. Simulation is a key ingredient for conducting such testing in a co...  
  关键词: gaussian splatting, 3d gaussian, neural rendering, real-time rendering, nerf  
- **[SplatFlow: Multi-View Rectified Flow Model for 3D Gaussian Splatting Synthesis](https://arxiv.org/abs/2411.16443v1)**  
  作者: Hyojun Go, Byeongjun Park, Jiho Jang, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.16443v1.pdf)  
  摘要: Text-based generation and editing of 3D scenes hold significant potential for streamlining content creation through intuitive user interactions. While recent advances leverage 3D Gaussian Splatting (3...  
  关键词: gaussian splatting, 3d gaussian, real-time rendering  
- **[Quadratic Gaussian Splatting for Efficient and Detailed Surface Reconstruction](https://arxiv.org/abs/2411.16392v1)**  
  作者: Ziyu Zhang, Binbin Huang, Hanqing Jiang, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.16392v1.pdf)  
  摘要: Recently, 3D Gaussian Splatting (3DGS) has attracted attention for its superior rendering quality and speed over Neural Radiance Fields (NeRF). To address 3DGS's limitations in surface representation,...  
  关键词: gaussian splatting, 3d gaussian, nerf  
- **[MAGiC-SLAM: Multi-Agent Gaussian Globally Consistent SLAM](https://arxiv.org/abs/2411.16785v1)**  
  作者: Vladimir Yugay, Theo Gevers, Martin R. Oswald  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.16785v1.pdf)  
  摘要: Simultaneous localization and mapping (SLAM) systems with novel view synthesis capabilities are widely used in computer vision, with applications in augmented reality, robotics, and autonomous driving...  
  关键词: 3d gaussian  
- **[Event-boosted Deformable 3D Gaussians for Fast Dynamic Scene Reconstruction](https://arxiv.org/abs/2411.16180v1)**  
  作者: Wenhao Xu, Wenming Weng, Yueyi Zhang, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.16180v1.pdf)  
  摘要: 3D Gaussian Splatting (3D-GS) enables real-time rendering but struggles with fast motion due to low temporal resolution of RGB cameras. To address this, we introduce the first approach combining event...  
  关键词: gaussian splatting, 3d gaussian, real-time rendering, 3d reconstruction  
- **[NovelGS: Consistent Novel-view Denoising via Large Gaussian Reconstruction Model](https://arxiv.org/abs/2411.16779v1)**  
  作者: Jinpeng Liu, Jiale Xu, Weihao Cheng, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.16779v1.pdf)  
  摘要: We introduce NovelGS, a diffusion model for Gaussian Splatting (GS) given sparse-view images. Recent works leverage feed-forward networks to generate pixel-aligned Gaussians, which could be fast rende...  
  关键词: gaussian splatting, 3d gaussian  
- **[GAST: Sequential Gaussian Avatars with Hierarchical Spatio-temporal Context](https://arxiv.org/abs/2411.16768v1)**  
  作者: Wangze Xu, Yifan Zhan, Zhihang Zhong, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.16768v1.pdf)  
  摘要: 3D human avatars, through the use of canonical radiance fields and per-frame observed warping, enable high-fidelity rendering and animating. However, existing methods, which rely on either spatial SMP...  
  关键词: 3d gaussian  
- **[UnitedVLN: Generalizable Gaussian Splatting for Continuous Vision-Language Navigation](https://arxiv.org/abs/2411.16053v1)**  
  作者: Guangzhao Dai, Jian Zhao, Yuantao Chen, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.16053v1.pdf)  
  摘要: Vision-and-Language Navigation (VLN), where an agent follows instructions to reach a target destination, has recently seen significant advancements. In contrast to navigation in discrete environments ...  
- **[PG-SLAM: Photo-realistic and Geometry-aware RGB-D SLAM in Dynamic Environments](https://arxiv.org/abs/2411.15800v1)**  
  作者: Haoang Li, Xiangqi Meng, Xingxing Zuo, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.15800v1.pdf)  
  摘要: Simultaneous localization and mapping (SLAM) has achieved impressive performance in static environments. However, SLAM in dynamic environments remains an open question. Many methods directly filter ou...  
  关键词: gaussian splatting, 3d gaussian  
- **[ZeroGS: Training 3D Gaussian Splatting from Unposed Images](https://arxiv.org/abs/2411.15779v1)**  
  作者: Yu Chen, Rolandos Alexandros Potamias, Evangelos Ververas, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.15779v1.pdf)  
  摘要: Neural radiance fields (NeRF) and 3D Gaussian Splatting (3DGS) are popular techniques to reconstruct and render photo-realistic images. However, the pre-requisite of running Structure-from-Motion (SfM...  
  关键词: gaussian splatting, 3d gaussian, nerf  
- **[Bundle Adjusted Gaussian Avatars Deblurring](https://arxiv.org/abs/2411.16758v1)**  
  作者: Muyao Niu, Yifan Zhan, Qingtian Zhu, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.16758v1.pdf)  
  摘要: The development of 3D human avatars from multi-view videos represents a significant yet challenging task in the field. Recent advancements, including 3D Gaussian Splattings (3DGS), have markedly progr...  
  关键词: gaussian splatting, 3d gaussian  
- **[DynamicAvatars: Accurate Dynamic Facial Avatars Reconstruction and Precise Editing with Diffusion Models](https://arxiv.org/abs/2411.15732v1)**  
  作者: Yangyang Qian, Yuan Sun, Yu Guo  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.15732v1.pdf)  
  摘要: Generating and editing dynamic 3D head avatars are crucial tasks in virtual reality and film production. However, existing methods often suffer from facial distortions, inaccurate head movements, and ...  
  关键词: gaussian splatting  
- **[GSurf: 3D Reconstruction via Signed Distance Fields with Direct Gaussian Supervision](https://arxiv.org/abs/2411.15723v2)**  
  作者: Baixin Xu, Jiangbei Hu, Jiaze Li, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.15723v2.pdf)  
  摘要: Surface reconstruction from multi-view images is a core challenge in 3D vision. Recent studies have explored signed distance fields (SDF) within Neural Radiance Fields (NeRF) to achieve high-fidelity ...  
  关键词: gaussian splatting, 3d gaussian, 3d reconstruction, nerf  
- **[EMD: Explicit Motion Modeling for High-Quality Street Gaussian Splatting](https://arxiv.org/abs/2411.15582v1)**  
  作者: Xiaobao Wei, Qingpo Wuwu, Zhongyu Zhao, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.15582v1.pdf)  
  摘要: Photorealistic reconstruction of street scenes is essential for developing real-world simulators in autonomous driving. While recent methods based on 3D/4D Gaussian Splatting (GS) have demonstrated pr...  
  关键词: gaussian splatting  
- **[SplatFlow: Self-Supervised Dynamic Gaussian Splatting in Neural Motion Flow Field for Autonomous Driving](https://arxiv.org/abs/2411.15482v1)**  
  作者: Su Sun, Cheng Zhao, Zhuoyang Sun, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.15482v1.pdf)  
  摘要: Most existing Dynamic Gaussian Splatting methods for complex dynamic urban scenarios rely on accurate object-level supervision from expensive manual labeling, limiting their scalability in real-world ...  
  关键词: gaussian splatting  
- **[Gassidy: Gaussian Splatting SLAM in Dynamic Environments](https://arxiv.org/abs/2411.15476v1)**  
  作者: Long Wen, Shixin Li, Yu Zhang, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.15476v1.pdf)  
  摘要: 3D Gaussian Splatting (3DGS) allows flexible adjustments to scene representation, enabling continuous optimization of scene quality during dense visual simultaneous localization and mapping (SLAM) in ...  
  关键词: gaussian splatting, 3d gaussian  
- **[SplatSDF: Boosting Neural Implicit SDF via Gaussian Splatting Fusion](https://arxiv.org/abs/2411.15468v1)**  
  作者: Runfa Blark Li, Keito Suzuki, Bang Du, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.15468v1.pdf)  
  摘要: A signed distance function (SDF) is a useful representation for continuous-space geometry and many related operations, including rendering, collision checking, and mesh generation. Hence, reconstructi...  
  关键词: gaussian splatting, 3d gaussian, nerf  
- **[UniGaussian: Driving Scene Reconstruction from Multiple Camera Models via Unified Gaussian Representations](https://arxiv.org/abs/2411.15355v1)**  
  作者: Yuan Ren, Guile Wu, Runhao Li, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.15355v1.pdf)  
  摘要: Urban scene reconstruction is crucial for real-world autonomous driving simulators. Although existing methods have achieved photorealistic reconstruction, they mostly focus on pinhole cameras and negl...  
  关键词: gaussian splatting, 3d gaussian, real-time rendering  
- **[Neural 4D Evolution under Large Topological Changes from 2D Images](https://arxiv.org/abs/2411.15018v1)**  
  作者: AmirHossein Naghi Razlighi, Tiago Novello, Asen Nachkov, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.15018v1.pdf) | [![Stars](https://img.shields.io/github/stars/insait-institute/N4DE?style=social)](https://github.com/insait-institute/N4DE)  
  摘要: In the literature, it has been shown that the evolution of the known explicit 3D surface to the target one can be learned from 2D images using the instantaneous flow field, where the known and target ...  
  关键词: gaussian splatting  
- **[3D Convex Splatting: Radiance Field Rendering with 3D Smooth Convexes](https://arxiv.org/abs/2411.14974v2)**  
  作者: Jan Held, Renaud Vandeghen, Abdullah Hamdi, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.14974v2.pdf)  
  摘要: Recent advances in radiance field reconstruction, such as 3D Gaussian Splatting (3DGS), have achieved high-quality novel view synthesis and fast rendering by representing scenes with compositions of G...  
  关键词: gaussian splatting, 3d gaussian, nerf  
- **[Dynamics-Aware Gaussian Splatting Streaming Towards Fast On-the-Fly Training for 4D Reconstruction](https://arxiv.org/abs/2411.14847v1)**  
  作者: Zhening Liu, Yingdong Hu, Xinjie Zhang, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.14847v1.pdf)  
  摘要: The recent development of 3D Gaussian Splatting (3DGS) has led to great interest in 4D dynamic spatial reconstruction from multi-view visual inputs. While existing approaches mainly rely on processing...  
  关键词: gaussian splatting, 3d gaussian, real-time rendering  
- **[VisionPAD: A Vision-Centric Pre-training Paradigm for Autonomous Driving](https://arxiv.org/abs/2411.14716v1)**  
  作者: Haiming Zhang, Wending Zhou, Yiyao Zhu, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.14716v1.pdf)  
  摘要: This paper introduces VisionPAD, a novel self-supervised pre-training paradigm designed for vision-centric algorithms in autonomous driving. In contrast to previous approaches that employ neural rende...  
  关键词: gaussian splatting, 3d gaussian, neural rendering  
- **[Unleashing the Potential of Multi-modal Foundation Models and Video Diffusion for 4D Dynamic Physical Scene Simulation](https://arxiv.org/abs/2411.14423v1)**  
  作者: Zhuoman Liu, Weicai Ye, Yan Luximon, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.14423v1.pdf)  
  摘要: Realistic simulation of dynamic scenes requires accurately capturing diverse material properties and modeling complex object interactions grounded in physical principles. However, existing methods are...  
  关键词: 3d gaussian  
- **[Baking Gaussian Splatting into Diffusion Denoiser for Fast and Scalable Single-stage Image-to-3D Generation](https://arxiv.org/abs/2411.14384v2)**  
  作者: Yuanhao Cai, He Zhang, Kai Zhang, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.14384v2.pdf)  
  摘要: Existing feed-forward image-to-3D methods mainly rely on 2D multi-view diffusion models that cannot guarantee 3D consistency. These methods easily collapse when changing the prompt view direction and ...  
  关键词: 3d gaussian  
- **[SplatR : Experience Goal Visual Rearrangement with 3D Gaussian Splatting and Dense Feature Matching](https://arxiv.org/abs/2411.14322v1)**  
  作者: Arjun P S, Andrew Melnik, Gora Chand Nandi  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.14322v1.pdf)  
  摘要: Experience Goal Visual Rearrangement task stands as a foundational challenge within Embodied AI, requiring an agent to construct a robust world model that accurately captures the goal state. The agent...  
  关键词: gaussian splatting, 3d gaussian  
- **[NexusSplats: Efficient 3D Gaussian Splatting in the Wild](https://arxiv.org/abs/2411.14514v4)**  
  作者: Yuzhou Tang, Dejun Xu, Yongjie Hou, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.14514v4.pdf)  
  摘要: While 3D Gaussian Splatting (3DGS) has recently demonstrated remarkable rendering quality and efficiency in 3D scene reconstruction, it struggles with varying lighting conditions and incidental occlus...  
  关键词: gaussian splatting, 3d gaussian  
- **[FAST-Splat: Fast, Ambiguity-Free Semantics Transfer in Gaussian Splatting](https://arxiv.org/abs/2411.13753v1)**  
  作者: Ola Shorinwa, Jiankai Sun, Mac Schwager  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.13753v1.pdf)  
  摘要: We present FAST-Splat for fast, ambiguity-free semantic Gaussian Splatting, which seeks to address the main limitations of existing semantic Gaussian Splatting methods, namely: slow training and rende...  
  关键词: gaussian splatting  
- **[Generating 3D-Consistent Videos from Unposed Internet Photos](https://arxiv.org/abs/2411.13549v1)**  
  作者: Gene Chou, Kai Zhang, Sai Bi, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.13549v1.pdf)  
  摘要: We address the problem of generating videos from unposed internet photos. A handful of input images serve as keyframes, and our model interpolates between them to simulate a path moving between the ca...  
  关键词: gaussian splatting, 3d gaussian  
- **[GazeGaussian: High-Fidelity Gaze Redirection with 3D Gaussian Splatting](https://arxiv.org/abs/2411.12981v1)**  
  作者: Xiaobao Wei, Peng Chen, Guangyu Li, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.12981v1.pdf)  
  摘要: Gaze estimation encounters generalization challenges when dealing with out-of-distribution data. To address this problem, recent methods use neural radiance fields (NeRF) to generate augmented data. H...  
  关键词: gaussian splatting, 3d gaussian, nerf  
- **[Video2BEV: Transforming Drone Videos to BEVs for Video-based Geo-localization](https://arxiv.org/abs/2411.13610v1)**  
  作者: Hao Ju, Zhedong Zheng  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.13610v1.pdf)  
  摘要: Existing approaches to drone visual geo-localization predominantly adopt the image-based setting, where a single drone-view snapshot is matched with images from other platforms. Such task formulation,...  
  关键词: gaussian splatting  
- **[PR-ENDO: Physically Based Relightable Gaussian Splatting for Endoscopy](https://arxiv.org/abs/2411.12510v1)**  
  作者: Joanna Kaleta, Weronika Smolak-Dyżewska, Dawid Malarz, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.12510v1.pdf)  
  摘要: Endoscopic procedures are crucial for colorectal cancer diagnosis, and three-dimensional reconstruction of the environment for real-time novel-view synthesis can significantly enhance diagnosis. We pr...  
  关键词: gaussian splatting, 3d gaussian  
- **[SCIGS: 3D Gaussians Splatting from a Snapshot Compressive Image](https://arxiv.org/abs/2411.12471v2)**  
  作者: Zixu Wang, Hao Yang, Yu Guo, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.12471v2.pdf)  
  摘要: Snapshot Compressive Imaging (SCI) offers a possibility for capturing information in high-speed dynamic scenes, requiring efficient reconstruction method to recover scene information. Despite promisin...  
  关键词: nerf  
- **[Automated 3D Physical Simulation of Open-world Scene with Gaussian Splatting](https://arxiv.org/abs/2411.12789v1)**  
  作者: Haoyu Zhao, Hao Wang, Xingyue Zhao, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.12789v1.pdf)  
  摘要: Recent advancements in 3D generation models have opened new possibilities for simulating dynamic 3D object movements and customizing behaviors, yet creating this content remains challenging. Current m...  
- **[GaussianPretrain: A Simple Unified 3D Gaussian Representation for Visual Pre-training in Autonomous Driving](https://arxiv.org/abs/2411.12452v1)**  
  作者: Shaoqing Xu, Fang Li, Shengyin Jiang, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.12452v1.pdf) | [![Stars](https://img.shields.io/github/stars/Public-BOTs/GaussianPretrain?style=social)](https://github.com/Public-BOTs/GaussianPretrain)  
  摘要: Self-supervised learning has made substantial strides in image processing, while visual pre-training for autonomous driving is still in its infancy. Existing methods often focus on learning geometric ...  
  关键词: 3d gaussian, nerf  
- **[Gradient-Weighted Feature Back-Projection: A Fast Alternative to Feature Distillation in 3D Gaussian Splatting](https://arxiv.org/abs/2411.15193v1)**  
  作者: Joji Joseph, Bharadwaj Amrutur, Shalabh Bhatnagar  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.15193v1.pdf)  
  摘要: We introduce a training-free method for feature field rendering in Gaussian splatting. Our approach back-projects 2D features into pre-trained 3D Gaussians, using a weighted sum based on each Gaussian...  
  关键词: gaussian splatting, 3d gaussian  
- **[Beyond Gaussians: Fast and High-Fidelity 3D Splatting with Linear Kernels](https://arxiv.org/abs/2411.12440v3)**  
  作者: Haodong Chen, Runnan Chen, Qiang Qu, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.12440v3.pdf)  
  摘要: Recent advancements in 3D Gaussian Splatting (3DGS) have substantially improved novel view synthesis, enabling high-quality reconstruction and real-time rendering. However, blurring artifacts, such as...  
  关键词: gaussian splatting, 3d gaussian, real-time rendering  
- **[Mini-Splatting2: Building 360 Scenes within Minutes via Aggressive Gaussian Densification](https://arxiv.org/abs/2411.12788v1)**  
  作者: Guangchi Fang, Bing Wang  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.12788v1.pdf)  
  摘要: In this study, we explore the essential challenge of fast scene optimization for Gaussian Splatting. Through a thorough analysis of the geometry modeling process, we reveal that dense point clouds can...  
  关键词: gaussian splatting  
- **[LiV-GS: LiDAR-Vision Integration for 3D Gaussian Splatting SLAM in Outdoor Environments](https://arxiv.org/abs/2411.12185v1)**  
  作者: Renxiang Xiao, Wei Liu, Yushuai Chen, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.12185v1.pdf)  
  摘要: We present LiV-GS, a LiDAR-visual SLAM system in outdoor environments that leverages 3D Gaussian as a differentiable spatial representation. Notably, LiV-GS is the first method that directly aligns di...  
  关键词: 3d gaussian  
- **[Sketch-guided Cage-based 3D Gaussian Splatting Deformation](https://arxiv.org/abs/2411.12168v2)**  
  作者: Tianhao Xie, Noam Aigerman, Eugene Belilovsky, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.12168v2.pdf)  
  摘要: 3D Gaussian Splatting (GS) is one of the most promising novel 3D representations that has received great interest in computer graphics and computer vision. While various systems have introduced editin...  
  关键词: gaussian splatting, 3d gaussian  
- **[FruitNinja: 3D Object Interior Texture Generation with Gaussian Splatting](https://arxiv.org/abs/2411.12089v2)**  
  作者: Fangyu Wu, Yuhao Chen  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.12089v2.pdf)  
  摘要: In the real world, objects reveal internal textures when sliced or cut, yet this behavior is not well-studied in 3D generation tasks today. For example, slicing a virtual 3D watermelon should reveal f...  
  关键词: gaussian splatting, 3d gaussian  
- **[RoboGSim: A Real2Sim2Real Robotic Gaussian Splatting Simulator](https://arxiv.org/abs/2411.11839v1)**  
  作者: Xinhai Li, Jialin Li, Ziheng Zhang, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.11839v1.pdf)  
  摘要: Efficient acquisition of real-world embodied data has been increasingly critical. However, large-scale demonstrations captured by remote operation tend to take extremely high costs and fail to scale u...  
  关键词: gaussian splatting, 3d gaussian  
- **[TimeFormer: Capturing Temporal Relationships of Deformable 3D Gaussians for Robust Reconstruction](https://arxiv.org/abs/2411.11941v1)**  
  作者: DaDong Jiang, Zhihui Ke, Xiaobo Zhou, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.11941v1.pdf)  
  摘要: Dynamic scene reconstruction is a long-term challenge in 3D vision. Recent methods extend 3D Gaussian Splatting to dynamic scenes via additional deformation fields and apply explicit constraints like ...  
  关键词: gaussian splatting, 3d gaussian  
- **[GPS-Gaussian+: Generalizable Pixel-wise 3D Gaussian Splatting for Real-Time Human-Scene Rendering from Sparse Views](https://arxiv.org/abs/2411.11363v1)**  
  作者: Boyao Zhou, Shunyuan Zheng, Hanzhang Tu, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.11363v1.pdf)  
  摘要: Differentiable rendering techniques have recently shown promising results for free-viewpoint video synthesis of characters. However, such methods, either Gaussian Splatting or neural implicit renderin...  
  关键词: gaussian splatting, real-time rendering  
- **[DeSiRe-GS: 4D Street Gaussians for Static-Dynamic Decomposition and Surface Reconstruction for Urban Driving Scenes](https://arxiv.org/abs/2411.11921v1)**  
  作者: Chensheng Peng, Chengwei Zhang, Yixiao Wang, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.11921v1.pdf) | [![Stars](https://img.shields.io/github/stars/chengweialan/DeSiRe-GS?style=social)](https://github.com/chengweialan/DeSiRe-GS)  
  摘要: We present DeSiRe-GS, a self-supervised gaussian splatting representation, enabling effective static-dynamic decomposition and high-fidelity surface reconstruction in complex driving scenarios. Our ap...  
  关键词: gaussian splatting, 3d gaussian  
- **[VeGaS: Video Gaussian Splatting](https://arxiv.org/abs/2411.11024v1)**  
  作者: Weronika Smolak-Dyżewska, Dawid Malarz, Kornel Howil, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.11024v1.pdf) | [![Stars](https://img.shields.io/github/stars/gmum/VeGaS?style=social)](https://github.com/gmum/VeGaS)  
  摘要: Implicit Neural Representations (INRs) employ neural networks to approximate discrete data as continuous functions. In the context of video data, such models can be utilized to transform the coordinat...  
  关键词: gaussian splatting, 3d gaussian  
- **[Direct and Explicit 3D Generation from a Single Image](https://arxiv.org/abs/2411.10947v1)**  
  作者: Haoyu Wu, Meher Gitika Karumuri, Chuhang Zou, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.10947v1.pdf)  
  摘要: Current image-to-3D approaches suffer from high computational costs and lack scalability for high-resolution outputs. In contrast, we introduce a novel framework to directly generate explicit surface ...  
  关键词: gaussian splatting, 3d gaussian  
- **[DGS-SLAM: Gaussian Splatting SLAM in Dynamic Environment](https://arxiv.org/abs/2411.10722v1)**  
  作者: Mangyu Kong, Jaewon Lee, Seongwon Lee, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.10722v1.pdf)  
  摘要: We introduce Dynamic Gaussian Splatting SLAM (DGS-SLAM), the first dynamic SLAM framework built on the foundation of Gaussian Splatting. While recent advancements in dense SLAM have leveraged Gaussian...  
  关键词: gaussian splatting, 3d gaussian  
- **[SPARS3R: Semantic Prior Alignment and Regularization for Sparse 3D Reconstruction](https://arxiv.org/abs/2411.12592v1)**  
  作者: Yutao Tang, Yuxiang Guo, Deming Li, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.12592v1.pdf)  
  摘要: Recent efforts in Gaussian-Splat-based Novel View Synthesis can achieve photorealistic rendering; however, such capability is limited in sparse-view scenarios due to sparse initialization and over-fit...  
- **[The Oxford Spires Dataset: Benchmarking Large-Scale LiDAR-Visual Localisation, Reconstruction and Radiance Field Methods](https://arxiv.org/abs/2411.10546v1)**  
  作者: Yifu Tao, Miguel Ángel Muñoz-Bañón, Lintong Zhang, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.10546v1.pdf)  
  摘要: This paper introduces a large-scale multi-modal dataset captured in and around well-known landmarks in Oxford using a custom-built multi-sensor perception unit as well as a millimetre-accurate map fro...  
  关键词: gaussian splatting, 3d gaussian, 3d reconstruction, nerf  
- **[USP-Gaussian: Unifying Spike-based Image Reconstruction, Pose Correction and Gaussian Splatting](https://arxiv.org/abs/2411.10504v1)**  
  作者: Kang Chen, Jiyuan Zhang, Zecheng Hao, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.10504v1.pdf) | [![Stars](https://img.shields.io/github/stars/chenkang455/USP-Gaussian?style=social)](https://github.com/chenkang455/USP-Gaussian)  
  摘要: Spike cameras, as an innovative neuromorphic camera that captures scenes with the 0-1 bit stream at 40 kHz, are increasingly employed for the 3D reconstruction task via Neural Radiance Fields (NeRF) o...  
  关键词: gaussian splatting, 3d gaussian, 3d reconstruction, nerf  
- **[Efficient Density Control for 3D Gaussian Splatting](https://arxiv.org/abs/2411.10133v1)**  
  作者: Xiaobin Deng, Changyu Diao, Min Li, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.10133v1.pdf)  
  摘要: 3D Gaussian Splatting (3DGS) excels in novel view synthesis, balancing advanced rendering quality with real-time performance. However, in trained scenes, a large number of Gaussians with low opacity s...  
  关键词: gaussian splatting, 3d gaussian  
- **[GSEditPro: 3D Gaussian Splatting Editing with Attention-based Progressive Localization](https://arxiv.org/abs/2411.10033v1)**  
  作者: Yanhao Sun, RunZe Tian, Xiao Han, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.10033v1.pdf)  
  摘要: With the emergence of large-scale Text-to-Image(T2I) models and implicit 3D representations like Neural Radiance Fields (NeRF), many text-driven generative editing methods based on NeRF have appeared....  
  关键词: gaussian splatting, 3d gaussian, real-time rendering, nerf  
- **[GGAvatar: Reconstructing Garment-Separated 3D Gaussian Splatting Avatars from Monocular Video](https://arxiv.org/abs/2411.09952v1)**  
  作者: Jingxuan Chen  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.09952v1.pdf) | [![Stars](https://img.shields.io/github/stars/J-X-Chen/GGAvatar?style=social)](https://github.com/J-X-Chen/GGAvatar/)  
  摘要: Avatar modelling has broad applications in human animation and virtual try-ons. Recent advancements in this field have focused on high-quality and comprehensive human reconstruction but often overlook...  
  关键词: gaussian splatting, 3d gaussian  
- **[Adversarial Attacks Using Differentiable Rendering: A Survey](https://arxiv.org/abs/2411.09749v1)**  
  作者: Matthew Hull, Chao Zhang, Zsolt Kira, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.09749v1.pdf)  
  摘要: Differentiable rendering methods have emerged as a promising means for generating photo-realistic and physically plausible adversarial attacks by manipulating 3D objects and scenes that can deceive de...  
  关键词: gaussian splatting, 3d gaussian  
- **[DyGASR: Dynamic Generalized Exponential Splatting with Surface Alignment for Accelerated 3D Mesh Reconstruction](https://arxiv.org/abs/2411.09156v2)**  
  作者: Shengchao Zhao, Yundong Li  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.09156v2.pdf)  
  摘要: Recent advancements in 3D Gaussian Splatting (3DGS), which lead to high-quality novel view synthesis and accelerated rendering, have remarkably improved the quality of radiance field reconstruction. H...  
  关键词: gaussian splatting, 3d gaussian  
- **[4D Gaussian Splatting in the Wild with Uncertainty-Aware Regularization](https://arxiv.org/abs/2411.08879v1)**  
  作者: Mijeong Kim, Jongwoo Lim, Bohyung Han  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.08879v1.pdf)  
  摘要: Novel view synthesis of dynamic scenes is becoming important in various applications, including augmented and virtual reality. We propose a novel 4D Gaussian Splatting (4DGS) algorithm for dynamic sce...  
  关键词: gaussian splatting  
- **[Towards More Accurate Fake Detection on Images Generated from Advanced Generative and Neural Rendering Models](https://arxiv.org/abs/2411.08642v1)**  
  作者: Chengdong Dong, Vijayakumar Bhagavatula, Zhenyu Zhou, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.08642v1.pdf)  
  摘要: The remarkable progress in neural-network-driven visual data generation, especially with neural rendering techniques like Neural Radiance Fields and 3D Gaussian splatting, offers a powerful alternativ...  
  关键词: gaussian splatting, 3d gaussian, neural rendering  
- **[BillBoard Splatting (BBSplat): Learnable Textured Primitives for Novel View Synthesis](https://arxiv.org/abs/2411.08508v2)**  
  作者: David Svitov, Pietro Morerio, Lourdes Agapito, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.08508v2.pdf)  
  摘要: We present billboard Splatting (BBSplat) - a novel approach for 3D scene representation based on textured geometric primitives. BBSplat represents the scene as a set of optimizable textured planar pri...  
  关键词: gaussian splatting, nerf  
- **[Biomass phenotyping of oilseed rape through UAV multi-view oblique imaging with 3DGS and SAM model](https://arxiv.org/abs/2411.08453v1)**  
  作者: Yutao Shen, Hongyu Zhou, Xin Yang, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.08453v1.pdf)  
  摘要: Biomass estimation of oilseed rape is crucial for optimizing crop productivity and breeding strategies. While UAV-based imaging has advanced high-throughput phenotyping, current methods often rely on ...  
  关键词: gaussian splatting, 3d gaussian, 3d reconstruction, nerf  
- **[DG-SLAM: Robust Dynamic Gaussian Splatting SLAM with Hybrid Pose Optimization](https://arxiv.org/abs/2411.08373v1)**  
  作者: Yueming Xu, Haochen Jiang, Zhongyang Xiao, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.08373v1.pdf)  
  摘要: Achieving robust and precise pose estimation in dynamic scenes is a significant research challenge in Visual Simultaneous Localization and Mapping (SLAM). Recent advancements integrating Gaussian Spla...  
  关键词: gaussian splatting, 3d gaussian, real-time rendering  
- **[MBA-SLAM: Motion Blur Aware Dense Visual SLAM with Radiance Fields Representation](https://arxiv.org/abs/2411.08279v1)**  
  作者: Peng Wang, Lingzhe Zhao, Yin Zhang, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.08279v1.pdf) | [![Stars](https://img.shields.io/github/stars/WU-CVGL/MBA-SLAM?style=social)](https://github.com/WU-CVGL/MBA-SLAM)  
  摘要: Emerging 3D scene representations, such as Neural Radiance Fields (NeRF) and 3D Gaussian Splatting (3DGS), have demonstrated their effectiveness in Simultaneous Localization and Mapping (SLAM) for pho...  
  关键词: gaussian splatting, 3d gaussian, nerf  
- **[Projecting Gaussian Ellipsoids While Avoiding Affine Projection Approximation](https://arxiv.org/abs/2411.07579v3)**  
  作者: Han Qi, Tao Cai, Xiyue Han  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.07579v3.pdf)  
  摘要: Recently, 3D Gaussian Splatting has dominated novel-view synthesis with its real-time rendering speed and state-of-the-art rendering quality. However, during the rendering process, the use of the Jaco...  
  关键词: gaussian splatting, 3d gaussian, real-time rendering  
- **[GaussianCut: Interactive segmentation via graph cut for 3D Gaussian Splatting](https://arxiv.org/abs/2411.07555v1)**  
  作者: Umangi Jain, Ashkan Mirzaei, Igor Gilitschenski  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.07555v1.pdf)  
  摘要: We introduce GaussianCut, a new method for interactive multiview segmentation of scenes represented as 3D Gaussians. Our approach allows for selecting the objects to be segmented by interacting with a...  
  关键词: gaussian splatting, 3d gaussian  
- **[HiCoM: Hierarchical Coherent Motion for Streamable Dynamic Scene with 3D Gaussian Splatting](https://arxiv.org/abs/2411.07541v1)**  
  作者: Qiankun Gao, Jiarui Meng, Chengxiang Wen, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.07541v1.pdf)  
  摘要: The online reconstruction of dynamic scenes from multi-view streaming videos faces significant challenges in training, rendering and storage efficiency. Harnessing superior learning speed and real-tim...  
  关键词: gaussian splatting, 3d gaussian, real-time rendering  
- **[GUS-IR: Gaussian Splatting with Unified Shading for Inverse Rendering](https://arxiv.org/abs/2411.07478v1)**  
  作者: Zhihao Liang, Hongdong Li, Kui Jia, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.07478v1.pdf)  
  摘要: Recovering the intrinsic physical attributes of a scene from images, generally termed as the inverse rendering problem, has been a central and challenging task in computer vision and computer graphics...  
  关键词: gaussian splatting, 3d gaussian  
- **[A Hierarchical Compression Technique for 3D Gaussian Splatting Compression](https://arxiv.org/abs/2411.06976v1)**  
  作者: He Huang, Wenjie Huang, Qi Yang, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.06976v1.pdf)  
  摘要: 3D Gaussian Splatting (GS) demonstrates excellent rendering quality and generation speed in novel view synthesis. However, substantial data size poses challenges for storage and transmission, making 3...  
  关键词: gaussian splatting, 3d gaussian  
- **[Adaptive and Temporally Consistent Gaussian Surfels for Multi-view Dynamic Reconstruction](https://arxiv.org/abs/2411.06602v1)**  
  作者: Decai Chen, Brianne Oberson, Ingo Feldmann, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.06602v1.pdf)  
  摘要: 3D Gaussian Splatting has recently achieved notable success in novel view synthesis for dynamic scenes and geometry reconstruction in static scenes. Building on these advancements, early methods have ...  
  关键词: gaussian splatting, 3d gaussian  
- **[SplatFormer: Point Transformer for Robust 3D Gaussian Splatting](https://arxiv.org/abs/2411.06390v2)**  
  作者: Yutong Chen, Marko Mihajlovic, Xiyi Chen, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.06390v2.pdf)  
  摘要: 3D Gaussian Splatting (3DGS) has recently transformed photorealistic reconstruction, achieving high visual fidelity and real-time performance. However, rendering quality significantly deteriorates whe...  
  关键词: gaussian splatting, 3d gaussian  
- **[Through the Curved Cover: Synthesizing Cover Aberrated Scenes with Refractive Field](https://arxiv.org/abs/2411.06365v1)**  
  作者: Liuyue Xie, Jiancong Guo, Laszlo A. Jeni, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.06365v1.pdf)  
  摘要: Recent extended reality headsets and field robots have adopted covers to protect the front-facing cameras from environmental hazards and falls. The surface irregularities on the cover can lead to opti...  
  关键词: gaussian splatting, 3d gaussian, nerf  
- **[AI-Driven Stylization of 3D Environments](https://arxiv.org/abs/2411.06067v1)**  
  作者: Yuanbo Chen, Yixiao Kang, Yukun Song, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.06067v1.pdf)  
  摘要: In this system, we discuss methods to stylize a scene of 3D primitive objects into a higher fidelity 3D scene using novel 3D representations like NeRFs and 3D Gaussian Splatting. Our approach leverage...  
  关键词: gaussian splatting, 3d gaussian, nerf  
- **[GaussianSpa: An "Optimizing-Sparsifying" Simplification Framework for Compact and High-Quality 3D Gaussian Splatting](https://arxiv.org/abs/2411.06019v1)**  
  作者: Yangming Zhang, Wenqi Jia, Wei Niu, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.06019v1.pdf)  
  摘要: 3D Gaussian Splatting (3DGS) has emerged as a mainstream for novel view synthesis, leveraging continuous aggregations of Gaussian functions to model scene geometry. However, 3DGS suffers from substant...  
  关键词: gaussian splatting, 3d gaussian  
- **[PEP-GS: Perceptually-Enhanced Precise Structured 3D Gaussians for View-Adaptive Rendering](https://arxiv.org/abs/2411.05731v1)**  
  作者: Junxi Jin, Xiulai Li, Haiping Huang, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.05731v1.pdf)  
  摘要: Recent advances in structured 3D Gaussians for view-adaptive rendering, particularly through methods like Scaffold-GS, have demonstrated promising results in neural scene representation. However, exis...  
  关键词: 3d gaussian  
- **[ProEdit: Simple Progression is All You Need for High-Quality 3D Scene Editing](https://arxiv.org/abs/2411.05006v1)**  
  作者: Jun-Kun Chen, Yu-Xiong Wang  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.05006v1.pdf)  
  摘要: This paper proposes ProEdit - a simple yet effective framework for high-quality 3D scene editing guided by diffusion distillation in a novel progressive manner. Inspired by the crucial observation tha...  
  关键词: gaussian splatting, 3d gaussian  
- **[MVSplat360: Feed-Forward 360 Scene Synthesis from Sparse Views](https://arxiv.org/abs/2411.04924v1)**  
  作者: Yuedong Chen, Chuanxia Zheng, Haofei Xu, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.04924v1.pdf)  
  摘要: We introduce MVSplat360, a feed-forward approach for 360{\deg} novel view synthesis (NVS) of diverse real-world scenes, using only sparse observations. This setting is inherently ill-posed due to mini...  
  关键词: gaussian splatting, 3d gaussian, 3d reconstruction  
- **[GS2Pose: Two-stage 6D Object Pose Estimation Guided by Gaussian Splatting](https://arxiv.org/abs/2411.03807v3)**  
  作者: Jilan Mei, Junbo Li, Cai Meng  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.03807v3.pdf)  
  摘要: This paper proposes a new method for accurate and robust 6D pose estimation of novel objects, named GS2Pose. By introducing 3D Gaussian splatting, GS2Pose can utilize the reconstruction results withou...  
  关键词: gaussian splatting, 3d gaussian  
- **[3DGS-CD: 3D Gaussian Splatting-based Change Detection for Physical Object Rearrangement](https://arxiv.org/abs/2411.03706v1)**  
  作者: Ziqi Lu, Jianbo Ye, John Leonard  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.03706v1.pdf) | [![Stars](https://img.shields.io/github/stars/520xyxyzq/3DGS-CD?style=social)](https://github.com/520xyxyzq/3DGS-CD)  
  摘要: We present 3DGS-CD, the first 3D Gaussian Splatting (3DGS)-based method for detecting physical object rearrangements in 3D scenes. Our approach estimates 3D object-level changes by comparing two sets ...  
  关键词: gaussian splatting, 3d gaussian  
- **[Structure Consistent Gaussian Splatting with Matching Prior for Few-shot Novel View Synthesis](https://arxiv.org/abs/2411.03637v1)**  
  作者: Rui Peng, Wangze Xu, Luyang Tang, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.03637v1.pdf) | [![Stars](https://img.shields.io/github/stars/prstrive/SCGaussian?style=social)](https://github.com/prstrive/SCGaussian)  
  摘要: Despite the substantial progress of novel view synthesis, existing methods, either based on the Neural Radiance Fields (NeRF) or more recently 3D Gaussian Splatting (3DGS), suffer significant degradat...  
  关键词: gaussian splatting, 3d gaussian, nerf  
- **[Object and Contact Point Tracking in Demonstrations Using 3D Gaussian Splatting](https://arxiv.org/abs/2411.03555v1)**  
  作者: Michael Büttner, Jonathan Francis, Helge Rhodin, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.03555v1.pdf)  
  摘要: This paper introduces a method to enhance Interactive Imitation Learning (IIL) by extracting touch interaction points and tracking object movement from video demonstrations. The approach extends curre...  
  关键词: gaussian splatting, 3d gaussian  
- **[HFGaussian: Learning Generalizable Gaussian Human with Integrated Human Features](https://arxiv.org/abs/2411.03086v1)**  
  作者: Arnab Dey, Cheng-You Lu, Andrew I. Comport, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.03086v1.pdf)  
  摘要: Recent advancements in radiance field rendering show promising results in 3D scene representation, where Gaussian splatting-based techniques emerge as state-of-the-art due to their quality and efficie...  
  关键词: gaussian splatting, 3d gaussian  
- **[LVI-GS: Tightly-coupled LiDAR-Visual-Inertial SLAM using 3D Gaussian Splatting](https://arxiv.org/abs/2411.02703v1)**  
  作者: Huibin Zhao, Weipeng Guan, Peng Lu  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.02703v1.pdf)  
  摘要: 3D Gaussian Splatting (3DGS) has shown its ability in rapid rendering and high-fidelity mapping. In this paper, we introduce LVI-GS, a tightly-coupled LiDAR-Visual-Inertial mapping framework with 3DGS...  
  关键词: gaussian splatting, 3d gaussian, 3d reconstruction  
- **[Modeling Uncertainty in 3D Gaussian Splatting through Continuous Semantic Splatting](https://arxiv.org/abs/2411.02547v1)**  
  作者: Joey Wilson, Marcelino Almeida, Min Sun, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.02547v1.pdf)  
  摘要: In this paper, we present a novel algorithm for probabilistically updating and rasterizing semantic maps within 3D Gaussian Splatting (3D-GS). Although previous methods have introduced algorithms whic...  
  关键词: gaussian splatting, 3d gaussian  
- **[SplatOverflow: Asynchronous Hardware Troubleshooting](https://arxiv.org/abs/2411.02332v2)**  
  作者: Amritansh Kwatra, Tobias Wienberg, Ilan Mandel, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.02332v2.pdf)  
  摘要: As tools for designing and manufacturing hardware become more accessible, smaller producers can develop and distribute novel hardware. However, there aren't established tools to support end-user hardw...  
  关键词: 3d gaussian  
- **[FewViewGS: Gaussian Splatting with Few View Matching and Multi-stage Training](https://arxiv.org/abs/2411.02229v2)**  
  作者: Ruihong Yin, Vladimir Yugay, Yue Li, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.02229v2.pdf)  
  摘要: The field of novel view synthesis from images has seen rapid advancements with the introduction of Neural Radiance Fields (NeRF) and more recently with 3D Gaussian Splatting. Gaussian Splatting became...  
  关键词: gaussian splatting, 3d gaussian, nerf  
- **[GVKF: Gaussian Voxel Kernel Functions for Highly Efficient Surface Reconstruction in Open Scenes](https://arxiv.org/abs/2411.01853v2)**  
  作者: Gaochao Song, Chong Cheng, Hao Wang  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.01853v2.pdf)  
  摘要: In this paper we present a novel method for efficient and effective 3D surface reconstruction in open scenes. Existing Neural Radiance Fields (NeRF) based works typically require extensive training an...  
  关键词: gaussian splatting, 3d gaussian, real-time rendering, nerf  
- **[Real-Time Spatio-Temporal Reconstruction of Dynamic Endoscopic Scenes with 4D Gaussian Splatting](https://arxiv.org/abs/2411.01218v1)**  
  作者: Fengze Li, Jishuai He, Jieming Ma, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.01218v1.pdf)  
  摘要: Dynamic scene reconstruction is essential in robotic minimally invasive surgery, providing crucial spatial information that enhances surgical precision and outcomes. However, existing methods struggle...  
  关键词: gaussian splatting  
- **[CityGaussianV2: Efficient and Geometrically Accurate Reconstruction for Large-Scale Scenes](https://arxiv.org/abs/2411.00771v1)**  
  作者: Yang Liu, Chuanchen Luo, Zhongkai Mao, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.00771v1.pdf)  
  摘要: Recently, 3D Gaussian Splatting (3DGS) has revolutionized radiance field reconstruction, manifesting efficient and high-fidelity novel view synthesis. However, accurately representing surfaces, especi...  
  关键词: gaussian splatting, 3d gaussian  
- **[PCoTTA: Continual Test-Time Adaptation for Multi-Task Point Cloud Understanding](https://arxiv.org/abs/2411.00632v1)**  
  作者: Jincen Jiang, Qianyu Zhou, Yuhang Li, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.00632v1.pdf)  
  摘要: In this paper, we present PCoTTA, an innovative, pioneering framework for Continual Test-Time Adaptation (CoTTA) in multi-task point cloud understanding, enhancing the model's transferability towards ...  

### 2024年10月
- **[Aquatic-GS: A Hybrid 3D Representation for Underwater Scenes](https://arxiv.org/abs/2411.00239v1)**  
  作者: Shaohua Liu, Junzhe Lu, Zuoya Gu, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.00239v1.pdf)  
  摘要: Representing underwater 3D scenes is a valuable yet complex task, as attenuation and scattering effects during underwater imaging significantly couple the information of the objects and the water. Thi...  
  关键词: gaussian splatting, 3d gaussian, real-time rendering  
- **[Self-Ensembling Gaussian Splatting for Few-Shot Novel View Synthesis](https://arxiv.org/abs/2411.00144v2)**  
  作者: Chen Zhao, Xuan Wang, Tong Zhang, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2411.00144v2.pdf)  
  摘要: 3D Gaussian Splatting (3DGS) has demonstrated remarkable effectiveness for novel view synthesis (NVS). However, the 3DGS model tends to overfit when trained with sparse posed views, limiting its gener...  
  关键词: gaussian splatting, 3d gaussian, nerf  
- **[URAvatar: Universal Relightable Gaussian Codec Avatars](https://arxiv.org/abs/2410.24223v1)**  
  作者: Junxuan Li, Chen Cao, Gabriel Schwartz, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.24223v1.pdf)  
  摘要: We present a new approach to creating photorealistic and relightable head avatars from a phone scan with unknown illumination. The reconstructed avatars can be animated and relit in real time with the...  
  关键词: 3d gaussian, real-time rendering  
- **[No Pose, No Problem: Surprisingly Simple 3D Gaussian Splats from Sparse Unposed Images](https://arxiv.org/abs/2410.24207v1)**  
  作者: Botao Ye, Sifei Liu, Haofei Xu, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.24207v1.pdf)  
  摘要: We introduce NoPoSplat, a feed-forward model capable of reconstructing 3D scenes parameterized by 3D Gaussians from \textit{unposed} sparse multi-view images. Our model, trained exclusively with photo...  
  关键词: 3d gaussian, 3d reconstruction  
- **[GeoSplatting: Towards Geometry Guided Gaussian Splatting for Physically-based Inverse Rendering](https://arxiv.org/abs/2410.24204v2)**  
  作者: Kai Ye, Chong Gao, Guanbin Li, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.24204v2.pdf)  
  摘要: We consider the problem of physically-based inverse rendering using 3D Gaussian Splatting (3DGS) representations. While recent 3DGS methods have achieved remarkable results in novel view synthesis (NV...  
  关键词: gaussian splatting, 3d gaussian  
- **[GaussianMarker: Uncertainty-Aware Copyright Protection of 3D Gaussian Splatting](https://arxiv.org/abs/2410.23718v1)**  
  作者: Xiufeng Huang, Ruiqi Li, Yiu-ming Cheung, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.23718v1.pdf)  
  摘要: 3D Gaussian Splatting (3DGS) has become a crucial method for acquiring 3D assets. To protect the copyright of these assets, digital watermarking techniques can be applied to embed ownership informatio...  
  关键词: gaussian splatting, 3d gaussian, nerf  
- **[XRDSLAM: A Flexible and Modular Framework for Deep Learning based SLAM](https://arxiv.org/abs/2410.23690v1)**  
  作者: Xiaomeng Wang, Nan Wang, Guofeng Zhang  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.23690v1.pdf)  
  摘要: In this paper, we propose a flexible SLAM framework, XRDSLAM. It adopts a modular code design and a multi-process running mechanism, providing highly reusable foundational modules such as unified data...  
  关键词: nerf  
- **[GS-Blur: A 3D Scene-Based Dataset for Realistic Image Deblurring](https://arxiv.org/abs/2410.23658v1)**  
  作者: Dongwoo Lee, Joonkyu Park, Kyoung Mu Lee  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.23658v1.pdf)  
  摘要: To train a deblurring network, an appropriate dataset with paired blurry and sharp images is essential. Existing datasets collect blurry images either synthetically by aggregating consecutive sharp fr...  
  关键词: gaussian splatting, 3d gaussian  
- **[ELMGS: Enhancing memory and computation scaLability through coMpression for 3D Gaussian Splatting](https://arxiv.org/abs/2410.23213v1)**  
  作者: Muhammad Salman Ali, Sung-Ho Bae, Enzo Tartaglione  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.23213v1.pdf)  
  摘要: 3D models have recently been popularized by the potentiality of end-to-end training offered first by Neural Radiance Fields and most recently by 3D Gaussian Splatting models. The latter has the big ad...  
  关键词: gaussian splatting, 3d gaussian  
- **[Epipolar-Free 3D Gaussian Splatting for Generalizable Novel View Synthesis](https://arxiv.org/abs/2410.22817v2)**  
  作者: Zhiyuan Min, Yawei Luo, Jianwen Sun, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.22817v2.pdf)  
  摘要: Generalizable 3D Gaussian splitting (3DGS) can reconstruct new scenes from sparse-view observations in a feed-forward inference manner, eliminating the need for scene-specific retraining required in c...  
  关键词: 3d gaussian  
- **[Geometry Cloak: Preventing TGS-based 3D Reconstruction from Copyrighted Images](https://arxiv.org/abs/2410.22705v1)**  
  作者: Qi Song, Ziyuan Luo, Ka Chun Cheung, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.22705v1.pdf)  
  摘要: Single-view 3D reconstruction methods like Triplane Gaussian Splatting (TGS) have enabled high-quality 3D model generation from just a single image input within seconds. However, this capability raise...  
  关键词: gaussian splatting, 3d reconstruction  
- **[PF3plat: Pose-Free Feed-Forward 3D Gaussian Splatting](https://arxiv.org/abs/2410.22128v1)**  
  作者: Sunghwan Hong, Jaewoo Jung, Heeseong Shin, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.22128v1.pdf)  
  摘要: We consider the problem of novel view synthesis from unposed images in a single feed-forward. Our framework capitalizes on fast speed, scalability, and high-quality 3D reconstruction and view synthesi...  
  关键词: 3d gaussian, 3d reconstruction  
- **[FreeGaussian: Guidance-free Controllable 3D Gaussian Splats with Flow Derivatives](https://arxiv.org/abs/2410.22070v1)**  
  作者: Qizhi Chen, Delin Qu, Yiwen Tang, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.22070v1.pdf)  
  摘要: Reconstructing controllable Gaussian splats from monocular video is a challenging task due to its inherently insufficient constraints. Widely adopted approaches supervise complex interactions with add...  
  关键词: 3d gaussian  
- **[ActiveSplat: High-Fidelity Scene Reconstruction through Active Gaussian Splatting](https://arxiv.org/abs/2410.21955v1)**  
  作者: Yuetao Li, Zijia Kuang, Ting Li, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.21955v1.pdf)  
  摘要: We propose ActiveSplat, an autonomous high-fidelity reconstruction system leveraging Gaussian splatting. Taking advantage of efficient and realistic rendering, the system establishes a unified framewo...  
  关键词: gaussian splatting  
- **[MVSDet: Multi-View Indoor 3D Object Detection via Efficient Plane Sweeps](https://arxiv.org/abs/2410.21566v1)**  
  作者: Yating Xu, Chen Li, Gim Hee Lee  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.21566v1.pdf) | [![Stars](https://img.shields.io/github/stars/Pixie8888/MVSDet?style=social)](https://github.com/Pixie8888/MVSDet)  
  摘要: The key challenge of multi-view indoor 3D object detection is to infer accurate geometry information from images for precise 3D detection. Previous method relies on NeRF for geometry reasoning. Howeve...  
  关键词: gaussian splatting, nerf  
- **[Grid4D: 4D Decomposed Hash Encoding for High-fidelity Dynamic Gaussian Splatting](https://arxiv.org/abs/2410.20815v1)**  
  作者: Jiawei Xu, Zexin Fan, Jian Yang, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.20815v1.pdf)  
  摘要: Recently, Gaussian splatting has received more and more attention in the field of static scene rendering. Due to the low computational overhead and inherent flexibility of explicit representations, pl...  
  关键词: gaussian splatting  
- **[LoDAvatar: Hierarchical Embedding and Adaptive Levels of Detail with Gaussian Splatting for Enhanced Human Avatars](https://arxiv.org/abs/2410.20789v1)**  
  作者: Xiaonuo Dongye, Hanzhi Guo, Le Luo, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.20789v1.pdf)  
  摘要: With the advancement of virtual reality, the demand for 3D human avatars is increasing. The emergence of Gaussian Splatting technology has enabled the rendering of Gaussian avatars with superior visua...  
  关键词: gaussian splatting  
- **[CompGS: Unleashing 2D Compositionality for Compositional Text-to-3D via Dynamically Optimizing 3D Gaussians](https://arxiv.org/abs/2410.20723v1)**  
  作者: Chongjian Ge, Chenfeng Xu, Yuanfeng Ji, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.20723v1.pdf)  
  摘要: Recent breakthroughs in text-guided image generation have significantly advanced the field of 3D generation. While generating a single high-quality 3D object is now feasible, generating multiple objec...  
  关键词: gaussian splatting, 3d gaussian  
- **[ODGS: 3D Scene Reconstruction from Omnidirectional Images with 3D Gaussian Splattings](https://arxiv.org/abs/2410.20686v1)**  
  作者: Suyoung Lee, Jaeyoung Chung, Jaeyoo Huh, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.20686v1.pdf) | [![Stars](https://img.shields.io/github/stars/esw0116/ODGS?style=social)](https://github.com/esw0116/ODGS)  
  摘要: Omnidirectional (or 360-degree) images are increasingly being used for 3D applications since they allow the rendering of an entire scene with a single image. Existing works based on neural radiance fi...  
  关键词: gaussian splatting, 3d gaussian, real-time rendering, 3d reconstruction, nerf  
- **[Normal-GS: 3D Gaussian Splatting with Normal-Involved Rendering](https://arxiv.org/abs/2410.20593v1)**  
  作者: Meng Wei, Qianyi Wu, Jianmin Zheng, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.20593v1.pdf)  
  摘要: Rendering and reconstruction are long-standing topics in computer vision and graphics. Achieving both high rendering quality and accurate geometry is a challenge. Recent advancements in 3D Gaussian Sp...  
  关键词: gaussian splatting, 3d gaussian, real-time rendering  
- **[Neural Fields in Robotics: A Survey](https://arxiv.org/abs/2410.20220v1)**  
  作者: Muhammad Zubair Irshad, Mauro Comi, Yen-Chen Lin, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.20220v1.pdf)  
  摘要: Neural Fields have emerged as a transformative approach for 3D scene representation in computer vision and robotics, enabling accurate inference of geometry, 3D semantics, and dynamics from posed 2D d...  
  关键词: gaussian splatting, 3d reconstruction, nerf  
- **[SCube: Instant Large-Scale Scene Reconstruction using VoxSplats](https://arxiv.org/abs/2410.20030v1)**  
  作者: Xuanchi Ren, Yifan Lu, Hanxue Liang, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.20030v1.pdf)  
  摘要: We present SCube, a novel method for reconstructing large-scale 3D scenes (geometry, appearance, and semantics) from a sparse set of posed images. Our method encodes reconstructed scenes using a novel...  
  关键词: 3d gaussian, 3d reconstruction  
- **[DiffGS: Functional Gaussian Splatting Diffusion](https://arxiv.org/abs/2410.19657v2)**  
  作者: Junsheng Zhou, Weiqi Zhang, Yu-Shen Liu  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.19657v2.pdf)  
  摘要: 3D Gaussian Splatting (3DGS) has shown convincing performance in rendering speed and fidelity, yet the generation of Gaussian Splatting remains a challenge due to its discreteness and unstructured nat...  
  关键词: gaussian splatting, 3d gaussian  
- **[Robotic Learning in your Backyard: A Neural Simulator from Open Source Components](https://arxiv.org/abs/2410.19564v1)**  
  作者: Liyou Zhou, Oleg Sinavski, Athanasios Polydoros  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.19564v1.pdf)  
  摘要: The emergence of 3D Gaussian Splatting for fast and high-quality novel view synthesize has opened up the possibility to construct photo-realistic simulations from video for robotic reinforcement learn...  
  关键词: gaussian splatting, 3d gaussian  
- **[Content-Aware Radiance Fields: Aligning Model Complexity with Scene Intricacy Through Learned Bitwidth Quantization](https://arxiv.org/abs/2410.19483v1)**  
  作者: Weihang Liu, Xue Xian Zheng, Jingyi Yu, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.19483v1.pdf) | [![Stars](https://img.shields.io/github/stars/WeihangLiu2024/Content_Aware_NeRF?style=social)](https://github.com/WeihangLiu2024/Content_Aware_NeRF)  
  摘要: The recent popular radiance field models, exemplified by Neural Radiance Fields (NeRF), Instant-NGP and 3D Gaussian Splatting, are designed to represent 3D content by that training models for each ind...  
  关键词: gaussian splatting, 3d gaussian, nerf  
- **[ArCSEM: Artistic Colorization of SEM Images via Gaussian Splatting](https://arxiv.org/abs/2410.21310v1)**  
  作者: Takuma Nishimura, Andreea Dogaru, Martin Oeggerli, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.21310v1.pdf)  
  摘要: Scanning Electron Microscopes (SEMs) are widely renowned for their ability to analyze the surface structures of microscopic objects, offering the capability to capture highly detailed, yet only graysc...  
- **[PixelGaussian: Generalizable 3D Gaussian Reconstruction from Arbitrary Views](https://arxiv.org/abs/2410.18979v1)**  
  作者: Xin Fei, Wenzhao Zheng, Yueqi Duan, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.18979v1.pdf) | [![Stars](https://img.shields.io/github/stars/Barrybarry-Smith/PixelGaussian?style=social)](https://github.com/Barrybarry-Smith/PixelGaussian)  
  摘要: We propose PixelGaussian, an efficient feed-forward framework for learning generalizable 3D Gaussian reconstruction from arbitrary views. Most existing methods rely on uniform pixel-wise Gaussian repr...  
  关键词: 3d gaussian  
- **[3D-Adapter: Geometry-Consistent Multi-View Diffusion for High-Quality 3D Generation](https://arxiv.org/abs/2410.18974v1)**  
  作者: Hansheng Chen, Bokui Shen, Yulin Liu, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.18974v1.pdf)  
  摘要: Multi-view image diffusion models have significantly advanced open-domain 3D object generation. However, most existing models rely on 2D network architectures that lack inherent 3D biases, resulting i...  
  关键词: gaussian splatting  
- **[Sort-free Gaussian Splatting via Weighted Sum Rendering](https://arxiv.org/abs/2410.18931v1)**  
  作者: Qiqi Hou, Randall Rauwendaal, Zifeng Li, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.18931v1.pdf)  
  摘要: Recently, 3D Gaussian Splatting (3DGS) has emerged as a significant advancement in 3D scene reconstruction, attracting considerable attention due to its ability to recover high-fidelity details while ...  
  关键词: gaussian splatting, 3d gaussian  
- **[Dynamic 3D Gaussian Tracking for Graph-Based Neural Dynamics Modeling](https://arxiv.org/abs/2410.18912v1)**  
  作者: Mingtong Zhang, Kaifeng Zhang, Yunzhu Li  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.18912v1.pdf)  
  摘要: Videos of robots interacting with objects encode rich information about the objects' dynamics. However, existing video prediction approaches typically do not explicitly account for the 3D information ...  
  关键词: gaussian splatting, 3d gaussian  
- **[Binocular-Guided 3D Gaussian Splatting with View Consistency for Sparse View Synthesis](https://arxiv.org/abs/2410.18822v2)**  
  作者: Liang Han, Junsheng Zhou, Yu-Shen Liu, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.18822v2.pdf)  
  摘要: Novel view synthesis from sparse inputs is a vital yet challenging task in 3D computer vision. Previous methods explore 3D Gaussian Splatting with neural priors (e.g. depth priors) as an additional su...  
  关键词: gaussian splatting, 3d gaussian, nerf  
- **[VR-Splatting: Foveated Radiance Field Rendering via 3D Gaussian Splatting and Neural Points](https://arxiv.org/abs/2410.17932v1)**  
  作者: Linus Franke, Laura Fink, Marc Stamminger  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.17932v1.pdf)  
  摘要: Recent advances in novel view synthesis (NVS), particularly neural radiance fields (NeRF) and Gaussian splatting (3DGS), have demonstrated impressive results in photorealistic scene rendering. These t...  
  关键词: gaussian splatting, nerf  
- **[PLGS: Robust Panoptic Lifting with 3D Gaussian Splatting](https://arxiv.org/abs/2410.17505v1)**  
  作者: Yu Wang, Xiaobao Wei, Ming Lu, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.17505v1.pdf)  
  摘要: Previous methods utilize the Neural Radiance Field (NeRF) for panoptic lifting, while their training and rendering speed are unsatisfactory. In contrast, 3D Gaussian Splatting (3DGS) has emerged as a ...  
  关键词: gaussian splatting, 3d gaussian, nerf  
- **[AG-SLAM: Active Gaussian Splatting SLAM](https://arxiv.org/abs/2410.17422v1)**  
  作者: Wen Jiang, Boshu Lei, Katrina Ashton, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.17422v1.pdf)  
  摘要: We present AG-SLAM, the first active SLAM system utilizing 3D Gaussian Splatting (3DGS) for online scene reconstruction. In recent years, radiance field scene representations, including 3DGS have been...  
  关键词: gaussian splatting, 3d gaussian  
- **[SpectroMotion: Dynamic 3D Reconstruction of Specular Scenes](https://arxiv.org/abs/2410.17249v1)**  
  作者: Cheng-De Fan, Chen-Wei Chang, Yi-Ruei Liu, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.17249v1.pdf)  
  摘要: We present SpectroMotion, a novel approach that combines 3D Gaussian Splatting (3DGS) with physically-based rendering (PBR) and deformation fields to reconstruct dynamic specular scenes. Previous meth...  
  关键词: gaussian splatting, 3d gaussian  
- **[LVSM: A Large View Synthesis Model with Minimal 3D Inductive Bias](https://arxiv.org/abs/2410.17242v1)**  
  作者: Haian Jin, Hanwen Jiang, Hao Tan, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.17242v1.pdf)  
  摘要: We propose the Large View Synthesis Model (LVSM), a novel transformer-based approach for scalable and generalizable novel view synthesis from sparse-view inputs. We introduce two architectures: (1) an...  
  关键词: nerf  
- **[E-3DGS: Gaussian Splatting with Exposure and Motion Events](https://arxiv.org/abs/2410.16995v1)**  
  作者: Xiaoting Yin, Hao Shi, Yuhan Bao, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.16995v1.pdf) | [![Stars](https://img.shields.io/github/stars/MasterHow/E-3DGS?style=social)](https://github.com/MasterHow/E-3DGS)  
  摘要: Estimating Neural Radiance Fields (NeRFs) from images captured under optimal conditions has been extensively explored in the vision community. However, robotic applications often face challenges such ...  
  关键词: gaussian splatting, 3d gaussian, 3d reconstruction, nerf  
- **[Multi-Layer Gaussian Splatting for Immersive Anatomy Visualization](https://arxiv.org/abs/2410.16978v1)**  
  作者: Constantin Kleinbeck, Hannah Schieber, Klaus Engel, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.16978v1.pdf)  
  摘要: In medical image visualization, path tracing of volumetric medical data like CT scans produces lifelike three-dimensional visualizations. Immersive VR displays can further enhance the understanding of...  
- **[MvDrag3D: Drag-based Creative 3D Editing via Multi-view Generation-Reconstruction Priors](https://arxiv.org/abs/2410.16272v1)**  
  作者: Honghua Chen, Yushi Lan, Yongwei Chen, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.16272v1.pdf)  
  摘要: Drag-based editing has become popular in 2D content creation, driven by the capabilities of image generative models. However, extending this technique to 3D remains a challenge. Existing 3D drag-based...  
  关键词: 3d gaussian  
- **[3DGS-Enhancer: Enhancing Unbounded 3D Gaussian Splatting with View-consistent 2D Diffusion Priors](https://arxiv.org/abs/2410.16266v1)**  
  作者: Xi Liu, Chaoyi Zhou, Siyu Huang  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.16266v1.pdf)  
  摘要: Novel-view synthesis aims to generate novel views of a scene from multiple input images or videos, and recent advancements like 3D Gaussian splatting (3DGS) have achieved notable success in producing ...  
  关键词: gaussian splatting, 3d gaussian  
- **[MSGField: A Unified Scene Representation Integrating Motion, Semantics, and Geometry for Robotic Manipulation](https://arxiv.org/abs/2410.15730v1)**  
  作者: Yu Sheng, Runfeng Lin, Lidian Wang, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.15730v1.pdf)  
  摘要: Combining accurate geometry with rich semantics has been proven to be highly effective for language-guided robotic manipulation. Existing methods for dynamic scenes either fail to update in real-time ...  
  关键词: gaussian splatting, real-time rendering  
- **[LucidFusion: Generating 3D Gaussians with Arbitrary Unposed Images](https://arxiv.org/abs/2410.15636v2)**  
  作者: Hao He, Yixun Liang, Luozhou Wang, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.15636v2.pdf)  
  摘要: Recent large reconstruction models have made notable progress in generating high-quality 3D objects from single images. However, these methods often struggle with controllability, as they lack informa...  
  关键词: 3d gaussian, 3d reconstruction  
- **[Fully Explicit Dynamic Gaussian Splatting](https://arxiv.org/abs/2410.15629v2)**  
  作者: Junoh Lee, Chang-Yeon Won, Hyunjun Jung, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.15629v2.pdf)  
  摘要: 3D Gaussian Splatting has shown fast and high-quality rendering results in static scenes by leveraging dense 3D prior and explicit representations. Unfortunately, the benefits of the prior and represe...  
  关键词: gaussian splatting, 3d gaussian  
- **[EF-3DGS: Event-Aided Free-Trajectory 3D Gaussian Splatting](https://arxiv.org/abs/2410.15392v2)**  
  作者: Bohao Liao, Wei Zhai, Zengyu Wan, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.15392v2.pdf)  
  摘要: Scene reconstruction from casually captured videos has wide applications in real-world scenarios. With recent advancements in differentiable rendering techniques, several methods have attempted to sim...  
  关键词: nerf  
- **[GS-LIVM: Real-Time Photo-Realistic LiDAR-Inertial-Visual Mapping with Gaussian Splatting](https://arxiv.org/abs/2410.17084v1)**  
  作者: Yusen Xie, Zhenmin Huang, Jin Wu, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.17084v1.pdf)  
  摘要: In this paper, we introduce GS-LIVM, a real-time photo-realistic LiDAR-Inertial-Visual mapping framework with Gaussian Splatting tailored for outdoor scenes. Compared to existing methods based on Neur...  
  关键词: gaussian splatting, 3d gaussian, nerf  
- **[LUDVIG: Learning-free Uplifting of 2D Visual features to Gaussian Splatting scenes](https://arxiv.org/abs/2410.14462v1)**  
  作者: Juliette Marrie, Romain Ménégaux, Michael Arbel, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.14462v1.pdf)  
  摘要: We address the task of uplifting visual features or semantic masks from 2D vision models to 3D scenes represented by Gaussian Splatting. Whereas common approaches rely on iterative optimization-based ...  
  关键词: gaussian splatting  
- **[Neural Signed Distance Function Inference through Splatting 3D Gaussians Pulled on Zero-Level Set](https://arxiv.org/abs/2410.14189v1)**  
  作者: Wenyuan Zhang, Yu-Shen Liu, Zhizhong Han  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.14189v1.pdf)  
  摘要: It is vital to infer a signed distance function (SDF) in multi-view based surface reconstruction. 3D Gaussian splatting (3DGS) provides a novel perspective for volume rendering, and shows advantages i...  
  关键词: gaussian splatting, 3d gaussian, neural rendering  
- **[DaRePlane: Direction-aware Representations for Dynamic Scene Reconstruction](https://arxiv.org/abs/2410.14169v1)**  
  作者: Ange Lou, Benjamin Planche, Zhongpai Gao, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.14169v1.pdf)  
  摘要: Numerous recent approaches to modeling and re-rendering dynamic scenes leverage plane-based explicit representations, addressing slow training times associated with models like neural radiance fields ...  
  关键词: gaussian splatting, nerf  
- **[DepthSplat: Connecting Gaussian Splatting and Depth](https://arxiv.org/abs/2410.13862v2)**  
  作者: Haofei Xu, Songyou Peng, Fangjinhua Wang, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.13862v2.pdf)  
  摘要: Gaussian splatting and single/multi-view depth estimation are typically studied in isolation. In this paper, we present DepthSplat to connect Gaussian splatting and depth estimation and study their in...  
  关键词: gaussian splatting, 3d gaussian  
- **[Differentiable Robot Rendering](https://arxiv.org/abs/2410.13851v1)**  
  作者: Ruoshi Liu, Alper Canberk, Shuran Song, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.13851v1.pdf)  
  摘要: Vision foundation models trained on massive amounts of visual data have shown unprecedented reasoning and planning skills in open-world settings. A key challenge in applying them to robotic tasks is t...  
- **[MEGA: Memory-Efficient 4D Gaussian Splatting for Dynamic Scenes](https://arxiv.org/abs/2410.13613v1)**  
  作者: Xinjie Zhang, Zhening Liu, Yifan Zhang, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.13613v1.pdf)  
  摘要: 4D Gaussian Splatting (4DGS) has recently emerged as a promising technique for capturing complex dynamic 3D scenes with high fidelity. It utilizes a 4D Gaussian representation and a GPU-friendly raste...  
  关键词: gaussian splatting  
- **[DN-4DGS: Denoised Deformable Network with Temporal-Spatial Aggregation for Dynamic Scene Rendering](https://arxiv.org/abs/2410.13607v2)**  
  作者: Jiahao Lu, Jiacheng Deng, Ruijie Zhu, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.13607v2.pdf)  
  摘要: Dynamic scenes rendering is an intriguing yet challenging problem. Although current methods based on NeRF have achieved satisfactory performance, they still can not reach real-time levels. Recently, 3...  
  关键词: gaussian splatting, 3d gaussian, nerf  
- **[DriveDreamer4D: World Models Are Effective Data Machines for 4D Driving Scene Representation](https://arxiv.org/abs/2410.13571v3)**  
  作者: Guosheng Zhao, Chaojun Ni, Xiaofeng Wang, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.13571v3.pdf)  
  摘要: Closed-loop simulation is essential for advancing end-to-end autonomous driving systems. Contemporary sensor simulation methods, such as NeRF and 3DGS, rely predominantly on conditions closely aligned...  
  关键词: nerf  
- **[L3DG: Latent 3D Gaussian Diffusion](https://arxiv.org/abs/2410.13530v1)**  
  作者: Barbara Roessle, Norman Müller, Lorenzo Porzi, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.13530v1.pdf)  
  摘要: We propose L3DG, the first approach for generative 3D modeling of 3D Gaussians through a latent 3D Gaussian diffusion formulation. This enables effective generative 3D modeling, scaling to generation ...  
  关键词: 3d gaussian  
- **[GlossyGS: Inverse Rendering of Glossy Objects with 3D Gaussian Splatting](https://arxiv.org/abs/2410.13349v1)**  
  作者: Shuichang Lai, Letian Huang, Jie Guo, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.13349v1.pdf)  
  摘要: Reconstructing objects from posed images is a crucial and complex task in computer graphics and computer vision. While NeRF-based neural reconstruction methods have exhibited impressive reconstruction...  
  关键词: gaussian splatting, 3d gaussian, nerf  
- **[Hybrid bundle-adjusting 3D Gaussians for view consistent rendering with pose optimization](https://arxiv.org/abs/2410.13280v1)**  
  作者: Yanan Guo, Ying Xie, Ying Chang, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.13280v1.pdf) | [![Stars](https://img.shields.io/github/stars/Bistu3DV/hybridBA?style=social)](https://github.com/Bistu3DV/hybridBA)  
  摘要: Novel view synthesis has made significant progress in the field of 3D computer vision. However, the rendering of view-consistent novel views from imperfect camera poses remains challenging. In this pa...  
  关键词: 3d gaussian  
- **[UniG: Modelling Unitary 3D Gaussians for View-consistent 3D Reconstruction](https://arxiv.org/abs/2410.13195v2)**  
  作者: Jiamin Wu, Kenkun Liu, Yukai Shi, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.13195v2.pdf) | [![Stars](https://img.shields.io/github/stars/jwubz123/UNIG?style=social)](https://github.com/jwubz123/UNIG)  
  摘要: In this work, we present UniG, a view-consistent 3D reconstruction and novel view synthesis model that generates a high-fidelity representation of 3D Gaussians from sparse images. Existing 3D Gaussian...  
  关键词: 3d gaussian, 3d reconstruction  
- **[Long-LRM: Long-sequence Large Reconstruction Model for Wide-coverage Gaussian Splats](https://arxiv.org/abs/2410.12781v1)**  
  作者: Chen Ziwen, Hao Tan, Kai Zhang, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.12781v1.pdf)  
  摘要: We propose Long-LRM, a generalizable 3D Gaussian reconstruction model that is capable of reconstructing a large scene from a long sequence of input images. Specifically, our model can process 32 sourc...  
  关键词: 3d gaussian  
- **[TV-3DG: Mastering Text-to-3D Customized Generation with Visual Prompt](https://arxiv.org/abs/2410.21299v2)**  
  作者: Jiahui Yang, Donglin Di, Baorui Ma, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.21299v2.pdf)  
  摘要: In recent years, advancements in generative models have significantly expanded the capabilities of text-to-3D generation. Many approaches rely on Score Distillation Sampling (SDS) technology. However,...  
- **[3D Gaussian Splatting in Robotics: A Survey](https://arxiv.org/abs/2410.12262v1)**  
  作者: Siting Zhu, Guangming Wang, Dezhi Kong, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.12262v1.pdf)  
  摘要: Dense 3D representations of the environment have been a long-term goal in the robotics field. While previous Neural Radiance Fields (NeRF) representation have been prevalent for its implicit, coordina...  
  关键词: gaussian splatting, 3d gaussian, real-time rendering, nerf  
- **[SplatPose+: Real-time Image-Based Pose-Agnostic 3D Anomaly Detection](https://arxiv.org/abs/2410.12080v1)**  
  作者: Yizhe Liu, Yan Song Hu, Yuhao Chen, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.12080v1.pdf)  
  摘要: Image-based Pose-Agnostic 3D Anomaly Detection is an important task that has emerged in industrial quality control. This task seeks to find anomalies from query images of a tested object given a set o...  
  关键词: gaussian splatting, 3d gaussian  
- **[LoGS: Visual Localization via Gaussian Splatting with Fewer Training Images](https://arxiv.org/abs/2410.11505v1)**  
  作者: Yuzhou Cheng, Jianhao Jiao, Yue Wang, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.11505v1.pdf)  
  摘要: Visual localization involves estimating a query image's 6-DoF (degrees of freedom) camera pose, which is a fundamental component in various computer vision and robotic tasks. This paper presents LoGS,...  
  关键词: gaussian splatting, 3d gaussian  
- **[GS^3: Efficient Relighting with Triple Gaussian Splatting](https://arxiv.org/abs/2410.11419v1)**  
  作者: Zoubin Bi, Yixin Zeng, Chong Zeng, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.11419v1.pdf)  
  摘要: We present a spatial and angular Gaussian based representation and a triple splatting process, for real-time, high-quality novel lighting-and-view synthesis from multi-view point-lit input images. To ...  
- **[MCGS: Multiview Consistency Enhancement for Sparse-View 3D Gaussian Radiance Fields](https://arxiv.org/abs/2410.11394v1)**  
  作者: Yuru Xiao, Deming Zhai, Wenbo Zhao, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.11394v1.pdf)  
  摘要: Radiance fields represented by 3D Gaussians excel at synthesizing novel views, offering both high training efficiency and fast rendering. However, with sparse input views, the lack of multi-view consi...  
  关键词: gaussian splatting, 3d gaussian  
- **[GSORB-SLAM: Gaussian Splatting SLAM benefits from ORB features and Transmittance information](https://arxiv.org/abs/2410.11356v2)**  
  作者: Wancai Zheng, Xinyi Yu, Jintao Rong, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.11356v2.pdf)  
  摘要: The emergence of 3D Gaussian Splatting (3DGS) has recently sparked a renewed wave of dense visual SLAM research. However, current methods face challenges such as sensitivity to artifacts and noise, su...  
  关键词: gaussian splatting, 3d gaussian  
- **[Scalable Indoor Novel-View Synthesis using Drone-Captured 360 Imagery with 3D Gaussian Splatting](https://arxiv.org/abs/2410.11285v1)**  
  作者: Yuanbo Chen, Chengyu Zhang, Jason Wang, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.11285v1.pdf)  
  摘要: Scene reconstruction and novel-view synthesis for large, complex, multi-story, indoor scenes is a challenging and time-consuming task. Prior methods have utilized drones for data capture and radiance ...  
  关键词: gaussian splatting, 3d gaussian  
- **[Few-shot Novel View Synthesis using Depth Aware 3D Gaussian Splatting](https://arxiv.org/abs/2410.11080v1)**  
  作者: Raja Kumar, Vanshika Vats  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.11080v1.pdf) | [![Stars](https://img.shields.io/github/stars/raja-kumar/depth-aware-3DGS?style=social)](https://github.com/raja-kumar/depth-aware-3DGS)  
  摘要: 3D Gaussian splatting has surpassed neural radiance field methods in novel view synthesis by achieving lower computational costs and real-time high-quality rendering. Although it produces a high-quali...  
  关键词: gaussian splatting, 3d gaussian  
- **[3DArticCyclists: Generating Simulated Dynamic 3D Cyclists for Human-Object Interaction (HOI) and Autonomous Driving Applications](https://arxiv.org/abs/2410.10782v1)**  
  作者: Eduardo R. Corral-Soto, Yang Liu, Tongtong Cao, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.10782v1.pdf)  
  摘要: Human-object interaction (HOI) and human-scene interaction (HSI) are crucial for human-centric scene understanding applications in Embodied Artificial Intelligence (EAI), robotics, and augmented reali...  
  关键词: 3d reconstruction, nerf  
- **[4-LEGS: 4D Language Embedded Gaussian Splatting](https://arxiv.org/abs/2410.10719v2)**  
  作者: Gal Fiebelman, Tamir Cohen, Ayellet Morgenstern, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.10719v2.pdf)  
  摘要: The emergence of neural representations has revolutionized our means for digitally viewing a wide range of 3D scenes, enabling the synthesis of photorealistic images rendered from novel views. Recentl...  
  关键词: gaussian splatting, 3d gaussian  
- **[4DStyleGaussian: Zero-shot 4D Style Transfer with Gaussian Splatting](https://arxiv.org/abs/2410.10412v1)**  
  作者: Wanlin Liang, Hongbin Xu, Weitao Chen, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.10412v1.pdf)  
  摘要: 3D neural style transfer has gained significant attention for its potential to provide user-friendly stylization with spatial consistency. However, existing 3D style transfer methods often fall short ...  
  关键词: gaussian splatting  
- **[GUISE: Graph GaUssIan Shading watErmark](https://arxiv.org/abs/2410.10178v1)**  
  作者: Renyi Yang  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.10178v1.pdf)  
  摘要: In the expanding field of generative artificial intelligence, integrating robust watermarking technologies is essential to protect intellectual property and maintain content authenticity. Traditionall...  
- **[Gaussian Splatting Visual MPC for Granular Media Manipulation](https://arxiv.org/abs/2410.09740v1)**  
  作者: Wei-Cheng Tseng, Ellina Zhang, Krishna Murthy Jatavallabhula, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.09740v1.pdf)  
  摘要: Recent advancements in learned 3D representations have enabled significant progress in solving complex robotic manipulation tasks, particularly for rigid-body objects. However, manipulating granular m...  
  关键词: gaussian splatting  
- **[Enhancing Single Image to 3D Generation using Gaussian Splatting and Hybrid Diffusion Priors](https://arxiv.org/abs/2410.09467v2)**  
  作者: Hritam Basak, Hadi Tabatabaee, Shreekant Gayaka, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.09467v2.pdf)  
  摘要: 3D object generation from a single image involves estimating the full 3D geometry and texture of unseen views from an unposed RGB image captured in the wild. Accurately reconstructing an object's comp...  
  关键词: gaussian splatting  
- **[SurgicalGS: Dynamic 3D Gaussian Splatting for Accurate Robotic-Assisted Surgical Scene Reconstruction](https://arxiv.org/abs/2410.09292v1)**  
  作者: Jialei Chen, Xin Zhang, Mobarakol Islam, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.09292v1.pdf)  
  摘要: Accurate 3D reconstruction of dynamic surgical scenes from endoscopic video is essential for robotic-assisted surgery. While recent 3D Gaussian Splatting methods have shown promise in achieving high-q...  
  关键词: gaussian splatting, 3d gaussian, 3d reconstruction  
- **[MeshGS: Adaptive Mesh-Aligned Gaussian Splatting for High-Quality Rendering](https://arxiv.org/abs/2410.08941v1)**  
  作者: Jaehoon Choi, Yonghan Lee, Hyungtae Lee, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.08941v1.pdf)  
  摘要: Recently, 3D Gaussian splatting has gained attention for its capability to generate high-fidelity rendering results. At the same time, most applications such as games, animation, and AR/VR use mesh-ba...  
  关键词: gaussian splatting, 3d gaussian, neural rendering, nerf  
- **[Learning Interaction-aware 3D Gaussian Splatting for One-shot Hand Avatars](https://arxiv.org/abs/2410.08840v1)**  
  作者: Xuan Huang, Hanhui Li, Wanquan Liu, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.08840v1.pdf) | [![Stars](https://img.shields.io/github/stars/XuanHuang0/GuassianHand?style=social)](https://github.com/XuanHuang0/GuassianHand)  
  摘要: In this paper, we propose to create animatable avatars for interacting hands with 3D Gaussian Splatting (GS) and single-image inputs. Existing GS-based methods designed for single subjects often yield...  
  关键词: gaussian splatting, 3d gaussian  
- **[Look Gauss, No Pose: Novel View Synthesis using Gaussian Splatting without Accurate Pose Initialization](https://arxiv.org/abs/2410.08743v1)**  
  作者: Christian Schmidt, Jens Piekenbrinck, Bastian Leibe  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.08743v1.pdf) | [![Stars](https://img.shields.io/github/stars/Schmiddo/noposegs?style=social)](https://github.com/Schmiddo/noposegs)  
  摘要: 3D Gaussian Splatting has recently emerged as a powerful tool for fast and accurate novel-view synthesis from a set of posed input images. However, like most novel-view synthesis approaches, it relies...  
  关键词: gaussian splatting, 3d gaussian  
- **[FusionSense: Bridging Common Sense, Vision, and Touch for Robust Sparse-View Reconstruction](https://arxiv.org/abs/2410.08282v1)**  
  作者: Irving Fang, Kairui Shi, Xujin He, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.08282v1.pdf)  
  摘要: Humans effortlessly integrate common-sense knowledge with sensory input from vision and touch to understand their surroundings. Emulating this capability, we introduce FusionSense, a novel 3D reconstr...  
  关键词: gaussian splatting, 3d gaussian, 3d reconstruction  
- **[Poison-splat: Computation Cost Attack on 3D Gaussian Splatting](https://arxiv.org/abs/2410.08190v1)**  
  作者: Jiahao Lu, Yifan Zhang, Qiuhong Shen, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.08190v1.pdf)  
  摘要: 3D Gaussian splatting (3DGS), known for its groundbreaking performance and efficiency, has become a dominant 3D representation and brought progress to many 3D vision tasks. However, in this work, we r...  
  关键词: gaussian splatting, 3d gaussian  
- **[DifFRelight: Diffusion-Based Facial Performance Relighting](https://arxiv.org/abs/2410.08188v1)**  
  作者: Mingming He, Pascal Clausen, Ahmet Levent Taşel, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.08188v1.pdf)  
  摘要: We present a novel framework for free-viewpoint facial performance relighting using diffusion-based image-to-image translation. Leveraging a subject-specific dataset containing diverse facial expressi...  
  关键词: gaussian splatting, 3d gaussian  
- **[RGM: Reconstructing High-fidelity 3D Car Assets with Relightable 3D-GS Generative Model from a Single Image](https://arxiv.org/abs/2410.08181v1)**  
  作者: Xiaoxue Chen, Jv Zheng, Hao Huang, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.08181v1.pdf)  
  摘要: The generation of high-quality 3D car assets is essential for various applications, including video games, autonomous driving, and virtual reality. Current 3D generation methods utilizing NeRF or 3D-G...  
  关键词: 3d gaussian, nerf  
- **[Neural Material Adaptor for Visual Grounding of Intrinsic Dynamics](https://arxiv.org/abs/2410.08257v1)**  
  作者: Junyi Cao, Shanyan Guan, Yanhao Ge, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.08257v1.pdf)  
  摘要: While humans effortlessly discern intrinsic dynamics and adapt to new scenarios, modern AI systems often struggle. Current methods for visual grounding of dynamics either use pure neural-network-based...  
  关键词: gaussian splatting, 3d gaussian  
- **[Efficient Perspective-Correct 3D Gaussian Splatting Using Hybrid Transparency](https://arxiv.org/abs/2410.08129v2)**  
  作者: Florian Hahlbohm, Fabian Friederichs, Tim Weyrich, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.08129v2.pdf)  
  摘要: 3D Gaussian Splats (3DGS) have proven a versatile rendering primitive, both for inverse rendering as well as real-time exploration of scenes. In these applications, coherence across camera frames and ...  
  关键词: gaussian splatting, 3d gaussian  
- **[IncEventGS: Pose-Free Gaussian Splatting from a Single Event Camera](https://arxiv.org/abs/2410.08107v2)**  
  作者: Jian Huang, Chengrui Dong, Peidong Liu  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.08107v2.pdf) | [![Stars](https://img.shields.io/github/stars/wu-cvgl/IncEventGS?style=social)](https://github.com/wu-cvgl/IncEventGS)  
  摘要: Implicit neural representation and explicit 3D Gaussian Splatting (3D-GS) for novel view synthesis have achieved remarkable progress with frame-based camera (e.g. RGB and RGB-D cameras) recently. Comp...  
  关键词: gaussian splatting, 3d gaussian, nerf  
- **[Fast Feedforward 3D Gaussian Splatting Compression](https://arxiv.org/abs/2410.08017v2)**  
  作者: Yihang Chen, Qianyi Wu, Mengyao Li, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.08017v2.pdf) | [![Stars](https://img.shields.io/github/stars/YihangChen-ee/FCGS?style=social)](https://github.com/YihangChen-ee/FCGS)  
  摘要: With 3D Gaussian Splatting (3DGS) advancing real-time and high-fidelity rendering for novel view synthesis, storage requirements pose challenges for their widespread adoption. Although various compres...  
  关键词: gaussian splatting, 3d gaussian  
- **[Generalizable and Animatable Gaussian Head Avatar](https://arxiv.org/abs/2410.07971v1)**  
  作者: Xuangeng Chu, Tatsuya Harada  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.07971v1.pdf) | [![Stars](https://img.shields.io/github/stars/xg-chu/GAGAvatar?style=social)](https://github.com/xg-chu/GAGAvatar)  
  摘要: In this paper, we propose Generalizable and Animatable Gaussian head Avatar (GAGAvatar) for one-shot animatable head avatar reconstruction. Existing methods rely on neural radiance fields, leading to ...  
  关键词: 3d gaussian  
- **[L-VITeX: Light-weight Visual Intuition for Terrain Exploration](https://arxiv.org/abs/2410.07872v1)**  
  作者: Antar Mazumder, Zarin Anjum Madhiha  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.07872v1.pdf)  
  摘要: This paper presents L-VITeX, a lightweight visual intuition system for terrain exploration designed for resource-constrained robots and swarms. L-VITeX aims to provide a hint of Regions of Interest (R...  
- **[MotionGS: Exploring Explicit Motion Guidance for Deformable 3D Gaussian Splatting](https://arxiv.org/abs/2410.07707v1)**  
  作者: Ruijie Zhu, Yanzhe Liang, Hanzhi Chang, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.07707v1.pdf)  
  摘要: Dynamic scene reconstruction is a long-term challenge in the field of 3D vision. Recently, the emergence of 3D Gaussian Splatting has provided new insights into this problem. Although subsequent effor...  
  关键词: gaussian splatting, 3d gaussian  
- **[3D Vision-Language Gaussian Splatting](https://arxiv.org/abs/2410.07577v1)**  
  作者: Qucheng Peng, Benjamin Planche, Zhongpai Gao, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.07577v1.pdf)  
  摘要: Recent advancements in 3D reconstruction methods and vision-language models have propelled the development of multi-modal 3D scene understanding, which has vital applications in robotics, autonomous d...  
  关键词: gaussian splatting, 3d reconstruction  
- **[Thing2Reality: Transforming 2D Content into Conditioned Multiviews and 3D Gaussian Objects for XR Communication](https://arxiv.org/abs/2410.07119v1)**  
  作者: Erzhen Hu, Mingyi Li, Jungtaek Hong, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.07119v1.pdf)  
  摘要: During remote communication, participants often share both digital and physical content, such as product designs, digital assets, and environments, to enhance mutual understanding. Recent advances in ...  
  关键词: 3d gaussian  
- **[DreamMesh4D: Video-to-4D Generation with Sparse-Controlled Gaussian-Mesh Hybrid Representation](https://arxiv.org/abs/2410.06756v1)**  
  作者: Zhiqi Li, Yiming Chen, Peidong Liu  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.06756v1.pdf)  
  摘要: Recent advancements in 2D/3D generative techniques have facilitated the generation of dynamic 3D objects from monocular videos. Previous methods mainly rely on the implicit neural radiance fields (NeR...  
  关键词: gaussian splatting, nerf  
- **[ES-Gaussian: Gaussian Splatting Mapping via Error Space-Based Gaussian Completion](https://arxiv.org/abs/2410.06613v2)**  
  作者: Lu Chen, Yingfu Zeng, Haoang Li, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.06613v2.pdf)  
  摘要: Accurate and affordable indoor 3D reconstruction is critical for effective robot navigation and interaction. Traditional LiDAR-based mapping provides high precision but is costly, heavy, and power-int...  
  关键词: 3d reconstruction  
- **[3D Representation Methods: A Survey](https://arxiv.org/abs/2410.06475v1)**  
  作者: Zhengren Wang  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.06475v1.pdf)  
  摘要: The field of 3D representation has experienced significant advancements, driven by the increasing demand for high-fidelity 3D models in various applications such as computer graphics, virtual reality,...  
  关键词: gaussian splatting, 3d gaussian, nerf  
- **[Spiking GS: Towards High-Accuracy and Low-Cost Surface Reconstruction via Spiking Neuron-based Gaussian Splatting](https://arxiv.org/abs/2410.07266v5)**  
  作者: Weixing Zhang, Zongrui Li, De Ma, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.07266v5.pdf) | [![Stars](https://img.shields.io/github/stars/zju-bmi-lab/SpikingGS?style=social)](https://github.com/zju-bmi-lab/SpikingGS)  
  摘要: 3D Gaussian Splatting is capable of reconstructing 3D scenes in minutes. Despite recent advances in improving surface reconstruction accuracy, the reconstructed results still exhibit bias and suffer f...  
  关键词: gaussian splatting, 3d gaussian  
- **[HiSplat: Hierarchical 3D Gaussian Splatting for Generalizable Sparse-View Reconstruction](https://arxiv.org/abs/2410.06245v1)**  
  作者: Shengji Tang, Weicai Ye, Peng Ye, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.06245v1.pdf)  
  摘要: Reconstructing 3D scenes from multiple viewpoints is a fundamental task in stereo vision. Recently, advances in generalizable 3D Gaussian Splatting have enabled high-quality novel view synthesis for u...  
  关键词: gaussian splatting, 3d gaussian  
- **[RelitLRM: Generative Relightable Radiance for Large Reconstruction Models](https://arxiv.org/abs/2410.06231v2)**  
  作者: Tianyuan Zhang, Zhengfei Kuang, Haian Jin, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.06231v2.pdf)  
  摘要: We propose RelitLRM, a Large Reconstruction Model (LRM) for generating high-quality Gaussian splatting representations of 3D objects under novel illuminations from sparse (4-8) posed images captured u...  
  关键词: gaussian splatting  
- **[GSLoc: Visual Localization with 3D Gaussian Splatting](https://arxiv.org/abs/2410.06165v1)**  
  作者: Kazii Botashev, Vladislav Pyatov, Gonzalo Ferrer, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.06165v1.pdf)  
  摘要: We present GSLoc: a new visual localization method that performs dense camera alignment using 3D Gaussian Splatting as a map representation of the scene. GSLoc backpropagates pose gradients over the r...  
  关键词: gaussian splatting, 3d gaussian  
- **[SplaTraj: Camera Trajectory Generation with Semantic Gaussian Splatting](https://arxiv.org/abs/2410.06014v1)**  
  作者: Xinyi Liu, Tianyi Zhang, Matthew Johnson-Roberson, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.06014v1.pdf)  
  摘要: Many recent developments for robots to represent environments have focused on photorealistic reconstructions. This paper particularly focuses on generating sequences of images from the photorealistic ...  
  关键词: gaussian splatting  
- **[Comparative Analysis of Novel View Synthesis and Photogrammetry for 3D Forest Stand Reconstruction and extraction of individual tree parameters](https://arxiv.org/abs/2410.05772v1)**  
  作者: Guoji Tian, Chongcheng Chen, Hongyu Huang  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.05772v1.pdf)  
  摘要: Accurate and efficient 3D reconstruction of trees is crucial for forest resource assessments and management. Close-Range Photogrammetry (CRP) is commonly used for reconstructing forest scenes but face...  
  关键词: gaussian splatting, 3d gaussian, 3d reconstruction, nerf  
- **[PH-Dropout: Practical Epistemic Uncertainty Quantification for View Synthesis](https://arxiv.org/abs/2410.05468v2)**  
  作者: Chuanhao Sun, Thanos Triantafyllou, Anthos Makris, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.05468v2.pdf)  
  摘要: View synthesis using Neural Radiance Fields (NeRF) and Gaussian Splatting (GS) has demonstrated impressive fidelity in rendering real-world scenarios. However, practical methods for accurate and effic...  
  关键词: gaussian splatting, nerf  
- **[GS-VTON: Controllable 3D Virtual Try-on with Gaussian Splatting](https://arxiv.org/abs/2410.05259v1)**  
  作者: Yukang Cao, Masoud Hadi, Liang Pan, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.05259v1.pdf)  
  摘要: Diffusion-based 2D virtual try-on (VTON) techniques have recently demonstrated strong performance, while the development of 3D VTON has largely lagged behind. Despite recent advances in text-guided 3D...  
  关键词: gaussian splatting, 3d gaussian  
- **[LiDAR-GS:Real-time LiDAR Re-Simulation using Gaussian Splatting](https://arxiv.org/abs/2410.05111v1)**  
  作者: Qifeng Chen, Sheng Yang, Sicong Du, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.05111v1.pdf)  
  摘要: LiDAR simulation plays a crucial role in closed-loop simulation for autonomous driving. Although recent advancements, such as the use of reconstructed mesh and Neural Radiance Fields (NeRF), have made...  
  关键词: gaussian splatting, nerf  
- **[DreamSat: Towards a General 3D Model for Novel View Synthesis of Space Objects](https://arxiv.org/abs/2410.05097v1)**  
  作者: Nidhi Mathihalli, Audrey Wei, Giovanni Lavezzi, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.05097v1.pdf) | [![Stars](https://img.shields.io/github/stars/ARCLab-MIT/space-nvs?style=social)](https://github.com/ARCLab-MIT/space-nvs)  
  摘要: Novel view synthesis (NVS) enables to generate new images of a scene or convert a set of 2D images into a comprehensive 3D model. In the context of Space Domain Awareness, since space is becoming incr...  
  关键词: gaussian splatting, 3d gaussian, 3d reconstruction  
- **[PhotoReg: Photometrically Registering 3D Gaussian Splatting Models](https://arxiv.org/abs/2410.05044v1)**  
  作者: Ziwen Yuan, Tianyi Zhang, Matthew Johnson-Roberson, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.05044v1.pdf)  
  摘要: Building accurate representations of the environment is critical for intelligent robots to make decisions during deployment. Advances in photorealistic environment models have enabled robots to develo...  
- **[6DGS: Enhanced Direction-Aware Gaussian Splatting for Volumetric Rendering](https://arxiv.org/abs/2410.04974v2)**  
  作者: Zhongpai Gao, Benjamin Planche, Meng Zheng, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.04974v2.pdf)  
  摘要: Novel view synthesis has advanced significantly with the development of neural radiance fields (NeRF) and 3D Gaussian splatting (3DGS). However, achieving high quality without compromising real-time r...  
  关键词: gaussian splatting, 3d gaussian, real-time rendering, nerf  
- **[Next Best Sense: Guiding Vision and Touch with FisherRF for 3D Gaussian Splatting](https://arxiv.org/abs/2410.04680v3)**  
  作者: Matthew Strong, Boshu Lei, Aiden Swann, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.04680v3.pdf)  
  摘要: We propose a framework for active next best view and touch selection for robotic manipulators using 3D Gaussian Splatting (3DGS). 3DGS is emerging as a useful explicit 3D scene representation for robo...  
  关键词: gaussian splatting, 3d gaussian  
- **[Mode-GS: Monocular Depth Guided Anchored 3D Gaussian Splatting for Robust Ground-View Scene Rendering](https://arxiv.org/abs/2410.04646v1)**  
  作者: Yonghan Lee, Jaehoon Choi, Dongki Jung, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.04646v1.pdf)  
  摘要: We present a novel-view rendering algorithm, Mode-GS, for ground-robot trajectory datasets. Our approach is based on using anchored Gaussian splats, which are designed to overcome the limitations of e...  
  关键词: gaussian splatting, 3d gaussian, neural rendering  
- **[StreetSurfGS: Scalable Urban Street Surface Reconstruction with Planar-based Gaussian Splatting](https://arxiv.org/abs/2410.04354v2)**  
  作者: Xiao Cui, Weicai Ye, Yifan Wang, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.04354v2.pdf)  
  摘要: Reconstructing urban street scenes is crucial due to its vital role in applications such as autonomous driving and urban planning. These scenes are characterized by long and narrow camera trajectories...  
  关键词: gaussian splatting  
- **[Variational Bayes Gaussian Splatting](https://arxiv.org/abs/2410.03592v1)**  
  作者: Toon Van de Maele, Ozan Catal, Alexander Tschantz, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.03592v1.pdf)  
  摘要: Recently, 3D Gaussian Splatting has emerged as a promising approach for modeling 3D scenes using mixtures of Gaussians. The predominant optimization method for these models relies on backpropagating g...  
  关键词: gaussian splatting, 3d gaussian  
- **[Flash-Splat: 3D Reflection Removal with Flash Cues and Gaussian Splats](https://arxiv.org/abs/2410.02764v1)**  
  作者: Mingyang Xie, Haoming Cai, Sachin Shah, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.02764v1.pdf)  
  摘要: We introduce a simple yet effective approach for separating transmitted and reflected light. Our key insight is that the powerful novel view synthesis capabilities provided by modern inverse rendering...  
  关键词: gaussian splatting, 3d gaussian  
- **[GI-GS: Global Illumination Decomposition on Gaussian Splatting for Inverse Rendering](https://arxiv.org/abs/2410.02619v1)**  
  作者: Hongze Chen, Zehong Lin, Jun Zhang  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.02619v1.pdf)  
  摘要: We present GI-GS, a novel inverse rendering framework that leverages 3D Gaussian Splatting (3DGS) and deferred shading to achieve photo-realistic novel view synthesis and relighting. In inverse render...  
  关键词: gaussian splatting, 3d gaussian  
- **[SuperGS: Super-Resolution 3D Gaussian Splatting via Latent Feature Field and Gradient-guided Splitting](https://arxiv.org/abs/2410.02571v2)**  
  作者: Shiyun Xie, Zhiru Wang, Yinghao Zhu, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.02571v2.pdf)  
  摘要: Recently, 3D Gaussian Splatting (3DGS) has exceled in novel view synthesis with its real-time rendering capabilities and superior quality. However, it faces challenges for high-resolution novel view s...  
  关键词: gaussian splatting, 3d gaussian, real-time rendering  
- **[MVGS: Multi-view-regulated Gaussian Splatting for Novel View Synthesis](https://arxiv.org/abs/2410.02103v1)**  
  作者: Xiaobiao Du, Yida Wang, Xin Yu  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.02103v1.pdf)  
  摘要: Recent works in volume rendering, \textit{e.g.} NeRF and 3D Gaussian Splatting (3DGS), significantly advance the rendering quality and efficiency with the help of the learned implicit neural radiance ...  
  关键词: gaussian splatting, 3d gaussian, nerf  
- **[EVER: Exact Volumetric Ellipsoid Rendering for Real-time View Synthesis](https://arxiv.org/abs/2410.01804v5)**  
  作者: Alexander Mai, Peter Hedman, George Kopanas, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.01804v5.pdf)  
  摘要: We present Exact Volumetric Ellipsoid Rendering (EVER), a method for real-time differentiable emission-only volume rendering. Unlike recent rasterization based approach by 3D Gaussian Splatting (3DGS)...  
  关键词: gaussian splatting, 3d gaussian, nerf  
- **[3DGS-DET: Empower 3D Gaussian Splatting with Boundary Guidance and Box-Focused Sampling for 3D Object Detection](https://arxiv.org/abs/2410.01647v1)**  
  作者: Yang Cao, Yuanliang Jv, Dan Xu  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.01647v1.pdf)  
  摘要: Neural Radiance Fields (NeRF) are widely used for novel-view synthesis and have been adapted for 3D Object Detection (3DOD), offering a promising approach to 3DOD through view-synthesis representation...  
  关键词: gaussian splatting, 3d gaussian, nerf  
- **[Gaussian Splatting in Mirrors: Reflection-Aware Rendering via Virtual Camera Optimization](https://arxiv.org/abs/2410.01614v1)**  
  作者: Zihan Wang, Shuzhe Wang, Matias Turkulainen, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.01614v1.pdf)  
  摘要: Recent advancements in 3D Gaussian Splatting (3D-GS) have revolutionized novel view synthesis, facilitating real-time, high-quality image rendering. However, in scenarios involving reflective surfaces...  
  关键词: gaussian splatting, 3d gaussian, nerf  
- **[GaussianBlock: Building Part-Aware Compositional and Editable 3D Scene by Primitives and Gaussians](https://arxiv.org/abs/2410.01535v2)**  
  作者: Shuyi Jiang, Qihao Zhao, Hossein Rahmani, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.01535v2.pdf)  
  摘要: Recently, with the development of Neural Radiance Fields and Gaussian Splatting, 3D reconstruction techniques have achieved remarkably high fidelity. However, the latent representations learnt by thes...  
  关键词: gaussian splatting, 3d gaussian, 3d reconstruction  
- **[MiraGe: Editable 2D Images using Gaussian Splatting](https://arxiv.org/abs/2410.01521v1)**  
  作者: Joanna Waczyńska, Tomasz Szczepanik, Piotr Borycki, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.01521v1.pdf)  
  摘要: Implicit Neural Representations (INRs) approximate discrete data through continuous functions and are commonly used for encoding 2D images. Traditional image-based INRs employ neural networks to map p...  
- **[UW-GS: Distractor-Aware 3D Gaussian Splatting for Enhanced Underwater Scene Reconstruction](https://arxiv.org/abs/2410.01517v1)**  
  作者: Haoran Wang, Nantheera Anantrasirichai, Fan Zhang, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.01517v1.pdf)  
  摘要: 3D Gaussian splatting (3DGS) offers the capability to achieve real-time high quality 3D scene rendering. However, 3DGS assumes that the scene is in a clear medium environment and struggles to generate...  
  关键词: gaussian splatting, 3d gaussian  
- **[EVA-Gaussian: 3D Gaussian-based Real-time Human Novel View Synthesis under Diverse Camera Settings](https://arxiv.org/abs/2410.01425v1)**  
  作者: Yingdong Hu, Zhening Liu, Jiawei Shao, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.01425v1.pdf)  
  摘要: The feed-forward based 3D Gaussian Splatting method has demonstrated exceptional capability in real-time human novel view synthesis. However, existing approaches are restricted to dense viewpoint sett...  
  关键词: gaussian splatting, 3d gaussian  
- **[Gaussian-Det: Learning Closed-Surface Gaussians for 3D Object Detection](https://arxiv.org/abs/2410.01404v1)**  
  作者: Hongru Yan, Yu Zheng, Yueqi Duan  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.01404v1.pdf)  
  摘要: Skins wrapping around our bodies, leathers covering over the sofa, sheet metal coating the car - it suggests that objects are enclosed by a series of continuous surfaces, which provides us with inform...  
  关键词: gaussian splatting, nerf  
- **[Flex3D: Feed-Forward 3D Generation With Flexible Reconstruction Model And Input View Curation](https://arxiv.org/abs/2410.00890v2)**  
  作者: Junlin Han, Jianyuan Wang, Andrea Vedaldi, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.00890v2.pdf)  
  摘要: Generating high-quality 3D content from text, single images, or sparse view images remains a challenging task with broad applications. Existing methods typically employ multi-view diffusion models to ...  
  关键词: 3d gaussian, 3d reconstruction  
- **[CaRtGS: Computational Alignment for Real-Time Gaussian Splatting SLAM](https://arxiv.org/abs/2410.00486v2)**  
  作者: Dapeng Feng, Zhiqiang Chen, Yizhen Yin, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.00486v2.pdf)  
  摘要: Simultaneous Localization and Mapping (SLAM) is pivotal in robotics, with photorealistic scene reconstruction emerging as a key challenge. To address this, we introduce Computational Alignment for Rea...  
  关键词: gaussian splatting, 3d gaussian  
- **[3DGR-CAR: Coronary artery reconstruction from ultra-sparse 2D X-ray views with a 3D Gaussians representation](https://arxiv.org/abs/2410.00404v1)**  
  作者: Xueming Fu, Yingtai Li, Fenghe Tang, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.00404v1.pdf) | [![Stars](https://img.shields.io/github/stars/windrise/3DGR-CAR?style=social)](https://github.com/windrise/3DGR-CAR)  
  摘要: Reconstructing 3D coronary arteries is important for coronary artery disease diagnosis, treatment planning and operation navigation. Traditional reconstruction techniques often require many projection...  
  关键词: 3d gaussian, 3d reconstruction  
- **[Seamless Augmented Reality Integration in Arthroscopy: A Pipeline for Articular Reconstruction and Guidance](https://arxiv.org/abs/2410.00386v1)**  
  作者: Hongchao Shu, Mingxu Liu, Lalithkumar Seenivasan, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.00386v1.pdf)  
  摘要: Arthroscopy is a minimally invasive surgical procedure used to diagnose and treat joint problems. The clinical workflow of arthroscopy typically involves inserting an arthroscope into the joint throug...  
  关键词: gaussian splatting, 3d gaussian, 3d reconstruction  
- **[GSPR: Multimodal Place Recognition Using 3D Gaussian Splatting for Autonomous Driving](https://arxiv.org/abs/2410.00299v1)**  
  作者: Zhangshuo Qi, Junyi Ma, Jingyi Xu, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.00299v1.pdf) | [![Stars](https://img.shields.io/github/stars/QiZS-BIT/GSPR?style=social)](https://github.com/QiZS-BIT/GSPR)  
  摘要: Place recognition is a crucial module to ensure autonomous vehicles obtain usable localization information in GPS-denied environments. In recent years, multimodal place recognition methods have gained...  
  关键词: gaussian splatting, 3d gaussian  

### 2024年09月
- **[DressRecon: Freeform 4D Human Reconstruction from Monocular Video](https://arxiv.org/abs/2409.20563v2)**  
  作者: Jeff Tan, Donglai Xiang, Shubham Tulsiani, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2409.20563v2.pdf)  
  摘要: We present a method to reconstruct time-consistent human body models from monocular videos, focusing on extremely loose clothing or handheld object interactions. Prior work in human reconstruction is ...  
  关键词: 3d gaussian, 3d reconstruction  
- **[RL-GSBridge: 3D Gaussian Splatting Based Real2Sim2Real Method for Robotic Manipulation Learning](https://arxiv.org/abs/2409.20291v1)**  
  作者: Yuxuan Wu, Lei Pan, Wenhua Wu, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2409.20291v1.pdf)  
  摘要: Sim-to-Real refers to the process of transferring policies learned in simulation to the real world, which is crucial for achieving practical robotics applications. However, recent Sim2real methods eit...  
  关键词: gaussian splatting, 3d gaussian  
- **[Robust Gaussian Splatting SLAM by Leveraging Loop Closure](https://arxiv.org/abs/2409.20111v1)**  
  作者: Zunjie Zhu, Youxu Fang, Xin Li, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2409.20111v1.pdf)  
  摘要: 3D Gaussian Splatting algorithms excel in novel view rendering applications and have been adapted to extend the capabilities of traditional SLAM systems. However, current Gaussian Splatting SLAM metho...  
  关键词: gaussian splatting, 3d gaussian  
- **[RNG: Relightable Neural Gaussians](https://arxiv.org/abs/2409.19702v4)**  
  作者: Jiahui Fan, Fujun Luan, Jian Yang, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2409.19702v4.pdf)  
  摘要: 3D Gaussian Splatting (3DGS) has shown impressive results for the novel view synthesis task, where lighting is assumed to be fixed. However, creating relightable 3D assets, especially for objects with...  
  关键词: gaussian splatting, 3d gaussian  
- **[G3R: Gradient Guided Generalizable Reconstruction](https://arxiv.org/abs/2409.19405v1)**  
  作者: Yun Chen, Jingkang Wang, Ze Yang, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2409.19405v1.pdf)  
  摘要: Large scale 3D scene reconstruction is important for applications such as virtual reality and simulation. Existing neural rendering approaches (e.g., NeRF, 3DGS) have achieved realistic reconstruction...  
  关键词: neural rendering, nerf  
- **[GS-EVT: Cross-Modal Event Camera Tracking based on Gaussian Splatting](https://arxiv.org/abs/2409.19228v1)**  
  作者: Tao Liu, Runze Yuan, Yi'ang Ju, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2409.19228v1.pdf)  
  摘要: Reliable self-localization is a foundational skill for many intelligent mobile platforms. This paper explores the use of event cameras for motion tracking thereby providing a solution with inherent ro...  
  关键词: gaussian splatting  
- **[1st Place Solution to the 8th HANDS Workshop Challenge -- ARCTIC Track: 3DGS-based Bimanual Category-agnostic Interaction Reconstruction](https://arxiv.org/abs/2409.19215v2)**  
  作者: Jeongwan On, Kyeonghwan Gwak, Gunyoung Kang, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2409.19215v2.pdf)  
  摘要: This report describes our 1st place solution to the 8th HANDS workshop challenge (ARCTIC track) in conjunction with ECCV 2024. In this challenge, we address the task of bimanual category-agnostic hand...  
  关键词: gaussian splatting, 3d gaussian, 3d reconstruction  
- **[Space-time 2D Gaussian Splatting for Accurate Surface Reconstruction under Complex Dynamic Scenes](https://arxiv.org/abs/2409.18852v1)**  
  作者: Shuo Wang, Binbin Huang, Ruoyu Wang, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2409.18852v1.pdf)  
  摘要: Previous surface reconstruction methods either suffer from low geometric accuracy or lengthy training times when dealing with real-world complex dynamic scenes involving multi-person activities, and h...  
  关键词: gaussian splatting  
- **[Gaussian Heritage: 3D Digitization of Cultural Heritage with Integrated Object Segmentation](https://arxiv.org/abs/2409.19039v1)**  
  作者: Mahtab Dahaghin, Myrna Castillo, Kourosh Riahidehkordi, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2409.19039v1.pdf)  
  摘要: The creation of digital replicas of physical objects has valuable applications for the preservation and dissemination of tangible cultural heritage. However, existing methods are often slow, expensive...  
  关键词: gaussian splatting  
- **[RT-GuIDE: Real-Time Gaussian splatting for Information-Driven Exploration](https://arxiv.org/abs/2409.18122v1)**  
  作者: Yuezhan Tao, Dexter Ong, Varun Murali, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2409.18122v1.pdf)  
  摘要: We propose a framework for active mapping and exploration that leverages Gaussian splatting for constructing information-rich maps. Further, we develop a parallelized motion planning algorithm that ca...  
  关键词: gaussian splatting  
- **[Language-Embedded Gaussian Splats (LEGS): Incrementally Building Room-Scale Representations with a Mobile Robot](https://arxiv.org/abs/2409.18108v1)**  
  作者: Justin Yu, Kush Hari, Kishore Srinivas, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2409.18108v1.pdf)  
  摘要: Building semantic 3D maps is valuable for searching for objects of interest in offices, warehouses, stores, and homes. We present a mapping system that incrementally builds a Language-Embedded Gaussia...  
- **[WaSt-3D: Wasserstein-2 Distance for Scene-to-Scene Stylization on 3D Gaussians](https://arxiv.org/abs/2409.17917v1)**  
  作者: Dmytro Kotovenko, Olga Grebenkova, Nikolaos Sarafianos, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2409.17917v1.pdf)  
  摘要: While style transfer techniques have been well-developed for 2D image stylization, the extension of these methods to 3D scenes remains relatively unexplored. Existing approaches demonstrate proficienc...  
  关键词: gaussian splatting  
- **[HGS-Planner: Hierarchical Planning Framework for Active Scene Reconstruction Using 3D Gaussian Splatting](https://arxiv.org/abs/2409.17624v2)**  
  作者: Zijun Xu, Rui Jin, Ke Wu, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2409.17624v2.pdf)  
  摘要: In complex missions such as search and rescue,robots must make intelligent decisions in unknown environments, relying on their ability to perceive and understand their surroundings. High-quality and r...  
  关键词: gaussian splatting, 3d gaussian  
- **[SeaSplat: Representing Underwater Scenes with 3D Gaussian Splatting and a Physically Grounded Image Formation Model](https://arxiv.org/abs/2409.17345v1)**  
  作者: Daniel Yang, John J. Leonard, Yogesh Girdhar  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2409.17345v1.pdf)  
  摘要: We introduce SeaSplat, a method to enable real-time rendering of underwater scenes leveraging recent advances in 3D radiance fields. Underwater scenes are challenging visual environments, as rendering...  
  关键词: gaussian splatting, 3d gaussian, real-time rendering, nerf  
- **[Disco4D: Disentangled 4D Human Generation and Animation from a Single Image](https://arxiv.org/abs/2409.17280v1)**  
  作者: Hui En Pang, Shuai Liu, Zhongang Cai, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2409.17280v1.pdf)  
  摘要: We present \textbf{Disco4D}, a novel Gaussian Splatting framework for 4D human generation and animation from a single image. Different from existing methods, Disco4D distinctively disentangles clothin...  
  关键词: gaussian splatting  
- **[DreamWaltz-G: Expressive 3D Gaussian Avatars from Skeleton-Guided 2D Diffusion](https://arxiv.org/abs/2409.17145v1)**  
  作者: Yukun Huang, Jianan Wang, Ailing Zeng, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2409.17145v1.pdf)  
  摘要: Leveraging pretrained 2D diffusion models and score distillation sampling (SDS), recent methods have shown promising results for text-to-3D avatar generation. However, generating high-quality 3D avata...  
  关键词: 3d gaussian, real-time rendering  
- **[Go-SLAM: Grounded Object Segmentation and Localization with Gaussian Splatting SLAM](https://arxiv.org/abs/2409.16944v1)**  
  作者: Phu Pham, Dipam Patel, Damon Conover, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2409.16944v1.pdf)  
  摘要: We introduce Go-SLAM, a novel framework that utilizes 3D Gaussian Splatting SLAM to reconstruct dynamic environments while embedding object-level information within the scene representations. This fra...  
  关键词: gaussian splatting, 3d gaussian  
- **[Generative Object Insertion in Gaussian Splatting with a Multi-View Diffusion Model](https://arxiv.org/abs/2409.16938v1)**  
  作者: Hongliang Zhong, Can Wang, Jingbo Zhang, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2409.16938v1.pdf)  
  摘要: Generating and inserting new objects into 3D content is a compelling approach for achieving versatile scene recreation. Existing methods, which rely on SDS optimization or single-view inpainting, ofte...  
  关键词: gaussian splatting, 3d reconstruction  
- **[Let's Make a Splan: Risk-Aware Trajectory Optimization in a Normalized Gaussian Splat](https://arxiv.org/abs/2409.16915v1)**  
  作者: Jonathan Michaux, Seth Isaacson, Challen Enninful Adu, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2409.16915v1.pdf)  
  摘要: Neural Radiance Fields and Gaussian Splatting have transformed the field of computer vision by enabling photo-realistic representation of complex scenes. Despite this success, they have seen only limi...  
  关键词: gaussian splatting  
- **[Towards Unified 3D Hair Reconstruction from Single-View Portraits](https://arxiv.org/abs/2409.16863v1)**  
  作者: Yujian Zheng, Yuda Qiu, Leyang Jin, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2409.16863v1.pdf)  
  摘要: Single-view 3D hair reconstruction is challenging, due to the wide range of shape variations among diverse hairstyles. Current state-of-the-art methods are specialized in recovering un-braided 3D hair...  
  关键词: 3d gaussian, 3d reconstruction  
- **[GSplatLoc: Grounding Keypoint Descriptors into 3D Gaussian Splatting for Improved Visual Localization](https://arxiv.org/abs/2409.16502v1)**  
  作者: Gennady Sidorov, Malik Mohrat, Ksenia Lebedeva, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2409.16502v1.pdf)  
  摘要: Although various visual localization approaches exist, such as scene coordinate and pose regression, these methods often struggle with high memory consumption or extensive optimization requirements. T...  
  关键词: gaussian splatting, 3d gaussian, nerf  
- **[Frequency-based View Selection in Gaussian Splatting Reconstruction](https://arxiv.org/abs/2409.16470v1)**  
  作者: Monica M. Q. Li, Pierre-Yves Lajoie, Giovanni Beltrame  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2409.16470v1.pdf)  
  摘要: Three-dimensional reconstruction is a fundamental problem in robotics perception. We examine the problem of active view selection to perform 3D Gaussian Splatting reconstructions with as few input ima...  
  关键词: gaussian splatting, 3d gaussian, 3d reconstruction  
- **[AIR-Embodied: An Efficient Active 3DGS-based Interaction and Reconstruction Framework with Embodied Large Language Model](https://arxiv.org/abs/2409.16019v1)**  
  作者: Zhenghao Qi, Shenghai Yuan, Fen Liu, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2409.16019v1.pdf)  
  摘要: Recent advancements in 3D reconstruction and neural rendering have enhanced the creation of high-quality digital assets, yet existing methods struggle to generalize across varying object shapes, textu...  
  关键词: neural rendering, 3d reconstruction  
- **[Semantics-Controlled Gaussian Splatting for Outdoor Scene Reconstruction and Rendering in Virtual Reality](https://arxiv.org/abs/2409.15959v1)**  
  作者: Hannah Schieber, Jacob Young, Tobias Langlotz, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2409.15959v1.pdf)  
  摘要: Advancements in 3D rendering like Gaussian Splatting (GS) allow novel view synthesis and real-time rendering in virtual reality (VR). However, GS-created 3D environments are often difficult to edit. F...  
  关键词: gaussian splatting, real-time rendering  
- **[Plenoptic PNG: Real-Time Neural Radiance Fields in 150 KB](https://arxiv.org/abs/2409.15689v1)**  
  作者: Jae Yong Lee, Yuqun Wu, Chuhang Zou, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2409.15689v1.pdf)  
  摘要: The goal of this paper is to encode a 3D scene into an extremely compact representation from 2D images and to enable its transmittance, decoding and rendering in real-time across various platforms. De...  
  关键词: real-time rendering, nerf  
- **[SpikeGS: Learning 3D Gaussian Fields from Continuous Spike Stream](https://arxiv.org/abs/2409.15176v5)**  
  作者: Jinze Yu, Xin Peng, Zhengda Lu, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2409.15176v5.pdf) | [![Stars](https://img.shields.io/github/stars/520jz/SpikeGS?style=social)](https://github.com/520jz/SpikeGS)  
  摘要: A spike camera is a specialized high-speed visual sensor that offers advantages such as high temporal resolution and high dynamic range compared to conventional frame cameras. These features provide t...  
  关键词: 3d gaussian, real-time rendering  
- **[TextToon: Real-Time Text Toonify Head Avatar from Single Video](https://arxiv.org/abs/2410.07160v1)**  
  作者: Luchuan Song, Lele Chen, Celong Liu, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2410.07160v1.pdf)  
  摘要: We propose TextToon, a method to generate a drivable toonified avatar. Given a short monocular video sequence and a written instruction about the avatar style, our model can generate a high-fidelity t...  
  关键词: gaussian splatting, 3d gaussian  
- **[Human Hair Reconstruction with Strand-Aligned 3D Gaussians](https://arxiv.org/abs/2409.14778v1)**  
  作者: Egor Zakharov, Vanessa Sklyarova, Michael Black, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2409.14778v1.pdf)  
  摘要: We introduce a new hair modeling method that uses a dual representation of classical hair strands and 3D Gaussians to produce accurate and realistic strand-based reconstructions from multi-view data. ...  
  关键词: gaussian splatting, 3d gaussian  
- **[Gaussian Deja-vu: Creating Controllable 3D Gaussian Head-Avatars with Enhanced Generalization and Personalization Abilities](https://arxiv.org/abs/2409.16147v3)**  
  作者: Peizhi Yan, Rabab Ward, Qiang Tang, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2409.16147v3.pdf)  
  摘要: Recent advancements in 3D Gaussian Splatting (3DGS) have unlocked significant potential for modeling 3D head avatars, providing greater flexibility than mesh-based methods and more efficient rendering...  
  关键词: gaussian splatting, 3d gaussian, nerf  
- **[MVPGS: Excavating Multi-view Priors for Gaussian Splatting from Sparse Input Views](https://arxiv.org/abs/2409.14316v1)**  
  作者: Wangze Xu, Huachen Gao, Shihe Shen, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2409.14316v1.pdf)  
  摘要: Recently, the Neural Radiance Field (NeRF) advancement has facilitated few-shot Novel View Synthesis (NVS), which is a significant challenge in 3D vision applications. Despite numerous attempts to red...  
  关键词: gaussian splatting, 3d gaussian, real-time rendering, nerf  
- **[SplatLoc: 3D Gaussian Splatting-based Visual Localization for Augmented Reality](https://arxiv.org/abs/2409.14067v1)**  
  作者: Hongjia Zhai, Xiyu Zhang, Boming Zhao, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2409.14067v1.pdf)  
  摘要: Visual localization plays an important role in the applications of Augmented Reality (AR), which enable AR devices to obtain their 6-DoF pose in the pre-build map in order to render virtual content in...  
  关键词: 3d gaussian  
- **[V^3: Viewing Volumetric Videos on Mobiles via Streamable 2D Dynamic Gaussians](https://arxiv.org/abs/2409.13648v2)**  
  作者: Penghao Wang, Zhirui Zhang, Liao Wang, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2409.13648v2.pdf)  
  摘要: Experiencing high-fidelity volumetric video as seamlessly as 2D videos is a long-held dream. However, current dynamic 3DGS methods, despite their high rendering quality, face challenges in streaming o...  
- **[Portrait Video Editing Empowered by Multimodal Generative Priors](https://arxiv.org/abs/2409.13591v1)**  
  作者: Xuan Gao, Haiyao Xiao, Chenglai Zhong, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2409.13591v1.pdf)  
  摘要: We introduce PortraitGen, a powerful portrait video editing method that achieves consistent and expressive stylization with multimodal prompts. Traditional portrait video editing methods often struggl...  
  关键词: 3d gaussian  
- **[Elite-EvGS: Learning Event-based 3D Gaussian Splatting by Distilling Event-to-Video Priors](https://arxiv.org/abs/2409.13392v1)**  
  作者: Zixin Zhang, Kanghao Chen, Lin Wang  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2409.13392v1.pdf)  
  摘要: Event cameras are bio-inspired sensors that output asynchronous and sparse event streams, instead of fixed frames. Benefiting from their distinct advantages, such as high dynamic range and high tempor...  
  关键词: gaussian splatting, 3d gaussian, neural rendering, 3d reconstruction  
- **[3D-GSW: 3D Gaussian Splatting for Robust Watermarking](https://arxiv.org/abs/2409.13222v2)**  
  作者: Youngdong Jang, Hyunje Park, Feng Yang, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2409.13222v2.pdf)  
  摘要: As 3D Gaussian Splatting (3D-GS) gains significant attention and its commercial usage increases, the need for watermarking technologies to prevent unauthorized use of the 3D-GS models and rendered ima...  
  关键词: gaussian splatting, 3d gaussian, real-time rendering  
- **[MGSO: Monocular Real-time Photometric SLAM with Efficient 3D Gaussian Splatting](https://arxiv.org/abs/2409.13055v1)**  
  作者: Yan Song Hu, Nicolas Abboud, Muhammad Qasim Ali, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2409.13055v1.pdf)  
  摘要: Real-time SLAM with dense 3D mapping is computationally challenging, especially on resource-limited devices. The recent development of 3D Gaussian Splatting (3DGS) offers a promising approach for real...  
  关键词: gaussian splatting, 3d gaussian, 3d reconstruction  
- **[GStex: Per-Primitive Texturing of 2D Gaussian Splatting for Decoupled Appearance and Geometry Modeling](https://arxiv.org/abs/2409.12954v2)**  
  作者: Victor Rong, Jingxiang Chen, Sherwin Bahmani, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2409.12954v2.pdf)  
  摘要: Gaussian splatting has demonstrated excellent performance for view synthesis and scene reconstruction. The representation achieves photorealistic quality by optimizing the position, scale, color, and ...  
  关键词: gaussian splatting, 3d gaussian  
- **[LI-GS: Gaussian Splatting with LiDAR Incorporated for Accurate Large-Scale Reconstruction](https://arxiv.org/abs/2409.12899v1)**  
  作者: Changjian Jiang, Ruilan Gao, Kele Shao, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2409.12899v1.pdf)  
  摘要: Large-scale 3D reconstruction is critical in the field of robotics, and the potential of 3D Gaussian Splatting (3DGS) for achieving accurate object-level reconstruction has been demonstrated. However,...  
  关键词: gaussian splatting, 3d gaussian, 3d reconstruction  
- **[3DGS-LM: Faster Gaussian-Splatting Optimization with Levenberg-Marquardt](https://arxiv.org/abs/2409.12892v1)**  
  作者: Lukas Höllein, Aljaž Božič, Michael Zollhöfer, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2409.12892v1.pdf)  
  摘要: We present 3DGS-LM, a new method that accelerates the reconstruction of 3D Gaussian Splatting (3DGS) by replacing its ADAM optimizer with a tailored Levenberg-Marquardt (LM). Existing methods reduce t...  
  关键词: gaussian splatting, 3d gaussian  
- **[EdgeGaussians -- 3D Edge Mapping via Gaussian Splatting](https://arxiv.org/abs/2409.12886v1)**  
  作者: Kunal Chelani, Assia Benbihi, Torsten Sattler, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2409.12886v1.pdf) | [![Stars](https://img.shields.io/github/stars/kunalchelani/EdgeGaussians?style=social)](https://github.com/kunalchelani/EdgeGaussians)  
  摘要: With their meaningful geometry and their omnipresence in the 3D world, edges are extremely useful primitives in computer vision. 3D edges comprise of lines and curves, and methods to reconstruct them ...  
  关键词: gaussian splatting, 3d gaussian  
- **[GaRField++: Reinforced Gaussian Radiance Fields for Large-Scale 3D Scene Reconstruction](https://arxiv.org/abs/2409.12774v3)**  
  作者: Hanyue Zhang, Zhiliu Yang, Xinhe Zuo, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2409.12774v3.pdf)  
  摘要: This paper proposes a novel framework for large-scale scene reconstruction based on 3D Gaussian splatting (3DGS) and aims to address the scalability and accuracy challenges faced by existing methods. ...  
  关键词: gaussian splatting, 3d gaussian  
- **[Spectral-GS: Taming 3D Gaussian Splatting with Spectral Entropy](https://arxiv.org/abs/2409.12771v2)**  
  作者: Letian Huang, Jie Guo, Jialin Dan, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2409.12771v2.pdf)  
  摘要: Recently, 3D Gaussian Splatting (3D-GS) has achieved impressive results in novel view synthesis, demonstrating high fidelity and efficiency. However, it easily exhibits needle-like artifacts, especial...  
  关键词: gaussian splatting, 3d gaussian  
- **[DrivingForward: Feed-forward 3D Gaussian Splatting for Driving Scene Reconstruction from Flexible Surround-view Input](https://arxiv.org/abs/2409.12753v1)**  
  作者: Qijian Tian, Xin Tan, Yuan Xie, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2409.12753v1.pdf)  
  摘要: We propose DrivingForward, a feed-forward Gaussian Splatting model that reconstructs driving scenes from flexible surround-view input. Driving scene images from vehicle-mounted cameras are typically s...  
  关键词: gaussian splatting  
- **[CrossRT: A cross platform programming technology for hardware-accelerated ray tracing in CG and CV applications](https://arxiv.org/abs/2409.12617v1)**  
  作者: Vladimir Frolov, Vadim Sanzharov, Garifullin Albert, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2409.12617v1.pdf)  
  摘要: We propose a programming technology that bridges cross-platform compatibility and hardware acceleration in ray tracing applications. Our methodology enables developers to define algorithms while our t...  
  关键词: gaussian splatting, 3d gaussian, nerf  
- **[Hi-SLAM: Scaling-up Semantics in SLAM with a Hierarchically Categorical Gaussian Splatting](https://arxiv.org/abs/2409.12518v2)**  
  作者: Boying Li, Zhixi Cai, Yuan-Fang Li, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2409.12518v2.pdf)  
  摘要: We propose Hi-SLAM, a semantic 3D Gaussian Splatting SLAM method featuring a novel hierarchical categorical representation, which enables accurate global 3D semantic mapping, scaling-up capability, an...  
  关键词: gaussian splatting, 3d gaussian  
- **[Depth Estimation Based on 3D Gaussian Splatting Siamese Defocus](https://arxiv.org/abs/2409.12323v1)**  
  作者: Jinchang Zhang, Ningning Xu, Hao Zhang, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2409.12323v1.pdf)  
  摘要: Depth estimation is a fundamental task in 3D geometry. While stereo depth estimation can be achieved through triangulation methods, it is not as straightforward for monocular methods, which require th...  
  关键词: gaussian splatting, 3d gaussian  
- **[Vista3D: Unravel the 3D Darkside of a Single Image](https://arxiv.org/abs/2409.12193v1)**  
  作者: Qiuhong Shen, Xingyi Yang, Michael Bi Mi, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2409.12193v1.pdf) | [![Stars](https://img.shields.io/github/stars/florinshen/Vista3D?style=social)](https://github.com/florinshen/Vista3D)  
  摘要: We embark on the age-old quest: unveiling the hidden dimensions of objects from mere glimpses of their visible parts. To address this, we present Vista3D, a framework that realizes swift and consisten...  
  关键词: gaussian splatting  
- **[GaussianHeads: End-to-End Learning of Drivable Gaussian Head Avatars from Coarse-to-fine Representations](https://arxiv.org/abs/2409.11951v1)**  
  作者: Kartik Teotia, Hyeongwoo Kim, Pablo Garrido, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2409.11951v1.pdf)  
  摘要: Real-time rendering of human head avatars is a cornerstone of many computer graphics applications, such as augmented reality, video games, and films, to name a few. Recent approaches address this chal...  
  关键词: 3d gaussian, real-time rendering  
- **[SRIF: Semantic Shape Registration Empowered by Diffusion-based Image Morphing and Flow Estimation](https://arxiv.org/abs/2409.11682v2)**  
  作者: Mingze Sun, Chen Guo, Puhua Jiang, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2409.11682v2.pdf) | [![Stars](https://img.shields.io/github/stars/rqhuang88/SRIF?style=social)](https://github.com/rqhuang88/SRIF)  
  摘要: In this paper, we propose SRIF, a novel Semantic shape Registration framework based on diffusion-based Image morphing and Flow estimation. More concretely, given a pair of extrinsically aligned shapes...  
  关键词: gaussian splatting, 3d gaussian  
- **[Gradient-Driven 3D Segmentation and Affordance Transfer in Gaussian Splatting Using 2D Masks](https://arxiv.org/abs/2409.11681v1)**  
  作者: Joji Joseph, Bharadwaj Amrutur, Shalabh Bhatnagar  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2409.11681v1.pdf)  
  摘要: 3D Gaussian Splatting has emerged as a powerful 3D scene representation technique, capturing fine details with high efficiency. In this paper, we introduce a novel voting-based method that extends 2D ...  
  关键词: gaussian splatting, 3d gaussian  
- **[RenderWorld: World Model with Self-Supervised 3D Label](https://arxiv.org/abs/2409.11356v1)**  
  作者: Ziyang Yan, Wenzhen Dong, Yihua Shao, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2409.11356v1.pdf)  
  摘要: End-to-end autonomous driving with vision-only is not only more cost-effective compared to LiDAR-vision fusion but also more reliable than traditional methods. To achieve a economical and robust purel...  
  关键词: gaussian splatting, nerf  
- **[GS-Net: Generalizable Plug-and-Play 3D Gaussian Splatting Module](https://arxiv.org/abs/2409.11307v1)**  
  作者: Yichen Zhang, Zihan Wang, Jiali Han, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2409.11307v1.pdf)  
  摘要: 3D Gaussian Splatting (3DGS) integrates the strengths of primitive-based representations and volumetric rendering techniques, enabling real-time, high-quality rendering. However, 3DGS models typically...  
  关键词: gaussian splatting, 3d gaussian  
- **[SplatFields: Neural Gaussian Splats for Sparse 3D and 4D Reconstruction](https://arxiv.org/abs/2409.11211v1)**  
  作者: Marko Mihajlovic, Sergey Prokudin, Siyu Tang, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2409.11211v1.pdf)  
  摘要: Digitizing 3D static scenes and 4D dynamic events from multi-view images has long been a challenge in computer vision and graphics. Recently, 3D Gaussian Splatting (3DGS) has emerged as a practical an...  
  关键词: gaussian splatting, 3d gaussian, real-time rendering  
- **[GLC-SLAM: Gaussian Splatting SLAM with Efficient Loop Closure](https://arxiv.org/abs/2409.10982v1)**  
  作者: Ziheng Xu, Qingfeng Li, Chen Chen, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2409.10982v1.pdf)  
  摘要: 3D Gaussian Splatting (3DGS) has gained significant attention for its application in dense Simultaneous Localization and Mapping (SLAM), enabling real-time rendering and high-fidelity mapping. However...  
  关键词: gaussian splatting, 3d gaussian, real-time rendering  
- **[HGSLoc: 3DGS-based Heuristic Camera Pose Refinement](https://arxiv.org/abs/2409.10925v2)**  
  作者: Zhongyan Niu, Zhen Tan, Jinpu Zhang, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2409.10925v2.pdf)  
  摘要: Visual localization refers to the process of determining camera poses and orientation within a known scene representation. This task is often complicated by factors such as illumination changes and va...  
  关键词: neural rendering, 3d reconstruction, nerf  
- **[Phys3DGS: Physically-based 3D Gaussian Splatting for Inverse Rendering](https://arxiv.org/abs/2409.10335v1)**  
  作者: Euntae Choi, Sungjoo Yoo  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2409.10335v1.pdf)  
  摘要: We propose two novel ideas (adoption of deferred rendering and mesh-based representation) to improve the quality of 3D Gaussian splatting (3DGS) based inverse rendering. We first report a problem incu...  
  关键词: gaussian splatting, 3d gaussian, real-time rendering  
- **[BEINGS: Bayesian Embodied Image-goal Navigation with Gaussian Splatting](https://arxiv.org/abs/2409.10216v1)**  
  作者: Wugang Meng, Tianfu Wu, Huan Yin, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2409.10216v1.pdf)  
  摘要: Image-goal navigation enables a robot to reach the location where a target image was captured, using visual cues for guidance. However, current methods either rely heavily on data and computationally ...  
  关键词: gaussian splatting, 3d gaussian  
- **[SplatSim: Zero-Shot Sim2Real Transfer of RGB Manipulation Policies Using Gaussian Splatting](https://arxiv.org/abs/2409.10161v3)**  
  作者: Mohammad Nomaan Qureshi, Sparsh Garg, Francisco Yandun, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2409.10161v3.pdf)  
  摘要: Sim2Real transfer, particularly for manipulation policies relying on RGB images, remains a critical challenge in robotics due to the significant domain shift between synthetic and real-world visual da...  
  关键词: gaussian splatting  
- **[Adaptive Segmentation-Based Initialization for Steered Mixture of Experts Image Regression](https://arxiv.org/abs/2409.10101v1)**  
  作者: Yi-Hsin Li, Sebastian Knorr, Mårten Sjöström, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2409.10101v1.pdf)  
  摘要: Kernel image regression methods have shown to provide excellent efficiency in many image processing task, such as image and light-field compression, Gaussian Splatting, denoising and super-resolution....  
  关键词: gaussian splatting  
- **[DENSER: 3D Gaussians Splatting for Scene Reconstruction of Dynamic Urban Environments](https://arxiv.org/abs/2409.10041v1)**  
  作者: Mahmud A. Mohamad, Gamal Elghazaly, Arthur Hubert, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2409.10041v1.pdf) | [![Stars](https://img.shields.io/github/stars/sntubix/denser?style=social)](https://github.com/sntubix/denser)  
  摘要: This paper presents DENSER, an efficient and effective approach leveraging 3D Gaussian splatting (3DGS) for the reconstruction of dynamic urban environments. While several methods for photorealistic s...  
  关键词: gaussian splatting, 3d gaussian, nerf  
- **[SAFER-Splat: A Control Barrier Function for Safe Navigation with Online Gaussian Splatting Maps](https://arxiv.org/abs/2409.09868v1)**  
  作者: Timothy Chen, Aiden Swann, Javier Yu, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2409.09868v1.pdf)  
  摘要: SAFER-Splat (Simultaneous Action Filtering and Environment Reconstruction) is a real-time, scalable, and minimally invasive action filter, based on control barrier functions, for safe robotic navigati...  
  关键词: gaussian splatting  
- **[MesonGS: Post-training Compression of 3D Gaussians via Efficient Attribute Transformation](https://arxiv.org/abs/2409.09756v1)**  
  作者: Shuzhao Xie, Weixiang Zhang, Chen Tang, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2409.09756v1.pdf)  
  摘要: 3D Gaussian Splatting demonstrates excellent quality and speed in novel view synthesis. Nevertheless, the huge file size of the 3D Gaussians presents challenges for transmission and storage. Current w...  
  关键词: gaussian splatting, 3d gaussian  
- **[GEVO: Memory-Efficient Monocular Visual Odometry Using Gaussians](https://arxiv.org/abs/2409.09295v1)**  
  作者: Dasong Gao, Peter Zhi Xuan Li, Vivienne Sze, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2409.09295v1.pdf)  
  摘要: Constructing a high-fidelity representation of the 3D scene using a monocular camera can enable a wide range of applications on mobile devices, such as micro-robots, smartphones, and AR/VR headsets. O...  
  关键词: gaussian splatting  
- **[A Diffusion Approach to Radiance Field Relighting using Multi-Illumination Synthesis](https://arxiv.org/abs/2409.08947v2)**  
  作者: Yohan Poirier-Ginter, Alban Gauthier, Julien Philip, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2409.08947v2.pdf)  
  摘要: Relighting radiance fields is severely underconstrained for multi-view data, which is most often captured under a single illumination condition; It is especially hard for full scenes containing multip...  
  关键词: 3d gaussian  
- **[AdR-Gaussian: Accelerating Gaussian Splatting with Adaptive Radius](https://arxiv.org/abs/2409.08669v1)**  
  作者: Xinzhe Wang, Ran Yi, Lizhuang Ma  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2409.08669v1.pdf)  
  摘要: 3D Gaussian Splatting (3DGS) is a recent explicit 3D representation that has achieved high-quality reconstruction and real-time rendering of complex scenes. However, the rasterization pipeline still s...  
  关键词: gaussian splatting, 3d gaussian, real-time rendering  
- **[Dense Point Clouds Matter: Dust-GS for Scene Reconstruction from Sparse Viewpoints](https://arxiv.org/abs/2409.08613v1)**  
  作者: Shan Chen, Jiale Zhou, Lei Li  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2409.08613v1.pdf)  
  摘要: 3D Gaussian Splatting (3DGS) has demonstrated remarkable performance in scene synthesis and novel view synthesis tasks. Typically, the initialization of 3D Gaussian primitives relies on point clouds d...  
  关键词: gaussian splatting, 3d gaussian  
- **[CSS: Overcoming Pose and Scene Challenges in Crowd-Sourced 3D Gaussian Splatting](https://arxiv.org/abs/2409.08562v1)**  
  作者: Runze Chen, Mingyu Xiao, Haiyong Luo, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2409.08562v1.pdf)  
  摘要: We introduce Crowd-Sourced Splatting (CSS), a novel 3D Gaussian Splatting (3DGS) pipeline designed to overcome the challenges of pose-free scene reconstruction using crowd-sourced imagery. The dream o...  
  关键词: gaussian splatting, 3d gaussian, 3d reconstruction  
- **[Robust Dual Gaussian Splatting for Immersive Human-centric Volumetric Videos](https://arxiv.org/abs/2409.08353v1)**  
  作者: Yuheng Jiang, Zhehao Shen, Yu Hong, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2409.08353v1.pdf)  
  摘要: Volumetric video represents a transformative advancement in visual media, enabling users to freely navigate immersive virtual experiences and narrowing the gap between digital and real worlds. However...  
- **[FlashSplat: 2D to 3D Gaussian Splatting Segmentation Solved Optimally](https://arxiv.org/abs/2409.08270v1)**  
  作者: Qiuhong Shen, Xingyi Yang, Xinchao Wang  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2409.08270v1.pdf) | [![Stars](https://img.shields.io/github/stars/florinshen/FlashSplat?style=social)](https://github.com/florinshen/FlashSplat)  
  摘要: This study addresses the challenge of accurately segmenting 3D Gaussian Splatting from 2D masks. Conventional methods often rely on iterative gradient descent to assign each Gaussian a unique label, l...  
  关键词: gaussian splatting, 3d gaussian  
- **[Thermal3D-GS: Physics-induced 3D Gaussians for Thermal Infrared Novel-view Synthesis](https://arxiv.org/abs/2409.08042v1)**  
  作者: Qian Chen, Shihao Shu, Xiangzhi Bai  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2409.08042v1.pdf) | [![Stars](https://img.shields.io/github/stars/mzzcdf/Thermal3DGS?style=social)](https://github.com/mzzcdf/Thermal3DGS)  
  摘要: Novel-view synthesis based on visible light has been extensively studied. In comparison to visible light imaging, thermal infrared imaging offers the advantage of all-weather imaging and strong penetr...  
  关键词: gaussian splatting, 3d gaussian  
- **[SwinGS: Sliding Window Gaussian Splatting for Volumetric Video Streaming with Arbitrary Length](https://arxiv.org/abs/2409.07759v1)**  
  作者: Bangya Liu, Suman Banerjee  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2409.07759v1.pdf)  
  摘要: Recent advances in 3D Gaussian Splatting (3DGS) have garnered significant attention in computer vision and computer graphics due to its high rendering speed and remarkable quality. While extant resear...  
  关键词: gaussian splatting, 3d gaussian  
- **[Self-Evolving Depth-Supervised 3D Gaussian Splatting from Rendered Stereo Pairs](https://arxiv.org/abs/2409.07456v1)**  
  作者: Sadra Safadoust, Fabio Tosi, Fatma Güney, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2409.07456v1.pdf)  
  摘要: 3D Gaussian Splatting (GS) significantly struggles to accurately represent the underlying 3D scene geometry, resulting in inaccuracies and floating artifacts when rendering depth maps. In this paper, ...  
  关键词: gaussian splatting, 3d gaussian  
- **[Hi3D: Pursuing High-Resolution Image-to-3D Generation with Video Diffusion Models](https://arxiv.org/abs/2409.07452v1)**  
  作者: Haibo Yang, Yang Chen, Yingwei Pan, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2409.07452v1.pdf) | [![Stars](https://img.shields.io/github/stars/yanghb22-fdu/Hi3D-Official?style=social)](https://github.com/yanghb22-fdu/Hi3D-Official)  
  摘要: Despite having tremendous progress in image-to-3D generation, existing methods still struggle to produce multi-view consistent images with high-resolution textures in detail, especially in the paradig...  
  关键词: gaussian splatting, 3d gaussian, 3d reconstruction  
- **[Instant Facial Gaussians Translator for Relightable and Interactable Facial Rendering](https://arxiv.org/abs/2409.07441v2)**  
  作者: Dafei Qin, Hongyang Lin, Qixuan Zhang, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2409.07441v2.pdf)  
  摘要: We propose GauFace, a novel Gaussian Splatting representation, tailored for efficient animation and rendering of physically-based facial assets. Leveraging strong geometric priors and constrained opti...  
  关键词: gaussian splatting, neural rendering  
- **[Single-View 3D Reconstruction via SO(2)-Equivariant Gaussian Sculpting Networks](https://arxiv.org/abs/2409.07245v1)**  
  作者: Ruihan Xu, Anthony Opipari, Joshua Mah, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2409.07245v1.pdf)  
  摘要: This paper introduces SO(2)-Equivariant Gaussian Sculpting Networks (GSNs) as an approach for SO(2)-Equivariant 3D object reconstruction from single-view image observations.   GSNs take a single obser...  
- **[ThermalGaussian: Thermal 3D Gaussian Splatting](https://arxiv.org/abs/2409.07200v1)**  
  作者: Rongfeng Lu, Hangyu Chen, Zunjie Zhu, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2409.07200v1.pdf)  
  摘要: Thermography is especially valuable for the military and other users of surveillance cameras. Some recent methods based on Neural Radiance Fields (NeRF) are proposed to reconstruct the thermal scenes ...  
  关键词: gaussian splatting, 3d gaussian, real-time rendering, nerf  
- **[gsplat: An Open-Source Library for Gaussian Splatting](https://arxiv.org/abs/2409.06765v1)**  
  作者: Vickie Ye, Ruilong Li, Justin Kerr, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2409.06765v1.pdf) | [![Stars](https://img.shields.io/github/stars/nerfstudio-project/gsplat?style=social)](https://github.com/nerfstudio-project/gsplat)  
  摘要: gsplat is an open-source library designed for training and developing Gaussian Splatting methods. It features a front-end with Python bindings compatible with the PyTorch library and a back-end with h...  
  关键词: gaussian splatting, nerf  
- **[GigaGS: Scaling up Planar-Based 3D Gaussians for Large Scene Surface Reconstruction](https://arxiv.org/abs/2409.06685v1)**  
  作者: Junyi Chen, Weicai Ye, Yifan Wang, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2409.06685v1.pdf)  
  摘要: 3D Gaussian Splatting (3DGS) has shown promising performance in novel view synthesis. Previous methods adapt it to obtaining surfaces of either individual 3D objects or within limited scenes. In this ...  
  关键词: gaussian splatting, 3d gaussian  
- **[MVGaussian: High-Fidelity text-to-3D Content Generation with Multi-View Guidance and Surface Densification](https://arxiv.org/abs/2409.06620v1)**  
  作者: Phu Pham, Aradhya N. Mathur, Ojaswa Sharma, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2409.06620v1.pdf)  
  摘要: The field of text-to-3D content generation has made significant progress in generating realistic 3D objects, with existing methodologies like Score Distillation Sampling (SDS) offering promising guida...  
  关键词: 3d gaussian  
- **[Sources of Uncertainty in 3D Scene Reconstruction](https://arxiv.org/abs/2409.06407v1)**  
  作者: Marcus Klasson, Riccardo Mereu, Juho Kannala, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2409.06407v1.pdf)  
  摘要: The process of 3D scene reconstruction can be affected by numerous uncertainty sources in real-world scenes. While Neural Radiance Fields (NeRFs) and 3D Gaussian Splatting (GS) achieve high-fidelity r...  
  关键词: gaussian splatting, 3d gaussian, 3d reconstruction, nerf  
- **[Online 3D reconstruction and dense tracking in endoscopic videos](https://arxiv.org/abs/2409.06037v1)**  
  作者: Michel Hayoz, Christopher Hahne, Thomas Kurmann, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2409.06037v1.pdf)  
  摘要: 3D scene reconstruction from stereo endoscopic video data is crucial for advancing surgical interventions. In this work, we present an online framework for online, dense 3D scene reconstruction and tr...  
  关键词: gaussian splatting  
- **[GASP: Gaussian Splatting for Physic-Based Simulations](https://arxiv.org/abs/2409.05819v1)**  
  作者: Piotr Borycki, Weronika Smolak, Joanna Waczyńska, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2409.05819v1.pdf)  
  摘要: Physics simulation is paramount for modeling and utilization of 3D scenes in various real-world applications. However, its integration with state-of-the-art 3D scene rendering techniques such as Gauss...  
  关键词: gaussian splatting, 3d gaussian  
- **[LiDAR-3DGS: LiDAR Reinforced 3D Gaussian Splatting for Multimodal Radiance Field Rendering](https://arxiv.org/abs/2409.16296v1)**  
  作者: Hansol Lim, Hanbeom Chang, Jongseong Brad Choi, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2409.16296v1.pdf)  
  摘要: In this paper, we explore the capabilities of multimodal inputs to 3D Gaussian Splatting (3DGS) based Radiance Field Rendering. We present LiDAR-3DGS, a novel method of reinforcing 3DGS inputs with Li...  
  关键词: gaussian splatting, 3d gaussian  
- **[Lagrangian Hashing for Compressed Neural Field Representations](https://arxiv.org/abs/2409.05334v1)**  
  作者: Shrisudhan Govindarajan, Zeno Sambugaro, Akhmedkhan, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2409.05334v1.pdf)  
  摘要: We present Lagrangian Hashing, a representation for neural fields combining the characteristics of fast training NeRF methods that rely on Eulerian grids (i.e.~InstantNGP), with those that employ poin...  
  关键词: gaussian splatting, 3d gaussian, nerf  
- **[DreamMapping: High-Fidelity Text-to-3D Generation via Variational Distribution Mapping](https://arxiv.org/abs/2409.05099v4)**  
  作者: Zeyu Cai, Duotun Wang, Yixun Liang, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2409.05099v4.pdf)  
  摘要: Score Distillation Sampling (SDS) has emerged as a prevalent technique for text-to-3D generation, enabling 3D content creation by distilling view-dependent information from text-to-2D guidance. Howeve...  
  关键词: gaussian splatting  
- **[GS-PT: Exploiting 3D Gaussian Splatting for Comprehensive Point Cloud Understanding via Self-supervised Learning](https://arxiv.org/abs/2409.04963v1)**  
  作者: Keyi Liu, Yeqi Luo, Weidong Yang, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2409.04963v1.pdf)  
  摘要: Self-supervised learning of point cloud aims to leverage unlabeled 3D data to learn meaningful representations without reliance on manual annotations. However, current approaches face challenges such ...  
  关键词: gaussian splatting, 3d gaussian  
- **[Fisheye-GS: Lightweight and Extensible Gaussian Splatting Module for Fisheye Cameras](https://arxiv.org/abs/2409.04751v2)**  
  作者: Zimu Liao, Siyan Chen, Rong Fu, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2409.04751v2.pdf)  
  摘要: Recently, 3D Gaussian Splatting (3DGS) has garnered attention for its high fidelity and real-time rendering. However, adapting 3DGS to different camera models, particularly fisheye lenses, poses chall...  
  关键词: gaussian splatting, 3d gaussian, real-time rendering  
- **[GST: Precise 3D Human Body from a Single Image with Gaussian Splatting Transformers](https://arxiv.org/abs/2409.04196v1)**  
  作者: Lorenza Prospero, Abdullah Hamdi, Joao F. Henriques, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2409.04196v1.pdf)  
  摘要: Reconstructing realistic 3D human models from monocular images has significant applications in creative industries, human-computer interfaces, and healthcare. We base our work on 3D Gaussian Splatting...  
  关键词: gaussian splatting, 3d gaussian  
- **[3D-GP-LMVIC: Learning-based Multi-View Image Coding with 3D Gaussian Geometric Priors](https://arxiv.org/abs/2409.04013v1)**  
  作者: Yujun Huang, Bin Chen, Niu Lian, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2409.04013v1.pdf)  
  摘要: Multi-view image compression is vital for 3D-related applications. To effectively model correlations between views, existing methods typically predict disparity between two views on a 2D plane, which ...  
  关键词: gaussian splatting, 3d gaussian  
- **[LM-Gaussian: Boost Sparse-view 3D Gaussian Splatting with Large Model Priors](https://arxiv.org/abs/2409.03456v2)**  
  作者: Hanyang Yu, Xiaoxiao Long, Ping Tan  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2409.03456v2.pdf)  
  摘要: We aim to address sparse-view reconstruction of a 3D scene by leveraging priors from large-scale vision models. While recent advancements such as 3D Gaussian Splatting (3DGS) have demonstrated remarka...  
  关键词: gaussian splatting, 3d gaussian, 3d reconstruction  
- **[Optimizing 3D Gaussian Splatting for Sparse Viewpoint Scene Reconstruction](https://arxiv.org/abs/2409.03213v1)**  
  作者: Shen Chen, Jiale Zhou, Lei Li  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2409.03213v1.pdf)  
  摘要: 3D Gaussian Splatting (3DGS) has emerged as a promising approach for 3D scene representation, offering a reduction in computational overhead compared to Neural Radiance Fields (NeRF). However, 3DGS is...  
  关键词: gaussian splatting, 3d gaussian, 3d reconstruction, nerf  
- **[Human-VDM: Learning Single-Image 3D Human Gaussian Splatting from Video Diffusion Models](https://arxiv.org/abs/2409.02851v1)**  
  作者: Zhibin Liu, Haoye Dong, Aviral Chharia, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2409.02851v1.pdf)  
  摘要: Generating lifelike 3D humans from a single RGB image remains a challenging task in computer vision, as it requires accurate modeling of geometry, high-quality texture, and plausible unseen parts. Exi...  
  关键词: gaussian splatting  
- **[Object Gaussian for Monocular 6D Pose Estimation from Sparse Views](https://arxiv.org/abs/2409.02581v1)**  
  作者: Luqing Luo, Shichu Sun, Jiangang Yang, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2409.02581v1.pdf)  
  摘要: Monocular object pose estimation, as a pivotal task in computer vision and robotics, heavily depends on accurate 2D-3D correspondences, which often demand costly CAD models that may not be readily ava...  
  关键词: gaussian splatting, 3d gaussian, 3d reconstruction  
- **[GGS: Generalizable Gaussian Splatting for Lane Switching in Autonomous Driving](https://arxiv.org/abs/2409.02382v1)**  
  作者: Huasong Han, Kaixuan Zhou, Xiaoxiao Long, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2409.02382v1.pdf)  
  摘要: We propose GGS, a Generalizable Gaussian Splatting method for Autonomous Driving which can achieve realistic rendering under large viewpoint changes. Previous generalizable 3D gaussian splatting metho...  
  关键词: gaussian splatting, 3d gaussian  
- **[DynOMo: Online Point Tracking by Dynamic Online Monocular Gaussian Reconstruction](https://arxiv.org/abs/2409.02104v1)**  
  作者: Jenny Seidenschwarz, Qunjie Zhou, Bardienus Duisterhof, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2409.02104v1.pdf)  
  摘要: Reconstructing scenes and tracking motion are two sides of the same coin. Tracking points allow for geometric reconstruction [14], while geometric reconstruction of (dynamic) scenes allows for 3D trac...  
  关键词: gaussian splatting, 3d gaussian  
- **[PRoGS: Progressive Rendering of Gaussian Splats](https://arxiv.org/abs/2409.01761v1)**  
  作者: Brent Zoomers, Maarten Wijnants, Ivan Molenaers, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2409.01761v1.pdf)  
  摘要: Over the past year, 3D Gaussian Splatting (3DGS) has received significant attention for its ability to represent 3D scenes in a perceptually accurate manner. However, it can require a substantial amou...  
  关键词: gaussian splatting, 3d gaussian  
- **[GaussianPU: A Hybrid 2D-3D Upsampling Framework for Enhancing Color Point Clouds via 3D Gaussian Splatting](https://arxiv.org/abs/2409.01581v1)**  
  作者: Zixuan Guo, Yifan Xie, Weijing Xie, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2409.01581v1.pdf)  
  摘要: Dense colored point clouds enhance visual perception and are of significant value in various robotic applications. However, existing learning-based point cloud upsampling methods are constrained by co...  
  关键词: gaussian splatting, 3d gaussian  
- **[Free-DyGS: Camera-Pose-Free Scene Reconstruction based on Gaussian Splatting for Dynamic Surgical Videos](https://arxiv.org/abs/2409.01003v2)**  
  作者: Qian Li, Shuojue Yang, Daiyun Shen, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2409.01003v2.pdf)  
  摘要: Reconstructing endoscopic videos is crucial for high-fidelity visualization and the efficiency of surgical operations. Despite the importance, existing 3D reconstruction methods encounter several chal...  
  关键词: gaussian splatting, 3d gaussian, 3d reconstruction  

### 2024年08月
- **[3D Gaussian Splatting for Large-scale Surface Reconstruction from Aerial Images](https://arxiv.org/abs/2409.00381v3)**  
  作者: YuanZheng Wu, Jin Liu, Shunping Ji  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2409.00381v3.pdf)  
  摘要: Recently, 3D Gaussian Splatting (3DGS) has demonstrated excellent ability in small-scale 3D surface reconstruction. However, extending 3DGS to large-scale scenes remains a significant challenge. To ad...  
  关键词: gaussian splatting, 3d gaussian  
- **[UDGS-SLAM : UniDepth Assisted Gaussian Splatting for Monocular SLAM](https://arxiv.org/abs/2409.00362v1)**  
  作者: Mostafa Mansour, Ahmed Abdelsalam, Ari Happonen, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2409.00362v1.pdf)  
  摘要: Recent advancements in monocular neural depth estimation, particularly those achieved by the UniDepth network, have prompted the investigation of integrating UniDepth within a Gaussian splatting frame...  
  关键词: gaussian splatting  
- **[OG-Mapping: Octree-based Structured 3D Gaussians for Online Dense Mapping](https://arxiv.org/abs/2408.17223v1)**  
  作者: Meng Wang, Junyi Wang, Changqun Xia, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2408.17223v1.pdf)  
  摘要: 3D Gaussian splatting (3DGS) has recently demonstrated promising advancements in RGB-D online dense mapping. Nevertheless, existing methods excessively rely on per-pixel depth cues to perform map dens...  
  关键词: gaussian splatting, 3d gaussian  
- **[2DGH: 2D Gaussian-Hermite Splatting for High-quality Rendering and Better Geometry Reconstruction](https://arxiv.org/abs/2408.16982v1)**  
  作者: Ruihan Yu, Tianyu Huang, Jingwang Ling, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2408.16982v1.pdf)  
  摘要: 2D Gaussian Splatting has recently emerged as a significant method in 3D reconstruction, enabling novel view synthesis and geometry reconstruction simultaneously. While the well-known Gaussian kernel ...  
  关键词: gaussian splatting, 3d reconstruction  
- **[ReconX: Reconstruct Any Scene from Sparse Views with Video Diffusion Model](https://arxiv.org/abs/2408.16767v2)**  
  作者: Fangfu Liu, Wenqiang Sun, Hanyang Wang, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2408.16767v2.pdf)  
  摘要: Advancements in 3D scene reconstruction have transformed 2D images from the real world into 3D models, producing realistic 3D results from hundreds of input photos. Despite great success in dense-view...  
  关键词: gaussian splatting, 3d gaussian  
- **[OmniRe: Omni Urban Scene Reconstruction](https://arxiv.org/abs/2408.16760v1)**  
  作者: Ziyu Chen, Jiawei Yang, Jiahui Huang, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2408.16760v1.pdf)  
  摘要: We introduce OmniRe, a holistic approach for efficiently reconstructing high-fidelity dynamic urban scenes from on-device logs. Recent methods for modeling driving sequences using neural radiance fiel...  
  关键词: gaussian splatting  
- **[Generic Objects as Pose Probes for Few-Shot View Synthesis](https://arxiv.org/abs/2408.16690v2)**  
  作者: Zhirui Gao, Renjiao Yi, Chenyang Zhu, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2408.16690v2.pdf)  
  摘要: Radiance fields including NeRFs and 3D Gaussians demonstrate great potential in high-fidelity rendering and scene reconstruction, while they require a substantial number of posed images as inputs. COL...  
  关键词: 3d gaussian, nerf  
- **[Towards Realistic Example-based Modeling via 3D Gaussian Stitching](https://arxiv.org/abs/2408.15708v1)**  
  作者: Xinyu Gao, Ziyi Yang, Bingchen Gong, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2408.15708v1.pdf)  
  摘要: Using parts of existing models to rebuild new models, commonly termed as example-based modeling, is a classical methodology in the realm of computer graphics. Previous works mostly focus on shape comp...  
  关键词: gaussian splatting, 3d gaussian, nerf  
- **[G-Style: Stylized Gaussian Splatting](https://arxiv.org/abs/2408.15695v2)**  
  作者: Áron Samuel Kovács, Pedro Hermosilla, Renata G. Raidou  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2408.15695v2.pdf)  
  摘要: We introduce G-Style, a novel algorithm designed to transfer the style of an image onto a 3D scene represented using Gaussian Splatting. Gaussian Splatting is a powerful 3D representation for novel vi...  
  关键词: gaussian splatting  
- **[Drone-assisted Road Gaussian Splatting with Cross-view Uncertainty](https://arxiv.org/abs/2408.15242v1)**  
  作者: Saining Zhang, Baijun Ye, Xiaoxue Chen, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2408.15242v1.pdf)  
  摘要: Robust and realistic rendering for large-scale road scenes is essential in autonomous driving simulation. Recently, 3D Gaussian Splatting (3D-GS) has made groundbreaking progress in neural rendering, ...  
  关键词: gaussian splatting, 3d gaussian, neural rendering  
- **[Learning-based Multi-View Stereo: A Survey](https://arxiv.org/abs/2408.15235v1)**  
  作者: Fangjinhua Wang, Qingtian Zhu, Di Chang, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2408.15235v1.pdf)  
  摘要: 3D reconstruction aims to recover the dense 3D structure of a scene. It plays an essential role in various applications such as Augmented/Virtual Reality (AR/VR), autonomous driving and robotics. Leve...  
  关键词: gaussian splatting, 3d gaussian, 3d reconstruction, nerf  
- **[Robo-GS: A Physics Consistent Spatial-Temporal Model for Robotic Arm with Hybrid Representation](https://arxiv.org/abs/2408.14873v2)**  
  作者: Haozhe Lou, Yurong Liu, Yike Pan, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2408.14873v2.pdf)  
  摘要: Real2Sim2Real plays a critical role in robotic arm control and reinforcement learning, yet bridging this gap remains a significant challenge due to the complex physical properties of robots and the ob...  
  关键词: gaussian splatting, 3d gaussian  
- **[LapisGS: Layered Progressive 3D Gaussian Splatting for Adaptive Streaming](https://arxiv.org/abs/2408.14823v1)**  
  作者: Yuang Shi, Simone Gasparini, Géraldine Morin, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2408.14823v1.pdf)  
  摘要: The rise of Extended Reality (XR) requires efficient streaming of 3D online worlds, challenging current 3DGS representations to adapt to bandwidth-constrained environments. This paper proposes LapisGS...  
- **[Avatar Concept Slider: Manipulate Concepts In Your Human Avatar With Fine-grained Control](https://arxiv.org/abs/2408.13995v2)**  
  作者: Yixuan He, Lin Geng Foo, Ajmal Saeed Mian, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2408.13995v2.pdf)  
  摘要: Language based editing of 3D human avatars to precisely match user requirements is challenging due to the inherent ambiguity and limited expressiveness of natural language. To overcome this, we propos...  
  关键词: gaussian splatting, 3d gaussian  
- **[DynaSurfGS: Dynamic Surface Reconstruction with Planar-based Gaussian Splatting](https://arxiv.org/abs/2408.13972v1)**  
  作者: Weiwei Cai, Weicai Ye, Peng Ye, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2408.13972v1.pdf)  
  摘要: Dynamic scene reconstruction has garnered significant attention in recent years due to its capabilities in high-quality and real-time rendering. Among various methodologies, constructing a 4D spatial-...  
  关键词: gaussian splatting, 3d gaussian, real-time rendering  
- **[Splatt3R: Zero-shot Gaussian Splatting from Uncalibrated Image Pairs](https://arxiv.org/abs/2408.13912v2)**  
  作者: Brandon Smart, Chuanxia Zheng, Iro Laina, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2408.13912v2.pdf)  
  摘要: In this paper, we introduce Splatt3R, a pose-free, feed-forward method for in-the-wild 3D reconstruction and novel view synthesis from stereo pairs. Given uncalibrated natural images, Splatt3R can pre...  
  关键词: 3d gaussian, 3d reconstruction  
- **[DESI Peculiar Velocity Survey -- Fundamental Plane](https://arxiv.org/abs/2408.13842v1)**  
  作者: Khaled Said, Cullan Howlett, Tamara Davis, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2408.13842v1.pdf)  
  摘要: The Dark Energy Spectroscopic Instrument (DESI) Peculiar Velocity Survey aims to measure the peculiar velocities of early and late type galaxies within the DESI footprint using both the Fundamental Pl...  
  关键词: 3d gaussian  
- **[TranSplat: Generalizable 3D Gaussian Splatting from Sparse Multi-View Images with Transformers](https://arxiv.org/abs/2408.13770v1)**  
  作者: Chuanrui Zhang, Yingshuang Zou, Zhuoling Li, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2408.13770v1.pdf)  
  摘要: Compared with previous 3D reconstruction methods like Nerf, recent Generalizable 3D Gaussian Splatting (G-3DGS) methods demonstrate impressive efficiency even in the sparse-view setting. However, the ...  
  关键词: gaussian splatting, 3d gaussian, 3d reconstruction, nerf  
- **[SceneDreamer360: Text-Driven 3D-Consistent Scene Generation with Panoramic Gaussian Splatting](https://arxiv.org/abs/2408.13711v2)**  
  作者: Wenrui Li, Fucheng Cai, Yapeng Mi, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2408.13711v2.pdf) | [![Stars](https://img.shields.io/github/stars/liwrui/SceneDreamer360?style=social)](https://github.com/liwrui/SceneDreamer360)  
  摘要: Text-driven 3D scene generation has seen significant advancements recently. However, most existing methods generate single-view images using generative models and then stitch them together in 3D space...  
  关键词: gaussian splatting, 3d gaussian  
- **[BiGS: Bidirectional Gaussian Primitives for Relightable 3D Gaussian Splatting](https://arxiv.org/abs/2408.13370v1)**  
  作者: Zhenyuan Liu, Yu Guo, Xinyuan Li, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2408.13370v1.pdf)  
  摘要: We present Bidirectional Gaussian Primitives, an image-based novel view synthesis technique designed to represent and render 3D objects with surface and volumetric materials under dynamic illumination...  
  关键词: gaussian splatting  
- **[LayerPano3D: Layered 3D Panorama for Hyper-Immersive Scene Generation](https://arxiv.org/abs/2408.13252v1)**  
  作者: Shuai Yang, Jing Tan, Mengchen Zhang, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2408.13252v1.pdf)  
  摘要: 3D immersive scene generation is a challenging yet critical task in computer vision and graphics. A desired virtual 3D scene should 1) exhibit omnidirectional view consistency, and 2) allow for free e...  
  关键词: 3d gaussian  
- **[SpecGaussian with Latent Features: A High-quality Modeling of the View-dependent Appearance for 3D Gaussian Splatting](https://arxiv.org/abs/2409.05868v1)**  
  作者: Zhiru Wang, Shiyun Xie, Chengwei Pan, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2409.05868v1.pdf)  
  摘要: Recently, the 3D Gaussian Splatting (3D-GS) method has achieved great success in novel view synthesis, providing real-time rendering while ensuring high-quality rendering results. However, this method...  
  关键词: gaussian splatting, 3d gaussian, real-time rendering  
- **[Atlas Gaussians Diffusion for 3D Generation](https://arxiv.org/abs/2408.13055v2)**  
  作者: Haitao Yang, Yuan Dong, Hanwen Jiang, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2408.13055v2.pdf)  
  摘要: Using the latent diffusion model has proven effective in developing novel 3D generation techniques. To harness the latent diffusion model, a key challenge is designing a high-fidelity and efficient re...  
  关键词: 3d gaussian  
- **[S4D: Streaming 4D Real-World Reconstruction with Gaussians and 3D Control Points](https://arxiv.org/abs/2408.13036v2)**  
  作者: Bing He, Yunuo Chen, Guo Lu, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2408.13036v2.pdf)  
  摘要: Dynamic scene reconstruction using Gaussians has recently attracted increased interest. Mainstream approaches typically employ a global deformation field to warp a 3D scene in canonical space. However...  
  关键词: gaussian splatting, 3d reconstruction  
- **[FLoD: Integrating Flexible Level of Detail into 3D Gaussian Splatting for Customizable Rendering](https://arxiv.org/abs/2408.12894v1)**  
  作者: Yunji Seo, Young Sun Choi, Hyun Seung Son, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2408.12894v1.pdf)  
  摘要: 3D Gaussian Splatting (3DGS) achieves fast and high-quality renderings by using numerous small Gaussians, which leads to significant memory consumption. This reliance on a large number of Gaussians re...  
  关键词: gaussian splatting, 3d gaussian, real-time rendering  
- **[GSFusion: Online RGB-D Mapping Where Gaussian Splatting Meets TSDF Fusion](https://arxiv.org/abs/2408.12677v3)**  
  作者: Jiaxin Wei, Stefan Leutenegger  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2408.12677v3.pdf) | [![Stars](https://img.shields.io/github/stars/goldoak/GSFusion?style=social)](https://github.com/goldoak/GSFusion)  
  摘要: Traditional volumetric fusion algorithms preserve the spatial structure of 3D scenes, which is beneficial for many tasks in computer vision and robotics. However, they often lack realism in terms of v...  
  关键词: gaussian splatting, 3d gaussian  
- **[Subsurface Scattering for 3D Gaussian Splatting](https://arxiv.org/abs/2408.12282v2)**  
  作者: Jan-Niklas Dihlmann, Arjun Majumdar, Andreas Engelhardt, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2408.12282v2.pdf)  
  摘要: 3D reconstruction and relighting of objects made from scattering materials present a significant challenge due to the complex light transport beneath the surface. 3D Gaussian Splatting introduced high...  
  关键词: gaussian splatting, 3d gaussian, 3d reconstruction  
- **[Robust 3D Gaussian Splatting for Novel View Synthesis in Presence of Distractors](https://arxiv.org/abs/2408.11697v1)**  
  作者: Paul Ungermann, Armin Ettenhofer, Matthias Nießner, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2408.11697v1.pdf)  
  摘要: 3D Gaussian Splatting has shown impressive novel view synthesis results; nonetheless, it is vulnerable to dynamic objects polluting the input data of an otherwise static scene, so called distractors. ...  
  关键词: gaussian splatting, 3d gaussian  
- **[DeRainGS: Gaussian Splatting for Enhanced Scene Reconstruction in Rainy Environments](https://arxiv.org/abs/2408.11540v4)**  
  作者: Shuhong Liu, Xiang Chen, Hongming Chen, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2408.11540v4.pdf)  
  摘要: Reconstruction under adverse rainy conditions poses significant challenges due to reduced visibility and the distortion of visual perception. These conditions can severely impair the quality of geomet...  
  关键词: 3d reconstruction  
- **[GaussianOcc: Fully Self-supervised and Efficient 3D Occupancy Estimation with Gaussian Splatting](https://arxiv.org/abs/2408.11447v2)**  
  作者: Wanshui Gan, Fang Liu, Hongbin Xu, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2408.11447v2.pdf) | [![Stars](https://img.shields.io/github/stars/GANWANSHUI/GaussianOcc.git?style=social)](https://github.com/GANWANSHUI/GaussianOcc.git)  
  摘要: We introduce GaussianOcc, a systematic method that investigates the two usages of Gaussian splatting for fully self-supervised and efficient 3D occupancy estimation in surround views. First, tradition...  
  关键词: gaussian splatting  
- **[Pano2Room: Novel View Synthesis from a Single Indoor Panorama](https://arxiv.org/abs/2408.11413v2)**  
  作者: Guo Pu, Yiming Zhao, Zhouhui Lian  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2408.11413v2.pdf) | [![Stars](https://img.shields.io/github/stars/TrickyGo/Pano2Room?style=social)](https://github.com/TrickyGo/Pano2Room)  
  摘要: Recent single-view 3D generative methods have made significant advancements by leveraging knowledge distilled from extensive 3D object datasets. However, challenges persist in the synthesis of 3D scen...  
  关键词: gaussian splatting, 3d gaussian  
- **[GSLoc: Efficient Camera Pose Refinement via 3D Gaussian Splatting](https://arxiv.org/abs/2408.11085v2)**  
  作者: Changkun Liu, Shuai Chen, Yash Bhalgat, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2408.11085v2.pdf)  
  摘要: We leverage 3D Gaussian Splatting (3DGS) as a scene representation and propose a novel test-time camera pose refinement framework, GSLoc. This framework enhances the localization accuracy of state-of-...  
  关键词: gaussian splatting, 3d gaussian, nerf  
- **[Large Point-to-Gaussian Model for Image-to-3D Generation](https://arxiv.org/abs/2408.10935v1)**  
  作者: Longfei Lu, Huachen Gao, Tao Dai, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2408.10935v1.pdf)  
  摘要: Recently, image-to-3D approaches have significantly advanced the generation quality and speed of 3D assets based on large reconstruction models, particularly 3D Gaussian reconstruction models. Existin...  
  关键词: 3d gaussian  
- **[ShapeSplat: A Large-scale Dataset of Gaussian Splats and Their Self-Supervised Pretraining](https://arxiv.org/abs/2408.10906v1)**  
  作者: Qi Ma, Yue Li, Bin Ren, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2408.10906v1.pdf)  
  摘要: 3D Gaussian Splatting (3DGS) has become the de facto method of 3D representation in many vision tasks. This calls for the 3D understanding directly in this representation space. To facilitate the rese...  
  关键词: gaussian splatting, 3d gaussian  
- **[PartGS:Learning Part-aware 3D Representations by Fusing 2D Gaussians and Superquadrics](https://arxiv.org/abs/2408.10789v2)**  
  作者: Zhirui Gao, Renjiao Yi, Yuhang Huang, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2408.10789v2.pdf)  
  摘要: Low-level 3D representations, such as point clouds, meshes, NeRFs, and 3D Gaussians, are commonly used to represent 3D objects or scenes. However, human perception typically understands 3D objects at ...  
  关键词: 3d gaussian, 3d reconstruction, nerf  
- **[DEGAS: Detailed Expressions on Full-Body Gaussian Avatars](https://arxiv.org/abs/2408.10588v1)**  
  作者: Zhijing Shao, Duotun Wang, Qing-Yao Tian, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2408.10588v1.pdf)  
  摘要: Although neural rendering has made significant advancements in creating lifelike, animatable full-body and head avatars, incorporating detailed expressions into full-body avatars remains largely unexp...  
  关键词: gaussian splatting, 3d gaussian, neural rendering  
- **[LoopSplat: Loop Closure by Registering 3D Gaussian Splats](https://arxiv.org/abs/2408.10154v2)**  
  作者: Liyuan Zhu, Yue Li, Erik Sandström, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2408.10154v2.pdf)  
  摘要: Simultaneous Localization and Mapping (SLAM) based on 3D Gaussian Splats (3DGS) has recently shown promise towards more accurate, dense 3D scene maps. However, existing 3DGS-based methods fail to addr...  
  关键词: 3d gaussian  
- **[Implicit Gaussian Splatting with Efficient Multi-Level Tri-Plane Representation](https://arxiv.org/abs/2408.10041v2)**  
  作者: Minye Wu, Tinne Tuytelaars  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2408.10041v2.pdf)  
  摘要: Recent advancements in photo-realistic novel view synthesis have been significantly driven by Gaussian Splatting (3DGS). Nevertheless, the explicit nature of 3DGS data entails considerable storage req...  
  关键词: gaussian splatting  
- **[Topology-aware Human Avatars with Semantically-guided Gaussian Splatting](https://arxiv.org/abs/2408.09665v2)**  
  作者: Haoyu Zhao, Chen Yang, Hao Wang, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2408.09665v2.pdf)  
  摘要: Reconstructing photo-realistic and topology-aware animatable human avatars from monocular videos remains challenging in computer vision and graphics. Recently, methods using 3D Gaussians to represent ...  
  关键词: 3d gaussian, real-time rendering  
- **[3D-Consistent Human Avatars with Sparse Inputs via Gaussian Splatting and Contrastive Learning](https://arxiv.org/abs/2408.09663v3)**  
  作者: Haoyu Zhao, Hao Wang, Chen Yang, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2408.09663v3.pdf)  
  摘要: Existing approaches for human avatar generation--both NeRF-based and 3D Gaussian Splatting (3DGS) based--struggle with maintaining 3D consistency and exhibit degraded detail reconstruction, particular...  
  关键词: gaussian splatting, 3d gaussian, nerf  
- **[Gaussian in the Dark: Real-Time View Synthesis From Inconsistent Dark Images Using Gaussian Splatting](https://arxiv.org/abs/2408.09130v2)**  
  作者: Sheng Ye, Zhen-Hui Dong, Yubin Hu, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2408.09130v2.pdf)  
  摘要: 3D Gaussian Splatting has recently emerged as a powerful representation that can synthesize remarkable novel views using consistent multi-view images as input. However, we notice that images captured ...  
  关键词: gaussian splatting, 3d gaussian  
- **[Correspondence-Guided SfM-Free 3D Gaussian Splatting for NVS](https://arxiv.org/abs/2408.08723v1)**  
  作者: Wei Sun, Xiaosong Zhang, Fang Wan, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2408.08723v1.pdf)  
  摘要: Novel View Synthesis (NVS) without Structure-from-Motion (SfM) pre-processed camera poses--referred to as SfM-free methods--is crucial for promoting rapid response capabilities and enhancing robustnes...  
  关键词: gaussian splatting, 3d gaussian  
- **[GS-ID: Illumination Decomposition on Gaussian Splatting via Diffusion Prior and Parametric Light Source Optimization](https://arxiv.org/abs/2408.08524v1)**  
  作者: Kang Du, Zhihao Liang, Zeyu Wang  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2408.08524v1.pdf)  
  摘要: We present GS-ID, a novel framework for illumination decomposition on Gaussian Splatting, achieving photorealistic novel view synthesis and intuitive light editing. Illumination decomposition is an il...  
  关键词: gaussian splatting  
- **[WaterSplatting: Fast Underwater 3D Scene Reconstruction Using Gaussian Splatting](https://arxiv.org/abs/2408.08206v1)**  
  作者: Huapeng Li, Wenxuan Song, Tianao Xu, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2408.08206v1.pdf)  
  摘要: The underwater 3D scene reconstruction is a challenging, yet interesting problem with applications ranging from naval robots to VR experiences. The problem was successfully tackled by fully volumetric...  
  关键词: gaussian splatting, 3d gaussian, real-time rendering, nerf  
- **[FlashGS: Efficient 3D Gaussian Splatting for Large-scale and High-resolution Rendering](https://arxiv.org/abs/2408.07967v2)**  
  作者: Guofeng Feng, Siyan Chen, Rong Fu, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2408.07967v2.pdf)  
  摘要: This work introduces FlashGS, an open-source CUDA Python library, designed to facilitate the efficient differentiable rasterization of 3D Gaussian Splatting through algorithmic and kernel-level optimi...  
  关键词: gaussian splatting, 3d gaussian  
- **[Progressive Radiance Distillation for Inverse Rendering with Gaussian Splatting](https://arxiv.org/abs/2408.07595v1)**  
  作者: Keyang Ye, Qiming Hou, Kun Zhou  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2408.07595v1.pdf)  
  摘要: We propose progressive radiance distillation, an inverse rendering method that combines physically-based rendering with Gaussian-based radiance field rendering using a distillation progress map. Takin...  
  关键词: gaussian splatting  
- **[3D Gaussian Editing with A Single Image](https://arxiv.org/abs/2408.07540v1)**  
  作者: Guan Luo, Tian-Xing Xu, Ying-Tian Liu, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2408.07540v1.pdf)  
  摘要: The modeling and manipulation of 3D scenes captured from the real world are pivotal in various applications, attracting growing research interest. While previous works on editing have achieved interes...  
  关键词: gaussian splatting, 3d gaussian  
- **[Rethinking Open-Vocabulary Segmentation of Radiance Fields in 3D Space](https://arxiv.org/abs/2408.07416v2)**  
  作者: Hyunjee Lee, Youngsik Yun, Jeongmin Bae, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2408.07416v2.pdf)  
  摘要: Understanding the 3D semantics of a scene is a fundamental problem for various scenarios such as embodied agents. While NeRFs and 3DGS excel at novel-view synthesis, previous methods for understanding...  
  关键词: real-time rendering, nerf  
- **[SpectralGaussians: Semantic, spectral 3D Gaussian splatting for multi-spectral scene representation, visualization and analysis](https://arxiv.org/abs/2408.06975v1)**  
  作者: Saptarshi Neil Sinha, Holger Graf, Michael Weinmann  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2408.06975v1.pdf)  
  摘要: We propose a novel cross-spectral rendering framework based on 3D Gaussian Splatting (3DGS) that generates realistic and semantically meaningful splats from registered multi-view spectrum and segmenta...  
  关键词: gaussian splatting, 3d gaussian, nerf  
- **[HDRGS: High Dynamic Range Gaussian Splatting](https://arxiv.org/abs/2408.06543v3)**  
  作者: Jiahao Wu, Lu Xiao, Rui Peng, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2408.06543v3.pdf)  
  摘要: Recent years have witnessed substantial advancements in the field of 3D reconstruction from 2D images, particularly following the introduction of the neural radiance field (NeRF) technique. However, r...  
  关键词: gaussian splatting, 3d reconstruction, nerf  
- **[Mipmap-GS: Let Gaussians Deform with Scale-specific Mipmap for Anti-aliasing Rendering](https://arxiv.org/abs/2408.06286v1)**  
  作者: Jiameng Li, Yue Shi, Jiezhang Cao, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2408.06286v1.pdf)  
  摘要: 3D Gaussian Splatting (3DGS) has attracted great attention in novel view synthesis because of its superior rendering efficiency and high fidelity. However, the trained Gaussians suffer from severe zoo...  
  关键词: gaussian splatting, 3d gaussian, nerf  
- **[Developing Smart MAVs for Autonomous Inspection in GPS-denied Constructions](https://arxiv.org/abs/2408.06030v1)**  
  作者: Paoqiang Pan, Kewei Hu, Xiao Huang, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2408.06030v1.pdf)  
  摘要: Smart Micro Aerial Vehicles (MAVs) have transformed infrastructure inspection by enabling efficient, high-resolution monitoring at various stages of construction, including hard-to-reach areas. Tradit...  
  关键词: gaussian splatting, 3d gaussian, 3d reconstruction  
- **[HeadGAP: Few-shot 3D Head Avatar via Generalizable Gaussian Priors](https://arxiv.org/abs/2408.06019v1)**  
  作者: Xiaozheng Zheng, Chao Wen, Zhaohu Li, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2408.06019v1.pdf)  
  摘要: In this paper, we present a novel 3D head avatar creation approach capable of generalizing from few-shot in-the-wild data with high-fidelity and animatable robustness. Given the underconstrained natur...  
  关键词: gaussian splatting  
- **[Visual SLAM with 3D Gaussian Primitives and Depth Priors Enabling Novel View Synthesis](https://arxiv.org/abs/2408.05635v2)**  
  作者: Zhongche Qu, Zhi Zhang, Cong Liu, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2408.05635v2.pdf)  
  摘要: Conventional geometry-based SLAM systems lack dense 3D reconstruction capabilities since their data association usually relies on feature correspondences. Additionally, learning-based SLAM systems oft...  
  关键词: gaussian splatting, 3d gaussian, real-time rendering, 3d reconstruction  
- **[PRTGaussian: Efficient Relighting Using 3D Gaussians with Precomputed Radiance Transfer](https://arxiv.org/abs/2408.05631v1)**  
  作者: Libo Zhang, Yuxuan Han, Wenbin Lin, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2408.05631v1.pdf) | [![Stars](https://img.shields.io/github/stars/zhanglbthu/PRTGaussian?style=social)](https://github.com/zhanglbthu/PRTGaussian)  
  摘要: We present PRTGaussian, a realtime relightable novel-view synthesis method made possible by combining 3D Gaussians and Precomputed Radiance Transfer (PRT). By fitting relightable Gaussians to multi-vi...  
  关键词: 3d gaussian  
- **[FlowDreamer: Exploring High Fidelity Text-to-3D Generation via Rectified Flow](https://arxiv.org/abs/2408.05008v3)**  
  作者: Hangyu Li, Xiangxiang Chu, Dingyuan Shi, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2408.05008v3.pdf)  
  摘要: Recent advances in text-to-3D generation have made significant progress. In particular, with the pretrained diffusion models, existing methods predominantly use Score Distillation Sampling (SDS) to tr...  
  关键词: gaussian splatting, 3d gaussian, nerf  
- **[Self-augmented Gaussian Splatting with Structure-aware Masks for Sparse-view 3D Reconstruction](https://arxiv.org/abs/2408.04831v2)**  
  作者: Lingbei Meng, Bi'an Du, Wei Hu  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2408.04831v2.pdf)  
  摘要: Sparse-view 3D reconstruction stands as a formidable challenge in computer vision, aiming to build complete three-dimensional models from a limited array of viewing perspectives. This task confronts s...  
  关键词: gaussian splatting, 3d reconstruction, nerf  
- **[A Review of 3D Reconstruction Techniques for Deformable Tissues in Robotic Surgery](https://arxiv.org/abs/2408.04426v1)**  
  作者: Mengya Xu, Ziqi Guo, An Wang, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2408.04426v1.pdf)  
  摘要: As a crucial and intricate task in robotic minimally invasive surgery, reconstructing surgical scenes using stereo or monocular endoscopic video holds immense potential for clinical applications. NeRF...  
  关键词: gaussian splatting, 3d gaussian, nerf  
- **[InstantStyleGaussian: Efficient Art Style Transfer with 3D Gaussian Splatting](https://arxiv.org/abs/2408.04249v2)**  
  作者: Xin-Yi Yu, Jun-Xin Yu, Li-Bo Zhou, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2408.04249v2.pdf)  
  摘要: We present InstantStyleGaussian, an innovative 3D style transfer method based on the 3D Gaussian Splatting (3DGS) scene representation. By inputting a target-style image, it quickly generates new 3D G...  
  关键词: gaussian splatting, 3d gaussian  
- **[Towards Real-Time Gaussian Splatting: Accelerating 3DGS through Photometric SLAM](https://arxiv.org/abs/2408.03825v1)**  
  作者: Yan Song Hu, Dayou Mao, Yuhao Chen, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2408.03825v1.pdf)  
  摘要: Initial applications of 3D Gaussian Splatting (3DGS) in Visual Simultaneous Localization and Mapping (VSLAM) demonstrate the generation of high-quality volumetric reconstructions from monocular video ...  
  关键词: gaussian splatting, 3d gaussian  
- **[Compact 3D Gaussian Splatting for Static and Dynamic Radiance Fields](https://arxiv.org/abs/2408.03822v1)**  
  作者: Joo Chan Lee, Daniel Rho, Xiangyu Sun, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2408.03822v1.pdf)  
  摘要: 3D Gaussian splatting (3DGS) has recently emerged as an alternative representation that leverages a 3D Gaussian-based representation and introduces an approximated volumetric rendering, achieving very...  
  关键词: gaussian splatting, 3d gaussian, real-time rendering  
- **[3iGS: Factorised Tensorial Illumination for 3D Gaussian Splatting](https://arxiv.org/abs/2408.03753v1)**  
  作者: Zhe Jun Tang, Tat-Jen Cham  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2408.03753v1.pdf)  
  摘要: The use of 3D Gaussians as representation of radiance fields has enabled high quality novel view synthesis at real-time rendering speed. However, the choice of optimising the outgoing radiance of each...  
  关键词: gaussian splatting, 3d gaussian, real-time rendering  
- **[PRTGS: Precomputed Radiance Transfer of Gaussian Splats for Real-Time High-Quality Relighting](https://arxiv.org/abs/2408.03538v1)**  
  作者: Yijia Guo, Yuanxi Bai, Liwen Hu, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2408.03538v1.pdf)  
  摘要: We proposed Precomputed RadianceTransfer of GaussianSplats (PRTGS), a real-time high-quality relighting method for Gaussian splats in low-frequency lighting environments that captures soft shadows and...  
  关键词: gaussian splatting, 3d gaussian  
- **[Leveraging LLMs for Enhanced Open-Vocabulary 3D Scene Understanding in Autonomous Driving](https://arxiv.org/abs/2408.03516v1)**  
  作者: Amirhosein Chahe, Lifeng Zhou  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2408.03516v1.pdf)  
  摘要: This paper introduces a novel method for open-vocabulary 3D scene understanding in autonomous driving by combining Language Embedded 3D Gaussians with Large Language Models (LLMs) for enhanced inferen...  
  关键词: 3d gaussian  
- **[LumiGauss: High-Fidelity Outdoor Relighting with 2D Gaussian Splatting](https://arxiv.org/abs/2408.04474v1)**  
  作者: Joanna Kaleta, Kacper Kania, Tomasz Trzcinski, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2408.04474v1.pdf)  
  摘要: Decoupling lighting from geometry using unconstrained photo collections is notoriously challenging. Solving it would benefit many users, as creating complex 3D assets takes days of manual labor. Many ...  
  关键词: gaussian splatting, 3d reconstruction, nerf  
- **[A General Framework to Boost 3D GS Initialization for Text-to-3D Generation by Lexical Richness](https://arxiv.org/abs/2408.01269v1)**  
  作者: Lutao Jiang, Hangyu Li, Lin Wang  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2408.01269v1.pdf)  
  摘要: Text-to-3D content creation has recently received much attention, especially with the prevalence of 3D Gaussians Splatting. In general, GS-based methods comprise two key stages: initialization and ren...  
  关键词: 3d gaussian  
- **[Reality Fusion: Robust Real-time Immersive Mobile Robot Teleoperation with Volumetric Visual Data Fusion](https://arxiv.org/abs/2408.01225v1)**  
  作者: Ke Li, Reinhard Bacher, Susanne Schmidt, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2408.01225v1.pdf) | [![Stars](https://img.shields.io/github/stars/uhhhci/RealityFusion?style=social)](https://github.com/uhhhci/RealityFusion)  
  摘要: We introduce Reality Fusion, a novel robot teleoperation system that localizes, streams, projects, and merges a typical onboard depth sensor with a photorealistic, high resolution, high framerate, and...  
  关键词: 3d gaussian  
- **[IG-SLAM: Instant Gaussian SLAM](https://arxiv.org/abs/2408.01126v2)**  
  作者: F. Aykut Sarikamis, A. Aydin Alatan  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2408.01126v2.pdf)  
  摘要: 3D Gaussian Splatting has recently shown promising results as an alternative scene representation in SLAM systems to neural implicit representations. However, current methods either lack dense depth m...  
  关键词: gaussian splatting, 3d gaussian, 3d reconstruction  
- **[EmoTalk3D: High-Fidelity Free-View Synthesis of Emotional 3D Talking Head](https://arxiv.org/abs/2408.00297v1)**  
  作者: Qianyun He, Xinya Ji, Yicheng Gong, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2408.00297v1.pdf)  
  摘要: We present a novel approach for synthesizing 3D talking heads with controllable emotion, featuring enhanced lip synchronization and rendering quality. Despite significant progress in the field, prior ...  
- **[LoopSparseGS: Loop Based Sparse-View Friendly Gaussian Splatting](https://arxiv.org/abs/2408.00254v1)**  
  作者: Zhenyu Bao, Guibiao Liao, Kaichen Zhou, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2408.00254v1.pdf)  
  摘要: Despite the photorealistic novel view synthesis (NVS) performance achieved by the original 3D Gaussian splatting (3DGS), its rendering quality significantly degrades with sparse input views. This perf...  
  关键词: gaussian splatting, 3d gaussian  

### 2024年07月
- **[Localized Gaussian Splatting Editing with Contextual Awareness](https://arxiv.org/abs/2408.00083v1)**  
  作者: Hanyuan Xiao, Yingshu Chen, Huajian Huang, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2408.00083v1.pdf)  
  摘要: Recent text-guided generation of individual 3D object has achieved great success using diffusion priors. However, these methods are not suitable for object insertion and replacement tasks as they do n...  
  关键词: gaussian splatting, 3d gaussian  
- **[Expressive Whole-Body 3D Gaussian Avatar](https://arxiv.org/abs/2407.21686v1)**  
  作者: Gyeongsik Moon, Takaaki Shiratori, Shunsuke Saito  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2407.21686v1.pdf)  
  摘要: Facial expression and hand motions are necessary to express our emotions and interact with the world. Nevertheless, most of the 3D human avatars modeled from a casually captured video only support bod...  
  关键词: gaussian splatting, 3d gaussian  
- **[SceneTeller: Language-to-3D Scene Generation](https://arxiv.org/abs/2407.20727v1)**  
  作者: Başak Melis Öcal, Maxim Tatarchenko, Sezer Karaoglu, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2407.20727v1.pdf)  
  摘要: Designing high-quality indoor 3D scenes is important in many practical applications, such as room planning or game development. Conventionally, this has been a time-consuming process which requires bo...  
- **[Improving 2D Feature Representations by 3D-Aware Fine-Tuning](https://arxiv.org/abs/2407.20229v1)**  
  作者: Yuanwen Yue, Anurag Das, Francis Engelmann, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2407.20229v1.pdf)  
  摘要: Current visual foundation models are trained purely on unstructured 2D data, limiting their understanding of 3D structure of objects and scenes. In this work, we show that fine-tuning on 3D-aware data...  
  关键词: 3d gaussian  
- **[Registering Neural 4D Gaussians for Endoscopic Surgery](https://arxiv.org/abs/2407.20213v1)**  
  作者: Yiming Huang, Beilei Cui, Ikemura Kei, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2407.20213v1.pdf)  
  摘要: The recent advance in neural rendering has enabled the ability to reconstruct high-quality 4D scenes using neural networks. Although 4D neural reconstruction is popular, registration for such represen...  
  关键词: gaussian splatting, neural rendering  
- **[Radiance Fields for Robotic Teleoperation](https://arxiv.org/abs/2407.20194v1)**  
  作者: Maximum Wilder-Smith, Vaishakh Patil, Marco Hutter  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2407.20194v1.pdf)  
  摘要: Radiance field methods such as Neural Radiance Fields (NeRFs) or 3D Gaussian Splatting (3DGS), have revolutionized graphics and novel view synthesis. Their ability to synthesize new viewpoints with ph...  
  关键词: gaussian splatting, 3d gaussian, nerf  
- **[ScalingGaussian: Enhancing 3D Content Creation with Generative Gaussian Splatting](https://arxiv.org/abs/2407.19035v1)**  
  作者: Shen Chen, Jiale Zhou, Zhongyu Jiang, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2407.19035v1.pdf)  
  摘要: The creation of high-quality 3D assets is paramount for applications in digital heritage preservation, entertainment, and robotics. Traditionally, this process necessitates skilled professionals and s...  
  关键词: 3d gaussian  
- **[GaussianSR: High Fidelity 2D Gaussian Splatting for Arbitrary-Scale Image Super-Resolution](https://arxiv.org/abs/2407.18046v1)**  
  作者: Jintong Hu, Bin Xia, Bin Chen, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2407.18046v1.pdf)  
  摘要: Implicit neural representations (INRs) have significantly advanced the field of arbitrary-scale super-resolution (ASSR) of images. Most existing INR-based ASSR networks first extract features from the...  
  关键词: gaussian splatting  
- **[3D Gaussian Splatting: Survey, Technologies, Challenges, and Opportunities](https://arxiv.org/abs/2407.17418v1)**  
  作者: Yanqi Bao, Tianyu Ding, Jing Huo, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2407.17418v1.pdf)  
  摘要: 3D Gaussian Splatting (3DGS) has emerged as a prominent technique with the potential to become a mainstream method for 3D representations. It can effectively transform multi-view images into explicit ...  
  关键词: gaussian splatting, 3d gaussian, real-time rendering  
- **[DHGS: Decoupled Hybrid Gaussian Splatting for Driving Scene](https://arxiv.org/abs/2407.16600v3)**  
  作者: Xi Shi, Lingli Chen, Peng Wei, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2407.16600v3.pdf)  
  摘要: Existing Gaussian splatting methods often fall short in achieving satisfactory novel view synthesis in driving scenes, primarily due to the absence of crafty designs and geometric constraints for the ...  
  关键词: gaussian splatting, neural rendering  
- **[HDRSplat: Gaussian Splatting for High Dynamic Range 3D Scene Reconstruction from Raw Images](https://arxiv.org/abs/2407.16503v1)**  
  作者: Shreyas Singh, Aryan Garg, Kaushik Mitra  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2407.16503v1.pdf)  
  摘要: The recent advent of 3D Gaussian Splatting (3DGS) has revolutionized the 3D scene reconstruction space enabling high-fidelity novel view synthesis in real-time. However, with the exception of RawNeRF,...  
  关键词: gaussian splatting, 3d gaussian, nerf  
- **[Integrating Meshes and 3D Gaussians for Indoor Scene Reconstruction with SAM Mask Guidance](https://arxiv.org/abs/2407.16173v1)**  
  作者: Jiyeop Kim, Jongwoo Lim  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2407.16173v1.pdf)  
  摘要: We present a novel approach for 3D indoor scene reconstruction that combines 3D Gaussian Splatting (3DGS) with mesh representations. We use meshes for the room layout of the indoor scene, such as wall...  
  关键词: gaussian splatting, 3d gaussian  
- **[6DGS: 6D Pose Estimation from a Single Image and a 3D Gaussian Splatting Model](https://arxiv.org/abs/2407.15484v1)**  
  作者: Matteo Bortolon, Theodore Tsesmelis, Stuart James, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2407.15484v1.pdf)  
  摘要: We propose 6DGS to estimate the camera pose of a target RGB image given a 3D Gaussian Splatting (3DGS) model representing the scene. 6DGS avoids the iterative process typical of analysis-by-synthesis ...  
  关键词: gaussian splatting, 3d gaussian, nerf  
- **[Enhancement of 3D Gaussian Splatting using Raw Mesh for Photorealistic Recreation of Architectures](https://arxiv.org/abs/2407.15435v2)**  
  作者: Ruizhe Wang, Chunliang Hua, Tomakayev Shingys, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2407.15435v2.pdf)  
  摘要: The photorealistic reconstruction and rendering of architectural scenes have extensive applications in industries such as film, games, and transportation. It also plays an important role in urban plan...  
  关键词: gaussian splatting, 3d gaussian, 3d reconstruction, nerf  
- **[HoloDreamer: Holistic 3D Panoramic World Generation from Text Descriptions](https://arxiv.org/abs/2407.15187v1)**  
  作者: Haiyang Zhou, Xinhua Cheng, Wangbo Yu, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2407.15187v1.pdf)  
  摘要: 3D scene generation is in high demand across various domains, including virtual reality, gaming, and the film industry. Owing to the powerful generative capabilities of text-to-image diffusion models ...  
  关键词: gaussian splatting, 3d gaussian  
- **[GPHM: Gaussian Parametric Head Model for Monocular Head Avatar Reconstruction](https://arxiv.org/abs/2407.15070v2)**  
  作者: Yuelang Xu, Zhaoqi Su, Qingyao Wu, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2407.15070v2.pdf)  
  摘要: Creating high-fidelity 3D human head avatars is crucial for applications in VR/AR, digital human, and film production. Recent advances have leveraged morphable face models to generate animated head av...  
  关键词: 3d gaussian  
- **[Realistic Surgical Image Dataset Generation Based On 3D Gaussian Splatting](https://arxiv.org/abs/2407.14846v1)**  
  作者: Tianle Zeng, Gerardo Loza Galindo, Junlei Hu, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2407.14846v1.pdf)  
  摘要: Computer vision technologies markedly enhance the automation capabilities of robotic-assisted minimally invasive surgery (RAMIS) through advanced tool tracking, detection, and localization. However, t...  
  关键词: gaussian splatting, 3d gaussian  
- **[A Benchmark for Gaussian Splatting Compression and Quality Assessment Study](https://arxiv.org/abs/2407.14197v1)**  
  作者: Qi Yang, Kaifa Yang, Yuke Xing, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2407.14197v1.pdf) | [![Stars](https://img.shields.io/github/stars/Qi-Yangsjtu/GGSC?style=social)](https://github.com/Qi-Yangsjtu/GGSC)  
  摘要: To fill the gap of traditional GS compression method, in this paper, we first propose a simple and effective GS data compression anchor called Graph-based GS Compression (GGSC). GGSC is inspired by gr...  
- **[GaussianBeV: 3D Gaussian Representation meets Perception Models for BeV Segmentation](https://arxiv.org/abs/2407.14108v1)**  
  作者: Florian Chabot, Nicolas Granger, Guillaume Lapouge  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2407.14108v1.pdf)  
  摘要: The Bird's-eye View (BeV) representation is widely used for 3D perception from multi-view camera images. It allows to merge features from different cameras into a common space, providing a unified rep...  
  关键词: gaussian splatting, 3d gaussian  
- **[DirectL: Efficient Radiance Fields Rendering for 3D Light Field Displays](https://arxiv.org/abs/2407.14053v1)**  
  作者: Zongyuan Yang, Baolin Liu, Yingde Song, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2407.14053v1.pdf)  
  摘要: Autostereoscopic display, despite decades of development, has not achieved extensive application, primarily due to the daunting challenge of 3D content creation for non-specialists. The emergence of R...  
  关键词: gaussian splatting, 3d gaussian, real-time rendering, 3d reconstruction, nerf  
- **[PlacidDreamer: Advancing Harmony in Text-to-3D Generation](https://arxiv.org/abs/2407.13976v1)**  
  作者: Shuo Huang, Shikun Sun, Zixuan Wang, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2407.13976v1.pdf) | [![Stars](https://img.shields.io/github/stars/HansenHuang0823/PlacidDreamer?style=social)](https://github.com/HansenHuang0823/PlacidDreamer)  
  摘要: Recently, text-to-3D generation has attracted significant attention, resulting in notable performance enhancements. Previous methods utilize end-to-end 3D generation models to initialize 3D Gaussians,...  
  关键词: 3d gaussian  
- **[Connecting Consistency Distillation to Score Distillation for Text-to-3D Generation](https://arxiv.org/abs/2407.13584v2)**  
  作者: Zongrui Li, Minghui Hu, Qian Zheng, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2407.13584v2.pdf) | [![Stars](https://img.shields.io/github/stars/LMozart/ECCV2024-GCS-BEG?style=social)](https://github.com/LMozart/ECCV2024-GCS-BEG)  
  摘要: Although recent advancements in text-to-3D generation have significantly improved generation quality, issues like limited level of detail and low fidelity still persist, which requires further improve...  
  关键词: gaussian splatting, 3d gaussian  
- **[EaDeblur-GS: Event assisted 3D Deblur Reconstruction with Gaussian Splatting](https://arxiv.org/abs/2407.13520v3)**  
  作者: Yuchen Weng, Zhengwen Shen, Ruofan Chen, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2407.13520v3.pdf)  
  摘要: 3D deblurring reconstruction techniques have recently seen significant advancements with the development of Neural Radiance Fields (NeRF) and 3D Gaussian Splatting (3DGS). Although these techniques ca...  
  关键词: gaussian splatting, 3d gaussian, 3d reconstruction, nerf  
- **[Generalizable Human Gaussians for Sparse View Synthesis](https://arxiv.org/abs/2407.12777v1)**  
  作者: Youngjoong Kwon, Baole Fang, Yixing Lu, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2407.12777v1.pdf)  
  摘要: Recent progress in neural rendering has brought forth pioneering methods, such as NeRF and Gaussian Splatting, which revolutionize view rendering across various domains like AR/VR, gaming, and content...  
  关键词: gaussian splatting, 3d gaussian, neural rendering, nerf  
- **[Splatfacto-W: A Nerfstudio Implementation of Gaussian Splatting for Unconstrained Photo Collections](https://arxiv.org/abs/2407.12306v2)**  
  作者: Congrong Xu, Justin Kerr, Angjoo Kanazawa  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2407.12306v2.pdf)  
  摘要: Novel view synthesis from unconstrained in-the-wild image collections remains a significant yet challenging task due to photometric variations and transient occluders that complicate accurate scene re...  
  关键词: gaussian splatting, 3d gaussian, real-time rendering, nerf  
- **[MVG-Splatting: Multi-View Guided Gaussian Splatting with Adaptive Quantile-Based Geometric Consistency Densification](https://arxiv.org/abs/2407.11840v1)**  
  作者: Zhuoxiao Li, Shanliang Yao, Yijie Chu, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2407.11840v1.pdf)  
  摘要: In the rapidly evolving field of 3D reconstruction, 3D Gaussian Splatting (3DGS) and 2D Gaussian Splatting (2DGS) represent significant advancements. Although 2DGS compresses 3D Gaussian primitives in...  
  关键词: gaussian splatting, 3d gaussian, 3d reconstruction  
- **[Click-Gaussian: Interactive Segmentation to Any 3D Gaussians](https://arxiv.org/abs/2407.11793v1)**  
  作者: Seokhun Choi, Hyeonseop Song, Jaechul Kim, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2407.11793v1.pdf)  
  摘要: Interactive segmentation of 3D Gaussians opens a great opportunity for real-time manipulation of 3D scenes thanks to the real-time rendering capability of 3D Gaussian Splatting. However, the current m...  
  关键词: gaussian splatting, 3d gaussian, real-time rendering  
- **[DreamCatalyst: Fast and High-Quality 3D Editing via Controlling Editability and Identity Preservation](https://arxiv.org/abs/2407.11394v2)**  
  作者: Jiwook Kim, Seonho Lee, Jaeyo Shin, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2407.11394v2.pdf)  
  摘要: Score distillation sampling (SDS) has emerged as an effective framework in text-driven 3D editing tasks, leveraging diffusion models for 3D consistent editing. However, existing SDS-based 3D editing m...  
  关键词: gaussian splatting, 3d gaussian, nerf  
- **[I$^2$-SLAM: Inverting Imaging Process for Robust Photorealistic Dense SLAM](https://arxiv.org/abs/2407.11347v1)**  
  作者: Gwangtak Bae, Changwoon Choi, Hyeongjun Heo, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2407.11347v1.pdf)  
  摘要: We present an inverse image-formation module that can enhance the robustness of existing visual SLAM pipelines for casually captured scenarios. Casual video captures often suffer from motion blur and ...  
  关键词: gaussian splatting  
- **[Ev-GS: Event-based Gaussian splatting for Efficient and Accurate Radiance Field Rendering](https://arxiv.org/abs/2407.11343v1)**  
  作者: Jingqian Wu, Shuo Zhu, Chutian Wang, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2407.11343v1.pdf)  
  摘要: Computational neuromorphic imaging (CNI) with event cameras offers advantages such as minimal motion blur and enhanced dynamic range, compared to conventional frame-based methods. Existing event-based...  
  关键词: gaussian splatting, 3d gaussian  
- **[Gaussian Splatting LK](https://arxiv.org/abs/2407.11309v1)**  
  作者: Liuyue Xie, Joel Julin, Koichiro Niinuma, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2407.11309v1.pdf)  
  摘要: Reconstructing dynamic 3D scenes from 2D images and generating diverse views over time presents a significant challenge due to the inherent complexity and temporal dynamics involved. While recent adva...  
  关键词: gaussian splatting  
- **[iHuman: Instant Animatable Digital Humans From Monocular Videos](https://arxiv.org/abs/2407.11174v1)**  
  作者: Pramish Paudel, Anubhav Khanal, Ajad Chhatkuli, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2407.11174v1.pdf)  
  摘要: Personalized 3D avatars require an animatable representation of digital humans. Doing so instantly from monocular videos offers scalability to broad class of users and wide-scale applications. In this...  
  关键词: gaussian splatting, 3d gaussian, 3d reconstruction  
- **[Scaling 3D Reasoning with LMMs to Large Robot Mission Environments Using Datagraphs](https://arxiv.org/abs/2407.10743v1)**  
  作者: W. J. Meijer, A. C. Kemmeren, E. H. J. Riemens, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2407.10743v1.pdf)  
  摘要: This paper addresses the challenge of scaling Large Multimodal Models (LMMs) to expansive 3D environments. Solving this open problem is especially relevant for robot deployment in many first-responder...  
- **[Interactive Rendering of Relightable and Animatable Gaussian Avatars](https://arxiv.org/abs/2407.10707v1)**  
  作者: Youyi Zhan, Tianjia Shao, He Wang, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2407.10707v1.pdf)  
  摘要: Creating relightable and animatable avatars from multi-view or monocular videos is a challenging task for digital human creation and virtual reality applications. Previous methods rely on neural radia...  
  关键词: gaussian splatting  
- **[Pathformer3D: A 3D Scanpath Transformer for 360° Images](https://arxiv.org/abs/2407.10563v1)**  
  作者: Rong Quan, Yantao Lai, Mengyu Qiu, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2407.10563v1.pdf) | [![Stars](https://img.shields.io/github/stars/lsztzp/Pathformer3D?style=social)](https://github.com/lsztzp/Pathformer3D)  
  摘要: Scanpath prediction in 360{\deg} images can help realize rapid rendering and better user interaction in Virtual/Augmented Reality applications. However, existing scanpath prediction models for 360{\de...  
  关键词: 3d gaussian  
- **[RecGS: Removing Water Caustic with Recurrent Gaussian Splatting](https://arxiv.org/abs/2407.10318v2)**  
  作者: Tianyi Zhang, Weiming Zhi, Kaining Huang, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2407.10318v2.pdf)  
  摘要: Water caustics are commonly observed in seafloor imaging data from shallow-water areas. Traditional methods that remove caustic patterns from images often rely on 2D filtering or pre-training on an an...  
  关键词: gaussian splatting, 3d reconstruction  
- **[3DEgo: 3D Editing on the Go!](https://arxiv.org/abs/2407.10102v1)**  
  作者: Umar Khalid, Hasan Iqbal, Azib Farooq, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2407.10102v1.pdf)  
  摘要: We introduce 3DEgo to address a novel problem of directly synthesizing photorealistic 3D scenes from monocular videos guided by textual prompts. Conventional methods construct a text-conditioned 3D sc...  
  关键词: gaussian splatting, 3d gaussian  
- **[SpikeGS: 3D Gaussian Splatting from Spike Streams with High-Speed Camera Motion](https://arxiv.org/abs/2407.10062v1)**  
  作者: Jiyuan Zhang, Kang Chen, Shiyan Chen, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2407.10062v1.pdf)  
  摘要: Novel View Synthesis plays a crucial role by generating new 2D renderings from multi-view images of 3D scenes. However, capturing high-speed scenes with conventional cameras often leads to motion blur...  
  关键词: gaussian splatting, 3d gaussian, 3d reconstruction, nerf  
- **[Textured-GS: Gaussian Splatting with Spatially Defined Color and Opacity](https://arxiv.org/abs/2407.09733v3)**  
  作者: Zhentao Huang, Minglun Gong  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2407.09733v3.pdf) | [![Stars](https://img.shields.io/github/stars/ZhentaoHuang/Textured-GS?style=social)](https://github.com/ZhentaoHuang/Textured-GS)  
  摘要: In this paper, we introduce Textured-GS, an innovative method for rendering Gaussian splatting that incorporates spatially defined color and opacity variations using Spherical Harmonics (SH). This app...  
  关键词: gaussian splatting  
- **[StyleSplat: 3D Object Style Transfer with Gaussian Splatting](https://arxiv.org/abs/2407.09473v1)**  
  作者: Sahil Jain, Avik Kuthiala, Prabhdeep Singh Sethi, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2407.09473v1.pdf)  
  摘要: Recent advancements in radiance fields have opened new avenues for creating high-quality 3D assets and scenes. Style transfer can enhance these 3D assets with diverse artistic styles, transforming cre...  
  关键词: gaussian splatting, 3d gaussian  
- **[WildGaussians: 3D Gaussian Splatting in the Wild](https://arxiv.org/abs/2407.08447v2)**  
  作者: Jonas Kulhanek, Songyou Peng, Zuzana Kukelova, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2407.08447v2.pdf)  
  摘要: While the field of 3D scene reconstruction is dominated by NeRFs due to their photorealistic quality, 3D Gaussian Splatting (3DGS) has recently emerged, offering similar quality with real-time renderi...  
  关键词: gaussian splatting, 3d gaussian, real-time rendering, nerf  
- **[Survey on Fundamental Deep Learning 3D Reconstruction Techniques](https://arxiv.org/abs/2407.08137v1)**  
  作者: Yonge Bai, LikHang Wong, TszYin Twan  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2407.08137v1.pdf)  
  摘要: This survey aims to investigate fundamental deep learning (DL) based 3D reconstruction techniques that produce photo-realistic 3D models and scenes, highlighting Neural Radiance Fields (NeRFs), Latent...  
  关键词: gaussian splatting, 3d gaussian, 3d reconstruction, nerf  
- **[MIGS: Multi-Identity Gaussian Splatting via Tensor Decomposition](https://arxiv.org/abs/2407.07284v2)**  
  作者: Aggelina Chatziagapi, Grigorios G. Chrysos, Dimitris Samaras  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2407.07284v2.pdf)  
  摘要: We introduce MIGS (Multi-Identity Gaussian Splatting), a novel method that learns a single neural representation for multiple identities, using only monocular videos. Recent 3D Gaussian Splatting (3DG...  
  关键词: gaussian splatting, 3d gaussian  
- **[Reference-based Controllable Scene Stylization with Gaussian Splatting](https://arxiv.org/abs/2407.07220v1)**  
  作者: Yiqun Mei, Jiacong Xu, Vishal M. Patel  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2407.07220v1.pdf)  
  摘要: Referenced-based scene stylization that edits the appearance based on a content-aligned reference image is an emerging research area. Starting with a pretrained neural radiance field (NeRF), existing ...  
  关键词: gaussian splatting, 3d gaussian, real-time rendering, nerf  
- **[3D Gaussian Ray Tracing: Fast Tracing of Particle Scenes](https://arxiv.org/abs/2407.07090v3)**  
  作者: Nicolas Moenne-Loccoz, Ashkan Mirzaei, Or Perel, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2407.07090v3.pdf)  
  摘要: Particle-based representations of radiance fields such as 3D Gaussian Splatting have found great success for reconstructing and re-rendering of complex scenes. Most existing methods render particles v...  
  关键词: gaussian splatting, 3d gaussian  
- **[PICA: Physics-Integrated Clothed Avatar](https://arxiv.org/abs/2407.05324v1)**  
  作者: Bo Peng, Yunfan Tao, Haoyu Zhan, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2407.05324v1.pdf)  
  摘要: We introduce PICA, a novel representation for high-fidelity animatable clothed human avatars with physics-accurate dynamics, even for loose clothing. Previous neural rendering-based representations of...  
  关键词: gaussian splatting, 3d gaussian, neural rendering  
- **[GaussReg: Fast 3D Registration with Gaussian Splatting](https://arxiv.org/abs/2407.05254v1)**  
  作者: Jiahao Chang, Yinglin Xu, Yihao Li, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2407.05254v1.pdf)  
  摘要: Point cloud registration is a fundamental problem for large-scale 3D scene scanning and reconstruction. With the help of deep learning, registration methods have evolved significantly, reaching a near...  
  关键词: gaussian splatting, 3d gaussian, nerf  
- **[Panopticon: a telescope for our times](https://arxiv.org/abs/2407.05103v2)**  
  作者: Will Saunders, Timothy Chin, Michael Goodwin  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2407.05103v2.pdf)  
  摘要: We present a design for a wide-field spectroscopic telescope. The only large powered mirror is spherical, the resulting spherical aberration is corrected for each target separately, giving exceptional...  
- **[SurgicalGaussian: Deformable 3D Gaussians for High-Fidelity Surgical Scene Reconstruction](https://arxiv.org/abs/2407.05023v1)**  
  作者: Weixing Xie, Junfeng Yao, Xianpeng Cao, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2407.05023v1.pdf)  
  摘要: Dynamic reconstruction of deformable tissues in endoscopic video is a key technology for robot-assisted surgery. Recent reconstruction methods based on neural radiance fields (NeRFs) have achieved rem...  
  关键词: gaussian splatting, 3d gaussian, real-time rendering, nerf  
- **[Gaussian Eigen Models for Human Heads](https://arxiv.org/abs/2407.04545v1)**  
  作者: Wojciech Zielonka, Timo Bolkart, Thabo Beeler, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2407.04545v1.pdf)  
  摘要: We present personalized Gaussian Eigen Models (GEMs) for human heads, a novel method that compresses dynamic 3D Gaussians into low-dimensional linear spaces. Our approach is inspired by the seminal wo...  
  关键词: gaussian splatting, 3d gaussian, real-time rendering  
- **[Segment Any 4D Gaussians](https://arxiv.org/abs/2407.04504v2)**  
  作者: Shengxiang Ji, Guanjun Wu, Jiemin Fang, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2407.04504v2.pdf)  
  摘要: Modeling, understanding, and reconstructing the real world are crucial in XR/VR. Recently, 3D Gaussian Splatting (3D-GS) methods have shown remarkable success in modeling and understanding 3D scenes. ...  
  关键词: gaussian splatting, 3d gaussian  
- **[GSD: View-Guided Gaussian Splatting Diffusion for 3D Reconstruction](https://arxiv.org/abs/2407.04237v4)**  
  作者: Yuxuan Mu, Xinxin Zuo, Chuan Guo, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2407.04237v4.pdf)  
  摘要: We present GSD, a diffusion model approach based on Gaussian Splatting (GS) representation for 3D object reconstruction from a single view. Prior works suffer from inconsistent 3D geometry or mediocre...  
  关键词: gaussian splatting  
- **[CRiM-GS: Continuous Rigid Motion-Aware Gaussian Splatting from Motion Blur Images](https://arxiv.org/abs/2407.03923v1)**  
  作者: Junghe Lee, Donghyeong Kim, Dogyoon Lee, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2407.03923v1.pdf)  
  摘要: Neural radiance fields (NeRFs) have received significant attention due to their high-quality novel view rendering ability, prompting research to address various real-world cases. One critical challeng...  
  关键词: gaussian splatting, real-time rendering, nerf  
- **[PFGS: High Fidelity Point Cloud Rendering via Feature Splatting](https://arxiv.org/abs/2407.03857v1)**  
  作者: Jiaxu Wang, Ziyi Zhang, Junhao He, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2407.03857v1.pdf)  
  摘要: Rendering high-fidelity images from sparse point clouds is still challenging. Existing learning-based approaches suffer from either hole artifacts, missing details, or expensive computations. In this ...  
  关键词: gaussian splatting, 3d gaussian  
- **[SpikeGS: Reconstruct 3D scene via fast-moving bio-inspired sensors](https://arxiv.org/abs/2407.03771v2)**  
  作者: Yijia Guo, Liwen Hu, Lei Ma, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2407.03771v2.pdf)  
  摘要: 3D Gaussian Splatting (3DGS) demonstrates unparalleled superior performance in 3D scene reconstruction. However, 3DGS heavily relies on the sharp images. Fulfilling this requirement can be challenging...  
  关键词: gaussian splatting, 3d gaussian  
- **[Expressive Gaussian Human Avatars from Monocular RGB Video](https://arxiv.org/abs/2407.03204v1)**  
  作者: Hezhen Hu, Zhiwen Fan, Tianhao Wu, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2407.03204v1.pdf)  
  摘要: Nuanced expressiveness, particularly through fine-grained hand and facial expressions, is pivotal for enhancing the realism and vitality of digital human representations. In this work, we focus on inv...  
  关键词: 3d gaussian  
- **[VEGS: View Extrapolation of Urban Scenes in 3D Gaussian Splatting using Learned Priors](https://arxiv.org/abs/2407.02945v3)**  
  作者: Sungwon Hwang, Min-Jung Kim, Taewoong Kang, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2407.02945v3.pdf)  
  摘要: Neural rendering-based urban scene reconstruction methods commonly rely on images collected from driving vehicles with cameras facing and moving forward. Although these methods can successfully synthe...  
  关键词: neural rendering  
- **[Free-SurGS: SfM-Free 3D Gaussian Splatting for Surgical Scene Reconstruction](https://arxiv.org/abs/2407.02918v1)**  
  作者: Jiaxin Guo, Jiangliu Wang, Di Kang, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2407.02918v1.pdf) | [![Stars](https://img.shields.io/github/stars/wrld/Free-SurGS?style=social)](https://github.com/wrld/Free-SurGS)  
  摘要: Real-time 3D reconstruction of surgical scenes plays a vital role in computer-assisted surgery, holding a promise to enhance surgeons' visibility. Recent advancements in 3D Gaussian Splatting (3DGS) h...  
  关键词: gaussian splatting, 3d gaussian, 3d reconstruction  
- **[Spatially Coherent 3D Distributions of HI and CO in the Milky Way](https://arxiv.org/abs/2407.02859v1)**  
  作者: Laurin Söding, Gordian Edenhofer, Torsten A. Enßlin, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2407.02859v1.pdf)  
  摘要: The spatial distribution of the gaseous components of the Milky Way is of great importance for a number of different fields, e.g. Galactic structure, star formation and cosmic rays. However, obtaining...  
  关键词: 3d gaussian  
- **[AutoSplat: Constrained Gaussian Splatting for Autonomous Driving Scene Reconstruction](https://arxiv.org/abs/2407.02598v2)**  
  作者: Mustafa Khan, Hamidreza Fazlali, Dhruv Sharma, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2407.02598v2.pdf)  
  摘要: Realistic scene reconstruction and view synthesis are essential for advancing autonomous driving systems by simulating safety-critical scenarios. 3D Gaussian Splatting excels in real-time rendering an...  
  关键词: gaussian splatting, 3d gaussian, real-time rendering  
- **[TrAME: Trajectory-Anchored Multi-View Editing for Text-Guided 3D Gaussian Splatting Manipulation](https://arxiv.org/abs/2407.02034v2)**  
  作者: Chaofan Luo, Donglin Di, Xun Yang, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2407.02034v2.pdf)  
  摘要: Despite significant strides in the field of 3D scene editing, current methods encounter substantial challenge, particularly in preserving 3D consistency in multi-view editing process. To tackle this c...  
- **[DRAGON: Drone and Ground Gaussian Splatting for 3D Building Reconstruction](https://arxiv.org/abs/2407.01761v1)**  
  作者: Yujin Ham, Mateusz Michalkiewicz, Guha Balakrishnan  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2407.01761v1.pdf)  
  摘要: 3D building reconstruction from imaging data is an important task for many applications ranging from urban planning to reconnaissance. Modern Novel View synthesis (NVS) methods like NeRF and Gaussian ...  
  关键词: gaussian splatting, nerf  
- **[GaussianStego: A Generalizable Stenography Pipeline for Generative 3D Gaussians Splatting](https://arxiv.org/abs/2407.01301v1)**  
  作者: Chenxin Li, Hengyu Liu, Zhiwen Fan, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2407.01301v1.pdf)  
  摘要: Recent advancements in large generative models and real-time neural rendering using point-based techniques pave the way for a future of widespread visual data distribution through sharing synthesized ...  
  关键词: gaussian splatting, neural rendering  
- **[Fast and Efficient: Mask Neural Fields for 3D Scene Segmentation](https://arxiv.org/abs/2407.01220v2)**  
  作者: Zihan Gao, Lingling Li, Licheng Jiao, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2407.01220v2.pdf)  
  摘要: Understanding 3D scenes is a crucial challenge in computer vision research with applications spanning multiple domains. Recent advancements in distilling 2D vision-language foundation models into neur...  
  关键词: nerf  
- **[Learning 3D Gaussians for Extremely Sparse-View Cone-Beam CT Reconstruction](https://arxiv.org/abs/2407.01090v2)**  
  作者: Yiqun Lin, Hualiang Wang, Jixiang Chen, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2407.01090v2.pdf)  
  摘要: Cone-Beam Computed Tomography (CBCT) is an indispensable technique in medical imaging, yet the associated radiation exposure raises concerns in clinical practice. To mitigate these risks, sparse-view ...  
  关键词: 3d gaussian  
- **[EndoSparse: Real-Time Sparse View Synthesis of Endoscopic Scenes using Gaussian Splatting](https://arxiv.org/abs/2407.01029v1)**  
  作者: Chenxin Li, Brandon Y. Feng, Yifan Liu, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2407.01029v1.pdf)  
  摘要: 3D reconstruction of biological tissues from a collection of endoscopic images is a key to unlock various important downstream surgical applications with 3D capabilities. Existing methods employ vario...  
  关键词: neural rendering, 3d reconstruction  

### 2024年06月
- **[RTGS: Enabling Real-Time Gaussian Splatting on Mobile Devices Using Efficiency-Guided Pruning and Foveated Rendering](https://arxiv.org/abs/2407.00435v2)**  
  作者: Weikai Lin, Yu Feng, Yuhao Zhu  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2407.00435v2.pdf) | [![Stars](https://img.shields.io/github/stars/horizon-research/Fov-3DGS?style=social)](https://github.com/horizon-research/Fov-3DGS)  
  摘要: Point-Based Neural Rendering (PBNR), i.e., the 3D Gaussian Splatting-family algorithms, emerges as a promising class of rendering techniques, which are permeating all aspects of society, driven by a g...  
  关键词: gaussian splatting, 3d gaussian, neural rendering  
- **[OccFusion: Rendering Occluded Humans with Generative Diffusion Priors](https://arxiv.org/abs/2407.00316v1)**  
  作者: Adam Sun, Tiange Xiang, Scott Delp, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2407.00316v1.pdf)  
  摘要: Most existing human rendering methods require every part of the human to be fully visible throughout the input video. However, this assumption does not hold in real-life settings where obstructions ar...  
  关键词: gaussian splatting, 3d gaussian  
- **[SpotlessSplats: Ignoring Distractors in 3D Gaussian Splatting](https://arxiv.org/abs/2406.20055v2)**  
  作者: Sara Sabour, Lily Goli, George Kopanas, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2406.20055v2.pdf)  
  摘要: 3D Gaussian Splatting (3DGS) is a promising technique for 3D reconstruction, offering efficient training and rendering speeds, making it suitable for real-time applications.However, current methods re...  
  关键词: gaussian splatting, 3d gaussian, 3d reconstruction  
- **[EgoGaussian: Dynamic Scene Understanding from Egocentric Video with 3D Gaussian Splatting](https://arxiv.org/abs/2406.19811v2)**  
  作者: Daiwei Zhang, Gengyan Li, Jiajie Li, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2406.19811v2.pdf)  
  摘要: Human activities are inherently complex, often involving numerous object interactions. To better understand these activities, it is crucial to model their interactions with the environment captured th...  
  关键词: gaussian splatting  
- **[Lightweight Predictive 3D Gaussian Splats](https://arxiv.org/abs/2406.19434v1)**  
  作者: Junli Cao, Vidit Goel, Chaoyang Wang, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2406.19434v1.pdf)  
  摘要: Recent approaches representing 3D objects and scenes using Gaussian splats show increased rendering speed across a variety of platforms and devices. While rendering such representations is indeed extr...  
  关键词: 3d gaussian  
- **[FAGhead: Fully Animate Gaussian Head from Monocular Videos](https://arxiv.org/abs/2406.19070v2)**  
  作者: Yixin Xuan, Xinyang Li, Gongxin Yao, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2406.19070v2.pdf)  
  摘要: High-fidelity reconstruction of 3D human avatars has a wild application in visual reality. In this paper, we introduce FAGhead, a method that enables fully controllable human portraits from monocular ...  
  关键词: 3d gaussian  
- **[Dynamic Gaussian Marbles for Novel View Synthesis of Casual Monocular Videos](https://arxiv.org/abs/2406.18717v2)**  
  作者: Colton Stearns, Adam Harley, Mikaela Uy, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2406.18717v2.pdf)  
  摘要: Gaussian splatting has become a popular representation for novel-view synthesis, exhibiting clear strengths in efficiency, photometric quality, and compositional edibility. Following its success, many...  
  关键词: gaussian splatting  
- **[On Scaling Up 3D Gaussian Splatting Training](https://arxiv.org/abs/2406.18533v1)**  
  作者: Hexu Zhao, Haoyang Weng, Daohan Lu, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2406.18533v1.pdf) | [![Stars](https://img.shields.io/github/stars/nyu-systems/Grendel-GS?style=social)](https://github.com/nyu-systems/Grendel-GS)  
  摘要: 3D Gaussian Splatting (3DGS) is increasingly popular for 3D reconstruction due to its superior visual quality and rendering speed. However, 3DGS training currently occurs on a single GPU, limiting its...  
  关键词: gaussian splatting, 3d gaussian, 3d reconstruction  
- **[GaussianDreamerPro: Text to Manipulable 3D Gaussians with Highly Enhanced Quality](https://arxiv.org/abs/2406.18462v1)**  
  作者: Taoran Yi, Jiemin Fang, Zanwei Zhou, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2406.18462v1.pdf)  
  摘要: Recently, 3D Gaussian splatting (3D-GS) has achieved great success in reconstructing and rendering real-world scenes. To transfer the high rendering quality to generation tasks, a series of research w...  
  关键词: gaussian splatting, 3d gaussian  
- **[Trimming the Fat: Efficient Compression of 3D Gaussian Splats through Pruning](https://arxiv.org/abs/2406.18214v2)**  
  作者: Muhammad Salman Ali, Maryam Qamar, Sung-Ho Bae, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2406.18214v2.pdf)  
  摘要: In recent times, the utilization of 3D models has gained traction, owing to the capacity for end-to-end training initially offered by Neural Radiance Fields and more recently by 3D Gaussian Splatting ...  
  关键词: gaussian splatting, 3d gaussian  
- **[GS-Octree: Octree-based 3D Gaussian Splatting for Robust Object-level 3D Reconstruction Under Strong Lighting](https://arxiv.org/abs/2406.18199v1)**  
  作者: Jiaze Li, Zhengyu Wen, Luo Zhang, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2406.18199v1.pdf)  
  摘要: The 3D Gaussian Splatting technique has significantly advanced the construction of radiance fields from multi-view images, enabling real-time rendering. While point-based rasterization effectively red...  
  关键词: gaussian splatting, 3d gaussian, real-time rendering  
- **[VDG: Vision-Only Dynamic Gaussian for Driving Simulation](https://arxiv.org/abs/2406.18198v1)**  
  作者: Hao Li, Jingfeng Li, Dingwen Zhang, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2406.18198v1.pdf)  
  摘要: Dynamic Gaussian splatting has led to impressive scene reconstruction and image synthesis advances in novel views. Existing methods, however, heavily rely on pre-computed poses and Gaussian initializa...  
  关键词: gaussian splatting  
- **[Director3D: Real-world Camera Trajectory and 3D Scene Generation from Text](https://arxiv.org/abs/2406.17601v1)**  
  作者: Xinyang Li, Zhangyu Lai, Linning Xu, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2406.17601v1.pdf)  
  摘要: Recent advancements in 3D generation have leveraged synthetic datasets with ground truth 3D assets and predefined cameras. However, the potential of adopting real-world datasets, which can produce sig...  
  关键词: 3d gaussian  
- **[NerfBaselines: Consistent and Reproducible Evaluation of Novel View Synthesis Methods](https://arxiv.org/abs/2406.17345v1)**  
  作者: Jonas Kulhanek, Torsten Sattler  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2406.17345v1.pdf)  
  摘要: Novel view synthesis is an important problem with many applications, including AR/VR, gaming, and simulations for robotics. With the recent rapid development of Neural Radiance Fields (NeRFs) and 3D G...  
  关键词: gaussian splatting, 3d gaussian, nerf  
- **[Reducing the Memory Footprint of 3D Gaussian Splatting](https://arxiv.org/abs/2406.17074v1)**  
  作者: Panagiotis Papantonakis, Georgios Kopanas, Bernhard Kerbl, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2406.17074v1.pdf)  
  摘要: 3D Gaussian splatting provides excellent visual quality for novel view synthesis, with fast training and real-time rendering; unfortunately, the memory requirements of this method for storing and tran...  
  关键词: gaussian splatting, 3d gaussian, real-time rendering  
- **[From Perfect to Noisy World Simulation: Customizable Embodied Multi-modal Perturbations for SLAM Robustness Benchmarking](https://arxiv.org/abs/2406.16850v1)**  
  作者: Xiaohao Xu, Tianyi Zhang, Sibo Wang, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2406.16850v1.pdf) | [![Stars](https://img.shields.io/github/stars/Xiaohao-Xu/SLAM-under-Perturbation?style=social)](https://github.com/Xiaohao-Xu/SLAM-under-Perturbation)  
  摘要: Embodied agents require robust navigation systems to operate in unstructured environments, making the robustness of Simultaneous Localization and Mapping (SLAM) models critical to embodied agent auton...  
  关键词: gaussian splatting, nerf  
- **[ClotheDreamer: Text-Guided Garment Generation with 3D Gaussians](https://arxiv.org/abs/2406.16815v1)**  
  作者: Yufei Liu, Junshu Tang, Chu Zheng, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2406.16815v1.pdf)  
  摘要: High-fidelity 3D garment synthesis from text is desirable yet challenging for digital avatar creation. Recent diffusion-based approaches via Score Distillation Sampling (SDS) have enabled new possibil...  
  关键词: gaussian splatting, 3d gaussian  
- **[LGS: A Light-weight 4D Gaussian Splatting for Efficient Surgical Scene Reconstruction](https://arxiv.org/abs/2406.16073v1)**  
  作者: Hengyu Liu, Yifan Liu, Chenxin Li, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2406.16073v1.pdf)  
  摘要: The advent of 3D Gaussian Splatting (3D-GS) techniques and their dynamic scene modeling variants, 4D-GS, offers promising prospects for real-time rendering of dynamic surgical scenarios. However, the ...  
  关键词: gaussian splatting, 3d gaussian, real-time rendering  
- **[Taming 3DGS: High-Quality Radiance Fields with Limited Resources](https://arxiv.org/abs/2406.15643v1)**  
  作者: Saswat Subhajyoti Mallick, Rahul Goel, Bernhard Kerbl, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2406.15643v1.pdf)  
  摘要: 3D Gaussian Splatting (3DGS) has transformed novel-view synthesis with its fast, interpretable, and high-fidelity rendering. However, its resource requirements limit its usability. Especially on const...  
  关键词: gaussian splatting, 3d gaussian  
- **[GeoLRM: Geometry-Aware Large Reconstruction Model for High-Quality 3D Gaussian Generation](https://arxiv.org/abs/2406.15333v2)**  
  作者: Chubin Zhang, Hongliang Song, Yi Wei, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2406.15333v2.pdf)  
  摘要: In this work, we introduce the Geometry-Aware Large Reconstruction Model (GeoLRM), an approach which can predict high-quality assets with 512k Gaussians and 21 input images in only 11 GB GPU memory. P...  
- **[Gaussian Splatting to Real World Flight Navigation Transfer with Liquid Networks](https://arxiv.org/abs/2406.15149v2)**  
  作者: Alex Quach, Makram Chahine, Alexander Amini, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2406.15149v2.pdf)  
  摘要: Simulators are powerful tools for autonomous robot learning as they offer scalable data generation, flexible design, and optimization of trajectories. However, transferring behavior learned from simul...  
  关键词: gaussian splatting, 3d gaussian  
- **[E2GS: Event Enhanced Gaussian Splatting](https://arxiv.org/abs/2406.14978v1)**  
  作者: Hiroyuki Deguchi, Mana Masuda, Takuya Nakabayashi, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2406.14978v1.pdf) | [![Stars](https://img.shields.io/github/stars/deguchihiroyuki/E2GS?style=social)](https://github.com/deguchihiroyuki/E2GS)  
  摘要: Event cameras, known for their high dynamic range, absence of motion blur, and low energy usage, have recently found a wide range of applications thanks to these attributes. In the past few years, the...  
  关键词: gaussian splatting, 3d reconstruction, nerf  
- **[GIC: Gaussian-Informed Continuum for Physical Property Identification and Simulation](https://arxiv.org/abs/2406.14927v3)**  
  作者: Junhao Cai, Yuji Yang, Weihao Yuan, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2406.14927v3.pdf)  
  摘要: This paper studies the problem of estimating physical properties (system identification) through visual observations. To facilitate geometry-aware guidance in physical property estimation, we introduc...  
  关键词: 3d gaussian  
- **[Splatter a Video: Video Gaussian Representation for Versatile Processing](https://arxiv.org/abs/2406.13870v2)**  
  作者: Yang-Tian Sun, Yi-Hua Huang, Lin Ma, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2406.13870v2.pdf)  
  摘要: Video representation is a long-standing problem that is crucial for various down-stream tasks, such as tracking,depth prediction,segmentation,view synthesis,and editing. However, current methods eithe...  
  关键词: 3d gaussian  
- **[Sampling 3D Gaussian Scenes in Seconds with Latent Diffusion Models](https://arxiv.org/abs/2406.13099v1)**  
  作者: Paul Henderson, Melonie de Almeida, Daniela Ivanova, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2406.13099v1.pdf)  
  摘要: We present a latent diffusion model over 3D scenes, that can be trained using only 2D image data. To achieve this, we first design an autoencoder that maps multi-view images to 3D Gaussian splats, and...  
  关键词: 3d gaussian, nerf  
- **[HumanSplat: Generalizable Single-Image Human Gaussian Splatting with Structure Priors](https://arxiv.org/abs/2406.12459v2)**  
  作者: Panwang Pan, Zhuo Su, Chenguo Lin, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2406.12459v2.pdf)  
  摘要: Despite recent advancements in high-fidelity human reconstruction techniques, the requirements for densely captured images or time-consuming per-instance optimization significantly hinder their applic...  
  关键词: gaussian splatting, 3d gaussian  
- **[A Hierarchical 3D Gaussian Representation for Real-Time Rendering of Very Large Datasets](https://arxiv.org/abs/2406.12080v1)**  
  作者: Bernhard Kerbl, Andréas Meuleman, Georgios Kopanas, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2406.12080v1.pdf)  
  摘要: Novel view synthesis has seen major advances in recent years, with 3D Gaussian splatting offering an excellent level of visual quality, fast training and real-time rendering. However, the resources ne...  
  关键词: gaussian splatting, 3d gaussian, real-time rendering  
- **[RetinaGS: Scalable Training for Dense Scene Rendering with Billion-Scale 3D Gaussians](https://arxiv.org/abs/2406.11836v2)**  
  作者: Bingling Li, Shengyi Chen, Luchao Wang, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2406.11836v2.pdf)  
  摘要: In this work, we explore the possibility of training high-parameter 3D Gaussian splatting (3DGS) models on large-scale, high-resolution datasets. We design a general model parallel training method for...  
  关键词: gaussian splatting, 3d gaussian  
- **[Effective Rank Analysis and Regularization for Enhanced 3D Gaussian Splatting](https://arxiv.org/abs/2406.11672v2)**  
  作者: Junha Hyung, Susung Hong, Sungwon Hwang, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2406.11672v2.pdf)  
  摘要: 3D reconstruction from multi-view images is one of the fundamental challenges in computer vision and graphics. Recently, 3D Gaussian Splatting (3DGS) has emerged as a promising technique capable of re...  
  关键词: gaussian splatting, 3d gaussian, real-time rendering, 3d reconstruction  
- **[Projecting Radiance Fields to Mesh Surfaces](https://arxiv.org/abs/2406.11570v1)**  
  作者: Adrian Xuan Wei Lim, Lynnette Hui Xian Ng, Nicholas Kyger, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2406.11570v1.pdf)  
  摘要: Radiance fields produce high fidelity images with high rendering speed, but are difficult to manipulate. We effectively perform avatar texture transfer across different appearances by combining benefi...  
  关键词: 3d gaussian  
- **[3DGS.zip: A survey on 3D Gaussian Splatting Compression Methods](https://arxiv.org/abs/2407.09510v4)**  
  作者: Milena T. Bagdasarian, Paul Knoll, Yi-Hsin Li, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2407.09510v4.pdf)  
  摘要: 3D Gaussian Splatting (3DGS) has emerged as a cutting-edge technique for real-time radiance field rendering, offering state-of-the-art performance in terms of both quality and speed. 3DGS models a sce...  
  关键词: gaussian splatting, 3d gaussian  
- **[Physically Embodied Gaussian Splatting: A Realtime Correctable World Model for Robotics](https://arxiv.org/abs/2406.10788v1)**  
  作者: Jad Abou-Chakra, Krishan Rana, Feras Dayoub, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2406.10788v1.pdf)  
  摘要: For robots to robustly understand and interact with the physical world, it is highly beneficial to have a comprehensive representation - modelling geometry, physics, and visual observations - that inf...  
  关键词: 3d gaussian  
- **[Wild-GS: Real-Time Novel View Synthesis from Unconstrained Photo Collections](https://arxiv.org/abs/2406.10373v1)**  
  作者: Jiacong Xu, Yiqun Mei, Vishal M. Patel  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2406.10373v1.pdf)  
  摘要: Photographs captured in unstructured tourist environments frequently exhibit variable appearances and transient occlusions, challenging accurate scene reconstruction and inducing artifacts in novel vi...  
  关键词: gaussian splatting, 3d gaussian, nerf  
- **[PUP 3D-GS: Principled Uncertainty Pruning for 3D Gaussian Splatting](https://arxiv.org/abs/2406.10219v1)**  
  作者: Alex Hanson, Allen Tu, Vasu Singla, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2406.10219v1.pdf)  
  摘要: Recent advancements in novel view synthesis have enabled real-time rendering speeds and high reconstruction accuracy. 3D Gaussian Splatting (3D-GS), a foundational point-based parametric 3D scene repr...  
  关键词: gaussian splatting, 3d gaussian, real-time rendering, nerf  
- **[L4GM: Large 4D Gaussian Reconstruction Model](https://arxiv.org/abs/2406.10324v1)**  
  作者: Jiawei Ren, Kevin Xie, Ashkan Mirzaei, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2406.10324v1.pdf)  
  摘要: We present L4GM, the first 4D Large Reconstruction Model that produces animated objects from a single-view video input -- in a single feed-forward pass that takes only a second. Key to our success is ...  
  关键词: gaussian splatting, 3d gaussian  
- **[GaussianSR: 3D Gaussian Super-Resolution with 2D Diffusion Priors](https://arxiv.org/abs/2406.10111v1)**  
  作者: Xiqian Yu, Hanxin Zhu, Tianyu He, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2406.10111v1.pdf)  
  摘要: Achieving high-resolution novel view synthesis (HRNVS) from low-resolution input views is a challenging task due to the lack of high-resolution data. Previous methods optimize high-resolution Neural R...  
  关键词: gaussian splatting, 3d gaussian, nerf  
- **[GradeADreamer: Enhanced Text-to-3D Generation Using Gaussian Splatting and Multi-View Diffusion](https://arxiv.org/abs/2406.09850v1)**  
  作者: Trapoom Ukarapol, Kevin Pruvost  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2406.09850v1.pdf) | [![Stars](https://img.shields.io/github/stars/trapoom555/GradeADreamer?style=social)](https://github.com/trapoom555/GradeADreamer)  
  摘要: Text-to-3D generation has shown promising results, yet common challenges such as the Multi-face Janus problem and extended generation time for high-quality assets. In this paper, we address these issu...  
- **[Unified Gaussian Primitives for Scene Representation and Rendering](https://arxiv.org/abs/2406.09733v2)**  
  作者: Yang Zhou, Songyin Wu, Ling-Qi Yan  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2406.09733v2.pdf)  
  摘要: Searching for a unified scene representation remains a research challenge in computer graphics. Traditional mesh-based representations are unsuitable for dense, fuzzy elements, and introduce additiona...  
  关键词: gaussian splatting, 3d gaussian  
- **[Modeling Ambient Scene Dynamics for Free-view Synthesis](https://arxiv.org/abs/2406.09395v1)**  
  作者: Meng-Li Shih, Jia-Bin Huang, Changil Kim, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2406.09395v1.pdf)  
  摘要: We introduce a novel method for dynamic free-view synthesis of an ambient scenes from a monocular capture bringing a immersive quality to the viewing experience. Our method builds upon the recent adva...  
  关键词: gaussian splatting, 3d gaussian  
- **[GGHead: Fast and Generalizable 3D Gaussian Heads](https://arxiv.org/abs/2406.09377v2)**  
  作者: Tobias Kirschstein, Simon Giebenhain, Jiapeng Tang, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2406.09377v2.pdf)  
  摘要: Learning 3D head priors from large 2D image collections is an important step towards high-quality 3D-aware human modeling. A core requirement is an efficient architecture that scales well to large-sca...  
  关键词: gaussian splatting, 3d gaussian  
- **[AV-GS: Learning Material and Geometry Aware Priors for Novel View Acoustic Synthesis](https://arxiv.org/abs/2406.08920v2)**  
  作者: Swapnil Bhosale, Haosen Yang, Diptesh Kanojia, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2406.08920v2.pdf)  
  摘要: Novel view acoustic synthesis (NVAS) aims to render binaural audio at any target viewpoint, given a mono audio emitted by a sound source at a 3D scene. Existing methods have proposed NeRF-based implic...  
  关键词: gaussian splatting, nerf  
- **[GaussianForest: Hierarchical-Hybrid 3D Gaussian Splatting for Compressed Scene Modeling](https://arxiv.org/abs/2406.08759v2)**  
  作者: Fengyi Zhang, Yadan Luo, Tianjun Zhang, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2406.08759v2.pdf) | [![Stars](https://img.shields.io/github/stars/Xian-Bei/GaussianForest?style=social)](https://github.com/Xian-Bei/GaussianForest)  
  摘要: The field of novel-view synthesis has recently witnessed the emergence of 3D Gaussian Splatting, which represents scenes in a point-based manner and renders through rasterization. This methodology, in...  
  关键词: gaussian splatting, 3d gaussian  
- **[ICE-G: Image Conditional Editing of 3D Gaussian Splats](https://arxiv.org/abs/2406.08488v1)**  
  作者: Vishnu Jaganathan, Hannah Hanyun Huang, Muhammad Zubair Irshad, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2406.08488v1.pdf)  
  摘要: Recently many techniques have emerged to create high quality 3D assets and scenes. When it comes to editing of these objects, however, existing approaches are either slow, compromise on quality, or do...  
  关键词: nerf  
- **[Human 3Diffusion: Realistic Avatar Creation via Explicit 3D Consistent Diffusion Models](https://arxiv.org/abs/2406.08475v1)**  
  作者: Yuxuan Xue, Xianghui Xie, Riccardo Marin, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2406.08475v1.pdf)  
  摘要: Creating realistic avatars from a single RGB image is an attractive yet challenging problem. Due to its ill-posed nature, recent works leverage powerful prior from 2D diffusion models pretrained on la...  
  关键词: 3d gaussian, 3d reconstruction  
- **[From Chaos to Clarity: 3DGS in the Dark](https://arxiv.org/abs/2406.08300v1)**  
  作者: Zhihao Li, Yufei Wang, Alex Kot, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2406.08300v1.pdf)  
  摘要: Novel view synthesis from raw images provides superior high dynamic range (HDR) information compared to reconstructions from low dynamic range RGB images. However, the inherent noise in unprocessed ra...  
  关键词: gaussian splatting, 3d gaussian, nerf  
- **[Trim 3D Gaussian Splatting for Accurate Geometry Representation](https://arxiv.org/abs/2406.07499v1)**  
  作者: Lue Fan, Yuxue Yang, Minxing Li, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2406.07499v1.pdf)  
  摘要: In this paper, we introduce Trim 3D Gaussian Splatting (TrimGS) to reconstruct accurate 3D geometry from images. Previous arts for geometry reconstruction from 3D Gaussians mainly focus on exploring s...  
  关键词: gaussian splatting, 3d gaussian  
- **[Cinematic Gaussians: Real-Time HDR Radiance Fields with Depth of Field](https://arxiv.org/abs/2406.07329v4)**  
  作者: Chao Wang, Krzysztof Wolski, Bernhard Kerbl, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2406.07329v4.pdf)  
  摘要: Radiance field methods represent the state of the art in reconstructing complex scenes from multi-view photos. However, these reconstructions often suffer from one or both of the following limitations...  
  关键词: gaussian splatting, 3d gaussian  
- **[GaussianCity: Generative Gaussian Splatting for Unbounded 3D City Generation](https://arxiv.org/abs/2406.06526v2)**  
  作者: Haozhe Xie, Zhaoxi Chen, Fangzhou Hong, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2406.06526v2.pdf)  
  摘要: 3D city generation with NeRF-based methods shows promising generation results but is computationally inefficient. Recently 3D Gaussian Splatting (3D-GS) has emerged as a highly efficient alternative f...  
  关键词: gaussian splatting, 3d gaussian, nerf  
- **[PGSR: Planar-based Gaussian Splatting for Efficient and High-Fidelity Surface Reconstruction](https://arxiv.org/abs/2406.06521v1)**  
  作者: Danpeng Chen, Hai Li, Weicai Ye, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2406.06521v1.pdf)  
  摘要: Recently, 3D Gaussian Splatting (3DGS) has attracted widespread attention due to its high-quality rendering, and ultra-fast training and rendering speed. However, due to the unstructured and irregular...  
  关键词: gaussian splatting, 3d gaussian, nerf  
- **[MVGamba: Unify 3D Content Generation as State Space Sequence Modeling](https://arxiv.org/abs/2406.06367v2)**  
  作者: Xuanyu Yi, Zike Wu, Qiuhong Shen, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2406.06367v2.pdf)  
  摘要: Recent 3D large reconstruction models (LRMs) can generate high-quality 3D content in sub-seconds by integrating multi-view diffusion models with scalable multi-view reconstructors. Current works furth...  
  关键词: gaussian splatting, 3d gaussian  
- **[Lighting Every Darkness with 3DGS: Fast Training and Real-Time Rendering for HDR View Synthesis](https://arxiv.org/abs/2406.06216v1)**  
  作者: Xin Jin, Pengyi Jiao, Zheng-Peng Duan, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2406.06216v1.pdf) | [![Stars](https://img.shields.io/github/stars/Srameo/LE3D?style=social)](https://github.com/Srameo/LE3D)  
  摘要: Volumetric rendering based methods, like NeRF, excel in HDR view synthesis from RAWimages, especially for nighttime scenes. While, they suffer from long training times and cannot perform real-time ren...  
  关键词: gaussian splatting, 3d gaussian, real-time rendering, nerf  
- **[Bits-to-Photon: End-to-End Learned Scalable Point Cloud Compression for Direct Rendering](https://arxiv.org/abs/2406.05915v2)**  
  作者: Yueyu Hu, Ran Gong, Yao Wang  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2406.05915v2.pdf)  
  摘要: Point cloud is a promising 3D representation for volumetric streaming in emerging AR/VR applications. Despite recent advances in point cloud compression, decoding and rendering high-quality images fro...  
  关键词: 3d gaussian  
- **[InfoGaussian: Structure-Aware Dynamic Gaussians through Lightweight Information Shaping](https://arxiv.org/abs/2406.05897v1)**  
  作者: Yunchao Zhang, Guandao Yang, Leonidas Guibas, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2406.05897v1.pdf)  
  摘要: 3D Gaussians, as a low-level scene representation, typically involve thousands to millions of Gaussians. This makes it difficult to control the scene in ways that reflect the underlying dynamic struct...  
  关键词: 3d gaussian  
- **[Simplicits: Mesh-Free, Geometry-Agnostic, Elastic Simulation](https://arxiv.org/abs/2407.09497v1)**  
  作者: Vismay Modi, Nicholas Sharp, Or Perel, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2407.09497v1.pdf)  
  摘要: The proliferation of 3D representations, from explicit meshes to implicit neural fields and more, motivates the need for simulators agnostic to representation. We present a data-, mesh-, and grid-free...  
- **[RefGaussian: Disentangling Reflections from 3D Gaussian Splatting for Realistic Rendering](https://arxiv.org/abs/2406.05852v1)**  
  作者: Rui Zhang, Tianyue Luo, Weidong Yang, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2406.05852v1.pdf)  
  摘要: 3D Gaussian Splatting (3D-GS) has made a notable advancement in the field of neural rendering, 3D scene reconstruction, and novel view synthesis. Nevertheless, 3D-GS encounters the main challenge when...  
  关键词: gaussian splatting, 3d gaussian, neural rendering  
- **[VCR-GauS: View Consistent Depth-Normal Regularizer for Gaussian Surface Reconstruction](https://arxiv.org/abs/2406.05774v2)**  
  作者: Hanlin Chen, Fangyin Wei, Chen Li, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2406.05774v2.pdf)  
  摘要: Although 3D Gaussian Splatting has been widely studied because of its realistic and efficient novel-view synthesis, it is still challenging to extract a high-quality surface from the point-based repre...  
  关键词: gaussian splatting, 3d gaussian  
- **[Flash3D: Feed-Forward Generalisable 3D Scene Reconstruction from a Single Image](https://arxiv.org/abs/2406.04343v1)**  
  作者: Stanislaw Szymanowicz, Eldar Insafutdinov, Chuanxia Zheng, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2406.04343v1.pdf)  
  摘要: In this paper, we propose Flash3D, a method for scene reconstruction and novel view synthesis from a single image which is both very generalisable and efficient. For generalisability, we start from a ...  
  关键词: gaussian splatting, 3d gaussian  
- **[Physics3D: Learning Physical Properties of 3D Gaussians via Video Diffusion](https://arxiv.org/abs/2406.04338v3)**  
  作者: Fangfu Liu, Hanyang Wang, Shunyu Yao, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2406.04338v3.pdf)  
  摘要: In recent years, there has been rapid development in 3D generation models, opening up new possibilities for applications such as simulating the dynamic movements of 3D objects and customizing their be...  
- **[A Survey on 3D Human Avatar Modeling -- From Reconstruction to Generation](https://arxiv.org/abs/2406.04253v1)**  
  作者: Ruihe Wang, Yukang Cao, Kai Han, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2406.04253v1.pdf)  
  摘要: 3D modeling has long been an important area in computer vision and computer graphics. Recently, thanks to the breakthroughs in neural representations and generative models, we witnessed a rapid develo...  
  关键词: gaussian splatting, 3d gaussian  
- **[Gaussian Splatting with Localized Points Management](https://arxiv.org/abs/2406.04251v2)**  
  作者: Haosen Yang, Chenhao Zhang, Wenqing Wang, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2406.04251v2.pdf)  
  摘要: Point management is a critical component in optimizing 3D Gaussian Splatting (3DGS) models, as the point initiation (e.g., via structure from motion) is distributionally inappropriate. Typically, the ...  
  关键词: gaussian splatting, 3d gaussian  
- **[Superpoint Gaussian Splatting for Real-Time High-Fidelity Dynamic Scene Reconstruction](https://arxiv.org/abs/2406.03697v1)**  
  作者: Diwen Wan, Ruijie Lu, Gang Zeng  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2406.03697v1.pdf)  
  摘要: Rendering novel view images in dynamic scenes is a crucial yet challenging task. Current methods mainly utilize NeRF-based methods to represent the static scene and an additional time-variant MLP to m...  
  关键词: gaussian splatting, 3d gaussian, real-time rendering, nerf  
- **[Gaussian Primitives for Deformable Image Registration](https://arxiv.org/abs/2406.03394v2)**  
  作者: Jihe Li, Xiang Liu, Fabian Zhang, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2406.03394v2.pdf)  
  摘要: Deformable Image Registration (DIR) is essential for aligning medical images that exhibit anatomical variations, facilitating applications such as disease tracking and radiotherapy planning. While cla...  
  关键词: gaussian splatting, 3d gaussian  
- **[Dynamic 3D Gaussian Fields for Urban Areas](https://arxiv.org/abs/2406.03175v2)**  
  作者: Tobias Fischer, Jonas Kulhanek, Samuel Rota Bulò, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2406.03175v2.pdf)  
  摘要: We present an efficient neural 3D scene representation for novel-view synthesis (NVS) in large-scale, dynamic urban areas. Existing works are not well suited for applications like mixed-reality or clo...  
  关键词: 3d gaussian  
- **[Event3DGS: Event-Based 3D Gaussian Splatting for High-Speed Robot Egomotion](https://arxiv.org/abs/2406.02972v4)**  
  作者: Tianyi Xiong, Jiayi Wu, Botao He, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2406.02972v4.pdf)  
  摘要: By combining differentiable rendering with explicit point-based scene representations, 3D Gaussian Splatting (3DGS) has demonstrated breakthrough 3D reconstruction capabilities. However, to date 3DGS ...  
  关键词: gaussian splatting, 3d gaussian, 3d reconstruction  
- **[GSGAN: Adversarial Learning for Hierarchical Generation of 3D Gaussian Splats](https://arxiv.org/abs/2406.02968v2)**  
  作者: Sangeek Hyun, Jae-Pil Heo  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2406.02968v2.pdf)  
  摘要: Most advances in 3D Generative Adversarial Networks (3D GANs) largely depend on ray casting-based volume rendering, which incurs demanding rendering costs. One promising alternative is rasterization-b...  
  关键词: gaussian splatting, 3d gaussian  
- **[3D-HGS: 3D Half-Gaussian Splatting](https://arxiv.org/abs/2406.02720v2)**  
  作者: Haolin Li, Jinyang Liu, Mario Sznaier, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2406.02720v2.pdf)  
  摘要: Photo-realistic 3D Reconstruction is a fundamental problem in 3D computer vision. This domain has seen considerable advancements owing to the advent of recent neural rendering techniques. These techni...  
  关键词: gaussian splatting, 3d gaussian, neural rendering, 3d reconstruction, nerf  
- **[Enhancing Temporal Consistency in Video Editing by Reconstructing Videos with 3D Gaussian Splatting](https://arxiv.org/abs/2406.02541v3)**  
  作者: Inkyu Shin, Qihang Yu, Xiaohui Shen, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2406.02541v3.pdf)  
  摘要: Recent advancements in zero-shot video diffusion models have shown promise for text-driven video editing, but challenges remain in achieving high temporal consistency. To address this, we introduce Vi...  
  关键词: gaussian splatting, 3d gaussian, nerf  
- **[SatSplatYOLO: 3D Gaussian Splatting-based Virtual Object Detection Ensembles for Satellite Feature Recognition](https://arxiv.org/abs/2406.02533v1)**  
  作者: Van Minh Nguyen, Emma Sandidge, Trupti Mahendrakar, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2406.02533v1.pdf)  
  摘要: On-orbit servicing (OOS), inspection of spacecraft, and active debris removal (ADR). Such missions require precise rendezvous and proximity operations in the vicinity of non-cooperative, possibly unkn...  
  关键词: gaussian splatting, 3d gaussian  
- **[DDGS-CT: Direction-Disentangled Gaussian Splatting for Realistic Volume Rendering](https://arxiv.org/abs/2406.02518v1)**  
  作者: Zhongpai Gao, Benjamin Planche, Meng Zheng, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2406.02518v1.pdf)  
  摘要: Digitally reconstructed radiographs (DRRs) are simulated 2D X-ray images generated from 3D CT volumes, widely used in preoperative settings but limited in intraoperative applications due to computatio...  
  关键词: gaussian splatting, 3d gaussian  
- **[WE-GS: An In-the-wild Efficient 3D Gaussian Representation for Unconstrained Photo Collections](https://arxiv.org/abs/2406.02407v1)**  
  作者: Yuze Wang, Junyi Wang, Yue Qi  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2406.02407v1.pdf)  
  摘要: Novel View Synthesis (NVS) from unconstrained photo collections is challenging in computer graphics. Recently, 3D Gaussian Splatting (3DGS) has shown promise for photorealistic and real-time NVS of st...  
  关键词: gaussian splatting, 3d gaussian  
- **[Query-based Semantic Gaussian Field for Scene Representation in Reinforcement Learning](https://arxiv.org/abs/2406.02370v4)**  
  作者: Jiaxu Wang, Ziyi Zhang, Qiang Zhang, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2406.02370v4.pdf)  
  摘要: Latent scene representation plays a significant role in training reinforcement learning (RL) agents. To obtain good latent vectors describing the scenes, recent works incorporate the 3D-aware latent-c...  
  关键词: gaussian splatting, 3d gaussian, nerf  
- **[OpenGaussian: Towards Point-Level 3D Gaussian-based Open Vocabulary Understanding](https://arxiv.org/abs/2406.02058v1)**  
  作者: Yanmin Wu, Jiarui Meng, Haijie Li, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2406.02058v1.pdf)  
  摘要: This paper introduces OpenGaussian, a method based on 3D Gaussian Splatting (3DGS) capable of 3D point-level open vocabulary understanding. Our primary motivation stems from observing that existing 3D...  
  关键词: gaussian splatting, 3d gaussian  
- **[FastLGS: Speeding up Language Embedded Gaussians with Feature Grid Mapping](https://arxiv.org/abs/2406.01916v3)**  
  作者: Yuzhou Ji, He Zhu, Junshu Tang, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2406.01916v3.pdf)  
  摘要: The semantically interactive radiance field has always been an appealing task for its potential to facilitate user-friendly and automated real-world 3D scene understanding applications. However, it is...  
  关键词: gaussian splatting, 3d gaussian  
- **[MaGS: Reconstructing and Simulating Dynamic 3D Objects with Mesh-adsorbed Gaussian Splatting](https://arxiv.org/abs/2406.01593v2)**  
  作者: Shaojie Ma, Yawei Luo, Wei Yang, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2406.01593v2.pdf)  
  摘要: 3D reconstruction and simulation, although interrelated, have distinct objectives: reconstruction requires a flexible 3D representation that can adapt to diverse scenes, while simulation needs a struc...  
  关键词: gaussian splatting, 3d gaussian, 3d reconstruction, nerf  
- **[Tetrahedron Splatting for 3D Generation](https://arxiv.org/abs/2406.01579v2)**  
  作者: Chun Gu, Zeyu Yang, Zijie Pan, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2406.01579v2.pdf)  
  摘要: 3D representation is essential to the significant advance of 3D generation with 2D diffusion priors. As a flexible representation, NeRF has been first adopted for 3D representation. With density-based...  
  关键词: gaussian splatting, 3d gaussian, real-time rendering, nerf  
- **[DreamPhysics: Learning Physical Properties of Dynamic 3D Gaussians with Video Diffusion Priors](https://arxiv.org/abs/2406.01476v2)**  
  作者: Tianyu Huang, Haoze Zhang, Yihan Zeng, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2406.01476v2.pdf) | [![Stars](https://img.shields.io/github/stars/tyhuang0428/DreamPhysics?style=social)](https://github.com/tyhuang0428/DreamPhysics)  
  摘要: Dynamic 3D interaction has been attracting a lot of attention recently. However, creating such 4D content remains challenging. One solution is to animate 3D scenes with physics-based simulation, which...  
- **[RaDe-GS: Rasterizing Depth in Gaussian Splatting](https://arxiv.org/abs/2406.01467v2)**  
  作者: Baowen Zhang, Chuan Fang, Rakesh Shrestha, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2406.01467v2.pdf)  
  摘要: Gaussian Splatting (GS) has proven to be highly effective in novel view synthesis, achieving high-quality and real-time rendering. However, its potential for reconstructing detailed 3D shapes has not ...  
  关键词: gaussian splatting, 3d gaussian, real-time rendering  
- **[Self-Calibrating 4D Novel View Synthesis from Monocular Videos Using Gaussian Splatting](https://arxiv.org/abs/2406.01042v2)**  
  作者: Fang Li, Hao Zhang, Narendra Ahuja  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2406.01042v2.pdf) | [![Stars](https://img.shields.io/github/stars/fangli333/SC-4DGS?style=social)](https://github.com/fangli333/SC-4DGS)  
  摘要: Gaussian Splatting (GS) has significantly elevated scene reconstruction efficiency and novel view synthesis (NVS) accuracy compared to Neural Radiance Fields (NeRF), particularly for dynamic scenes. H...  
  关键词: gaussian splatting, nerf  
- **[SuperGaussian: Repurposing Video Models for 3D Super Resolution](https://arxiv.org/abs/2406.00609v4)**  
  作者: Yuan Shen, Duygu Ceylan, Paul Guerrero, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2406.00609v4.pdf)  
  摘要: We present a simple, modular, and generic method that upsamples coarse 3D models by adding geometric and appearance details. While generative 3D models now exist, they do not yet match the quality of ...  
  关键词: nerf  
- **[Topo4D: Topology-Preserving Gaussian Splatting for High-Fidelity 4D Head Capture](https://arxiv.org/abs/2406.00440v3)**  
  作者: Xuanchen Li, Yuhao Cheng, Xingyu Ren, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2406.00440v3.pdf)  
  摘要: 4D head capture aims to generate dynamic topological meshes and corresponding texture maps from videos, which is widely utilized in movies and games for its ability to simulate facial muscle movements...  
  关键词: 3d gaussian  
- **[MoDGS: Dynamic Gaussian Splatting from Casually-captured Monocular Videos](https://arxiv.org/abs/2406.00434v2)**  
  作者: Qingming Liu, Yuan Liu, Jiepeng Wang, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2406.00434v2.pdf)  
  摘要: In this paper, we propose MoDGS, a new pipeline to render novel views of dy namic scenes from a casually captured monocular video. Previous monocular dynamic NeRF or Gaussian Splatting methods strongl...  
  关键词: gaussian splatting, nerf  

### 2024年05月
- **[GS-Phong: Meta-Learned 3D Gaussians for Relightable Novel View Synthesis](https://arxiv.org/abs/2405.20791v1)**  
  作者: Yumeng He, Yunbo Wang, Xiaokang Yang  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2405.20791v1.pdf)  
  摘要: Decoupling the illumination in 3D scenes is crucial for novel view synthesis and relighting. In this paper, we propose a novel method for representing a scene illuminated by a point light using a set ...  
  关键词: 3d gaussian  
- **[ContextGS: Compact 3D Gaussian Splatting with Anchor Level Context Model](https://arxiv.org/abs/2405.20721v1)**  
  作者: Yufei Wang, Zhihao Li, Lanqing Guo, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2405.20721v1.pdf)  
  摘要: Recently, 3D Gaussian Splatting (3DGS) has become a promising framework for novel view synthesis, offering fast rendering speeds and high fidelity. However, the large number of Gaussians and their ass...  
  关键词: gaussian splatting, 3d gaussian  
- **[R$^2$-Gaussian: Rectifying Radiative Gaussian Splatting for Tomographic Reconstruction](https://arxiv.org/abs/2405.20693v2)**  
  作者: Ruyi Zha, Tao Jun Lin, Yuanhao Cai, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2405.20693v2.pdf) | [![Stars](https://img.shields.io/github/stars/Ruyi-Zha/r2_gaussian?style=social)](https://github.com/Ruyi-Zha/r2_gaussian)  
  摘要: 3D Gaussian splatting (3DGS) has shown promising results in image rendering and surface reconstruction. However, its potential in volumetric reconstruction tasks, such as X-ray computed tomography, re...  
  关键词: gaussian splatting, 3d gaussian, nerf  
- **[Hybrid Fourier Score Distillation for Efficient One Image to 3D Object Generation](https://arxiv.org/abs/2405.20669v2)**  
  作者: Shuzhou Yang, Yu Wang, Haijie Li, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2405.20669v2.pdf)  
  摘要: Single image-to-3D generation is pivotal for crafting controllable 3D assets. Given its under-constrained nature, we attempt to leverage 3D geometric priors from a novel view diffusion model and 2D ap...  
  关键词: 3d gaussian  
- **[$\textit{S}^3$Gaussian: Self-Supervised Street Gaussians for Autonomous Driving](https://arxiv.org/abs/2405.20323v1)**  
  作者: Nan Huang, Xiaobao Wei, Wenzhao Zheng, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2405.20323v1.pdf) | [![Stars](https://img.shields.io/github/stars/nnanhuang/S3Gaussian?style=social)](https://github.com/nnanhuang/S3Gaussian/)  
  摘要: Photorealistic 3D reconstruction of street scenes is a critical technique for developing real-world simulators for autonomous driving. Despite the efficacy of Neural Radiance Fields (NeRF) for driving...  
  关键词: gaussian splatting, 3d gaussian, 3d reconstruction, nerf  
- **[A Pixel Is Worth More Than One 3D Gaussians in Single-View 3D Reconstruction](https://arxiv.org/abs/2405.20310v3)**  
  作者: Jianghao Shen, Nan Xue, Tianfu Wu  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2405.20310v3.pdf)  
  摘要: Learning 3D scene representation from a single-view image is a long-standing fundamental problem in computer vision, with the inherent ambiguity in predicting contents unseen from the input view. Buil...  
  关键词: gaussian splatting, 3d gaussian  
- **[Object-centric Reconstruction and Tracking of Dynamic Unknown Objects using 3D Gaussian Splatting](https://arxiv.org/abs/2405.20104v2)**  
  作者: Kuldeep R Barad, Antoine Richard, Jan Dentler, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2405.20104v2.pdf)  
  摘要: Generalizable perception is one of the pillars of high-level autonomy in space robotics. Estimating the structure and motion of unknown objects in dynamic environments is fundamental for such autonomo...  
  关键词: gaussian splatting, 3d gaussian, 3d reconstruction  
- **[PLA4D: Pixel-Level Alignments for Text-to-4D Gaussian Splatting](https://arxiv.org/abs/2405.19957v4)**  
  作者: Qiaowei Miao, JinSheng Quan, Kehan Li, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2405.19957v4.pdf)  
  摘要: Previous text-to-4D methods have leveraged multiple Score Distillation Sampling (SDS) techniques, combining motion priors from video-based diffusion models (DMs) with geometric priors from multiview D...  
  关键词: gaussian splatting  
- **[GaussianPrediction: Dynamic 3D Gaussian Prediction for Motion Extrapolation and Free View Synthesis](https://arxiv.org/abs/2405.19745v1)**  
  作者: Boming Zhao, Yuan Li, Ziyu Sun, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2405.19745v1.pdf)  
  摘要: Forecasting future scenarios in dynamic environments is essential for intelligent decision-making and navigation, a challenge yet to be fully realized in computer vision and robotics. Traditional appr...  
  关键词: 3d gaussian  
- **[GaussianRoom: Improving 3D Gaussian Splatting with SDF Guidance and Monocular Cues for Indoor Scene Reconstruction](https://arxiv.org/abs/2405.19671v1)**  
  作者: Haodong Xiang, Xinghui Li, Xiansong Lai, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2405.19671v1.pdf)  
  摘要: Recently, 3D Gaussian Splatting(3DGS) has revolutionized neural rendering with its high-quality rendering and real-time speed. However, when it comes to indoor scenes with a significant number of text...  
  关键词: gaussian splatting, 3d gaussian, neural rendering  
- **[Uncertainty-guided Optimal Transport in Depth Supervised Sparse-View 3D Gaussian](https://arxiv.org/abs/2405.19657v1)**  
  作者: Wei Sun, Qi Zhang, Yanzhao Zhou, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2405.19657v1.pdf)  
  摘要: 3D Gaussian splatting has demonstrated impressive performance in real-time novel view synthesis. However, achieving successful reconstruction from RGB images generally requires multiple input views ca...  
  关键词: gaussian splatting, 3d gaussian  
- **[TAMBRIDGE: Bridging Frame-Centered Tracking and 3D Gaussian Splatting for Enhanced SLAM](https://arxiv.org/abs/2405.19614v1)**  
  作者: Peifeng Jiang, Hong Liu, Xia Li, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2405.19614v1.pdf)  
  摘要: The limited robustness of 3D Gaussian Splatting (3DGS) to motion blur and camera noise, along with its poor real-time performance, restricts its application in robotic SLAM tasks. Upon analysis, the p...  
  关键词: gaussian splatting, 3d gaussian  
- **[NPGA: Neural Parametric Gaussian Avatars](https://arxiv.org/abs/2405.19331v2)**  
  作者: Simon Giebenhain, Tobias Kirschstein, Martin Rünz, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2405.19331v2.pdf)  
  摘要: The creation of high-fidelity, digital versions of human heads is an important stepping stone in the process of further integrating virtual components into our everyday lives. Constructing such avatar...  
  关键词: gaussian splatting, 3d gaussian, real-time rendering  
- **[DGD: Dynamic 3D Gaussians Distillation](https://arxiv.org/abs/2405.19321v1)**  
  作者: Isaac Labe, Noam Issachar, Itai Lang, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2405.19321v1.pdf)  
  摘要: We tackle the task of learning dynamic 3D semantic radiance fields given a single monocular video as input. Our learned semantic radiance field captures per-point semantics as well as color and geomet...  
  关键词: 3d gaussian  
- **[$E^{3}$Gen: Efficient, Expressive and Editable Avatars Generation](https://arxiv.org/abs/2405.19203v2)**  
  作者: Weitian Zhang, Yichao Yan, Yunhui Liu, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2405.19203v2.pdf)  
  摘要: This paper aims to introduce 3D Gaussian for efficient, expressive, and editable digital avatar generation. This task faces two major challenges: (1) The unstructured nature of 3D Gaussian makes it in...  
  关键词: 3d gaussian  
- **[LP-3DGS: Learning to Prune 3D Gaussian Splatting](https://arxiv.org/abs/2405.18784v1)**  
  作者: Zhaoliang Zhang, Tianchen Song, Yongjae Lee, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2405.18784v1.pdf)  
  摘要: Recently, 3D Gaussian Splatting (3DGS) has become one of the mainstream methodologies for novel view synthesis (NVS) due to its high quality and fast rendering speed. However, as a point-based scene r...  
  关键词: gaussian splatting, 3d gaussian  
- **[EvaGaussians: Event Stream Assisted Gaussian Splatting from Blurry Images](https://arxiv.org/abs/2405.20224v2)**  
  作者: Wangbo Yu, Chaoran Feng, Jiye Tang, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2405.20224v2.pdf)  
  摘要: 3D Gaussian Splatting (3D-GS) has demonstrated exceptional capabilities in 3D scene reconstruction and novel view synthesis. However, its training heavily depends on high-quality, sharp images and acc...  
  关键词: gaussian splatting, 3d gaussian  
- **[GFlow: Recovering 4D World from Monocular Video](https://arxiv.org/abs/2405.18426v1)**  
  作者: Shizun Wang, Xingyi Yang, Qiuhong Shen, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2405.18426v1.pdf)  
  摘要: Reconstructing 4D scenes from video inputs is a crucial yet challenging task. Conventional methods usually rely on the assumptions of multi-view video inputs, known camera parameters, or static scenes...  
  关键词: gaussian splatting, 3d gaussian  
- **[3DitScene: Editing Any Scene via Language-guided Disentangled Gaussian Splatting](https://arxiv.org/abs/2405.18424v1)**  
  作者: Qihang Zhang, Yinghao Xu, Chaoyang Wang, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2405.18424v1.pdf)  
  摘要: Scene image editing is crucial for entertainment, photography, and advertising design. Existing methods solely focus on either 2D individual object or 3D global scene editing. This results in a lack o...  
  关键词: gaussian splatting, 3d gaussian  
- **[3D StreetUnveiler with Semantic-Aware 2DGS](https://arxiv.org/abs/2405.18416v2)**  
  作者: Jingwei Xu, Yikai Wang, Yiqun Zhao, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2405.18416v2.pdf)  
  摘要: Unveiling an empty street from crowded observations captured by in-car cameras is crucial for autonomous driving. However, removing all temporarily static objects, such as stopped vehicles and standin...  
  关键词: gaussian splatting  
- **[NegGS: Negative Gaussian Splatting](https://arxiv.org/abs/2405.18163v2)**  
  作者: Artur Kasymov, Bartosz Czekaj, Marcin Mazur, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2405.18163v2.pdf)  
  摘要: One of the key advantages of 3D rendering is its ability to simulate intricate scenes accurately. One of the most widely used methods for this purpose is Gaussian Splatting, a novel approach that is k...  
  关键词: gaussian splatting  
- **[A Grid-Free Fluid Solver based on Gaussian Spatial Representation](https://arxiv.org/abs/2405.18133v1)**  
  作者: Jingrui Xing, Bin Wang, Mengyu Chu, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2405.18133v1.pdf)  
  摘要: We present a grid-free fluid solver featuring a novel Gaussian representation. Drawing inspiration from the expressive capabilities of 3D Gaussian Splatting in multi-view image reconstruction, we mode...  
  关键词: gaussian splatting, 3d gaussian  
- **[EG4D: Explicit Generation of 4D Object without Score Distillation](https://arxiv.org/abs/2405.18132v1)**  
  作者: Qi Sun, Zhiyang Guo, Ziyu Wan, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2405.18132v1.pdf) | [![Stars](https://img.shields.io/github/stars/jasongzy/EG4D?style=social)](https://github.com/jasongzy/EG4D)  
  摘要: In recent years, the increasing demand for dynamic 3D assets in design and gaming applications has given rise to powerful generative pipelines capable of synthesizing high-quality 4D objects. Previous...  
  关键词: gaussian splatting  
- **[RT-GS2: Real-Time Generalizable Semantic Segmentation for 3D Gaussian Representations of Radiance Fields](https://arxiv.org/abs/2405.18033v2)**  
  作者: Mihnea-Bogdan Jurca, Remco Royen, Ion Giosan, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2405.18033v2.pdf)  
  摘要: Gaussian Splatting has revolutionized the world of novel view synthesis by achieving high rendering performance in real-time. Recently, studies have focused on enriching these 3D representations with ...  
  关键词: gaussian splatting, 3d gaussian  
- **[FreeSplat: Generalizable 3D Gaussian Splatting Towards Free-View Synthesis of Indoor Scenes](https://arxiv.org/abs/2405.17958v3)**  
  作者: Yunsong Wang, Tianxin Huang, Hanlin Chen, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2405.17958v3.pdf)  
  摘要: Empowering 3D Gaussian Splatting with generalization ability is appealing. However, existing generalizable 3D Gaussian Splatting methods are largely confined to narrow-range interpolation between ster...  
  关键词: gaussian splatting, 3d gaussian  
- **[A Refined 3D Gaussian Representation for High-Quality Dynamic Scene Reconstruction](https://arxiv.org/abs/2405.17891v1)**  
  作者: Bin Zhang, Bi Zeng, Zexin Peng  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2405.17891v1.pdf)  
  摘要: In recent years, Neural Radiance Fields (NeRF) has revolutionized three-dimensional (3D) reconstruction with its implicit representation. Building upon NeRF, 3D Gaussian Splatting (3D-GS) has departed...  
  关键词: gaussian splatting, 3d gaussian, nerf  
- **[HFGS: 4D Gaussian Splatting with Emphasis on Spatial and Temporal High-Frequency Components for Endoscopic Scene Reconstruction](https://arxiv.org/abs/2405.17872v3)**  
  作者: Haoyu Zhao, Xingyue Zhao, Lingting Zhu, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2405.17872v3.pdf)  
  摘要: Robot-assisted minimally invasive surgery benefits from enhancing dynamic scene reconstruction, as it improves surgical outcomes. While Neural Radiance Fields (NeRF) have been effective in scene recon...  
  关键词: gaussian splatting, 3d gaussian, neural rendering, nerf  
- **[Deform3DGS: Flexible Deformation for Fast Surgical Scene Reconstruction with Gaussian Splatting](https://arxiv.org/abs/2405.17835v3)**  
  作者: Shuojue Yang, Qian Li, Daiyun Shen, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2405.17835v3.pdf) | [![Stars](https://img.shields.io/github/stars/jinlab-imvr/Deform3DGS?style=social)](https://github.com/jinlab-imvr/Deform3DGS)  
  摘要: Tissue deformation poses a key challenge for accurate surgical scene reconstruction. Despite yielding high reconstruction quality, existing methods suffer from slow rendering speeds and long training ...  
  关键词: gaussian splatting, 3d gaussian, real-time rendering  
- **[Mani-GS: Gaussian Splatting Manipulation with Triangular Mesh](https://arxiv.org/abs/2405.17811v1)**  
  作者: Xiangjun Gao, Xiaoyu Li, Yiyu Zhuang, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2405.17811v1.pdf)  
  摘要: Neural 3D representations such as Neural Radiance Fields (NeRF), excel at producing photo-realistic rendering results but lack the flexibility for manipulation and editing which is crucial for content...  
  关键词: gaussian splatting, 3d gaussian, nerf  
- **[SafeguardGS: 3D Gaussian Primitive Pruning While Avoiding Catastrophic Scene Destruction](https://arxiv.org/abs/2405.17793v2)**  
  作者: Yongjae Lee, Zhaoliang Zhang, Deliang Fan  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2405.17793v2.pdf)  
  摘要: 3D Gaussian Splatting (3DGS) has made significant strides in novel view synthesis. However, its suboptimal densification process results in the excessively large number of Gaussian primitives, which i...  
  关键词: gaussian splatting, 3d gaussian  
- **[DC-Gaussian: Improving 3D Gaussian Splatting for Reflective Dash Cam Videos](https://arxiv.org/abs/2405.17705v3)**  
  作者: Linhan Wang, Kai Cheng, Shuo Lei, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2405.17705v3.pdf)  
  摘要: We present DC-Gaussian, a new method for generating novel views from in-vehicle dash cam videos. While neural rendering techniques have made significant strides in driving scenarios, existing methods ...  
  关键词: gaussian splatting, 3d gaussian, neural rendering  
- **[GOI: Find 3D Gaussians of Interest with an Optimizable Open-vocabulary Semantic-space Hyperplane](https://arxiv.org/abs/2405.17596v2)**  
  作者: Yansong Qu, Shaohui Dai, Xinyang Li, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2405.17596v2.pdf)  
  摘要: 3D open-vocabulary scene understanding, crucial for advancing augmented reality and robotic applications, involves interpreting and locating specific regions within a 3D space as directed by natural l...  
  关键词: gaussian splatting, 3d gaussian  
- **[GaussianFormer: Scene as Gaussians for Vision-Based 3D Semantic Occupancy Prediction](https://arxiv.org/abs/2405.17429v1)**  
  作者: Yuanhui Huang, Wenzhao Zheng, Yunpeng Zhang, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2405.17429v1.pdf) | [![Stars](https://img.shields.io/github/stars/huang-yh/GaussianFormer?style=social)](https://github.com/huang-yh/GaussianFormer)  
  摘要: 3D semantic occupancy prediction aims to obtain 3D fine-grained geometry and semantics of the surrounding scene and is an important task for the robustness of vision-centric autonomous driving. Most e...  
  关键词: 3d gaussian  
- **[MoSca: Dynamic Gaussian Fusion from Casual Videos via 4D Motion Scaffolds](https://arxiv.org/abs/2405.17421v2)**  
  作者: Jiahui Lei, Yijia Weng, Adam Harley, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2405.17421v2.pdf)  
  摘要: We introduce 4D Motion Scaffolds (MoSca), a modern 4D reconstruction system designed to reconstruct and synthesize novel views of dynamic scenes from monocular videos captured casually in the wild. To...  
  关键词: gaussian splatting  
- **[DOF-GS: Adjustable Depth-of-Field 3D Gaussian Splatting for Refocusing,Defocus Rendering and Blur Removal](https://arxiv.org/abs/2405.17351v1)**  
  作者: Yujie Wang, Praneeth Chakravarthula, Baoquan Chen  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2405.17351v1.pdf)  
  摘要: 3D Gaussian Splatting-based techniques have recently advanced 3D scene reconstruction and novel view synthesis, achieving high-quality real-time rendering. However, these approaches are inherently lim...  
  关键词: gaussian splatting, 3d gaussian, real-time rendering  
- **[Memorize What Matters: Emergent Scene Decomposition from Multitraverse](https://arxiv.org/abs/2405.17187v2)**  
  作者: Yiming Li, Zehong Wang, Yue Wang, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2405.17187v2.pdf)  
  摘要: Humans naturally retain memories of permanent elements, while ephemeral moments often slip through the cracks of memory. This selective retention is crucial for robotic perception, localization, and m...  
  关键词: gaussian splatting, 3d gaussian, neural rendering, 3d reconstruction  
- **[F-3DGS: Factorized Coordinates and Representations for 3D Gaussian Splatting](https://arxiv.org/abs/2405.17083v2)**  
  作者: Xiangyu Sun, Joo Chan Lee, Daniel Rho, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2405.17083v2.pdf)  
  摘要: The neural radiance field (NeRF) has made significant strides in representing 3D scenes and synthesizing novel views. Despite its advancements, the high computational costs of NeRF have posed challeng...  
  关键词: gaussian splatting, 3d gaussian, neural rendering, nerf  
- **[SA-GS: Semantic-Aware Gaussian Splatting for Large Scene Reconstruction with Geometry Constrain](https://arxiv.org/abs/2405.16923v2)**  
  作者: Butian Xiong, Xiaoyu Ye, Tze Ho Elden Tse, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2405.16923v2.pdf)  
  摘要: With the emergence of Gaussian Splats, recent efforts have focused on large-scale scene geometric reconstruction. However, most of these efforts either concentrate on memory reduction or spatial space...  
  关键词: 3d gaussian  
- **[Sync4D: Video Guided Controllable Dynamics for Physics-Based 4D Generation](https://arxiv.org/abs/2405.16849v3)**  
  作者: Zhoujie Fu, Jiacheng Wei, Wenhao Shen, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2405.16849v3.pdf)  
  摘要: In this work, we introduce a novel approach for creating controllable dynamics in 3D-generated Gaussians using casually captured reference videos. Our method transfers the motion of objects from refer...  
  关键词: 3d gaussian  
- **[PyGS: Large-scale Scene Representation with Pyramidal 3D Gaussian Splatting](https://arxiv.org/abs/2405.16829v3)**  
  作者: Zipeng Wang, Dan Xu  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2405.16829v3.pdf)  
  摘要: Neural Radiance Fields (NeRFs) have demonstrated remarkable proficiency in synthesizing photorealistic images of large-scale scenes. However, they are often plagued by a loss of fine details and long ...  
  关键词: gaussian splatting, 3d gaussian, nerf  
- **[Diffusion4D: Fast Spatial-temporal Consistent 4D Generation via Video Diffusion Models](https://arxiv.org/abs/2405.16645v1)**  
  作者: Hanwen Liang, Yuyang Yin, Dejia Xu, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2405.16645v1.pdf)  
  摘要: The availability of large-scale multimodal datasets and advancements in diffusion models have significantly accelerated progress in 4D content generation. Most prior approaches rely on multiple image ...  
  关键词: gaussian splatting  
- **[Splat-SLAM: Globally Optimized RGB-only SLAM with 3D Gaussians](https://arxiv.org/abs/2405.16544v1)**  
  作者: Erik Sandström, Keisuke Tateno, Michael Oechsle, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2405.16544v1.pdf) | [![Stars](https://img.shields.io/github/stars/eriksandstroem/Splat-SLAM?style=social)](https://github.com/eriksandstroem/Splat-SLAM)  
  摘要: 3D Gaussian Splatting has emerged as a powerful representation of geometry and appearance for RGB-only dense Simultaneous Localization and Mapping (SLAM), as it provides a compact dense map representa...  
  关键词: gaussian splatting, 3d gaussian, 3d reconstruction  
- **[Sp2360: Sparse-view 360 Scene Reconstruction using Cascaded 2D Diffusion Priors](https://arxiv.org/abs/2405.16517v2)**  
  作者: Soumava Paul, Christopher Wewer, Bernt Schiele, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2405.16517v2.pdf)  
  摘要: We aim to tackle sparse-view reconstruction of a 360 3D scene using priors from latent diffusion models (LDM). The sparse-view setting is ill-posed and underconstrained, especially for scenes where th...  
  关键词: 3d gaussian, nerf  
- **[Feature Splatting for Better Novel View Synthesis with Low Overlap](https://arxiv.org/abs/2405.15518v2)**  
  作者: T. Berriel Martins, Javier Civera  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2405.15518v2.pdf) | [![Stars](https://img.shields.io/github/stars/tberriel/FeatSplat?style=social)](https://github.com/tberriel/FeatSplat)  
  摘要: 3D Gaussian Splatting has emerged as a very promising scene representation, achieving state-of-the-art quality in novel view synthesis significantly faster than competing alternatives. However, its us...  
  关键词: gaussian splatting, 3d gaussian  
- **[GSDeformer: Direct Cage-based Deformation for 3D Gaussian Splatting](https://arxiv.org/abs/2405.15491v1)**  
  作者: Jiajun Huang, Hongchuan Yu  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2405.15491v1.pdf)  
  摘要: We present GSDeformer, a method that achieves free-form deformation on 3D Gaussian Splatting(3DGS) without requiring any architectural changes. Our method extends cage-based deformation, a traditional...  
  关键词: gaussian splatting, 3d gaussian  
- **[Don't Splat your Gaussians: Volumetric Ray-Traced Primitives for Modeling and Rendering Scattering and Emissive Media](https://arxiv.org/abs/2405.15425v2)**  
  作者: Jorge Condor, Sebastien Speierer, Lukas Bode, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2405.15425v2.pdf)  
  摘要: Efficient scene representations are essential for many computer graphics applications. A general unified representation that can handle both surfaces and volumes simultaneously, remains a research cha...  
  关键词: 3d gaussian  
- **[DisC-GS: Discontinuity-aware Gaussian Splatting](https://arxiv.org/abs/2405.15196v2)**  
  作者: Haoxuan Qu, Zhuoling Li, Hossein Rahmani, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2405.15196v2.pdf)  
  摘要: Recently, Gaussian Splatting, a method that represents a 3D scene as a collection of Gaussian distributions, has gained significant attention in addressing the task of novel view synthesis. In this pa...  
  关键词: gaussian splatting  
- **[HDR-GS: Efficient High Dynamic Range Novel View Synthesis at 1000x Speed via Gaussian Splatting](https://arxiv.org/abs/2405.15125v4)**  
  作者: Yuanhao Cai, Zihao Xiao, Yixun Liang, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2405.15125v4.pdf) | [![Stars](https://img.shields.io/github/stars/caiyuanhao1998/HDR-GS?style=social)](https://github.com/caiyuanhao1998/HDR-GS)  
  摘要: High dynamic range (HDR) novel view synthesis (NVS) aims to create photorealistic images from novel viewpoints using HDR imaging techniques. The rendered HDR images capture a wider range of brightness...  
  关键词: gaussian splatting, 3d gaussian, nerf  
- **[GS-Hider: Hiding Messages into 3D Gaussian Splatting](https://arxiv.org/abs/2405.15118v2)**  
  作者: Xuanyu Zhang, Jiarui Meng, Runyi Li, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2405.15118v2.pdf)  
  摘要: 3D Gaussian Splatting (3DGS) has already become the emerging research focus in the fields of 3D scene reconstruction and novel view synthesis. Given that training a 3DGS requires a significant amount ...  
  关键词: gaussian splatting, 3d gaussian, real-time rendering, nerf  
- **[EvGGS: A Collaborative Learning Framework for Event-based Generalizable Gaussian Splatting](https://arxiv.org/abs/2405.14959v3)**  
  作者: Jiaxu Wang, Junhao He, Ziyi Zhang, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2405.14959v3.pdf)  
  摘要: Event cameras offer promising advantages such as high dynamic range and low latency, making them well-suited for challenging lighting conditions and fast-moving scenarios. However, reconstructing 3D s...  
  关键词: 3d gaussian, 3d reconstruction  
- **[Tele-Aloha: A Low-budget and High-authenticity Telepresence System Using Sparse RGB Cameras](https://arxiv.org/abs/2405.14866v1)**  
  作者: Hanzhang Tu, Ruizhi Shao, Xue Dong, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2405.14866v1.pdf)  
  摘要: In this paper, we present a low-budget and high-authenticity bidirectional telepresence system, Tele-Aloha, targeting peer-to-peer communication scenarios. Compared to previous systems, Tele-Aloha uti...  
  关键词: gaussian splatting  
- **[LDM: Large Tensorial SDF Model for Textured Mesh Generation](https://arxiv.org/abs/2405.14580v3)**  
  作者: Rengan Xie, Wenting Zheng, Kai Huang, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2405.14580v3.pdf)  
  摘要: Previous efforts have managed to generate production-ready 3D assets from text or images. However, these methods primarily employ NeRF or 3D Gaussian representations, which are not adept at producing ...  
  关键词: 3d gaussian, nerf  
- **[MagicDrive3D: Controllable 3D Generation for Any-View Rendering in Street Scenes](https://arxiv.org/abs/2405.14475v3)**  
  作者: Ruiyuan Gao, Kai Chen, Zhihao Li, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2405.14475v3.pdf)  
  摘要: While controllable generative models for images and videos have achieved remarkable success, high-quality models for 3D scenes, particularly in unbounded scenarios like autonomous driving, remain unde...  
  关键词: gaussian splatting  
- **[TIGER: Text-Instructed 3D Gaussian Retrieval and Coherent Editing](https://arxiv.org/abs/2405.14455v2)**  
  作者: Teng Xu, Jiamin Chen, Peng Chen, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2405.14455v2.pdf)  
  摘要: Editing objects within a scene is a critical functionality required across a broad spectrum of applications in computer vision and graphics. As 3D Gaussian Splatting (3DGS) emerges as a frontier in sc...  
  关键词: gaussian splatting, 3d gaussian  
- **[RoGs: Large Scale Road Surface Reconstruction with Meshgrid Gaussian](https://arxiv.org/abs/2405.14342v3)**  
  作者: Zhiheng Feng, Wenhua Wu, Tianchen Deng, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2405.14342v3.pdf)  
  摘要: Road surface reconstruction plays a crucial role in autonomous driving, which can be used for road lane perception and autolabeling. Recently, mesh-based road surface reconstruction algorithms have sh...  
  关键词: 3d gaussian  
- **[D-MiSo: Editing Dynamic 3D Scenes using Multi-Gaussians Soup](https://arxiv.org/abs/2405.14276v3)**  
  作者: Joanna Waczyńska, Piotr Borycki, Joanna Kaleta, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2405.14276v3.pdf)  
  摘要: Over the past years, we have observed an abundance of approaches for modeling dynamic 3D scenes using Gaussian Splatting (GS). Such solutions use GS to represent the scene's structure and the neural n...  
  关键词: gaussian splatting  
- **[NeuroGauss4D-PCI: 4D Neural Fields and Gaussian Deformation Fields for Point Cloud Interpolation](https://arxiv.org/abs/2405.14241v1)**  
  作者: Chaokang Jiang, Dalong Du, Jiuming Liu, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2405.14241v1.pdf) | [![Stars](https://img.shields.io/github/stars/jiangchaokang/NeuroGauss4D-PCI?style=social)](https://github.com/jiangchaokang/NeuroGauss4D-PCI)  
  摘要: Point Cloud Interpolation confronts challenges from point sparsity, complex spatiotemporal dynamics, and the difficulty of deriving complete 3D point clouds from sparse temporal information. This pape...  
- **[DOGS: Distributed-Oriented Gaussian Splatting for Large-Scale 3D Reconstruction Via Gaussian Consensus](https://arxiv.org/abs/2405.13943v2)**  
  作者: Yu Chen, Gim Hee Lee  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2405.13943v2.pdf) | [![Stars](https://img.shields.io/github/stars/AIBluefisher/DOGS?style=social)](https://github.com/AIBluefisher/DOGS)  
  摘要: The recent advances in 3D Gaussian Splatting (3DGS) show promising results on the novel view synthesis (NVS) task. With its superior rendering performance and high-fidelity rendering quality, 3DGS is ...  
  关键词: gaussian splatting, 3d gaussian, nerf  
- **[Monocular Gaussian SLAM with Language Extended Loop Closure](https://arxiv.org/abs/2405.13748v1)**  
  作者: Tian Lan, Qinwei Lin, Haoqian Wang  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2405.13748v1.pdf)  
  摘要: Recently,3DGaussianSplattinghasshowngreatpotentialin visual Simultaneous Localization And Mapping (SLAM). Existing methods have achieved encouraging results on RGB-D SLAM, but studies of the monocular...  
  关键词: 3d gaussian  
- **[Gaussian Time Machine: A Real-Time Rendering Methodology for Time-Variant Appearances](https://arxiv.org/abs/2405.13694v1)**  
  作者: Licheng Shen, Ho Ngai Chow, Lingyun Wang, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2405.13694v1.pdf)  
  摘要: Recent advancements in neural rendering techniques have significantly enhanced the fidelity of 3D reconstruction. Notably, the emergence of 3D Gaussian Splatting (3DGS) has marked a significant milest...  
  关键词: gaussian splatting, 3d gaussian, neural rendering, real-time rendering, 3d reconstruction  
- **[GS-ROR: 3D Gaussian Splatting for Reflective Object Relighting via SDF Priors](https://arxiv.org/abs/2406.18544v2)**  
  作者: Zuo-Liang Zhu, Beibei Wang, Jian Yang  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2406.18544v2.pdf)  
  摘要: 3D Gaussian Splatting (3DGS) has shown a powerful capability for novel view synthesis due to its detailed expressive ability and highly efficient rendering speed. Unfortunately, creating relightable 3...  
  关键词: gaussian splatting, 3d gaussian, nerf  
- **[MOSS: Motion-based 3D Clothed Human Synthesis from Monocular Video](https://arxiv.org/abs/2405.12806v3)**  
  作者: Hongsheng Wang, Xiang Cai, Xi Sun, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2405.12806v3.pdf)  
  摘要: Single-view clothed human reconstruction holds a central position in virtual reality applications, especially in contexts involving intricate human motions. It presents notable challenges in achieving...  
  关键词: gaussian splatting, nerf  
- **[LAGA: Layered 3D Avatar Generation and Customization via Gaussian Splatting](https://arxiv.org/abs/2405.12663v1)**  
  作者: Jia Gong, Shenyu Ji, Lin Geng Foo, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2405.12663v1.pdf)  
  摘要: Creating and customizing a 3D clothed avatar from textual descriptions is a critical and challenging task. Traditional methods often treat the human body and clothing as inseparable, limiting users' a...  
- **[Gaussian Control with Hierarchical Semantic Graphs in 3D Human Recovery](https://arxiv.org/abs/2405.12477v3)**  
  作者: Hongsheng Wang, Weiyue Zhang, Sihao Liu, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2405.12477v3.pdf)  
  摘要: Although 3D Gaussian Splatting (3DGS) has recently made progress in 3D human reconstruction, it primarily relies on 2D pixel-level supervision, overlooking the geometric complexity and topological rel...  
  关键词: gaussian splatting, 3d gaussian  
- **[GarmentDreamer: 3DGS Guided Garment Synthesis with Diverse Geometry and Texture Details](https://arxiv.org/abs/2405.12420v1)**  
  作者: Boqian Li, Xuan Li, Ying Jiang, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2405.12420v1.pdf)  
  摘要: Traditional 3D garment creation is labor-intensive, involving sketching, modeling, UV mapping, and texturing, which are time-consuming and costly. Recent advances in diffusion-based generative models ...  
  关键词: gaussian splatting, 3d gaussian  
- **[AtomGS: Atomizing Gaussian Splatting for High-Fidelity Radiance Field](https://arxiv.org/abs/2405.12369v3)**  
  作者: Rong Liu, Rui Xu, Yue Hu, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2405.12369v3.pdf)  
  摘要: 3D Gaussian Splatting (3DGS) has recently advanced radiance field reconstruction by offering superior capabilities for novel view synthesis and real-time rendering speed. However, its strategy of blen...  
  关键词: gaussian splatting, 3d gaussian, real-time rendering  
- **[MVSGaussian: Fast Generalizable Gaussian Splatting Reconstruction from Multi-View Stereo](https://arxiv.org/abs/2405.12218v3)**  
  作者: Tianqi Liu, Guangcong Wang, Shoukang Hu, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2405.12218v3.pdf)  
  摘要: We present MVSGaussian, a new generalizable 3D Gaussian representation approach derived from Multi-View Stereo (MVS) that can efficiently reconstruct unseen scenes. Specifically, 1) we leverage MVS to...  
  关键词: 3d gaussian, real-time rendering, nerf  
- **[Embracing Radiance Field Rendering in 6G: Over-the-Air Training and Inference with 3D Contents](https://arxiv.org/abs/2405.12155v2)**  
  作者: Guanlin Wu, Zhonghao Lyu, Juyong Zhang, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2405.12155v2.pdf)  
  摘要: The efficient representation, transmission, and reconstruction of three-dimensional (3D) contents are becoming increasingly important for sixth-generation (6G) networks that aim to merge virtual and p...  
  关键词: gaussian splatting, 3d gaussian, nerf  
- **[CoR-GS: Sparse-View 3D Gaussian Splatting via Co-Regularization](https://arxiv.org/abs/2405.12110v2)**  
  作者: Jiawei Zhang, Jiahe Li, Xiaohan Yu, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2405.12110v2.pdf)  
  摘要: 3D Gaussian Splatting (3DGS) creates a radiance field consisting of 3D Gaussians to represent a scene. With sparse training views, 3DGS easily suffers from overfitting, negatively impacting rendering....  
  关键词: gaussian splatting, 3d gaussian, nerf  
- **[Gaussian Head & Shoulders: High Fidelity Neural Upper Body Avatars with Anchor Gaussian Guided Texture Warping](https://arxiv.org/abs/2405.12069v2)**  
  作者: Tianhao Wu, Jing Yang, Zhilin Guo, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2405.12069v2.pdf)  
  摘要: By equipping the most recent 3D Gaussian Splatting representation with head 3D morphable models (3DMM), existing methods manage to create head avatars with high fidelity. However, most existing method...  
  关键词: gaussian splatting, 3d gaussian  
- **[MirrorGaussian: Reflecting 3D Gaussians for Reconstructing Mirror Reflections](https://arxiv.org/abs/2405.11921v1)**  
  作者: Jiayue Liu, Xiao Tang, Freeman Cheng, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2405.11921v1.pdf)  
  摘要: 3D Gaussian Splatting showcases notable advancements in photo-realistic and real-time novel view synthesis. However, it faces challenges in modeling mirror reflections, which exhibit substantial appea...  
  关键词: gaussian splatting, 3d gaussian, real-time rendering  
- **[Dreamer XL: Towards High-Resolution Text-to-3D Generation via Trajectory Score Matching](https://arxiv.org/abs/2405.11252v1)**  
  作者: Xingyu Miao, Haoran Duan, Varun Ojha, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2405.11252v1.pdf) | [![Stars](https://img.shields.io/github/stars/xingy038/Dreamer-XL?style=social)](https://github.com/xingy038/Dreamer-XL)  
  摘要: In this work, we propose a novel Trajectory Score Matching (TSM) method that aims to solve the pseudo ground truth inconsistency problem caused by the accumulated error in Interval Score Matching (ISM...  
  关键词: gaussian splatting, 3d gaussian  
- **[MotionGS : Compact Gaussian Splatting SLAM by Motion Filter](https://arxiv.org/abs/2405.11129v2)**  
  作者: Xinli Guo, Weidong Zhang, Ruonan Liu, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2405.11129v2.pdf)  
  摘要: With their high-fidelity scene representation capability, the attention of SLAM field is deeply attracted by the Neural Radiation Field (NeRF) and 3D Gaussian Splatting (3DGS). Recently, there has bee...  
  关键词: gaussian splatting, 3d gaussian, nerf  
- **[Enhanced 3D Urban Scene Reconstruction and Point Cloud Densification using Gaussian Splatting and Google Earth Imagery](https://arxiv.org/abs/2405.11021v2)**  
  作者: Kyle Gao, Dening Lu, Hongjie He, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2405.11021v2.pdf)  
  摘要: 3D urban scene reconstruction and modelling is a crucial research area in remote sensing with numerous applications in academia, commerce, industry, and administration. Recent advancements in view syn...  
  关键词: gaussian splatting, 3d gaussian, 3d reconstruction  
- **[ART3D: 3D Gaussian Splatting for Text-Guided Artistic Scenes Generation](https://arxiv.org/abs/2405.10508v1)**  
  作者: Pengzhi Li, Chengshuai Tang, Qinxuan Huang, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2405.10508v1.pdf)  
  摘要: In this paper, we explore the existing challenges in 3D artistic scene generation by introducing ART3D, a novel framework that combines diffusion models and 3D Gaussian splatting techniques. Our metho...  
  关键词: gaussian splatting, 3d gaussian  
- **[GS-Planner: A Gaussian-Splatting-based Planning Framework for Active High-Fidelity Reconstruction](https://arxiv.org/abs/2405.10142v2)**  
  作者: Rui Jin, Yuman Gao, Yingjian Wang, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2405.10142v2.pdf)  
  摘要: Active reconstruction technique enables robots to autonomously collect scene data for full coverage, relieving users from tedious and time-consuming data capturing process. However, designed based on ...  
  关键词: gaussian splatting, 3d gaussian  
- **[From NeRFs to Gaussian Splats, and Back](https://arxiv.org/abs/2405.09717v3)**  
  作者: Siming He, Zach Osman, Pratik Chaudhari  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2405.09717v3.pdf)  
  摘要: For robotics applications where there is a limited number of (typically ego-centric) views, parametric representations such as neural radiance fields (NeRFs) generalize better than non-parametric ones...  
  关键词: gaussian splatting, real-time rendering, nerf  
- **[GaussianVTON: 3D Human Virtual Try-ON via Multi-Stage Gaussian Splatting Editing with Image Prompting](https://arxiv.org/abs/2405.07472v2)**  
  作者: Haodong Chen, Yongle Huang, Haojian Huang, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2405.07472v2.pdf)  
  摘要: The increasing prominence of e-commerce has underscored the importance of Virtual Try-On (VTON). However, previous studies predominantly focus on the 2D realm and rely heavily on extensive data for tr...  
  关键词: gaussian splatting  
- **[LayGA: Layered Gaussian Avatars for Animatable Clothing Transfer](https://arxiv.org/abs/2405.07319v1)**  
  作者: Siyou Lin, Zhe Li, Zhaoqi Su, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2405.07319v1.pdf)  
  摘要: Animatable clothing transfer, aiming at dressing and animating garments across characters, is a challenging problem. Most human avatar works entangle the representations of the human body and clothing...  
  关键词: 3d gaussian  
- **[Direct Learning of Mesh and Appearance via 3D Gaussian Splatting](https://arxiv.org/abs/2405.06945v2)**  
  作者: Ancheng Lin, Jun Li  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2405.06945v2.pdf)  
  摘要: Accurately reconstructing a 3D scene including explicit geometry information is both attractive and challenging. Geometry reconstruction can benefit from incorporating differentiable appearance models...  
  关键词: gaussian splatting, 3d gaussian  
- **[OneTo3D: One Image to Re-editable Dynamic 3D Model and Video Generation](https://arxiv.org/abs/2405.06547v1)**  
  作者: Jinwei Lin  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2405.06547v1.pdf)  
  摘要: One image to editable dynamic 3D model and video generation is novel direction and change in the research area of single image to 3D representation or 3D reconstruction of image. Gaussian Splatting ha...  
  关键词: gaussian splatting, 3d reconstruction  
- **[I3DGS: Improve 3D Gaussian Splatting from Multiple Dimensions](https://arxiv.org/abs/2405.06408v1)**  
  作者: Jinwei Lin  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2405.06408v1.pdf)  
  摘要: 3D Gaussian Splatting is a novel method for 3D view synthesis, which can gain an implicit neural learning rendering result than the traditional neural rendering technology but keep the more high-defin...  
  关键词: gaussian splatting, 3d gaussian, neural rendering  
- **[MGS-SLAM: Monocular Sparse Tracking and Gaussian Mapping with Depth Smooth Regularization](https://arxiv.org/abs/2405.06241v2)**  
  作者: Pengcheng Zhu, Yaoming Zhuang, Baoquan Chen, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2405.06241v2.pdf)  
  摘要: This letter introduces a novel framework for dense Visual Simultaneous Localization and Mapping (VSLAM) based on Gaussian Splatting. Recently, SLAM based on Gaussian Splatting has shown promising resu...  
  关键词: gaussian splatting, 3d gaussian  
- **[DragGaussian: Enabling Drag-style Manipulation on 3D Gaussian Representation](https://arxiv.org/abs/2405.05800v1)**  
  作者: Sitian Shen, Jing Xu, Yuheng Yuan, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2405.05800v1.pdf)  
  摘要: User-friendly 3D object editing is a challenging task that has attracted significant attention recently. The limitations of direct 3D object editing without 2D prior knowledge have prompted increased ...  
  关键词: gaussian splatting, 3d gaussian, nerf  
- **[FastScene: Text-Driven Fast 3D Indoor Scene Generation via Panoramic Gaussian Splatting](https://arxiv.org/abs/2405.05768v1)**  
  作者: Yikun Ma, Dandan Zhan, Zhi Jin  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2405.05768v1.pdf)  
  摘要: Text-driven 3D indoor scene generation holds broad applications, ranging from gaming and smart homes to AR/VR applications. Fast and high-fidelity scene generation is paramount for ensuring user-frien...  
  关键词: gaussian splatting, 3d gaussian  
- **[NGM-SLAM: Gaussian Splatting SLAM with Radiance Field Submap](https://arxiv.org/abs/2405.05702v6)**  
  作者: Mingrui Li, Jingwei Huang, Lei Sun, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2405.05702v6.pdf)  
  摘要: SLAM systems based on Gaussian Splatting have garnered attention due to their capabilities for rapid real-time rendering and high-fidelity mapping. However, current Gaussian Splatting SLAM systems usu...  
  关键词: gaussian splatting, 3d gaussian, real-time rendering  
- **[Benchmarking Neural Radiance Fields for Autonomous Robots: An Overview](https://arxiv.org/abs/2405.05526v2)**  
  作者: Yuhang Ming, Xingrui Yang, Weihan Wang, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2405.05526v2.pdf)  
  摘要: Neural Radiance Fields (NeRF) have emerged as a powerful paradigm for 3D scene representation, offering high-fidelity renderings and reconstructions from a set of sparse and unstructured sensor data. ...  
  关键词: gaussian splatting, 3d gaussian, 3d reconstruction, nerf  
- **[GDGS: Gradient Domain Gaussian Splatting for Sparse Representation of Radiance Fields](https://arxiv.org/abs/2405.05446v1)**  
  作者: Yuanhao Gong  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2405.05446v1.pdf)  
  摘要: The 3D Gaussian splatting methods are getting popular. However, they work directly on the signal, leading to a dense representation of the signal. Even with some techniques such as pruning or distilla...  
  关键词: gaussian splatting, 3d gaussian  
- **[Splat-MOVER: Multi-Stage, Open-Vocabulary Robotic Manipulation via Editable Gaussian Splatting](https://arxiv.org/abs/2405.04378v4)**  
  作者: Ola Shorinwa, Johnathan Tucker, Aliyah Smith, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2405.04378v4.pdf)  
  摘要: We present Splat-MOVER, a modular robotics stack for open-vocabulary robotic manipulation, which leverages the editability of Gaussian Splatting (GSplat) scene representations to enable multi-stage ma...  
  关键词: gaussian splatting  
- **[A Construct-Optimize Approach to Sparse View Synthesis without Camera Pose](https://arxiv.org/abs/2405.03659v2)**  
  作者: Kaiwen Jiang, Yang Fu, Mukund Varma T, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2405.03659v2.pdf)  
  摘要: Novel view synthesis from a sparse set of input images is a challenging problem of great practical interest, especially when camera poses are absent or inaccurate. Direct optimization of camera poses ...  
  关键词: gaussian splatting, 3d gaussian  
- **[Gaussian Splatting: 3D Reconstruction and Novel View Synthesis, a Review](https://arxiv.org/abs/2405.03417v1)**  
  作者: Anurag Dalal, Daniel Hagen, Kjell G. Robbersmyr, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2405.03417v1.pdf)  
  摘要: Image-based 3D reconstruction is a challenging task that involves inferring the 3D shape of an object or scene from a set of input images. Learning-based methods have gained attention for their abilit...  
  关键词: gaussian splatting, 3d reconstruction  
- **[HoloGS: Instant Depth-based 3D Gaussian Splatting with Microsoft HoloLens 2](https://arxiv.org/abs/2405.02005v1)**  
  作者: Miriam Jäger, Theodor Kapler, Michael Feßenbecker, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2405.02005v1.pdf)  
  摘要: In the fields of photogrammetry, computer vision and computer graphics, the task of neural 3D scene reconstruction has led to the exploration of various techniques. Among these, 3D Gaussian Splatting ...  
  关键词: gaussian splatting, 3d gaussian  
- **[SimEndoGS: Efficient Data-driven Scene Simulation using Robotic Surgery Videos via Physics-embedded 3D Gaussians](https://arxiv.org/abs/2405.00956v3)**  
  作者: Zhenya Yang, Kai Chen, Yonghao Long, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2405.00956v3.pdf)  
  摘要: Surgical scene simulation plays a crucial role in surgical education and simulator-based robot learning. Traditional approaches for creating these environments with surgical scene involve a labor-inte...  
  关键词: 3d gaussian  
- **[Spectrally Pruned Gaussian Fields with Neural Compensation](https://arxiv.org/abs/2405.00676v1)**  
  作者: Runyi Yang, Zhenxin Zhu, Zhou Jiang, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2405.00676v1.pdf)  
  摘要: Recently, 3D Gaussian Splatting, as a novel 3D representation, has garnered attention for its fast rendering speed and high rendering quality. However, this comes with high memory consumption, e.g., a...  
  关键词: gaussian splatting, 3d gaussian, nerf  

### 2024年04月
- **[RTG-SLAM: Real-time 3D Reconstruction at Scale using Gaussian Splatting](https://arxiv.org/abs/2404.19706v3)**  
  作者: Zhexi Peng, Tianjia Shao, Yong Liu, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2404.19706v3.pdf)  
  摘要: We present Real-time Gaussian SLAM (RTG-SLAM), a real-time 3D reconstruction system with an RGBD camera for large-scale environments using Gaussian splatting. The system features a compact Gaussian re...  
  关键词: gaussian splatting, 3d reconstruction, nerf  
- **[GS-LRM: Large Reconstruction Model for 3D Gaussian Splatting](https://arxiv.org/abs/2404.19702v1)**  
  作者: Kai Zhang, Sai Bi, Hao Tan, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2404.19702v1.pdf)  
  摘要: We propose GS-LRM, a scalable large reconstruction model that can predict high-quality 3D Gaussian primitives from 2-4 posed sparse images in 0.23 seconds on single A100 GPU. Our model features a very...  
  关键词: 3d gaussian  
- **[MicroDreamer: Efficient 3D Generation in $\sim$20 Seconds by Score-based Iterative Reconstruction](https://arxiv.org/abs/2404.19525v3)**  
  作者: Luxi Chen, Zhengyi Wang, Zihan Zhou, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2404.19525v3.pdf) | [![Stars](https://img.shields.io/github/stars/ML-GSAI/MicroDreamer?style=social)](https://github.com/ML-GSAI/MicroDreamer)  
  摘要: Optimization-based approaches, such as score distillation sampling (SDS), show promise in zero-shot 3D generation but suffer from low efficiency, primarily due to the high number of function evaluatio...  
  关键词: gaussian splatting, 3d gaussian, 3d reconstruction  
- **[3D Gaussian Blendshapes for Head Avatar Animation](https://arxiv.org/abs/2404.19398v2)**  
  作者: Shengjie Ma, Yanlin Weng, Tianjia Shao, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2404.19398v2.pdf)  
  摘要: We introduce 3D Gaussian blendshapes for modeling photorealistic head avatars. Taking a monocular video as input, we learn a base head model of neutral expression, along with a group of expression ble...  
  关键词: gaussian splatting, 3d gaussian  
- **[SAGS: Structure-Aware 3D Gaussian Splatting](https://arxiv.org/abs/2404.19149v1)**  
  作者: Evangelos Ververas, Rolandos Alexandros Potamias, Jifei Song, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2404.19149v1.pdf)  
  摘要: Following the advent of NeRFs, 3D Gaussian Splatting (3D-GS) has paved the way to real-time neural rendering overcoming the computational burden of volumetric methods. Following the pioneering work of...  
  关键词: gaussian splatting, 3d gaussian, neural rendering, nerf  
- **[GSTalker: Real-time Audio-Driven Talking Face Generation via Deformable Gaussian Splatting](https://arxiv.org/abs/2404.19040v1)**  
  作者: Bo Chen, Shoukang Hu, Qi Chen, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2404.19040v1.pdf)  
  摘要: We present GStalker, a 3D audio-driven talking face generation model with Gaussian Splatting for both fast training (40 minutes) and real-time rendering (125 FPS) with a 3$\sim$5 minute video for trai...  
  关键词: gaussian splatting, 3d gaussian, real-time rendering, nerf  
- **[MeGA: Hybrid Mesh-Gaussian Head Avatar for High-Fidelity Rendering and Head Editing](https://arxiv.org/abs/2404.19026v1)**  
  作者: Cong Wang, Di Kang, He-Yi Sun, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2404.19026v1.pdf)  
  摘要: Creating high-fidelity head avatars from multi-view videos is a core issue for many AR/VR applications. However, existing methods usually struggle to obtain high-quality renderings for all different h...  
  关键词: gaussian splatting, 3d gaussian, neural rendering  
- **[DGE: Direct Gaussian 3D Editing by Consistent Multi-view Editing](https://arxiv.org/abs/2404.18929v3)**  
  作者: Minghao Chen, Iro Laina, Andrea Vedaldi  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2404.18929v3.pdf)  
  摘要: We consider the problem of editing 3D objects and scenes based on open-ended language instructions. A common approach to this problem is to use a 2D image generator or editor to guide the 3D editing p...  
  关键词: gaussian splatting, 3d gaussian  
- **[Bootstrap 3D Reconstructed Scenes from 3D Gaussian Splatting](https://arxiv.org/abs/2404.18669v2)**  
  作者: Yifei Gao, Jie Ou, Lei Wang, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2404.18669v2.pdf)  
  摘要: Recent developments in neural rendering techniques have greatly enhanced the rendering of photo-realistic 3D scenes across both academic and commercial fields. The latest method, known as 3D Gaussian ...  
  关键词: gaussian splatting, 3d gaussian, neural rendering, 3d reconstruction  
- **[3D Gaussian Splatting with Deferred Reflection](https://arxiv.org/abs/2404.18454v2)**  
  作者: Keyang Ye, Qiming Hou, Kun Zhou  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2404.18454v2.pdf)  
  摘要: The advent of neural and Gaussian-based radiance field methods have achieved great success in the field of novel view synthesis. However, specular reflection remains non-trivial, as the high frequency...  
  关键词: gaussian splatting  
- **[Reconstructing Satellites in 3D from Amateur Telescope Images](https://arxiv.org/abs/2404.18394v2)**  
  作者: Zhiming Chang, Boyang Liu, Yifei Xia, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2404.18394v2.pdf)  
  摘要: This paper proposes a framework for the 3D reconstruction of satellites in low-Earth orbit, utilizing videos captured by small amateur telescopes. The video data obtained from these telescopes differ ...  
  关键词: gaussian splatting, 3d gaussian, 3d reconstruction  
- **[High-quality Surface Reconstruction using Gaussian Surfels](https://arxiv.org/abs/2404.17774v2)**  
  作者: Pinxuan Dai, Jiamin Xu, Wenxiang Xie, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2404.17774v2.pdf)  
  摘要: We propose a novel point-based representation, Gaussian surfels, to combine the advantages of the flexible optimization procedure in 3D Gaussian points and the surface alignment property of surfels. T...  
  关键词: 3d gaussian  
- **[SLAM for Indoor Mapping of Wide Area Construction Environments](https://arxiv.org/abs/2404.17215v1)**  
  作者: Vincent Ress, Wei Zhang, David Skuddis, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2404.17215v1.pdf)  
  摘要: Simultaneous localization and mapping (SLAM), i.e., the reconstruction of the environment represented by a (3D) map and the concurrent pose estimation, has made astonishing progress. Meanwhile, large ...  
  关键词: gaussian splatting, 3d gaussian  
- **[Interactive3D: Create What You Want by Interactive 3D Generation](https://arxiv.org/abs/2404.16510v1)**  
  作者: Shaocong Dong, Lihe Ding, Zhanpeng Huang, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2404.16510v1.pdf)  
  摘要: 3D object generation has undergone significant advancements, yielding high-quality results. However, fall short of achieving precise user control, often yielding results that do not align with user ex...  
  关键词: gaussian splatting  
- **[LeanGaussian: Breaking Pixel or Point Cloud Correspondence in Modeling 3D Gaussians](https://arxiv.org/abs/2404.16323v2)**  
  作者: Jiamin Wu, Kenkun Liu, Han Gao, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2404.16323v2.pdf) | [![Stars](https://img.shields.io/github/stars/jwubz123/DIG3D?style=social)](https://github.com/jwubz123/DIG3D)  
  摘要: Rencently, Gaussian splatting has demonstrated significant success in novel view synthesis. Current methods often regress Gaussians with pixel or point cloud correspondence, linking each Gaussian with...  
  关键词: gaussian splatting, 3d gaussian, 3d reconstruction  
- **[GaussianTalker: Real-Time High-Fidelity Talking Head Synthesis with Audio-Driven 3D Gaussian Splatting](https://arxiv.org/abs/2404.16012v2)**  
  作者: Kyusun Cho, Joungbin Lee, Heeji Yoon, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2404.16012v2.pdf) | [![Stars](https://img.shields.io/github/stars/KU-CVLAB/GaussianTalker?style=social)](https://github.com/KU-CVLAB/GaussianTalker)  
  摘要: We propose GaussianTalker, a novel framework for real-time generation of pose-controllable talking heads. It leverages the fast rendering capabilities of 3D Gaussian Splatting (3DGS) while addressing ...  
  关键词: gaussian splatting, 3d gaussian  
- **[OMEGAS: Object Mesh Extraction from Large Scenes Guided by Gaussian Segmentation](https://arxiv.org/abs/2404.15891v4)**  
  作者: Lizhi Wang, Feng Zhou, Bo yu, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2404.15891v4.pdf) | [![Stars](https://img.shields.io/github/stars/CrystalWlz/OMEGAS?style=social)](https://github.com/CrystalWlz/OMEGAS)  
  摘要: Recent advancements in 3D reconstruction technologies have paved the way for high-quality and real-time rendering of complex 3D scenes. Despite these achievements, a notable challenge persists: it is ...  
  关键词: gaussian splatting, real-time rendering, 3d reconstruction  
- **[TalkingGaussian: Structure-Persistent 3D Talking Head Synthesis via Gaussian Splatting](https://arxiv.org/abs/2404.15264v2)**  
  作者: Jiahe Li, Jiawei Zhang, Xiao Bai, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2404.15264v2.pdf)  
  摘要: Radiance fields have demonstrated impressive performance in synthesizing lifelike 3D talking heads. However, due to the difficulty in fitting steep appearance changes, the prevailing paradigm that pre...  
  关键词: gaussian splatting  
- **[FlowMap: High-Quality Camera Poses, Intrinsics, and Depth via Gradient Descent](https://arxiv.org/abs/2404.15259v3)**  
  作者: Cameron Smith, David Charatan, Ayush Tewari, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2404.15259v3.pdf)  
  摘要: This paper introduces FlowMap, an end-to-end differentiable method that solves for precise camera poses, camera intrinsics, and per-frame dense depth of a video sequence. Our method performs per-video...  
  关键词: gaussian splatting  
- **[Guess The Unseen: Dynamic 3D Scene Reconstruction from Partial 2D Glimpses](https://arxiv.org/abs/2404.14410v1)**  
  作者: Inhee Lee, Byungjun Kim, Hanbyul Joo  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2404.14410v1.pdf)  
  摘要: In this paper, we present a method to reconstruct the world and multiple dynamic humans in 3D from a monocular video input. As a key idea, we represent both the world and multiple humans via the recen...  
  关键词: gaussian splatting, 3d gaussian  
- **[CLIP-GS: CLIP-Informed Gaussian Splatting for Real-time and View-consistent 3D Semantic Understanding](https://arxiv.org/abs/2404.14249v1)**  
  作者: Guibiao Liao, Jiankun Li, Zhenyu Bao, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2404.14249v1.pdf)  
  摘要: The recent 3D Gaussian Splatting (GS) exhibits high-quality and real-time synthesis of novel views in 3D scenes. Currently, it primarily focuses on geometry and appearance modeling, while lacking the ...  
  关键词: gaussian splatting, 3d gaussian, real-time rendering  
- **[GaussianTalker: Speaker-specific Talking Head Synthesis via 3D Gaussian Splatting](https://arxiv.org/abs/2404.14037v3)**  
  作者: Hongyun Yu, Zhan Qu, Qihang Yu, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2404.14037v3.pdf)  
  摘要: Recent works on audio-driven talking head synthesis using Neural Radiance Fields (NeRF) have achieved impressive results. However, due to inadequate pose and expression control caused by NeRF implicit...  
  关键词: gaussian splatting, 3d gaussian, real-time rendering, nerf  
- **[GScream: Learning 3D Geometry and Feature Consistent Gaussian Splatting for Object Removal](https://arxiv.org/abs/2404.13679v1)**  
  作者: Yuxin Wang, Qianyi Wu, Guofeng Zhang, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2404.13679v1.pdf)  
  摘要: This paper tackles the intricate challenge of object removal to update the radiance field using the 3D Gaussian Splatting. The main challenges of this task lie in the preservation of geometric consist...  
  关键词: gaussian splatting, 3d gaussian  
- **[Learn2Talk: 3D Talking Face Learns from 2D Talking Face](https://arxiv.org/abs/2404.12888v1)**  
  作者: Yixiang Zhuang, Baoping Cheng, Yao Cheng, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2404.12888v1.pdf)  
  摘要: Speech-driven facial animation methods usually contain two main classes, 3D and 2D talking face, both of which attract considerable research attention in recent years. However, to the best of our know...  
  关键词: gaussian splatting, 3d gaussian  
- **[Contrastive Gaussian Clustering: Weakly Supervised 3D Scene Segmentation](https://arxiv.org/abs/2404.12784v1)**  
  作者: Myrna C. Silva, Mahtab Dahaghin, Matteo Toso, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2404.12784v1.pdf)  
  摘要: We introduce Contrastive Gaussian Clustering, a novel approach capable of provide segmentation masks from any viewpoint and of enabling 3D segmentation of the scene. Recent works in novel-view synthes...  
  关键词: 3d gaussian  
- **[EfficientGS: Streamlining Gaussian Splatting for Large-Scale High-Resolution Scene Representation](https://arxiv.org/abs/2404.12777v1)**  
  作者: Wenkai Liu, Tao Guan, Bin Zhu, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2404.12777v1.pdf)  
  摘要: In the domain of 3D scene representation, 3D Gaussian Splatting (3DGS) has emerged as a pivotal technology. However, its application to large-scale, high-resolution scenes (exceeding 4k$\times$4k pixe...  
  关键词: gaussian splatting, 3d gaussian  
- **[Evaluating Alternatives to SFM Point Cloud Initialization for Gaussian Splatting](https://arxiv.org/abs/2404.12547v3)**  
  作者: Yalda Foroutan, Daniel Rebain, Kwang Moo Yi, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2404.12547v3.pdf)  
  摘要: 3D Gaussian Splatting has recently been embraced as a versatile and effective method for scene reconstruction and novel view synthesis, owing to its high-quality results and compatibility with hardwar...  
  关键词: gaussian splatting, 3d gaussian, nerf  
- **[Dynamic Gaussians Mesh: Consistent Mesh Reconstruction from Monocular Videos](https://arxiv.org/abs/2404.12379v2)**  
  作者: Isabella Liu, Hao Su, Xiaolong Wang  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2404.12379v2.pdf)  
  摘要: Modern 3D engines and graphics pipelines require mesh as a memory-efficient representation, which allows efficient rendering, geometry processing, texture editing, and many other downstream operations...  
  关键词: gaussian splatting, 3d gaussian  
- **[InFusion: Inpainting 3D Gaussians via Learning Depth Completion from Diffusion Prior](https://arxiv.org/abs/2404.11613v1)**  
  作者: Zhiheng Liu, Hao Ouyang, Qiuyu Wang, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2404.11613v1.pdf)  
  摘要: 3D Gaussians have recently emerged as an efficient representation for novel view synthesis. This work studies its editability with a particular focus on the inpainting task, which aims to supplement a...  
  关键词: 3d gaussian  
- **[RainyScape: Unsupervised Rainy Scene Reconstruction using Decoupled Neural Rendering](https://arxiv.org/abs/2404.11401v1)**  
  作者: Xianqiang Lyu, Hui Liu, Junhui Hou  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2404.11401v1.pdf)  
  摘要: We propose RainyScape, an unsupervised framework for reconstructing clean scenes from a collection of multi-view rainy images. RainyScape consists of two main modules: a neural rendering module and a ...  
  关键词: gaussian splatting, 3d gaussian, neural rendering  
- **[DeblurGS: Gaussian Splatting for Camera Motion Blur](https://arxiv.org/abs/2404.11358v2)**  
  作者: Jeongtaek Oh, Jaeyoung Chung, Dongwoo Lee, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2404.11358v2.pdf)  
  摘要: Although significant progress has been made in reconstructing sharp 3D scenes from motion-blurred images, a transition to real-world applications remains challenging. The primary obstacle stems from t...  
  关键词: gaussian splatting, 3d gaussian  
- **[Application of 3D Gaussian Splatting for Cinematic Anatomy on Consumer Class Devices](https://arxiv.org/abs/2404.11285v2)**  
  作者: Simon Niedermayr, Christoph Neuhauser, Kaloian Petkov, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2404.11285v2.pdf)  
  摘要: Interactive photorealistic rendering of 3D anatomy is used in medical education to explain the structure of the human body. It is currently restricted to frontal teaching scenarios, where even with a ...  
  关键词: gaussian splatting, 3d gaussian  
- **[Gaussian Opacity Fields: Efficient Adaptive Surface Reconstruction in Unbounded Scenes](https://arxiv.org/abs/2404.10772v2)**  
  作者: Zehao Yu, Torsten Sattler, Andreas Geiger  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2404.10772v2.pdf)  
  摘要: Recently, 3D Gaussian Splatting (3DGS) has demonstrated impressive novel view synthesis results, while allowing the rendering of high-resolution images in real-time. However, leveraging 3D Gaussians f...  
  关键词: gaussian splatting, 3d gaussian  
- **[Gaussian Splatting Decoder for 3D-aware Generative Adversarial Networks](https://arxiv.org/abs/2404.10625v2)**  
  作者: Florian Barthel, Arian Beckmann, Wieland Morgenstern, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2404.10625v2.pdf)  
  摘要: NeRF-based 3D-aware Generative Adversarial Networks (GANs) like EG3D or GIRAFFE have shown very high rendering quality under large representational variety. However, rendering with Neural Radiance Fie...  
  关键词: gaussian splatting, 3d gaussian, nerf  
- **[AbsGS: Recovering Fine Details for 3D Gaussian Splatting](https://arxiv.org/abs/2404.10484v1)**  
  作者: Zongxin Ye, Wenyu Li, Sidun Liu, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2404.10484v1.pdf)  
  摘要: 3D Gaussian Splatting (3D-GS) technique couples 3D Gaussian primitives with differentiable rasterization to achieve high-quality novel view synthesis results while providing advanced real-time renderi...  
  关键词: gaussian splatting, 3d gaussian, real-time rendering  
- **[SRGS: Super-Resolution 3D Gaussian Splatting](https://arxiv.org/abs/2404.10318v2)**  
  作者: Xiang Feng, Yongbo He, Yubo Wang, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2404.10318v2.pdf)  
  摘要: Recently, 3D Gaussian Splatting (3DGS) has gained popularity as a novel explicit 3D representation. This approach relies on the representation power of Gaussian primitives to provide a high-quality re...  
  关键词: gaussian splatting, 3d gaussian, nerf  
- **[LetsGo: Large-Scale Garage Modeling and Rendering via LiDAR-Assisted Gaussian Primitives](https://arxiv.org/abs/2404.09748v3)**  
  作者: Jiadi Cui, Junming Cao, Fuqiang Zhao, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2404.09748v3.pdf)  
  摘要: Large garages are ubiquitous yet intricate scenes that present unique challenges due to their monotonous colors, repetitive patterns, reflective surfaces, and transparent vehicle glass. Conventional S...  
  关键词: gaussian splatting, 3d gaussian, 3d reconstruction  
- **[3D Gaussian Splatting as Markov Chain Monte Carlo](https://arxiv.org/abs/2404.09591v2)**  
  作者: Shakiba Kheradmand, Daniel Rebain, Gopal Sharma, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2404.09591v2.pdf)  
  摘要: While 3D Gaussian Splatting has recently become popular for neural rendering, current methods rely on carefully engineered cloning and splitting strategies for placing Gaussians, which can lead to poo...  
  关键词: gaussian splatting, 3d gaussian, neural rendering  
- **[CompGS: Efficient 3D Scene Representation via Compressed Gaussian Splatting](https://arxiv.org/abs/2404.09458v1)**  
  作者: Xiangrui Liu, Xinju Wu, Pingping Zhang, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2404.09458v1.pdf)  
  摘要: Gaussian splatting, renowned for its exceptional rendering quality and efficiency, has emerged as a prominent technique in 3D scene representation. However, the substantial data volume of Gaussian spl...  
  关键词: gaussian splatting  
- **[DeferredGS: Decoupled and Editable Gaussian Splatting with Deferred Shading](https://arxiv.org/abs/2404.09412v2)**  
  作者: Tong Wu, Jia-Mu Sun, Yu-Kun Lai, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2404.09412v2.pdf)  
  摘要: Reconstructing and editing 3D objects and scenes both play crucial roles in computer graphics and computer vision. Neural radiance fields (NeRFs) can achieve realistic reconstruction and editing resul...  
  关键词: gaussian splatting, nerf  
- **[DreamScape: 3D Scene Creation via Gaussian Splatting joint Correlation Modeling](https://arxiv.org/abs/2404.09227v2)**  
  作者: Xuening Yuan, Hongyu Yang, Yueming Zhao, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2404.09227v2.pdf)  
  摘要: Recent progress in text-to-3D creation has been propelled by integrating the potent prior of Diffusion Models from text-to-image generation into the 3D domain. Nevertheless, generating 3D scenes chara...  
  关键词: gaussian splatting, 3d gaussian  
- **[EGGS: Edge Guided Gaussian Splatting for Radiance Fields](https://arxiv.org/abs/2404.09105v2)**  
  作者: Yuanhao Gong  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2404.09105v2.pdf)  
  摘要: The Gaussian splatting methods are getting popular. However, their loss function only contains the $\ell_1$ norm and the structural similarity between the rendered and input images, without considerin...  
  关键词: gaussian splatting, 3d reconstruction  
- **[LoopGaussian: Creating 3D Cinemagraph with Multi-view Images via Eulerian Motion Field](https://arxiv.org/abs/2404.08966v2)**  
  作者: Jiyang Li, Lechao Cheng, Zhangye Wang, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2404.08966v2.pdf)  
  摘要: Cinemagraph is a unique form of visual media that combines elements of still photography and subtle motion to create a captivating experience. However, the majority of videos generated by recent works...  
  关键词: gaussian splatting, 3d gaussian  
- **[OccGaussian: 3D Gaussian Splatting for Occluded Human Rendering](https://arxiv.org/abs/2404.08449v2)**  
  作者: Jingrui Ye, Zongkai Zhang, Yujiao Jiang, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2404.08449v2.pdf)  
  摘要: Rendering dynamic 3D human from monocular videos is crucial for various applications such as virtual reality and digital entertainment. Most methods assume the people is in an unobstructed scene, whil...  
  关键词: gaussian splatting, 3d gaussian, nerf  
- **[GoMAvatar: Efficient Animatable Human Modeling from Monocular Video Using Gaussians-on-Mesh](https://arxiv.org/abs/2404.07991v1)**  
  作者: Jing Wen, Xiaoming Zhao, Zhongzheng Ren, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2404.07991v1.pdf)  
  摘要: We introduce GoMAvatar, a novel approach for real-time, memory-efficient, high-quality animatable human modeling. GoMAvatar takes as input a single monocular video to create a digital avatar capable o...  
  关键词: gaussian splatting, real-time rendering  
- **[RealmDreamer: Text-Driven 3D Scene Generation with Inpainting and Depth Diffusion](https://arxiv.org/abs/2404.07199v1)**  
  作者: Jaidev Shriram, Alex Trevithick, Lingjie Liu, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2404.07199v1.pdf)  
  摘要: We introduce RealmDreamer, a technique for generation of general forward-facing 3D scenes from text descriptions. Our technique optimizes a 3D Gaussian Splatting representation to match complex text p...  
  关键词: gaussian splatting, 3d gaussian  
- **[Gaussian-LIC: Real-Time Photo-Realistic SLAM with Gaussian Splatting and LiDAR-Inertial-Camera Fusion](https://arxiv.org/abs/2404.06926v2)**  
  作者: Xiaolei Lang, Laijian Li, Chenming Wu, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2404.06926v2.pdf)  
  摘要: In this paper, we present a real-time photo-realistic SLAM method based on marrying Gaussian Splatting with LiDAR-Inertial-Camera SLAM. Most existing radiance-field-based SLAM systems mainly focus on ...  
  关键词: gaussian splatting, 3d gaussian  
- **[DreamScene360: Unconstrained Text-to-3D Scene Generation with Panoramic Gaussian Splatting](https://arxiv.org/abs/2404.06903v2)**  
  作者: Shijie Zhou, Zhiwen Fan, Dejia Xu, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2404.06903v2.pdf)  
  摘要: The increasing demand for virtual reality applications has highlighted the significance of crafting immersive 3D assets. We present a text-to-3D 360$^{\circ}$ scene generation pipeline that facilitate...  
  关键词: 3d gaussian  
- **[SplatPose & Detect: Pose-Agnostic 3D Anomaly Detection](https://arxiv.org/abs/2404.06832v1)**  
  作者: Mathis Kruse, Marco Rudolph, Dominik Woiwode, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2404.06832v1.pdf)  
  摘要: Detecting anomalies in images has become a well-explored problem in both academia and industry. State-of-the-art algorithms are able to detect defects in increasingly difficult settings and data modal...  
  关键词: gaussian splatting, 3d gaussian, nerf  
- **[Zero-shot Point Cloud Completion Via 2D Priors](https://arxiv.org/abs/2404.06814v1)**  
  作者: Tianxin Huang, Zhiwen Yan, Yuyang Zhao, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2404.06814v1.pdf)  
  摘要: 3D point cloud completion is designed to recover complete shapes from partially observed point clouds. Conventional completion methods typically depend on extensive point cloud data for training %, wi...  
  关键词: gaussian splatting  
- **[SpikeNVS: Enhancing Novel View Synthesis from Blurry Images via Spike Camera](https://arxiv.org/abs/2404.06710v3)**  
  作者: Gaole Dai, Zhenyu Wang, Qinwen Xu, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2404.06710v3.pdf)  
  摘要: One of the most critical factors in achieving sharp Novel View Synthesis (NVS) using neural field methods like Neural Radiance Fields (NeRF) and 3D Gaussian Splatting (3DGS) is the quality of the trai...  
  关键词: gaussian splatting, 3d gaussian, nerf  
- **[End-to-End Rate-Distortion Optimized 3D Gaussian Representation](https://arxiv.org/abs/2406.01597v2)**  
  作者: Henan Wang, Hanxin Zhu, Tianyu He, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2406.01597v2.pdf)  
  摘要: 3D Gaussian Splatting (3DGS) has become an emerging technique with remarkable potential in 3D representation and image rendering. However, the substantial storage overhead of 3DGS significantly impede...  
  关键词: gaussian splatting, 3d gaussian  
- **[3D Geometry-aware Deformable Gaussian Splatting for Dynamic View Synthesis](https://arxiv.org/abs/2404.06270v2)**  
  作者: Zhicheng Lu, Xiang Guo, Le Hui, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2404.06270v2.pdf)  
  摘要: In this paper, we propose a 3D geometry-aware deformable Gaussian Splatting method for dynamic view synthesis. Existing neural radiance fields (NeRF) based solutions learn the deformation in an implic...  
  关键词: gaussian splatting, 3d gaussian, nerf  
- **[Gaussian Pancakes: Geometrically-Regularized 3D Gaussian Splatting for Realistic Endoscopic Reconstruction](https://arxiv.org/abs/2404.06128v2)**  
  作者: Sierra Bonilla, Shuai Zhang, Dimitrios Psychogyios, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2404.06128v2.pdf)  
  摘要: Within colorectal cancer diagnostics, conventional colonoscopy techniques face critical limitations, including a limited field of view and a lack of depth information, which can impede the detection o...  
  关键词: gaussian splatting, 3d gaussian, 3d reconstruction  
- **[Revising Densification in Gaussian Splatting](https://arxiv.org/abs/2404.06109v1)**  
  作者: Samuel Rota Bulò, Lorenzo Porzi, Peter Kontschieder  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2404.06109v1.pdf)  
  摘要: In this paper, we address the limitations of Adaptive Density Control (ADC) in 3D Gaussian Splatting (3DGS), a scene representation method achieving high-quality, photorealistic results for novel view...  
  关键词: gaussian splatting, 3d gaussian  
- **[Hash3D: Training-free Acceleration for 3D Generation](https://arxiv.org/abs/2404.06091v1)**  
  作者: Xingyi Yang, Xinchao Wang  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2404.06091v1.pdf)  
  摘要: The evolution of 3D generative modeling has been notably propelled by the adoption of 2D diffusion models. Despite this progress, the cumbersome optimization process per se presents a critical hurdle ...  
  关键词: gaussian splatting, 3d gaussian  
- **[StylizedGS: Controllable Stylization for 3D Gaussian Splatting](https://arxiv.org/abs/2404.05220v2)**  
  作者: Dingxi Zhang, Yu-Jie Yuan, Zhuoxun Chen, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2404.05220v2.pdf)  
  摘要: As XR technology continues to advance rapidly, 3D generation and editing are increasingly crucial. Among these, stylization plays a key role in enhancing the appearance of 3D models. By utilizing styl...  
  关键词: gaussian splatting, 3d gaussian, nerf  
- **[Dual-Camera Smooth Zoom on Mobile Phones](https://arxiv.org/abs/2404.04908v2)**  
  作者: Renlong Wu, Zhilu Zhang, Yu Yang, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2404.04908v2.pdf) | [![Stars](https://img.shields.io/github/stars/ZcsrenlongZ/ZoomGS?style=social)](https://github.com/ZcsrenlongZ/ZoomGS)  
  摘要: When zooming between dual cameras on a mobile, noticeable jumps in geometric content and image color occur in the preview, inevitably affecting the user's zoom experience. In this work, we introduce a...  
  关键词: gaussian splatting  
- **[GauU-Scene V2: Assessing the Reliability of Image-Based Metrics with Expansive Lidar Image Dataset Using 3DGS and NeRF](https://arxiv.org/abs/2404.04880v2)**  
  作者: Butian Xiong, Nanjun Zheng, Junhua Liu, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2404.04880v2.pdf)  
  摘要: We introduce a novel, multimodal large-scale scene reconstruction benchmark that utilizes newly developed 3D representation approaches: Gaussian Splatting and Neural Radiance Fields (NeRF). Our expans...  
  关键词: gaussian splatting, nerf  
- **[Z-Splat: Z-Axis Gaussian Splatting for Camera-Sonar Fusion](https://arxiv.org/abs/2404.04687v2)**  
  作者: Ziyuan Qu, Omkar Vengurlekar, Mohamad Qadri, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2404.04687v2.pdf)  
  摘要: Differentiable 3D-Gaussian splatting (GS) is emerging as a prominent technique in computer vision and graphics for reconstructing 3D scenes. GS represents a scene as a set of 3D Gaussians with varying...  
  关键词: gaussian splatting, 3d gaussian  
- **[PhysAvatar: Learning the Physics of Dressed 3D Avatars from Visual Observations](https://arxiv.org/abs/2404.04421v2)**  
  作者: Yang Zheng, Qingqing Zhao, Guandao Yang, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2404.04421v2.pdf)  
  摘要: Modeling and rendering photorealistic avatars is of crucial importance in many applications. Existing methods that build a 3D avatar from visual observations, however, struggle to reconstruct clothed ...  
- **[Robust Gaussian Splatting](https://arxiv.org/abs/2404.04211v1)**  
  作者: François Darmon, Lorenzo Porzi, Samuel Rota-Bulò, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2404.04211v1.pdf)  
  摘要: In this paper, we address common error sources for 3D Gaussian Splatting (3DGS) including blur, imperfect camera poses, and color inconsistencies, with the goal of improving its robustness for practic...  
  关键词: gaussian splatting, 3d gaussian, nerf  
- **[MM-Gaussian: 3D Gaussian-based Multi-modal Fusion for Localization and Reconstruction in Unbounded Scenes](https://arxiv.org/abs/2404.04026v1)**  
  作者: Chenyang Wu, Yifan Duan, Xinran Zhang, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2404.04026v1.pdf)  
  摘要: Localization and mapping are critical tasks for various applications such as autonomous vehicles and robotics. The challenges posed by outdoor environments present particular complexities due to their...  
  关键词: 3d gaussian  
- **[SC4D: Sparse-Controlled Video-to-4D Generation and Motion Transfer](https://arxiv.org/abs/2404.03736v2)**  
  作者: Zijie Wu, Chaohui Yu, Yanqin Jiang, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2404.03736v2.pdf)  
  摘要: Recent advances in 2D/3D generative models enable the generation of dynamic 3D objects from a single-view video. Existing approaches utilize score distillation sampling to form the dynamic scene as dy...  
  关键词: 3d gaussian, nerf  
- **[Per-Gaussian Embedding-Based Deformation for Deformable 3D Gaussian Splatting](https://arxiv.org/abs/2404.03613v5)**  
  作者: Jeongmin Bae, Seoha Kim, Youngsik Yun, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2404.03613v5.pdf)  
  摘要: As 3D Gaussian Splatting (3DGS) provides fast and high-quality novel view synthesis, it is a natural extension to deform a canonical 3DGS to multiple frames for representing a dynamic scene. However, ...  
  关键词: gaussian splatting, 3d gaussian  
- **[DreamScene: 3D Gaussian-based Text-to-3D Scene Generation via Formation Pattern Sampling](https://arxiv.org/abs/2404.03575v2)**  
  作者: Haoran Li, Haolin Shi, Wenli Zhang, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2404.03575v2.pdf)  
  摘要: Text-to-3D scene generation holds immense potential for the gaming, film, and architecture sectors. Despite significant progress, existing methods struggle with maintaining high quality, consistency, ...  
  关键词: 3d gaussian  
- **[OmniGS: Fast Radiance Field Reconstruction using Omnidirectional Gaussian Splatting](https://arxiv.org/abs/2404.03202v5)**  
  作者: Longwei Li, Huajian Huang, Sai-Kit Yeung, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2404.03202v5.pdf)  
  摘要: Photorealistic reconstruction relying on 3D Gaussian Splatting has shown promising potential in various domains. However, the current 3D Gaussian Splatting system only supports radiance field reconstr...  
  关键词: gaussian splatting, 3d gaussian  
- **[GaSpCT: Gaussian Splatting for Novel CT Projection View Synthesis](https://arxiv.org/abs/2404.03126v1)**  
  作者: Emmanouil Nikolakakis, Utkarsh Gupta, Jonathan Vengosh, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2404.03126v1.pdf)  
  摘要: We present GaSpCT, a novel view synthesis and 3D scene representation method used to generate novel projection views for Computer Tomography (CT) scans. We adapt the Gaussian Splatting framework to en...  
  关键词: gaussian splatting  
- **[TCLC-GS: Tightly Coupled LiDAR-Camera Gaussian Splatting for Autonomous Driving](https://arxiv.org/abs/2404.02410v2)**  
  作者: Cheng Zhao, Su Sun, Ruoyu Wang, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2404.02410v2.pdf)  
  摘要: Most 3D Gaussian Splatting (3D-GS) based methods for urban scenes initialize 3D Gaussians directly with 3D LiDAR points, which not only underutilizes LiDAR data capabilities but also overlooks the pot...  
  关键词: gaussian splatting, 3d gaussian, 3d reconstruction  
- **[Sketch3D: Style-Consistent Guidance for Sketch-to-3D Generation](https://arxiv.org/abs/2404.01843v2)**  
  作者: Wangguandong Zheng, Haifeng Xia, Rui Chen, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2404.01843v2.pdf)  
  摘要: Recently, image-to-3D approaches have achieved significant results with a natural image as input. However, it is not always possible to access these enriched color input samples in practical applicati...  
  关键词: 3d gaussian  
- **[GS2Mesh: Surface Reconstruction from Gaussian Splatting via Novel Stereo Views](https://arxiv.org/abs/2404.01810v2)**  
  作者: Yaniv Wolf, Amit Bracha, Ron Kimmel  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2404.01810v2.pdf)  
  摘要: Recently, 3D Gaussian Splatting (3DGS) has emerged as an efficient approach for accurately representing scenes. However, despite its superior novel view synthesis capabilities, extracting the geometry...  
  关键词: gaussian splatting, 3d gaussian  
- **[Feature Splatting: Language-Driven Physics-Based Scene Synthesis and Editing](https://arxiv.org/abs/2404.01223v1)**  
  作者: Ri-Zhao Qiu, Ge Yang, Weijia Zeng, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2404.01223v1.pdf)  
  摘要: Scene representations using 3D Gaussian primitives have produced excellent results in modeling the appearance of static and dynamic 3D scenes. Many graphics applications, however, demand the ability t...  
  关键词: 3d gaussian  
- **[Mirror-3DGS: Incorporating Mirror Reflections into 3D Gaussian Splatting](https://arxiv.org/abs/2404.01168v1)**  
  作者: Jiarui Meng, Haijie Li, Yanmin Wu, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2404.01168v1.pdf)  
  摘要: 3D Gaussian Splatting (3DGS) has marked a significant breakthrough in the realm of 3D scene reconstruction and novel view synthesis. However, 3DGS, much like its predecessor Neural Radiance Fields (Ne...  
  关键词: gaussian splatting, 3d gaussian, nerf  
- **[CityGaussian: Real-time High-quality Large-Scale Scene Rendering with Gaussians](https://arxiv.org/abs/2404.01133v3)**  
  作者: Yang Liu, He Guan, Chuanchen Luo, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2404.01133v3.pdf)  
  摘要: The advancement of real-time 3D scene reconstruction and novel view synthesis has been significantly propelled by 3D Gaussian Splatting (3DGS). However, effectively training large-scale 3DGS and rende...  
  关键词: gaussian splatting, 3d gaussian, real-time rendering  
- **[HAHA: Highly Articulated Gaussian Human Avatars with Textured Mesh Prior](https://arxiv.org/abs/2404.01053v2)**  
  作者: David Svitov, Pietro Morerio, Lourdes Agapito, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2404.01053v2.pdf)  
  摘要: We present HAHA - a novel approach for animatable human avatar generation from monocular input videos. The proposed method relies on learning the trade-off between the use of Gaussian splatting and a ...  
  关键词: gaussian splatting  
- **[MM3DGS SLAM: Multi-modal 3D Gaussian Splatting for SLAM Using Vision, Depth, and Inertial Measurements](https://arxiv.org/abs/2404.00923v1)**  
  作者: Lisong C. Sun, Neel P. Bhatt, Jonathan C. Liu, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2404.00923v1.pdf)  
  摘要: Simultaneous localization and mapping is essential for position tracking and scene understanding. 3D Gaussian-based map representations enable photorealistic reconstruction and real-time rendering of ...  
  关键词: 3d gaussian, real-time rendering  

### 2024年03月
- **[3DGSR: Implicit Surface Reconstruction with 3D Gaussian Splatting](https://arxiv.org/abs/2404.00409v1)**  
  作者: Xiaoyang Lyu, Yang-Tian Sun, Yi-Hua Huang, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2404.00409v1.pdf) | [![Stars](https://img.shields.io/github/stars/CVMI-Lab/3DGSR?style=social)](https://github.com/CVMI-Lab/3DGSR)  
  摘要: In this paper, we present an implicit surface reconstruction method with 3D Gaussian Splatting (3DGS), namely 3DGSR, that allows for accurate 3D reconstruction with intricate details while inheriting ...  
  关键词: gaussian splatting, 3d gaussian, 3d reconstruction  
- **[InstantSplat: Sparse-view SfM-free Gaussian Splatting in Seconds](https://arxiv.org/abs/2403.20309v3)**  
  作者: Zhiwen Fan, Wenyan Cong, Kairun Wen, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2403.20309v3.pdf)  
  摘要: While novel view synthesis (NVS) from a sparse set of images has advanced significantly in 3D computer vision, it relies on precise initial estimation of camera parameters using Structure-from-Motion ...  
  关键词: gaussian splatting, 3d gaussian  
- **[Snap-it, Tap-it, Splat-it: Tactile-Informed 3D Gaussian Splatting for Reconstructing Challenging Surfaces](https://arxiv.org/abs/2403.20275v1)**  
  作者: Mauro Comi, Alessio Tonioni, Max Yang, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2403.20275v1.pdf)  
  摘要: Touch and vision go hand in hand, mutually enhancing our ability to understand the world. From a research perspective, the problem of mixing touch and vision is underexplored and presents interesting ...  
  关键词: 3d gaussian  
- **[HGS-Mapping: Online Dense Mapping Using Hybrid Gaussian Representation in Urban Scenes](https://arxiv.org/abs/2403.20159v1)**  
  作者: Ke Wu, Kaizhao Zhang, Zhiwei Zhang, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2403.20159v1.pdf)  
  摘要: Online dense mapping of urban scenes forms a fundamental cornerstone for scene understanding and navigation of autonomous vehicles. Recent advancements in mapping methods are mainly based on NeRF, who...  
  关键词: gaussian splatting, 3d gaussian, nerf  
- **[SGD: Street View Synthesis with Gaussian Splatting and Diffusion Prior](https://arxiv.org/abs/2403.20079v1)**  
  作者: Zhongrui Yu, Haoran Wang, Jinze Yang, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2403.20079v1.pdf)  
  摘要: Novel View Synthesis (NVS) for street scenes play a critical role in the autonomous driving simulation. The current mainstream technique to achieve it is neural rendering, such as Neural Radiance Fiel...  
  关键词: gaussian splatting, 3d gaussian, neural rendering, nerf  
- **[HO-Gaussian: Hybrid Optimization of 3D Gaussian Splatting for Urban Scenes](https://arxiv.org/abs/2403.20032v1)**  
  作者: Zhuopeng Li, Yilin Zhang, Chenming Wu, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2403.20032v1.pdf)  
  摘要: The rapid growth of 3D Gaussian Splatting (3DGS) has revolutionized neural rendering, enabling real-time production of high-quality renderings. However, the previous 3DGS-based methods have limitation...  
  关键词: gaussian splatting, 3d gaussian, neural rendering  
- **[GauStudio: A Modular Framework for 3D Gaussian Splatting and Beyond](https://arxiv.org/abs/2403.19632v1)**  
  作者: Chongjie Ye, Yinyu Nie, Jiahao Chang, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2403.19632v1.pdf)  
  摘要: We present GauStudio, a novel modular framework for modeling 3D Gaussian Splatting (3DGS) to provide standardized, plug-and-play components for users to easily customize and implement a 3DGS pipeline....  
  关键词: gaussian splatting, 3d gaussian  
- **[SA-GS: Scale-Adaptive Gaussian Splatting for Training-Free Anti-Aliasing](https://arxiv.org/abs/2403.19615v1)**  
  作者: Xiaowei Song, Jv Zheng, Shiran Yuan, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2403.19615v1.pdf) | [![Stars](https://img.shields.io/github/stars/zsy1987/SA-GS?style=social)](https://github.com/zsy1987/SA-GS)  
  摘要: In this paper, we present a Scale-adaptive method for Anti-aliasing Gaussian Splatting (SA-GS). While the state-of-the-art method Mip-Splatting needs modifying the training procedure of Gaussian splat...  
  关键词: gaussian splatting  
- **[TOGS: Gaussian Splatting with Temporal Opacity Offset for Real-Time 4D DSA Rendering](https://arxiv.org/abs/2403.19586v2)**  
  作者: Shuai Zhang, Huangxuan Zhao, Zhenghong Zhou, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2403.19586v2.pdf) | [![Stars](https://img.shields.io/github/stars/hustvl/TOGS?style=social)](https://github.com/hustvl/TOGS)  
  摘要: Four-dimensional Digital Subtraction Angiography (4D DSA) is a medical imaging technique that provides a series of 2D images captured at different stages and angles during the process of contrast agen...  
  关键词: gaussian splatting, real-time rendering  
- **[CoherentGS: Sparse Novel View Synthesis with Coherent 3D Gaussians](https://arxiv.org/abs/2403.19495v1)**  
  作者: Avinash Paliwal, Wei Ye, Jinhui Xiong, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2403.19495v1.pdf)  
  摘要: The field of 3D reconstruction from images has rapidly evolved in the past few years, first with the introduction of Neural Radiance Field (NeRF) and more recently with 3D Gaussian Splatting (3DGS). T...  
  关键词: gaussian splatting, 3d gaussian, 3d reconstruction, nerf  
- **[Gamba: Marry Gaussian Splatting with Mamba for single view 3D reconstruction](https://arxiv.org/abs/2403.18795v3)**  
  作者: Qiuhong Shen, Zike Wu, Xuanyu Yi, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2403.18795v3.pdf)  
  摘要: We tackle the challenge of efficiently reconstructing a 3D asset from a single image at millisecond speed. Existing methods for single-image 3D reconstruction are primarily based on Score Distillation...  
  关键词: gaussian splatting, 3d gaussian, 3d reconstruction  
- **[SplatFace: Gaussian Splat Face Reconstruction Leveraging an Optimizable Surface](https://arxiv.org/abs/2403.18784v3)**  
  作者: Jiahao Luo, Jing Liu, James Davis  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2403.18784v3.pdf)  
  摘要: We present SplatFace, a novel Gaussian splatting framework designed for 3D human face reconstruction without reliance on accurate pre-determined geometry. Our method is designed to simultaneously deli...  
  关键词: gaussian splatting, 3d reconstruction  
- **[Modeling uncertainty for Gaussian Splatting](https://arxiv.org/abs/2403.18476v1)**  
  作者: Luca Savant, Diego Valsesia, Enrico Magli  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2403.18476v1.pdf)  
  摘要: We present Stochastic Gaussian Splatting (SGS): the first framework for uncertainty estimation using Gaussian Splatting (GS). GS recently advanced the novel-view synthesis field by achieving impressiv...  
  关键词: gaussian splatting, nerf  
- **[EgoLifter: Open-world 3D Segmentation for Egocentric Perception](https://arxiv.org/abs/2403.18118v2)**  
  作者: Qiao Gu, Zhaoyang Lv, Duncan Frost, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2403.18118v2.pdf)  
  摘要: In this paper we present EgoLifter, a novel system that can automatically segment scenes captured from egocentric sensors into a complete decomposition of individual 3D objects. The system is specific...  
  关键词: 3d gaussian, 3d reconstruction  
- **[Octree-GS: Towards Consistent Real-time Rendering with LOD-Structured 3D Gaussians](https://arxiv.org/abs/2403.17898v2)**  
  作者: Kerui Ren, Lihan Jiang, Tao Lu, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2403.17898v2.pdf)  
  摘要: The recent 3D Gaussian splatting (3D-GS) has shown remarkable rendering fidelity and efficiency compared to NeRF-based neural scene representations. While demonstrating the potential for real-time ren...  
  关键词: gaussian splatting, 3d gaussian, real-time rendering, nerf  
- **[2D Gaussian Splatting for Geometrically Accurate Radiance Fields](https://arxiv.org/abs/2403.17888v2)**  
  作者: Binbin Huang, Zehao Yu, Anpei Chen, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2403.17888v2.pdf)  
  摘要: 3D Gaussian Splatting (3DGS) has recently revolutionized radiance field reconstruction, achieving high quality novel view synthesis and fast rendering speed without baking. However, 3DGS fails to accu...  
  关键词: gaussian splatting, 3d gaussian, real-time rendering  
- **[DN-Splatter: Depth and Normal Priors for Gaussian Splatting and Meshing](https://arxiv.org/abs/2403.17822v3)**  
  作者: Matias Turkulainen, Xuqian Ren, Iaroslav Melekhov, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2403.17822v3.pdf)  
  摘要: High-fidelity 3D reconstruction of common indoor scenes is crucial for VR and AR applications. 3D Gaussian splatting, a novel differentiable rendering technique, has achieved state-of-the-art novel vi...  
  关键词: gaussian splatting, 3d gaussian, 3d reconstruction  
- **[DreamPolisher: Towards High-Quality Text-to-3D Generation via Geometric Diffusion](https://arxiv.org/abs/2403.17237v1)**  
  作者: Yuanze Lin, Ronald Clark, Philip Torr  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2403.17237v1.pdf)  
  摘要: We present DreamPolisher, a novel Gaussian Splatting based method with geometric guidance, tailored to learn cross-view consistency and intricate detail from textual descriptions. While recent progres...  
  关键词: gaussian splatting  
- **[GSDF: 3DGS Meets SDF for Improved Rendering and Reconstruction](https://arxiv.org/abs/2403.16964v2)**  
  作者: Mulin Yu, Tao Lu, Linning Xu, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2403.16964v2.pdf)  
  摘要: Presenting a 3D scene from multiview images remains a core and long-standing challenge in computer vision and computer graphics. Two main requirements lie in rendering and reconstruction. Notably, SOT...  
  关键词: gaussian splatting, 3d gaussian, neural rendering  
- **[latentSplat: Autoencoding Variational Gaussians for Fast Generalizable 3D Reconstruction](https://arxiv.org/abs/2403.16292v2)**  
  作者: Christopher Wewer, Kevin Raj, Eddy Ilg, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2403.16292v2.pdf)  
  摘要: We present latentSplat, a method to predict semantic Gaussians in a 3D latent space that can be splatted and decoded by a light-weight generative 2D architecture. Existing methods for generalizable 3D...  
  关键词: 3d gaussian, 3d reconstruction  
- **[CG-SLAM: Efficient Dense RGB-D SLAM in a Consistent Uncertainty-aware 3D Gaussian Field](https://arxiv.org/abs/2403.16095v1)**  
  作者: Jiarui Hu, Xianhao Chen, Boyin Feng, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2403.16095v1.pdf)  
  摘要: Recently neural radiance fields (NeRF) have been widely exploited as 3D representations for dense simultaneous localization and mapping (SLAM). Despite their notable successes in surface modeling and ...  
  关键词: gaussian splatting, 3d gaussian, nerf  
- **[Gaussian in the Wild: 3D Gaussian Splatting for Unconstrained Image Collections](https://arxiv.org/abs/2403.15704v2)**  
  作者: Dongbin Zhang, Chuming Wang, Weitao Wang, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2403.15704v2.pdf)  
  摘要: Novel view synthesis from unconstrained in-the-wild images remains a meaningful but challenging task. The photometric variation and transient occluders in those unconstrained images make it difficult ...  
  关键词: 3d gaussian, nerf  
- **[Semantic Gaussians: Open-Vocabulary Scene Understanding with 3D Gaussian Splatting](https://arxiv.org/abs/2403.15624v2)**  
  作者: Jun Guo, Xiaojian Ma, Yue Fan, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2403.15624v2.pdf)  
  摘要: Open-vocabulary 3D scene understanding presents a significant challenge in computer vision, with wide-ranging applications in embodied agents and augmented reality systems. Existing methods adopt neur...  
  关键词: gaussian splatting, 3d gaussian  
- **[Pixel-GS: Density Control with Pixel-aware Gradient for 3D Gaussian Splatting](https://arxiv.org/abs/2403.15530v1)**  
  作者: Zheng Zhang, Wenbo Hu, Yixing Lao, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2403.15530v1.pdf)  
  摘要: 3D Gaussian Splatting (3DGS) has demonstrated impressive novel view synthesis results while advancing real-time rendering performance. However, it relies heavily on the quality of the initial point cl...  
  关键词: gaussian splatting, 3d gaussian, real-time rendering, nerf  
- **[EndoGSLAM: Real-Time Dense Reconstruction and Tracking in Endoscopic Surgeries using Gaussian Splatting](https://arxiv.org/abs/2403.15124v1)**  
  作者: Kailing Wang, Chen Yang, Yuehao Wang, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2403.15124v1.pdf)  
  摘要: Precise camera tracking, high-fidelity 3D tissue reconstruction, and real-time online visualization are critical for intrabody medical imaging devices such as endoscopes and capsule robots. However, e...  
- **[STAG4D: Spatial-Temporal Anchored Generative 4D Gaussians](https://arxiv.org/abs/2403.14939v1)**  
  作者: Yifei Zeng, Yanqin Jiang, Siyu Zhu, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2403.14939v1.pdf)  
  摘要: Recent progress in pre-trained diffusion models and 3D generation have spurred interest in 4D content creation. However, achieving high-fidelity 4D generation with spatial-temporal consistency remains...  
  关键词: gaussian splatting, 3d gaussian  
- **[MVSplat: Efficient 3D Gaussian Splatting from Sparse Multi-View Images](https://arxiv.org/abs/2403.14627v2)**  
  作者: Yuedong Chen, Haofei Xu, Chuanxia Zheng, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2403.14627v2.pdf)  
  摘要: We introduce MVSplat, an efficient model that, given sparse multi-view images as input, predicts clean feed-forward 3D Gaussians. To accurately localize the Gaussian centers, we build a cost volume re...  
  关键词: 3d gaussian  
- **[GRM: Large Gaussian Reconstruction Model for Efficient 3D Reconstruction and Generation](https://arxiv.org/abs/2403.14621v1)**  
  作者: Yinghao Xu, Zifan Shi, Wang Yifan, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2403.14621v1.pdf)  
  摘要: We introduce GRM, a large-scale reconstructor capable of recovering a 3D asset from sparse-view images in around 0.1s. GRM is a feed-forward transformer-based model that efficiently incorporates multi...  
  关键词: 3d gaussian  
- **[Gaussian Frosting: Editable Complex Radiance Fields with Real-Time Rendering](https://arxiv.org/abs/2403.14554v1)**  
  作者: Antoine Guédon, Vincent Lepetit  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2403.14554v1.pdf)  
  摘要: We propose Gaussian Frosting, a novel mesh-based representation for high-quality rendering and editing of complex 3D effects in real-time. Our approach builds on the recent 3D Gaussian Splatting frame...  
  关键词: gaussian splatting, 3d gaussian  
- **[HAC: Hash-grid Assisted Context for 3D Gaussian Splatting Compression](https://arxiv.org/abs/2403.14530v3)**  
  作者: Yihang Chen, Qianyi Wu, Weiyao Lin, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2403.14530v3.pdf) | [![Stars](https://img.shields.io/github/stars/YihangChen-ee/HAC?style=social)](https://github.com/YihangChen-ee/HAC)  
  摘要: 3D Gaussian Splatting (3DGS) has emerged as a promising framework for novel view synthesis, boasting rapid rendering speed with high fidelity. However, the substantial Gaussians and their associated a...  
  关键词: gaussian splatting, 3d gaussian  
- **[SyncTweedies: A General Generative Framework Based on Synchronized Diffusions](https://arxiv.org/abs/2403.14370v4)**  
  作者: Jaihoon Kim, Juil Koo, Kyeongmin Yeo, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2403.14370v4.pdf)  
  摘要: We introduce a general framework for generating diverse visual content, including ambiguous images, panorama images, mesh textures, and Gaussian splat textures, by synchronizing multiple diffusion pro...  
- **[Isotropic Gaussian Splatting for Real-Time Radiance Field Rendering](https://arxiv.org/abs/2403.14244v1)**  
  作者: Yuanhao Gong, Lantao Yu, Guanghui Yue  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2403.14244v1.pdf)  
  摘要: The 3D Gaussian splatting method has drawn a lot of attention, thanks to its high performance in training and high quality of the rendered image. However, it uses anisotropic Gaussian kernels to repre...  
  关键词: gaussian splatting, 3d gaussian, 3d reconstruction  
- **[Mini-Splatting: Representing Scenes with a Constrained Number of Gaussians](https://arxiv.org/abs/2403.14166v3)**  
  作者: Guangchi Fang, Bing Wang  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2403.14166v3.pdf) | [![Stars](https://img.shields.io/github/stars/fatPeter/mini-splatting?style=social)](https://github.com/fatPeter/mini-splatting)  
  摘要: In this study, we explore the challenge of efficiently representing scenes with a constrained number of Gaussians. Our analysis shifts from traditional graphics and 2D computer vision to the perspecti...  
- **[RadSplat: Radiance Field-Informed Gaussian Splatting for Robust Real-Time Rendering with 900+ FPS](https://arxiv.org/abs/2403.13806v1)**  
  作者: Michael Niemeyer, Fabian Manhardt, Marie-Julie Rakotosaona, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2403.13806v1.pdf)  
  摘要: Recent advances in view synthesis and real-time rendering have achieved photorealistic quality at impressive rendering speeds. While Radiance Field-based methods achieve state-of-the-art quality in ch...  
  关键词: gaussian splatting, real-time rendering  
- **[Gaussian Splatting on the Move: Blur and Rolling Shutter Compensation for Natural Camera Motion](https://arxiv.org/abs/2403.13327v3)**  
  作者: Otto Seiskari, Jerry Ylilammi, Valtteri Kaatrasalo, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2403.13327v3.pdf)  
  摘要: High-quality scene reconstruction and novel view synthesis based on Gaussian Splatting (3DGS) typically require steady, high-quality photographs, often impractical to capture with handheld cameras. We...  
  关键词: gaussian splatting  
- **[GVGEN: Text-to-3D Generation with Volumetric Representation](https://arxiv.org/abs/2403.12957v2)**  
  作者: Xianglong He, Junyi Chen, Sida Peng, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2403.12957v2.pdf)  
  摘要: In recent years, 3D Gaussian splatting has emerged as a powerful technique for 3D reconstruction and generation, known for its fast and high-quality rendering capabilities. To address these shortcomin...  
  关键词: gaussian splatting, 3d gaussian, 3d reconstruction  
- **[HUGS: Holistic Urban 3D Scene Understanding via Gaussian Splatting](https://arxiv.org/abs/2403.12722v1)**  
  作者: Hongyu Zhou, Jiahao Shao, Lu Xu, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2403.12722v1.pdf)  
  摘要: Holistic understanding of urban scenes based on RGB images is a challenging yet important problem. It encompasses understanding both the geometry and appearance to enable novel view synthesis, parsing...  
  关键词: gaussian splatting, 3d gaussian  
- **[RGBD GS-ICP SLAM](https://arxiv.org/abs/2403.12550v2)**  
  作者: Seongbo Ha, Jiung Yeon, Hyeonwoo Yu  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2403.12550v2.pdf)  
  摘要: Simultaneous Localization and Mapping (SLAM) with dense representation plays a key role in robotics, Virtual Reality (VR), and Augmented Reality (AR) applications. Recent advancements in dense represe...  
  关键词: gaussian splatting, 3d gaussian  
- **[High-Fidelity SLAM Using Gaussian Splatting with Rendering-Guided Densification and Regularized Optimization](https://arxiv.org/abs/2403.12535v2)**  
  作者: Shuo Sun, Malcolm Mielle, Achim J. Lilienthal, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2403.12535v2.pdf)  
  摘要: We propose a dense RGBD SLAM system based on 3D Gaussian Splatting that provides metrically accurate pose tracking and visually realistic reconstruction. To this end, we first propose a Gaussian densi...  
  关键词: gaussian splatting, 3d gaussian  
- **[GaussianFlow: Splatting Gaussian Dynamics for 4D Content Creation](https://arxiv.org/abs/2403.12365v2)**  
  作者: Quankai Gao, Qiangeng Xu, Zhe Cao, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2403.12365v2.pdf)  
  摘要: Creating 4D fields of Gaussian Splatting from images or videos is a challenging task due to its under-constrained nature. While the optimization can draw photometric reference from the input videos or...  
  关键词: gaussian splatting, 3d gaussian  
- **[VideoMV: Consistent Multi-View Generation Based on Large Video Generative Model](https://arxiv.org/abs/2403.12010v1)**  
  作者: Qi Zuo, Xiaodong Gu, Lingteng Qiu, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2403.12010v1.pdf)  
  摘要: Generating multi-view images based on text or single-image prompts is a critical capability for the creation of 3D content. Two fundamental questions on this topic are what data we use for training an...  
  关键词: 3d gaussian  
- **[Reinforcement Learning with Generalizable Gaussian Splatting](https://arxiv.org/abs/2404.07950v3)**  
  作者: Jiaxu Wang, Qiang Zhang, Jingkai Sun, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2404.07950v3.pdf)  
  摘要: An excellent representation is crucial for reinforcement learning (RL) performance, especially in vision-based reinforcement learning tasks. The quality of the environment representation directly infl...  
  关键词: gaussian splatting, 3d gaussian  
- **[View-Consistent 3D Editing with Gaussian Splatting](https://arxiv.org/abs/2403.11868v9)**  
  作者: Yuxuan Wang, Xuanyu Yi, Zike Wu, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2403.11868v9.pdf)  
  摘要: The advent of 3D Gaussian Splatting (3DGS) has revolutionized 3D editing, offering efficient, high-fidelity rendering and enabling precise local manipulations. Currently, diffusion-based 2D editing mo...  
  关键词: gaussian splatting, 3d gaussian  
- **[BAD-Gaussians: Bundle Adjusted Deblur Gaussian Splatting](https://arxiv.org/abs/2403.11831v2)**  
  作者: Lingzhe Zhao, Peng Wang, Peidong Liu  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2403.11831v2.pdf)  
  摘要: While neural rendering has demonstrated impressive capabilities in 3D scene reconstruction and novel view synthesis, it heavily relies on high-quality sharp images and accurate camera poses. Numerous ...  
  关键词: gaussian splatting, 3d gaussian, neural rendering, real-time rendering, nerf  
- **[NEDS-SLAM: A Neural Explicit Dense Semantic SLAM Framework using 3D Gaussian Splatting](https://arxiv.org/abs/2403.11679v3)**  
  作者: Yiming Ji, Yang Liu, Guanghu Xie, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2403.11679v3.pdf)  
  摘要: We propose NEDS-SLAM, a dense semantic SLAM system based on 3D Gaussian representation, that enables robust 3D semantic mapping, accurate camera tracking, and high-quality rendering in real-time. In t...  
  关键词: gaussian splatting, 3d gaussian  
- **[GaussNav: Gaussian Splatting for Visual Navigation](https://arxiv.org/abs/2403.11625v2)**  
  作者: Xiaohan Lei, Min Wang, Wengang Zhou, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2403.11625v2.pdf)  
  摘要: In embodied vision, Instance ImageGoal Navigation (IIN) requires an agent to locate a specific object depicted in a goal image within an unexplored environment. The primary difficulty of IIN stems fro...  
  关键词: gaussian splatting, 3d gaussian  
- **[UV Gaussians: Joint Learning of Mesh Deformation and Gaussian Textures for Human Avatar Modeling](https://arxiv.org/abs/2403.11589v1)**  
  作者: Yujiao Jiang, Qingmin Liao, Xiaoyu Li, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2403.11589v1.pdf)  
  摘要: Reconstructing photo-realistic drivable human avatars from multi-view image sequences has been a popular and challenging topic in the field of computer vision and graphics. While existing NeRF-based m...  
  关键词: 3d gaussian, nerf  
- **[3DGS-Calib: 3D Gaussian Splatting for Multimodal SpatioTemporal Calibration](https://arxiv.org/abs/2403.11577v2)**  
  作者: Quentin Herau, Moussab Bennehar, Arthur Moreau, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2403.11577v2.pdf)  
  摘要: Reliable multimodal sensor fusion algorithms require accurate spatiotemporal calibration. Recently, targetless calibration techniques based on implicit neural representations have proven to provide pr...  
  关键词: gaussian splatting, 3d gaussian  
- **[Fed3DGS: Scalable 3D Gaussian Splatting with Federated Learning](https://arxiv.org/abs/2403.11460v1)**  
  作者: Teppei Suzuki  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2403.11460v1.pdf)  
  摘要: In this work, we present Fed3DGS, a scalable 3D reconstruction framework based on 3D Gaussian splatting (3DGS) with federated learning. Existing city-scale reconstruction methods typically adopt a cen...  
  关键词: gaussian splatting, 3d gaussian, 3d reconstruction  
- **[Bridging 3D Gaussian and Mesh for Freeview Video Rendering](https://arxiv.org/abs/2403.11453v1)**  
  作者: Yuting Xiao, Xuan Wang, Jiafei Li, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2403.11453v1.pdf)  
  摘要: This is only a preview version of GauMesh. Recently, primitive-based rendering has been proven to achieve convincing results in solving the problem of modeling and rendering the 3D dynamic scene from ...  
  关键词: gaussian splatting, 3d gaussian  
- **[Motion-aware 3D Gaussian Splatting for Efficient Dynamic Scene Reconstruction](https://arxiv.org/abs/2403.11447v1)**  
  作者: Zhiyang Guo, Wengang Zhou, Li Li, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2403.11447v1.pdf)  
  摘要: 3D Gaussian Splatting (3DGS) has become an emerging tool for dynamic scene reconstruction. However, existing methods focus mainly on extending static 3DGS into a time-variant representation, while ove...  
  关键词: gaussian splatting, 3d gaussian  
- **[BAGS: Building Animatable Gaussian Splatting from a Monocular Video with Diffusion Priors](https://arxiv.org/abs/2403.11427v1)**  
  作者: Tingyang Zhang, Qingzhe Gao, Weiyu Li, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2403.11427v1.pdf)  
  摘要: Animatable 3D reconstruction has significant applications across various fields, primarily relying on artists' handcraft creation. Recently, some studies have successfully constructed animatable 3D mo...  
  关键词: gaussian splatting, 3d gaussian, 3d reconstruction  
- **[Beyond Uncertainty: Risk-Aware Active View Acquisition for Safe Robot Navigation and 3D Scene Understanding with FisherRF](https://arxiv.org/abs/2403.11396v1)**  
  作者: Guangyi Liu, Wen Jiang, Boshu Lei, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2403.11396v1.pdf)  
  摘要: This work proposes a novel approach to bolster both the robot's risk assessment and safety measures while deepening its understanding of 3D scenes, which is achieved by leveraging Radiance Field (RF) ...  
  关键词: gaussian splatting, 3d gaussian  
- **[3DGS-ReLoc: 3D Gaussian Splatting for Map Representation and Visual ReLocalization](https://arxiv.org/abs/2403.11367v1)**  
  作者: Peng Jiang, Gaurav Pandey, Srikanth Saripalli  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2403.11367v1.pdf)  
  摘要: This paper presents a novel system designed for 3D mapping and visual relocalization using 3D Gaussian Splatting. Our proposed method uses LiDAR and camera data to create accurate and visually plausib...  
  关键词: gaussian splatting, 3d gaussian  
- **[Creating Seamless 3D Maps Using Radiance Fields](https://arxiv.org/abs/2403.11364v1)**  
  作者: Sai Tarun Sathyan, Thomas B. Kinsman  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2403.11364v1.pdf)  
  摘要: It is desirable to create 3D object models and 3D maps from 2D input images for applications such as navigation, virtual tourism, and urban planning. The traditional methods of creating 3D maps, (such...  
  关键词: gaussian splatting, nerf  
- **[GeoGaussian: Geometry-aware Gaussian Splatting for Scene Rendering](https://arxiv.org/abs/2403.11324v2)**  
  作者: Yanyan Li, Chenyu Lyu, Yan Di, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2403.11324v2.pdf)  
  摘要: During the Gaussian Splatting optimization process, the scene's geometry can gradually deteriorate if its structure is not deliberately preserved, especially in non-textured regions such as walls, cei...  
  关键词: gaussian splatting, 3d gaussian  
- **[BrightDreamer: Generic 3D Gaussian Generative Framework for Fast Text-to-3D Synthesis](https://arxiv.org/abs/2403.11273v2)**  
  作者: Lutao Jiang, Xu Zheng, Yuanhuiyi Lyu, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2403.11273v2.pdf)  
  摘要: Text-to-3D synthesis has recently seen intriguing advances by combining the text-to-image priors with 3D representation methods, e.g., 3D Gaussian Splatting (3D GS), via Score Distillation Sampling (S...  
  关键词: gaussian splatting, 3d gaussian  
- **[Compact 3D Gaussian Splatting For Dense Visual SLAM](https://arxiv.org/abs/2403.11247v2)**  
  作者: Tianchen Deng, Yaohui Chen, Leyan Zhang, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2403.11247v2.pdf)  
  摘要: Recent work has shown that 3D Gaussian-based SLAM enables high-quality reconstruction, accurate pose estimation, and real-time rendering of scenes. However, these approaches are built on a tremendous ...  
  关键词: gaussian splatting, 3d gaussian, real-time rendering  
- **[Recent Advances in 3D Gaussian Splatting](https://arxiv.org/abs/2403.11134v2)**  
  作者: Tong Wu, Yu-Jie Yuan, Ling-Xiao Zhang, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2403.11134v2.pdf)  
  摘要: The emergence of 3D Gaussian Splatting (3DGS) has greatly accelerated the rendering speed of novel view synthesis. Unlike neural implicit representations like Neural Radiance Fields (NeRF) that repres...  
  关键词: gaussian splatting, 3d gaussian, 3d reconstruction, nerf  
- **[Analytic-Splatting: Anti-Aliased 3D Gaussian Splatting via Analytic Integration](https://arxiv.org/abs/2403.11056v2)**  
  作者: Zhihao Liang, Qi Zhang, Wenbo Hu, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2403.11056v2.pdf)  
  摘要: The 3D Gaussian Splatting (3DGS) gained its popularity recently by combining the advantages of both primitive-based and volumetric 3D representations, resulting in improved quality and efficiency for ...  
  关键词: gaussian splatting, 3d gaussian  
- **[DarkGS: Learning Neural Illumination and 3D Gaussians Relighting for Robotic Exploration in the Dark](https://arxiv.org/abs/2403.10814v2)**  
  作者: Tianyi Zhang, Kaining Huang, Weiming Zhi, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2403.10814v2.pdf)  
  摘要: Humans have the remarkable ability to construct consistent mental models of an environment, even under limited or varying levels of illumination. We wish to endow robots with this same capability. In ...  
  关键词: 3d gaussian  
- **[GS-Pose: Generalizable Segmentation-based 6D Object Pose Estimation with 3D Gaussian Splatting](https://arxiv.org/abs/2403.10683v2)**  
  作者: Dingding Cai, Janne Heikkilä, Esa Rahtu  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2403.10683v2.pdf)  
  摘要: This paper introduces GS-Pose, a unified framework for localizing and estimating the 6D pose of novel objects. GS-Pose begins with a set of posed RGB images of a previously unseen object and builds th...  
  关键词: gaussian splatting, 3d gaussian  
- **[SWAG: Splatting in the Wild images with Appearance-conditioned Gaussians](https://arxiv.org/abs/2403.10427v2)**  
  作者: Hiba Dahmani, Moussab Bennehar, Nathan Piasco, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2403.10427v2.pdf)  
  摘要: Implicit neural representation methods have shown impressive advancements in learning 3D scenes from unstructured in-the-wild photo collections but are still limited by the large computational cost of...  
  关键词: gaussian splatting, 3d gaussian  
- **[GeoGS3D: Single-view 3D Reconstruction via Geometric-aware Diffusion Model and Gaussian Splatting](https://arxiv.org/abs/2403.10242v2)**  
  作者: Qijun Feng, Zhen Xing, Zuxuan Wu, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2403.10242v2.pdf)  
  摘要: We introduce GeoGS3D, a novel two-stage framework for reconstructing detailed 3D objects from single-view images. Inspired by the success of pre-trained 2D diffusion models, our method incorporates an...  
  关键词: gaussian splatting  
- **[GGRt: Towards Pose-free Generalizable 3D Gaussian Splatting in Real-time](https://arxiv.org/abs/2403.10147v2)**  
  作者: Hao Li, Yuanyuan Gao, Chenming Wu, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2403.10147v2.pdf)  
  摘要: This paper presents GGRt, a novel approach to generalizable novel view synthesis that alleviates the need for real camera poses, complexity in processing high-resolution images, and lengthy optimizati...  
  关键词: gaussian splatting, 3d gaussian, real-time rendering, nerf  
- **[Texture-GS: Disentangling the Geometry and Texture for 3D Gaussian Splatting Editing](https://arxiv.org/abs/2403.10050v1)**  
  作者: Tian-Xing Xu, Wenbo Hu, Yu-Kun Lai, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2403.10050v1.pdf)  
  摘要: 3D Gaussian splatting, emerging as a groundbreaking approach, has drawn increasing attention for its capabilities of high-fidelity reconstruction and real-time rendering. However, it couples the appea...  
  关键词: gaussian splatting, 3d gaussian, real-time rendering  
- **[Controllable Text-to-3D Generation via Surface-Aligned Gaussian Splatting](https://arxiv.org/abs/2403.09981v2)**  
  作者: Zhiqi Li, Yiming Chen, Lingzhe Zhao, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2403.09981v2.pdf)  
  摘要: While text-to-3D and image-to-3D generation tasks have received considerable attention, one important but under-explored field between them is controllable text-to-3D generation, which we mainly focus...  
  关键词: 3d gaussian  
- **[Den-SOFT: Dense Space-Oriented Light Field DataseT for 6-DOF Immersive Experience](https://arxiv.org/abs/2403.09973v1)**  
  作者: Xiaohang Yu, Zhengxian Yang, Shi Pan, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2403.09973v1.pdf)  
  摘要: We have built a custom mobile multi-camera large-space dense light field capture system, which provides a series of high-quality and sufficiently dense light field images for various scenarios. Our ai...  
  关键词: 3d gaussian, 3d reconstruction, nerf  
- **[Touch-GS: Visual-Tactile Supervised 3D Gaussian Splatting](https://arxiv.org/abs/2403.09875v3)**  
  作者: Aiden Swann, Matthew Strong, Won Kyung Do, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2403.09875v3.pdf)  
  摘要: In this work, we propose a novel method to supervise 3D Gaussian Splatting (3DGS) scenes using optical tactile sensors. Optical tactile sensors have become widespread in their use in robotics for mani...  
  关键词: gaussian splatting, 3d gaussian  
- **[GaussianGrasper: 3D Language Gaussian Splatting for Open-vocabulary Robotic Grasping](https://arxiv.org/abs/2403.09637v1)**  
  作者: Yuhang Zheng, Xiangyu Chen, Yupeng Zheng, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2403.09637v1.pdf) | [![Stars](https://img.shields.io/github/stars/MrSecant/GaussianGrasper?style=social)](https://github.com/MrSecant/GaussianGrasper)  
  摘要: Constructing a 3D scene capable of accommodating open-ended language queries, is a pivotal pursuit, particularly within the domain of robotics. Such technology facilitates robots in executing object m...  
  关键词: gaussian splatting, 3d gaussian, nerf  
- **[Reconstruction and Simulation of Elastic Objects with Spring-Mass 3D Gaussians](https://arxiv.org/abs/2403.09434v3)**  
  作者: Licheng Zhong, Hong-Xing Yu, Jiajun Wu, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2403.09434v3.pdf)  
  摘要: Reconstructing and simulating elastic objects from visual observations is crucial for applications in computer vision and robotics. Existing methods, such as 3D Gaussians, model 3D appearance and geom...  
  关键词: 3d gaussian  
- **[Relaxing Accurate Initialization Constraint for 3D Gaussian Splatting](https://arxiv.org/abs/2403.09413v2)**  
  作者: Jaewoo Jung, Jisang Han, Honggyu An, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2403.09413v2.pdf)  
  摘要: 3D Gaussian splatting (3DGS) has recently demonstrated impressive capabilities in real-time novel view synthesis and 3D reconstruction. However, 3DGS heavily depends on the accurate initialization der...  
  关键词: gaussian splatting, 3d gaussian, 3d reconstruction  
- **[Hyper-3DG: Text-to-3D Gaussian Generation via Hypergraph](https://arxiv.org/abs/2403.09236v1)**  
  作者: Donglin Di, Jiahui Yang, Chaofan Luo, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2403.09236v1.pdf) | [![Stars](https://img.shields.io/github/stars/yjhboy/Hyper3DG?style=social)](https://github.com/yjhboy/Hyper3DG)  
  摘要: Text-to-3D generation represents an exciting field that has seen rapid advancements, facilitating the transformation of textual descriptions into detailed 3D models. However, current progress often ne...  
  关键词: 3d gaussian  
- **[A New Split Algorithm for 3D Gaussian Splatting](https://arxiv.org/abs/2403.09143v1)**  
  作者: Qiyuan Feng, Gengchen Cao, Haoxiang Chen, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2403.09143v1.pdf)  
  摘要: 3D Gaussian splatting models, as a novel explicit 3D representation, have been applied in many domains recently, such as explicit geometric editing and geometry generation. Progress has been rapid. Ho...  
  关键词: gaussian splatting, 3d gaussian  
- **[GaussCtrl: Multi-View Consistent Text-Driven 3D Gaussian Splatting Editing](https://arxiv.org/abs/2403.08733v4)**  
  作者: Jing Wu, Jia-Wang Bian, Xinghui Li, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2403.08733v4.pdf)  
  摘要: We propose GaussCtrl, a text-driven method to edit a 3D scene reconstructed by the 3D Gaussian Splatting (3DGS).   Our method first renders a collection of images by using the 3DGS and edits them by u...  
  关键词: gaussian splatting, 3d gaussian  
- **[GaussianImage: 1000 FPS Image Representation and Compression by 2D Gaussian Splatting](https://arxiv.org/abs/2403.08551v5)**  
  作者: Xinjie Zhang, Xingtong Ge, Tongda Xu, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2403.08551v5.pdf) | [![Stars](https://img.shields.io/github/stars/Xinjie-Q/GaussianImage?style=social)](https://github.com/Xinjie-Q/GaussianImage)  
  摘要: Implicit neural representations (INRs) recently achieved great success in image representation and compression, offering high visual quality and fast rendering speeds with 10-1000 FPS, assuming suffic...  
  关键词: gaussian splatting  
- **[Gaussian Splatting in Style](https://arxiv.org/abs/2403.08498v2)**  
  作者: Abhishek Saroha, Mariia Gladkova, Cecilia Curreli, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2403.08498v2.pdf)  
  摘要: 3D scene stylization extends the work of neural style transfer to 3D. A vital challenge in this problem is to maintain the uniformity of the stylized appearance across multiple views. A vast majority ...  
  关键词: gaussian splatting, 3d gaussian, nerf  
- **[ManiGaussian: Dynamic Gaussian Splatting for Multi-task Robotic Manipulation](https://arxiv.org/abs/2403.08321v2)**  
  作者: Guanxing Lu, Shiyi Zhang, Ziwei Wang, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2403.08321v2.pdf)  
  摘要: Performing language-conditioned robotic manipulation tasks in unstructured environments is highly demanded for general intelligent robots. Conventional robotic manipulation methods usually learn seman...  
  关键词: gaussian splatting  
- **[StyleGaussian: Instant 3D Style Transfer with Gaussian Splatting](https://arxiv.org/abs/2403.07807v1)**  
  作者: Kunhao Liu, Fangneng Zhan, Muyu Xu, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2403.07807v1.pdf)  
  摘要: We introduce StyleGaussian, a novel 3D style transfer technique that allows instant transfer of any image's style to a 3D scene at 10 frames per second (fps). Leveraging 3D Gaussian Splatting (3DGS), ...  
  关键词: gaussian splatting, 3d gaussian, real-time rendering  
- **[SemGauss-SLAM: Dense Semantic Gaussian Splatting SLAM](https://arxiv.org/abs/2403.07494v3)**  
  作者: Siting Zhu, Renjie Qin, Guangming Wang, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2403.07494v3.pdf)  
  摘要: We propose SemGauss-SLAM, a dense semantic SLAM system utilizing 3D Gaussian representation, that enables accurate 3D semantic mapping, robust camera tracking, and high-quality rendering simultaneousl...  
  关键词: 3d gaussian  
- **[DNGaussian: Optimizing Sparse-View 3D Gaussian Radiance Fields with Global-Local Depth Normalization](https://arxiv.org/abs/2403.06912v3)**  
  作者: Jiahe Li, Jiawei Zhang, Xiao Bai, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2403.06912v3.pdf)  
  摘要: Radiance fields have demonstrated impressive performance in synthesizing novel views from sparse input views, yet prevailing methods suffer from high training costs and slow inference speed. This pape...  
  关键词: gaussian splatting, 3d gaussian  
- **[FreGS: 3D Gaussian Splatting with Progressive Frequency Regularization](https://arxiv.org/abs/2403.06908v2)**  
  作者: Jiahui Zhang, Fangneng Zhan, Muyu Xu, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2403.06908v2.pdf)  
  摘要: 3D Gaussian splatting has achieved very impressive performance in real-time novel view synthesis. However, it often suffers from over-reconstruction during Gaussian densification where high-variance i...  
  关键词: gaussian splatting, 3d gaussian, nerf  
- **[V3D: Video Diffusion Models are Effective 3D Generators](https://arxiv.org/abs/2403.06738v1)**  
  作者: Zilong Chen, Yikai Wang, Feng Wang, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2403.06738v1.pdf) | [![Stars](https://img.shields.io/github/stars/heheyas/V3D?style=social)](https://github.com/heheyas/V3D)  
  摘要: Automatic 3D generation has recently attracted widespread attention. Recent methods have greatly accelerated the generation speed, but usually produce less-detailed objects due to limited model capaci...  
  关键词: 3d gaussian  
- **[GSEdit: Efficient Text-Guided Editing of 3D Objects via Gaussian Splatting](https://arxiv.org/abs/2403.05154v2)**  
  作者: Francesco Palandra, Andrea Sanchietti, Daniele Baieri, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2403.05154v2.pdf)  
  摘要: We present GSEdit, a pipeline for text-guided 3D object editing based on Gaussian Splatting models. Our method enables the editing of the style and appearance of 3D objects without altering their main...  
  关键词: gaussian splatting, nerf  
- **[SplattingAvatar: Realistic Real-Time Human Avatars with Mesh-Embedded Gaussian Splatting](https://arxiv.org/abs/2403.05087v1)**  
  作者: Zhijing Shao, Zhaolong Wang, Zhuang Li, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2403.05087v1.pdf)  
  摘要: We present SplattingAvatar, a hybrid 3D representation of photorealistic human avatars with Gaussian Splatting embedded on a triangle mesh, which renders over 300 FPS on a modern GPU and 30 FPS on a m...  
  关键词: gaussian splatting  
- **[BAGS: Blur Agnostic Gaussian Splatting through Multi-Scale Kernel Modeling](https://arxiv.org/abs/2403.04926v2)**  
  作者: Cheng Peng, Yutao Tang, Yifan Zhou, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2403.04926v2.pdf)  
  摘要: Recent efforts in using 3D Gaussians for scene reconstruction and novel view synthesis can achieve impressive results on curated benchmarks; however, images captured in real life are often blurry. In ...  
  关键词: gaussian splatting, 3d gaussian  
- **[Radiative Gaussian Splatting for Efficient X-ray Novel View Synthesis](https://arxiv.org/abs/2403.04116v3)**  
  作者: Yuanhao Cai, Yixun Liang, Jiahao Wang, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2403.04116v3.pdf) | [![Stars](https://img.shields.io/github/stars/caiyuanhao1998/X-Gaussian?style=social)](https://github.com/caiyuanhao1998/X-Gaussian)  
  摘要: X-ray is widely applied for transmission imaging due to its stronger penetration than natural light. When rendering novel view X-ray projections, existing methods mainly based on NeRF suffer from long...  
  关键词: gaussian splatting, 3d gaussian, nerf  
- **[Online Photon Guiding with 3D Gaussians for Caustics Rendering](https://arxiv.org/abs/2403.03641v2)**  
  作者: Jiawei Huang, Hajime Tanaka, Taku Komura, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2403.03641v2.pdf)  
  摘要: In production rendering systems, caustics are typically rendered via photon mapping and gathering, a process often hindered by insufficient photon density. In this paper, we propose a novel photon gui...  
  关键词: 3d gaussian  
- **[Splat-Nav: Safe Real-Time Robot Navigation in Gaussian Splatting Maps](https://arxiv.org/abs/2403.02751v2)**  
  作者: Timothy Chen, Ola Shorinwa, Joseph Bruno, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2403.02751v2.pdf)  
  摘要: We present Splat-Nav, a real-time navigation pipeline designed to work with environment representations generated by Gaussian Splatting (GSplat), a popular emerging 3D scene representation from comput...  
  关键词: gaussian splatting, nerf  
- **[3DGStream: On-the-Fly Training of 3D Gaussians for Efficient Streaming of Photo-Realistic Free-Viewpoint Videos](https://arxiv.org/abs/2403.01444v4)**  
  作者: Jiakai Sun, Han Jiao, Guangyuan Li, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2403.01444v4.pdf)  
  摘要: Constructing photo-realistic Free-Viewpoint Videos (FVVs) of dynamic scenes from multi-view videos remains a challenging endeavor. Despite the remarkable advancements achieved by current neural render...  
  关键词: 3d gaussian, neural rendering, real-time rendering  

### 2024年02月
- **[3D Gaussian Model for Animation and Texturing](https://arxiv.org/abs/2402.19441v1)**  
  作者: Xiangzhi Eric Wang, Zackary P. T. Sin  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2402.19441v1.pdf)  
  摘要: 3D Gaussian Splatting has made a marked impact on neural rendering by achieving impressive fidelity and performance. Despite this achievement, however, it is not readily applicable to developing inter...  
  关键词: gaussian splatting, 3d gaussian, neural rendering  
- **[VastGaussian: Vast 3D Gaussians for Large Scene Reconstruction](https://arxiv.org/abs/2402.17427v1)**  
  作者: Jiaqi Lin, Zhihao Li, Xiao Tang, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2402.17427v1.pdf)  
  摘要: Existing NeRF-based methods for large scene reconstruction often have limitations in visual quality and rendering speed. While the recent 3D Gaussian Splatting works well on small-scale and object-cen...  
  关键词: gaussian splatting, 3d gaussian, real-time rendering, nerf  
- **[GVA: Reconstructing Vivid 3D Gaussian Avatars from Monocular Videos](https://arxiv.org/abs/2402.16607v2)**  
  作者: Xinqi Liu, Chenming Wu, Jialun Liu, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2402.16607v2.pdf)  
  摘要: In this paper, we present a novel method that facilitates the creation of vivid 3D Gaussian avatars from monocular video inputs (GVA). Our innovation lies in addressing the intricate challenges of del...  
  关键词: 3d gaussian  
- **[Spec-Gaussian: Anisotropic View-Dependent Appearance for 3D Gaussian Splatting](https://arxiv.org/abs/2402.15870v2)**  
  作者: Ziyi Yang, Xinyu Gao, Yangtian Sun, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2402.15870v2.pdf)  
  摘要: The recent advancements in 3D Gaussian splatting (3D-GS) have not only facilitated real-time rendering through modern GPU rasterization pipelines but have also attained state-of-the-art rendering qual...  
  关键词: gaussian splatting, 3d gaussian, real-time rendering  
- **[GaussianPro: 3D Gaussian Splatting with Progressive Propagation](https://arxiv.org/abs/2402.14650v1)**  
  作者: Kai Cheng, Xiaoxiao Long, Kaizhi Yang, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2402.14650v1.pdf)  
  摘要: The advent of 3D Gaussian Splatting (3DGS) has recently brought about a revolution in the field of neural rendering, facilitating high-quality renderings at real-time speed. However, 3DGS heavily depe...  
  关键词: gaussian splatting, 3d gaussian, neural rendering  
- **[Identifying Unnecessary 3D Gaussians using Clustering for Fast Rendering of 3D Gaussian Splatting](https://arxiv.org/abs/2402.13827v2)**  
  作者: Joongho Jo, Hyeongwon Kim, Jongsun Park  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2402.13827v2.pdf)  
  摘要: 3D Gaussian splatting (3D-GS) is a new rendering approach that outperforms the neural radiance field (NeRF) in terms of both speed and image quality. 3D-GS represents 3D scenes by utilizing millions o...  
  关键词: gaussian splatting, 3d gaussian, nerf  
- **[How NeRFs and 3D Gaussian Splatting are Reshaping SLAM: a Survey](https://arxiv.org/abs/2402.13255v2)**  
  作者: Fabio Tosi, Youmin Zhang, Ziren Gong, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2402.13255v2.pdf)  
  摘要: Over the past two decades, research in the field of Simultaneous Localization and Mapping (SLAM) has undergone a significant evolution, highlighting its critical role in enabling autonomous exploratio...  
  关键词: gaussian splatting, 3d gaussian, nerf  
- **[GaussianHair: Hair Modeling and Rendering with Light-aware Gaussians](https://arxiv.org/abs/2402.10483v1)**  
  作者: Haimin Luo, Min Ouyang, Zijun Zhao, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2402.10483v1.pdf)  
  摘要: Hairstyle reflects culture and ethnicity at first glance. In the digital era, various realistic human hairstyles are also critical to high-fidelity digital human assets for beauty and inclusivity. Yet...  
  关键词: 3d gaussian, real-time rendering  
- **[GaussianObject: High-Quality 3D Object Reconstruction from Four Views with Gaussian Splatting](https://arxiv.org/abs/2402.10259v4)**  
  作者: Chen Yang, Sikuang Li, Jiemin Fang, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2402.10259v4.pdf) | [![Stars](https://img.shields.io/github/stars/GaussianObject/GaussianObject?style=social)](https://github.com/GaussianObject/GaussianObject)  
  摘要: Reconstructing and rendering 3D objects from highly sparse views is of critical importance for promoting applications of 3D vision techniques and improving user experience. However, images from sparse...  
  关键词: gaussian splatting, 3d gaussian, nerf  
- **[GES: Generalized Exponential Splatting for Efficient Radiance Field Rendering](https://arxiv.org/abs/2402.10128v2)**  
  作者: Abdullah Hamdi, Luke Melas-Kyriazi, Jinjie Mai, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2402.10128v2.pdf)  
  摘要: Advancements in 3D Gaussian Splatting have significantly accelerated 3D reconstruction and generation. However, it may require a large number of Gaussians, which creates a substantial memory footprint...  
  关键词: gaussian splatting, 3d gaussian, 3d reconstruction  
- **[Magic-Me: Identity-Specific Video Customized Diffusion](https://arxiv.org/abs/2402.09368v2)**  
  作者: Ze Ma, Daquan Zhou, Chun-Hsiao Yeh, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2402.09368v2.pdf) | [![Stars](https://img.shields.io/github/stars/Zhen-Dong/Magic-Me?style=social)](https://github.com/Zhen-Dong/Magic-Me)  
  摘要: Creating content with specified identities (ID) has attracted significant interest in the field of generative models. In the field of text-to-image generation (T2I), subject-driven creation has achiev...  
  关键词: 3d gaussian  
- **[IM-3D: Iterative Multiview Diffusion and Reconstruction for High-Quality 3D Generation](https://arxiv.org/abs/2402.08682v1)**  
  作者: Luke Melas-Kyriazi, Iro Laina, Christian Rupprecht, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2402.08682v1.pdf)  
  摘要: Most text-to-3D generators build upon off-the-shelf text-to-image models trained on billions of images. They use variants of Score Distillation Sampling (SDS), which is slow, somewhat unstable, and pr...  
  关键词: gaussian splatting, 3d reconstruction  
- **[GALA3D: Towards Text-to-3D Complex Scene Generation via Layout-guided Generative Gaussian Splatting](https://arxiv.org/abs/2402.07207v2)**  
  作者: Xiaoyu Zhou, Xingjian Ran, Yajiao Xiong, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2402.07207v2.pdf)  
  摘要: We present GALA3D, generative 3D GAussians with LAyout-guided control, for effective compositional text-to-3D generation. We first utilize large language models (LLMs) to generate the initial layout a...  
  关键词: 3d gaussian  
- **[3D Gaussian as a New Era: A Survey](https://arxiv.org/abs/2402.07181v2)**  
  作者: Ben Fei, Jingyi Xu, Rui Zhang, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2402.07181v2.pdf)  
  摘要: 3D Gaussian Splatting (3D-GS) has emerged as a significant advancement in the field of Computer Graphics, offering explicit scene representation and novel view synthesis without the reliance on neural...  
  关键词: gaussian splatting, 3d gaussian, nerf  
- **[Deepfake for the Good: Generating Avatars through Face-Swapping with Implicit Deepfake Generation](https://arxiv.org/abs/2402.06390v2)**  
  作者: Georgii Stanishevskii, Jakub Steczkiewicz, Tomasz Szczepanik, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2402.06390v2.pdf)  
  摘要: Numerous emerging deep-learning techniques have had a substantial impact on computer graphics. Among the most promising breakthroughs are the rise of Neural Radiance Fields (NeRFs) and Gaussian Splatt...  
  关键词: gaussian splatting, nerf  
- **[GS-CLIP: Gaussian Splatting for Contrastive Language-Image-3D Pretraining from Real-World Data](https://arxiv.org/abs/2402.06198v2)**  
  作者: Haoyuan Li, Yanpeng Zhou, Yihan Zeng, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2402.06198v2.pdf)  
  摘要: 3D Shape represented as point cloud has achieve advancements in multimodal pre-training to align image and language descriptions, which is curial to object identification, classification, and retrieva...  
  关键词: gaussian splatting, 3d gaussian  
- **[HeadStudio: Text to Animatable Head Avatars with 3D Gaussian Splatting](https://arxiv.org/abs/2402.06149v1)**  
  作者: Zhenglin Zhou, Fan Ma, Hehe Fan, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2402.06149v1.pdf)  
  摘要: Creating digital avatars from textual prompts has long been a desirable yet challenging task. Despite the promising outcomes obtained through 2D diffusion priors in recent works, current methods face ...  
  关键词: gaussian splatting, 3d gaussian  
- **[Mesh-based Gaussian Splatting for Real-time Large-scale Deformation](https://arxiv.org/abs/2402.04796v1)**  
  作者: Lin Gao, Jie Yang, Bo-Tao Zhang, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2402.04796v1.pdf)  
  摘要: Neural implicit representations, including Neural Distance Fields and Neural Radiance Fields, have demonstrated significant capabilities for reconstructing surfaces with complicated geometry and topol...  
  关键词: gaussian splatting, 3d gaussian  
- **[Rig3DGS: Creating Controllable Portraits from Casual Monocular Videos](https://arxiv.org/abs/2402.03723v1)**  
  作者: Alfredo Rivero, ShahRukh Athar, Zhixin Shu, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2402.03723v1.pdf)  
  摘要: Creating controllable 3D human portraits from casual smartphone videos is highly desirable due to their immense value in AR/VR applications. The recent development of 3D Gaussian Splatting (3DGS) has ...  
  关键词: gaussian splatting, 3d gaussian  
- **[4D-Rotor Gaussian Splatting: Towards Efficient Novel View Synthesis for Dynamic Scenes](https://arxiv.org/abs/2402.03307v3)**  
  作者: Yuanxing Duan, Fangyin Wei, Qiyu Dai, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2402.03307v3.pdf)  
  摘要: We consider the problem of novel-view synthesis (NVS) for dynamic scenes. Recent neural approaches have accomplished exceptional NVS results for static 3D scenes, but extensions to 4D time-varying sce...  
  关键词: gaussian splatting, 3d gaussian  
- **[SGS-SLAM: Semantic Gaussian Splatting For Neural Dense SLAM](https://arxiv.org/abs/2402.03246v6)**  
  作者: Mingrui Li, Shuhong Liu, Heng Zhou, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2402.03246v6.pdf)  
  摘要: We present SGS-SLAM, the first semantic visual SLAM system based on Gaussian Splatting. It incorporates appearance, geometry, and semantic features through multi-channel optimization, addressing the o...  
  关键词: gaussian splatting, real-time rendering  
- **[GaMeS: Mesh-Based Adapting and Modification of Gaussian Splatting](https://arxiv.org/abs/2402.01459v4)**  
  作者: Joanna Waczyńska, Piotr Borycki, Sławomir Tadeja, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2402.01459v4.pdf)  
  摘要: Gaussian Splatting (GS) is a novel, state-of-the-art technique for rendering points in a 3D scene by approximating their contribution to image pixels through Gaussian distributions, warranting fast tr...  
  关键词: gaussian splatting, real-time rendering  
- **[GaussianStyle: Gaussian Head Avatar via StyleGAN](https://arxiv.org/abs/2402.00827v3)**  
  作者: Pinxin Liu, Luchuan Song, Daoan Zhang, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2402.00827v3.pdf)  
  摘要: Existing methods like Neural Radiation Fields (NeRF) and 3D Gaussian Splatting (3DGS) have made significant strides in facial attribute control such as facial animation and components editing, yet the...  
  关键词: gaussian splatting, 3d gaussian, nerf  
- **[360-GS: Layout-guided Panoramic Gaussian Splatting For Indoor Roaming](https://arxiv.org/abs/2402.00763v1)**  
  作者: Jiayang Bai, Letian Huang, Jie Guo, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2402.00763v1.pdf)  
  摘要: 3D Gaussian Splatting (3D-GS) has recently attracted great attention with real-time and photo-realistic renderings. This technique typically takes perspective images as input and optimizes a set of 3D...  
  关键词: gaussian splatting, 3d gaussian  
- **[On the Error Analysis of 3D Gaussian Splatting and an Optimal Projection Strategy](https://arxiv.org/abs/2402.00752v4)**  
  作者: Letian Huang, Jiayang Bai, Jie Guo, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2402.00752v4.pdf)  
  摘要: 3D Gaussian Splatting has garnered extensive attention and application in real-time neural rendering. Concurrently, concerns have been raised about the limitations of this technology in aspects such a...  
  关键词: gaussian splatting, 3d gaussian, neural rendering  
- **[StopThePop: Sorted Gaussian Splatting for View-Consistent Real-time Rendering](https://arxiv.org/abs/2402.00525v3)**  
  作者: Lukas Radl, Michael Steiner, Mathias Parger, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2402.00525v3.pdf)  
  摘要: Gaussian Splatting has emerged as a prominent model for constructing 3D representations from images across diverse domains. However, the efficiency of the 3D Gaussian Splatting rendering pipeline reli...  
  关键词: gaussian splatting, 3d gaussian  

### 2024年01月
- **[SAGD: Boundary-Enhanced Segment Anything in 3D Gaussian via Gaussian Decomposition](https://arxiv.org/abs/2401.17857v3)**  
  作者: Xu Hu, Yuxi Wang, Lue Fan, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2401.17857v3.pdf)  
  摘要: 3D Gaussian Splatting has emerged as an alternative 3D representation for novel view synthesis, benefiting from its high-quality rendering results and real-time rendering speed. However, the 3D Gaussi...  
  关键词: gaussian splatting, 3d gaussian, real-time rendering  
- **[VR-GS: A Physical Dynamics-Aware Interactive Gaussian Splatting System in Virtual Reality](https://arxiv.org/abs/2401.16663v2)**  
  作者: Ying Jiang, Chang Yu, Tianyi Xie, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2401.16663v2.pdf)  
  摘要: As consumer Virtual Reality (VR) and Mixed Reality (MR) technologies gain momentum, there's a growing focus on the development of engagements with 3D virtual content. Unfortunately, traditional techni...  
  关键词: gaussian splatting  
- **[3DG: A Framework for Using Generative AI for Handling Sparse Learner Performance Data From Intelligent Tutoring Systems](https://arxiv.org/abs/2402.01746v1)**  
  作者: Liang Zhang, Jionghao Lin, Conrad Borchers, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2402.01746v1.pdf)  
  摘要: Learning performance data (e.g., quiz scores and attempts) is significant for understanding learner engagement and knowledge mastery level. However, the learning performance data collected from Intell...  
- **[Endo-4DGS: Endoscopic Monocular Scene Reconstruction with 4D Gaussian Splatting](https://arxiv.org/abs/2401.16416v4)**  
  作者: Yiming Huang, Beilei Cui, Long Bai, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2401.16416v4.pdf)  
  摘要: In the realm of robot-assisted minimally invasive surgery, dynamic scene reconstruction can significantly enhance downstream tasks and improve surgical outcomes. Neural Radiance Fields (NeRF)-based me...  
  关键词: gaussian splatting, 3d gaussian, nerf  
- **[Gaussian Splashing: Unified Particles for Versatile Motion Synthesis and Rendering](https://arxiv.org/abs/2401.15318v2)**  
  作者: Yutao Feng, Xiang Feng, Yintong Shang, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2401.15318v2.pdf)  
  摘要: We demonstrate the feasibility of integrating physics-based animations of solids and fluids with 3D Gaussian Splatting (3DGS) to create novel effects in virtual scenes reconstructed using 3DGS. Levera...  
  关键词: gaussian splatting, 3d gaussian  
- **[TIP-Editor: An Accurate 3D Editor Following Both Text-Prompts And Image-Prompts](https://arxiv.org/abs/2401.14828v3)**  
  作者: Jingyu Zhuang, Di Kang, Yan-Pei Cao, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2401.14828v3.pdf)  
  摘要: Text-driven 3D scene editing has gained significant attention owing to its convenience and user-friendliness. However, existing methods still lack accurate control of the specified appearance and loca...  
  关键词: gaussian splatting, 3d gaussian  
- **[GauU-Scene: A Scene Reconstruction Benchmark on Large Scale 3D Reconstruction Dataset Using Gaussian Splatting](https://arxiv.org/abs/2401.14032v1)**  
  作者: Butian Xiong, Zhuo Li, Zhen Li  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2401.14032v1.pdf)  
  摘要: We introduce a novel large-scale scene reconstruction benchmark using the newly developed 3D representation approach, Gaussian Splatting, on our expansive U-Scene dataset. U-Scene encompasses over one...  
  关键词: gaussian splatting  
- **[EndoGaussians: Single View Dynamic Gaussian Splatting for Deformable Endoscopic Tissues Reconstruction](https://arxiv.org/abs/2401.13352v1)**  
  作者: Yangsen Chen, Hao Wang  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2401.13352v1.pdf)  
  摘要: The accurate 3D reconstruction of deformable soft body tissues from endoscopic videos is a pivotal challenge in medical applications such as VR surgery and medical image analysis. Existing methods oft...  
  关键词: gaussian splatting, 3d reconstruction, nerf  
- **[PSAvatar: A Point-based Shape Model for Real-Time Head Avatar Animation with 3D Gaussian Splatting](https://arxiv.org/abs/2401.12900v5)**  
  作者: Zhongyuan Zhao, Zhenyu Bao, Qing Li, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2401.12900v5.pdf)  
  摘要: Despite much progress, achieving real-time high-fidelity head avatar animation is still difficult and existing methods have to trade-off between speed and quality. 3DMM based methods often fail to mod...  
  关键词: 3d gaussian  
- **[EndoGaussian: Real-time Gaussian Splatting for Dynamic Endoscopic Scene Reconstruction](https://arxiv.org/abs/2401.12561v2)**  
  作者: Yifan Liu, Chenxin Li, Chen Yang, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2401.12561v2.pdf)  
  摘要: Reconstructing deformable tissues from endoscopic videos is essential in many downstream surgical applications. However, existing methods suffer from slow rendering speed, greatly limiting their pract...  
  关键词: gaussian splatting, 3d gaussian  
- **[EndoGS: Deformable Endoscopic Tissues Reconstruction with Gaussian Splatting](https://arxiv.org/abs/2401.11535v3)**  
  作者: Lingting Zhu, Zhao Wang, Jiahao Cui, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2401.11535v3.pdf) | [![Stars](https://img.shields.io/github/stars/HKU-MedAI/EndoGS?style=social)](https://github.com/HKU-MedAI/EndoGS)  
  摘要: Surgical 3D reconstruction is a critical area of research in robotic surgery, with recent works adopting variants of dynamic radiance fields to achieve success in 3D reconstruction of deformable tissu...  
  关键词: gaussian splatting, 3d gaussian, 3d reconstruction  
- **[GaussianBody: Clothed Human Reconstruction via 3d Gaussian Splatting](https://arxiv.org/abs/2401.09720v2)**  
  作者: Mengtian Li, Shengxiang Yao, Zhifeng Xie, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2401.09720v2.pdf)  
  摘要: In this work, we propose a novel clothed human reconstruction method called GaussianBody, based on 3D Gaussian Splatting. Compared with the costly neural radiance based models, 3D Gaussian Splatting h...  
  关键词: gaussian splatting, 3d gaussian  
- **[Efficient4D: Fast Dynamic 3D Object Generation from a Single-view Video](https://arxiv.org/abs/2401.08742v3)**  
  作者: Zijie Pan, Zeyu Yang, Xiatian Zhu, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2401.08742v3.pdf)  
  摘要: Generating dynamic 3D object from a single-view video is challenging due to the lack of 4D labeled data. An intuitive approach is to extend previous image-to-3D pipelines by transferring off-the-shelf...  
  关键词: gaussian splatting, real-time rendering  
- **[Forging Vision Foundation Models for Autonomous Driving: Challenges, Methodologies, and Opportunities](https://arxiv.org/abs/2401.08045v1)**  
  作者: Xu Yan, Haiming Zhang, Yingjie Cai, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2401.08045v1.pdf) | [![Stars](https://img.shields.io/github/stars/zhanghm1995/Forge_VFM4AD?style=social)](https://github.com/zhanghm1995/Forge_VFM4AD)  
  摘要: The rise of large foundation models, trained on extensive datasets, is revolutionizing the field of AI. Models such as SAM, DALL-E2, and GPT-4 showcase their adaptability by extracting intricate patte...  
  关键词: gaussian splatting, 3d gaussian, nerf  
- **[Gaussian Shadow Casting for Neural Characters](https://arxiv.org/abs/2401.06116v1)**  
  作者: Luis Bolanos, Shih-Yang Su, Helge Rhodin  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2401.06116v1.pdf)  
  摘要: Neural character models can now reconstruct detailed geometry and texture from video, but they lack explicit shadows and shading, leading to artifacts when generating novel views and poses or during r...  
  关键词: gaussian splatting, neural rendering  
- **[TRIPS: Trilinear Point Splatting for Real-Time Radiance Field Rendering](https://arxiv.org/abs/2401.06003v2)**  
  作者: Linus Franke, Darius Rückert, Laura Fink, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2401.06003v2.pdf)  
  摘要: Point-based radiance field rendering has demonstrated impressive results for novel view synthesis, offering a compelling blend of rendering quality and computational efficiency. However, also latest a...  
  关键词: gaussian splatting, 3d gaussian  
- **[Learning Segmented 3D Gaussians via Efficient Feature Unprojection for Zero-shot Neural Scene Segmentation](https://arxiv.org/abs/2401.05925v4)**  
  作者: Bin Dou, Tianyu Zhang, Zhaohui Wang, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2401.05925v4.pdf)  
  摘要: Zero-shot neural scene segmentation, which reconstructs 3D neural segmentation field without manual annotations, serves as an effective way for scene understanding. However, existing models, especiall...  
  关键词: 3d gaussian  
- **[AGG: Amortized Generative 3D Gaussians for Single Image to 3D](https://arxiv.org/abs/2401.04099v1)**  
  作者: Dejia Xu, Ye Yuan, Morteza Mardani, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2401.04099v1.pdf)  
  摘要: Given the growing need for automatic 3D content creation pipelines, various 3D representations have been studied to generate 3D objects from a single image. Due to its superior rendering efficiency, 3...  
  关键词: gaussian splatting, 3d gaussian, 3d reconstruction  
- **[A Survey on 3D Gaussian Splatting](https://arxiv.org/abs/2401.03890v4)**  
  作者: Guikun Chen, Wenguan Wang  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2401.03890v4.pdf)  
  摘要: 3D Gaussian splatting (GS) has recently emerged as a transformative technique in the realm of explicit radiance field and computer graphics. This innovative approach, characterized by the utilization ...  
  关键词: gaussian splatting, 3d gaussian, real-time rendering, 3d reconstruction  
- **[Progress and Prospects in 3D Generative AI: A Technical Overview including 3D human](https://arxiv.org/abs/2401.02620v1)**  
  作者: Song Bai, Jie Li  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2401.02620v1.pdf)  
  摘要: While AI-generated text and 2D images continue to expand its territory, 3D generation has gradually emerged as a trend that cannot be ignored. Since the year 2023 an abundant amount of research papers...  
  关键词: gaussian splatting, 3d gaussian, nerf  
- **[Characterizing Satellite Geometry via Accelerated 3D Gaussian Splatting](https://arxiv.org/abs/2401.02588v1)**  
  作者: Van Minh Nguyen, Emma Sandidge, Trupti Mahendrakar, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2401.02588v1.pdf)  
  摘要: The accelerating deployment of spacecraft in orbit have generated interest in on-orbit servicing (OOS), inspection of spacecraft, and active debris removal (ADR). Such missions require precise rendezv...  
  关键词: gaussian splatting, 3d gaussian, nerf  
- **[PEGASUS: Physically Enhanced Gaussian Splatting Simulation System for 6DoF Object Pose Dataset Generation](https://arxiv.org/abs/2401.02281v2)**  
  作者: Lukas Meyer, Floris Erich, Yusuke Yoshiyasu, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2401.02281v2.pdf)  
  摘要: We introduce Physically Enhanced Gaussian Splatting Simulation System (PEGASUS) for 6DOF object pose dataset generation, a versatile dataset generator based on 3D Gaussian Splatting.   Environment and...  
  关键词: gaussian splatting, 3d gaussian  
- **[FMGS: Foundation Model Embedded 3D Gaussian Splatting for Holistic 3D Scene Understanding](https://arxiv.org/abs/2401.01970v2)**  
  作者: Xingxing Zuo, Pouya Samangouei, Yunwen Zhou, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2401.01970v2.pdf)  
  摘要: Precisely perceiving the geometric and semantic properties of real-world 3D objects is crucial for the continued evolution of augmented reality and robotic applications. To this end, we present Founda...  
  关键词: gaussian splatting, 3d gaussian  
- **[Street Gaussians: Modeling Dynamic Urban Scenes with Gaussian Splatting](https://arxiv.org/abs/2401.01339v3)**  
  作者: Yunzhi Yan, Haotong Lin, Chenxu Zhou, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2401.01339v3.pdf)  
  摘要: This paper aims to tackle the problem of modeling dynamic urban streets for autonomous driving scenes. Recent methods extend NeRF by incorporating tracked vehicle poses to animate vehicles, enabling p...  
  关键词: 3d gaussian, nerf  
- **[Deblurring 3D Gaussian Splatting](https://arxiv.org/abs/2401.00834v3)**  
  作者: Byeonghyeon Lee, Howoong Lee, Xiangyu Sun, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2401.00834v3.pdf)  
  摘要: Recent studies in Radiance Fields have paved the robust way for novel view synthesis with their photorealistic rendering quality. Nevertheless, they usually employ neural networks and volumetric rende...  
  关键词: gaussian splatting, 3d gaussian, real-time rendering  

### 2023年12月
- **[4DGen: Grounded 4D Content Generation with Spatial-temporal Consistency](https://arxiv.org/abs/2312.17225v2)**  
  作者: Yuyang Yin, Dejia Xu, Zhangyang Wang, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2312.17225v2.pdf)  
  摘要: Aided by text-to-image and text-to-video diffusion models, existing 4D content creation pipelines utilize score distillation sampling to optimize the entire dynamic 3D scene. However, as these pipelin...  
  关键词: 3d gaussian  
- **[DreamGaussian4D: Generative 4D Gaussian Splatting](https://arxiv.org/abs/2312.17142v3)**  
  作者: Jiawei Ren, Liang Pan, Jiaxiang Tang, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2312.17142v3.pdf)  
  摘要: 4D content generation has achieved remarkable progress recently. However, existing methods suffer from long optimization times, a lack of motion controllability, and a low quality of details. In this ...  
  关键词: gaussian splatting  
- **[Spacetime Gaussian Feature Splatting for Real-Time Dynamic View Synthesis](https://arxiv.org/abs/2312.16812v2)**  
  作者: Zhan Li, Zhang Chen, Zhong Li, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2312.16812v2.pdf) | [![Stars](https://img.shields.io/github/stars/oppo-us-research/SpacetimeGaussians?style=social)](https://github.com/oppo-us-research/SpacetimeGaussians)  
  摘要: Novel view synthesis of dynamic scenes has been an intriguing yet challenging problem. Despite recent advancements, simultaneously achieving high-resolution photorealistic results, real-time rendering...  
  关键词: 3d gaussian, real-time rendering  
- **[LangSplat: 3D Language Gaussian Splatting](https://arxiv.org/abs/2312.16084v2)**  
  作者: Minghan Qin, Wanhua Li, Jiawei Zhou, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2312.16084v2.pdf)  
  摘要: Humans live in a 3D world and commonly use natural language to interact with a 3D scene. Modeling a 3D language field to support open-ended language queries in 3D has gained increasing attention recen...  
  关键词: 3d gaussian, nerf  
- **[2D-Guided 3D Gaussian Segmentation](https://arxiv.org/abs/2312.16047v1)**  
  作者: Kun Lan, Haoran Li, Haolin Shi, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2312.16047v1.pdf)  
  摘要: Recently, 3D Gaussian, as an explicit 3D representation method, has demonstrated strong competitiveness over NeRF (Neural Radiance Fields) in terms of expressing complex scenes and training duration. ...  
  关键词: 3d gaussian, nerf  
- **[Sparse-view CT Reconstruction with 3D Gaussian Volumetric Representation](https://arxiv.org/abs/2312.15676v1)**  
  作者: Yingtai Li, Xueming Fu, Shang Zhao, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2312.15676v1.pdf)  
  摘要: Sparse-view CT is a promising strategy for reducing the radiation dose of traditional CT scans, but reconstructing high-quality images from incomplete and noisy data is challenging. Recently, 3D Gauss...  
  关键词: 3d gaussian  
- **[Human101: Training 100+FPS Human Gaussians in 100s from 1 View](https://arxiv.org/abs/2312.15258v1)**  
  作者: Mingwei Li, Jiachen Tao, Zongxin Yang, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2312.15258v1.pdf) | [![Stars](https://img.shields.io/github/stars/longxiang-ai/Human101?style=social)](https://github.com/longxiang-ai/Human101)  
  摘要: Reconstructing the human body from single-view videos plays a pivotal role in the virtual reality domain. One prevalent application scenario necessitates the rapid reconstruction of high-fidelity 3D d...  
  关键词: gaussian splatting, 3d gaussian, real-time rendering, nerf  
- **[Deformable 3D Gaussian Splatting for Animatable Human Avatars](https://arxiv.org/abs/2312.15059v1)**  
  作者: HyunJun Jung, Nikolas Brasch, Jifei Song, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2312.15059v1.pdf)  
  摘要: Recent advances in neural radiance fields enable novel view synthesis of photo-realistic images in dynamic settings, which can be applied to scenarios with human animation. Commonly used implicit back...  
  关键词: gaussian splatting, 3d gaussian  
- **[Align Your Gaussians: Text-to-4D with Dynamic 3D Gaussians and Composed Diffusion Models](https://arxiv.org/abs/2312.13763v2)**  
  作者: Huan Ling, Seung Wook Kim, Antonio Torralba, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2312.13763v2.pdf)  
  摘要: Text-guided diffusion models have revolutionized image and video generation and have also been successfully used for optimization-based 3D object synthesis. Here, we instead focus on the underexplored...  
  关键词: gaussian splatting, 3d gaussian  
- **[Gaussian Splatting with NeRF-based Color and Opacity](https://arxiv.org/abs/2312.13729v5)**  
  作者: Dawid Malarz, Weronika Smolak, Jacek Tabor, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2312.13729v5.pdf)  
  摘要: Neural Radiance Fields (NeRFs) have demonstrated the remarkable potential of neural networks to capture the intricacies of 3D objects. By encoding the shape and color information within neural network...  
  关键词: gaussian splatting, nerf  
- **[Splatter Image: Ultra-Fast Single-View 3D Reconstruction](https://arxiv.org/abs/2312.13150v2)**  
  作者: Stanislaw Szymanowicz, Christian Rupprecht, Andrea Vedaldi  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2312.13150v2.pdf)  
  摘要: We introduce the \method, an ultra-efficient approach for monocular 3D object reconstruction. Splatter Image is based on Gaussian Splatting, which allows fast and high-quality reconstruction of 3D sce...  
  关键词: gaussian splatting, 3d gaussian  
- **[SWinGS: Sliding Windows for Dynamic 3D Gaussian Splatting](https://arxiv.org/abs/2312.13308v2)**  
  作者: Richard Shaw, Michal Nazarczuk, Jifei Song, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2312.13308v2.pdf)  
  摘要: Novel view synthesis has shown rapid progress recently, with methods capable of producing increasingly photorealistic results. 3D Gaussian Splatting has emerged as a promising method, producing high-q...  
  关键词: gaussian splatting, 3d gaussian  
- **[Compact 3D Scene Representation via Self-Organizing Gaussian Grids](https://arxiv.org/abs/2312.13299v2)**  
  作者: Wieland Morgenstern, Florian Barthel, Anna Hilsmann, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2312.13299v2.pdf)  
  摘要: 3D Gaussian Splatting has recently emerged as a highly promising technique for modeling of static 3D scenes. In contrast to Neural Radiance Fields, it utilizes efficient rasterization allowing for ver...  
  关键词: gaussian splatting, 3d gaussian  
- **[pixelSplat: 3D Gaussian Splats from Image Pairs for Scalable Generalizable 3D Reconstruction](https://arxiv.org/abs/2312.12337v4)**  
  作者: David Charatan, Sizhe Li, Andrea Tagliasacchi, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2312.12337v4.pdf)  
  摘要: We introduce pixelSplat, a feed-forward model that learns to reconstruct 3D radiance fields parameterized by 3D Gaussian primitives from pairs of images. Our model features real-time and memory-effici...  
  关键词: gaussian splatting, 3d gaussian, 3d reconstruction  
- **[GAvatar: Animatable 3D Gaussian Avatars with Implicit Mesh Learning](https://arxiv.org/abs/2312.11461v2)**  
  作者: Ye Yuan, Xueting Li, Yangyi Huang, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2312.11461v2.pdf)  
  摘要: Gaussian splatting has emerged as a powerful 3D representation that harnesses the advantages of both explicit (mesh) and implicit (NeRF) 3D representations. In this paper, we seek to leverage Gaussian...  
  关键词: gaussian splatting, 3d gaussian, nerf  
- **[GauFRe: Gaussian Deformation Fields for Real-time Dynamic Novel View Synthesis](https://arxiv.org/abs/2312.11458v1)**  
  作者: Yiqing Liang, Numair Khan, Zhengqin Li, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2312.11458v1.pdf)  
  摘要: We propose a method for dynamic scene reconstruction using deformable 3D Gaussians that is tailored for monocular video. Building upon the efficiency of Gaussian splatting, our approach extends the re...  
  关键词: gaussian splatting, 3d gaussian, real-time rendering  
- **[Exploring the Feasibility of Generating Realistic 3D Models of Endangered Species Using DreamGaussian: An Analysis of Elevation Angle's Impact on Model Generation](https://arxiv.org/abs/2312.09682v1)**  
  作者: Selcuk Anil Karatopak, Deniz Sen  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2312.09682v1.pdf)  
  摘要: Many species face the threat of extinction. It's important to study these species and gather information about them as much as possible to preserve biodiversity. Due to the rarity of endangered specie...  
  关键词: gaussian splatting  
- **[Text2Immersion: Generative Immersive Scene with 3D Gaussians](https://arxiv.org/abs/2312.09242v1)**  
  作者: Hao Ouyang, Kathryn Heal, Stephen Lombardi, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2312.09242v1.pdf)  
  摘要: We introduce Text2Immersion, an elegant method for producing high-quality 3D immersive scenes from text prompts. Our proposed pipeline initiates by progressively generating a Gaussian cloud using pre-...  
- **[3DGS-Avatar: Animatable Avatars via Deformable 3D Gaussian Splatting](https://arxiv.org/abs/2312.09228v3)**  
  作者: Zhiyin Qian, Shaofei Wang, Marko Mihajlovic, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2312.09228v3.pdf)  
  摘要: We introduce an approach that creates animatable human avatars from monocular videos using 3D Gaussian Splatting (3DGS). Existing methods based on neural radiance fields (NeRFs) achieve high-quality n...  
  关键词: gaussian splatting, 3d gaussian, nerf  
- **[Triplane Meets Gaussian Splatting: Fast and Generalizable Single-View 3D Reconstruction with Transformers](https://arxiv.org/abs/2312.09147v2)**  
  作者: Zi-Xin Zou, Zhipeng Yu, Yuan-Chen Guo, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2312.09147v2.pdf)  
  摘要: Recent advancements in 3D reconstruction from single images have been driven by the evolution of generative models. Prominent among these are methods based on Score Distillation Sampling (SDS) and the...  
  关键词: 3d gaussian, 3d reconstruction  
- **[iComMa: Inverting 3D Gaussian Splatting for Camera Pose Estimation via Comparing and Matching](https://arxiv.org/abs/2312.09031v2)**  
  作者: Yuan Sun, Xuan Wang, Yunfan Zhang, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2312.09031v2.pdf)  
  摘要: We present a method named iComMa to address the 6D camera pose estimation problem in computer vision. Conventional pose estimation methods typically rely on the target's CAD model or necessitate speci...  
  关键词: gaussian splatting, 3d gaussian, nerf  
- **[DrivingGaussian: Composite Gaussian Splatting for Surrounding Dynamic Autonomous Driving Scenes](https://arxiv.org/abs/2312.07920v3)**  
  作者: Xiaoyu Zhou, Zhiwei Lin, Xiaojun Shan, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2312.07920v3.pdf) | [![Stars](https://img.shields.io/github/stars/VDIGPKU/DrivingGaussian?style=social)](https://github.com/VDIGPKU/DrivingGaussian)  
  摘要: We present DrivingGaussian, an efficient and effective framework for surrounding dynamic autonomous driving scenes. For complex scenes with moving objects, we first sequentially and progressively mode...  
  关键词: gaussian splatting, 3d gaussian  
- **[COLMAP-Free 3D Gaussian Splatting](https://arxiv.org/abs/2312.07504v2)**  
  作者: Yang Fu, Sifei Liu, Amey Kulkarni, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2312.07504v2.pdf)  
  摘要: While neural rendering has led to impressive advances in scene reconstruction and novel view synthesis, it relies heavily on accurately pre-computed camera poses. To relax this constraint, multiple ef...  
  关键词: gaussian splatting, 3d gaussian, neural rendering, nerf  
- **[Gaussian Splatting SLAM](https://arxiv.org/abs/2312.06741v2)**  
  作者: Hidenobu Matsuki, Riku Murai, Paul H. J. Kelly, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2312.06741v2.pdf)  
  摘要: We present the first application of 3D Gaussian Splatting in monocular SLAM, the most fundamental but the hardest setup for Visual SLAM. Our method, which runs live at 3fps, utilises Gaussians as the ...  
  关键词: gaussian splatting, 3d gaussian  
- **[ASH: Animatable Gaussian Splats for Efficient and Photoreal Human Rendering](https://arxiv.org/abs/2312.05941v2)**  
  作者: Haokai Pang, Heming Zhu, Adam Kortylewski, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2312.05941v2.pdf)  
  摘要: Real-time rendering of photorealistic and controllable human avatars stands as a cornerstone in Computer Vision and Graphics. While recent advances in neural implicit rendering have unlocked unprecede...  
  关键词: gaussian splatting, 3d gaussian, real-time rendering  
- **[CoGS: Controllable Gaussian Splatting](https://arxiv.org/abs/2312.05664v2)**  
  作者: Heng Yu, Joel Julin, Zoltán Á. Milacski, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2312.05664v2.pdf)  
  摘要: Capturing and re-animating the 3D structure of articulated objects present significant barriers. On one hand, methods requiring extensively calibrated multi-view setups are prohibitively complex and r...  
  关键词: gaussian splatting, 3d gaussian, nerf  
- **[GIR: 3D Gaussian Inverse Rendering for Relightable Scene Factorization](https://arxiv.org/abs/2312.05133v2)**  
  作者: Yahao Shi, Yanmin Wu, Chenming Wu, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2312.05133v2.pdf) | [![Stars](https://img.shields.io/github/stars/guduxiaolang/GIR?style=social)](https://github.com/guduxiaolang/GIR)  
  摘要: This paper presents a 3D Gaussian Inverse Rendering (GIR) method, employing 3D Gaussian representations to effectively factorize the scene into material properties, light, and geometry. The key contri...  
  关键词: 3d gaussian, real-time rendering  
- **[Learn to Optimize Denoising Scores for 3D Generation: A Unified and Improved Diffusion Prior on NeRF and 3D Gaussian Splatting](https://arxiv.org/abs/2312.04820v1)**  
  作者: Xiaofeng Yang, Yiwen Chen, Cheng Chen, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2312.04820v1.pdf)  
  摘要: We propose a unified framework aimed at enhancing the diffusion priors for 3D generation tasks. Despite the critical importance of these tasks, existing methodologies often struggle to generate high-c...  
  关键词: gaussian splatting, 3d gaussian, nerf  
- **[EAGLES: Efficient Accelerated 3D Gaussians with Lightweight EncodingS](https://arxiv.org/abs/2312.04564v3)**  
  作者: Sharath Girish, Kamal Gupta, Abhinav Shrivastava  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2312.04564v3.pdf)  
  摘要: Recently, 3D Gaussian splatting (3D-GS) has gained popularity in novel-view scene synthesis. It addresses the challenges of lengthy training times and slow rendering speeds associated with Neural Radi...  
  关键词: gaussian splatting, 3d gaussian, real-time rendering, nerf  
- **[MonoGaussianAvatar: Monocular Gaussian Point-based Head Avatar](https://arxiv.org/abs/2312.04558v1)**  
  作者: Yufan Chen, Lizhen Wang, Qijing Li, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2312.04558v1.pdf)  
  摘要: The ability to animate photo-realistic head avatars reconstructed from monocular portrait video sequences represents a crucial step in bridging the gap between the virtual and real worlds. Recent adva...  
  关键词: gaussian splatting, 3d gaussian  
- **[Relightable Gaussian Codec Avatars](https://arxiv.org/abs/2312.03704v2)**  
  作者: Shunsuke Saito, Gabriel Schwartz, Tomas Simon, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2312.03704v2.pdf)  
  摘要: The fidelity of relighting is bounded by both geometry and appearance representations. For geometry, both mesh and volumetric approaches have difficulty modeling intricate structures like 3D hair geom...  
  关键词: 3d gaussian  
- **[HiFi4G: High-Fidelity Human Performance Rendering via Compact Gaussian Splatting](https://arxiv.org/abs/2312.03461v2)**  
  作者: Yuheng Jiang, Zhehao Shen, Penghao Wang, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2312.03461v2.pdf)  
  摘要: We have recently seen tremendous progress in photo-real human modeling and rendering. Yet, efficiently rendering realistic human performance and integrating it into the rasterization pipeline remains ...  
  关键词: 3d gaussian  
- **[Gaussian-Flow: 4D Reconstruction with Dynamic 3D Gaussian Particle](https://arxiv.org/abs/2312.03431v1)**  
  作者: Youtian Lin, Zuozhuo Dai, Siyu Zhu, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2312.03431v1.pdf)  
  摘要: We introduce Gaussian-Flow, a novel point-based approach for fast dynamic scene reconstruction and real-time rendering from both multi-view and monocular videos. In contrast to the prevalent NeRF-base...  
  关键词: gaussian splatting, 3d gaussian, real-time rendering, 3d reconstruction, nerf  
- **[Gaussian-SLAM: Photo-realistic Dense SLAM with Gaussian Splatting](https://arxiv.org/abs/2312.10070v2)**  
  作者: Vladimir Yugay, Yue Li, Theo Gevers, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2312.10070v2.pdf)  
  摘要: We present a dense simultaneous localization and mapping (SLAM) method that uses 3D Gaussians as a scene representation. Our approach enables interactive-time reconstruction and photo-realistic render...  
  关键词: 3d gaussian, real-time rendering  
- **[Feature 3DGS: Supercharging 3D Gaussian Splatting to Enable Distilled Feature Fields](https://arxiv.org/abs/2312.03203v3)**  
  作者: Shijie Zhou, Haoran Chang, Sicheng Jiang, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2312.03203v3.pdf)  
  摘要: 3D scene representations have gained immense popularity in recent years. Methods that use Neural Radiance fields are versatile for traditional tasks such as novel view synthesis. In recent times, some...  
  关键词: gaussian splatting, 3d gaussian, nerf  
- **[Gaussian3Diff: 3D Gaussian Diffusion for 3D Full Head Synthesis and Editing](https://arxiv.org/abs/2312.03763v3)**  
  作者: Yushi Lan, Feitong Tan, Di Qiu, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2312.03763v3.pdf)  
  摘要: We present a novel framework for generating photorealistic 3D human head and subsequently manipulating and reposing them with remarkable flexibility. The proposed approach leverages an implicit functi...  
  关键词: 3d gaussian  
- **[GauHuman: Articulated Gaussian Splatting from Monocular Human Videos](https://arxiv.org/abs/2312.02973v1)**  
  作者: Shoukang Hu, Ziwei Liu  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2312.02973v1.pdf)  
  摘要: We present, GauHuman, a 3D human model with Gaussian Splatting for both fast training (1 ~ 2 minutes) and real-time rendering (up to 189 FPS), compared with existing NeRF-based implicit representation...  
  关键词: gaussian splatting, 3d gaussian, real-time rendering, nerf  
- **[HeadGaS: Real-Time Animatable Head Avatars via 3D Gaussian Splatting](https://arxiv.org/abs/2312.02902v2)**  
  作者: Helisa Dhamo, Yinyu Nie, Arthur Moreau, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2312.02902v2.pdf)  
  摘要: 3D head animation has seen major quality and runtime improvements over the last few years, particularly empowered by the advances in differentiable rendering and neural radiance fields. Real-time rend...  
  关键词: 3d gaussian, real-time rendering  
- **[HHAvatar: Gaussian Head Avatar with Dynamic Hairs](https://arxiv.org/abs/2312.03029v3)**  
  作者: Zhanfeng Liao, Yuelang Xu, Zhe Li, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2312.03029v3.pdf)  
  摘要: Creating high-fidelity 3D head avatars has always been a research hotspot, but it remains a great challenge under lightweight sparse view setups. In this paper, we propose HHAvatar represented by cont...  
  关键词: 3d gaussian  
- **[GPS-Gaussian: Generalizable Pixel-wise 3D Gaussian Splatting for Real-time Human Novel View Synthesis](https://arxiv.org/abs/2312.02155v3)**  
  作者: Shunyuan Zheng, Boyao Zhou, Ruizhi Shao, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2312.02155v3.pdf)  
  摘要: We present a new approach, termed GPS-Gaussian, for synthesizing novel views of a character in a real-time manner. The proposed method enables 2K-resolution rendering under a sparse-view camera settin...  
  关键词: gaussian splatting  
- **[MANUS: Markerless Grasp Capture using Articulated 3D Gaussians](https://arxiv.org/abs/2312.02137v2)**  
  作者: Chandradeep Pokhariya, Ishaan N Shah, Angela Xing, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2312.02137v2.pdf)  
  摘要: Understanding how we grasp objects with our hands has important applications in areas like robotics and mixed reality. However, this challenging problem requires accurate modeling of the contact betwe...  
  关键词: gaussian splatting, 3d gaussian  
- **[Re-Nerfing: Improving Novel View Synthesis through Novel View Synthesis](https://arxiv.org/abs/2312.02255v3)**  
  作者: Felix Tristram, Stefano Gasperini, Nassir Navab, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2312.02255v3.pdf)  
  摘要: Recent neural rendering and reconstruction techniques, such as NeRFs or Gaussian Splatting, have shown remarkable novel view synthesis capabilities but require hundreds of images of the scene from div...  
  关键词: gaussian splatting, neural rendering, nerf  
- **[GaussianAvatar: Towards Realistic Human Avatar Modeling from a Single Video via Animatable 3D Gaussians](https://arxiv.org/abs/2312.02134v3)**  
  作者: Liangxiao Hu, Hongwen Zhang, Yuxiang Zhang, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2312.02134v3.pdf)  
  摘要: We present GaussianAvatar, an efficient approach to creating realistic human avatars with dynamic 3D appearances from a single video. We start by introducing animatable 3D Gaussians to explicitly repr...  
  关键词: 3d gaussian  
- **[SplaTAM: Splat, Track & Map 3D Gaussians for Dense RGB-D SLAM](https://arxiv.org/abs/2312.02126v3)**  
  作者: Nikhil Keetha, Jay Karhade, Krishna Murthy Jatavallabhula, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2312.02126v3.pdf)  
  摘要: Dense simultaneous localization and mapping (SLAM) is crucial for robotics and augmented reality applications. However, current methods are often hampered by the non-volumetric or implicit way they re...  
  关键词: 3d gaussian  
- **[Mathematical Supplement for the $\texttt{gsplat}$ Library](https://arxiv.org/abs/2312.02121v1)**  
  作者: Vickie Ye, Angjoo Kanazawa  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2312.02121v1.pdf) | [![Stars](https://img.shields.io/github/stars/nerfstudio-project/gsplat?style=social)](https://github.com/nerfstudio-project/gsplat)  
  摘要: This report provides the mathematical details of the gsplat library, a modular toolbox for efficient differentiable Gaussian splatting, as proposed by Kerbl et al. It provides a self-contained referen...  
  关键词: gaussian splatting, nerf  
- **[GaussianAvatars: Photorealistic Head Avatars with Rigged 3D Gaussians](https://arxiv.org/abs/2312.02069v2)**  
  作者: Shenhan Qian, Tobias Kirschstein, Liam Schoneveld, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2312.02069v2.pdf)  
  摘要: We introduce GaussianAvatars, a new method to create photorealistic head avatars that are fully controllable in terms of expression, pose, and viewpoint. The core idea is a dynamic 3D representation b...  
  关键词: 3d gaussian  
- **[SC-GS: Sparse-Controlled Gaussian Splatting for Editable Dynamic Scenes](https://arxiv.org/abs/2312.14937v3)**  
  作者: Yi-Hua Huang, Yang-Tian Sun, Ziyi Yang, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2312.14937v3.pdf)  
  摘要: Novel view synthesis for dynamic scenes is still a challenging problem in computer vision and graphics. Recently, Gaussian splatting has emerged as a robust technique to represent static scenes and en...  
  关键词: gaussian splatting, 3d gaussian  
- **[GaussianHead: High-fidelity Head Avatars with Learnable Gaussian Derivation](https://arxiv.org/abs/2312.01632v4)**  
  作者: Jie Wang, Jiu-Cheng Xie, Xianyan Li, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2312.01632v4.pdf) | [![Stars](https://img.shields.io/github/stars/chiehwangs/gaussian-head?style=social)](https://github.com/chiehwangs/gaussian-head)  
  摘要: Constructing vivid 3D head avatars for given subjects and realizing a series of animations on them is valuable yet challenging. This paper presents GaussianHead, which models the actional human head w...  
  关键词: 3d gaussian  
- **[FlashAvatar: High-fidelity Head Avatar with Efficient Gaussian Embedding](https://arxiv.org/abs/2312.02214v2)**  
  作者: Jun Xiang, Xuan Gao, Yudong Guo, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2312.02214v2.pdf)  
  摘要: We propose FlashAvatar, a novel and lightweight 3D animatable avatar representation that could reconstruct a digital avatar from a short monocular video sequence in minutes and render high-fidelity ph...  
  关键词: 3d gaussian  
- **[Neural Parametric Gaussians for Monocular Non-Rigid Object Reconstruction](https://arxiv.org/abs/2312.01196v2)**  
  作者: Devikalyan Das, Christopher Wewer, Raza Yunus, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2312.01196v2.pdf)  
  摘要: Reconstructing dynamic objects from monocular videos is a severely underconstrained and challenging problem, and recent work has approached it in various directions. However, owing to the ill-posed na...  
  关键词: 3d gaussian  
- **[StableDreamer: Taming Noisy Score Distillation Sampling for Text-to-3D](https://arxiv.org/abs/2312.02189v1)**  
  作者: Pengsheng Guo, Hans Hao, Adam Caccavale, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2312.02189v1.pdf)  
  摘要: In the realm of text-to-3D generation, utilizing 2D diffusion models through score distillation sampling (SDS) frequently leads to issues such as blurred appearances and multi-faced geometry, primaril...  
  关键词: 3d gaussian, nerf  
- **[DISTWAR: Fast Differentiable Rendering on Raster-based Rendering Pipelines](https://arxiv.org/abs/2401.05345v1)**  
  作者: Sankeerth Durvasula, Adrian Zhao, Fan Chen, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2401.05345v1.pdf)  
  摘要: Differentiable rendering is a technique used in an important emerging class of visual computing applications that involves representing a 3D scene as a model that is trained from 2D images using gradi...  
  关键词: gaussian splatting, 3d gaussian  
- **[Segment Any 3D Gaussians](https://arxiv.org/abs/2312.00860v2)**  
  作者: Jiazhong Cen, Jiemin Fang, Chen Yang, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2312.00860v2.pdf)  
  摘要: This paper presents SAGA (Segment Any 3D GAussians), a highly efficient 3D promptable segmentation method based on 3D Gaussian Splatting (3D-GS). Given 2D visual prompts as input, SAGA can segment the...  
  关键词: gaussian splatting, 3d gaussian  
- **[Gaussian Grouping: Segment and Edit Anything in 3D Scenes](https://arxiv.org/abs/2312.00732v2)**  
  作者: Mingqiao Ye, Martin Danelljan, Fisher Yu, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2312.00732v2.pdf) | [![Stars](https://img.shields.io/github/stars/lkeab/gaussian-grouping?style=social)](https://github.com/lkeab/gaussian-grouping)  
  摘要: The recent Gaussian Splatting achieves high-quality and real-time novel-view synthesis of the 3D scenes. However, it is solely concentrated on the appearance and geometry modeling, while lacking in fi...  
  关键词: gaussian splatting, 3d gaussian, nerf  
- **[FSGS: Real-Time Few-shot View Synthesis using Gaussian Splatting](https://arxiv.org/abs/2312.00451v2)**  
  作者: Zehao Zhu, Zhiwen Fan, Yifan Jiang, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2312.00451v2.pdf)  
  摘要: Novel view synthesis from limited observations remains an important and persistent task. However, high efficiency in existing NeRF-based few-shot view synthesis is often compromised to obtain an accur...  
  关键词: gaussian splatting, 3d gaussian, nerf  
- **[NeuSG: Neural Implicit Surface Reconstruction with 3D Gaussian Splatting Guidance](https://arxiv.org/abs/2312.00846v1)**  
  作者: Hanlin Chen, Chen Li, Gim Hee Lee  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2312.00846v1.pdf)  
  摘要: Existing neural implicit surface reconstruction methods have achieved impressive performance in multi-view 3D reconstruction by leveraging explicit geometry priors such as depth maps or point clouds a...  
  关键词: gaussian splatting, 3d gaussian, 3d reconstruction  

### 2023年11月
- **[SparseGS: Real-Time 360° Sparse View Synthesis using Gaussian Splatting](https://arxiv.org/abs/2312.00206v2)**  
  作者: Haolin Xiong, Sairisheek Muttukuru, Rishi Upadhyay, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2312.00206v2.pdf)  
  摘要: The problem of novel view synthesis has grown significantly in popularity recently with the introduction of Neural Radiance Fields (NeRFs) and other implicit scene representation methods. A recent adv...  
  关键词: gaussian splatting, 3d gaussian, real-time rendering, nerf  
- **[DynMF: Neural Motion Factorization for Real-time Dynamic View Synthesis with 3D Gaussian Splatting](https://arxiv.org/abs/2312.00112v1)**  
  作者: Agelos Kratimenos, Jiahui Lei, Kostas Daniilidis  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2312.00112v1.pdf)  
  摘要: Accurately and efficiently modeling dynamic scenes and motions is considered so challenging a task due to temporal dynamics and motion complexity. To address these challenges, we propose DynMF, a comp...  
  关键词: gaussian splatting, 3d gaussian  
- **[DeformGS: Scene Flow in Highly Deformable Scenes for Deformable Object Manipulation](https://arxiv.org/abs/2312.00583v2)**  
  作者: Bardienus P. Duisterhof, Zhao Mandi, Yunchao Yao, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2312.00583v2.pdf)  
  摘要: Teaching robots to fold, drape, or reposition deformable objects such as cloth will unlock a variety of automation applications. While remarkable progress has been made for rigid object manipulation, ...  
  关键词: gaussian splatting  
- **[Scaffold-GS: Structured 3D Gaussians for View-Adaptive Rendering](https://arxiv.org/abs/2312.00109v1)**  
  作者: Tao Lu, Mulin Yu, Linning Xu, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2312.00109v1.pdf)  
  摘要: Neural rendering methods have significantly advanced photo-realistic 3D scene rendering in various academic and industrial applications. The recent 3D Gaussian Splatting method has achieved the state-...  
  关键词: gaussian splatting, 3d gaussian, neural rendering  
- **[Periodic Vibration Gaussian: Dynamic Urban Scene Reconstruction and Real-time Rendering](https://arxiv.org/abs/2311.18561v2)**  
  作者: Yurui Chen, Chun Gu, Junzhe Jiang, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2311.18561v2.pdf)  
  摘要: Modeling dynamic, large-scale urban scenes is challenging due to their highly intricate geometric structures and unconstrained dynamics in both space and time. Prior methods often employ high-level ar...  
  关键词: gaussian splatting, 3d gaussian  
- **[Language Embedded 3D Gaussians for Open-Vocabulary Scene Understanding](https://arxiv.org/abs/2311.18482v1)**  
  作者: Jin-Chuan Shi, Miao Wang, Hao-Bin Duan, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2311.18482v1.pdf)  
  摘要: Open-vocabulary querying in 3D space is challenging but essential for scene understanding tasks such as object localization and segmentation. Language-embedded scene representations have made progress...  
  关键词: 3d gaussian, real-time rendering  
- **[CompGS: Smaller and Faster Gaussian Splatting with Vector Quantization](https://arxiv.org/abs/2311.18159v3)**  
  作者: KL Navaneet, Kossar Pourahmadi Meibodi, Soroush Abbasi Koohpayegani, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2311.18159v3.pdf)  
  摘要: 3D Gaussian Splatting (3DGS) is a new method for modeling and rendering 3D radiance fields that achieves much faster learning and rendering time compared to SOTA NeRF methods. However, it comes with a...  
  关键词: gaussian splatting, 3d gaussian, nerf  
- **[HUGS: Human Gaussian Splats](https://arxiv.org/abs/2311.17910v1)**  
  作者: Muhammed Kocabas, Jen-Hao Rick Chang, James Gabriel, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2311.17910v1.pdf) | [![Stars](https://img.shields.io/github/stars/apple/ml-hugs?style=social)](https://github.com/apple/ml-hugs)  
  摘要: Recent advances in neural rendering have improved both training and rendering times by orders of magnitude. While these methods demonstrate state-of-the-art quality and speed, they are designed for ph...  
  关键词: gaussian splatting, 3d gaussian, neural rendering  
- **[CG3D: Compositional Generation for Text-to-3D via Gaussian Splatting](https://arxiv.org/abs/2311.17907v1)**  
  作者: Alexander Vilesov, Pradyumna Chari, Achuta Kadambi  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2311.17907v1.pdf)  
  摘要: With the onset of diffusion-based generative models and their ability to generate text-conditioned images, content generation has received a massive invigoration. Recently, these models have been show...  
- **[FisherRF: Active View Selection and Uncertainty Quantification for Radiance Fields using Fisher Information](https://arxiv.org/abs/2311.17874v1)**  
  作者: Wen Jiang, Boshu Lei, Kostas Daniilidis  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2311.17874v1.pdf)  
  摘要: This study addresses the challenging problem of active view selection and uncertainty quantification within the domain of Radiance Fields. Neural Radiance Fields (NeRF) have greatly advanced image ren...  
  关键词: gaussian splatting, 3d gaussian, nerf  
- **[Gaussian Shell Maps for Efficient 3D Human Generation](https://arxiv.org/abs/2311.17857v1)**  
  作者: Rameen Abdal, Wang Yifan, Zifan Shi, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2311.17857v1.pdf)  
  摘要: Efficient generation of 3D digital humans is important in several industries, including virtual reality, social media, and cinematic production. 3D generative adversarial networks (GANs) have demonstr...  
  关键词: 3d gaussian  
- **[GaussianShader: 3D Gaussian Splatting with Shading Functions for Reflective Surfaces](https://arxiv.org/abs/2311.17977v1)**  
  作者: Yingwenqi Jiang, Jiadong Tu, Yuan Liu, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2311.17977v1.pdf)  
  摘要: The advent of neural 3D Gaussians has recently brought about a revolution in the field of neural rendering, facilitating the generation of high-quality renderings at real-time speeds. However, the exp...  
  关键词: gaussian splatting, 3d gaussian, neural rendering, nerf  
- **[LightGaussian: Unbounded 3D Gaussian Compression with 15x Reduction and 200+ FPS](https://arxiv.org/abs/2311.17245v6)**  
  作者: Zhiwen Fan, Kevin Wang, Kairun Wen, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2311.17245v6.pdf)  
  摘要: Recent advances in real-time neural rendering using point-based techniques have enabled broader adoption of 3D representations. However, foundational approaches like 3D Gaussian Splatting impose subst...  
  关键词: gaussian splatting, 3d gaussian, neural rendering, nerf  
- **[HumanGaussian: Text-Driven 3D Human Generation with Gaussian Splatting](https://arxiv.org/abs/2311.17061v2)**  
  作者: Xian Liu, Xiaohang Zhan, Jiaxiang Tang, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2311.17061v2.pdf)  
  摘要: Realistic 3D human generation from text prompts is a desirable yet challenging task. Existing methods optimize 3D representations like mesh or neural fields via score distillation sampling (SDS), whic...  
  关键词: gaussian splatting, 3d gaussian  
- **[Point'n Move: Interactive Scene Object Manipulation on Gaussian Splatting Radiance Fields](https://arxiv.org/abs/2311.16737v1)**  
  作者: Jiajun Huang, Hongchuan Yu  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2311.16737v1.pdf)  
  摘要: We propose Point'n Move, a method that achieves interactive scene object manipulation with exposed region inpainting. Interactivity here further comes from intuitive object selection and real-time edi...  
  关键词: gaussian splatting  
- **[Human Gaussian Splatting: Real-time Rendering of Animatable Avatars](https://arxiv.org/abs/2311.17113v2)**  
  作者: Arthur Moreau, Jifei Song, Helisa Dhamo, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2311.17113v2.pdf)  
  摘要: This work addresses the problem of real-time rendering of photorealistic human body avatars learned from multi-view videos. While the classical approaches to model and render virtual humans generally ...  
  关键词: gaussian splatting, 3d gaussian, real-time rendering  
- **[Multi-Scale 3D Gaussian Splatting for Anti-Aliased Rendering](https://arxiv.org/abs/2311.17089v2)**  
  作者: Zhiwen Yan, Weng Fei Low, Yu Chen, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2311.17089v2.pdf)  
  摘要: 3D Gaussians have recently emerged as a highly efficient representation for 3D reconstruction and rendering. Despite its high rendering quality and speed at high resolutions, they both deteriorate dra...  
  关键词: gaussian splatting, 3d gaussian, 3d reconstruction, nerf  
- **[GART: Gaussian Articulated Template Models](https://arxiv.org/abs/2311.16099v1)**  
  作者: Jiahui Lei, Yufu Wang, Georgios Pavlakos, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2311.16099v1.pdf)  
  摘要: We introduce Gaussian Articulated Template Model GART, an explicit, efficient, and expressive representation for non-rigid articulated subject capturing and rendering from monocular videos. GART utili...  
  关键词: 3d gaussian  
- **[Animatable and Relightable Gaussians for High-fidelity Human Avatar Modeling](https://arxiv.org/abs/2311.16096v4)**  
  作者: Zhe Li, Yipengjing Sun, Zerong Zheng, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2311.16096v4.pdf)  
  摘要: Modeling animatable human avatars from RGB videos is a long-standing and challenging problem. Recent works usually adopt MLP-based neural radiance fields (NeRF) to represent 3D humans, but it remains ...  
  关键词: gaussian splatting, 3d gaussian, nerf  
- **[Relightable 3D Gaussians: Realistic Point Cloud Relighting with BRDF Decomposition and Ray Tracing](https://arxiv.org/abs/2311.16043v2)**  
  作者: Jian Gao, Chun Gu, Youtian Lin, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2311.16043v2.pdf)  
  摘要: In this paper, we present a novel differentiable point-based rendering framework to achieve photo-realistic relighting. To make the reconstructed scene relightable, we enhance vanilla 3D Gaussians by ...  
  关键词: gaussian splatting, 3d gaussian  
- **[GaussianEditor: Editing 3D Gaussians Delicately with Text Instructions](https://arxiv.org/abs/2311.16037v2)**  
  作者: Junjie Wang, Jiemin Fang, Xiaopeng Zhang, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2311.16037v2.pdf)  
  摘要: Recently, impressive results have been achieved in 3D scene editing with text instructions based on a 2D diffusion model. However, current diffusion models primarily generate images by predicting nois...  
  关键词: gaussian splatting, 3d gaussian, nerf  
- **[Mip-Splatting: Alias-free 3D Gaussian Splatting](https://arxiv.org/abs/2311.16493v1)**  
  作者: Zehao Yu, Anpei Chen, Binbin Huang, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2311.16493v1.pdf)  
  摘要: Recently, 3D Gaussian Splatting has demonstrated impressive novel view synthesis results, reaching high fidelity and efficiency. However, strong artifacts can be observed when changing the sampling ra...  
  关键词: gaussian splatting, 3d gaussian  
- **[Animatable 3D Gaussian: Fast and High-Quality Reconstruction of Multiple Human Avatars](https://arxiv.org/abs/2311.16482v3)**  
  作者: Yang Liu, Xiang Huang, Minghan Qin, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2311.16482v3.pdf)  
  摘要: Neural radiance fields are capable of reconstructing high-quality drivable human avatars but are expensive to train and render and not suitable for multi-human scenes with complex shadows. To reduce c...  
  关键词: 3d gaussian  
- **[GS-IR: 3D Gaussian Splatting for Inverse Rendering](https://arxiv.org/abs/2311.16473v3)**  
  作者: Zhihao Liang, Qi Zhang, Ying Feng, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2311.16473v3.pdf)  
  摘要: We propose GS-IR, a novel inverse rendering approach based on 3D Gaussian Splatting (GS) that leverages forward mapping volume rendering to achieve photorealistic novel view synthesis and relighting r...  
  关键词: gaussian splatting, 3d gaussian, nerf  
- **[GaussianEditor: Swift and Controllable 3D Editing with Gaussian Splatting](https://arxiv.org/abs/2311.14521v4)**  
  作者: Yiwen Chen, Zilong Chen, Chi Zhang, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2311.14521v4.pdf)  
  摘要: 3D editing plays a crucial role in many areas such as gaming and virtual reality. Traditional 3D editing methods, which rely on representations like meshes and point clouds, often fall short in realis...  
  关键词: gaussian splatting, nerf  
- **[Compact 3D Gaussian Representation for Radiance Field](https://arxiv.org/abs/2311.13681v2)**  
  作者: Joo Chan Lee, Daniel Rho, Xiangyu Sun, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2311.13681v2.pdf)  
  摘要: Neural Radiance Fields (NeRFs) have demonstrated remarkable potential in capturing complex 3D scenes with high fidelity. However, one persistent challenge that hinders the widespread adoption of NeRFs...  
  关键词: gaussian splatting, 3d gaussian, real-time rendering, nerf  
- **[Animatable 3D Gaussians for High-fidelity Synthesis of Human Motions](https://arxiv.org/abs/2311.13404v2)**  
  作者: Keyang Ye, Tianjia Shao, Kun Zhou  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2311.13404v2.pdf)  
  摘要: We present a novel animatable 3D Gaussian model for rendering high-fidelity free-view human motions in real time. Compared to existing NeRF-based methods, the model owns better capability in synthesiz...  
  关键词: 3d gaussian, nerf  
- **[Depth-Regularized Optimization for 3D Gaussian Splatting in Few-Shot Images](https://arxiv.org/abs/2311.13398v3)**  
  作者: Jaeyoung Chung, Jeongtaek Oh, Kyoung Mu Lee  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2311.13398v3.pdf)  
  摘要: In this paper, we present a method to optimize Gaussian splatting with a limited number of images while avoiding overfitting. Representing a 3D scene by combining numerous Gaussian splats has yielded ...  
  关键词: gaussian splatting, 3d gaussian, nerf  
- **[LucidDreamer: Domain-free Generation of 3D Gaussian Splatting Scenes](https://arxiv.org/abs/2311.13384v2)**  
  作者: Jaeyoung Chung, Suyoung Lee, Hyeongjin Nam, 等  
  链接: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2311.13384v2.pdf)  
  摘要: With the widespread usage of VR devices and contents, demands for 3D scene generation techniques become more popular. Existing 3D scene generation models, however, limit the target scene to specific d...  



## 经典论文
- **[3D Gaussian Splatting for Real-Time Radiance Field Rendering](https://repo-sam.inria.fr/fungraph/3d-gaussian-splatting/)** (SIGGRAPH 2023)  
  作者: Bernhard Kerbl, Georgios Kopanas, Thomas Leimkühler, George Drettakis  
  代码: 🔗 [GitHub](https://github.com/graphdeco-inria/gaussian-splatting)  
  关键词: Real-time Rendering, Neural Rendering, Point-based Graphics

## 开源项目
- [gaussian-splatting](https://github.com/graphdeco-inria/gaussian-splatting) - 原始的3D Gaussian Splatting实现
- [taichi-3d-gaussian-splatting](https://github.com/wanmeihuali/taichi-3d-gaussian-splatting) - 使用Taichi实现的3D Gaussian Splatting

## 应用
- [3D Gaussian Splatting for Real-Time Radiance Field Rendering Demo](https://repo-sam.inria.fr/fungraph/3d-gaussian-splatting/) - 在线演示

## 教程与博客
- [3D Gaussian Splatting介绍](https://github.com/graphdeco-inria/gaussian-splatting) - 官方教程

## 贡献指南
欢迎提交 Pull Request 来完善这个列表！请确保遵循以下格式：
- 论文条目格式：`**[论文标题](链接)** - 简短描述`
- 项目条目格式：`[项目名称](链接) - 项目描述`

## 许可证
[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/) 