---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "Graph Processing on FPGA"
summary: "In this project, we present GraVF-M, a framework designed to ease the implementation of FPGA-based graph processing accelerators for multi-FPGA platforms with distributed memory."
authors: [Hayden Kwok-Hay So]
profile: false
tags: []
categories: []
date: 2015-09-01

# Optional external URL for project (replaces project detail page).
external_link: ""

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: ""
  focal_point: ""
  preview_only: true

# Custom links (optional).
#   Uncomment and edit lines below to show custom links.
# links:
# - name: Follow
#   url: https://twitter.com
#   icon_pack: fab
#   icon: twitter

url_code: ""
url_pdf: ""
url_slides: ""
url_video: ""

# Slides (optional).
#   Associate this project with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides = "example-slides"` references `content/slides/example-slides.md`.
#   Otherwise, set `slides = ""`.
slides: ""
---

Due to the irregular nature of connections in most graph datasets, partitioning graph analysis algorithms across multiple computational nodes that do not share a common memory inevitably leads to large amounts of interconnect traffic. Previous research has shown that FPGAs can outcompete software-based graph processing in shared memory contexts, but it remains an open question if this advantage can be maintained in distributed systems.


In this work, we present GraVF-M, a framework designed to ease the implementation of FPGA-based graph processing accelerators for multi-FPGA platforms with distributed memory. Based on a lightweight description of the algorithm kernel, the framework automatically generates optimized RTL code for the whole multi-FPGA design. We exploit an aspect of the programming model to present a familiar message-passing paradigm to the user, while under the hood implementing a more efficient architecture that can reduce the necessary inter-FPGA network traffic by a factor equal to the average degree of the input graph. A performance model based on a theoretical analysis of the factors influencing performance serves to evaluate the efficiency of our implementation. With a throughput of up to 5.8 GTEPS (billions of traversed edges per second) on a 4-FPGA system, the designs generated by GraVF-M compare favorably to state-of-the-art frameworks from the literature and reach 94% of the projected performance limit of the system.










































