"""One-time generator for the multi-page portfolio. Writes plain static HTML files."""
import os, sys
ROOT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(__file__), "..")

ORB = "https://www.orbisfactoryos.ai"
EKA = "https://ekamobility.com"
GH = "https://github.com/c0ntr1butr"
LI = "https://www.linkedin.com/in/praneeth2709/"
SCHOLAR = "https://scholar.google.com/citations?hl=en&user=O3Y1Lm0AAAAJ"
IEEE = "https://ieeexplore.ieee.org/abstract/document/11076959"
MAIL = "mailto:praneethmangala339@gmail.com"
PHONE = "tel:+918328575111"
CV = "assets/Praneeth_Mangala_CV.pdf"

PAGES = [("index.html", "Home"), ("experience.html", "Experience"), ("research.html", "Research"),
         ("projects.html", "Projects"), ("events.html", "Events"), ("honors.html", "Honors"),
         ("education.html", "Education")]

def ne(cls="h-3.5 w-3.5"): return f'<svg class="icon {cls}" aria-hidden="true"><use href="#i-ne"/></svg>'

SPRITE = '''  <svg xmlns="http://www.w3.org/2000/svg" class="hidden">
    <symbol id="i-ne" viewBox="0 0 24 24"><path d="M7 17 17 7M8 7h9v9"/></symbol>
    <symbol id="i-menu" viewBox="0 0 24 24"><path d="M4 8h16M4 16h16"/></symbol>
    <symbol id="i-close" viewBox="0 0 24 24"><path d="M6 6l12 12M18 6 6 18"/></symbol>
    <symbol id="i-left" viewBox="0 0 24 24"><path d="M15 6l-6 6 6 6"/></symbol>
    <symbol id="i-right" viewBox="0 0 24 24"><path d="M9 6l6 6-6 6"/></symbol>
    <symbol id="i-phone" viewBox="0 0 24 24"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1.9.4 1.8.7 2.7a2 2 0 0 1-.5 2.1L8 9.8a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.7.7a2 2 0 0 1 1.7 2z"/></symbol>
    <symbol id="i-mail" viewBox="0 0 24 24"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/></symbol>
    <symbol id="i-cap" viewBox="0 0 24 24"><path d="M22 10 12 5 2 10l10 5 10-5z"/><path d="M6 12v5c3 2.5 9 2.5 12 0v-5"/></symbol>
    <symbol id="i-doc" viewBox="0 0 24 24"><path d="M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8z"/><path d="M14 3v5h5M9 13h6M9 17h6"/></symbol>
    <symbol id="i-github" viewBox="0 0 24 24"><path d="M12 .5C5.65.5.5 5.65.5 12a11.5 11.5 0 0 0 7.86 10.92c.58.1.79-.25.79-.56v-2c-3.2.7-3.88-1.37-3.88-1.37-.52-1.33-1.28-1.69-1.28-1.69-1.05-.72.08-.7.08-.7 1.16.08 1.77 1.19 1.77 1.19 1.03 1.77 2.7 1.26 3.36.96.1-.75.4-1.26.73-1.55-2.55-.29-5.24-1.28-5.24-5.68 0-1.26.45-2.28 1.19-3.08-.12-.29-.52-1.46.11-3.05 0 0 .97-.31 3.17 1.18a11 11 0 0 1 5.77 0c2.2-1.49 3.17-1.18 3.17-1.18.63 1.59.23 2.76.11 3.05.74.8 1.19 1.82 1.19 3.08 0 4.41-2.69 5.39-5.25 5.67.41.36.78 1.06.78 2.14v3.17c0 .31.21.67.8.56A11.5 11.5 0 0 0 23.5 12C23.5 5.65 18.35.5 12 .5z"/></symbol>
    <symbol id="i-linkedin" viewBox="0 0 24 24"><path d="M20.45 20.45h-3.55v-5.57c0-1.33-.03-3.04-1.85-3.04-1.86 0-2.14 1.45-2.14 2.94v5.67H9.35V9h3.41v1.56h.05c.48-.9 1.64-1.85 3.37-1.85 3.6 0 4.27 2.37 4.27 5.46v6.28zM5.34 7.43a2.06 2.06 0 1 1 0-4.12 2.06 2.06 0 0 1 0 4.12zM7.12 20.45H3.56V9h3.56v11.45zM22.22 0H1.77C.79 0 0 .77 0 1.73v20.54C0 23.23.79 24 1.77 24h20.45c.98 0 1.78-.77 1.78-1.73V1.73C24 .77 23.2 0 22.22 0z"/></symbol>
  </svg>'''

