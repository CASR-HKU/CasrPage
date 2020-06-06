---
title: "QuickDough: a rapid FPGA loop accelerator design framework using soft CGRA overlay"
authors: [Cheng Liu, Ho-Cheung Ng, Hayden Kwok-Hay So]
date: 2015-12-07
doi: "10.1109/FPT.2015.7393130"
publishDate: 2015-12-07
publication_types: ["1"]
publication: "2015 International Conference on Field Programmable Technology (FPT)"
publication_short: "FPT'15"
abstract: "
The use of FPGAs as compute accelerators has been demonstrated by numerous researchers as an effective solution to meet the performance requirement across many application domains. However, the design productivity of developing FPGA accelerators remains much lower compared to the use of a typical software development flow. Although the use of the high-level design tools may partly alleviate this shortcoming, the lengthy low-level FPGA implementation process including synthesis, placing and routing still dramatically limits the number of compile-debug-edit cycles per day and hinders the widespread adoption of FPGAs. To address this design productivity problem, we have developed a rapid FPGA loop accelerator generation framework called QuickDough. By utilizing a soft coarse-grained reconfigurable array (SCGRA) overlay built on top of off-the-shelf FPGAs, it compiles a high-level loop to the overlay through a rapid operation scheduling first and then generates the FPGA accelerator bitstream through a rapid integration of the scheduling result and a pre-built overlay bitstream. According to the experiments, QuickDough is able to produce accelerators in the order of seconds while achieving up to 9X performance speedup over the execution of the same software running on a hard ARM processor.
"
tags: []
featured: true
url_code: https://github.com/Liu-Cheng/QuickDough
url_poster: 
url_slides: 
projects: [overlay]
---
