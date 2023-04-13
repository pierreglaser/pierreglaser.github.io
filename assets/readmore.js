function myFunction(more_id) {
  var dots = document.getElementById("dots-"+more_id);
  var moreText = document.getElementById("more-"+more_id);
  var btnText = document.getElementById("myBtn-"+more_id);

  if (dots.style.display === "none") {
    dots.style.display = "inline";
    btnText.innerHTML = "Read more"; 
    moreText.style.display = "none";
  } else {
    dots.style.display = "none";
    btnText.innerHTML = "Read less"; 
    moreText.style.display = "inline";
  }
}