def profile_links(cls=""):
    items = [(LI, "i-linkedin", "LinkedIn", True), (GH, "i-github", "GitHub", True),
             (SCHOLAR, "i-cap", "Google Scholar", False), (IEEE, "i-doc", "IEEE Xplore", False),
             (MAIL, "i-mail", "Email", False), (PHONE, "i-phone", "+91 8328575111", False)]
    out = []
    for href, icon, label, fill in items:
        ic = "icon-fill" if fill else "icon"
        tgt = '' if href.startswith(("mailto", "tel")) else ' target="_blank" rel="noopener"'
        out.append(f'<a class="plink" href="{href}"{tgt}><svg class="{ic}" aria-hidden="true"><use href="#{icon}"/></svg>{label}</a>')
    return f'<div class="flex flex-wrap gap-2 {cls}">' + "".join(out) + '</div>'

def header(active):
    links = "\n".join(
        f'          <a class="nav-link" href="{f}"{" aria-current=\"page\"" if t == active else ""}>{t}</a>'
        for f, t in PAGES[1:])
    return f'''  <header class="sticky top-0 z-40 border-b border-line bg-paper/90 backdrop-blur-md">
    <div class="wrap flex h-16 items-center justify-between gap-6">
      <a href="index.html" class="flex items-center gap-2.5"{' aria-current="page"' if active == "Home" else ''}>
        <span class="grid h-7 w-7 place-items-center rounded-[5px] bg-ink font-serif text-[18px] leading-none text-paper">P</span>
        <span class="text-[15.5px] font-medium tracking-[-0.01em]">Praneeth Mangala</span>
      </a>
      <nav id="nav" aria-label="Main navigation" class="absolute inset-x-4 top-[4.25rem] hidden flex-col rounded-xl border border-line bg-paper-card p-2 shadow-xl lg:static lg:flex lg:flex-row lg:items-center lg:gap-0.5 lg:border-0 lg:bg-transparent lg:p-0 lg:shadow-none">
{links}
        <a class="btn-dark mt-2 justify-center lg:ml-3 lg:mt-0 lg:py-2" href="{CV}" target="_blank" rel="noopener">CV</a>
      </nav>
      <button id="menu" type="button" class="grid h-10 w-10 place-items-center rounded-md lg:hidden" aria-label="Open menu" aria-controls="nav" aria-expanded="false">
        <svg class="icon h-5 w-5" aria-hidden="true"><use href="#i-menu"/></svg>
      </button>
    </div>
  </header>'''

FOOTER = f'''  <footer class="mt-24 border-t border-line">
    <div class="wrap flex flex-col gap-5 py-8 md:flex-row md:items-center md:justify-between">
      {profile_links()}
      <p class="font-mono text-[11px] uppercase tracking-[0.08em] text-ink-50">© <span id="year">2026</span> Praneeth Mangala</p>
    </div>
  </footer>'''

LIGHTBOX = '''  <dialog id="lightbox" class="lightbox" aria-label="Photo viewer">
    <div class="flex h-[100dvh] w-screen flex-col items-center justify-center gap-4 p-4 md:p-10">
      <div class="flex w-full max-w-4xl items-center justify-between text-white/80">
        <span id="lb-count" class="font-mono text-[11px] uppercase tracking-[0.08em]"></span>
        <button type="button" class="lb-btn" data-lb="close" aria-label="Close"><svg class="icon h-5 w-5"><use href="#i-close"/></svg></button>
      </div>
      <div class="relative flex min-h-0 w-full max-w-4xl flex-1 items-center justify-center">
        <img id="lb-img" alt="" class="max-h-full max-w-full rounded-xl object-contain shadow-2xl">
        <button type="button" class="lb-btn absolute left-0 md:-left-16" data-lb="prev" aria-label="Previous photo"><svg class="icon h-5 w-5"><use href="#i-left"/></svg></button>
        <button type="button" class="lb-btn absolute right-0 md:-right-16" data-lb="next" aria-label="Next photo"><svg class="icon h-5 w-5"><use href="#i-right"/></svg></button>
      </div>
      <p id="lb-caption" class="max-w-2xl text-center text-[14px] text-white/85"></p>
    </div>
  </dialog>'''

def page(fname, title, desc, body, active):
    full_title = "Praneeth Mangala" if active == "Home" else f"{title} — Praneeth Mangala"
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{full_title}</title>
  <meta name="description" content="{desc}">
  <meta name="theme-color" content="#efefeb">
  <meta property="og:title" content="{full_title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:image" content="assets/img/profile-passport.webp">
  <link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect width='64' height='64' rx='10' fill='%23000'/%3E%3Ctext x='32' y='44' font-family='Georgia,serif' font-size='34' fill='%23efefeb' text-anchor='middle'%3EP%3C/text%3E%3C/svg%3E">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Geist:wght@400;500&family=Geist+Mono:wght@400&family=Instrument+Serif&display=swap">
  <link rel="stylesheet" href="assets/styles.css">
