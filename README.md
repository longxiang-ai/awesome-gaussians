# Awesome Gaussian Splatting [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of latest research papers, projects and resources related to Gaussian Splatting. Content is automatically updated daily.

🗺️ **[Explore the Paper Atlas](https://longxiang-ai.github.io/awesome-gaussians/)**: an interactive paper map, monthly trends, topic network and co-author network of every tracked paper.

> Last Update: 2026-11-03 04:31:39

## 📰 Latest Updates

🗺️ **[2026-09-30] Paper Atlas on GitHub Pages**
- New [interactive site](https://longxiang-ai.github.io/awesome-gaussians/) built from all daily snapshots, rebuilt after every update

🔧 **[2026-08-08] Resilient arXiv Updates**
- Switched the crawler to the official HTTPS export API endpoint
- Added bounded retries for rate limits, server errors, and network timeouts
- Temporary arXiv outages now preserve existing data and finish scheduled runs with a warning
- Added atomic, non-empty JSON writes and fallback to the latest valid data when generating README

📚 **[2026-08-08] Community Paper Added**
- Added the HDR Gaussian Splatting paper suggested in [Issue #3](https://github.com/longxiang-ai/awesome-gaussians/issues/3)

🚀 **[2026-02] Major Feature Update — v2.0**
- **Unified CLI**: Single entry point `python main.py` with subcommands: `init`, `search`, `suggest`, `export-bib`, `readme`
- **Interactive Configuration Wizard**: Run `python main.py init` to set up keywords, domains, time range, and API keys step-by-step
- **Custom Time Range Filtering**: Support relative periods (`6m`, `1y`, `2y`) and absolute date ranges (`2024-01-01` to `2025-06-01`)
- **Smart Link Extraction**: Automatically extracts and classifies GitHub, project page, dataset, video, demo, and HuggingFace links from paper abstracts
- **BibTeX Export**: Fetch BibTeX from arXiv and export to `.bib` files with category/date filters
- **LLM Keyword Suggestion**: Paste a few paper titles or arXiv IDs, and an LLM automatically generates optimized search keywords
- **arXiv Domain Filtering**: Restrict searches to specific arXiv categories (e.g., `cs.CV`, `cs.GR`)

🔧 **[2025-06-26] Configurable Search Keywords Added**
- You can now customize search keywords by modifying `data/search_config.json`

- View detailed updates: [News.md](News.md) 📋

---

## Categories

- [3DGS Surveys](#3dgs-surveys) (5 papers) - Survey papers and benchmarks about 3D Gaussian Splatting
- [Acceleration](#acceleration) (73 papers) - Papers about speeding up rendering or training
- [Applications](#applications) (500 papers) - Papers about specific applications
- [Avatar Generation](#avatar-generation) (154 papers) - Papers about human avatar generation
- [Dynamic Scene](#dynamic-scene) (182 papers) - Papers about dynamic scene reconstruction and rendering
- [Few-shot](#few-shot) (36 papers) - Papers about few-shot or sparse view reconstruction
- [Geometry Reconstruction](#geometry-reconstruction) (200 papers) - Papers about 3D geometry reconstruction
- [Large Scene](#large-scene) (28 papers) - Papers about large-scale scene reconstruction
- [Model Compression](#model-compression) (190 papers) - Papers about model compression and optimization
- [Quality Enhancement](#quality-enhancement) (57 papers) - Papers focusing on improving rendering quality
- [Ray Tracing](#ray-tracing) (5 papers) - Papers about ray tracing and ray casting in Gaussian Splatting
- [Relighting](#relighting) (43 papers) - Papers about relighting and illumination effects in Gaussian Splatting
- [SLAM](#slam) (69 papers) - Papers about SLAM using Gaussian Splatting
- [Scene Understanding](#scene-understanding) (98 papers) - Papers about scene understanding and semantic analysis



## Table of Contents

- [Categorized Papers](#categorized-papers)
- [Classic Papers](#classic-papers)
- [Open Source Projects](#open-source-projects)
- [Applications](#applications)
- [Tutorials & Blogs](#tutorials--blogs)





## Categorized Papers

### 3DGS Surveys

- **[Gaussian Splatting for Real-Time Scene Reconstruction: Methods, Systems, and Trade-offs](https://arxiv.org/abs/2610.17513v1)**  
  Authors: Ashim Dahal, Rabab Abdelfattah, Nick Rahimi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.17513v1.pdf)  
  Keywords: sparse-view, mapping, localization, dynamic, ar, slam, compression, real-time rendering, survey, gaussian splatting, tracking, 3d gaussian  
- **[GS-Pool: Object-Level Change Detection in 3D Gaussian Splatting](https://arxiv.org/abs/2610.06688v1)**  
  Authors: Boaz Keren-Gil, James Gain, Patrick Marais  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.06688v1.pdf)  
  Keywords: ar, survey, gaussian splatting, geometry, 3d gaussian  
- **[OpenFlyScan: A Quality-Guided Aerial Reconstruction System for Consumer Drones](https://arxiv.org/abs/2609.24253v1)**  
  Authors: Zhongrui You, Zhen Li, Junli Liu, Zhigang Wang, Bin Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.24253v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://openflyscan.github.io)  
  Keywords: high-fidelity, ar, survey, gaussian splatting, face, 3d gaussian  
- **[Quality Assessment of 3D Gaussian Splatting: Distortions, Benchmarks, and Open Challenges](https://arxiv.org/abs/2609.23027v1)**  
  Authors: Shuai Liu, Binqiang Liu, Qingyu Mao, Jiacong Chen, Yongsheng Liang, Youneng Bao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.23027v1.pdf)  
  Keywords: ar, compression, survey, gaussian splatting, 3d gaussian  
- **[Gaussian Splatting Underwater: A Controlled Cross-Regime Study](https://arxiv.org/abs/2608.25483v1)**  
  Authors: Olaya Álvarez-Tuñón, Stella Graßhof  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.25483v1.pdf) | [![GitHub](https://img.shields.io/github/stars/olayasturias/uw3dgs?style=social)](https://github.com/olayasturias/uw3dgs)  
  Keywords: 3d reconstruction, illumination, ar, motion, survey, gaussian splatting, geometry  

### Acceleration

*Showing the latest 50 out of 73 papers*

- **[AbacusGS: Gaussian Splatting without Per-Splat Sorting](https://arxiv.org/abs/2611.01534v1)**  
  Authors: Jiacheng Ding, Yanliang Qi, Cong Guo, Peihua Mai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.01534v1.pdf)  
  Keywords: ar, compact, fast, gaussian splatting, 3d gaussian  
- **[L3G-World: Real-Time Infinite World Generation with Latent 3D Gaussian Memory](https://arxiv.org/abs/2610.40614v1)**  
  Authors: Jinhyeok Choi, JoungBin Lee, Jongmin Lee, Minkyeong Jeon, Jiyoung Kim, Kaeun Han, Yoonjin Yoon, Seungryong Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.40614v1.pdf)  
  Keywords: ar, compact, fast, efficient, 3d gaussian  
- **[MLLM-GS: Multimodal Large Language Model Prior-Guided Fast Novel View Synthesis in Extreme Environments](https://arxiv.org/abs/2610.39936v1)**  
  Authors: Zhiliang Wu, Xinye Zheng, Kun Li, Fei Wang, Hao Guo, Yanyan Wei, Guanghui Yue, Beier Zhu, Wei Zhou, Xun Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.39936v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://wzlwlm13.github.io/MLLM-GS)  
  Keywords: 3d reconstruction, head, lightweight, ar, fast  
- **[BudSplat: Feed-forward 3D Gaussian Splatting under a Rendering Budget](https://arxiv.org/abs/2610.38278v1)**  
  Authors: Muyu Xu, Fangneng Zhan, Yu Wei, Ling Shao, Shijian Lu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.38278v1.pdf)  
  Keywords: ar, compact, fast, gaussian splatting, face, 3d gaussian  
- **[Spatial MIMO Channel Rendering: A 3D Gaussian Splatting Approach](https://arxiv.org/abs/2610.36880v1)**  
  Authors: Juntaek Han, Geonha Kim, Chaozheng Wen, Ahmed Alkhateeb, Jun Zhang, Jeonghun Park  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.36880v1.pdf)  
  Keywords: head, ar, ray tracing, fast, gaussian splatting, 3d gaussian  
- **[CVTSplat: Multi-view Reconstruction Using an Adaptive Centroidal Voronoi Tessellation](https://arxiv.org/abs/2610.35347v1)**  
  Authors: Briac Toussaint, Diego Thomas, Jean-Sébastien Franco, Edmond Boyer, Christian Theobalt  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.35347v1.pdf)  
  Keywords: ar, efficient, face, fast  
- **[RacerGS: Residual-Autoregressive Context for 3D Gaussian Splatting Compression](https://arxiv.org/abs/2610.34263v1)**  
  Authors: Wenqing Wang, Huimin Zeng, Yun Fu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.34263v1.pdf)  
  Keywords: ar, compression, compact, fast, gaussian splatting, 3d gaussian  
- **[PixGR: Pixel-Space Generative Decoding for Fast Feed-Forward 3D Reconstruction](https://arxiv.org/abs/2610.31908v1)**  
  Authors: Ranran Huang, Wenjing Bian, Weixun Luo, Ye Mao, Krystian Mikolajczyk  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.31908v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://ranrhuang.github.io/pixgr)  
  Keywords: sparse-view, 3d reconstruction, lightweight, ar, compression, fast, efficient, 3d gaussian  
- **[GSHeadRelight: Fast Relightability for 3D Gaussian Head Synthesis](https://arxiv.org/abs/2610.30619v1)**  
  Authors: Henglei Lv, Bailin Deng, Jianzhu Guo, Xiaoqiang Liu, Pengfei Wan, Di Zhang, Lin Gao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.30619v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](http://www.geometrylearning.com/GSHeadRelight)  
  Keywords: lighting, human, head, relighting, ar, vr, fast, nerf, geometry, 3d gaussian  
- **[KoalaGS: Complexity-Aware Continuous Level of Detail for Gaussian Splatting](https://arxiv.org/abs/2610.28615v1)**  
  Authors: Radu Beche, Raoul de Charette  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.28615v1.pdf)  
  Keywords: ar, fast, gaussian splatting, 3d gaussian  

### Applications

*Showing the latest 50 out of 500 papers*

- **[VLSplat: Vision-Language Guided Object-Centric 3D Gaussian Splatting via Scene Graph](https://arxiv.org/abs/2611.01939v1)**  
  Authors: Yuntae Jeon, Younho Jeon, Sujin Jin, Sungho Jo, Seunghee Park  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.01939v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://vlsplat.github.io)  
  Keywords: ar, semantic, understanding, gaussian splatting, segmentation, 3d gaussian  
- **[Xiaomi Auto World Model 2.0: Causal World Models for Real-World Driving and Embodied Intelligence](https://arxiv.org/abs/2611.01677v1)**  
  Authors: Zhenxin Zhu, Zhijian Huang, Cheng Chi, Yuru Wang, Jianhua Wu, Jiayi Guan, Yonggang Li, Mingfei Tu, JiaKui Hu, Tao Xu, Xianqi Wang, Hao Li, Yuechuan Pu, Qizeng Jia, Ruiling Yang, Hongxiao Yu, Xuhan Sheng, Jian Mao, Ruiqiang Zhang, Yu Zhu, Guang Chen, Hangjun Ye, Bing Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.01677v1.pdf)  
  Keywords: dynamic, ar, efficient, geometry, 3d gaussian  
- **[GSExplorer: Interactive World Generation with a Persistent 3D Gaussian World State](https://arxiv.org/abs/2611.01543v1)**  
  Authors: Sicheng Yu, Liu Liu, Xinjie Wang, Xinjiang Wang, Taojun Ding, Wenhao Hu, Beizhen Zhao, Puxin Yan, Zhizhong Su, Hao Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.01543v1.pdf)  
  Keywords: ar, geometry, slam, 3d gaussian  
- **[AbacusGS: Gaussian Splatting without Per-Splat Sorting](https://arxiv.org/abs/2611.01534v1)**  
  Authors: Jiacheng Ding, Yanliang Qi, Cong Guo, Peihua Mai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.01534v1.pdf)  
  Keywords: ar, compact, fast, gaussian splatting, 3d gaussian  
- **[SHield: Watermarking 4D Gaussian Splatting via Spherical Harmonic Coefficient Perturbation](https://arxiv.org/abs/2611.01162v1)**  
  Authors: Kunal Bhosikar, Prajas Wadekar, Venkata Sai Pranav Bachina, Ankit Gangwal, Charu Sharma, Nicole Meng, Yingjie Lao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.01162v1.pdf)  
  Keywords: dynamic, 4d, ar, efficient, nerf, gaussian splatting  
- **[3D Gaussian Splatting: A New Paradigm for Wireless Environment Representation](https://arxiv.org/abs/2611.01122v1)**  
  Authors: Jinya Zhang, Jiajia Guo, Chao-Kai Wen, Shi Jin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.01122v1.pdf)  
  Keywords: ar, gaussian splatting, 3d gaussian  
- **[A Reproducible Reconstruction and Evaluation Framework for Photorealistic Lunar Analog Scene Reconstruction Toward Digital Twins](https://arxiv.org/abs/2611.00870v1)**  
  Authors: Antar Mazumder, Ryan Hartzell, Luke Boyd, Alexander Robinson, Neha Sharma, Chance Carnival, Frances Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.00870v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://rose-lab-admin.github.io/rose-lunar-dt-rec)  
  Keywords: human, ar, motion, gaussian splatting, 3d gaussian, geometry, sparse view  
- **[3D Neural Rendering for Automated Ultrasonic Laser Scans](https://arxiv.org/abs/2611.00527v1)**  
  Authors: Thomas Pierson, Matthew Mitchell, Kira Perna, Anand Iyer, Eric Flynn, Adam Wachtor  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.00527v1.pdf)  
  Keywords: head, ar, nerf, geometry, neural rendering, face  
- **[MoRE-GS: Motion-Regime Experts for Future Gaussian Splatting](https://arxiv.org/abs/2611.00375v1)**  
  Authors: Shima Salehi, Joshua Peeples  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.00375v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://advanced-vision-and-learning-lab.github.io/MoRE-GS-website)  
  Keywords: dynamic, ar, compact, efficient, nerf, gaussian splatting, motion, 3d gaussian  
- **[Scaling Trusted Autonomy: Towards Generally Capable Verifiable Robots](https://arxiv.org/abs/2611.00158v1)**  
  Authors: Benedict Quartey  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.00158v1.pdf)  
  Keywords: ar, motion, semantic, geometry, 3d gaussian  

### Avatar Generation

*Showing the latest 50 out of 154 papers*

- **[A Reproducible Reconstruction and Evaluation Framework for Photorealistic Lunar Analog Scene Reconstruction Toward Digital Twins](https://arxiv.org/abs/2611.00870v1)**  
  Authors: Antar Mazumder, Ryan Hartzell, Luke Boyd, Alexander Robinson, Neha Sharma, Chance Carnival, Frances Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.00870v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://rose-lab-admin.github.io/rose-lunar-dt-rec)  
  Keywords: human, ar, motion, gaussian splatting, 3d gaussian, geometry, sparse view  
- **[3D Neural Rendering for Automated Ultrasonic Laser Scans](https://arxiv.org/abs/2611.00527v1)**  
  Authors: Thomas Pierson, Matthew Mitchell, Kira Perna, Anand Iyer, Eric Flynn, Adam Wachtor  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.00527v1.pdf)  
  Keywords: head, ar, nerf, geometry, neural rendering, face  
- **[MLLM-GS: Multimodal Large Language Model Prior-Guided Fast Novel View Synthesis in Extreme Environments](https://arxiv.org/abs/2610.39936v1)**  
  Authors: Zhiliang Wu, Xinye Zheng, Kun Li, Fei Wang, Hao Guo, Yanyan Wei, Guanghui Yue, Beier Zhu, Wei Zhou, Xun Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.39936v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://wzlwlm13.github.io/MLLM-GS)  
  Keywords: 3d reconstruction, head, lightweight, ar, fast  
- **[COGS: A Diagnostic Benchmark for Attribute-Aware Object-Level 3D Gaussian Splatting Perception](https://arxiv.org/abs/2610.39201v1)**  
  Authors: Zheng Xiao, Yifan Liu, Weijian Deng, Jiashu Li, Ziqin Liu, Zhenjun Han, Jianbin Jiao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.39201v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://huggingface.co/datasets/XiaoZhengCV/COGS.) | [![Dataset](https://img.shields.io/badge/-Dataset-orange)](https://huggingface.co/datasets/XiaoZhengCV/COGS)  
  Keywords: ar, gaussian splatting, face, 3d gaussian  
- **[BudSplat: Feed-forward 3D Gaussian Splatting under a Rendering Budget](https://arxiv.org/abs/2610.38278v1)**  
  Authors: Muyu Xu, Fangneng Zhan, Yu Wei, Ling Shao, Shijian Lu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.38278v1.pdf)  
  Keywords: ar, compact, fast, gaussian splatting, face, 3d gaussian  
- **[GOFish: Full Field-of-View Gaussian Splatting and Mesh Extraction](https://arxiv.org/abs/2610.37818v1)**  
  Authors: Allen Tu, Meher Gitika Karumuri, Shifan Zhu, Hailing Wang, Yen-Liang Lin, David Held, Matthias Zwicker, Tom Goldstein  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.37818v1.pdf)  
  Keywords: ar, gaussian splatting, geometry, face, 3d gaussian  
- **[GraftRay: Physically Based Mesh Insertion into Gaussian Splatting Scenes via Path Tracing](https://arxiv.org/abs/2610.37036v1)**  
  Authors: Jinxin Ai, Matthias Niessner  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.37036v1.pdf)  
  Keywords: lighting, shadow, illumination, ar, gaussian splatting, 3d gaussian, reflection, face, path tracing  
- **[Spatial MIMO Channel Rendering: A 3D Gaussian Splatting Approach](https://arxiv.org/abs/2610.36880v1)**  
  Authors: Juntaek Han, Geonha Kim, Chaozheng Wen, Ahmed Alkhateeb, Jun Zhang, Jeonghun Park  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.36880v1.pdf)  
  Keywords: head, ar, ray tracing, fast, gaussian splatting, 3d gaussian  
- **[PrinGS: Privacy Preservation in Gaussian Splatting](https://arxiv.org/abs/2610.36168v2)**  
  Authors: Gaurav Behera, Abhinav Raundhal, Archisha Panda, Saumya Balina, Gargi Shroff, Ponnurangam Kumaraguru  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.36168v2.pdf)  
  Keywords: human, high-fidelity, ar, gaussian splatting, geometry, face, 3d gaussian  
- **[VidEdit3D: Flexible 3D Gaussian Editing with Video Diffusion](https://arxiv.org/abs/2610.35756v1)**  
  Authors: Yanming Yang, Chenxi Song, Tong Zhao, Juntao Xu, Wenhao Rao, Yiwen Chen, Yiwei Wang, Chi Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.35756v1.pdf)  
  Keywords: dynamic, ar, semantic, gaussian splatting, face, 3d gaussian  

### Dynamic Scene

*Showing the latest 50 out of 182 papers*

- **[Xiaomi Auto World Model 2.0: Causal World Models for Real-World Driving and Embodied Intelligence](https://arxiv.org/abs/2611.01677v1)**  
  Authors: Zhenxin Zhu, Zhijian Huang, Cheng Chi, Yuru Wang, Jianhua Wu, Jiayi Guan, Yonggang Li, Mingfei Tu, JiaKui Hu, Tao Xu, Xianqi Wang, Hao Li, Yuechuan Pu, Qizeng Jia, Ruiling Yang, Hongxiao Yu, Xuhan Sheng, Jian Mao, Ruiqiang Zhang, Yu Zhu, Guang Chen, Hangjun Ye, Bing Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.01677v1.pdf)  
  Keywords: dynamic, ar, efficient, geometry, 3d gaussian  
- **[SHield: Watermarking 4D Gaussian Splatting via Spherical Harmonic Coefficient Perturbation](https://arxiv.org/abs/2611.01162v1)**  
  Authors: Kunal Bhosikar, Prajas Wadekar, Venkata Sai Pranav Bachina, Ankit Gangwal, Charu Sharma, Nicole Meng, Yingjie Lao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.01162v1.pdf)  
  Keywords: dynamic, 4d, ar, efficient, nerf, gaussian splatting  
- **[A Reproducible Reconstruction and Evaluation Framework for Photorealistic Lunar Analog Scene Reconstruction Toward Digital Twins](https://arxiv.org/abs/2611.00870v1)**  
  Authors: Antar Mazumder, Ryan Hartzell, Luke Boyd, Alexander Robinson, Neha Sharma, Chance Carnival, Frances Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.00870v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://rose-lab-admin.github.io/rose-lunar-dt-rec)  
  Keywords: human, ar, motion, gaussian splatting, 3d gaussian, geometry, sparse view  
- **[MoRE-GS: Motion-Regime Experts for Future Gaussian Splatting](https://arxiv.org/abs/2611.00375v1)**  
  Authors: Shima Salehi, Joshua Peeples  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.00375v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://advanced-vision-and-learning-lab.github.io/MoRE-GS-website)  
  Keywords: dynamic, ar, compact, efficient, nerf, gaussian splatting, motion, 3d gaussian  
- **[Scaling Trusted Autonomy: Towards Generally Capable Verifiable Robots](https://arxiv.org/abs/2611.00158v1)**  
  Authors: Benedict Quartey  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.00158v1.pdf)  
  Keywords: ar, motion, semantic, geometry, 3d gaussian  
- **[Prior-Guided Single-Exposure HDR Novel View Synthesis via Base-Gain Representation](https://arxiv.org/abs/2610.41011v1)**  
  Authors: Armin Shafiee Sarvestani, Sheyang Tang, Jialu Xu, Zhou Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.41011v1.pdf)  
  Keywords: dynamic, gaussian splatting, ar, 3d gaussian  
- **[LucidLyra: Feed-Forward Generative 3D Scene Reconstruction and Joint Understanding via Multi-Task Distillation](https://arxiv.org/abs/2610.40495v1)**  
  Authors: Oliver Hahn, Rodrigo Marcuzzi, Sangeetha Grama Srinivasan, Alessandro Burzio, Sherwin Bahmani, Jiahui Huang, Stefan Roth, Shengyu Huang, Qunjie Zhou, Laura Leal-Taixé  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.40495v1.pdf)  
  Keywords: 3d reconstruction, dynamic, ar, semantic, understanding, robotics, geometry, segmentation, 3d gaussian  
- **[LingGS: Decoupling Feed-Forward Geometry Prediction from Camera Tracking for High-Fidelity Gaussian SLAM](https://arxiv.org/abs/2610.36853v1)**  
  Authors: Da Li, Yihan Zang, Ivan Viola, Zeyu Wang, Dominik Engel  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.36853v1.pdf)  
  Keywords: high-fidelity, ar, slam, motion, tracking, gaussian splatting, geometry, outdoor  
- **[SG^2SLAM: Spatial Geometry-Informed 3D Gaussian Splatting SLAM for Monocular Outdoor Navigation](https://arxiv.org/abs/2610.36312v1)**  
  Authors: Ziang Guo, Didar Seyidov, Yixiao Zhou, Xuefeng Zhang, Ali Alridha Abdulkarim, Chen Min, Zufeng Zhang, Dzmitry Tsetserukou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.36312v1.pdf)  
  Keywords: mapping, ar, slam, motion, tracking, gaussian splatting, geometry, outdoor, 3d gaussian  
- **[FL4N: Feed-forward Latent Model for 4D Novel View Synthesis](https://arxiv.org/abs/2610.35854v1)**  
  Authors: Eunbeen Hong, Hyeonseo Yu, Honggyu An, Jooho Son, Hyunah Ko, Soowon Son, Chaehyun Kim, Jahyeok Koo, Jisoo Kim, Junhwa Hur, Seungryong Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.35854v1.pdf)  
  Keywords: dynamic, 4d, ar, lightweight, motion  

### Few-shot

- **[A Reproducible Reconstruction and Evaluation Framework for Photorealistic Lunar Analog Scene Reconstruction Toward Digital Twins](https://arxiv.org/abs/2611.00870v1)**  
  Authors: Antar Mazumder, Ryan Hartzell, Luke Boyd, Alexander Robinson, Neha Sharma, Chance Carnival, Frances Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.00870v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://rose-lab-admin.github.io/rose-lunar-dt-rec)  
  Keywords: human, ar, motion, gaussian splatting, 3d gaussian, geometry, sparse view  
- **[P^2-Gaussian: Prior-Driven and Projection-Guided Gaussian Splatting for Sparse-View Cone-Beam CT Reconstruction](https://arxiv.org/abs/2610.39359v1)**  
  Authors: Jinqiu Xia, Jianhui Ma, Bin Ouyang, Xiaoyan Huang, Yuan Xu, Zun Piao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.39359v1.pdf) | [![GitHub](https://img.shields.io/github/stars/Ballbo5354/P-2-Gaussian?style=social)](https://github.com/Ballbo5354/P-2-Gaussian)  
  Keywords: sparse-view, ar, compact, gaussian splatting, 3d gaussian  
- **[DUET4D: Self-Corrective Coupled Guidance for Sparse-View 4D Reconstruction](https://arxiv.org/abs/2610.35002v1)**  
  Authors: Beizhen Zhao, Nanjie Yao, Boyi Fu, Qingsong Yan, Haofan Ren, Kaiyong Zhao, Hao Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.35002v1.pdf)  
  Keywords: 4d, sparse-view, gaussian splatting, ar  
- **[PixGR: Pixel-Space Generative Decoding for Fast Feed-Forward 3D Reconstruction](https://arxiv.org/abs/2610.31908v1)**  
  Authors: Ranran Huang, Wenjing Bian, Weixun Luo, Ye Mao, Krystian Mikolajczyk  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.31908v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://ranrhuang.github.io/pixgr)  
  Keywords: sparse-view, 3d reconstruction, lightweight, ar, compression, fast, efficient, 3d gaussian  
- **[Rethinking Sparse-View 3D Gaussian Splatting: A Few-Shot Learning Perspective on Overfitting Prevention](https://arxiv.org/abs/2610.25887v1)**  
  Authors: Lejia Ye, Bin Wu, Jingjing Gao, Yiyang Wu, Xiaohu Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.25887v1.pdf)  
  Keywords: sparse-view, dynamic, ar, motion, vr, gaussian splatting, few-shot, geometry, 3d gaussian  
- **[Holi-Spatial 360: Generative Reconstruction from Sparse Panoramas for Spatial Rendering and Intelligence](https://arxiv.org/abs/2610.19502v1)**  
  Authors: Yuanyuan Gao, Zhirui Liu, Yuning Gong, Yifei Liu, Yifan Zhan, Kuixuan Jiao, Xiaolong Zhou, Yifan Yang, Hongjie Zhang, Xue Yang, Dan Xu, Zhihang Zhong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.19502v1.pdf)  
  Keywords: ar, semantic, understanding, gaussian splatting, 3d gaussian, sparse view  
- **[Gaussian Splatting for Real-Time Scene Reconstruction: Methods, Systems, and Trade-offs](https://arxiv.org/abs/2610.17513v1)**  
  Authors: Ashim Dahal, Rabab Abdelfattah, Nick Rahimi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.17513v1.pdf)  
  Keywords: sparse-view, mapping, localization, dynamic, ar, slam, compression, real-time rendering, survey, gaussian splatting, tracking, 3d gaussian  
- **[AD-GS: Anatomical Density-guided 3D Gaussian Splatting for Sparse-View Dental CBCT Reconstruction](https://arxiv.org/abs/2610.14963v1)**  
  Authors: Zonglin Li, Kexian Xie, Feiran Li, Chu Zhou, Yixing Huang, Ruiyang Chen, Zhanyu Ma, Heng Guo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.14963v1.pdf) | [![GitHub](https://img.shields.io/github/stars/yulinjiaxue/AD-GS-BMVC2026?style=social)](https://github.com/yulinjiaxue/AD-GS-BMVC2026)  
  Keywords: sparse-view, ar, semantic, gaussian splatting, medical, 3d gaussian  
- **[CompactSplat: Spatially Adaptive Gaussian Distribution for Feedforward Scene Reconstruction](https://arxiv.org/abs/2610.13177v1)**  
  Authors: Bing He, Jingnan Gao, Yunuo Chen, Zhengxue Cheng, Rong Xie, Li Song, Wenjun Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.13177v1.pdf)  
  Keywords: high-fidelity, dynamic, ar, sparse view, compact, gaussian splatting, geometry, face, 3d gaussian  
- **[OX-NeRF: 3D X-ray Tomography Reconstruction from Sparse Views Using Implicit Neural Representation](https://arxiv.org/abs/2610.11547v1)**  
  Authors: Thomas Welsch, Min-Hsin Tu, David J. Chapman, Daniel E. Eakins  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.11547v1.pdf)  
  Keywords: 3d reconstruction, ar, nerf, gaussian splatting, sparse view  

### Geometry Reconstruction

*Showing the latest 50 out of 200 papers*

- **[Xiaomi Auto World Model 2.0: Causal World Models for Real-World Driving and Embodied Intelligence](https://arxiv.org/abs/2611.01677v1)**  
  Authors: Zhenxin Zhu, Zhijian Huang, Cheng Chi, Yuru Wang, Jianhua Wu, Jiayi Guan, Yonggang Li, Mingfei Tu, JiaKui Hu, Tao Xu, Xianqi Wang, Hao Li, Yuechuan Pu, Qizeng Jia, Ruiling Yang, Hongxiao Yu, Xuhan Sheng, Jian Mao, Ruiqiang Zhang, Yu Zhu, Guang Chen, Hangjun Ye, Bing Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.01677v1.pdf)  
  Keywords: dynamic, ar, efficient, geometry, 3d gaussian  
- **[GSExplorer: Interactive World Generation with a Persistent 3D Gaussian World State](https://arxiv.org/abs/2611.01543v1)**  
  Authors: Sicheng Yu, Liu Liu, Xinjie Wang, Xinjiang Wang, Taojun Ding, Wenhao Hu, Beizhen Zhao, Puxin Yan, Zhizhong Su, Hao Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.01543v1.pdf)  
  Keywords: ar, geometry, slam, 3d gaussian  
- **[A Reproducible Reconstruction and Evaluation Framework for Photorealistic Lunar Analog Scene Reconstruction Toward Digital Twins](https://arxiv.org/abs/2611.00870v1)**  
  Authors: Antar Mazumder, Ryan Hartzell, Luke Boyd, Alexander Robinson, Neha Sharma, Chance Carnival, Frances Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.00870v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://rose-lab-admin.github.io/rose-lunar-dt-rec)  
  Keywords: human, ar, motion, gaussian splatting, 3d gaussian, geometry, sparse view  
- **[3D Neural Rendering for Automated Ultrasonic Laser Scans](https://arxiv.org/abs/2611.00527v1)**  
  Authors: Thomas Pierson, Matthew Mitchell, Kira Perna, Anand Iyer, Eric Flynn, Adam Wachtor  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.00527v1.pdf)  
  Keywords: head, ar, nerf, geometry, neural rendering, face  
- **[Scaling Trusted Autonomy: Towards Generally Capable Verifiable Robots](https://arxiv.org/abs/2611.00158v1)**  
  Authors: Benedict Quartey  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.00158v1.pdf)  
  Keywords: ar, motion, semantic, geometry, 3d gaussian  
- **[LucidLyra: Feed-Forward Generative 3D Scene Reconstruction and Joint Understanding via Multi-Task Distillation](https://arxiv.org/abs/2610.40495v1)**  
  Authors: Oliver Hahn, Rodrigo Marcuzzi, Sangeetha Grama Srinivasan, Alessandro Burzio, Sherwin Bahmani, Jiahui Huang, Stefan Roth, Shengyu Huang, Qunjie Zhou, Laura Leal-Taixé  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.40495v1.pdf)  
  Keywords: 3d reconstruction, dynamic, ar, semantic, understanding, robotics, geometry, segmentation, 3d gaussian  
- **[MLLM-GS: Multimodal Large Language Model Prior-Guided Fast Novel View Synthesis in Extreme Environments](https://arxiv.org/abs/2610.39936v1)**  
  Authors: Zhiliang Wu, Xinye Zheng, Kun Li, Fei Wang, Hao Guo, Yanyan Wei, Guanghui Yue, Beier Zhu, Wei Zhou, Xun Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.39936v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://wzlwlm13.github.io/MLLM-GS)  
  Keywords: 3d reconstruction, head, lightweight, ar, fast  
- **[ACD-GS: Asymmetric Curvature-aware Densification for 3D Gaussian Splatting](https://arxiv.org/abs/2610.39399v1)**  
  Authors: Houqiang Zhong, Tianchi Zhu, Qiang Hu, Xiaoyun Zhang, Li Song, Wenjun Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.39399v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://waveviewer.github.io/ACD-GS)  
  Keywords: ar, compression, compact, gaussian splatting, geometry, 3d gaussian  
- **[Aligning Misaligned Benchmarks for Single-View Novel View Synthesis](https://arxiv.org/abs/2610.38349v1)**  
  Authors: Yang-Che Tseng, Erqun Dong, Jeong-gi Kwak, Gopal Sharma, Shakiba Kheradmand, Stephan Garbin, Hossam Isack, Kwang Moo Yi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.38349v1.pdf)  
  Keywords: ar, 3d reconstruction, geometry, 3d gaussian  
- **[GOFish: Full Field-of-View Gaussian Splatting and Mesh Extraction](https://arxiv.org/abs/2610.37818v1)**  
  Authors: Allen Tu, Meher Gitika Karumuri, Shifan Zhu, Hailing Wang, Yen-Liang Lin, David Held, Matthias Zwicker, Tom Goldstein  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.37818v1.pdf)  
  Keywords: ar, gaussian splatting, geometry, face, 3d gaussian  

### Large Scene

- **[DomeGS: Perceptually Consistent Background Completion for Unbounded 3D Gaussian Splatting in Virtual Reality](https://arxiv.org/abs/2610.37172v1)**  
  Authors: Anastasiya Pechko, Agata Szymańska, Piotr Borycki, Joanna Szelewska, Michał Mnich, Sławomir Tadeja, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.37172v1.pdf)  
  Keywords: high-fidelity, ar, vr, gaussian splatting, geometry, outdoor, 3d gaussian  
- **[LingGS: Decoupling Feed-Forward Geometry Prediction from Camera Tracking for High-Fidelity Gaussian SLAM](https://arxiv.org/abs/2610.36853v1)**  
  Authors: Da Li, Yihan Zang, Ivan Viola, Zeyu Wang, Dominik Engel  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.36853v1.pdf)  
  Keywords: high-fidelity, ar, slam, motion, tracking, gaussian splatting, geometry, outdoor  
- **[SG^2SLAM: Spatial Geometry-Informed 3D Gaussian Splatting SLAM for Monocular Outdoor Navigation](https://arxiv.org/abs/2610.36312v1)**  
  Authors: Ziang Guo, Didar Seyidov, Yixiao Zhou, Xuefeng Zhang, Ali Alridha Abdulkarim, Chen Min, Zufeng Zhang, Dzmitry Tsetserukou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.36312v1.pdf)  
  Keywords: mapping, ar, slam, motion, tracking, gaussian splatting, geometry, outdoor, 3d gaussian  
- **[BoundedGS: Memory-Efficient High-Resolution Training for 3D Gaussian Splatting](https://arxiv.org/abs/2610.34233v1)**  
  Authors: Xiaobin Deng, Changyu Diao, Min Li, Duanqing Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.34233v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://xiaobin2001.github.io/BoundedGS-Web)  
  Keywords: ar, compact, efficient, gaussian splatting, outdoor, 3d gaussian  
- **[LegoOcc++: Towards Consistent Open-Vocabulary 3D Occupancy Prediction](https://arxiv.org/abs/2610.34093v1)**  
  Authors: Changqing Zhou, Yueru Luo, Han Zhang, Zeyu Jiang, Changhao Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.34093v1.pdf) | [![GitHub](https://img.shields.io/github/stars/JuIvyy/LegoOcc?style=social)](https://github.com/JuIvyy/LegoOcc)  
  Keywords: ar, semantic, gaussian splatting, geometry, outdoor  
- **[AirPlayground: Benchmarking Aerial Navigation across Diverse Reconstructed Environments](https://arxiv.org/abs/2610.29699v1)**  
  Authors: Rangya Zhang, Yujing Shang, Zhuoyuan Yu, Mingsheng Li, Qingsong Yan, Chao Yan, Yuhang Zhang, Mir Feroskhan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.29699v1.pdf)  
  Keywords: ar, gaussian splatting, geometry, outdoor, 3d gaussian  
- **[Counting Contributions, Not Views: Occlusion-Aware Densification for 3D Gaussian Splatting](https://arxiv.org/abs/2610.27108v1)**  
  Authors: Marcel Rogge, René Schuster, Didier Stricker  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.27108v1.pdf)  
  Keywords: large scene, ar, gaussian splatting, geometry, 3d gaussian  
- **[HyperLoop: Hyperspectral-Assisted Loop Closure Detection in 3D-SLAM for Planetary Exploration](https://arxiv.org/abs/2610.19742v1)**  
  Authors: Annie Bhalla, Dennis Rotondi, Riccardo Giubilato, Kai O. Arras, Wolfgang Stuerzl  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.19742v1.pdf)  
  Keywords: illumination, mapping, ar, slam, gaussian splatting, outdoor, 3d gaussian  
- **[I2O2I-Nav: A Benchmark with a Modular Agent for Long-Horizon Indoor-to-Outdoor-to-Indoor Navigation](https://arxiv.org/abs/2610.18307v1)**  
  Authors: Zhengjie Shu, Wanyu Li, Di Xiao, Lingxin Jiang, Lai Jiang, Kaidi Hu, Xincheng Tang, Wenkang Hu, Haoran Wang, Jinchuan Zhang, Chang Chen, Wei Li, Jia Pan, Ruigang Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.18307v1.pdf)  
  Keywords: ar, geometry, outdoor  
- **[3D Gaussian Splatting for Fine-grained Urban Scene Reconstruction via Semantic-guided Density Control and Loss Design](https://arxiv.org/abs/2610.16292v1)**  
  Authors: Yueling Liao, San Jiang, Xing Zhang, Zhongwen Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.16292v1.pdf)  
  Keywords: 3d reconstruction, high-fidelity, dynamic, ar, semantic, gaussian splatting, urban scene, segmentation, 3d gaussian  

### Model Compression

*Showing the latest 50 out of 190 papers*

- **[Xiaomi Auto World Model 2.0: Causal World Models for Real-World Driving and Embodied Intelligence](https://arxiv.org/abs/2611.01677v1)**  
  Authors: Zhenxin Zhu, Zhijian Huang, Cheng Chi, Yuru Wang, Jianhua Wu, Jiayi Guan, Yonggang Li, Mingfei Tu, JiaKui Hu, Tao Xu, Xianqi Wang, Hao Li, Yuechuan Pu, Qizeng Jia, Ruiling Yang, Hongxiao Yu, Xuhan Sheng, Jian Mao, Ruiqiang Zhang, Yu Zhu, Guang Chen, Hangjun Ye, Bing Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.01677v1.pdf)  
  Keywords: dynamic, ar, efficient, geometry, 3d gaussian  
- **[AbacusGS: Gaussian Splatting without Per-Splat Sorting](https://arxiv.org/abs/2611.01534v1)**  
  Authors: Jiacheng Ding, Yanliang Qi, Cong Guo, Peihua Mai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.01534v1.pdf)  
  Keywords: ar, compact, fast, gaussian splatting, 3d gaussian  
- **[SHield: Watermarking 4D Gaussian Splatting via Spherical Harmonic Coefficient Perturbation](https://arxiv.org/abs/2611.01162v1)**  
  Authors: Kunal Bhosikar, Prajas Wadekar, Venkata Sai Pranav Bachina, Ankit Gangwal, Charu Sharma, Nicole Meng, Yingjie Lao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.01162v1.pdf)  
  Keywords: dynamic, 4d, ar, efficient, nerf, gaussian splatting  
- **[MoRE-GS: Motion-Regime Experts for Future Gaussian Splatting](https://arxiv.org/abs/2611.00375v1)**  
  Authors: Shima Salehi, Joshua Peeples  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.00375v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://advanced-vision-and-learning-lab.github.io/MoRE-GS-website)  
  Keywords: dynamic, ar, compact, efficient, nerf, gaussian splatting, motion, 3d gaussian  
- **[L3G-World: Real-Time Infinite World Generation with Latent 3D Gaussian Memory](https://arxiv.org/abs/2610.40614v1)**  
  Authors: Jinhyeok Choi, JoungBin Lee, Jongmin Lee, Minkyeong Jeon, Jiyoung Kim, Kaeun Han, Yoonjin Yoon, Seungryong Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.40614v1.pdf)  
  Keywords: ar, compact, fast, efficient, 3d gaussian  
- **[MLLM-GS: Multimodal Large Language Model Prior-Guided Fast Novel View Synthesis in Extreme Environments](https://arxiv.org/abs/2610.39936v1)**  
  Authors: Zhiliang Wu, Xinye Zheng, Kun Li, Fei Wang, Hao Guo, Yanyan Wei, Guanghui Yue, Beier Zhu, Wei Zhou, Xun Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.39936v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://wzlwlm13.github.io/MLLM-GS)  
  Keywords: 3d reconstruction, head, lightweight, ar, fast  
- **[ACD-GS: Asymmetric Curvature-aware Densification for 3D Gaussian Splatting](https://arxiv.org/abs/2610.39399v1)**  
  Authors: Houqiang Zhong, Tianchi Zhu, Qiang Hu, Xiaoyun Zhang, Li Song, Wenjun Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.39399v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://waveviewer.github.io/ACD-GS)  
  Keywords: ar, compression, compact, gaussian splatting, geometry, 3d gaussian  
- **[P^2-Gaussian: Prior-Driven and Projection-Guided Gaussian Splatting for Sparse-View Cone-Beam CT Reconstruction](https://arxiv.org/abs/2610.39359v1)**  
  Authors: Jinqiu Xia, Jianhui Ma, Bin Ouyang, Xiaoyan Huang, Yuan Xu, Zun Piao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.39359v1.pdf) | [![GitHub](https://img.shields.io/github/stars/Ballbo5354/P-2-Gaussian?style=social)](https://github.com/Ballbo5354/P-2-Gaussian)  
  Keywords: sparse-view, ar, compact, gaussian splatting, 3d gaussian  
- **[BudSplat: Feed-forward 3D Gaussian Splatting under a Rendering Budget](https://arxiv.org/abs/2610.38278v1)**  
  Authors: Muyu Xu, Fangneng Zhan, Yu Wei, Ling Shao, Shijian Lu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.38278v1.pdf)  
  Keywords: ar, compact, fast, gaussian splatting, face, 3d gaussian  
- **[GeoGSplat: Geometry-Grounded Non-Pixel-Aligned Gaussian Splatting](https://arxiv.org/abs/2610.36760v1)**  
  Authors: Jiale Wang, Chen Zhao, Haoyang Zhang, Yanhao Wu, Fei He, Yanhu Shan, Rui Wu, Wei Ke, Tong Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.36760v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://comedy0913.github.io/projects/geogsplat)  
  Keywords: 3d reconstruction, ar, efficient, gaussian splatting, geometry  

### Quality Enhancement

*Showing the latest 50 out of 57 papers*

- **[DomeGS: Perceptually Consistent Background Completion for Unbounded 3D Gaussian Splatting in Virtual Reality](https://arxiv.org/abs/2610.37172v1)**  
  Authors: Anastasiya Pechko, Agata Szymańska, Piotr Borycki, Joanna Szelewska, Michał Mnich, Sławomir Tadeja, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.37172v1.pdf)  
  Keywords: high-fidelity, ar, vr, gaussian splatting, geometry, outdoor, 3d gaussian  
- **[LingGS: Decoupling Feed-Forward Geometry Prediction from Camera Tracking for High-Fidelity Gaussian SLAM](https://arxiv.org/abs/2610.36853v1)**  
  Authors: Da Li, Yihan Zang, Ivan Viola, Zeyu Wang, Dominik Engel  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.36853v1.pdf)  
  Keywords: high-fidelity, ar, slam, motion, tracking, gaussian splatting, geometry, outdoor  
- **[PrinGS: Privacy Preservation in Gaussian Splatting](https://arxiv.org/abs/2610.36168v2)**  
  Authors: Gaurav Behera, Abhinav Raundhal, Archisha Panda, Saumya Balina, Gargi Shroff, Ponnurangam Kumaraguru  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.36168v2.pdf)  
  Keywords: human, high-fidelity, ar, gaussian splatting, geometry, face, 3d gaussian  
- **[GaussianSpline: Adaptive Bézier Splines for Highly Dynamic 4D Gaussian Splatting](https://arxiv.org/abs/2610.35224v1)**  
  Authors: Tom Yachil, Andrei Sharf  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.35224v1.pdf)  
  Keywords: high-fidelity, dynamic, 4d, ar, compact, gaussian splatting, deformation, reflection, motion  
- **[AutoPhyX: Automatic Text-Condition Physics Property Generation](https://arxiv.org/abs/2610.29517v1)**  
  Authors: Bei Huang, Yixin Chen, Hongbin Zha, Yuru Pei, Siyuan Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.29517v1.pdf)  
  Keywords: high-fidelity, dynamic, 4d, ar, semantic, nerf, gaussian splatting  
- **[GOFusion: Real-Time Gaussian-Occupancy Submap Fusion for Fisher-Informed Autonomous Robot Navigation](https://arxiv.org/abs/2610.25261v1)**  
  Authors: Boxin Bu, Simon Boche, Haoming Zhang, Jaehyung Jung, Jiaxin Wei, Hannah Schieber, Daniel Roth, Angela P. Schoellig, Stefan Leutenegger  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.25261v1.pdf) | [![GitHub](https://img.shields.io/github/stars/Bennnoo/GOFusion?style=social)](https://github.com/Bennnoo/GOFusion) | [![Project](https://img.shields.io/badge/-Project-blue)](https://youtu.be/pLQKbxQvb6I.) | [![Video](https://img.shields.io/badge/-Video-red)](https://youtu.be/pLQKbxQvb6I)  
  Keywords: high-fidelity, mapping, ar, slam, gaussian splatting, 3d gaussian  
- **[SwitchSplat: Learning Discrete Object States from Casually Captured Scenes](https://arxiv.org/abs/2610.24812v2)**  
  Authors: Yizheng Xie, Yalda Foroutan, George Shramko, Daniel Rebain, Shrisudhan Govindarajan, Andrea Tagliasacchi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.24812v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://switchsplat.github.io)  
  Keywords: 3d reconstruction, high-fidelity, dynamic, 4d, ar, fast, gaussian splatting, geometry, 3d gaussian  
- **[TriFold: Folding irregular 3D Gaussians into structured latents for 3D Scene Generation](https://arxiv.org/abs/2610.23050v2)**  
  Authors: Yun Wang, Chiyu Wang, Fan Jiang, Ziyu Zhu, Zhaoxu Sun, Guangchi Fang, Mu Xu, Dapeng Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.23050v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://fantasy-amap.github.io/TriFold)  
  Keywords: high-fidelity, ar, compact, geometry, 3d gaussian  
- **[3D Gaussian Splatting for Fine-grained Urban Scene Reconstruction via Semantic-guided Density Control and Loss Design](https://arxiv.org/abs/2610.16292v1)**  
  Authors: Yueling Liao, San Jiang, Xing Zhang, Zhongwen Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.16292v1.pdf)  
  Keywords: 3d reconstruction, high-fidelity, dynamic, ar, semantic, gaussian splatting, urban scene, segmentation, 3d gaussian  
- **[Demiurge: Forging Navigable 4D Worlds via Autoregressive Video Rerendering](https://arxiv.org/abs/2610.14685v1)**  
  Authors: Hanxin Zhu, Jianqi Ma, Cong Wang, Zhihao Hu, Junyao Gao, Tianyu He, Junyan Lin, Jiayin Xiao, Jiateng Shou, Sen Liang, Weidong Zhang, Zhibo Chen, Jun Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.14685v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://hanxinzhu-lab.github.io/demiurge_project_page)  
  Keywords: high-fidelity, dynamic, 4d, ar, motion, gaussian splatting, geometry, 3d gaussian  

### Ray Tracing

- **[GraftRay: Physically Based Mesh Insertion into Gaussian Splatting Scenes via Path Tracing](https://arxiv.org/abs/2610.37036v1)**  
  Authors: Jinxin Ai, Matthias Niessner  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.37036v1.pdf)  
  Keywords: lighting, shadow, illumination, ar, gaussian splatting, 3d gaussian, reflection, face, path tracing  
- **[Spatial MIMO Channel Rendering: A 3D Gaussian Splatting Approach](https://arxiv.org/abs/2610.36880v1)**  
  Authors: Juntaek Han, Geonha Kim, Chaozheng Wen, Ahmed Alkhateeb, Jun Zhang, Jeonghun Park  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.36880v1.pdf)  
  Keywords: head, ar, ray tracing, fast, gaussian splatting, 3d gaussian  
- **[A Hybrid and Hierarchical Ray Tracing Method for Efficient 3D Gaussian Rendering](https://arxiv.org/abs/2610.13498v1)**  
  Authors: Tiancheng Zhao, Sixu Li, Yuzhou Chen, Hengyu Ding, Zhiming Pan, Chaojian Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.13498v1.pdf)  
  Keywords: lighting, head, ar, ray tracing, efficient, gaussian splatting, 3d gaussian  
- **[Differentiable Voronoi Ray Tracing Beyond Rasterization Speeds](https://arxiv.org/abs/2608.17682v1)**  
  Authors: Bernardo Taveira, Carl Lindström, Joakim Johnander, Fredrik Kahl  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.17682v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://research.zenseact.com/publications/vorotracing)  
  Keywords: ar, ray tracing, compact, fast, real-time rendering, nerf, gaussian splatting, motion, face, 3d gaussian  
- **[3D Gaussian Accelerated Ray Tracing: Fast training through particle-based backward propagation](https://arxiv.org/abs/2608.17298v1)**  
  Authors: Laurent Vit, Oliver Batchelor, Richard Green  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.17298v1.pdf)  
  Keywords: shadow, mapping, ar, ray tracing, compact, fast, efficient, nerf, gaussian splatting, reflection, 3d gaussian  

### Relighting

- **[CTBakeGS: training-free baking of photorealistic CT volume renderings into 3D Gaussian splats](https://arxiv.org/abs/2610.37406v1)**  
  Authors: Haruki Fukuda, Constantin Lux, Wolf Schweitzer, Tadashi Hosoya, Lars Ebert  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.37406v1.pdf)  
  Keywords: lighting, ar, gaussian splatting, medical, 3d gaussian  
- **[GraftRay: Physically Based Mesh Insertion into Gaussian Splatting Scenes via Path Tracing](https://arxiv.org/abs/2610.37036v1)**  
  Authors: Jinxin Ai, Matthias Niessner  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.37036v1.pdf)  
  Keywords: lighting, shadow, illumination, ar, gaussian splatting, 3d gaussian, reflection, face, path tracing  
- **[GaussianSpline: Adaptive Bézier Splines for Highly Dynamic 4D Gaussian Splatting](https://arxiv.org/abs/2610.35224v1)**  
  Authors: Tom Yachil, Andrei Sharf  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.35224v1.pdf)  
  Keywords: high-fidelity, dynamic, 4d, ar, compact, gaussian splatting, deformation, reflection, motion  
- **[RIDE-Splat: Reflection Removal for In-the-Wild Driving Environments](https://arxiv.org/abs/2610.34632v1)**  
  Authors: Kevin David Hayes, Alex Hanson, Allen Tu, Pranav Asthana, Matthias Zwicker, Tom Goldstein  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.34632v1.pdf)  
  Keywords: 3d reconstruction, ar, gaussian splatting, reflection, geometry, 3d gaussian  
- **[GSHeadRelight: Fast Relightability for 3D Gaussian Head Synthesis](https://arxiv.org/abs/2610.30619v1)**  
  Authors: Henglei Lv, Bailin Deng, Jianzhu Guo, Xiaoqiang Liu, Pengfei Wan, Di Zhang, Lin Gao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.30619v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](http://www.geometrylearning.com/GSHeadRelight)  
  Keywords: lighting, human, head, relighting, ar, vr, fast, nerf, geometry, 3d gaussian  
- **[CoGaussian: Open-Vocabulary Gaussian-based Collaborative 3D Scene Understanding](https://arxiv.org/abs/2610.28530v1)**  
  Authors: Om Shivam Verma, Shaya Farahmand, Lingjun Zhao, Lu Gan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.28530v1.pdf)  
  Keywords: lighting, ar, compact, semantic, understanding, geometry, 3d gaussian  
- **[SplatXR: A Toolkit for Multi-Layered Extended Reality via On-Headset 3D Gaussian Splatting](https://arxiv.org/abs/2610.26338v1)**  
  Authors: Cyrus Vachha, Mohamed Kari, Parastoo Abtahi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.26338v1.pdf)  
  Keywords: head, ar, gaussian splatting, 3d gaussian, geometry, face, shadow  
- **[RxGS: Relightable Gaussian Stylization via BRDF Decomposition](https://arxiv.org/abs/2610.25681v1)**  
  Authors: Wanrong Hong, Liu Jiang, Mukesh Prasad, Jun Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.25681v1.pdf)  
  Keywords: lighting, illumination, ar, relightable, nerf, gaussian splatting, geometry, face, 3d gaussian  
- **[MCSplat: Multi-View Photometric and Geometric Consistent Feed-Forward Gaussian Splatting for Driving Scenes](https://arxiv.org/abs/2610.25345v1)**  
  Authors: Yifei Wang, Wei Tian, Wenhua Bao, Jia Zhou, Hanshi Wang, Fudong Ge, Jianhua Wu, Shuai Yuan, Zhipeng Zhang, Xingliang Liu, Xianming Zeng, Jianyun Xu, Bingzhao Gao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.25345v1.pdf)  
  Keywords: illumination, ar, gaussian splatting, geometry, face  
- **[Directionally Factorized Illumination with Spherical Harmonic Rotation](https://arxiv.org/abs/2610.24811v1)**  
  Authors: Yimeng Dou, Adam M. Saunders, Andre T. S. Hucke, Michael E. Kim, Adam W. Anderson, Eric R. Tkaczyk, Bennett A. Landman, Daniel Moyer  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.24811v1.pdf)  
  Keywords: lighting, illumination, ar, nerf, gaussian splatting, medical, geometry, neural rendering, face  

### SLAM

*Showing the latest 50 out of 69 papers*

- **[GSExplorer: Interactive World Generation with a Persistent 3D Gaussian World State](https://arxiv.org/abs/2611.01543v1)**  
  Authors: Sicheng Yu, Liu Liu, Xinjie Wang, Xinjiang Wang, Taojun Ding, Wenhao Hu, Beizhen Zhao, Puxin Yan, Zhizhong Su, Hao Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.01543v1.pdf)  
  Keywords: ar, geometry, slam, 3d gaussian  
- **[LingGS: Decoupling Feed-Forward Geometry Prediction from Camera Tracking for High-Fidelity Gaussian SLAM](https://arxiv.org/abs/2610.36853v1)**  
  Authors: Da Li, Yihan Zang, Ivan Viola, Zeyu Wang, Dominik Engel  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.36853v1.pdf)  
  Keywords: high-fidelity, ar, slam, motion, tracking, gaussian splatting, geometry, outdoor  
- **[SG^2SLAM: Spatial Geometry-Informed 3D Gaussian Splatting SLAM for Monocular Outdoor Navigation](https://arxiv.org/abs/2610.36312v1)**  
  Authors: Ziang Guo, Didar Seyidov, Yixiao Zhou, Xuefeng Zhang, Ali Alridha Abdulkarim, Chen Min, Zufeng Zhang, Dzmitry Tsetserukou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.36312v1.pdf)  
  Keywords: mapping, ar, slam, motion, tracking, gaussian splatting, geometry, outdoor, 3d gaussian  
- **[ClunoGS: Compact Language 3D Gaussian Splatting via Unified Optimization](https://arxiv.org/abs/2610.30013v1)**  
  Authors: Jian Xu, Yi Li, Ying Huang, Siyi Wu, Bingzhe Li, Yuede Ji, Miao Yin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.30013v1.pdf)  
  Keywords: localization, ar, compression, compact, semantic, understanding, gaussian splatting, segmentation, 3d gaussian  
- **[AOV-GS: Active Open-Vocabulary Semantic Mapping with 3D Gaussian Splatting](https://arxiv.org/abs/2610.29374v1)**  
  Authors: Rodion Shkokov, Tatiana Zemskova, Dmitry Yudin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.29374v1.pdf) | [![GitHub](https://img.shields.io/github/stars/OptimusFaber/AOV-GS?style=social)](https://github.com/OptimusFaber/AOV-GS)  
  Keywords: human, mapping, lightweight, ar, semantic, gaussian splatting, geometry, segmentation, 3d gaussian  
- **[GOFusion: Real-Time Gaussian-Occupancy Submap Fusion for Fisher-Informed Autonomous Robot Navigation](https://arxiv.org/abs/2610.25261v1)**  
  Authors: Boxin Bu, Simon Boche, Haoming Zhang, Jaehyung Jung, Jiaxin Wei, Hannah Schieber, Daniel Roth, Angela P. Schoellig, Stefan Leutenegger  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.25261v1.pdf) | [![GitHub](https://img.shields.io/github/stars/Bennnoo/GOFusion?style=social)](https://github.com/Bennnoo/GOFusion) | [![Project](https://img.shields.io/badge/-Project-blue)](https://youtu.be/pLQKbxQvb6I.) | [![Video](https://img.shields.io/badge/-Video-red)](https://youtu.be/pLQKbxQvb6I)  
  Keywords: high-fidelity, mapping, ar, slam, gaussian splatting, 3d gaussian  
- **[Localization and Neural Splatting on the Edge: An FPGA Scene Memory for Robots](https://arxiv.org/abs/2610.25068v2)**  
  Authors: Haohua Que, Mingkai Liu, Tianle Zhu, Handong Yao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.25068v2.pdf)  
  Keywords: localization, ar, acceleration, fast, gaussian splatting, 3d gaussian  
- **[RoMo-GS: Efficient Online 3D Gaussian Splatting for Robot Mapping via Exposure-Integrated Motion Blur](https://arxiv.org/abs/2610.24605v1)**  
  Authors: Sangwoo Jung, Di Deng, Jiahui Fu, Laura Herlant, Ayoung Kim, Yafei Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.24605v1.pdf)  
  Keywords: mapping, ar, motion, fast, efficient, robotics, gaussian splatting, geometry, 3d gaussian  
- **[KFS$^4$LAM: Adaptive KeyFrame Selection with Structure-Aware Mapping for Endoscopic Gaussian Splatting SLAM](https://arxiv.org/abs/2610.22505v1)**  
  Authors: Xinwei Ju, Zhehua Mao, Tianyi Song, Danail Stoyanov, Sophia Bano, Francisco Vasconcelos  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.22505v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://xinweiju.github.io/KFSLAM)  
  Keywords: mapping, localization, dynamic, ar, slam, gaussian splatting, deformation, motion  
- **[CF-Splat: Closed-Form Triangle Splatting with Mesh Priors](https://arxiv.org/abs/2610.22108v1)**  
  Authors: Yixin Fang, Liang Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.22108v1.pdf)  
  Keywords: ar, geometry, mapping, efficient  

### Scene Understanding

*Showing the latest 50 out of 98 papers*

- **[VLSplat: Vision-Language Guided Object-Centric 3D Gaussian Splatting via Scene Graph](https://arxiv.org/abs/2611.01939v1)**  
  Authors: Yuntae Jeon, Younho Jeon, Sujin Jin, Sungho Jo, Seunghee Park  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.01939v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://vlsplat.github.io)  
  Keywords: ar, semantic, understanding, gaussian splatting, segmentation, 3d gaussian  
- **[Scaling Trusted Autonomy: Towards Generally Capable Verifiable Robots](https://arxiv.org/abs/2611.00158v1)**  
  Authors: Benedict Quartey  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.00158v1.pdf)  
  Keywords: ar, motion, semantic, geometry, 3d gaussian  
- **[LucidLyra: Feed-Forward Generative 3D Scene Reconstruction and Joint Understanding via Multi-Task Distillation](https://arxiv.org/abs/2610.40495v1)**  
  Authors: Oliver Hahn, Rodrigo Marcuzzi, Sangeetha Grama Srinivasan, Alessandro Burzio, Sherwin Bahmani, Jiahui Huang, Stefan Roth, Shengyu Huang, Qunjie Zhou, Laura Leal-Taixé  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.40495v1.pdf)  
  Keywords: 3d reconstruction, dynamic, ar, semantic, understanding, robotics, geometry, segmentation, 3d gaussian  
- **[GCSR-OCC: Geometry Calibration and Semantic Routing for Open-Vocabulary Occupancy Prediction](https://arxiv.org/abs/2610.37149v1)**  
  Authors: Bohua Wang, Congyang Zhao, Tianxiong Lv, Chenxu Zhao, He Zheng, Hangqi Fan, Leigang Luo, Zhihao Liao, Yihong Guo, Yang Cai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.37149v1.pdf)  
  Keywords: ar, semantic, geometry, recognition, 3d gaussian  
- **[ClusterSplat: Semantic Cluster Selection for 3D Visual Grounding in Gaussian Splatting](https://arxiv.org/abs/2610.36462v1)**  
  Authors: Jaesung Lee, Hyeontaek Hwang, Gabriel Manalu, Daeyoung Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.36462v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://jaesung8.github.io/clustersplat)  
  Keywords: lightweight, ar, semantic, gaussian splatting, segmentation, 3d gaussian  
- **[VidEdit3D: Flexible 3D Gaussian Editing with Video Diffusion](https://arxiv.org/abs/2610.35756v1)**  
  Authors: Yanming Yang, Chenxi Song, Tong Zhao, Juntao Xu, Wenhao Rao, Yiwen Chen, Yiwei Wang, Chi Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.35756v1.pdf)  
  Keywords: dynamic, ar, semantic, gaussian splatting, face, 3d gaussian  
- **[SceneAgent: An Agentic Pipeline from 3D and 4D Captures to Simulation Environments](https://arxiv.org/abs/2610.34745v1)**  
  Authors: Luke Hollis, Tianxing Fan, Heng Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.34745v1.pdf)  
  Keywords: dynamic, 4d, ar, gaussian splatting, segmentation, 3d gaussian  
- **[LegoOcc++: Towards Consistent Open-Vocabulary 3D Occupancy Prediction](https://arxiv.org/abs/2610.34093v1)**  
  Authors: Changqing Zhou, Yueru Luo, Han Zhang, Zeyu Jiang, Changhao Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.34093v1.pdf) | [![GitHub](https://img.shields.io/github/stars/JuIvyy/LegoOcc?style=social)](https://github.com/JuIvyy/LegoOcc)  
  Keywords: ar, semantic, gaussian splatting, geometry, outdoor  
- **[RelateGS: Reliable Semantic and Relational Evidence for 3D Scene Understanding with Gaussian Splatting](https://arxiv.org/abs/2610.33868v1)**  
  Authors: Seongjun Choi, Sangyoun Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.33868v1.pdf)  
  Keywords: ar, semantic, understanding, gaussian splatting, 3d gaussian  
- **[RecallGS: Geometry-Grounded Recall for Online Semantic Gaussian Splatting](https://arxiv.org/abs/2610.31293v1)**  
  Authors: Thanh-Khoi Nguyen, Thien-Phuc Tran, Minh-Triet Tran  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.31293v1.pdf)  
  Keywords: head, lightweight, ar, semantic, understanding, gaussian splatting, geometry, segmentation, 3d gaussian  



## Classic Papers
- **[3D Gaussian Splatting for Real-Time Radiance Field Rendering](https://repo-sam.inria.fr/fungraph/3d-gaussian-splatting/)** (SIGGRAPH 2023)  
  Authors: Bernhard Kerbl, Georgios Kopanas, Thomas Leimkühler, George Drettakis  
  Code: 🔗 [GitHub](https://github.com/graphdeco-inria/gaussian-splatting)  
  Keywords: Real-time Rendering, Neural Rendering, Point-based Graphics

- **[A Study on the Use of High Dynamic Range Imaging for Gaussian Splatting Methods: Are 8 Bits Enough?](https://doi.org/10.2312/stag.20241341)** (STAG 2024)  
  Authors: Valentina Piras, Amedeo F. Bonatti, Carmelo De Maria, Paolo Cignoni, Francesco Banterle  
  Paper: 📄 [PDF](https://iris.cnr.it/bitstream/20.500.14243/513755/3/Piras-Cignoni-Banterle_STAG20241341.pdf)  
  Keywords: High Dynamic Range, HDR, Tone Mapping, 3D Gaussian Splatting, Neural Radiance Fields

- **[Instruct-4DGS: Efficient Dynamic Scene Editing via 4D Gaussian-based Static-Dynamic Separation](https://hanbyelcho.info/instruct-4dgs/)** (CVPR 2025)  
  Authors: Hanbyel Cho, Juhyeon Kwon, et al.  
  Paper: 📄 [arXiv](https://arxiv.org/abs/2502.02091)  
  Code: 🔗 [GitHub](https://github.com/juhyeon-kwon/efficient_4d_gaussian_editing)  
  Keywords: Dynamic Scene Editing, 4D Gaussian Splatting, Static-Dynamic Separation

## Open Source Projects
- [gaussian-splatting](https://github.com/graphdeco-inria/gaussian-splatting) - Original implementation of 3D Gaussian Splatting
- [taichi-3d-gaussian-splatting](https://github.com/wanmeihuali/taichi-3d-gaussian-splatting) - 3D Gaussian Splatting implemented in Taichi

## Applications
- [3D Gaussian Splatting for Real-Time Radiance Field Rendering Demo](https://repo-sam.inria.fr/fungraph/3d-gaussian-splatting/) - Online Demo

## Tutorials & Blogs
- [Introduction to 3D Gaussian Splatting](https://github.com/graphdeco-inria/gaussian-splatting) - Official Tutorial

## 📋 Project Features

### 🛠️ Core Features
- **Unified CLI** (`main.py`): Single entry point with `init`, `search`, `suggest`, `export-bib`, `readme` subcommands
- **Interactive Config Wizard**: Guided setup for keywords, domains, time range, and API keys via `python main.py init`
- **Custom Search Keywords**: Configure keywords for title, abstract, or both; with arXiv domain filtering (`cs.CV`, `cs.GR`, etc.)
- **Time Range Filtering**: Relative periods (`30d`, `6m`, `1y`, `2y`) or absolute date ranges (`YYYY-MM-DD` to `YYYY-MM-DD`)
- **Smart Link Extraction**: Auto-classifies URLs from abstracts into GitHub, project page, dataset, video, demo, HuggingFace links
- **BibTeX Export**: Fetch BibTeX from arXiv official API; export to `.bib` files with category and date filters
- **LLM Keyword Suggestion**: Input paper titles or arXiv IDs to auto-generate optimized search keywords via OpenAI-compatible API
- **Automated Paper Collection**: Daily automatic crawling with GitHub Actions
- **Intelligent Classification**: Auto-categorize papers into 14+ topics (Acceleration, Dynamic Scenes, SLAM, etc.)

### 🛠️ Technical Features
- **Robust Error Handling**: Multi-layer retry and fallback strategies ensure stable operation
- **GitHub Actions Integration**: Automated CI/CD workflows for daily updates
- **Multi-type Link Badges**: README entries display PDF, GitHub (with stars), Project, Dataset, Video, Demo, HuggingFace, and Citation badges
- **Detailed Logging**: Comprehensive logging for debugging and monitoring
- **Cross-Platform**: Support for Windows/Linux/macOS

### 📚 Data Output
- **Paper JSON files** (`data/papers_YYYY-MM-DD.json`): Full paper metadata with title, authors, abstract, links, keywords, BibTeX
- **BibTeX files** (`output/*.bib`): Ready-to-use bibliography files for LaTeX
- **Auto-generated README**: Categorized and formatted paper listings

## 🚀 Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Interactive Setup (Recommended)

```bash
python main.py init
```

This wizard walks you through:
- Setting search keywords (for title, abstract, or both)
- Selecting arXiv domains (e.g., `cs.CV`, `cs.GR`, `cs.AI`)
- Configuring time range (relative like `6m`/`1y`, or absolute dates)
- Setting max results
- Optionally configuring an OpenAI-compatible API key for keyword suggestion

### 3. Search Papers

```bash
# Search with settings from user_config.json
python main.py search

# Override: fetch 200 papers from the last 6 months, include BibTeX
python main.py search --max-results 200 --recent 6m --bibtex

# Search with absolute date range
python main.py search --date-from 2024-01-01 --date-to 2025-01-01

# Include citation counts from Semantic Scholar
python main.py search --citations
```

### 4. Export BibTeX

```bash
# Export all papers from the latest data file
python main.py export-bib --output output/references.bib

# Export only "Dynamic Scene" papers
python main.py export-bib --category "Dynamic Scene" --output output/dynamic.bib

# Export papers from a specific date range
python main.py export-bib --date-from 2024-06-01 --date-to 2025-01-01 --output output/recent.bib
```

### 5. LLM Keyword Suggestion

```bash
# Generate keywords from paper titles
python main.py suggest --titles "3D Gaussian Splatting for Real-Time Rendering" "Dynamic 3D Gaussians"

# Generate from arXiv IDs (auto-fetches titles)
python main.py suggest --arxiv-ids 2308.04079 2311.12897

# Auto-write suggested keywords to config
python main.py suggest --titles "NeRF" "Gaussian Splatting" --apply

# Use a custom API endpoint (e.g., DeepSeek)
python main.py suggest --titles "Paper Title" --base-url https://api.deepseek.com/v1 --api-key sk-xxx --model deepseek-chat
```

### 6. Generate README

```bash
# Basic README
python main.py readme

# Include latest papers section and abstracts
python main.py readme --show-latest --show-abstracts
```

### Configuration File

All settings are stored in `data/user_config.json`:

```json
{
  "search": {
    "keywords": {
      "both_abstract_and_title": ["gaussian splatting", "3d gaussian"],
      "abstract_only": ["neural radiance field gaussian"],
      "title_only": ["3D scene reconstruction"]
    },
    "domains": ["cs.CV", "cs.GR"],
    "time_range": {
      "mode": "relative",
      "relative": "1y"
    },
    "max_results": 500
  },
  "api_keys": {
    "openai_api_key": "",
    "openai_base_url": "https://api.openai.com/v1",
    "openai_model": "gpt-4o-mini"
  }
}
```

## Contribution Guidelines
Feel free to submit Pull Requests to improve this list! Please follow these formats:
- Paper entry format: `**[Paper Title](link)** - Brief description`
- Project entry format: `[Project Name](link) - Project description`

## License
[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/) 
