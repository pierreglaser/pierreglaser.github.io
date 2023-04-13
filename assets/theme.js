function toggleTheme() {
    console.log("toggle theme clicked");
    var currentTheme = document.documentElement.getAttribute("data-theme");
    if (currentTheme === "light") {
      targetTheme = "dark";
      targetclassName = "fa-regular fa-moon";
      console.log("dark");
    } else {
      targetTheme = "light";
      targetclassName = "fa-regular fa-sun";
      console.log("light");
    }

    toggle.className = targetclassName;

    document.documentElement.setAttribute('data-theme', targetTheme)
    localStorage.setItem('theme', targetTheme);
};
