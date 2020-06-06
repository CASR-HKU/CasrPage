---
title: "Energy-efficient dataflow computations on FPGAs using application-specific coarse-grain architecture synthesis"
authors: [Colin Yu Lin, Hayden Kwok-Hay So]
date: 2012-03-01
doi: "10.1145/2460216.2460227"
publishDate: 2012-03-01
publication_types: ["1"]
publication: "ACM SIGARCH Computer Architecture News"
publication_short: "CAN'12"
abstract: "
Compiling high-level user applications to execute on FPGAbased reconfigurable computers often involve synthesizing dataflow graphs beyond the capacity of the available hardware resources. A framework that provides rapid and energyefficient compilation of such dataflow graphs on FPGAs using an array of pre-placed configurable processing elements is proposed. The mapping schedule of the compute operations on the CPEs and the direct network among the CPEs are co-synthesized on a per-application basis to provide the targeted power-performance tradeoff. Compared to the use of a fixed generic topology, the use of an application-specific topology derived by a genetic algorithm can achieve up to 28% improvement in energy-delay product. As the CPEs are pre-placed, compiling for a new application involve only the generation of a new operation schedule, which is stored in on-chip memory, and the new routes among the CPEs. With optimization in operation scheduling and mapping and application-specific interconnect network, the proposed framework achieved up to 199X better energy-delay product compared to a traditional FPGA high-level synthesis tool xPilot. The use of such framework is anticipated to serve as part of a high-level application compiler for hybrid CPU-FPGA computation.
"
tags: []
featured: true
url_code: 
url_poster: 
url_slides: 
projects: [overlay]
---
