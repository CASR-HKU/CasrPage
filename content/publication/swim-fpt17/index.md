---
title: "Ultra-low latency continuous block-parallel stream windowing using FPGA on-chip memory"
authors: [Justin Wong, Runbin Shi, Maolin Wang, Hayden Kwok-Hay So]
date: 2017-12-11
doi: "10.1109/FPT.2017.8280121"
publishDate: 2017-12-11
publication_types: ["1"]
publication: "2017 International Conference on Field Programmable Technology"
publication_short: "FPT'17"
abstract: "
In this paper, we propose and demonstrate a real-time ultra-fast multi-data stream processing methodology on FPGA called “SWIM” (Stream Windowing on Interleaved Memory). The method exploits the flexible on-chip block memory fabric on existing FPGA architectures to achieve ultra-low-latency and fully pipelined continuous data flow while maintaining linear spatial locality of data for efficient data addressing and processing. The SWIM method is directly applicable to many practical applications such as real-time stencil computing, streaming image data processing, as well as closed loop-control systems that require ultra-low latency interleaved access and processing of high-speed sensor data. We demonstrate two practical cases on actual FPGA for generic 3-by-3 2-D convolution filter and image super-resolution method using pixel interleaving. Both memory usage and latency scales linearly with window height, or width of the 2-D input data set. The generic implementation of SWIM on FPGA showed impressive worst-case operation frequency of 410 MHz and uses 9.0χ and 5.6χ less Register and LUT resources respectively compared with a high-level synthesis solution.

"
tags: [FPGA, BRAM partition, line buffer]
featured: true
url_code: 
url_poster: 
url_slides: 
projects: []
---
