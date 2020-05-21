---
title: "E-LSTM: Efficient inference of sparse LSTM on embedded heterogeneous system"
authors: [Runbin Shi, Junjie Liu, Hayden Kwok-Hay So, Shuo Wang, Yun Liang]
date: 2019-06-08
doi: "10.1145/3316781.3317813"
publishDate: 2019-06-08
publication_types: ["1"]
publication: "Proceedings of the 56th Annual Design Automation Conference 2019"
publication_short: "DAC'19"
abstract: "
Various models with Long Short-Term Memory (LSTM) network have demonstrated prior art performances in sequential information processing. Previous LSTM-specific architectures set large on-chip memory for weight storage to alleviate the memory-bound issue and facilitate the LSTM inference in cloud computing. In this paper, E-LSTM is proposed for embedded scenarios with the consideration of the chip-area and limited data-access bandwidth. The heterogeneous hardware in E-LSTM tightly couples an LSTM co-processor with an embedded RISC-V CPU. The eSELL format is developed to represent the sparse weight matrix. With the proposed cell fusion optimization based on the inherent sparsity in computation, E-LSTM achieves up to 2.2× speedup of processing throughput.
"
tags: []
featured: true
url_code: https://github.com/rbshi/elstm
url_poster: elstm-poster-dac19.pdf
url_slides: elstm-slides-dac19.pdf
projects: []
---
