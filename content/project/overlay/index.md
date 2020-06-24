---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "FPGA Overlay"
summary: "FPGAs demonstrate valuable potential for customized acceleration. However, the design productivity of developing FPGA accelerators remains much lower compared to the use of a typical software development flow. In this project, we investigate the FPGA overlay, an effective FPGA design abstraction for general computation dataflow and domain-specific scenarios."
authors: [Hayden Kwok-Hay So]
profile: false
tags: []
categories: []
date: 2017-02-01

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

The use of FPGAs as compute accelerators has been demonstrated by numerous researchers as an effective solution to meet the performance requirement across many application domains. However, the design productivity of developing FPGA accelerators remains much lower compared to the use of a typical software development flow. Although the use of the high-level design tools may partly alleviate this shortcoming, the lengthy low-level FPGA implementation process, including synthesis, placing and routing still dramatically limits the number of compile-debug-edit cycles per day and hinders the widespread adoption of FPGAs.

In this project, we investigate the FPGA overlay, an effective FPGA design abstraction for general computation dataflow and domain-specific scenarios. 

For the general cases, we have developed a rapid FPGA loop accelerator generation framework called [QuickDough](/publication/quickdough-fpt15/). By utilizing a soft coarse-grained reconfigurable array (SCGRA) overlay built on top of off-the-shelf FPGAs, it compiles a high-level loop to the overlay through rapid operation scheduling first and then generates the FPGA accelerator bitstream through rapid integration of the scheduling result and a pre-built overlay bitstream.

The domain-specific overlay is also popular that provides the specialization for the a package of **parameterized** applications. For example, we present [FTDL](/publication/ftdl-dac20/), an FPGA tailored deep learning overlay, which is optimized for the timing in FPGA implementation and hardware utilization in real-world cases. 

{{< figure src="featured.png" title="Demonstration of FPGA overaly framework." numbered="true" lightbox="true" width=60% >}}





































