# Praneeth Mangala

**AI Lead Engineer, Founding Team at [Orbis AI Technologies Inc.](https://www.orbisfactoryos.ai) · Research Intern at NIT Raipur**

[Portfolio](https://c0ntr1butr.github.io/Praneeth_Portfolio/) · [LinkedIn](https://www.linkedin.com/in/praneeth2709/) · [GitHub](https://github.com/c0ntr1butr) · [Google Scholar](https://scholar.google.com/citations?hl=en&user=O3Y1Lm0AAAAJ) · [IEEE Xplore](https://ieeexplore.ieee.org/abstract/document/11076959) · [Email](mailto:praneethmangala339@gmail.com)

---

## About me

I build AI systems that can be trusted: agentic AI with runtime governance in industry, and physics-informed machine learning in research.

I am part of the founding team at Orbis AI Technologies Inc., where I lead AI engineering for **FactoryOS**, an AI-native manufacturing operations platform. My work there covers the Orbis family of AI agents that orchestrate and monitor the data-ingestion pipeline, the factory context layer, and RAG-grounded AI copilots with human-in-the-loop approval. I also founded **Agentflow.ai**, where I'm building Memory OS, a governance layer for agent memory, permissions and auditability.

In research, I work with Prof. Dr. V. K. Vidyarthi at NIT Raipur on physics-informed neural networks (PINNs) for the Richards equation, comparing them against numerical methods for hydrology applications. My undergraduate thesis at VNIT Nagpur, with Prof. Dr. Anamika Singh, produced a guided-medium molecular communication test bed. It was published at IEEE ICMOCE'25, selected for hardware demonstration at NCC'25 (IIT Delhi), and led to a patent application.

I hold a B.Tech in Electronics and Communication Engineering from VNIT Nagpur (2025).

## Research interests

- Agentic AI, multi-agent orchestration and persistent memory
- Runtime governance and policy enforcement for AI systems
- Physics-informed neural networks and scientific machine learning
- Retrieval-augmented generation for operational knowledge

## Selected highlights

- **Publication:** *Design and Implementation of Guided Medium based Molecular Communication Test Bed*, IEEE ICMOCE 2025, IIT Bhubaneswar
- **In preparation:** *Comparing PINN vs Numerical Methods for Hydrology Applications*, and a paper on runtime governance for agentic AI
- **Patent filed:** guided-medium molecular communication hardware architecture
- **Runner-up, RBI HaRBInger (4th edition):** Enhancing Trust track, ₹20 lakh prize
- **Global Finalist, Global Fintech Fest 2025** · **Jury Award, HackIITK 2026** · **5th of 60 teams, EmberGround AI Hackathon 2026**
- **Top 1%, JEE Main 2021** (1.2M candidates)

## Open to work and collaboration

I'm open to:

- **Graduate study and research positions** in AI systems, agentic AI and scientific machine learning
- **Research collaborations** on AI governance, PINNs and physics-guided learning
- **Engineering roles and projects** building production AI systems and agent infrastructure

The best way to reach me is by [email](mailto:praneethmangala339@gmail.com) or on [LinkedIn](https://www.linkedin.com/in/praneeth2709/). My CV is [here](assets/Praneeth_Mangala_CV.pdf).

---

## About this site

A lightweight, seven-page static site: Home, Experience, Research, Projects, Events, Honors and Education. It's built with Tailwind CSS (compiled ahead of time) and a few lines of vanilla JavaScript, and hosted on GitHub Pages.

```bash
npm install      # once
npm run build    # regenerate the HTML pages from scripts/build_pages.py and rebuild the CSS
```

- **Content:** all page text, the header and the footer live in `scripts/build_pages.py`. Running the build overwrites the HTML files, so edit the content there.
- **Styles:** design tokens are in `tailwind.config.js`; shared component classes are in `src/input.css`.
- **Images:** compressed WebP files in `assets/img/`, loaded lazily as they come into view.
