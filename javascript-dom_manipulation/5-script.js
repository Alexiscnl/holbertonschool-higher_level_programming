const element = document.querySelector("#update_header");
const header = document.querySelector("header");

element.addEventListener("click", function() {
	header.textContent = "New header!!!";
})
