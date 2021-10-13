
window.addEventListener('load', () => {

	const alertDiv = document.getElementsByClassName('alert')[0];
	console.log(alertDiv);
	if (alertDiv) {
		console.log(alertDiv);
		if (alertDiv.textContent.includes("Account is created for")) {
			console.log(1);
			alertDiv.style.color = "#64ff64";
		}
		else {
			console.log(2);
			alertDiv.style.color = "red";
		}
	}
	// ......

	let passField = document.getElementById('togglePassword');
	let inputPass = document.getElementById('password');

	passField.addEventListener('click', function () {

		if (passField.innerText != "visibility") {

			passField.innerText = "visibility";
			inputPass.type = "text";
		} else {

			passField.innerText = "visibility_off";
			inputPass.type = "password";
		}

	})

	document.getElementById('loginBtn').addEventListener('click', function () {
		passField.innerText = "visibility_off";
		inputPass.type = "password";
	});

	// ...
	document.getElementById("username").focus();
});