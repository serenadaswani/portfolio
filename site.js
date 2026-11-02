// Edit this block to make the site yours.
const SITE = {
  name: "Anoushka Ghosh",
  timezone: "America/Los_Angeles",
  nav: [
    { label: "Work", href: "index.html" },
    { label: "Fun", href: "fun.html" },
    { label: "Notes", href: "notes.html" },
    { label: "About", href: "about.html" },
  ],
  socials: [
    { label: "LinkedIn", href: "https://www.linkedin.com/in/anoushkaghosh/" },
    { label: "Behance", href: "https://www.behance.net/Anoushka-Ghosh" },
    { label: "GitHub", href: "https://github.com/ghoshanoushka" },
    { label: "Resume", href: "https://drive.google.com/file/d/1x3pUb8lTMzYpkzIJ6nRIZ6F23U4mlWyp/view" },
    { label: "Let's Chat", href: "https://calendly.com/noushka-umich/30min" },
  ],
  // `media` can be an image or .mp4 path (e.g. "media/project.mp4").
  // Without media, a gradient placeholder is drawn from `colors`.
  // `cursor` is the label that follows the mouse: "View project", "Visit site", "Coming soon".
  // `ratio` is the thumbnail aspect ratio (width / height).
  projects: [
    { title: "Mensio", sub: "Shipped 2026", href: "projects/mensio.html", cursor: "View project", ratio: 16 / 9, colors: ["#2b3a67", "#7aaee9"] },
    { title: "Project One", sub: "Concept 2025", href: "projects/project-one.html", cursor: "View project", ratio: 16 / 9, colors: ["#e98d34", "#d0a8d8"] },
    { title: "Project Two", sub: "Shipped 2026", href: "projects/project-two.html", cursor: "View project", ratio: 16 / 9, colors: ["#8fb8a8", "#e8f0ee"] },
    { title: "Project Three", sub: "Contract 2026", href: "https://example.com", external: true, cursor: "Visit site", ratio: 4 / 3, colors: ["#007fff", "#7aaee9"] },
    { title: "Project Four", sub: "Shipping 2026", cursor: "Coming soon", ratio: 16 / 9, colors: ["#c9c4bc", "#f3f2f0"] },
    { title: "Project Five", sub: "Concept 2025", href: "projects/project-five.html", cursor: "View project", ratio: 16 / 9, colors: ["#b8bec6", "#e6e8eb"] },
    { title: "Project Six", sub: "Contract 2025", href: "projects/project-six.html", cursor: "View overview", ratio: 16 / 9, colors: ["#001445", "#3b5a9a"] },
    { title: "Project Seven", sub: "Shipped 2025", href: "projects/project-seven.html", cursor: "View project", ratio: 16 / 9, colors: ["#1a316e", "#4a68b0"] },
    { title: "Project Eight", sub: "Shipped 2023", href: "projects/project-eight.html", cursor: "View project", ratio: 5 / 4, colors: ["#ddd0fc", "#b9a6ec"] },
    { title: "Project Nine", sub: "Shipped 2023", href: "projects/project-nine.html", cursor: "View project", ratio: 5 / 4, colors: ["#7aaee9", "#cfe2f7"] },
  ],
};

// Pages in subfolders (e.g. projects/) set <body data-root="../"> so shared links resolve.
const ROOT = document.body.dataset.root || "";
const currentPage = location.pathname.split("/").pop() || "index.html";
const isProject = document.body.dataset.page === "project";

function navLinks() {
  return SITE.nav
    .map(({ label, href }) => {
      const active = href === currentPage || (isProject && href === "index.html") ? ' data-active="true"' : "";
      return `<a class="nav-link" href="${ROOT}${href}"${active}>${label}</a>`;
    })
    .join("");
}

// Sidebar table of contents built from <section id> and .project-subsection[id] on project pages.
function tocLinks() {
  return [...document.querySelectorAll("main section[id], main .project-subsection[id]")]
    .map((el) => {
      const sub = el.classList.contains("project-subsection") ? " toc-sub" : "";
      return `<a class="nav-link${sub}" href="#${el.id}" data-toc="${el.id}">${el.dataset.toc || el.id}</a>`;
    })
    .join("");
}

