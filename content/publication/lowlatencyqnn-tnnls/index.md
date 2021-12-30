---
title: "Low-Latency In Situ Image Analytics With FPGA-Based Quantized Convolutional Neural Network"
authors: [Maolin Wang, Kelvin C.M. Lee, Bob M.F. Chung, Sharatchandra Varma Bogaraju, Ho-Cheung Ng, Justin S.J. Wong, Ho Cheung Shum, Kevin K. Tsia, Hayden Kwok-Hay So]
date: 2021-01-12
doi: "10.1109/TNNLS.2020.3046452"
publishDate: 2021-01-12
publication_types: ["2"]
publication: "IEEE Transactions on Neural Networks and Learning Systems"
publication_short: "TNNLS"
abstract: "
Real-time in situ image analytics impose stringent latency requirements on intelligent neural network inference operations. While conventional software-based implementations on the graphic processing unit (GPU)-accelerated platforms are flexible and have achieved very high inference throughput, they are not suitable for latency-sensitive applications where real-time feedback is needed. Here, we demonstrate that high-performance reconfigurable computing platforms based on field-programmable gate array (FPGA) processing can successfully bridge the gap between low-level hardware processing and high-level intelligent image analytics algorithm deployment within a unified system. The proposed design performs inference operations on a stream of individual images as they are produced and has a deeply pipelined hardware design that allows all layers of a quantized convolutional neural network (QCNN) to compute concurrently with partial image inputs. Using the case of label-free classification of human peripheral blood mononuclear cell (PBMC) subtypes as a proof-of-concept illustration, our system achieves an ultralow classification latency of 34.2 μs with over 95% end-to-end accuracy by using a QCNN, while the cells are imaged at throughput exceeding 29,200 cells/s. Our QCNN design is modular and is readily adaptable to other QCNNs with different latency and resource requirements.
"
tags: []
featured: true
url_code: 
url_poster: 
url_slides: 
projects: [aihardware]
---
