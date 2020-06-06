---
title: "High-throughput line buffer microarchitecture for arbitrary sized streaming image processing"
authors: [Runbin Shi, Justin Wong, Hayden Kwok-Hay So]
date: 2019-03-06
doi: "10.3390/jimaging5030034"
publishDate: 2019-03-06
publication_types: ["2"]
publication: "Journal of Imaging"
publication_short: ""
abstract: "
Parallel hardware designed for image processing promotes vision-guided intelligent applications. With the advantages of high-throughput and low-latency, streaming architecture on FPGA is especially attractive to real-time image processing. Notably, many real-world applications, such as region of interest (ROI) detection, demand the ability to process images continuously at different sizes and resolutions in hardware without interruptions. FPGA is especially suitable for implementation of such flexible streaming architecture, but most existing solutions require run-time reconfiguration, and hence cannot achieve seamless image size-switching. In this paper, we propose a dynamically-programmable buffer architecture (D-SWIM) based on the Stream-Windowing Interleaved Memory (SWIM) architecture to realize image processing on FPGA for image streams at arbitrary sizes defined at run time. D-SWIM redefines the way that on-chip memory is organized and controlled, and the hardware adapts to arbitrary image size with sub-100 ns delay that ensures minimum interruptions to the image processing at a high frame rate. Compared to the prior SWIM buffer for high-throughput scenarios, D-SWIM achieved dynamic programmability with only a slight overhead on logic resource usage, but saved up to 56% of the BRAM resource. The D-SWIM buffer achieves a max operating frequency of 329.5 MHz and reduction in power consumption by 45.7% comparing with the SWIM scheme. Real-world image processing applications, such as 2D-Convolution and the Harris Corner Detector, have also been used to evaluate D-SWIM’s performance, where a pixel throughput of 4.5 Giga Pixel/s and 4.2 Giga Pixel/s were achieved respectively in each case. Compared to the implementation with prior streaming frameworks, the D-SWIM-based design not only realizes seamless image size-switching, but also improves hardware efficiency up to 30×.

"
tags: []
featured: true
url_code: https://github.com/rbshi/swin_bram
url_poster: 
url_slides: 
projects: [imghardware]
---
