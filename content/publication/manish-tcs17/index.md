---
title: "Area-Efficient Architecture for Dual-Mode Double Precision Floating Point Division"
authors: [Manish Kumar Jaiswal, Hayden Kwok-Hay So]
date: 2017-02-01
doi: "10.1109/TCSI.2016.2607227"
publishDate: 2017-02-01
publication_types: ["2"]
publication: "IEEE Transactions on Circuits and Systems I: Regular Papers"
publication_short: "TCSI'17"
abstract: "
Floating point division is a core arithmetic widely used in scientific and engineering applications. This paper proposed an architecture for double precision floating point division. This architecture is designed for dual-mode functionality, which can either compute on a pair of double precision operands or on two pairs of single precision operands in parallel. The architecture is based on the series expansion multiplicative methodology of mantissa computation. For this, a novel dual-mode Radix-4 Modified Booth multiplier is designed, which is used iteratively in the architecture of dual-mode mantissa computation. Other key components of floating point division flow (such as leading-one-detection, left/right dynamic shifters, rounding, etc.) are also re-designed for the dual-mode operation. The proposed dual-mode architecture is synthesized using UMC 90 nm technology ASIC implementation. Two versions of proposed architecture are presented, one with single stage multiplier and another with two stage multiplier. Compared to a standalone double precision division architecture, the proposed dual-mode architecture requires 17% to 19% extra hardware resources, with 3% to 5% period overhead. In comparison to prior art on this, the proposed architecture out-performs them in terms of required area, time-period and throughput.
"
tags: []
featured: true
url_code: 
url_poster: 
url_slides: 
projects: [arithmetic]
---
