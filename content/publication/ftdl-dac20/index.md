---
title: "FTDL: A tailored FPGA-overlay for deep learning with high scalability"
authors: [Runbin Shi, Yuhao Ding, Xuechao Wei, He Li, Hang Liu, Hayden Kwok-Hay So, Caiwen Ding]
date: 2020-07-29
doi: ""
publishDate: 2020-05-29
publication_types: ["1"]
publication: "Proceedings of the 57th Annual Design Automation Conference 2020"
publication_short: "DAC'20 (to appear)"
abstract: "
Fast inference is of paramount value to a wide range of deep learning applications. To address the architecture and hardware mismatch faced by traditional efforts, this work presents FTDL, a highlyscalable FPGA overlay framework for deep learning applications. The FTDL overlay is speciﬁcally optimized for the tiled structure of FPGAs, thereby achieving post-place-and-route operating frequencies exceeding 88 % of the theoretical maximum across different devices and design scales. A ﬂexible compilation framework efﬁciently schedules matrix multiply and convolution operations of large neural network inference on the overlay and achieved over 80 % hardware-efﬁciency on average. Taking advantage of both high operating-frequency and hardwareefﬁciency, FTDL achieves 402.6 and 151.2 FPS with GoogLeNet and ResNet50 on ImageNet respectively while operating at a power efﬁciency of 27.6 GOPS/W, making it up to 7.7× higher performance and 1.9× more power efﬁcient than prior art.

"
tags: []
featured: true
url_code: https://github.com/rbshi/ftdnn
url_poster: 
url_slides: 
projects: [overlay, aihardware]
---
