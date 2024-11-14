# Awesome Gaussian Splatting [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

这个仓库收集了与 Gaussian Splatting 相关的最新研究论文、项目和资源。内容每日自动更新。

> 最后更新时间: 2024-11-14 14:31:52

## 目录

- [最新论文](#最新论文)
- [经典论文](#经典论文)
- [开源项目](#开源项目)
- [应用](#应用)
- [教程与博客](#教程与博客)

## 最新论文
> 🔄 每日更新

### 2024年11月
- **[4D Gaussian Splatting in the Wild with Uncertainty-Aware Regularization](https://arxiv.org/abs/2411.08879v1)**  
  作者: Mijeong Kim, Jongwoo Lim, Bohyung Han  
  链接: [📄 论文](https://arxiv.org/pdf/2411.08879v1.pdf)  
  摘要: Novel view synthesis of dynamic scenes is becoming important in various applications, including augmented and virtual reality. We propose a novel 4D Gaussian Splatting (4DGS) algorithm for dynamic sce...  
  关键词: gaussian splatting  
- **[Towards More Accurate Fake Detection on Images Generated from Advanced Generative and Neural Rendering Models](https://arxiv.org/abs/2411.08642v1)**  
  作者: Chengdong Dong, Vijayakumar Bhagavatula, Zhenyu Zhou, 等  
  链接: [📄 论文](https://arxiv.org/pdf/2411.08642v1.pdf)  
  摘要: The remarkable progress in neural-network-driven visual data generation, especially with neural rendering techniques like Neural Radiance Fields and 3D Gaussian splatting, offers a powerful alternativ...  
  关键词: gaussian splatting, 3d gaussian, neural rendering  
- **[BillBoard Splatting (BBSplat): Learnable Textured Primitives for Novel View Synthesis](https://arxiv.org/abs/2411.08508v1)**  
  作者: David Svitov, Pietro Morerio, Lourdes Agapito, 等  
  链接: [📄 论文](https://arxiv.org/pdf/2411.08508v1.pdf)  
  摘要: We present billboard Splatting (BBSplat) - a novel approach for 3D scene representation based on textured geometric primitives. BBSplat represents the scene as a set of optimizable textured planar pri...  
  关键词: gaussian splatting, nerf  
- **[Biomass phenotyping of oilseed rape through UAV multi-view oblique imaging with 3DGS and SAM model](https://arxiv.org/abs/2411.08453v1)**  
  作者: Yutao Shen, Hongyu Zhou, Xin Yang, 等  
  链接: [📄 论文](https://arxiv.org/pdf/2411.08453v1.pdf)  
  摘要: Biomass estimation of oilseed rape is crucial for optimizing crop productivity and breeding strategies. While UAV-based imaging has advanced high-throughput phenotyping, current methods often rely on ...  
  关键词: gaussian splatting, 3d gaussian, 3d reconstruction, nerf  
- **[DG-SLAM: Robust Dynamic Gaussian Splatting SLAM with Hybrid Pose Optimization](https://arxiv.org/abs/2411.08373v1)**  
  作者: Yueming Xu, Haochen Jiang, Zhongyang Xiao, 等  
  链接: [📄 论文](https://arxiv.org/pdf/2411.08373v1.pdf)  
  摘要: Achieving robust and precise pose estimation in dynamic scenes is a significant research challenge in Visual Simultaneous Localization and Mapping (SLAM). Recent advancements integrating Gaussian Spla...  
  关键词: gaussian splatting, 3d gaussian, real-time rendering  
- **[MBA-SLAM: Motion Blur Aware Dense Visual SLAM with Radiance Fields Representation](https://arxiv.org/abs/2411.08279v1)**  
  作者: Peng Wang, Lingzhe Zhao, Yin Zhang, 等  
  链接: [📄 论文](https://arxiv.org/pdf/2411.08279v1.pdf)  
  摘要: Emerging 3D scene representations, such as Neural Radiance Fields (NeRF) and 3D Gaussian Splatting (3DGS), have demonstrated their effectiveness in Simultaneous Localization and Mapping (SLAM) for pho...  
  关键词: gaussian splatting, 3d gaussian, nerf  
- **[Projecting Gaussian Ellipsoids While Avoiding Affine Projection Approximation](https://arxiv.org/abs/2411.07579v2)**  
  作者: Han Qi, Tao Cai, Xiyue Han  
  链接: [📄 论文](https://arxiv.org/pdf/2411.07579v2.pdf)  
  摘要: Recently, 3D Gaussian Splatting has dominated novel-view synthesis with its real-time rendering speed and state-of-the-art rendering quality. However, during the rendering process, the use of the Jaco...  
  关键词: gaussian splatting, 3d gaussian, real-time rendering  
- **[GaussianCut: Interactive segmentation via graph cut for 3D Gaussian Splatting](https://arxiv.org/abs/2411.07555v1)**  
  作者: Umangi Jain, Ashkan Mirzaei, Igor Gilitschenski  
  链接: [📄 论文](https://arxiv.org/pdf/2411.07555v1.pdf)  
  摘要: We introduce GaussianCut, a new method for interactive multiview segmentation of scenes represented as 3D Gaussians. Our approach allows for selecting the objects to be segmented by interacting with a...  
  关键词: gaussian splatting, 3d gaussian  
- **[HiCoM: Hierarchical Coherent Motion for Streamable Dynamic Scene with 3D Gaussian Splatting](https://arxiv.org/abs/2411.07541v1)**  
  作者: Qiankun Gao, Jiarui Meng, Chengxiang Wen, 等  
  链接: [📄 论文](https://arxiv.org/pdf/2411.07541v1.pdf)  
  摘要: The online reconstruction of dynamic scenes from multi-view streaming videos faces significant challenges in training, rendering and storage efficiency. Harnessing superior learning speed and real-tim...  
  关键词: gaussian splatting, 3d gaussian, real-time rendering  
- **[GUS-IR: Gaussian Splatting with Unified Shading for Inverse Rendering](https://arxiv.org/abs/2411.07478v1)**  
  作者: Zhihao Liang, Hongdong Li, Kui Jia, 等  
  链接: [📄 论文](https://arxiv.org/pdf/2411.07478v1.pdf)  
  摘要: Recovering the intrinsic physical attributes of a scene from images, generally termed as the inverse rendering problem, has been a central and challenging task in computer vision and computer graphics...  
  关键词: gaussian splatting, 3d gaussian  
- **[A Hierarchical Compression Technique for 3D Gaussian Splatting Compression](https://arxiv.org/abs/2411.06976v1)**  
  作者: He Huang, Wenjie Huang, Qi Yang, 等  
  链接: [📄 论文](https://arxiv.org/pdf/2411.06976v1.pdf)  
  摘要: 3D Gaussian Splatting (GS) demonstrates excellent rendering quality and generation speed in novel view synthesis. However, substantial data size poses challenges for storage and transmission, making 3...  
  关键词: gaussian splatting, 3d gaussian  
- **[Adaptive and Temporally Consistent Gaussian Surfels for Multi-view Dynamic Reconstruction](https://arxiv.org/abs/2411.06602v1)**  
  作者: Decai Chen, Brianne Oberson, Ingo Feldmann, 等  
  链接: [📄 论文](https://arxiv.org/pdf/2411.06602v1.pdf)  
  摘要: 3D Gaussian Splatting has recently achieved notable success in novel view synthesis for dynamic scenes and geometry reconstruction in static scenes. Building on these advancements, early methods have ...  
  关键词: gaussian splatting, 3d gaussian  
- **[SplatFormer: Point Transformer for Robust 3D Gaussian Splatting](https://arxiv.org/abs/2411.06390v2)**  
  作者: Yutong Chen, Marko Mihajlovic, Xiyi Chen, 等  
  链接: [📄 论文](https://arxiv.org/pdf/2411.06390v2.pdf)  
  摘要: 3D Gaussian Splatting (3DGS) has recently transformed photorealistic reconstruction, achieving high visual fidelity and real-time performance. However, rendering quality significantly deteriorates whe...  
  关键词: gaussian splatting, 3d gaussian  
- **[Through the Curved Cover: Synthesizing Cover Aberrated Scenes with Refractive Field](https://arxiv.org/abs/2411.06365v1)**  
  作者: Liuyue Xie, Jiancong Guo, Laszlo A. Jeni, 等  
  链接: [📄 论文](https://arxiv.org/pdf/2411.06365v1.pdf)  
  摘要: Recent extended reality headsets and field robots have adopted covers to protect the front-facing cameras from environmental hazards and falls. The surface irregularities on the cover can lead to opti...  
  关键词: gaussian splatting, 3d gaussian, nerf  
- **[AI-Driven Stylization of 3D Environments](https://arxiv.org/abs/2411.06067v1)**  
  作者: Yuanbo Chen, Yixiao Kang, Yukun Song, 等  
  链接: [📄 论文](https://arxiv.org/pdf/2411.06067v1.pdf)  
  摘要: In this system, we discuss methods to stylize a scene of 3D primitive objects into a higher fidelity 3D scene using novel 3D representations like NeRFs and 3D Gaussian Splatting. Our approach leverage...  
  关键词: gaussian splatting, 3d gaussian, nerf  
- **[GaussianSpa: An "Optimizing-Sparsifying" Simplification Framework for Compact and High-Quality 3D Gaussian Splatting](https://arxiv.org/abs/2411.06019v1)**  
  作者: Yangming Zhang, Wenqi Jia, Wei Niu, 等  
  链接: [📄 论文](https://arxiv.org/pdf/2411.06019v1.pdf)  
  摘要: 3D Gaussian Splatting (3DGS) has emerged as a mainstream for novel view synthesis, leveraging continuous aggregations of Gaussian functions to model scene geometry. However, 3DGS suffers from substant...  
  关键词: gaussian splatting, 3d gaussian  
- **[PEP-GS: Perceptually-Enhanced Precise Structured 3D Gaussians for View-Adaptive Rendering](https://arxiv.org/abs/2411.05731v1)**  
  作者: Junxi Jin, Xiulai Li, Haiping Huang, 等  
  链接: [📄 论文](https://arxiv.org/pdf/2411.05731v1.pdf)  
  摘要: Recent advances in structured 3D Gaussians for view-adaptive rendering, particularly through methods like Scaffold-GS, have demonstrated promising results in neural scene representation. However, exis...  
  关键词: 3d gaussian  
- **[ProEdit: Simple Progression is All You Need for High-Quality 3D Scene Editing](https://arxiv.org/abs/2411.05006v1)**  
  作者: Jun-Kun Chen, Yu-Xiong Wang  
  链接: [📄 论文](https://arxiv.org/pdf/2411.05006v1.pdf)  
  摘要: This paper proposes ProEdit - a simple yet effective framework for high-quality 3D scene editing guided by diffusion distillation in a novel progressive manner. Inspired by the crucial observation tha...  
  关键词: gaussian splatting, 3d gaussian  
- **[MVSplat360: Feed-Forward 360 Scene Synthesis from Sparse Views](https://arxiv.org/abs/2411.04924v1)**  
  作者: Yuedong Chen, Chuanxia Zheng, Haofei Xu, 等  
  链接: [📄 论文](https://arxiv.org/pdf/2411.04924v1.pdf)  
  摘要: We introduce MVSplat360, a feed-forward approach for 360{\deg} novel view synthesis (NVS) of diverse real-world scenes, using only sparse observations. This setting is inherently ill-posed due to mini...  
  关键词: gaussian splatting, 3d gaussian, 3d reconstruction  
- **[GS2Pose: Two-stage 6D Object Pose Estimation Guided by Gaussian Splatting](https://arxiv.org/abs/2411.03807v3)**  
  作者: Jilan Mei, Junbo Li, Cai Meng  
  链接: [📄 论文](https://arxiv.org/pdf/2411.03807v3.pdf)  
  摘要: This paper proposes a new method for accurate and robust 6D pose estimation of novel objects, named GS2Pose. By introducing 3D Gaussian splatting, GS2Pose can utilize the reconstruction results withou...  
  关键词: gaussian splatting, 3d gaussian  
- **[3DGS-CD: 3D Gaussian Splatting-based Change Detection for Physical Object Rearrangement](https://arxiv.org/abs/2411.03706v1)**  
  作者: Ziqi Lu, Jianbo Ye, John Leonard  
  链接: [📄 论文](https://arxiv.org/pdf/2411.03706v1.pdf)  
  摘要: We present 3DGS-CD, the first 3D Gaussian Splatting (3DGS)-based method for detecting physical object rearrangements in 3D scenes. Our approach estimates 3D object-level changes by comparing two sets ...  
  关键词: gaussian splatting, 3d gaussian  
- **[Structure Consistent Gaussian Splatting with Matching Prior for Few-shot Novel View Synthesis](https://arxiv.org/abs/2411.03637v1)**  
  作者: Rui Peng, Wangze Xu, Luyang Tang, 等  
  链接: [📄 论文](https://arxiv.org/pdf/2411.03637v1.pdf)  
  摘要: Despite the substantial progress of novel view synthesis, existing methods, either based on the Neural Radiance Fields (NeRF) or more recently 3D Gaussian Splatting (3DGS), suffer significant degradat...  
  关键词: gaussian splatting, 3d gaussian, nerf  
- **[Object and Contact Point Tracking in Demonstrations Using 3D Gaussian Splatting](https://arxiv.org/abs/2411.03555v1)**  
  作者: Michael Büttner, Jonathan Francis, Helge Rhodin, 等  
  链接: [📄 论文](https://arxiv.org/pdf/2411.03555v1.pdf)  
  摘要: This paper introduces a method to enhance Interactive Imitation Learning (IIL) by extracting touch interaction points and tracking object movement from video demonstrations. The approach extends curre...  
  关键词: gaussian splatting, 3d gaussian  
- **[HFGaussian: Learning Generalizable Gaussian Human with Integrated Human Features](https://arxiv.org/abs/2411.03086v1)**  
  作者: Arnab Dey, Cheng-You Lu, Andrew I. Comport, 等  
  链接: [📄 论文](https://arxiv.org/pdf/2411.03086v1.pdf)  
  摘要: Recent advancements in radiance field rendering show promising results in 3D scene representation, where Gaussian splatting-based techniques emerge as state-of-the-art due to their quality and efficie...  
  关键词: gaussian splatting, 3d gaussian  
- **[LVI-GS: Tightly-coupled LiDAR-Visual-Inertial SLAM using 3D Gaussian Splatting](https://arxiv.org/abs/2411.02703v1)**  
  作者: Huibin Zhao, Weipeng Guan, Peng Lu  
  链接: [📄 论文](https://arxiv.org/pdf/2411.02703v1.pdf)  
  摘要: 3D Gaussian Splatting (3DGS) has shown its ability in rapid rendering and high-fidelity mapping. In this paper, we introduce LVI-GS, a tightly-coupled LiDAR-Visual-Inertial mapping framework with 3DGS...  
  关键词: gaussian splatting, 3d gaussian, 3d reconstruction  
- **[Modeling Uncertainty in 3D Gaussian Splatting through Continuous Semantic Splatting](https://arxiv.org/abs/2411.02547v1)**  
  作者: Joey Wilson, Marcelino Almeida, Min Sun, 等  
  链接: [📄 论文](https://arxiv.org/pdf/2411.02547v1.pdf)  
  摘要: In this paper, we present a novel algorithm for probabilistically updating and rasterizing semantic maps within 3D Gaussian Splatting (3D-GS). Although previous methods have introduced algorithms whic...  
  关键词: gaussian splatting, 3d gaussian  
- **[SplatOverflow: Asynchronous Hardware Troubleshooting](https://arxiv.org/abs/2411.02332v2)**  
  作者: Amritansh Kwatra, Tobias Wienberg, Ilan Mandel, 等  
  链接: [📄 论文](https://arxiv.org/pdf/2411.02332v2.pdf)  
  摘要: As tools for designing and manufacturing hardware become more accessible, smaller producers can develop and distribute novel hardware. However, there aren't established tools to support end-user hardw...  
  关键词: 3d gaussian  
- **[FewViewGS: Gaussian Splatting with Few View Matching and Multi-stage Training](https://arxiv.org/abs/2411.02229v2)**  
  作者: Ruihong Yin, Vladimir Yugay, Yue Li, 等  
  链接: [📄 论文](https://arxiv.org/pdf/2411.02229v2.pdf)  
  摘要: The field of novel view synthesis from images has seen rapid advancements with the introduction of Neural Radiance Fields (NeRF) and more recently with 3D Gaussian Splatting. Gaussian Splatting became...  
  关键词: gaussian splatting, 3d gaussian, nerf  
- **[GVKF: Gaussian Voxel Kernel Functions for Highly Efficient Surface Reconstruction in Open Scenes](https://arxiv.org/abs/2411.01853v2)**  
  作者: Gaochao Song, Chong Cheng, Hao Wang  
  链接: [📄 论文](https://arxiv.org/pdf/2411.01853v2.pdf)  
  摘要: In this paper we present a novel method for efficient and effective 3D surface reconstruction in open scenes. Existing Neural Radiance Fields (NeRF) based works typically require extensive training an...  
  关键词: gaussian splatting, 3d gaussian, real-time rendering, nerf  
- **[Real-Time Spatio-Temporal Reconstruction of Dynamic Endoscopic Scenes with 4D Gaussian Splatting](https://arxiv.org/abs/2411.01218v1)**  
  作者: Fengze Li, Jishuai He, Jieming Ma, 等  
  链接: [📄 论文](https://arxiv.org/pdf/2411.01218v1.pdf)  
  摘要: Dynamic scene reconstruction is essential in robotic minimally invasive surgery, providing crucial spatial information that enhances surgical precision and outcomes. However, existing methods struggle...  
  关键词: gaussian splatting  
- **[CityGaussianV2: Efficient and Geometrically Accurate Reconstruction for Large-Scale Scenes](https://arxiv.org/abs/2411.00771v1)**  
  作者: Yang Liu, Chuanchen Luo, Zhongkai Mao, 等  
  链接: [📄 论文](https://arxiv.org/pdf/2411.00771v1.pdf)  
  摘要: Recently, 3D Gaussian Splatting (3DGS) has revolutionized radiance field reconstruction, manifesting efficient and high-fidelity novel view synthesis. However, accurately representing surfaces, especi...  
  关键词: gaussian splatting, 3d gaussian  
- **[PCoTTA: Continual Test-Time Adaptation for Multi-Task Point Cloud Understanding](https://arxiv.org/abs/2411.00632v1)**  
  作者: Jincen Jiang, Qianyu Zhou, Yuhang Li, 等  
  链接: [📄 论文](https://arxiv.org/pdf/2411.00632v1.pdf)  
  摘要: In this paper, we present PCoTTA, an innovative, pioneering framework for Continual Test-Time Adaptation (CoTTA) in multi-task point cloud understanding, enhancing the model's transferability towards ...  

### 2024年10月
- **[Aquatic-GS: A Hybrid 3D Representation for Underwater Scenes](https://arxiv.org/abs/2411.00239v1)**  
  作者: Shaohua Liu, Junzhe Lu, Zuoya Gu, 等  
  链接: [📄 论文](https://arxiv.org/pdf/2411.00239v1.pdf)  
  摘要: Representing underwater 3D scenes is a valuable yet complex task, as attenuation and scattering effects during underwater imaging significantly couple the information of the objects and the water. Thi...  
  关键词: gaussian splatting, 3d gaussian, real-time rendering  
- **[Self-Ensembling Gaussian Splatting for Few-shot Novel View Synthesis](https://arxiv.org/abs/2411.00144v1)**  
  作者: Chen Zhao, Xuan Wang, Tong Zhang, 等  
  链接: [📄 论文](https://arxiv.org/pdf/2411.00144v1.pdf)  
  摘要: 3D Gaussian Splatting (3DGS) has demonstrated remarkable effectiveness for novel view synthesis (NVS). However, the 3DGS model tends to overfit when trained with sparse posed views, limiting its gener...  
  关键词: gaussian splatting, 3d gaussian, nerf  
- **[URAvatar: Universal Relightable Gaussian Codec Avatars](https://arxiv.org/abs/2410.24223v1)**  
  作者: Junxuan Li, Chen Cao, Gabriel Schwartz, 等  
  链接: [📄 论文](https://arxiv.org/pdf/2410.24223v1.pdf)  
  摘要: We present a new approach to creating photorealistic and relightable head avatars from a phone scan with unknown illumination. The reconstructed avatars can be animated and relit in real time with the...  
  关键词: 3d gaussian, real-time rendering  
- **[No Pose, No Problem: Surprisingly Simple 3D Gaussian Splats from Sparse Unposed Images](https://arxiv.org/abs/2410.24207v1)**  
  作者: Botao Ye, Sifei Liu, Haofei Xu, 等  
  链接: [📄 论文](https://arxiv.org/pdf/2410.24207v1.pdf)  
  摘要: We introduce NoPoSplat, a feed-forward model capable of reconstructing 3D scenes parameterized by 3D Gaussians from \textit{unposed} sparse multi-view images. Our model, trained exclusively with photo...  
  关键词: 3d gaussian, 3d reconstruction  
- **[GeoSplatting: Towards Geometry Guided Gaussian Splatting for Physically-based Inverse Rendering](https://arxiv.org/abs/2410.24204v2)**  
  作者: Kai Ye, Chong Gao, Guanbin Li, 等  
  链接: [📄 论文](https://arxiv.org/pdf/2410.24204v2.pdf)  
  摘要: We consider the problem of physically-based inverse rendering using 3D Gaussian Splatting (3DGS) representations. While recent 3DGS methods have achieved remarkable results in novel view synthesis (NV...  
  关键词: gaussian splatting, 3d gaussian  
- **[GaussianMarker: Uncertainty-Aware Copyright Protection of 3D Gaussian Splatting](https://arxiv.org/abs/2410.23718v1)**  
  作者: Xiufeng Huang, Ruiqi Li, Yiu-ming Cheung, 等  
  链接: [📄 论文](https://arxiv.org/pdf/2410.23718v1.pdf)  
  摘要: 3D Gaussian Splatting (3DGS) has become a crucial method for acquiring 3D assets. To protect the copyright of these assets, digital watermarking techniques can be applied to embed ownership informatio...  
  关键词: gaussian splatting, 3d gaussian, nerf  
- **[GS-Blur: A 3D Scene-Based Dataset for Realistic Image Deblurring](https://arxiv.org/abs/2410.23658v1)**  
  作者: Dongwoo Lee, Joonkyu Park, Kyoung Mu Lee  
  链接: [📄 论文](https://arxiv.org/pdf/2410.23658v1.pdf)  
  摘要: To train a deblurring network, an appropriate dataset with paired blurry and sharp images is essential. Existing datasets collect blurry images either synthetically by aggregating consecutive sharp fr...  
  关键词: gaussian splatting, 3d gaussian  
- **[ELMGS: Enhancing memory and computation scaLability through coMpression for 3D Gaussian Splatting](https://arxiv.org/abs/2410.23213v1)**  
  作者: Muhammad Salman Ali, Sung-Ho Bae, Enzo Tartaglione  
  链接: [📄 论文](https://arxiv.org/pdf/2410.23213v1.pdf)  
  摘要: 3D models have recently been popularized by the potentiality of end-to-end training offered first by Neural Radiance Fields and most recently by 3D Gaussian Splatting models. The latter has the big ad...  
  关键词: gaussian splatting, 3d gaussian  
- **[Epipolar-Free 3D Gaussian Splatting for Generalizable Novel View Synthesis](https://arxiv.org/abs/2410.22817v2)**  
  作者: Zhiyuan Min, Yawei Luo, Jianwen Sun, 等  
  链接: [📄 论文](https://arxiv.org/pdf/2410.22817v2.pdf)  
  摘要: Generalizable 3D Gaussian splitting (3DGS) can reconstruct new scenes from sparse-view observations in a feed-forward inference manner, eliminating the need for scene-specific retraining required in c...  
  关键词: 3d gaussian  
- **[Geometry Cloak: Preventing TGS-based 3D Reconstruction from Copyrighted Images](https://arxiv.org/abs/2410.22705v1)**  
  作者: Qi Song, Ziyuan Luo, Ka Chun Cheung, 等  
  链接: [📄 论文](https://arxiv.org/pdf/2410.22705v1.pdf)  
  摘要: Single-view 3D reconstruction methods like Triplane Gaussian Splatting (TGS) have enabled high-quality 3D model generation from just a single image input within seconds. However, this capability raise...  
  关键词: gaussian splatting, 3d reconstruction  
- **[PF3plat: Pose-Free Feed-Forward 3D Gaussian Splatting](https://arxiv.org/abs/2410.22128v1)**  
  作者: Sunghwan Hong, Jaewoo Jung, Heeseong Shin, 等  
  链接: [📄 论文](https://arxiv.org/pdf/2410.22128v1.pdf)  
  摘要: We consider the problem of novel view synthesis from unposed images in a single feed-forward. Our framework capitalizes on fast speed, scalability, and high-quality 3D reconstruction and view synthesi...  
  关键词: 3d gaussian, 3d reconstruction  
- **[FreeGaussian: Guidance-free Controllable 3D Gaussian Splats with Flow Derivatives](https://arxiv.org/abs/2410.22070v1)**  
  作者: Qizhi Chen, Delin Qu, Yiwen Tang, 等  
  链接: [📄 论文](https://arxiv.org/pdf/2410.22070v1.pdf)  
  摘要: Reconstructing controllable Gaussian splats from monocular video is a challenging task due to its inherently insufficient constraints. Widely adopted approaches supervise complex interactions with add...  
  关键词: 3d gaussian  
- **[ActiveSplat: High-Fidelity Scene Reconstruction through Active Gaussian Splatting](https://arxiv.org/abs/2410.21955v1)**  
  作者: Yuetao Li, Zijia Kuang, Ting Li, 等  
  链接: [📄 论文](https://arxiv.org/pdf/2410.21955v1.pdf)  
  摘要: We propose ActiveSplat, an autonomous high-fidelity reconstruction system leveraging Gaussian splatting. Taking advantage of efficient and realistic rendering, the system establishes a unified framewo...  
  关键词: gaussian splatting  
- **[MVSDet: Multi-View Indoor 3D Object Detection via Efficient Plane Sweeps](https://arxiv.org/abs/2410.21566v1)**  
  作者: Yating Xu, Chen Li, Gim Hee Lee  
  链接: [📄 论文](https://arxiv.org/pdf/2410.21566v1.pdf)  
  摘要: The key challenge of multi-view indoor 3D object detection is to infer accurate geometry information from images for precise 3D detection. Previous method relies on NeRF for geometry reasoning. Howeve...  
  关键词: gaussian splatting, nerf  
- **[Grid4D: 4D Decomposed Hash Encoding for High-fidelity Dynamic Gaussian Splatting](https://arxiv.org/abs/2410.20815v1)**  
  作者: Jiawei Xu, Zexin Fan, Jian Yang, 等  
  链接: [📄 论文](https://arxiv.org/pdf/2410.20815v1.pdf)  
  摘要: Recently, Gaussian splatting has received more and more attention in the field of static scene rendering. Due to the low computational overhead and inherent flexibility of explicit representations, pl...  
  关键词: gaussian splatting  
- **[LoDAvatar: Hierarchical Embedding and Adaptive Levels of Detail with Gaussian Splatting for Enhanced Human Avatars](https://arxiv.org/abs/2410.20789v1)**  
  作者: Xiaonuo Dongye, Hanzhi Guo, Le Luo, 等  
  链接: [📄 论文](https://arxiv.org/pdf/2410.20789v1.pdf)  
  摘要: With the advancement of virtual reality, the demand for 3D human avatars is increasing. The emergence of Gaussian Splatting technology has enabled the rendering of Gaussian avatars with superior visua...  
  关键词: gaussian splatting  
- **[CompGS: Unleashing 2D Compositionality for Compositional Text-to-3D via Dynamically Optimizing 3D Gaussians](https://arxiv.org/abs/2410.20723v1)**  
  作者: Chongjian Ge, Chenfeng Xu, Yuanfeng Ji, 等  
  链接: [📄 论文](https://arxiv.org/pdf/2410.20723v1.pdf)  
  摘要: Recent breakthroughs in text-guided image generation have significantly advanced the field of 3D generation. While generating a single high-quality 3D object is now feasible, generating multiple objec...  
  关键词: gaussian splatting, 3d gaussian  
- **[ODGS: 3D Scene Reconstruction from Omnidirectional Images with 3D Gaussian Splattings](https://arxiv.org/abs/2410.20686v1)**  
  作者: Suyoung Lee, Jaeyoung Chung, Jaeyoo Huh, 等  
  链接: [📄 论文](https://arxiv.org/pdf/2410.20686v1.pdf)  
  摘要: Omnidirectional (or 360-degree) images are increasingly being used for 3D applications since they allow the rendering of an entire scene with a single image. Existing works based on neural radiance fi...  
  关键词: gaussian splatting, 3d gaussian, real-time rendering, 3d reconstruction, nerf  
- **[Normal-GS: 3D Gaussian Splatting with Normal-Involved Rendering](https://arxiv.org/abs/2410.20593v1)**  
  作者: Meng Wei, Qianyi Wu, Jianmin Zheng, 等  
  链接: [📄 论文](https://arxiv.org/pdf/2410.20593v1.pdf)  
  摘要: Rendering and reconstruction are long-standing topics in computer vision and graphics. Achieving both high rendering quality and accurate geometry is a challenge. Recent advancements in 3D Gaussian Sp...  
  关键词: gaussian splatting, 3d gaussian, real-time rendering  
- **[Neural Fields in Robotics: A Survey](https://arxiv.org/abs/2410.20220v1)**  
  作者: Muhammad Zubair Irshad, Mauro Comi, Yen-Chen Lin, 等  
  链接: [📄 论文](https://arxiv.org/pdf/2410.20220v1.pdf)  
  摘要: Neural Fields have emerged as a transformative approach for 3D scene representation in computer vision and robotics, enabling accurate inference of geometry, 3D semantics, and dynamics from posed 2D d...  
  关键词: gaussian splatting, 3d reconstruction, nerf  
- **[SCube: Instant Large-Scale Scene Reconstruction using VoxSplats](https://arxiv.org/abs/2410.20030v1)**  
  作者: Xuanchi Ren, Yifan Lu, Hanxue Liang, 等  
  链接: [📄 论文](https://arxiv.org/pdf/2410.20030v1.pdf)  
  摘要: We present SCube, a novel method for reconstructing large-scale 3D scenes (geometry, appearance, and semantics) from a sparse set of posed images. Our method encodes reconstructed scenes using a novel...  
  关键词: 3d gaussian, 3d reconstruction  
- **[DiffGS: Functional Gaussian Splatting Diffusion](https://arxiv.org/abs/2410.19657v2)**  
  作者: Junsheng Zhou, Weiqi Zhang, Yu-Shen Liu  
  链接: [📄 论文](https://arxiv.org/pdf/2410.19657v2.pdf)  
  摘要: 3D Gaussian Splatting (3DGS) has shown convincing performance in rendering speed and fidelity, yet the generation of Gaussian Splatting remains a challenge due to its discreteness and unstructured nat...  
  关键词: gaussian splatting, 3d gaussian  
- **[Robotic Learning in your Backyard: A Neural Simulator from Open Source Components](https://arxiv.org/abs/2410.19564v1)**  
  作者: Liyou Zhou, Oleg Sinavski, Athanasios Polydoros  
  链接: [📄 论文](https://arxiv.org/pdf/2410.19564v1.pdf)  
  摘要: The emergence of 3D Gaussian Splatting for fast and high-quality novel view synthesize has opened up the possibility to construct photo-realistic simulations from video for robotic reinforcement learn...  
  关键词: gaussian splatting, 3d gaussian  
- **[Content-Aware Radiance Fields: Aligning Model Complexity with Scene Intricacy Through Learned Bitwidth Quantization](https://arxiv.org/abs/2410.19483v1)**  
  作者: Weihang Liu, Xue Xian Zheng, Jingyi Yu, 等  
  链接: [📄 论文](https://arxiv.org/pdf/2410.19483v1.pdf)  
  摘要: The recent popular radiance field models, exemplified by Neural Radiance Fields (NeRF), Instant-NGP and 3D Gaussian Splatting, are designed to represent 3D content by that training models for each ind...  
  关键词: gaussian splatting, 3d gaussian, nerf  
- **[ArCSEM: Artistic Colorization of SEM Images via Gaussian Splatting](https://arxiv.org/abs/2410.21310v1)**  
  作者: Takuma Nishimura, Andreea Dogaru, Martin Oeggerli, 等  
  链接: [📄 论文](https://arxiv.org/pdf/2410.21310v1.pdf)  
  摘要: Scanning Electron Microscopes (SEMs) are widely renowned for their ability to analyze the surface structures of microscopic objects, offering the capability to capture highly detailed, yet only graysc...  
- **[PixelGaussian: Generalizable 3D Gaussian Reconstruction from Arbitrary Views](https://arxiv.org/abs/2410.18979v1)**  
  作者: Xin Fei, Wenzhao Zheng, Yueqi Duan, 等  
  链接: [📄 论文](https://arxiv.org/pdf/2410.18979v1.pdf)  
  摘要: We propose PixelGaussian, an efficient feed-forward framework for learning generalizable 3D Gaussian reconstruction from arbitrary views. Most existing methods rely on uniform pixel-wise Gaussian repr...  
  关键词: 3d gaussian  
- **[3D-Adapter: Geometry-Consistent Multi-View Diffusion for High-Quality 3D Generation](https://arxiv.org/abs/2410.18974v1)**  
  作者: Hansheng Chen, Bokui Shen, Yulin Liu, 等  
  链接: [📄 论文](https://arxiv.org/pdf/2410.18974v1.pdf)  
  摘要: Multi-view image diffusion models have significantly advanced open-domain 3D object generation. However, most existing models rely on 2D network architectures that lack inherent 3D biases, resulting i...  
  关键词: gaussian splatting  
- **[Sort-free Gaussian Splatting via Weighted Sum Rendering](https://arxiv.org/abs/2410.18931v1)**  
  作者: Qiqi Hou, Randall Rauwendaal, Zifeng Li, 等  
  链接: [📄 论文](https://arxiv.org/pdf/2410.18931v1.pdf)  
  摘要: Recently, 3D Gaussian Splatting (3DGS) has emerged as a significant advancement in 3D scene reconstruction, attracting considerable attention due to its ability to recover high-fidelity details while ...  
  关键词: gaussian splatting, 3d gaussian  
- **[Dynamic 3D Gaussian Tracking for Graph-Based Neural Dynamics Modeling](https://arxiv.org/abs/2410.18912v1)**  
  作者: Mingtong Zhang, Kaifeng Zhang, Yunzhu Li  
  链接: [📄 论文](https://arxiv.org/pdf/2410.18912v1.pdf)  
  摘要: Videos of robots interacting with objects encode rich information about the objects' dynamics. However, existing video prediction approaches typically do not explicitly account for the 3D information ...  
  关键词: gaussian splatting, 3d gaussian  
- **[Binocular-Guided 3D Gaussian Splatting with View Consistency for Sparse View Synthesis](https://arxiv.org/abs/2410.18822v2)**  
  作者: Liang Han, Junsheng Zhou, Yu-Shen Liu, 等  
  链接: [📄 论文](https://arxiv.org/pdf/2410.18822v2.pdf)  
  摘要: Novel view synthesis from sparse inputs is a vital yet challenging task in 3D computer vision. Previous methods explore 3D Gaussian Splatting with neural priors (e.g. depth priors) as an additional su...  
  关键词: gaussian splatting, 3d gaussian, nerf  
- **[VR-Splatting: Foveated Radiance Field Rendering via 3D Gaussian Splatting and Neural Points](https://arxiv.org/abs/2410.17932v1)**  
  作者: Linus Franke, Laura Fink, Marc Stamminger  
  链接: [📄 论文](https://arxiv.org/pdf/2410.17932v1.pdf)  
  摘要: Recent advances in novel view synthesis (NVS), particularly neural radiance fields (NeRF) and Gaussian splatting (3DGS), have demonstrated impressive results in photorealistic scene rendering. These t...  
  关键词: gaussian splatting, nerf  
- **[PLGS: Robust Panoptic Lifting with 3D Gaussian Splatting](https://arxiv.org/abs/2410.17505v1)**  
  作者: Yu Wang, Xiaobao Wei, Ming Lu, 等  
  链接: [📄 论文](https://arxiv.org/pdf/2410.17505v1.pdf)  
  摘要: Previous methods utilize the Neural Radiance Field (NeRF) for panoptic lifting, while their training and rendering speed are unsatisfactory. In contrast, 3D Gaussian Splatting (3DGS) has emerged as a ...  
  关键词: gaussian splatting, 3d gaussian, nerf  
- **[AG-SLAM: Active Gaussian Splatting SLAM](https://arxiv.org/abs/2410.17422v1)**  
  作者: Wen Jiang, Boshu Lei, Katrina Ashton, 等  
  链接: [📄 论文](https://arxiv.org/pdf/2410.17422v1.pdf)  
  摘要: We present AG-SLAM, the first active SLAM system utilizing 3D Gaussian Splatting (3DGS) for online scene reconstruction. In recent years, radiance field scene representations, including 3DGS have been...  
  关键词: gaussian splatting, 3d gaussian  
- **[SpectroMotion: Dynamic 3D Reconstruction of Specular Scenes](https://arxiv.org/abs/2410.17249v1)**  
  作者: Cheng-De Fan, Chen-Wei Chang, Yi-Ruei Liu, 等  
  链接: [📄 论文](https://arxiv.org/pdf/2410.17249v1.pdf)  
  摘要: We present SpectroMotion, a novel approach that combines 3D Gaussian Splatting (3DGS) with physically-based rendering (PBR) and deformation fields to reconstruct dynamic specular scenes. Previous meth...  
  关键词: gaussian splatting, 3d gaussian  
- **[E-3DGS: Gaussian Splatting with Exposure and Motion Events](https://arxiv.org/abs/2410.16995v1)**  
  作者: Xiaoting Yin, Hao Shi, Yuhan Bao, 等  
  链接: [📄 论文](https://arxiv.org/pdf/2410.16995v1.pdf)  
  摘要: Estimating Neural Radiance Fields (NeRFs) from images captured under optimal conditions has been extensively explored in the vision community. However, robotic applications often face challenges such ...  
  关键词: gaussian splatting, 3d gaussian, 3d reconstruction, nerf  
- **[Multi-Layer Gaussian Splatting for Immersive Anatomy Visualization](https://arxiv.org/abs/2410.16978v1)**  
  作者: Constantin Kleinbeck, Hannah Schieber, Klaus Engel, 等  
  链接: [📄 论文](https://arxiv.org/pdf/2410.16978v1.pdf)  
  摘要: In medical image visualization, path tracing of volumetric medical data like CT scans produces lifelike three-dimensional visualizations. Immersive VR displays can further enhance the understanding of...  
- **[MvDrag3D: Drag-based Creative 3D Editing via Multi-view Generation-Reconstruction Priors](https://arxiv.org/abs/2410.16272v1)**  
  作者: Honghua Chen, Yushi Lan, Yongwei Chen, 等  
  链接: [📄 论文](https://arxiv.org/pdf/2410.16272v1.pdf)  
  摘要: Drag-based editing has become popular in 2D content creation, driven by the capabilities of image generative models. However, extending this technique to 3D remains a challenge. Existing 3D drag-based...  
  关键词: 3d gaussian  
- **[3DGS-Enhancer: Enhancing Unbounded 3D Gaussian Splatting with View-consistent 2D Diffusion Priors](https://arxiv.org/abs/2410.16266v1)**  
  作者: Xi Liu, Chaoyi Zhou, Siyu Huang  
  链接: [📄 论文](https://arxiv.org/pdf/2410.16266v1.pdf)  
  摘要: Novel-view synthesis aims to generate novel views of a scene from multiple input images or videos, and recent advancements like 3D Gaussian splatting (3DGS) have achieved notable success in producing ...  
  关键词: gaussian splatting, 3d gaussian  
- **[MSGField: A Unified Scene Representation Integrating Motion, Semantics, and Geometry for Robotic Manipulation](https://arxiv.org/abs/2410.15730v1)**  
  作者: Yu Sheng, Runfeng Lin, Lidian Wang, 等  
  链接: [📄 论文](https://arxiv.org/pdf/2410.15730v1.pdf)  
  摘要: Combining accurate geometry with rich semantics has been proven to be highly effective for language-guided robotic manipulation. Existing methods for dynamic scenes either fail to update in real-time ...  
  关键词: gaussian splatting, real-time rendering  
- **[LucidFusion: Generating 3D Gaussians with Arbitrary Unposed Images](https://arxiv.org/abs/2410.15636v2)**  
  作者: Hao He, Yixun Liang, Luozhou Wang, 等  
  链接: [📄 论文](https://arxiv.org/pdf/2410.15636v2.pdf)  
  摘要: Recent large reconstruction models have made notable progress in generating high-quality 3D objects from single images. However, these methods often struggle with controllability, as they lack informa...  
  关键词: 3d gaussian, 3d reconstruction  
- **[Fully Explicit Dynamic Gaussian Splatting](https://arxiv.org/abs/2410.15629v2)**  
  作者: Junoh Lee, Chang-Yeon Won, Hyunjun Jung, 等  
  链接: [📄 论文](https://arxiv.org/pdf/2410.15629v2.pdf)  
  摘要: 3D Gaussian Splatting has shown fast and high-quality rendering results in static scenes by leveraging dense 3D prior and explicit representations. Unfortunately, the benefits of the prior and represe...  
  关键词: gaussian splatting, 3d gaussian  
- **[EF-3DGS: Event-Aided Free-Trajectory 3D Gaussian Splatting](https://arxiv.org/abs/2410.15392v2)**  
  作者: Bohao Liao, Wei Zhai, Zengyu Wan, 等  
  链接: [📄 论文](https://arxiv.org/pdf/2410.15392v2.pdf)  
  摘要: Scene reconstruction from casually captured videos has wide applications in real-world scenarios. With recent advancements in differentiable rendering techniques, several methods have attempted to sim...  
  关键词: nerf  
- **[GS-LIVM: Real-Time Photo-Realistic LiDAR-Inertial-Visual Mapping with Gaussian Splatting](https://arxiv.org/abs/2410.17084v1)**  
  作者: Yusen Xie, Zhenmin Huang, Jin Wu, 等  
  链接: [📄 论文](https://arxiv.org/pdf/2410.17084v1.pdf)  
  摘要: In this paper, we introduce GS-LIVM, a real-time photo-realistic LiDAR-Inertial-Visual mapping framework with Gaussian Splatting tailored for outdoor scenes. Compared to existing methods based on Neur...  
  关键词: gaussian splatting, 3d gaussian, nerf  
- **[LUDVIG: Learning-free Uplifting of 2D Visual features to Gaussian Splatting scenes](https://arxiv.org/abs/2410.14462v1)**  
  作者: Juliette Marrie, Romain Ménégaux, Michael Arbel, 等  
  链接: [📄 论文](https://arxiv.org/pdf/2410.14462v1.pdf)  
  摘要: We address the task of uplifting visual features or semantic masks from 2D vision models to 3D scenes represented by Gaussian Splatting. Whereas common approaches rely on iterative optimization-based ...  
  关键词: gaussian splatting  
- **[Neural Signed Distance Function Inference through Splatting 3D Gaussians Pulled on Zero-Level Set](https://arxiv.org/abs/2410.14189v1)**  
  作者: Wenyuan Zhang, Yu-Shen Liu, Zhizhong Han  
  链接: [📄 论文](https://arxiv.org/pdf/2410.14189v1.pdf)  
  摘要: It is vital to infer a signed distance function (SDF) in multi-view based surface reconstruction. 3D Gaussian splatting (3DGS) provides a novel perspective for volume rendering, and shows advantages i...  
  关键词: gaussian splatting, 3d gaussian, neural rendering  
- **[DaRePlane: Direction-aware Representations for Dynamic Scene Reconstruction](https://arxiv.org/abs/2410.14169v1)**  
  作者: Ange Lou, Benjamin Planche, Zhongpai Gao, 等  
  链接: [📄 论文](https://arxiv.org/pdf/2410.14169v1.pdf)  
  摘要: Numerous recent approaches to modeling and re-rendering dynamic scenes leverage plane-based explicit representations, addressing slow training times associated with models like neural radiance fields ...  
  关键词: gaussian splatting, nerf  
- **[DepthSplat: Connecting Gaussian Splatting and Depth](https://arxiv.org/abs/2410.13862v1)**  
  作者: Haofei Xu, Songyou Peng, Fangjinhua Wang, 等  
  链接: [📄 论文](https://arxiv.org/pdf/2410.13862v1.pdf)  
  摘要: Gaussian splatting and single/multi-view depth estimation are typically studied in isolation. In this paper, we present DepthSplat to connect Gaussian splatting and depth estimation and study their in...  
  关键词: gaussian splatting, 3d gaussian  
- **[Differentiable Robot Rendering](https://arxiv.org/abs/2410.13851v1)**  
  作者: Ruoshi Liu, Alper Canberk, Shuran Song, 等  
  链接: [📄 论文](https://arxiv.org/pdf/2410.13851v1.pdf)  
  摘要: Vision foundation models trained on massive amounts of visual data have shown unprecedented reasoning and planning skills in open-world settings. A key challenge in applying them to robotic tasks is t...  
- **[MEGA: Memory-Efficient 4D Gaussian Splatting for Dynamic Scenes](https://arxiv.org/abs/2410.13613v1)**  
  作者: Xinjie Zhang, Zhening Liu, Yifan Zhang, 等  
  链接: [📄 论文](https://arxiv.org/pdf/2410.13613v1.pdf)  
  摘要: 4D Gaussian Splatting (4DGS) has recently emerged as a promising technique for capturing complex dynamic 3D scenes with high fidelity. It utilizes a 4D Gaussian representation and a GPU-friendly raste...  
  关键词: gaussian splatting  
- **[DN-4DGS: Denoised Deformable Network with Temporal-Spatial Aggregation for Dynamic Scene Rendering](https://arxiv.org/abs/2410.13607v2)**  
  作者: Jiahao Lu, Jiacheng Deng, Ruijie Zhu, 等  
  链接: [📄 论文](https://arxiv.org/pdf/2410.13607v2.pdf)  
  摘要: Dynamic scenes rendering is an intriguing yet challenging problem. Although current methods based on NeRF have achieved satisfactory performance, they still can not reach real-time levels. Recently, 3...  
  关键词: gaussian splatting, 3d gaussian, nerf  
- **[L3DG: Latent 3D Gaussian Diffusion](https://arxiv.org/abs/2410.13530v1)**  
  作者: Barbara Roessle, Norman Müller, Lorenzo Porzi, 等  
  链接: [📄 论文](https://arxiv.org/pdf/2410.13530v1.pdf)  
  摘要: We propose L3DG, the first approach for generative 3D modeling of 3D Gaussians through a latent 3D Gaussian diffusion formulation. This enables effective generative 3D modeling, scaling to generation ...  
  关键词: 3d gaussian  
- **[GlossyGS: Inverse Rendering of Glossy Objects with 3D Gaussian Splatting](https://arxiv.org/abs/2410.13349v1)**  
  作者: Shuichang Lai, Letian Huang, Jie Guo, 等  
  链接: [📄 论文](https://arxiv.org/pdf/2410.13349v1.pdf)  
  摘要: Reconstructing objects from posed images is a crucial and complex task in computer graphics and computer vision. While NeRF-based neural reconstruction methods have exhibited impressive reconstruction...  
  关键词: gaussian splatting, 3d gaussian, nerf  
- **[Hybrid bundle-adjusting 3D Gaussians for view consistent rendering with pose optimization](https://arxiv.org/abs/2410.13280v1)**  
  作者: Yanan Guo, Ying Xie, Ying Chang, 等  
  链接: [📄 论文](https://arxiv.org/pdf/2410.13280v1.pdf)  
  摘要: Novel view synthesis has made significant progress in the field of 3D computer vision. However, the rendering of view-consistent novel views from imperfect camera poses remains challenging. In this pa...  
  关键词: 3d gaussian  
- **[UniG: Modelling Unitary 3D Gaussians for View-consistent 3D Reconstruction](https://arxiv.org/abs/2410.13195v2)**  
  作者: Jiamin Wu, Kenkun Liu, Yukai Shi, 等  
  链接: [📄 论文](https://arxiv.org/pdf/2410.13195v2.pdf)  
  摘要: In this work, we present UniG, a view-consistent 3D reconstruction and novel view synthesis model that generates a high-fidelity representation of 3D Gaussians from sparse images. Existing 3D Gaussian...  
  关键词: 3d gaussian, 3d reconstruction  
- **[Long-LRM: Long-sequence Large Reconstruction Model for Wide-coverage Gaussian Splats](https://arxiv.org/abs/2410.12781v1)**  
  作者: Chen Ziwen, Hao Tan, Kai Zhang, 等  
  链接: [📄 论文](https://arxiv.org/pdf/2410.12781v1.pdf)  
  摘要: We propose Long-LRM, a generalizable 3D Gaussian reconstruction model that is capable of reconstructing a large scene from a long sequence of input images. Specifically, our model can process 32 sourc...  
  关键词: 3d gaussian  
- **[3D Gaussian Splatting in Robotics: A Survey](https://arxiv.org/abs/2410.12262v1)**  
  作者: Siting Zhu, Guangming Wang, Dezhi Kong, 等  
  链接: [📄 论文](https://arxiv.org/pdf/2410.12262v1.pdf)  
  摘要: Dense 3D representations of the environment have been a long-term goal in the robotics field. While previous Neural Radiance Fields (NeRF) representation have been prevalent for its implicit, coordina...  
  关键词: gaussian splatting, 3d gaussian, real-time rendering, nerf  
- **[SplatPose+: Real-time Image-Based Pose-Agnostic 3D Anomaly Detection](https://arxiv.org/abs/2410.12080v1)**  
  作者: Yizhe Liu, Yan Song Hu, Yuhao Chen, 等  
  链接: [📄 论文](https://arxiv.org/pdf/2410.12080v1.pdf)  
  摘要: Image-based Pose-Agnostic 3D Anomaly Detection is an important task that has emerged in industrial quality control. This task seeks to find anomalies from query images of a tested object given a set o...  
  关键词: gaussian splatting, 3d gaussian  
- **[LoGS: Visual Localization via Gaussian Splatting with Fewer Training Images](https://arxiv.org/abs/2410.11505v1)**  
  作者: Yuzhou Cheng, Jianhao Jiao, Yue Wang, 等  
  链接: [📄 论文](https://arxiv.org/pdf/2410.11505v1.pdf)  
  摘要: Visual localization involves estimating a query image's 6-DoF (degrees of freedom) camera pose, which is a fundamental component in various computer vision and robotic tasks. This paper presents LoGS,...  
  关键词: gaussian splatting, 3d gaussian  
- **[GS^3: Efficient Relighting with Triple Gaussian Splatting](https://arxiv.org/abs/2410.11419v1)**  
  作者: Zoubin Bi, Yixin Zeng, Chong Zeng, 等  
  链接: [📄 论文](https://arxiv.org/pdf/2410.11419v1.pdf)  
  摘要: We present a spatial and angular Gaussian based representation and a triple splatting process, for real-time, high-quality novel lighting-and-view synthesis from multi-view point-lit input images. To ...  
- **[MCGS: Multiview Consistency Enhancement for Sparse-View 3D Gaussian Radiance Fields](https://arxiv.org/abs/2410.11394v1)**  
  作者: Yuru Xiao, Deming Zhai, Wenbo Zhao, 等  
  链接: [📄 论文](https://arxiv.org/pdf/2410.11394v1.pdf)  
  摘要: Radiance fields represented by 3D Gaussians excel at synthesizing novel views, offering both high training efficiency and fast rendering. However, with sparse input views, the lack of multi-view consi...  
  关键词: gaussian splatting, 3d gaussian  
- **[GSORB-SLAM: Gaussian Splatting SLAM benefits from ORB features and Transmittance information](https://arxiv.org/abs/2410.11356v1)**  
  作者: Wancai Zheng, Xinyi Yu, Jintao Rong, 等  
  链接: [📄 论文](https://arxiv.org/pdf/2410.11356v1.pdf)  
  摘要: The emergence of 3D Gaussian Splatting (3DGS) has recently sparked a renewed wave of dense visual SLAM research. However, current methods face challenges such as sensitivity to artifacts and noise, su...  
  关键词: gaussian splatting, 3d gaussian  
- **[Scalable Indoor Novel-View Synthesis using Drone-Captured 360 Imagery with 3D Gaussian Splatting](https://arxiv.org/abs/2410.11285v1)**  
  作者: Yuanbo Chen, Chengyu Zhang, Jason Wang, 等  
  链接: [📄 论文](https://arxiv.org/pdf/2410.11285v1.pdf)  
  摘要: Scene reconstruction and novel-view synthesis for large, complex, multi-story, indoor scenes is a challenging and time-consuming task. Prior methods have utilized drones for data capture and radiance ...  
  关键词: gaussian splatting, 3d gaussian  
- **[Few-shot Novel View Synthesis using Depth Aware 3D Gaussian Splatting](https://arxiv.org/abs/2410.11080v1)**  
  作者: Raja Kumar, Vanshika Vats  
  链接: [📄 论文](https://arxiv.org/pdf/2410.11080v1.pdf)  
  摘要: 3D Gaussian splatting has surpassed neural radiance field methods in novel view synthesis by achieving lower computational costs and real-time high-quality rendering. Although it produces a high-quali...  
  关键词: gaussian splatting, 3d gaussian  
- **[4-LEGS: 4D Language Embedded Gaussian Splatting](https://arxiv.org/abs/2410.10719v2)**  
  作者: Gal Fiebelman, Tamir Cohen, Ayellet Morgenstern, 等  
  链接: [📄 论文](https://arxiv.org/pdf/2410.10719v2.pdf)  
  摘要: The emergence of neural representations has revolutionized our means for digitally viewing a wide range of 3D scenes, enabling the synthesis of photorealistic images rendered from novel views. Recentl...  
  关键词: gaussian splatting, 3d gaussian  
- **[4DStyleGaussian: Zero-shot 4D Style Transfer with Gaussian Splatting](https://arxiv.org/abs/2410.10412v1)**  
  作者: Wanlin Liang, Hongbin Xu, Weitao Chen, 等  
  链接: [📄 论文](https://arxiv.org/pdf/2410.10412v1.pdf)  
  摘要: 3D neural style transfer has gained significant attention for its potential to provide user-friendly stylization with spatial consistency. However, existing 3D style transfer methods often fall short ...  
  关键词: gaussian splatting  
- **[Gaussian Splatting Visual MPC for Granular Media Manipulation](https://arxiv.org/abs/2410.09740v1)**  
  作者: Wei-Cheng Tseng, Ellina Zhang, Krishna Murthy Jatavallabhula, 等  
  链接: [📄 论文](https://arxiv.org/pdf/2410.09740v1.pdf)  
  摘要: Recent advancements in learned 3D representations have enabled significant progress in solving complex robotic manipulation tasks, particularly for rigid-body objects. However, manipulating granular m...  
  关键词: gaussian splatting  
- **[Enhancing Single Image to 3D Generation using Gaussian Splatting and Hybrid Diffusion Priors](https://arxiv.org/abs/2410.09467v1)**  
  作者: Hritam Basak, Hadi Tabatabaee, Shreekant Gayaka, 等  
  链接: [📄 论文](https://arxiv.org/pdf/2410.09467v1.pdf)  
  摘要: 3D object generation from a single image involves estimating the full 3D geometry and texture of unseen views from an unposed RGB image captured in the wild. Accurately reconstructing an object's comp...  
  关键词: gaussian splatting  
- **[SurgicalGS: Dynamic 3D Gaussian Splatting for Accurate Robotic-Assisted Surgical Scene Reconstruction](https://arxiv.org/abs/2410.09292v1)**  
  作者: Jialei Chen, Xin Zhang, Mobarakol Islam, 等  
  链接: [📄 论文](https://arxiv.org/pdf/2410.09292v1.pdf)  
  摘要: Accurate 3D reconstruction of dynamic surgical scenes from endoscopic video is essential for robotic-assisted surgery. While recent 3D Gaussian Splatting methods have shown promise in achieving high-q...  
  关键词: gaussian splatting, 3d gaussian, 3d reconstruction  



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