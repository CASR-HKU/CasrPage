---
title: "FTDL: An FPGA-tailored architecture for deep learning systems"
authors: [Runbin Shi, Yuhao Ding, Xuechao Wei, Hang Liu, Hayden Kwok-Hay So, Caiwen Ding]
date: 2020-02-16
doi: "10.1145/3373087.3375384"
publishDate: 2020-02-16
publication_types: ["1"]
publication: "Proceedings of the 2020 ACM/SIGDA International Symposium on Field-Programmable Gate Arrays"
publication_short: "FPGA'20"
abstract: "
Hardware acceleration of deep learning (DL) systems has been increasingly studied to achieve desirable performance and energy efficiency. The FPGA strikes a balance between high energy efficiency and fast development cycle and therefore is widely used as a DNN accelerator. However, there exists an architecture-layout mismatch in the current designs, which introduces scalability and flexibility issues, leading to irregular routing and resource imbalance problems. To address these limitations, in this work, we propose FTDL, an FPGA-tailored architecture with a parameterized and hierarchical hardware that is adaptive to different FPGA devices. FTDL has the following novelties: (i) At the architecture level, FTDL consists of Tiled Processing Elements (TPE) and super blocks, to achieve a near-to-theoretical digital signal processing (DSP) operating-frequency of 650 MHz. More importantly, FTDL is configurable and delivers good scalability, i.e., the timing is stabilized even when the design is scaled-up to 100% resource utilization for different deep learning systems. (ii) In workload compilation, FTDL provides a compiler that manages to map the DL workloads to the architecture level in an optimal manner. Experimental results show that for most benchmark layers in MLPerf, FTDL achieves an over 80% hardware efficiency.

"
tags: [FPGA, machien learning acceleration, timing optimization, architecture-compilation co-design]
featured: true
url_code: https://github.com/rbshi/ftdnn
url_poster: ftdl-poster-fpga20.pdf
url_slides: ftdl-slides-fpga20.pdf
projects: []
---
