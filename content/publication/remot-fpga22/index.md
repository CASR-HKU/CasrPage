---
title: "REMOT: A Hardware-Software Architecture for Attention-Guided Multi-Object Tracking with Dynamic Vision Sensors on FPGAs"
authors: [Yizhao Gao, Song Wang, Hayden Kwok-Hay So]
date: 2021-12-29
doi: "10.1145/3490422.3502365"
publishDate: 2022-02-29
publication_types: ["1"]
publication: " The 2022 ACM/SIGDA International Symposium on Field-Programmable Gate Arrays"
publication_short: "FPGA'22 (to appear)"
abstract: "
In contrast to conventional vision sensors that produce images of the entire field-of-view at a fixed frame rate, dynamic vision sensors (DVS) are neuromorphic devices that only produce sparse events in response to changes in light intensity local to each pixel, making them promising technologies for use in demanding edge scenarios where energy-efficient intelligent computations are needed. While several early research have demonstrated promising results in performing high-level machine vision tasks using vision events only, these algorithms are often too complex for real-time deployments in edge systems with limited processing and storage capabilities. In this work, a novel hardware-software architecture, called REMOT, is proposed to leverage the unique properties of DVS to perform real-time multi-object tracking (MOT) on FPGAs. REMOT incorporates a parallel set of reconfigurable hardware attention units (AUs) that work in tandem with a modular attention-guided software framework running in the attached processor. Each hardware AU autonomously adjusts its region of attention by processing each vision event as they are produced by the DVS. Using information aggregated by the AUs, high-level analyses are performed in software. To demonstrate the flexibility and modularity of REMOT, a family of MOT algorithms with different hardware-software configurations and  tradeoffs have been implemented on 2 different edge reconfigurable systems. Experimental results show that REMOT is capable of processing 0.43-2.22 million events per second at 1.75-5.68 watts, making them suitable for real-time operations while maintaining good MOT accuracy in our target datasets.  When compared with a software-only implementation using the same edge platforms, our HW-SW implementation results in up to 33.6 times higher event processing throughput and 25.9 times higher power efficiency.
"
tags: []
featured: true
url_code: "https://doi.org/10.25442/hku.17284643" 
url_poster: 
url_slides: 
projects: [aihardware]
---
