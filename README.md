# Awesome Gaussian Splatting [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of latest research papers, projects and resources related to Gaussian Splatting. Content is automatically updated daily.

> Last Update: 2025-09-29 00:51:34

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

- [Acceleration](#acceleration) (2 papers) - Papers about speeding up rendering or training
- [Applications](#applications) (10 papers) - Papers about specific applications
- [Avatar Generation](#avatar-generation) (2 papers) - Papers about human avatar generation
- [Dynamic Scene](#dynamic-scene) (4 papers) - Papers about dynamic scene reconstruction and rendering
- [Few-shot](#few-shot) (1 papers) - Papers about few-shot or sparse view reconstruction
- [Geometry Reconstruction](#geometry-reconstruction) (5 papers) - Papers about 3D geometry reconstruction
- [Large Scene](#large-scene) (1 papers) - Papers about large-scale scene reconstruction
- [Model Compression](#model-compression) (3 papers) - Papers about model compression and optimization
- [Scene Understanding](#scene-understanding) (1 papers) - Papers about scene understanding and semantic analysis



## Table of Contents

- [Categorized Papers](#categorized-papers)
- [Classic Papers](#classic-papers)
- [Open Source Projects](#open-source-projects)
- [Applications](#applications)
- [Tutorials & Blogs](#tutorials--blogs)





## Categorized Papers

### Acceleration

- **[PolGS: Polarimetric Gaussian Splatting for Fast Reflective Surface
  Reconstruction](https://arxiv.org/abs/2509.19726v1)**  
  Authors: Yufei Han, Bowen Tie, Heng Guo, Youwei Lyu, Si Li, Boxin Shi, Yunpeng Jia, Zhanyu Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.19726v1.pdf)  
  Keywords: ar, fast, efficient, face, shape reconstruction, gaussian splatting, 3d gaussian  
- **[Lyra: Generative 3D Scene Reconstruction via Video Diffusion Model
  Self-Distillation](https://arxiv.org/abs/2509.19296v1)**  
  Authors: Sherwin Bahmani, Tianchang Shen, Jiawei Ren, Jiahui Huang, Yifeng Jiang, Haithem Turki, Andrea Tagliasacchi, David B. Lindell, Zan Gojcic, Sanja Fidler, Huan Ling, Jun Gao, Xuanchi Ren  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.19296v1.pdf)  
  Keywords: dynamic, ar, real-time rendering, 3d reconstruction, robotics, autonomous driving, gaussian splatting, 3d gaussian  

### Applications

- **[Gaussian splatting holography](https://arxiv.org/abs/2509.20774v1)**  
  Authors: Shuhe Zhang, Liangcai Cao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.20774v1.pdf)  
  Keywords: face, ar, gaussian splatting, compression  
- **[4D Driving Scene Generation With Stereo Forcing](https://arxiv.org/abs/2509.20251v1)**  
  Authors: Hao Lu, Zhuang Ma, Guangfeng Jiang, Wenhang Ge, Bohan Li, Yuzhan Cai, Wenzhao Zheng, Yunpeng Zhang, Yingcong Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.20251v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://jiangxb98.github.io/PhiGensis}{PhiGensis}.)  
  Keywords: dynamic, motion, semantic, ar, 4d, geometry, gaussian splatting  
- **[GS-RoadPatching: Inpainting Gaussians via 3D Searching and Placing for
  Driving Scenes](https://arxiv.org/abs/2509.19937v1)**  
  Authors: Guo Chen, Jiarun Liu, Sicong Du, Chenming Wu, Deqi Li, Shi-Sheng Huang, Guofeng Zhang, Sheng Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.19937v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://shanzhaguoo.github.io/GS-RoadPatching/)  
  Keywords: ar, gaussian splatting, 3d gaussian  
- **[Aerial-Ground Image Feature Matching via 3D Gaussian Splatting-based
  Intermediate View Rendering](https://arxiv.org/abs/2509.19898v1)**  
  Authors: Jiangxue Yu, Hui Wang, San Jiang, Xing Zhang, Dejin Zhang, Qingquan Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.19898v1.pdf)  
  Keywords: motion, ar, large scene, gaussian splatting, 3d gaussian  
- **[BiTAA: A Bi-Task Adversarial Attack for Object Detection and Depth
  Estimation via 3D Gaussian Splatting](https://arxiv.org/abs/2509.19793v1)**  
  Authors: Yixun Zhang, Feng Zhou, Jianqin Yin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.19793v1.pdf)  
  Keywords: autonomous driving, ar, gaussian splatting, 3d gaussian  
- **[PolGS: Polarimetric Gaussian Splatting for Fast Reflective Surface
  Reconstruction](https://arxiv.org/abs/2509.19726v1)**  
  Authors: Yufei Han, Bowen Tie, Heng Guo, Youwei Lyu, Si Li, Boxin Shi, Yunpeng Jia, Zhanyu Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.19726v1.pdf)  
  Keywords: ar, fast, efficient, face, shape reconstruction, gaussian splatting, 3d gaussian  
- **[SeHDR: Single-Exposure HDR Novel View Synthesis via 3D Gaussian
  Bracketing](https://arxiv.org/abs/2509.20400v1)**  
  Authors: Yiyu Li, Haoyuan Wang, Ke Xu, Gerhard Petrus Hancke, Rynson W. H. Lau  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.20400v1.pdf)  
  Keywords: dynamic, motion, ar, geometry, gaussian splatting, 3d gaussian  
- **[VolSplat: Rethinking Feed-Forward 3D Gaussian Splatting with
  Voxel-Aligned Prediction](https://arxiv.org/abs/2509.19297v1)**  
  Authors: Weijie Wang, Yeqing Chen, Zeyu Zhang, Hengyu Liu, Haoxiao Wang, Zhiyuan Feng, Wenkang Qin, Zheng Zhu, Donny Y. Chen, Bohan Zhuang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.19297v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://lhmd.top/volsplat.)  
  Keywords: 3d reconstruction, gaussian splatting, 3d gaussian, ar  
- **[Lyra: Generative 3D Scene Reconstruction via Video Diffusion Model
  Self-Distillation](https://arxiv.org/abs/2509.19296v1)**  
  Authors: Sherwin Bahmani, Tianchang Shen, Jiawei Ren, Jiahui Huang, Yifeng Jiang, Haithem Turki, Andrea Tagliasacchi, David B. Lindell, Zan Gojcic, Sanja Fidler, Huan Ling, Jun Gao, Xuanchi Ren  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.19296v1.pdf)  
  Keywords: dynamic, ar, real-time rendering, 3d reconstruction, robotics, autonomous driving, gaussian splatting, 3d gaussian  
- **[WaveletGaussian: Wavelet-domain Diffusion for Sparse-view 3D Gaussian
  Object Reconstruction](https://arxiv.org/abs/2509.19073v1)**  
  Authors: Hung Nguyen, Runfa Li, An Le, Truong Nguyen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.19073v1.pdf)  
  Keywords: ar, lightweight, nerf, sparse-view, efficient, gaussian splatting, 3d gaussian  

### Avatar Generation

- **[Gaussian splatting holography](https://arxiv.org/abs/2509.20774v1)**  
  Authors: Shuhe Zhang, Liangcai Cao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.20774v1.pdf)  
  Keywords: face, ar, gaussian splatting, compression  
- **[PolGS: Polarimetric Gaussian Splatting for Fast Reflective Surface
  Reconstruction](https://arxiv.org/abs/2509.19726v1)**  
  Authors: Yufei Han, Bowen Tie, Heng Guo, Youwei Lyu, Si Li, Boxin Shi, Yunpeng Jia, Zhanyu Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.19726v1.pdf)  
  Keywords: ar, fast, efficient, face, shape reconstruction, gaussian splatting, 3d gaussian  

### Dynamic Scene

- **[4D Driving Scene Generation With Stereo Forcing](https://arxiv.org/abs/2509.20251v1)**  
  Authors: Hao Lu, Zhuang Ma, Guangfeng Jiang, Wenhang Ge, Bohan Li, Yuzhan Cai, Wenzhao Zheng, Yunpeng Zhang, Yingcong Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.20251v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://jiangxb98.github.io/PhiGensis}{PhiGensis}.)  
  Keywords: dynamic, motion, semantic, ar, 4d, geometry, gaussian splatting  
- **[Aerial-Ground Image Feature Matching via 3D Gaussian Splatting-based
  Intermediate View Rendering](https://arxiv.org/abs/2509.19898v1)**  
  Authors: Jiangxue Yu, Hui Wang, San Jiang, Xing Zhang, Dejin Zhang, Qingquan Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.19898v1.pdf)  
  Keywords: motion, ar, large scene, gaussian splatting, 3d gaussian  
- **[SeHDR: Single-Exposure HDR Novel View Synthesis via 3D Gaussian
  Bracketing](https://arxiv.org/abs/2509.20400v1)**  
  Authors: Yiyu Li, Haoyuan Wang, Ke Xu, Gerhard Petrus Hancke, Rynson W. H. Lau  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.20400v1.pdf)  
  Keywords: dynamic, motion, ar, geometry, gaussian splatting, 3d gaussian  
- **[Lyra: Generative 3D Scene Reconstruction via Video Diffusion Model
  Self-Distillation](https://arxiv.org/abs/2509.19296v1)**  
  Authors: Sherwin Bahmani, Tianchang Shen, Jiawei Ren, Jiahui Huang, Yifeng Jiang, Haithem Turki, Andrea Tagliasacchi, David B. Lindell, Zan Gojcic, Sanja Fidler, Huan Ling, Jun Gao, Xuanchi Ren  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.19296v1.pdf)  
  Keywords: dynamic, ar, real-time rendering, 3d reconstruction, robotics, autonomous driving, gaussian splatting, 3d gaussian  

### Few-shot

- **[WaveletGaussian: Wavelet-domain Diffusion for Sparse-view 3D Gaussian
  Object Reconstruction](https://arxiv.org/abs/2509.19073v1)**  
  Authors: Hung Nguyen, Runfa Li, An Le, Truong Nguyen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.19073v1.pdf)  
  Keywords: ar, lightweight, nerf, sparse-view, efficient, gaussian splatting, 3d gaussian  

### Geometry Reconstruction

- **[4D Driving Scene Generation With Stereo Forcing](https://arxiv.org/abs/2509.20251v1)**  
  Authors: Hao Lu, Zhuang Ma, Guangfeng Jiang, Wenhang Ge, Bohan Li, Yuzhan Cai, Wenzhao Zheng, Yunpeng Zhang, Yingcong Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.20251v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://jiangxb98.github.io/PhiGensis}{PhiGensis}.)  
  Keywords: dynamic, motion, semantic, ar, 4d, geometry, gaussian splatting  
- **[PolGS: Polarimetric Gaussian Splatting for Fast Reflective Surface
  Reconstruction](https://arxiv.org/abs/2509.19726v1)**  
  Authors: Yufei Han, Bowen Tie, Heng Guo, Youwei Lyu, Si Li, Boxin Shi, Yunpeng Jia, Zhanyu Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.19726v1.pdf)  
  Keywords: ar, fast, efficient, face, shape reconstruction, gaussian splatting, 3d gaussian  
- **[SeHDR: Single-Exposure HDR Novel View Synthesis via 3D Gaussian
  Bracketing](https://arxiv.org/abs/2509.20400v1)**  
  Authors: Yiyu Li, Haoyuan Wang, Ke Xu, Gerhard Petrus Hancke, Rynson W. H. Lau  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.20400v1.pdf)  
  Keywords: dynamic, motion, ar, geometry, gaussian splatting, 3d gaussian  
- **[VolSplat: Rethinking Feed-Forward 3D Gaussian Splatting with
  Voxel-Aligned Prediction](https://arxiv.org/abs/2509.19297v1)**  
  Authors: Weijie Wang, Yeqing Chen, Zeyu Zhang, Hengyu Liu, Haoxiao Wang, Zhiyuan Feng, Wenkang Qin, Zheng Zhu, Donny Y. Chen, Bohan Zhuang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.19297v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://lhmd.top/volsplat.)  
  Keywords: 3d reconstruction, gaussian splatting, 3d gaussian, ar  
- **[Lyra: Generative 3D Scene Reconstruction via Video Diffusion Model
  Self-Distillation](https://arxiv.org/abs/2509.19296v1)**  
  Authors: Sherwin Bahmani, Tianchang Shen, Jiawei Ren, Jiahui Huang, Yifeng Jiang, Haithem Turki, Andrea Tagliasacchi, David B. Lindell, Zan Gojcic, Sanja Fidler, Huan Ling, Jun Gao, Xuanchi Ren  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.19296v1.pdf)  
  Keywords: dynamic, ar, real-time rendering, 3d reconstruction, robotics, autonomous driving, gaussian splatting, 3d gaussian  

### Large Scene

- **[Aerial-Ground Image Feature Matching via 3D Gaussian Splatting-based
  Intermediate View Rendering](https://arxiv.org/abs/2509.19898v1)**  
  Authors: Jiangxue Yu, Hui Wang, San Jiang, Xing Zhang, Dejin Zhang, Qingquan Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.19898v1.pdf)  
  Keywords: motion, ar, large scene, gaussian splatting, 3d gaussian  

### Model Compression

- **[Gaussian splatting holography](https://arxiv.org/abs/2509.20774v1)**  
  Authors: Shuhe Zhang, Liangcai Cao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.20774v1.pdf)  
  Keywords: face, ar, gaussian splatting, compression  
- **[PolGS: Polarimetric Gaussian Splatting for Fast Reflective Surface
  Reconstruction](https://arxiv.org/abs/2509.19726v1)**  
  Authors: Yufei Han, Bowen Tie, Heng Guo, Youwei Lyu, Si Li, Boxin Shi, Yunpeng Jia, Zhanyu Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.19726v1.pdf)  
  Keywords: ar, fast, efficient, face, shape reconstruction, gaussian splatting, 3d gaussian  
- **[WaveletGaussian: Wavelet-domain Diffusion for Sparse-view 3D Gaussian
  Object Reconstruction](https://arxiv.org/abs/2509.19073v1)**  
  Authors: Hung Nguyen, Runfa Li, An Le, Truong Nguyen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.19073v1.pdf)  
  Keywords: ar, lightweight, nerf, sparse-view, efficient, gaussian splatting, 3d gaussian  

### Scene Understanding

- **[4D Driving Scene Generation With Stereo Forcing](https://arxiv.org/abs/2509.20251v1)**  
  Authors: Hao Lu, Zhuang Ma, Guangfeng Jiang, Wenhang Ge, Bohan Li, Yuzhan Cai, Wenzhao Zheng, Yunpeng Zhang, Yingcong Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2509.20251v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://jiangxb98.github.io/PhiGensis}{PhiGensis}.)  
  Keywords: dynamic, motion, semantic, ar, 4d, geometry, gaussian splatting  



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