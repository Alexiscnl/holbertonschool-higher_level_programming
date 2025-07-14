const element = document.querySelector("#red_header");
const header = document.querySelector("header");

element.addEventListener("click", function() {
	header.classList.add("red")
})
