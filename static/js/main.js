// get  to-up-btn
const toUpBtn = document.querySelector("#to-up-btn");

// show  to-up-btn
window.addEventListener("scroll", () => {
this.scrollY >= 1000
? toUpBtn.classList.add("show")
: toUpBtn.classList.remove("show");
});

// add event to the to-up-btn
toUpBtn.addEventListener("click", () => {
window.scrollTo({
top: 0,
behavior: "smooth",
});
});


function openNav() {
    document.getElementById("mySidenav").style.width = "250px";
  }
  
function closeNav() {
document.getElementById("mySidenav").style.width = "0";
}

