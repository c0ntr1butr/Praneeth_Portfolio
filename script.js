(() => {
  const $ = (s, el = document) => el.querySelector(s);

  // Mobile menu
  const menu = $("#menu"), nav = $("#nav");
  const setMenu = (open) => {
    nav.classList.toggle("hidden", !open);
    nav.classList.toggle("flex", open);
    menu.setAttribute("aria-expanded", String(open));
    menu.setAttribute("aria-label", open ? "Close menu" : "Open menu");
    $("use", menu).setAttribute("href", open ? "#i-close" : "#i-menu");
  };
  menu.addEventListener("click", () => setMenu(menu.getAttribute("aria-expanded") !== "true"));

  // Photo viewer: elements sharing a data-lightbox name form one gallery
  const dlg = $("#lightbox"), img = $("#lb-img"), cap = $("#lb-caption"), count = $("#lb-count");
  let group = [], i = 0;
  const show = () => {
    const el = group[i];
    img.src = el.dataset.src;
    img.alt = cap.textContent = el.dataset.caption || "";
    count.textContent = group.length > 1 ? `${i + 1} / ${group.length}` : "";
    dlg.querySelectorAll('[data-lb="prev"],[data-lb="next"]').forEach((b) => (b.hidden = group.length < 2));
  };
  const open = (name, start) => {
    group = [...document.querySelectorAll(`[data-lightbox="${name}"]`)];
    i = Math.max(0, group.indexOf(start)); show(); dlg.showModal();
  };
  const step = (d) => { i = (i + d + group.length) % group.length; show(); };

  document.addEventListener("click", (e) => {
    const t = e.target.closest("button[data-lightbox], [data-lightbox-open]");
    if (!t) return;
    open(t.dataset.lightbox || t.dataset.lightboxOpen, t.dataset.lightbox ? t : null);
  });
  dlg.addEventListener("click", (e) => {
    const a = e.target.closest("[data-lb]")?.dataset.lb;
    if (a === "next") step(1);
    else if (a === "prev") step(-1);
    else if (a === "close" || e.target === dlg || e.target === dlg.firstElementChild) dlg.close();
  });
  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape") setMenu(false);
    if (!dlg.open) return;
    if (e.key === "ArrowRight") step(1);
    if (e.key === "ArrowLeft") step(-1);
  });

  $("#year").textContent = new Date().getFullYear();
})();
