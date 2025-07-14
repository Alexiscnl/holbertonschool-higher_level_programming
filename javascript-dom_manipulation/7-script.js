const element = document.querySelector("#list_movies");

fetch("https://swapi-api.hbtn.io/api/films/?format=json")
	.then(function(response) {
		return response.json();
	})
	.then(function(data) {
		data.results.forEach(function(film) {
			const newlist = document.createElement("li");
			newlist.textContent = film.title;
			element.appendChild(newlist);
		});
	})
