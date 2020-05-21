---
title: "CSB-RNN: A faster-than-realtime RNN acceleration framework with compressed structured blocks"
authors: [Runbin Shi, Peiyan Dong, Tong Geng, Yuhao Ding, Xiaolong Ma, Hayden Kwok-Hay So, Martin Herbordt, Ang Li, Yanzhi Wang]
date: 2020-06-29
doi: "10.1145/3392717.3392749"
publishDate: 2020-03-29
publication_types: ["1"]
publication: "2020 International Conference on Supercomputing"
publication_short: "ICS'20 (to appear)"
abstract: "
Recurrent neural networks (RNNs) have been widely adopted in temporal sequence analysis, where realtime performance is often in demand. However, RNNs suffer from heavy computational workload as the model often comes with large weight matrices. Pruning (a model compression method) schemes have been proposed for RNNs to eliminate the redundant (close-to-zero) weight values. On one hand, the non-structured pruning methods achieve a high pruning rate but introducing computation irregularity (random sparsity), which is unfriendly to parallel hardware. On the other hand, hardware-oriented structured pruning suffers from low pruning rate due to restricted constraints on allowable pruning structure.


This paper presents CSB-RNN, an optimized full-stack RNN framework with a novel compressed structured block (CSB) pruning technique. The CSB pruned RNN model comes with both fine pruning granularity that facilitates a high pruning rate and regular structure that benefits the hardware parallelism. To address the challenges in parallelizing the CSB pruned model inference with fine-grained structural sparsity, we propose a novel hardware architecture with a dedicated compiler. Gaining from the architecturecompilation co-design, the hardware not only supports various RNN cell types, but is also able to address the challenging workload imbalance issue and therefore significantly improves the hardware efficiency (utilization). Compared to the vanilla design without optimizations, the hardware utilization has been enhanced by over 2×. With experiments on 10 RNN models from multiple application domains, CSB pruning demonstrates 3.5×-25× lossless pruning rate, which is 1.6× to 3.9× over existing designs. With several other innovations applied, the CSB-RNN inference can achieve fasterthan-realtime latency of 0.79µs-6.58µs in an FPGA implementation, which contributes to 1.12×-12.57× lower latency and 3.53×-58.89× improvement on power-efficiency over the state-of-the-art.


"
tags: [machine learning acceleration, sparsity, FPGA, architecture-compilation co-design]
featured: true
url_code: 
url_poster: 
url_slides: 
projects: []
---
