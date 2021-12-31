---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "Event Camera"
summary: "Dynamic vision sensors (DVS) are neuromorphic devices that produce vision events asynchronously in response to changes in light intensity local to each pixel. This is in contrast to conventional vision sensors that produce images of the entire field-of-view at a fixed frame rate. The goal of this project is to address this need by developing an advanced hardware-software architecture that natively supports co-design of DVS vision algorithms optimized for deployment in demanding edge applications."

authors: [Hayden Kwok-Hay So]
profile: false
tags: []
categories: []
date: 2021-12-31

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

Dynamic vision sensors (DVS) are neuromorphic devices that produce vision events asynchronously in response to changes in light intensity local to each pixel. This is in contrast to conventional vision sensors that produce images of the entire field-of-view at a fixed frame rate. Together with other desirable imaging properties such as having high dynamic range and high temporal resolution, DVS sensors are promising technologies for use in demanding edge scenarios where energy-efficient intelligent computations are needed. The goal of this project is to address this need by developing an advanced hardware-software architecture that natively supports co-design of DVS vision algorithms optimized for deployment in demanding edge applications.

<html>
<body>
<h2>Multi-Object Tracking using REMOT</h2>
<video width="160" height="120" loop autoplay muted>
  <source src="shapesoutput.mp4" type="video/mp4">
</video>
</body>
</html>

**FIGURE 1** shows the overall hardware/software architecture of our attention-guided Multi-Object Tracking framework using event camera on FPGA called **REMOT**. REMOT incorporates a parallel set of reconfigurable hardware attention units (AUs) that work in tandem with a modular attention-guided software framework running in the attached processor. Each hardware AU autonomously adjusts its region of attention by processing each vision event as they are produced by the event camera.

{{< figure src="hw_sw.jpg" title="REMOT: A HW/SW Architecture for Attention-Guided Multi-Object Tracking" numbered="true" lightbox="true" width=100% >}}

REMOT is capable of processing 0.43–2.22 million events per second at 1.75–5.68 watts, making them suitable for real-time operations while maintaining good MOT accuracy in our target datasets. When compared with a software-only implementation using the same edge platforms, our HW-SW implementation results in up to 33.6 times higher event processing throughput and 25.9 times higher power efficiency.


