// Smart Click Media — site interactions
(function () {
  var WA_NUMBER = "263771269979";
  var EMAIL = "info@smartclick.co.zw";
  var MOBILE = "(max-width: 1020px)";

  function track(name, params) {
    if (typeof window.gtag === "function") window.gtag("event", name, params || {});
  }

  // Mobile menu
  var header = document.querySelector(".site-header");
  var toggle = document.querySelector(".menu-toggle");
  if (toggle && header) {
    toggle.addEventListener("click", function () {
      var open = header.classList.toggle("nav-open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
      toggle.setAttribute("aria-label", open ? "Close menu" : "Open menu");
    });
  }
  // Dropdowns open on first tap on small screens
  document.querySelectorAll(".has-mega > a").forEach(function (link) {
    link.addEventListener("click", function (e) {
      if (window.matchMedia(MOBILE).matches) {
        var li = link.parentElement;
        if (!li.classList.contains("open")) {
          e.preventDefault();
          li.classList.add("open");
        }
      }
    });
  });

  // Reveal on scroll (the html.js class is added in <head>, so content is visible without JavaScript)
  var items = document.querySelectorAll(".reveal");
  if ("IntersectionObserver" in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add("in"); io.unobserve(en.target); }
      });
    }, { threshold: 0.08, rootMargin: "0px 0px -40px 0px" });
    items.forEach(function (el) { io.observe(el); });
  } else {
    items.forEach(function (el) { el.classList.add("in"); });
  }

  // Footer year
  var y = document.getElementById("year");
  if (y) y.textContent = new Date().getFullYear();

  // Analytics events for contact clicks (only fire if Google Analytics is switched on)
  document.addEventListener("click", function (e) {
    var a = e.target.closest ? e.target.closest("a[href]") : null;
    if (!a) return;
    var href = a.getAttribute("href");
    if (href.indexOf("https://wa.me/") === 0) track("whatsapp_click", { link_url: href });
    else if (href.indexOf("tel:") === 0) track("phone_click", { link_url: href });
    else if (href.indexOf("mailto:") === 0) track("email_click", { link_url: href });
  });

  // Contact form: opens WhatsApp or email with the details filled in (no server needed)
  document.querySelectorAll("form[data-contact-form]").forEach(function (form) {
    var channel = "whatsapp";
    form.querySelectorAll('button[type="submit"]').forEach(function (b) {
      b.addEventListener("click", function () { channel = b.value || "whatsapp"; });
    });
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var firstBad = null;
      form.querySelectorAll("[required]").forEach(function (f) {
        var bad = !f.value.trim() || (f.type === "email" && f.value && !/^\S+@\S+\.\S+$/.test(f.value));
        f.setAttribute("aria-invalid", bad ? "true" : "false");
        if (bad && !firstBad) firstBad = f;
      });
      var email = form.querySelector('input[type="email"]');
      if (email && email.value && !/^\S+@\S+\.\S+$/.test(email.value)) {
        email.setAttribute("aria-invalid", "true");
        if (!firstBad) firstBad = email;
      }
      if (firstBad) { firstBad.focus(); if (form.reportValidity) form.reportValidity(); return; }

      var data = new FormData(form);
      var lines = ["Hi Smart Click Media, I'd like to enquire about your services."];
      data.forEach(function (value, key) {
        if (key === "services" || !String(value).trim()) return;
        var field = form.querySelector('[name="' + key + '"]');
        lines.push((field && field.dataset.label ? field.dataset.label : key) + ": " + value);
      });
      var services = data.getAll("services");
      if (services.length) lines.push("Services: " + services.join(", "));
      var text = lines.join("\n");
      var url = channel === "email"
        ? "mailto:" + EMAIL + "?subject=" + encodeURIComponent("Website enquiry") + "&body=" + encodeURIComponent(text)
        : "https://wa.me/" + WA_NUMBER + "?text=" + encodeURIComponent(text);
      track("generate_lead", { method: channel });
      if (channel === "email") window.location.href = url;
      else window.open(url, "_blank", "noopener");
      var ok = form.querySelector(".form-success");
      if (ok) ok.hidden = false;
    });
  });
})();
