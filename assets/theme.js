function toggleTheme() {
    var currentTheme = document.documentElement.getAttribute("data-theme");
    if (currentTheme === "light") {
      targetTheme = "dark";
      targetclassName = "fa-regular fa-sun";
    } else {
      targetTheme = "light";
      targetclassName = "fa-regular fa-moon";
    }

    var toggle = document.getElementById("img-theme-toggle");
    toggle.className = targetclassName;

    document.documentElement.setAttribute('data-theme', targetTheme)
    localStorage.setItem('theme', targetTheme);
};
var storedTheme = localStorage.getItem('theme') || (window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light") || "light";
document.documentElement.setAttribute('data-theme', storedTheme)

document.addEventListener("DOMContentLoaded", function () {
    var toggle = document.getElementById("img-theme-toggle");
    var storedTheme = localStorage.getItem('theme') || (window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light") || "light";
    document.documentElement.setAttribute('data-theme', storedTheme)
    
    if (toggle) {
        if (storedTheme) {
            if (storedTheme === "dark") {
              toggle.className = "fa-regular fa-sun";
            }
            if (storedTheme === "light") {
              toggle.className = "fa-regular fa-moon";
            }
        }
    }
});
