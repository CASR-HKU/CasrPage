---
title: "High-throughput cellular imaging with high-speed asymmetric-detection time-stretch optical microscopy under FPGA platform"
authors: [Ho-Cheung Ng, Maolin Wang, Bob M.F. Chung, B. Sharat Chandra Varma, Manish Kumar Jaiswal, Sam M.H. Ho, Kevin K. Tsia, Ho Cheung Shum, Hayden Kwok-Hay So]
date: 2017-02-16
doi: "10.1109/ReConFig.2016.7857175"
publishDate: 2017-02-16
publication_types: ["1"]
publication: "2016 International Conference on ReConFigurable Computing and FPGAs (ReConFig)"
publication_short: "RECONFIG'16"
abstract: "
Asymmetric-Detection Time-Stretch Optical Microscopy (ATOM) is a recently emerged technology that provides ultra-fast cell imaging with a frame rate up to MHz - orders-of-magnitude higher than any classical imaging systems. However, existing measuring instruments are unable to fully exploit the capability of ATOM. For example, the volume of imaging data-set of ATOM quickly increases beyond the capacity of available onboard buffer of a modern high-speed oscilloscope. This paper presents an open source, FPGA-based solution which serves as a dual role of collecting low-level signals from ATOM frontend as well as processing and transferring data to backing store. Optical signals are sampled by a high-speed analog-to-digital converter and the resulting values are collected by an FPGA. The quantized values received are then further processed and divided into four segments for subsequent data transfer with 10 Gbit Ethernet. Four computing units are attached to these channels with direct connection in order to reliably receive the data for post-processing. Experiments show that, with decent quality images for single-cell analysis, the proposed system can store 10x more dataset than existing high-end oscilloscope. With 8x decrease in equipment cost, the proposed FPGA-based system will definitely be beneficial for many bio imaging applications with ATOM technology such as rare cancer cell imaging and identification.
"
tags: []
featured: true
url_code: https://github.com/hku-casr/atom-droplet
url_poster: 
url_slides: 
projects: [imghardware]
---
