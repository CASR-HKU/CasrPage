---
title: "GraVF: A vertex-centric distributed graph processing framework on FPGAs"
authors: [Nina Engelhardt, Hayden Kwok-Hay So]
date: 2016-08-29
doi: "10.1109/FPL.2016.7577360"
publishDate: 2016-08-29
publication_types: ["1"]
publication: "2016 26th International Conference on Field Programmable Logic and Applications (FPL)"
publication_short: "FPL'16"
abstract: "
FPGAs are promising platforms to efficiently execute distributed graph algorithms. Unfortunately, they are notoriously hard to program, especially when the problem size and system complexity increases. In this paper, we propose GraVF, a high-level design framework for distributed graph processing on FPGAs. It leverages the vertex-centric paradigm, which is naturally distributed and requires the user to define only very small kernels and their associated message semantics for the target application. The user design may subsequently be elaborated and compiled to the target system automatically by the framework. To demonstrate the flexibility and capabilities of the proposed framework, 4 graph algorithms with distinct requirements have been implemented, namely breadth-first search, PageRank, single source shortest path, and connected component. Results show that the proposed framework is capable of producing FPGA designs with performance comparable to similar custom designs while requiring only minimal input from the user.
"
tags: []
featured: true
url_code: https://github.com/nakengelhardt/fpgagraphlib/
url_poster: gravf-fccm2016-poster.pdf
url_slides: gravf-fpl2016-slides.pdf
projects: []
---