function renderChrome() {
  document.querySelectorAll("[data-name]").forEach((el) => (el.textContent = SITE.name));

  const top = isProject
    ? `<div class="breadcrumb fade-in"><a href="${ROOT}index.html">← Work</a><span class="sep">/</span><span>${document.body.dataset.title}</span></div>`
    : `<a class="logo fade-in" href="${ROOT}index.html">${SITE.name}</a>`;

  document.body.insertAdjacentHTML(
    "afterbegin",
    `<div class="sidebar"><div class="page-margin" style="height:100%"><div class="grid-12">
      <aside>
        ${top}
        <nav class="fade-in${isProject ? " toc" : ""}">${isProject ? tocLinks() : navLinks()}</nav>
      </aside>
    </div></div></div>`
  );

  document.querySelector(".content").insertAdjacentHTML(
    "afterbegin",
    `<nav class="mobile-nav fade-in">${navLinks()}</nav>`
  );

  document.querySelector(".shell .page-margin").insertAdjacentHTML(
    "beforeend",
    `<footer>
      <div class="status"><div class="dot"></div><p class="clock" aria-live="polite"></p></div>
      <div class="links">${SITE.socials
        .map(({ label, href }) => {
          const ext = href.startsWith("http") ? ' target="_blank" rel="noopener noreferrer"' : "";
          return `<a href="${href}"${ext}>${label}</a>`;
        })
        .join("")}</div>
    </footer>`
  );

  const clock = document.querySelector(".clock");
  const fmt = new Intl.DateTimeFormat("en-US", { timeZone: SITE.timezone, hour: "numeric", minute: "2-digit", second: "2-digit", timeZoneName: "short" });
  const tick = () => (clock.textContent = fmt.format(new Date()));
  tick();
  setInterval(tick, 1000);
}

function projectCard(p) {
  const media = p.media
    ? p.media.endsWith(".mp4")
      ? `<video src="${p.media}" autoplay muted loop playsinline></video>`
      : `<img src="${p.media}" alt="" loading="lazy">`
    : `<div class="placeholder" style="background:linear-gradient(135deg, ${p.colors[0]}, ${p.colors[1]})">${p.title}</div>`;

  const inner = `
    <div class="thumb" style="aspect-ratio:${p.ratio}" role="img" aria-label="Project thumbnail for ${p.title}">
      ${media}<div class="overlay"></div>
    </div>
    <div class="caption"><p class="title">${p.title}</p><p class="sep">/</p><p class="sub">${p.sub}</p></div>`;

  if (!p.href) return `<div class="project" data-cursor="coming-soon" data-label="${p.cursor}">${inner}</div>`;
  const ext = p.external ? ' target="_blank" rel="noopener noreferrer"' : "";
  return `<a class="project" href="${p.href}"${ext} data-label="${p.cursor}">${inner}</a>`;
}

function renderProjects() {
  const root = document.querySelector(".projects");
  if (!root) return;
  // Two independent columns give the staggered masonry look.
  const cols = [[], []];
  SITE.projects.forEach((p, i) => cols[i % 2].push(projectCard(p)));
  root.innerHTML = cols.map((c) => `<div class="column">${c.join("")}</div>`).join("");
}

function initCursorLabel() {
  const label = document.createElement("div");
  label.className = "cursor-label";
  document.body.appendChild(label);

  document.addEventListener("mousemove", (e) => {
    label.style.transform = `translate(${e.clientX + 14}px, ${e.clientY + 4}px)`;
    const target = e.target.closest("[data-label]");
    label.classList.toggle("visible", !!target);
    if (target) label.textContent = target.dataset.label;
  });
  document.addEventListener("mouseleave", () => label.classList.remove("visible"));
}

// Highlights the TOC entry for the last section whose top has passed 40% of the viewport.
function initScrollSpy() {
  const links = [...document.querySelectorAll("a[data-toc]")];
  if (!links.length) return;
  const targets = links.map((l) => document.getElementById(l.dataset.toc));

  const update = () => {
    const line = window.innerHeight * 0.4;
    let current = targets[0];
    for (const t of targets) if (t.getBoundingClientRect().top <= line) current = t;
    // The last sections may never reach the line, so activate the last one at the page bottom.
    if (window.innerHeight + window.scrollY >= document.documentElement.scrollHeight - 2) current = targets[targets.length - 1];
    links.forEach((l) => l.toggleAttribute("data-active", l.dataset.toc === current.id));
  };
  window.addEventListener("scroll", update, { passive: true });
  update();
}

renderChrome();
renderProjects();
initCursorLabel();
initScrollSpy();
