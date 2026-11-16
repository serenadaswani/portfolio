// Mensio case study interactions. Every diagram is readable at rest; hover, focus or tap adds detail.
(() => {
  const $ = (s, r = document) => r.querySelector(s);
  const $$ = (s, r = document) => [...r.querySelectorAll(s)];
  const reduce = matchMedia("(prefers-reduced-motion: reduce)").matches;
  const pct = (r, W, H) => `left:${(r[0] / W) * 100}%;top:${(r[1] / H) * 100}%;width:${((r[2] - r[0]) / W) * 100}%;height:${((r[3] - r[1]) / H) * 100}%`;

  /* ---------- Before / after slider ---------- */
  $$(".mx-cmp").forEach((cmp) => {
    const f = $(".mx-cmp-frame", cmp), range = $(".mx-cmp-range", f), btns = $$(".mx-cmp-btn", cmp);
    const animated = [$(".mx-cmp-before", f), $(".mx-cmp-line", f)];
    const mark = (v) => btns.forEach((b) => b.setAttribute("aria-pressed", String(b.dataset.go === "100" ? v >= 75 : v <= 25)));
    const set = (v, ease) => {
      animated.forEach((el) => (el.style.transition = ease && !reduce ? "clip-path .6s cubic-bezier(.65,0,.35,1), left .6s cubic-bezier(.65,0,.35,1)" : ""));
      f.style.setProperty("--pos", v + "%");
      range.value = v;
      mark(v);
    };
    range.addEventListener("input", () => set(range.value, false));
    range.addEventListener("pointerdown", () => f.classList.add("is-dragging"));
    addEventListener("pointerup", () => f.classList.remove("is-dragging"));
    btns.forEach((b) => b.addEventListener("click", () => {
      const v = Number(b.dataset.go);
      set(Number(range.value) === v ? 50 : v, true); // clicking again returns to the split view
    }));
    if (!reduce) {
      const io = new IntersectionObserver((es) => {
        if (!es[0].isIntersecting) return;
        io.disconnect();
        [[0, 62], [550, 38], [1100, 50]].forEach(([t, v]) => setTimeout(() => { if (!f.classList.contains("is-dragging")) set(v, true); }, t));
      }, { threshold: 0.6 });
      io.observe(f);
    }
  });

  /* ---------- Request timeline ---------- */
  $$(".mx-tl").forEach((tl) => {
    const dots = $$(".mx-tl-svg .dot", tl), segs = $$(".seg", tl);
    const det = $(".mx-tl-detail", tl), n = $(".n", det), w = $(".w", det), t = $(".t", det), d = $(".d", det);
    const rest = [n.textContent, w.textContent, t.textContent, d.textContent];
    const show = (i) => {
      tl.classList.toggle("is-active", i >= 0);
      dots.forEach((x, j) => { x.classList.toggle("is-on", j === i); x.classList.toggle("is-done", i >= 0 && j < i); });
      segs.forEach((x, j) => x.classList.toggle("is-on", i >= 0 && j < i));
      if (i < 0) { [n.textContent, w.textContent, t.textContent, d.textContent] = rest; return; }
      const [who, label, desc] = tl.dataset["s" + i].split("|");
      n.textContent = i + 1; w.textContent = `Step ${i + 1} of 8 · ${who}`; t.textContent = label; d.textContent = desc;
    };
    dots.forEach((dot, i) => { dot.addEventListener("mouseenter", () => show(i)); dot.addEventListener("click", () => show(i)); });
    $(".mx-tl-svg", tl).addEventListener("mouseleave", () => show(-1));
    const btns = $$(".mx-tl-btn", tl);
    btns.forEach((b, i) => {
      b.addEventListener("focus", () => show(i));
      b.addEventListener("blur", () => show(-1));
      b.addEventListener("keydown", (e) => {
        if (e.key === "ArrowRight" || e.key === "ArrowDown") { e.preventDefault(); btns[Math.min(7, i + 1)].focus(); }
        if (e.key === "ArrowLeft" || e.key === "ArrowUp") { e.preventDefault(); btns[Math.max(0, i - 1)].focus(); }
      });
    });
    // vertical version: draw the path between dots from their real positions
    const ol = $(".mx-tlv-wrap", tl);
    const drawV = () => {
      if (!ol.offsetParent) return;
      const o = ol.getBoundingClientRect();
      const c = $$(".mx-tlv-dot", ol).map((e) => { const r = e.getBoundingClientRect(); return [r.left - o.left + r.width / 2, r.top - o.top + r.height / 2]; });
      let path = "";
      for (let i = 0; i < c.length - 1; i++) { const [ax, ay] = c[i], [bx, by] = c[i + 1], k = (by - ay) * 0.55; path += `M${ax},${ay} C${ax},${ay + k} ${bx},${by - k} ${bx},${by} `; }
      const h = o.height;
      $(".mx-tlv-svg", ol).innerHTML = `<g class="lanes">${[18, 56, 94].map((x) => `<line x1="${x}" x2="${x}" y1="0" y2="${h}"/>`).join("")}</g><path d="${path}"/>`;
    };
    drawV(); addEventListener("resize", drawV); document.fonts && document.fonts.ready.then(drawV);
  });

  /* ---------- Stakeholders' vision: a six-step wizard that steps itself ---------- */
  $$(".mx-wiz").forEach((wz) => {
    const steps = $$(".steps li", wz), panes = $$(".pane", wz), fill = $(".fill", wz), next = $(".next", wz);
    const N = steps.length, HOLD = 1900;
    let i = 0, timers = [], running = false;
    const later = (fn, t) => timers.push(setTimeout(fn, t));
    const render = () => {
      wz.dataset.step = i;
      steps.forEach((s, k) => { s.classList.toggle("is-done", k < i); s.classList.toggle("is-current", k === i); });
      panes.forEach((p, k) => { p.classList.toggle("is-on", k === i); p.classList.toggle("is-past", k < i); });
      fill.style.setProperty("--p", i / (N - 1));
    };
    const press = () => { next.classList.add("is-press"); later(() => next.classList.remove("is-press"), 160); };
    const cycle = () => {
      if (!running) return;
      later(() => {
        press();
        later(() => {
          if (i < N - 1) { i++; render(); cycle(); return; }
          steps.forEach((s) => { s.classList.add("is-done"); s.classList.remove("is-current"); });
          fill.style.setProperty("--p", 1);
          wz.classList.add("is-done");
          later(() => { wz.classList.remove("is-done"); i = 0; render(); cycle(); }, 1600);
        }, 200);
      }, HOLD);
    };
    render();
    if (reduce) { i = 2; render(); return; }
    new IntersectionObserver((es) => {
      const vis = es[0].isIntersecting;
      if (vis && !running) { running = true; cycle(); }
      if (!vis && running) { running = false; timers.forEach(clearTimeout); timers = []; }
    }, { threshold: 0.35 }).observe(wz);
  });

  /* ---------- Bento progression: segments fill one after another, then loop ---------- */
  $$(".mx-seg-steps").forEach((ol) => {
    const items = $$("li", ol), SEG = 1600;
    ol.style.setProperty("--seg", SEG + "ms");
    if (reduce) { items.forEach((li) => li.classList.add("is-done")); return; }
    let i = 0, t = null, running = false;
    const show = () => {
      items.forEach((li, k) => { li.classList.toggle("is-done", k < i); li.classList.remove("is-on"); });
      const cur = items[i]; void cur.offsetWidth; cur.classList.add("is-on");
    };
    const tick = () => {
      if (!running) return;
      show();
      t = setTimeout(() => {
        if (i < items.length - 1) { i++; tick(); }
        else { items[i].classList.add("is-done"); t = setTimeout(() => { i = 0; tick(); }, 1400); }
      }, SEG);
    };
    new IntersectionObserver((es) => {
      const vis = es[0].isIntersecting;
      if (vis && !running) { running = true; tick(); }
      if (!vis && running) { running = false; clearTimeout(t); }
    }, { threshold: 0.4 }).observe(ol);
  });

  /* ---------- Sticky-note affinity map: click a note to bring it forward ---------- */
  $$(".mx-stack").forEach((stack) => {
    const notes = $$(".mx-sn", stack);
    let z = notes.length;
    notes.forEach((n) => n.addEventListener("click", () => {
      notes.forEach((x) => x.classList.remove("is-front"));
      n.style.zIndex = ++z;
      n.classList.add("is-front");
    }));
  });

  /* ---------- Customer map: tooltip sits right next to the dot it describes ---------- */
  const map = $(".mx-map");
  if (map) {
    const plot = $(".mx-map-plot", map), dots = $$(".mx-dot", map), card = $(".mx-dot-card", map);
    const on = (i) => {
      dots.forEach((d, j) => d.classList.toggle("is-on", j === i));
      if (i < 0) return card.classList.remove("is-on");
      const d = dots[i];
      card.innerHTML = `<b>${d.dataset.who}</b>${d.dataset.desc}`;
      const pw = plot.clientWidth, ph = plot.clientHeight, cw = card.offsetWidth, ch = card.offsetHeight;
      const dx = d.offsetLeft, dy = d.offsetTop;              // dot centre, in plot coordinates
      // each dot has a side chosen so its card never covers a neighbouring label
      const clamp = (v, lo, hi) => Math.min(Math.max(v, lo), hi);
      let side = d.dataset.place, x, y;
      if (side === "left" && dx - 18 - cw < 6) side = "above";      // narrow plots: fall back to above
      if (side === "left") { x = dx - 18 - cw; y = clamp(dy - ch / 2, 6, ph - ch - 6); card.style.setProperty("--ay", clamp(dy - y, 12, ch - 12) + "px"); }
      else { x = clamp(dx - 22, 6, pw - cw - 6); y = dy - 18 - ch; if (y < 6) { y = dy + 30; side = "below"; } card.style.setProperty("--ax", clamp(dx - x, 14, cw - 14) + "px"); }
      card.style.left = x + "px"; card.style.top = y + "px";
      card.dataset.side = side;
      card.classList.add("is-on");
    };
    dots.forEach((d, i) => {
      d.addEventListener("mouseenter", () => on(i)); d.addEventListener("mouseleave", () => on(-1));
      d.addEventListener("focus", () => on(i)); d.addEventListener("blur", () => on(-1));
    });
  }

  /* ---------- Exploration wireframes: hover shows what it became ---------- */
  $$(".explore-panel").forEach((p) => {
    const card = $(".panel-card", p);
    card.tabIndex = 0;
    card.setAttribute("role", "button");
    card.setAttribute("aria-label", "Show what this became");
    card.addEventListener("mouseenter", () => p.classList.add("is-after"));
    card.addEventListener("mouseleave", () => p.classList.remove("is-after"));
    card.addEventListener("click", () => p.classList.toggle("is-after"));
    card.addEventListener("keydown", (e) => { if (e.key === "Enter" || e.key === " ") { e.preventDefault(); p.classList.toggle("is-after"); } });
  });

  const fit = () => $$(".mx-wf").forEach((w) => { w.style.transform = `scale(${w.parentElement.clientWidth / 380})`; });
  fit(); addEventListener("resize", fit);

  /* ---------- Solution flow: step detail ---------- */
  $$(".mx-flow2").forEach((f) => {
    const det = f.parentElement.querySelector(".mx-detail");
    const steps = $$(".mx-step", f);
    const show = (s) => {
      steps.forEach((x) => x.classList.toggle("is-on", x === s));
      $(".n", det).textContent = s.dataset.n;
      $(".t", det).textContent = s.dataset.t;
      $(".d", det).textContent = s.dataset.d;
    };
    steps.forEach((s) => { s.addEventListener("mouseenter", () => show(s)); s.addEventListener("focus", () => show(s)); s.addEventListener("click", () => show(s)); });
  });

  /* ---------- Screen tour: zoom into each part of the UI ---------- */
  $$(".mx-tour").forEach((tour) => {
    const frame = $(".mx-tour-frame", tour), layer = $(".mx-tour-layer", tour);
    const tabs = $$(".mx-ind", tour), imgs = $$("img", layer), ring = $(".mx-ring", layer);
    const head = $(".mx-tour-head", tour);
    const W = 1440, H = 1024, DUR = 4800;
    let i = 0, timer = null, paused = false;
    const zoom = (r) => {
      const fw = frame.clientWidth, fh = frame.clientHeight, base = fw / W;
      if (!r) return (layer.style.transform = "none");
      const rw = r[2] - r[0], rh = r[3] - r[1];
      let s = Math.min((fw * 0.86) / (rw * base), (fh * 0.8) / (rh * base));
      s = Math.max(1, Math.min(s, 2.1));
      const cx = ((r[0] + rw / 2) * base) * s, cy = ((r[1] + rh / 2) * base) * s;
      let tx = fw / 2 - cx, ty = fh / 2 - cy;
      tx = Math.min(0, Math.max(fw - fw * s, tx));
      ty = Math.min(0, Math.max(fh - (H * base) * s, ty));
      layer.style.transform = `translate(${tx}px,${ty}px) scale(${s})`;
    };
    const go = (k, user) => {
      i = (k + tabs.length) % tabs.length;
      const t = tabs[i], r = t.dataset.r.split(",").map(Number);
      tabs.forEach((b, j) => { b.setAttribute("aria-selected", String(j === i)); b.classList.toggle("is-done", j < i); });
      if (user) t.scrollIntoView({ block: "nearest", inline: "nearest", behavior: reduce ? "auto" : "smooth" });
      head.children[0].textContent = t.dataset.t;
      head.children[1].textContent = t.dataset.d;
      ring.classList.remove("is-on");
      zoom(null);
      setTimeout(() => {
        imgs.forEach((im) => im.classList.toggle("is-on", im.dataset.k === t.dataset.img));
        ring.style.cssText = pct(r, W, H);
        setTimeout(() => { zoom(r); setTimeout(() => ring.classList.add("is-on"), 700); }, reduce ? 0 : 380);
      }, reduce ? 0 : 450);
      clearTimeout(timer);
      if (!paused && !reduce) timer = setTimeout(() => go(i + 1), DUR);
      // restart progress bar
      const bar = t.querySelector(".trk i"); bar.style.animation = "none"; void bar.offsetWidth; bar.style.animation = "";
    };
    tabs.forEach((t, k) => t.addEventListener("click", () => go(k, true)));
    tour.addEventListener("mouseenter", () => { paused = true; tour.classList.add("is-paused"); clearTimeout(timer); });
    tour.addEventListener("mouseleave", () => { paused = false; tour.classList.remove("is-paused"); timer = setTimeout(() => go(i + 1), 1800); });
    addEventListener("resize", () => zoom(tabs[i].dataset.r.split(",").map(Number)));
    tour.style.setProperty("--mx-dur", DUR + "ms");
    // start when visible
    const io = new IntersectionObserver((es) => { if (es[0].isIntersecting) { go(0); io.disconnect(); } }, { threshold: 0.35 });
    io.observe(tour);
    imgs[0].classList.add("is-on");
  });

  /* ---------- Charts with hover tooltips (illustrative data) ---------- */
  const tipFor = (box) => { let t = $(".mx-tipbox", box); if (!t) { t = document.createElement("div"); t.className = "mx-tipbox"; box.appendChild(t); } return t; };
  const rnd = (seed) => () => ((seed = (seed * 16807) % 2147483647) / 2147483647);

  const sc = $("#mx-scatter");
  if (sc) {
    const BR = [["Ford", "#1089f5", 210, 62], ["Toyota", "#00ad7f", 150, 44], ["Chevrolet", "#a86cdc", 95, 30], ["Honda", "#e0a63a", 300, 78], ["Nissan", "#e57373", 60, 22]];
    const r = rnd(11), pts = [];
    BR.forEach(([n, c, bx, by]) => { for (let k = 0; k < 4; k++) { const d = bx * (0.7 + r() * 0.6), e = by * (0.75 + r() * 0.5); pts.push({ n, c, d, e, v: d * e / 40, ep: k + 1 }); } });
    const w = 320, h = 190, x0 = 34, y1 = 166, x1 = 312, y0 = 8;
    const sx = (d) => x0 + d / 420 * (x1 - x0), sy = (e) => y1 - e / 100 * (y1 - y0);
    let s = `<svg viewBox="0 0 ${w} ${h + 16}">`;
    for (let e = 0; e <= 100; e += 25) s += `<line class="grid" x1="${x0}" x2="${x1}" y1="${sy(e)}" y2="${sy(e)}"/><text class="axis" x="${x0 - 6}" y="${sy(e) + 3}" text-anchor="end">${e}%</text>`;
    for (let d = 0; d <= 420; d += 120) s += `<text class="axis" x="${sx(d)}" y="${y1 + 13}" text-anchor="middle">${d / 60}:00</text>`;
    s += `<text class="axis" x="${(x0 + x1) / 2}" y="${y1 + 27}" text-anchor="middle">Duration (MM:SS) → Avg. equivalency ↑</text>`;
    pts.sort((a, b) => b.v - a.v).forEach((p) => {
      const mm = Math.floor(p.d / 60), ss = String(Math.round(p.d % 60)).padStart(2, "0");
      s += `<circle class="pt" data-n="${p.n}" data-tip="<b>${p.n}</b> · Episode ${p.ep}<br>${mm}:${ss} on screen · ${Math.round(p.e)}% equivalency" cx="${sx(p.d).toFixed(1)}" cy="${sy(p.e).toFixed(1)}" r="${(2.5 + Math.sqrt(p.v) * 0.42).toFixed(1)}" fill="${p.c}" fill-opacity=".85" stroke="#fff" stroke-width="1.2"/>`;
    });
    sc.querySelector(".plot").innerHTML = s + "</svg>";
    sc.querySelector(".mx-legend").innerHTML = BR.map(([n, c]) => `<button type="button" data-n="${n}"><span style="background:${c}"></span>${n}</button>`).join("");
  }

  const hm = $("#mx-heatmap");
  if (hm) {
    const brands = ["Capital One", "Ford", "Toyota", "Chevrolet", "Honda"], assets = ["Jersey", "Helmet", "Signage", "Scoreboard", "Overlay"];
    const r = rnd(5), vals = brands.map(() => assets.map(() => Math.round(Math.pow(r(), 1.5) * 900 + 15)));
    vals[0][2] = 1240; vals[1][4] = 980; vals[3][0] = 860;
    const mx = Math.max(...vals.flat());
    const ramp = ["#eff6ff", "#dbeafe", "#bfdbfe", "#93c5fd", "#60a5fa", "#3b82f6", "#2563eb", "#1d4ed8", "#1e40af"];
    const col = (v) => ramp[Math.min(8, Math.round((v / mx) * 8))];
    const L = 62, T = 4, cw = 50, ch = 30;
    let s = `<svg viewBox="0 0 ${L + cw * 5 + 4} ${T + ch * 5 + 20}">`;
    brands.forEach((b, i) => {
      s += `<text class="axis" x="${L - 6}" y="${T + i * ch + ch / 2 + 3}" text-anchor="end">${b}</text>`;
      assets.forEach((a, j) => {
        const v = vals[i][j], c = col(v), dark = ramp.indexOf(c) >= 5;
        s += `<g class="cell" data-tip="<b>${b}</b> · ${a}<br>${v.toLocaleString()} visual occurrences"><rect x="${L + j * cw}" y="${T + i * ch}" width="${cw - 2}" height="${ch - 2}" rx="3" fill="${c}"/><text x="${L + j * cw + (cw - 2) / 2}" y="${T + i * ch + ch / 2 + 3}" text-anchor="middle" font-size="9.5" font-family="Inter, sans-serif" fill="${dark ? "#fff" : "#334155"}">${v.toLocaleString()}</text></g>`;
      });
    });
    assets.forEach((a, j) => (s += `<text class="axis" x="${L + j * cw + (cw - 2) / 2}" y="${T + 5 * ch + 12}" text-anchor="middle">${a}</text>`));
    hm.querySelector(".plot").innerHTML = s + "</svg>";
  }

  $$(".mx-chart").forEach((box) => {
    const tip = tipFor(box);
    box.addEventListener("pointermove", (e) => {
      if (e.target.closest(".mx-legend")) return;
      const el = e.target.closest("[data-tip]");
      $$(".is-on", box).forEach((x) => x !== el && x.classList.remove("is-on"));
      if (!el) { tip.classList.remove("is-on"); box.classList.remove("dim"); return; }
      const o = box.getBoundingClientRect(), r = el.getBoundingClientRect();
      tip.innerHTML = el.dataset.tip;
      tip.style.left = `${r.left - o.left + r.width / 2}px`;
      tip.style.top = `${r.top - o.top}px`;
      tip.classList.add("is-on");
      el.classList.add("is-on");
      box.classList.add("dim");
    });
    box.addEventListener("pointerleave", () => { tip.classList.remove("is-on"); box.classList.remove("dim"); $$(".is-on", box).forEach((x) => x.classList.remove("is-on")); });
    $$(".mx-legend", box).forEach((lg) => {
      lg.addEventListener("pointerover", (e) => {
        const b = e.target.closest("button"); if (!b) return;
        box.classList.add("dim");
        $$(".pt", box).forEach((p) => p.classList.toggle("is-on", p.dataset.n === b.dataset.n));
      });
      lg.addEventListener("pointerleave", () => { box.classList.remove("dim"); $$(".pt", box).forEach((p) => p.classList.remove("is-on")); });
    });
  });

  /* ---------- Side contents list fades in at the Overview section, out again above it ---------- */
  const toc = $(".sidebar nav.toc"), hero = $(".project-hero"), ov = $("#overview");
  if (toc && ov) {
    const check = () => {
      const show = ov.getBoundingClientRect().top < innerHeight * 0.75 && (!hero || hero.getBoundingClientRect().bottom < toc.getBoundingClientRect().top);
      toc.classList.toggle("is-hidden", !show);
    };
    check();
    addEventListener("scroll", check, { passive: true });
    addEventListener("resize", check);
  }
})();
