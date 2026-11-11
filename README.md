# Praneeth Mangala — Portfolio

A responsive, single-page portfolio built with HTML, CSS and vanilla JavaScript.

## Run locally
Open `index.html` in a browser. The site has seven pages: Home, Experience, Research, Projects, Events, Honors and Education.

## Editing content
All page content, the shared header and footer, and the profile links live in `scripts/build_pages.py`. Edit the content there, then run:

```bash
npm run build   # regenerates the seven HTML pages and the CSS
```

Running the build overwrites the HTML files, so don't hand-edit them unless you stop using the script.

## Editing styles (Tailwind CSS)
The site uses Tailwind CSS v3, compiled ahead of time into one small minified file. It does not use the Tailwind CDN script.

```bash
npm install          # once
npm run dev          # rebuilds assets/styles.css on every save
npm run build        # minified production build
```

- Design tokens (colors, fonts, radii, animations): `tailwind.config.js`
- Shared component classes (`.card`, `.btn-dark`, `.statement`, …): `src/input.css`
- Run `npm run build` after changing classes in `index.html`, then commit `assets/styles.css`.

## Performance notes
- No JS frameworks or icon fonts. Icons are an inline SVG sprite, and `script.js` is about 40 lines.
- Fonts: Geist, Geist Mono and Instrument Serif from Google Fonts (`display=swap`).
- The profile photo is a compressed JPEG with explicit dimensions, so the layout doesn't shift while it loads.
- Animations respect the visitor's `prefers-reduced-motion` setting.

## Publish with GitHub Pages
1. Push this folder to the repository root (`assets/styles.css` included).
2. In GitHub, open **Settings → Pages**, choose **Deploy from a branch**, `main`, `/ (root)`.

## Images
All images live in `assets/img/` as compressed WebP files and load lazily as they scroll into view.

**Add an event photo:** resize it to about 1400px wide and save it as WebP (quality around 78). Then copy an `<article>` inside `#events`. To give one event several photos, give each `data-lightbox` element the same name; the photo viewer then steps through them in order.

## Still to do
- Replace `assets/img/profile.webp` with a sharper headshot (the current source is upscaled).
- Add a photo for NCC'25 (IIT Delhi) and RBI HaRBInger'25 if you have one.
- Confirm Orbis AI is comfortable with the FactoryOS screenshot being public.
- Fix the resume issues (LinkedIn placeholder link, CGPA scale, typos) and overwrite `assets/Praneeth_Mangala_CV.pdf`.

## Contact and profiles
Email: praneethmangala339@gmail.com  
LinkedIn: https://www.linkedin.com/in/praneeth2709/  
GitHub: https://github.com/c0ntr1butr  
Google Scholar: https://scholar.google.com/citations?hl=en&user=O3Y1Lm0AAAAJ
