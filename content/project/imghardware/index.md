---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "Imaging Hardware and Applications"
summary: "A fundamental technical challenge for ultra-fast cell microscopy is the trade-off between imaging throughput and resolution. In this project, we investigate the imaging and enhancement schemes and the dedicated FPGA hardware for the cutting edge cell microscopy."
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

Recent advances in high-throughput cell microscopy promise a new generation of image-based biomedical applications, e.g., cell sorting and classification, otherwise impossible with traditional biomolecular assays.
As the prior art in the cytometry technique, [ATOM system](https://www.eee.hku.hk/~alphahku/wordpress/research/) (as illustrated in **FIG.1**) is a home-built optical microscopy for cell flow imaging by [our colleborator](https://www.eee.hku.hk/~alphahku). 
One **challenge** with this system, however, is that we must derive adequate information from the cell images in realtime to facilitate various forms of image analytics while avoiding signiﬁcant impact on the overall imaging throughput.

As **FIG.1**, the cell flow imaging adopts the line scan technique, where the periodic laser pulse shines through the cell tunnel, and each pulse encodes an image line to the *time-stretched* signal. 
Subsequently, a digitizer (ADC) samples the continuous signal in an ultra-high-speed **(5 Giga samples per second)**, which still limits the imaging resolution. Hence, this research investigates a **realtime** super-resolution (SR) scheme for the ATOM system under the speed limitation of ADC.

{{< figure src="atom.png" title="Organization of ATOM microscopy for cell flow imaging." numbered="true" lightbox="true" width=90% >}}

We proposed a novel technique, **coprime line scan super-resolution (CLSS)**, for not only ATOM microscopy but also imaging systems with a similar mechanism.
Further, we designed **FPGA** based hardware architecture for CLSS that reaches a realtime processing throughput of **5 Gigapixels per second**, which is scarcely possible on other platforms.
The realtime super-resolution on FPGA facilitates the subsequent image-based cell classification and sorting. 
**FIG.2** demonstrates cell images for comparison. These images were sampled with the same ADC frequency, but different reconstruction schemes: (1) original sampling without SR; (2) with conventional rectilinear SR (interpolation); (3)-(5) with different options in CLSS sampling scheme. 


{{< figure src="cell.png" title="Cell images from ATOM system with/without **CLSS SR** for comparison." numbered="true" lightbox="true" width=80% >}}









































