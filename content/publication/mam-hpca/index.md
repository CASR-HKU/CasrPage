---
title: "Mix and Match: A Novel FPGA-Centric Deep Neural Network Quantization Framework"
authors: [Sung-En Chang, Yanyu Li, Mengshu Sun, Runbin Shi, Hayden Kwok-Hay So, Xuehai Qian, Yanzhi Wang, Xue Lin]
date: 2021-04-21
doi: "10.1109/HPCA51647.2021.00027"
publishDate: 2021-04-21
publication_types: ["1"]
publication: "2021 IEEE International Symposium on High-Performance Computer Architecture (HPCA)"
publication_short: "HPCA'21"
abstract: "
Deep Neural Networks (DNNs) have achieved extraordinary performance in various application domains. To support diverse DNN models, efficient implementations of DNN inference on edge-computing platforms, e.g., ASICs, FPGAs, and embedded systems, are extensively investigated. Due to the huge model size and computation amount, model compression is a critical step to deploy DNN models on edge devices. This paper focuses on weight quantization, a hardware-friendly model compression approach that is complementary to weight pruning.Unlike existing methods that use the same quantization scheme for all weights, we propose the first solution that applies different quantization schemes for different rows of the weight matrix. It is motivated by (1) the distribution of the weights in the different rows are not the same; and (2) the potential of achieving better utilization of heterogeneous FPGA hardware resources. To achieve that, we first propose a hardware-friendly quantization scheme named sum-of-power-of-2 (SP2) suitable for Gaussian-like weight distribution, in which the multiplication arithmetic can be replaced with logic shifter and adder, thereby enabling highly efficient implementations with the FPGA LUT resources. In contrast, the existing fixed-point quantization is suitable for Uniform-like weight distribution and can be implemented efficiently by DSP. Then to fully explore the resources, we propose an FPGA-centric mixed scheme quantization (MSQ) with an ensemble of the proposed SP2 and the fixed-point schemes. Combining the two schemes can maintain, or even increase accuracy due to better matching with weight distributions.For the FPGA implementations, we develop a parameterized architecture with heterogeneous Generalized Matrix Multiplication (GEMM) cores-one using LUTs for computations with SP2 quantized weights and the other utilizing DSPs for fixed-point quantized weights. Given the partition ratio among the two schemes based on resource characterization, MSQ quantization training algorithm derives an optimally quantized model for the FPGA implementation. We evaluate our FPGA-centric quantization framework across multiple application domains. With optimal SP2/fixed-point ratios on two FPGA devices, i.e., Zynq XC7Z020 and XC7Z045, we achieve performance improvement of 2.1 × -4.1 × compared to solely exploiting DSPs for all multiplication operations. In addition, the CNN implementations with the proposed MSQ scheme can achieve higher accuracy and comparable hardware utilization efficiency compared to the state-of-the-art designs.
"
tags: []
featured: true
url_code: 
url_poster: 
url_slides: 
projects: [aihardware]
---