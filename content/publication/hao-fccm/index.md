---
title: "HAO: Hardware-aware Neural Architecture Optimization for Efficient Inference"
authors: [Zhen Dong, Yizhao Gao, Qijing Huang, John Wawrzynek, Hayden Kwok-Hay So, Kurt Keutzer]
date: 2021-07-02
doi: "10.1109/FCCM51124.2021.00014"
publishDate: 2021-07-02
publication_types: ["1"]
publication: "2021 IEEE 29th Annual International Symposium on Field-Programmable Custom Computing Machines (FCCM)"
publication_short: "FCCM'21"
abstract: "
Automatic algorithm-hardware co-design for DNN has shown great success in improving the performance of DNNs on FPGAs. However, this process remains challenging due to the intractable search space of neural network architectures and hardware accelerator implementation. Differing from existing hardware-aware neural architecture search (NAS) algorithms that rely solely on the expensive learning-based approaches, our work incorporates integer programming into the search algorithm to prune the design space. Given a set of hardware resource constraints, our integer programming formulation directly outputs the optimal accelerator configuration for mapping a DNN subgraph that minimizes latency. We use an accuracy predictor for different DNN subgraphs with different quantization schemes and generate accuracy-latency pareto frontiers. With low computational cost, our algorithm can generate quantized networks that achieve state-of-the-art accuracy and hardware performance on Xilinx Zynq (ZU3EG) FPGA for image classification on ImageNet dataset. The solution searched by our algorithm achieves 72.5% top-1 accuracy on ImageNet at framerate 50, which is 60% faster than MnasNet [37] and 135% faster than FBNet [43] with comparable accuracy.
"
tags: []
featured: true
url_code: 
url_poster: 
url_slides: 
projects: [aihardware]
---
