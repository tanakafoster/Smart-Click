// Smart Click Media — site interactions
(function () {
  var WA_NUMBER = "263771269979";

  // Mobile menu
  var header = document.querySelector(".site-header");
  var toggle = document.querySelector(".menu-toggle");
  if (toggle && header) {
    toggle.addEventListener("click", function () {
      var open = header.classList.toggle("nav-open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
    });
  }
  // Services dropdown on touch / small screens
  document.querySelectorAll(".has-mega > a").forEach(function (link) {
    link.addEventListener("click", function (e) {
      if (window.matchMedia("(max-width: 960px)").matches) {
        var li = link.parentElement;
        if (!li.classList.contains("open")) {
          e.preventDefault();
          li.classList.add("open");
        }
      }
    });
  });

  // Reveal on scroll
  var items = document.querySelectorAll(".reveal");
  if ("IntersectionObserver" in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add("in"); io.unobserve(en.target); }
      });
    }, { threshold: 0.12 });
    items.forEach(function (el) { io.observe(el); });
  } else {
    items.forEach(function (el) { el.classList.add("in"); });
  }

  // Footer year
  var y = document.getElementById("year");
  if (y) y.textContent = new Date().getFullYear();

  // Contact / audit forms send the enquiry to WhatsApp (no server needed)
  document.querySelectorAll("form[data-wa-form]").forEach(function (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      if (!form.reportValidity()) return;
      var data = new FormData(form);
      var lines = ["Hi Smart Click Media, I'd like to enquire about your services."];
      var services = data.getAll("services");
      data.forEach(function (value, key) {
        if (key === "services" || !String(value).trim()) return;
        var label = form.querySelector('[name="' + key + '"]');
        var name = label && label.dataset.label ? label.dataset.label : key;
        lines.push(name + ": " + value);
      });
      if (services.length) lines.push("Services: " + services.join(", "));
      var url = "https://wa.me/" + WA_NUMBER + "?text=" + encodeURIComponent(lines.join("\n"));
      window.open(url, "_blank", "noopener");
      var ok = form.querySelector(".form-success");
      if (ok) ok.hidden = false;
    });
  });
})();
