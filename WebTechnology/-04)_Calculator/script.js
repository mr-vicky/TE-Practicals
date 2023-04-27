var display = document.getElementById("display");
var buttons = document.getElementsByTagName("button");

for (var i = 0; i < buttons.length; i++) {
	buttons[i].addEventListener("click", function() {
		var buttonValue = this.innerHTML;

		if (buttonValue == "C") {
			display.value = "";
		} else if (buttonValue == "=") {
			display.value = eval(display.value);
		} else {
			display.value += buttonValue;
		}
	});
}
