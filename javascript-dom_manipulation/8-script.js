document.addEventListener("DOMContentLoaded", function(){
const element = document.querySelector("#hello")

fetch("https://hellosalut.stefanbohacek.dev/?lang=fr")
	.then(function(response) {
		return response.json();
	})
	.then(function(data) {
		element.textContent = data.hello;
	})
});
