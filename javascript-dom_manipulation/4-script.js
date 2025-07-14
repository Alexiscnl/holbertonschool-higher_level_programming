const element = document.querySelector("#add_item");
const mylist = document.querySelector(".my_list")

element.addEventListener("click", function() {
	const newItem = document.createElement("li");
	newItem.textContent = "Item";
	mylist.appendChild(newItem)
})
