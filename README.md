# Awesome Gaussian Splatting [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of latest research papers, projects and resources related to Gaussian Splatting. Content is automatically updated daily.

> Last Update: 2025-11-03 00:55:48

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

- [3DGS Surveys](#3dgs-surveys) (1 papers) - Survey papers and benchmarks about 3D Gaussian Splatting
- [Applications](#applications) (10 papers) - Papers about specific applications
- [Avatar Generation](#avatar-generation) (3 papers) - Papers about human avatar generation
- [Dynamic Scene](#dynamic-scene) (5 papers) - Papers about dynamic scene reconstruction and rendering
- [Geometry Reconstruction](#geometry-reconstruction) (4 papers) - Papers about 3D geometry reconstruction
- [Large Scene](#large-scene) (3 papers) - Papers about large-scale scene reconstruction
- [Model Compression](#model-compression) (3 papers) - Papers about model compression and optimization
- [Quality Enhancement](#quality-enhancement) (2 papers) - Papers focusing on improving rendering quality
- [SLAM](#slam) (3 papers) - Papers about SLAM using Gaussian Splatting
- [Scene Understanding](#scene-understanding) (4 papers) - Papers about scene understanding and semantic analysis



## Table of Contents

- [Categorized Papers](#categorized-papers)
- [Classic Papers](#classic-papers)
- [Open Source Projects](#open-source-projects)
- [Applications](#applications)
- [Tutorials & Blogs](#tutorials--blogs)





## Categorized Papers

### 3DGS Surveys

- **[A Survey on Collaborative SLAM with 3D Gaussian Splatting](https://arxiv.org/abs/2510.23988v1)**  
  Authors: Phuc Nguyen Xuan, Thanh Nguyen Canh, Huu-Hung Nguyen, Nak Young Chong, Xiem HoangVan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.23988v1.pdf)  
  Keywords: localization, ar, mapping, slam, 3d gaussian, gaussian splatting, semantic, survey, efficient, high-fidelity, robotics  

### Applications

- **[HEIR: Learning Graph-Based Motion Hierarchies](https://arxiv.org/abs/2510.26786v1)**  
  Authors: Cheng Zheng, William Koch, Baiang Li, Felix Heide  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.26786v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://light.princeton.edu/HEIR/)  
  Keywords: ar, 3d gaussian, motion, gaussian splatting, dynamic, deformation, robotics  
- **[The Impact and Outlook of 3D Gaussian Splatting](https://arxiv.org/abs/2510.26694v1)**  
  Authors: Bernhard Kerbl  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.26694v1.pdf)  
  Keywords: ar, 3d gaussian, gaussian splatting, 4d, dynamic, body, efficient  
- **[AgriGS-SLAM: Orchard Mapping Across Seasons via Multi-View Gaussian
  Splatting SLAM](https://arxiv.org/abs/2510.26358v1)**  
  Authors: Mirko Usuelli, David Rapado-Rincon, Gert Kootstra, Matteo Matteucci  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.26358v1.pdf)  
  Keywords: understanding, ar, geometry, slam, 3d gaussian, motion, gaussian splatting, outdoor, mapping  
- **[6D Channel Knowledge Map Construction via Bidirectional Wireless
  Gaussian Splatting](https://arxiv.org/abs/2510.26166v1)**  
  Authors: Juncong Zhou, Chao Hu, Guanlin Wu, Zixiang Ren, Han Hu, Juyong Zhang, Rui Zhang, Jie Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.26166v1.pdf)  
  Keywords: dynamic, gaussian splatting, ar  
- **[$D^2GS$: Dense Depth Regularization for LiDAR-free Urban Scene
  Reconstruction](https://arxiv.org/abs/2510.25173v1)**  
  Authors: Kejing Xia, Jidong Jia, Ke Jin, Yucai Bai, Li Sun, Dacheng Tao, Youjian Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.25173v1.pdf)  
  Keywords: ar, geometry, autonomous driving, urban scene, gaussian splatting  
- **[AtlasGS: Atlanta-world Guided Surface Reconstruction with Implicit
  Structured Gaussians](https://arxiv.org/abs/2510.25129v1)**  
  Authors: Xiyu Zhang, Chong Bao, Yipeng Chen, Hongjia Zhai, Yitong Dong, Hujun Bao, Zhaopeng Cui, Guofeng Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.25129v1.pdf)  
  Keywords: ar, face, 3d reconstruction, urban scene, gaussian splatting, semantic  
- **[NVSim: Novel View Synthesis Simulator for Large Scale Indoor Navigation](https://arxiv.org/abs/2510.24335v1)**  
  Authors: Mingyu Jeong, Eunsung Kim, Sehun Park, Andrew Jaeyong Choi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.24335v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://youtu.be/tTiIQt6nXC8)  
  Keywords: 3d gaussian, gaussian splatting, ar  
- **[LagMemo: Language 3D Gaussian Splatting Memory for Multi-modal
  Open-vocabulary Multi-goal Visual Navigation](https://arxiv.org/abs/2510.24118v1)**  
  Authors: Haotian Zhou, Xiaole Wang, He Li, Fusheng Sun, Shengyu Guo, Guolei Qi, Jianghuan Xu, Huijing Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.24118v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://weekgoodday.github.io/lagmemo)  
  Keywords: ar, 3d gaussian, gaussian splatting, dynamic, localization  
- **[A Survey on Collaborative SLAM with 3D Gaussian Splatting](https://arxiv.org/abs/2510.23988v1)**  
  Authors: Phuc Nguyen Xuan, Thanh Nguyen Canh, Huu-Hung Nguyen, Nak Young Chong, Xiem HoangVan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.23988v1.pdf)  
  Keywords: localization, ar, mapping, slam, 3d gaussian, gaussian splatting, semantic, survey, efficient, high-fidelity, robotics  
- **[PlanarGS: High-Fidelity Indoor 3D Gaussian Splatting Guided by
  Vision-Language Planar Priors](https://arxiv.org/abs/2510.23930v1)**  
  Authors: Xirui Jin, Renbiao Jin, Boying Li, Danping Zou, Wenxian Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.23930v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://planargs.github.io)  
  Keywords: ar, face, geometry, 3d gaussian, gaussian splatting, segmentation, efficient, high-fidelity  

### Avatar Generation

- **[The Impact and Outlook of 3D Gaussian Splatting](https://arxiv.org/abs/2510.26694v1)**  
  Authors: Bernhard Kerbl  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.26694v1.pdf)  
  Keywords: ar, 3d gaussian, gaussian splatting, 4d, dynamic, body, efficient  
- **[AtlasGS: Atlanta-world Guided Surface Reconstruction with Implicit
  Structured Gaussians](https://arxiv.org/abs/2510.25129v1)**  
  Authors: Xiyu Zhang, Chong Bao, Yipeng Chen, Hongjia Zhai, Yitong Dong, Hujun Bao, Zhaopeng Cui, Guofeng Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.25129v1.pdf)  
  Keywords: ar, face, 3d reconstruction, urban scene, gaussian splatting, semantic  
- **[PlanarGS: High-Fidelity Indoor 3D Gaussian Splatting Guided by
  Vision-Language Planar Priors](https://arxiv.org/abs/2510.23930v1)**  
  Authors: Xirui Jin, Renbiao Jin, Boying Li, Danping Zou, Wenxian Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.23930v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://planargs.github.io)  
  Keywords: ar, face, geometry, 3d gaussian, gaussian splatting, segmentation, efficient, high-fidelity  

### Dynamic Scene

- **[HEIR: Learning Graph-Based Motion Hierarchies](https://arxiv.org/abs/2510.26786v1)**  
  Authors: Cheng Zheng, William Koch, Baiang Li, Felix Heide  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.26786v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://light.princeton.edu/HEIR/)  
  Keywords: ar, 3d gaussian, motion, gaussian splatting, dynamic, deformation, robotics  
- **[The Impact and Outlook of 3D Gaussian Splatting](https://arxiv.org/abs/2510.26694v1)**  
  Authors: Bernhard Kerbl  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.26694v1.pdf)  
  Keywords: ar, 3d gaussian, gaussian splatting, 4d, dynamic, body, efficient  
- **[AgriGS-SLAM: Orchard Mapping Across Seasons via Multi-View Gaussian
  Splatting SLAM](https://arxiv.org/abs/2510.26358v1)**  
  Authors: Mirko Usuelli, David Rapado-Rincon, Gert Kootstra, Matteo Matteucci  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.26358v1.pdf)  
  Keywords: understanding, ar, geometry, slam, 3d gaussian, motion, gaussian splatting, outdoor, mapping  
- **[6D Channel Knowledge Map Construction via Bidirectional Wireless
  Gaussian Splatting](https://arxiv.org/abs/2510.26166v1)**  
  Authors: Juncong Zhou, Chao Hu, Guanlin Wu, Zixiang Ren, Han Hu, Juyong Zhang, Rui Zhang, Jie Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.26166v1.pdf)  
  Keywords: dynamic, gaussian splatting, ar  
- **[LagMemo: Language 3D Gaussian Splatting Memory for Multi-modal
  Open-vocabulary Multi-goal Visual Navigation](https://arxiv.org/abs/2510.24118v1)**  
  Authors: Haotian Zhou, Xiaole Wang, He Li, Fusheng Sun, Shengyu Guo, Guolei Qi, Jianghuan Xu, Huijing Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.24118v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://weekgoodday.github.io/lagmemo)  
  Keywords: ar, 3d gaussian, gaussian splatting, dynamic, localization  

### Geometry Reconstruction

- **[AgriGS-SLAM: Orchard Mapping Across Seasons via Multi-View Gaussian
  Splatting SLAM](https://arxiv.org/abs/2510.26358v1)**  
  Authors: Mirko Usuelli, David Rapado-Rincon, Gert Kootstra, Matteo Matteucci  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.26358v1.pdf)  
  Keywords: understanding, ar, geometry, slam, 3d gaussian, motion, gaussian splatting, outdoor, mapping  
- **[$D^2GS$: Dense Depth Regularization for LiDAR-free Urban Scene
  Reconstruction](https://arxiv.org/abs/2510.25173v1)**  
  Authors: Kejing Xia, Jidong Jia, Ke Jin, Yucai Bai, Li Sun, Dacheng Tao, Youjian Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.25173v1.pdf)  
  Keywords: ar, geometry, autonomous driving, urban scene, gaussian splatting  
- **[AtlasGS: Atlanta-world Guided Surface Reconstruction with Implicit
  Structured Gaussians](https://arxiv.org/abs/2510.25129v1)**  
  Authors: Xiyu Zhang, Chong Bao, Yipeng Chen, Hongjia Zhai, Yitong Dong, Hujun Bao, Zhaopeng Cui, Guofeng Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.25129v1.pdf)  
  Keywords: ar, face, 3d reconstruction, urban scene, gaussian splatting, semantic  
- **[PlanarGS: High-Fidelity Indoor 3D Gaussian Splatting Guided by
  Vision-Language Planar Priors](https://arxiv.org/abs/2510.23930v1)**  
  Authors: Xirui Jin, Renbiao Jin, Boying Li, Danping Zou, Wenxian Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.23930v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://planargs.github.io)  
  Keywords: ar, face, geometry, 3d gaussian, gaussian splatting, segmentation, efficient, high-fidelity  

### Large Scene

- **[AgriGS-SLAM: Orchard Mapping Across Seasons via Multi-View Gaussian
  Splatting SLAM](https://arxiv.org/abs/2510.26358v1)**  
  Authors: Mirko Usuelli, David Rapado-Rincon, Gert Kootstra, Matteo Matteucci  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.26358v1.pdf)  
  Keywords: understanding, ar, geometry, slam, 3d gaussian, motion, gaussian splatting, outdoor, mapping  
- **[$D^2GS$: Dense Depth Regularization for LiDAR-free Urban Scene
  Reconstruction](https://arxiv.org/abs/2510.25173v1)**  
  Authors: Kejing Xia, Jidong Jia, Ke Jin, Yucai Bai, Li Sun, Dacheng Tao, Youjian Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.25173v1.pdf)  
  Keywords: ar, geometry, autonomous driving, urban scene, gaussian splatting  
- **[AtlasGS: Atlanta-world Guided Surface Reconstruction with Implicit
  Structured Gaussians](https://arxiv.org/abs/2510.25129v1)**  
  Authors: Xiyu Zhang, Chong Bao, Yipeng Chen, Hongjia Zhai, Yitong Dong, Hujun Bao, Zhaopeng Cui, Guofeng Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.25129v1.pdf)  
  Keywords: ar, face, 3d reconstruction, urban scene, gaussian splatting, semantic  

### Model Compression

- **[The Impact and Outlook of 3D Gaussian Splatting](https://arxiv.org/abs/2510.26694v1)**  
  Authors: Bernhard Kerbl  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.26694v1.pdf)  
  Keywords: ar, 3d gaussian, gaussian splatting, 4d, dynamic, body, efficient  
- **[A Survey on Collaborative SLAM with 3D Gaussian Splatting](https://arxiv.org/abs/2510.23988v1)**  
  Authors: Phuc Nguyen Xuan, Thanh Nguyen Canh, Huu-Hung Nguyen, Nak Young Chong, Xiem HoangVan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.23988v1.pdf)  
  Keywords: localization, ar, mapping, slam, 3d gaussian, gaussian splatting, semantic, survey, efficient, high-fidelity, robotics  
- **[PlanarGS: High-Fidelity Indoor 3D Gaussian Splatting Guided by
  Vision-Language Planar Priors](https://arxiv.org/abs/2510.23930v1)**  
  Authors: Xirui Jin, Renbiao Jin, Boying Li, Danping Zou, Wenxian Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.23930v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://planargs.github.io)  
  Keywords: ar, face, geometry, 3d gaussian, gaussian splatting, segmentation, efficient, high-fidelity  

### Quality Enhancement

- **[A Survey on Collaborative SLAM with 3D Gaussian Splatting](https://arxiv.org/abs/2510.23988v1)**  
  Authors: Phuc Nguyen Xuan, Thanh Nguyen Canh, Huu-Hung Nguyen, Nak Young Chong, Xiem HoangVan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.23988v1.pdf)  
  Keywords: localization, ar, mapping, slam, 3d gaussian, gaussian splatting, semantic, survey, efficient, high-fidelity, robotics  
- **[PlanarGS: High-Fidelity Indoor 3D Gaussian Splatting Guided by
  Vision-Language Planar Priors](https://arxiv.org/abs/2510.23930v1)**  
  Authors: Xirui Jin, Renbiao Jin, Boying Li, Danping Zou, Wenxian Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.23930v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://planargs.github.io)  
  Keywords: ar, face, geometry, 3d gaussian, gaussian splatting, segmentation, efficient, high-fidelity  

### SLAM

- **[AgriGS-SLAM: Orchard Mapping Across Seasons via Multi-View Gaussian
  Splatting SLAM](https://arxiv.org/abs/2510.26358v1)**  
  Authors: Mirko Usuelli, David Rapado-Rincon, Gert Kootstra, Matteo Matteucci  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.26358v1.pdf)  
  Keywords: understanding, ar, geometry, slam, 3d gaussian, motion, gaussian splatting, outdoor, mapping  
- **[LagMemo: Language 3D Gaussian Splatting Memory for Multi-modal
  Open-vocabulary Multi-goal Visual Navigation](https://arxiv.org/abs/2510.24118v1)**  
  Authors: Haotian Zhou, Xiaole Wang, He Li, Fusheng Sun, Shengyu Guo, Guolei Qi, Jianghuan Xu, Huijing Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.24118v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://weekgoodday.github.io/lagmemo)  
  Keywords: ar, 3d gaussian, gaussian splatting, dynamic, localization  
- **[A Survey on Collaborative SLAM with 3D Gaussian Splatting](https://arxiv.org/abs/2510.23988v1)**  
  Authors: Phuc Nguyen Xuan, Thanh Nguyen Canh, Huu-Hung Nguyen, Nak Young Chong, Xiem HoangVan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.23988v1.pdf)  
  Keywords: localization, ar, mapping, slam, 3d gaussian, gaussian splatting, semantic, survey, efficient, high-fidelity, robotics  

### Scene Understanding

- **[AgriGS-SLAM: Orchard Mapping Across Seasons via Multi-View Gaussian
  Splatting SLAM](https://arxiv.org/abs/2510.26358v1)**  
  Authors: Mirko Usuelli, David Rapado-Rincon, Gert Kootstra, Matteo Matteucci  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.26358v1.pdf)  
  Keywords: understanding, ar, geometry, slam, 3d gaussian, motion, gaussian splatting, outdoor, mapping  
- **[AtlasGS: Atlanta-world Guided Surface Reconstruction with Implicit
  Structured Gaussians](https://arxiv.org/abs/2510.25129v1)**  
  Authors: Xiyu Zhang, Chong Bao, Yipeng Chen, Hongjia Zhai, Yitong Dong, Hujun Bao, Zhaopeng Cui, Guofeng Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.25129v1.pdf)  
  Keywords: ar, face, 3d reconstruction, urban scene, gaussian splatting, semantic  
- **[A Survey on Collaborative SLAM with 3D Gaussian Splatting](https://arxiv.org/abs/2510.23988v1)**  
  Authors: Phuc Nguyen Xuan, Thanh Nguyen Canh, Huu-Hung Nguyen, Nak Young Chong, Xiem HoangVan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.23988v1.pdf)  
  Keywords: localization, ar, mapping, slam, 3d gaussian, gaussian splatting, semantic, survey, efficient, high-fidelity, robotics  
- **[PlanarGS: High-Fidelity Indoor 3D Gaussian Splatting Guided by
  Vision-Language Planar Priors](https://arxiv.org/abs/2510.23930v1)**  
  Authors: Xirui Jin, Renbiao Jin, Boying Li, Danping Zou, Wenxian Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2510.23930v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://planargs.github.io)  
  Keywords: ar, face, geometry, 3d gaussian, gaussian splatting, segmentation, efficient, high-fidelity  



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