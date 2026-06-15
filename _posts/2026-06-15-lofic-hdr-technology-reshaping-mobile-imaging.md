---
title: "LOFIC HDR: The Technology Reshaping Mobile Imaging in 2026"
date: 2026-06-15
layout: post
excerpt: "A technical deep dive into Lateral Overflow Integration Capacitor HDR technology — why it matters, who is winning, and what comes next in the pixel-level HDR race."
---

> **Tagline**: Every flagship phone in 2026 uses LOFIC or a variant. Here is how it works and who leads.

---

## The HDR Bottleneck

For years, mobile CIS HDR was a game of compromises:

| Technology | Dynamic Range | Artifacts | Pixel Impact |
|:-----------|:-------------:|:---------:|:------------:|
| Multi-exposure (DCG) | 100-110 dB | Motion blur, ghosting | Minimal |
| Dual conversion gain | 90-100 dB | Seamless, but range limited | ~10% area |
| **LOFIC** | **130-140 dB** | **None** | **~5% area** |

Multi-exposure HDR works by capturing the same scene at different integration times — short, medium, long — then fusing them in the ISP. The result is impressive dynamic range, but moving objects appear in multiple positions across frames: the classic **ghosting artifact**.

Dual Conversion Gain (DCG) solves ghosting by switching the conversion gain within a single exposure. But the capacitance-limited range caps at ~100 dB, insufficient for extreme scenes like tunnel exits or backlit portraits.

**LOFIC changes the game.**

---

## How LOFIC Works (For Engineers)

A standard 4T pixel has a floating diffusion (FD) node with a fixed charge capacity — typically 30,000-60,000 e⁻ for a 1.0µm pixel. Once the FD saturates, extra photoelectrons spill into adjacent pixels (blooming) or are simply lost.

LOFIC adds a small capacitor — the **Lateral Overflow Integration Capacitor** — connected to the FD through a dedicated transfer gate (TG):

```
                 VDD
                  |
    RST ──┐      RST
          |       |
    PD ──TG── FD ──┐── SF ──> Output
                   |   |
    LOFIC_TG ──||──┘   |
                C      VSS
              LOFIC
              (Capacitor)
```

**Operation sequence:**

1. **Low-light mode**: LOFIC_TG OFF. The pixel operates as a standard 4T cell with high conversion gain. Excellent read noise (~1.5 e⁻). Full well capacity (FWC) = 30,000 e⁻.

2. **Bright-light mode**: LOFIC_TG ON. The LOFIC capacitor is connected in parallel with the FD, increasing total capacitance by 2-4×. FWC jumps to 80,000-120,000 e⁻. Conversion gain drops proportionally.

3. **Dual-readout**: The pixel is read twice — once with LOFIC off (for detail in dark areas) and once with LOFIC on (for highlight retention). A per-pixel HDR fusion algorithm combines both readings into a single 130-140 dB image.

**The critical advantage**: Both readouts occur within the **same exposure**. No temporal misalignment means zero motion artifacts. For video, this is transformative — true single-exposure HDR at 60 fps or higher.

---

## The LOFIC Battleship: Who Has What

| Feature | Sony | Samsung | OmniVision | SmartSens |
|:--------|:----:|:-------:|:----------:|:---------:|
| LOFIC production | ✅ STARVIS 3 (IMX908, Mar 2026) | ❌ R&D | ✅ TheiaCel (OV50H/X) | ✅ LOFIC 3.0 (SCC90XS) |
| Single-exposure HDR | 110 dB | — | 130-140 dB | 105 dB |
| Pixel pitch supported | 2.0µm+ (automotive) | — | 0.7-1.2µm | 0.61µm |
| 200MP + LOFIC | ❌ | ❌ | ❌ | ✅ SCC90XS |
| Mass prod. maturity | Ramping | 2 years behind | **3 generations mature** | Rapid iteration |

**Sony's STARVIS 3** (IMX908) is technically impressive, but it targets the automotive market at 2.0µm+ pixel pitch. For mobile at 0.7-1.0µm, Sony has not yet announced a LOFIC product.

**OmniVision's TheiaCel** — the OV50H (1.2µm) and OV50X (1.0µm) — is the clear leader for mobile LOFIC. Three generations of refinement have yielded the industry's highest single-exposure dynamic range at 130-140 dB with minimal pixel penalty (~5% area overhead).

**SmartSens SCC90XS** is the technical dark horse: 0.61µm pixel + LOFIC + 200MP in a single sensor. The 0.61µm pitch pushes the physical limits of photon collection, but the LOFIC implementation at such a small pitch is an impressive engineering feat.

---

## The Physics Limit: Why LOFIC Matters at Small Pixels

As pixels shrink below 1.0µm, every electron counts:

| Pixel Pitch | FWC (4T) | FWC (LOFIC) | SNR Boost |
|:-----------:|:--------:|:-----------:|:---------:|
| 1.0µm | 60,000 e⁻ | 180,000 e⁻ | +4.8 dB |
| 0.8µm | 38,000 e⁻ | 114,000 e⁻ | +4.8 dB |
| 0.61µm | 22,000 e⁻ | 66,000 e⁻ | +4.8 dB |

The SNR improvement is independent of pixel size — it's a function of the capacitance ratio. For a 3× boost in FWC, you get a consistent 4.8 dB improvement in highlight-region SNR.

This is critical because **small-pixel sensors are inherently photon-starved**. LOFIC doesn't help with photon shot noise in the shadows (that requires larger pixels or better QE), but it **rescues highlights that would otherwise be clipped**. In practical terms, a LOFIC-equipped 0.61µm pixel can capture a scene that would require a 1.0µm pixel without LOFIC — a significant area/cost advantage.

---

## The 2026-2027 Outlook

| Year | Milestone | Implication |
|:----:|:---------|:------------|
| **2026 H2** | Xiaomi 15 Ultra with OV50X (TheiaCel) | Mass-market validation |
| **2026 H2** | Sony Xperia (potential IMX908 mobile variant) | Sony's mobile LOFIC debut? |
| **2027 H1** | SmartSens SCC90XS in Chinese flagships | 200MP LOFIC goes mainstream |
| **2027 H2** | Samsung ISOCELL LOFIC samples | Late entrant, but IDM advantage |

**The takeaway**: LOFIC has crossed the chasm from niche automotive technology to mainstream mobile imaging. The companies with mature LOFIC IP — **OmniVision (Will Semi)** and **SmartSens** — have a 2-3 year lead over Samsung and a mobile-specific lead over Sony.

---

*This is not investment advice. Technical analysis based on publicly available datasheets, patent filings, and industry briefings as of June 2026.*