</head>
<body>
{SPRITE}
  <a href="#main" class="sr-only focus:not-sr-only focus:fixed focus:left-4 focus:top-4 focus:z-50 focus:rounded-md focus:bg-ink focus:px-3 focus:py-2 focus:text-paper">Skip to content</a>
{header(active)}

  <main id="main" class="wrap">
{body}
  </main>

{FOOTER}
{LIGHTBOX}
  <script src="script.js" defer></script>
</body>
</html>
'''

def page_head(title, sub):
    return f'''    <header class="page-head">
      <h1 class="page-title">{title}</h1>
      <p class="page-sub">{sub}</p>
    </header>'''

def section(title, inner, first=False):
    return f'''    <section class="{'' if first else 'mt-14'}">
      <h2 class="section-label">{title}</h2>
{inner}
    </section>'''

def ul(items): return '<ul class="bullets">' + "".join(f"<li>{i}</li>" for i in items) + "</ul>"

def thumb(group, full, sq, caption, label=None, size="h-24 w-24 sm:h-28 sm:w-28"):
    return (f'<button type="button" class="thumb {size}" data-lightbox="{group}" data-src="assets/img/{full}.webp" data-caption="{caption}">'
            f'<img src="assets/img/{sq}.webp" width="320" height="320" alt="{caption}" loading="lazy" decoding="async"></button>')

def extra(group, full, caption):
    return f'<span hidden data-lightbox="{group}" data-src="assets/img/{full}.webp" data-caption="{caption}"></span>'

# ---------------------------------------------------------------- HOME
home = f'''    <section class="grid gap-8 pt-12 md:grid-cols-[11rem_1fr] md:gap-12 md:pt-20">
      <img src="assets/img/profile-passport.webp" width="590" height="758" alt="Passport-size portrait of Praneeth Mangala" class="aspect-[35/45] w-36 rounded-2xl border border-line bg-white object-cover md:w-44" fetchpriority="high">
      <div>
        <p class="subhead">AI Lead Engineer, Founding Team · Researcher</p>
        <h1 class="mt-3 font-serif text-[clamp(2.4rem,5vw,3.4rem)] font-normal leading-none tracking-[-0.01em]">Praneeth Mangala</h1>
        <p class="mt-5 max-w-2xl text-[17px] leading-relaxed text-ink-80">I build AI systems that can be trusted — agentic AI with runtime governance in industry, and physics-informed machine learning in research.</p>
        <p class="body mt-4 max-w-2xl">I am part of the founding team at <a class="ext text-ink" href="{ORB}" target="_blank" rel="noopener">Orbis AI Technologies Inc.</a>, where I lead AI engineering for FactoryOS as AI Lead Engineer. I am also a research intern at NIT Raipur working on physics-informed neural networks for hydrological PDEs. I hold a B.Tech in Electronics and Communication Engineering from VNIT Nagpur (2025).</p>
        <div class="mt-6 flex flex-wrap gap-2.5">
          <a class="btn-dark" href="{CV}" target="_blank" rel="noopener">Download CV</a>
          <a class="btn-line" href="{MAIL}">Contact</a>
        </div>
        {profile_links("mt-6")}
      </div>
    </section>

    <div class="mt-16 grid gap-12 border-t border-line pt-10 md:grid-cols-2">
      <section>
        <h2 class="section-label">Research interests</h2>
        <ul class="bullets">
          <li>Agentic AI, multi-agent orchestration, and persistent memory</li>
          <li>Runtime governance and policy enforcement for AI systems</li>
          <li>Physics-informed neural networks and scientific ML</li>
          <li>Retrieval-augmented generation for operational knowledge</li>
        </ul>
      </section>
      <section>
        <h2 class="section-label">Highlights</h2>
        <ul class="bullets">
          <li><a class="ext text-ink" href="research.html">IEEE publication</a> — ICMOCE’25, IIT Bhubaneswar</li>
          <li><a class="ext text-ink" href="research.html">Patent filed</a> — molecular communication hardware</li>
          <li><a class="ext text-ink" href="research.html">Two papers in preparation</a> — AI governance and PINNs</li>
          <li><a class="ext text-ink" href="honors.html">Runner-up, RBI HaRBInger</a> — ₹20 lakh prize</li>
          <li><a class="ext text-ink" href="events.html">Global Finalist</a> — Global Fintech Fest 2025</li>
          <li>Top 1% in JEE Main 2021 (1.2M candidates)</li>
        </ul>
      </section>
    </div>'''

# ---------------------------------------------------------------- EXPERIENCE
def stack_block(rows):
    if not rows: return ""
    body = "".join(f'<div class="stack-row"><dt>{k}</dt><dd>{v}</dd></div>' for k, v in rows)
    return f'<dl class="stack">{body}</dl>'

def role(logo, title, org, dates, items, stack=None):
    return f'''      <article class="entry">
        {logo}
        <div>
          <div class="flex flex-wrap items-baseline justify-between gap-x-6 gap-y-1">
            <h3 class="entry-title">{title}</h3>
            <p class="subhead">{dates}</p>
          </div>
          <p class="entry-org">{org}</p>
          {ul(items)}
          {stack_block(stack)}
        </div>
      </article>'''

experience = page_head("Experience", "Industry and research roles.") + "\n" + section("Roles", "\n".join([
    role(f'<a class="logo-tile" href="{ORB}" target="_blank" rel="noopener" aria-label="Orbis AI website"><img src="assets/img/logo-orbis.webp" width="200" height="200" alt="Orbis AI logo" loading="lazy"></a>',
         'AI Lead Engineer, Founding Team',
         f'<a class="ext" href="{ORB}" target="_blank" rel="noopener">Orbis AI Technologies Inc. {ne()}</a> <span class="text-ink-50">(Submitted to YC Winter 2027)</span><br>Headquartered in Michigan, USA · Bengaluru',
         "Aug 2026 — Present",
         ["Founding engineer on FactoryOS V1, an AI-native manufacturing operations platform; shipped core modules from prototype to production.",
          "Built the Orbis agent family that orchestrates and monitors the data-ingestion pipeline: job scheduling, record validation, and failure alerting.",
          "Designed the factory context layer, a unified PostgreSQL schema spanning machines, production, workforce, quality, and maintenance.",
          "Built RAG and memory services over SOPs and manuals that ground AI copilots, with human-in-the-loop approval and audit logging."]),
    role('<span class="logo-tile"><img src="assets/img/logo-agentflow.webp" width="200" height="182" alt="Agentflow.ai logo" loading="lazy"></span>',
         "Founder", "Agentflow.ai Systems · Bengaluru", "Jul 2026 — Present",
         ["Building Memory OS, a governance layer for agent memory: scoped access, permission policies, and audit trails.",
          "Designing a runtime that orchestrates AI agents across tools and workflows under enforceable governance policies."]),
    role('<span class="monogram">N</span>', "Research Intern (Remote)", "NIT Raipur · Prof. Dr. V. K. Vidyarthi", "Jan 2026 — Present",
         ["Developing PyTorch PINNs for the nonlinear Richards equation governing variably saturated subsurface flow.",
          "Encoding PDE residuals and boundary/initial conditions in the loss; benchmarking accuracy and convergence against numerical solvers."]),
    role(f'<a class="logo-tile !p-0" href="{EKA}" target="_blank" rel="noopener" aria-label="EKA Mobility website"><img src="assets/img/logo-eka.webp" width="200" height="200" alt="EKA Mobility logo" loading="lazy" class="!object-cover"></a>', "R&amp;D Software Engineer",
         f'<a class="ext" href="{EKA}" target="_blank" rel="noopener">EKA Mobility {ne()}</a> · Pune', "Jul 2025 — Aug 2026",
         ["Estimated battery SoC and SoH from 8 months of EV telemetry using time-series analysis, improving life-cycle accuracy by 15%.",
          "Built scikit-learn models to detect operational bottlenecks, reducing system-wide errors by 20%.",
          "Built SQL pipelines for 100K+ daily records; index optimisation cut query latency by 30%.",
          "Built EKA-Connect, a React dashboard for real-time operational insights."]),
]), first=True)

# ---------------------------------------------------------------- RESEARCH
PREP = """      <article class="entry !grid-cols-1">
        <div>
          <div class="flex flex-wrap items-baseline justify-between gap-x-6 gap-y-1"><h3 class="entry-title">Runtime Governance for Agentic AI Systems</h3><p class="subhead">In preparation</p></div>
          <p class="body mt-1">Policy enforcement over agent memory, tool permissions, and auditability at runtime.</p>
        </div>
      </article>
      <article class="entry !grid-cols-1">
        <div>
          <div class="flex flex-wrap items-baseline justify-between gap-x-6 gap-y-1"><h3 class="entry-title">Comparing PINN vs Numerical Methods for Hydrology Applications</h3><p class="subhead">In preparation</p></div>
          <p class="body mt-1">Benchmarking physics-informed neural networks against numerical solvers for the Richards equation · NIT Raipur.</p>
        </div>
      </article>"""

research = page_head("Research", "Physics-informed machine learning and molecular communication.") + "\n" + \
section("Publication", f'''      <article class="entry !grid-cols-1">
        <div>
          <h3 class="entry-title">Design and Implementation of Guided Medium based Molecular Communication Test Bed</h3>
          <p class="entry-org"><b class="font-medium text-ink">P. Mangala</b>, V. Lokhande, A. Singh, P. Sharma</p>
          <p class="body mt-1">3rd International Conference on Microwave, Optical and Communication Engineering (ICMOCE), IIT Bhubaneswar, 2025 · IEEE</p>
          <div class="mt-4 flex flex-wrap gap-2"><a class="plink" href="{IEEE}" target="_blank" rel="noopener"><svg class="icon"><use href="#i-doc"/></svg>IEEE Xplore</a><a class="plink" href="{SCHOLAR}" target="_blank" rel="noopener"><svg class="icon"><use href="#i-cap"/></svg>Google Scholar</a></div>
        </div>
      </article>''', first=True) + "\n" + \
section("Papers in preparation", PREP) + "\n" + \
section("Research projects", f'''      <article class="entry !grid-cols-1">
        <div>
          <div class="flex flex-wrap items-baseline justify-between gap-x-6 gap-y-1"><h3 class="entry-title">Physics-Informed Neural Networks for Hydrological PDEs</h3><p class="subhead">Jan 2026 — Present</p></div>
          <p class="entry-org">NIT Raipur · Advisor: Prof. Dr. V. K. Vidyarthi</p>
          {ul(["Solving the nonlinear Richards equation for subsurface flow with PINNs in PyTorch.",
               "Benchmarking PINNs against numerical solvers for hydrology applications."])}
        </div>
      </article>
      <article class="entry !grid-cols-1">
        <div>
          <div class="flex flex-wrap items-baseline justify-between gap-x-6 gap-y-1"><h3 class="entry-title">Guided-Medium Molecular Communication Test Bed</h3><p class="subhead">Sep 2024 — Apr 2025</p></div>
          <p class="entry-org">B.Tech thesis, VNIT Nagpur · Advisor: Prof. Dr. Anamika Singh</p>
          {ul(["Built a water-based test bed achieving N-bit transmission with a bit error rate below 5%.",
               "Designed an N-bit transmission algorithm using solenoid valves and FOOK modulation.",
               "Presented at ICMOCE’25 and NCC’25; patent filed for the hardware architecture."])}
          <div class="mt-5 flex flex-wrap gap-3">
            {thumb("mc", "research-testbed", "research-testbed-sq", "3-bit (8-node) molecular communication transmitter")}
            {thumb("mc", "research-tx", "research-tx-sq", "Transmitter architecture — relay banks driving solenoid valves")}
            {thumb("mc", "evt-icmoce-algo", "evt-icmoce-algo-sq", "Proposed N-bit algorithm (ICMOCE’25)")}
            {thumb("mc", "evt-ncc", "evt-ncc-sq", "Research demonstration at NCC’25, IIT Delhi")}
          </div>
        </div>
      </article>''') + "\n" + \
section("Patent", '''      <p class="body">Patent application filed for the guided-medium molecular communication hardware architecture.</p>''')

# ---------------------------------------------------------------- PROJECTS
def proj(name, meta, desc, link=None, label="GitHub", icon="i-github", fill=True):
    btn = ""
    if link:
        ic = "icon-fill" if fill else "icon"
        btn = f'<a class="plink shrink-0" href="{link}" target="_blank" rel="noopener"><svg class="{ic}" aria-hidden="true"><use href="#{icon}"/></svg>{label}</a>'
    return f'''      <article class="flex flex-col gap-3 border-b border-line py-6 last:border-0 sm:flex-row sm:items-start sm:justify-between sm:gap-8">
        <div>
          <h3 class="entry-title">{name}</h3>
          <p class="mt-0.5 font-mono text-[11.5px] uppercase tracking-[0.05em] text-ink-50">{meta}</p>
          <p class="body mt-2 max-w-2xl">{desc}</p>
        </div>
        {btn}
      </article>'''

projects = page_head("Projects", "Selected work across AI systems, scientific ML, and embedded hardware.") + "\n" + \
section("Industry", "\n".join([
    proj("FactoryOS", "Orbis AI Technologies Inc. · Next.js · FastAPI · PostgreSQL · Redshift · LangGraph",
         "AI-native manufacturing operations platform with agent-orchestrated data ingestion, a factory context layer, and RAG-grounded AI copilots.",
         ORB, "orbisfactoryos.ai", "i-ne", False),
    proj("Memory OS", "Agentflow.ai · Agentic AI · Governance",
         "Governance layer for agentic AI that controls agent memory, permissions, access, and auditability."),
]), first=True) + "\n" + \
section("Independent", "\n".join([
    proj("PINN for a 1D Harmonic Oscillator", "PyTorch · NumPy · Matplotlib",
         "Physics-informed network that learns underdamped oscillator dynamics by embedding the governing ODE in the loss.",
         f"{GH}/1D-Oscillator_PINN"),
    proj("AI Co-Founder System", "Python · Multi-agent · RAG",
         "Planner, Validator, and Executor agents that turn startup ideas into execution plans, with Cognee + RAG memory.",
         f"{GH}/AI-Cofounder"),
    proj("App Graph Builder", "TypeScript · React · ReactFlow · Zustand",
         "Visual node-based workflow builder with a state-graph engine and pluggable Input, LLM, and API nodes.",
         f"{GH}/App-Graph-Builder"),
    proj("StayEase", "Flutter · Firebase · Node.js",
         "PG management system with real-time tenant, payment, and occupancy sync and role-based access."),
    proj("8086 Analog-to-Digital Converter", "8086 Assembly · Embedded C",
         "ADC/DAC interfacing via the 8255 PPI and 8253 timer with a 32-point moving-average filter.",
         f"{GH}/Analog-to-Digital-Converter"),
]))

# ---------------------------------------------------------------- EVENTS
def event(group, photos, date, place, title, role):
    main = photos[0]
    rest = "".join(extra(group, f, c) for f, _, c in photos[1:])
    n = len(photos)
    more = f'<button type="button" class="mt-3 inline-flex items-center gap-1.5 text-[13.5px] text-ink-80 underline decoration-ink-30 underline-offset-4 hover:decoration-ink" data-lightbox-open="{group}">View {n} photo{"s" if n > 1 else ""}</button>'
    return f'''      <article class="flex gap-5 border-b border-line py-6 last:border-0 sm:gap-6">
        {thumb(group, main[0], main[1], main[2])}{rest}
        <div class="min-w-0">
          <p class="subhead">{date}{" · " + place if place else ""}</p>
          <h3 class="entry-title mt-1.5">{title}</h3>
          <p class="body mt-1">{role}</p>
          {more}
        </div>
      </article>'''


def attended(title, meta, note=""):
    n = f'<p class="body mt-0.5">{note}</p>' if note else ""
    return f'''      <li class="flex flex-col gap-1 border-b border-line py-4 last:border-0 sm:flex-row sm:items-baseline sm:justify-between sm:gap-6">
        <div><p class="entry-title !text-[16px]">{title}</p>{n}</div>
        <p class="subhead shrink-0">{meta}</p>
      </li>'''

events = page_head("Events &amp; Conferences", "Talks, conferences, and competitions.") + "\n" + \
section("2026", "\n".join([
    event("sam", [("evt-sam-poster", "evt-sam-poster-sq", "Software Architects Meetup — speaker poster")],
          "24 Oct 2026", "", "Software Architects Meetup", "Speaker — AI governance at runtime: designing secure, observable, controllable agents."),
    event("ember", [("evt-emberground", "evt-emberground-sq", "EmberGround AI Hackathon 2026 — Startup Park, Bengaluru")],
          "27 Sep 2026", "Bengaluru", "EmberGround AI Hackathon 2026", "5th Prize out of 60 participating teams — autonomous systems and intelligent apps."),
    event("rbi", [("evt-rbi-team", "evt-rbi-team-sq", "RBI HaRBInger — team FraudLens Aura with the runner-up award"),
                  ("evt-rbi-plaque", None, "Runner-up plaque — Enhancing Trust track, 18 Apr 2026")],
          "18 Apr 2026", "Bengaluru", "RBI HaRBInger — 4th Edition", "Runner-up, Enhancing Trust track (FraudLens Aura) — ₹20 lakh prize."),
    event("iitk", [("evt-hackiitk", "evt-hackiitk-sq", "HackIITK 2026 Grand Finale — IIT Kanpur"),
                   ("evt-hackiitk-cert", None, "Jury Award for Promising Solution — HackIITK 2026")],
          "9–10 Apr 2026", "IIT Kanpur", "HackIITK 2026", "Jury Award for Promising Solution — AI-driven fraud detection."),
]), first=True) + "\n" + \
section("2025", "\n".join([
    event("seed", [("evt-seed", "evt-seed-sq", "SEED Hackathon — Team 28 VNITx, 2nd place"),
                   ("evt-seed-cert", None, "Certificate of Achievement — 2nd Place, SEED Hackathon")],
          "20 Nov 2025", "Virtual", "SEED Hackathon", "2nd Place — co-presented by George Washington University and Boston University."),
    event("gff", [("evt-gff-stage", "evt-gff-stage-sq", "Global Fintech Fest 2025 — FraudLens team on stage"),
                  ("evt-gff-group", None, "Global Fintech Fest 2025 — with finalists and organisers"),
                  ("evt-gff-hall", None, "Global Fintech Fest 2025 — main stage")],
          "Oct 2025", "Mumbai", "Global Fintech Fest 2025", "Global Finalist — FraudLens, AI-powered fraud detection."),
    event("icmoce", [("evt-icmoce-photo", "evt-icmoce-photo-sq", "At ICMOCE’25, IIT Bhubaneswar"),
                     ("evt-icmoce", None, "ICMOCE’25 — Paper 418 title slide"),
                     ("evt-icmoce-algo", None, "ICMOCE’25 — proposed N-bit algorithm")],
          "23–25 May 2025", "IIT Bhubaneswar", "ICMOCE’25", "Paper presentation — guided-medium molecular communication test bed (IEEE)."),
    event("ncc", [("evt-ncc", "evt-ncc-sq", "Research demonstration at NCC’25, IIT Delhi"),
                  ("research-testbed", None, "The molecular communication transmitter demonstrated at NCC’25")],
          "2025", "IIT Delhi", "NCC’25 — National Conference on Communications", "Selected for hardware demonstration of the molecular communication test bed."),
])) + "\n" + \
section("Upcoming", '<ul>' + "\n".join([
    attended("Build with AI Bootcamp", "13–14 Nov 2026 · Google Ananta, Bengaluru", "Hands-on bootcamp hosted by Google."),
    attended("Altera Innovation", "17 Nov 2026 · Bengaluru"),
]) + '</ul>') + "\n" + \
section("Also attended", '<ul>' + "\n".join([
    attended("Build with Gemini", "Bengaluru", "Building applications with Google’s Gemini models."),
    attended("ElevenLabs Summit", "Bengaluru", "Voice AI and audio models."),
    attended("AWS Marketplace Conclave", "ITC Gardenia, Bengaluru"),
    attended("BMC Control-M", "Bengaluru", "Workflow orchestration with Control-M."),
    attended("Wiz Club", "Conrad, Bengaluru", "Cloud security community meetup by Wiz."),
    attended("Central Bank of India Cybersecurity Hackathon — Finals", "2025 · MANIT Bhopal", "Finalist · $6,000 award."),
]) + '</ul>')

# ---------------------------------------------------------------- HONORS
def award(year, title, detail):
    return f'''      <li class="grid gap-1 border-b border-line py-4 last:border-0 sm:grid-cols-[5rem_1fr] sm:gap-6">
        <span class="subhead pt-0.5">{year}</span>
        <div><p class="entry-title !text-[16px]">{title}</p><p class="body mt-0.5">{detail}</p></div>
      </li>'''

honors = page_head("Honors", "Awards, programs, and leadership.") + "\n" + \
section("Awards", '<ul>' + "\n".join([
    award("2026", "5th Prize — EmberGround AI Hackathon", "Out of 60 teams · Bengaluru"),
    award("2026", "Runner-up — RBI HaRBInger (4th Edition)", "Enhancing Trust track, FraudLens Aura · ₹20 lakh"),
    award("2026", "Jury Award — HackIITK", "Promising Solution · $600"),
    award("2025", "Global Finalist — Global Fintech Fest", "FraudLens"),
    award("2025", "2nd Place — SEED Hackathon", "$420 prize and 50% fee waiver"),
    award("2025", "Runner-up — BITS Pilani Innovators Conclave", "Innovation and pitch competition"),
    award("2025", "Central Bank of India Cybersecurity Hackathon", "Finals at MANIT Bhopal · $6,000 award"),
    award("2025", "Selected for Hardware Demonstration — NCC’25, IIT Delhi", "National Conference on Communications · guided-medium molecular communication test bed"),
    award("2021", "Top 1% — JEE Main", "Among 1.2M candidates"),
]) + '</ul>', first=True) + "\n" + \
section("Programs &amp; talks", '<ul>' + "\n".join([
    award("Oct 2026", "Speaker — Software Architects Meetup", "AI governance at runtime"),
    award("Aug 2026", "AWS re:Grant", "Selected participant"),
    award("Aug 2026", "McKinsey.org Forward", "Selected participant"),
]) + '</ul>') + "\n" + \
section("Leadership", '<ul>' + "\n".join([
    award("2024", "Event Manager — AXIS’24, VNIT", "Led logistics for the national techfest with 20+ volunteers"),
    award("2024", "Creative Secretary — ECE Department", "Led branding; department placed 2nd at IG’24"),
    award("2023", "Workshop — AI for Wireless Communications", "Prof. Arumugam Nallanathan, Queen Mary University of London"),
]) + '</ul>')

# ---------------------------------------------------------------- EDUCATION
education = page_head("Education", "Academic background and technical foundations.") + "\n" + \
section("Academic history", f'''      <article class="flex gap-5 border-b border-line py-6 sm:gap-6">
        {thumb("conv", "edu-convocation", "edu-convocation-sq", "Receiving the B.Tech degree at VNIT Nagpur’s 22nd Convocation, 15 Sep 2025")}
        <div class="min-w-0 flex-1">
          <div class="flex flex-wrap items-baseline justify-between gap-x-6 gap-y-1"><h3 class="entry-title">Visvesvaraya National Institute of Technology (VNIT), Nagpur</h3><p class="subhead">Oct 2021 — May 2025</p></div>
          <p class="entry-org">B.Tech, Electronics and Communication Engineering · CGPA 6.75 / 10</p>
          <p class="body mt-1">Thesis: Guided-medium molecular communication test bed · Advisor: Prof. Dr. Anamika Singh</p>
        </div>
      </article>
      <article class="py-6">
        <div class="flex flex-wrap items-baseline justify-between gap-x-6 gap-y-1"><h3 class="entry-title">Shastra Junior College</h3><p class="subhead">2019 — 2021</p></div>
        <p class="entry-org">Higher Secondary Certificate (Mathematics, Physics, Chemistry) · 98.6%</p>
      </article>
      <article class="border-t border-line py-6">
        <div class="flex flex-wrap items-baseline justify-between gap-x-6 gap-y-1"><h3 class="entry-title">Viswa Bharathi English Medium High School</h3><p class="subhead">2006 — 2019</p></div>
        <p class="entry-org">Secondary School Certificate (SSC) · GPA 10 / 10</p>
      </article>''', first=True) + "\n" + \
section("Relevant coursework", '''      <div class="border-t border-line">
        <p class="row"><b>Mathematics</b> Linear Algebra, Numerical Linear Algebra, Numerical Methods, Probability &amp; Statistics, Calculus</p>
        <p class="row"><b>Computer science</b> Data Structures, Algorithms, Operating Systems, Object-Oriented Programming</p>
        <p class="row"><b>Applied ML</b> Machine Learning, Physics-Informed ML, Deep Learning, Digital Signal Processing, Embedded Systems</p>
      </div>''') + "\n" + \
section("Technical skills", '''      <div class="border-t border-line">
        <p class="row"><b>Languages</b> Python, C/C++, SQL, JavaScript, TypeScript, MATLAB, 8086 Assembly</p>
        <p class="row"><b>AI &amp; ML</b> PyTorch, LangChain, LangGraph, scikit-learn, NumPy, SciPy, Pandas, Statsmodels</p>
        <p class="row"><b>Backend &amp; APIs</b> FastAPI, Node.js, Spring Boot · REST, gRPC</p>
        <p class="row"><b>Frontend</b> React, Next.js</p>
        <p class="row"><b>Databases</b> PostgreSQL (OLTP), Amazon Redshift (OLAP), Firebase</p>
        <p class="row"><b>Cloud &amp; tools</b> AWS, Git, Jupyter, LaTeX</p>
      </div>''')

CONTENT = {
    "index.html": ("Home", "AI engineer and researcher working on agentic AI, runtime governance, and physics-informed machine learning.", home),
    "experience.html": ("Experience", "Industry and research roles of Praneeth Mangala.", experience),
    "research.html": ("Research", "Publication and research projects of Praneeth Mangala.", research),
    "projects.html": ("Projects", "Selected projects by Praneeth Mangala.", projects),
    "events.html": ("Events", "Talks, conferences, and competitions attended by Praneeth Mangala.", events),
    "honors.html": ("Honors", "Awards, programs, and leadership of Praneeth Mangala.", honors),
    "education.html": ("Education", "Education of Praneeth Mangala.", education),
}
for fname, (active, desc, body) in CONTENT.items():
    title = active if active != "Events" else "Events & Conferences"
    with open(os.path.join(ROOT, fname), "w") as f:
        f.write(page(fname, title, desc, body, active))
    print("wrote", fname)
