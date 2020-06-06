---
title: "Towards FPGA-assisted Spark: An SVM training acceleartion case study"
authors: [Sam M.H. Ho, Maolin Wang, Ho-Cheung Ng, Hayden Kwok-Hay So]
date: 2016-11-01
doi: "10.1109/ReConFig.2016.7857194"
publishDate: 2016-11-01
publication_types: ["1"]
publication: "2016 International Conference on ReConFigurable Computing and FPGAs (ReConFig)"
publication_short: "RECONFIG'16"
abstract: "
A system that augments the Apache Spark data processing framework with FPGA accelerators is presented as a way to model and deploy FPGA-assisted applications in large-scale clusters. In our proposed framework, FPGAs can optionally be used in place of the host CPU for Resilient distributed datasets (RDDs) transformations, allowing seamless integration between gateware and software processing. Using the case of training an Support Vector Machine (SVM) cell image classifier as a case study, we explore the feasibilities, benefits and challenges of such technique. In our experiments where data communication between CPU and FPGA is tightly controlled, a consistent speedup of up to 1.6x can be achieved for the target SVM training application as the cluster size increases. Hardware-software techniques that are crucial to achieve acceleration such as the management of data partition size are explored. We demonstrate the benefits of the proposed framework, while also illustrate the importance of careful hardware-software management to avoid excessive CPU-FPGA communication that can quickly diminish the benefits of FPGA acceleration.
"
tags: []
featured: true
url_code: https://bitbucket.org/sammhho/sparkaccel/src/master/
url_poster: 
url_slides: 
projects: [graph]
---
