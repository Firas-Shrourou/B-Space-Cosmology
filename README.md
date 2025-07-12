# B-Space Cosmology
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Paper Version](https://img.shields.io/badge/paper-July%202025-blue.svg)](./paper/B-Space-Cosmology.pdf)
[![Community Call](https://img.shields.io/badge/Next%20Step-Community%20MCMC%20Analysis-red.svg)](#the-path-forward-a-call-for-community-led-mcmc-analysis)

**A physical framework that provides a unified, first-principles resolution to the Hubble Tension, the cosmic slowdown, and anomalous galaxy spin alignments.**

This repository contains the scientific paper and supplementary materials for B-Space Cosmology, a complete physical alternative to the standard ΛCDM model.

---

## Abstract

We introduce B-Space Cosmology, a framework motivated by an accumulating set of observational crises in modern cosmology. We postulate that dark matter is not a particle but the physical fabric of a static, infinite background (B-Space), and our observable universe is a finite domain of baryonic matter (the "Drip") expanding into this medium. This paradigm replaces metric expansion and dark energy with a dynamic system governed by pressure and a growing volumetric drag. We demonstrate that this single framework provides a unified physical origin for three of the most significant anomalies in modern cosmology: the Hubble Tension, the recently observed weakening of cosmic acceleration, and the large-scale alignment of galaxy spins. The model is presented with its governing equations and a series of sharp, falsifiable predictions that distinguish it from ΛCDM.

## A Convergence of Crises

The Standard Model of Cosmology (ΛCDM) is facing a crisis of concordance. B-Space Cosmology is designed to address these core issues from a single, consistent framework:
1.  **The Hubble Tension:** The persistent ~5σ discrepancy between early-universe (Planck) and late-universe (SHOES) measurements of the cosmic expansion rate, H₀.
2.  **The Weakening of Dark Energy:** Recent evidence from the Dark Energy Spectroscopic Instrument (DESI) suggests that cosmic acceleration is slowing down, in direct contradiction to ΛCDM's constant dark energy.
3.  **Anomalous Galaxy Spin Alignments:** JWST has observed large-scale, coherent galaxy spin alignments that challenge the Cosmological Principle of isotropy.

## The B-Space Solution

B-Space replaces the abstract concepts of dark matter and dark energy with physical mechanics. The model is built on three postulates:
1.  **B-Space as the Static Background:** A 3D physical medium that constitutes the fundamental arena of the cosmos. This medium is the physical reality of dark matter.
2.  **The Drip as a Localized, Dynamic Universe:** The observable universe is a finite domain of baryonic matter expanding into B-Space. This expansion is physical motion, not metric expansion.
3.  **The Drip Obeys Known Local Physics:** The intrinsic laws governing matter within the Drip are the established laws of physics (e.g., General Relativity, Standard Model).

For the post-recombination universe (z ≤ 1100), this leads to a definitive **Master Equation of Expansion**:

<p align="center">
  <img src="https://latex.codecogs.com/svg.latex?\frac{\ddot{a}}{a}=-\frac{4\pi&space;G}{3}\rho_{m}+\frac{8\pi&space;G}{3}\rho_{\text{ext}}-(\Gamma_{0}a^{3})H" title="\frac{\ddot{a}}{a}=-\frac{4\pi G}{3}\rho_{m}+\frac{8\pi G}{3}\rho_{\text{ext}}-(\Gamma_{0}a^{3})H" />
</p>

Here, expansion is driven by a constant pressure (`ρ_ext`) and resisted by gravity and a growing volumetric **drag** (`Γ₀a³H`). This drag term is the key to the model's dynamics.

## A Framework of Predictive Unity

B-Space offers a network of interconnected, falsifiable predictions that resolve the aforementioned crises.

| Anomaly | B-Space Resolution | Status |
| :--- | :--- | :--- |
| **Hubble Tension** | The drag force was negligible in the early universe (yielding a low H₀) but has grown over time, reshaping the expansion history to match the high H₀ observed today. | **Solves by Design.** The model is built to resolve this. |
| **Weakening Dark Energy** | The growing drag (`~a³`) must inevitably overtake the constant pressure, causing cosmic acceleration to slow down. | **Inevitable Prediction.** The DESI slowdown is the first sign of this. |
| **Anomalous IGM Heating** | The kinetic energy lost to drag must be converted to heat, providing a natural explanation for the observed excess temperature of the intergalactic medium (IGM). | **Natural Consequence.** |
| **High-z Galaxy Spin Alignments** | A "Primordial Vorticity Field" (PVF) in B-Space imprints a coherent spin on forming galaxies. The model provides an excellent statistical fit (χ²/dof = 0.21) to JWST data. | **Excellent Statistical Fit.** |
| **A Diffuse Infrared Glow** | The drag-heated IGM must radiate, producing a faint, isotropic component of the Cosmic Infrared Background (CIB), uncorrelated with galaxies. | **Falsifiable Prediction.** |

## The Path Forward: A Call for Community-Led MCMC Analysis

The B-Space model is defined by a small number of parameters (e.g., `ρ_ext`, `Γ₀`, `z_c`) that are not free but are constrained by observational data. The next critical step is for the scientific community to perform a full **Markov Chain Monte Carlo (MCMC)** analysis.

We invite researchers to fit the B-Space model to the complete set of cosmological data (CMB, SNe, BAO, SHOES, JWST spins). This will provide definitive, data-driven measurements of the model's parameters and allow for high-precision tests of its predictions.

This repository provides the theoretical foundation for this analysis.

## Repository Contents

*   **`/B-Space-Cosmology.pdf`**: The complete scientific paper, "B-Space Cosmology: A Unified Alternative to the Standard Cosmological Model," including all appendices and references. This is the primary document.
*   **`/code`**: This directory will host the analysis code. The full analysis code for the Primordial Vorticity Field (PVF) work is available at:
    *   [github.com/Firas-Shrourou/B-Space-Cosmology/PVF](https://github.com/Firas-Shrourou/B-Space-Cosmology/PVF)

## Licensing
This project is licensed to encourage open scientific collaboration.
Written Works: The scientific paper and all other written content are licensed under the Creative Commons Attribution 4.0 International License (CC BY 4.0).
Source Code: All source code is released under the MIT License.

## Contact
For questions, comments, or collaboration inquiries, please contact:
Firas Shrourou
Email: firas@chamsolutions.com

## How to Cite

If you use the concepts or results from this work, please cite the main paper. A BibTeX entry is provided below for your convenience.

```bibtex
@article{Shrourou2025BSpace,
  title   = {{B-Space Cosmology: A Unified Alternative to the Standard Cosmological Model}},
  author  = {Firas Shrourou},
  year    = {2025},
  month   = {July},
  url     = {https://github.com/Firas-Shrourou/B-Space-Cosmology}
}
