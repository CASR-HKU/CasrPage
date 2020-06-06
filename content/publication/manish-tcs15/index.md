---
title: "Configurable Architectures for Multi-Mode Floating Point Adders"
authors: [Manish Kumar Jaiswal, B. Sharat Chandra Varma, Hayden Kwok-Hay So]
date: 2015-08-01
doi: "10.1109/TCSI.2015.2452351"
publishDate: 2015-08-01
publication_types: ["2"]
publication: "IEEE Transactions on Circuits and Systems I: Regular Papers"
publication_short: "TCSI'15"
abstract: "
This paper presents two architectures for floating point (FP) adders, which operates in multi-mode configuration with multi-precision support. First architecture (named QPdDP) works in dual-mode which can operates either for quadruple precision or two-parallel double precision. The second architecture (named QPdDPqSP) works in tri-mode which is able to compute either of a quadruple precision, two-parallel double precision and four-parallel single precision computations. The architectures are based on the standard state-of-the-art flow for FP adder which supports the computation of normal and sub-normal operands, along with the support for the exceptional case handling. The key components in the architecture, such as comparator, swap, dynamic shifters, leading-one-detector (LOD), mantissa adders/subtractors, and rounding circuit, are re-designed and optimized for multi-mode computation, to enable efficient resource sharing for multi-precision operands. The data-path in each multi-mode architecture is tuned for multi-precision support with minimal multiplexing circuitry overhead. These proposed architectures provide multi-precision SIMD support for lower precision operands, along with high precision computational support, and thus, have a better resource utilization. A fully pipelined version of both adder architectures are presented. The proposed adder architectures are synthesized using UMC 90 nm technology ASIC implementation. The proposed architectures are compared with the best available literature works, and have shown better design metrics in terms of area, delay and area×period, along with more computational support.
"
tags: []
featured: true
url_code: 
url_poster: 
url_slides: 
projects: [arithmetic]
---
