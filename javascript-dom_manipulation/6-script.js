const element = document.querySelector("#character");

fetch("https://swapi-api.hbtn.io/api/people/5/?format=json")
	.then(function(response) {
		return response.json()
	})

	.then(function(data) {
		element.textContent = data.name;
	})
