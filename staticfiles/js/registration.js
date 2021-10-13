window.addEventListener('load', () => {

    const input1 = document.querySelectorAll(".inputbox1 > div > input");
    const input = document.querySelectorAll(".inputbox > input");
    const firstName = document.querySelector(".inputbox1 > .first > input")
    const userName = document.getElementById('id_username');
    console.log(input, input1)

    Array.from(input).forEach((ele) => {
        if (ele.getAttribute('name') != 'password1') {
            ele.setAttribute("required", "");
        }
    });

    Array.from(input1).forEach((ele) => {
        ele.setAttribute("required", "");
    });
    console.log(firstName);
    userName.removeAttribute("autofocus");
    firstName.focus();

    document.getElementById('id_first_name').placeholder = 'Enter First Name';
    document.getElementById('id_last_name').placeholder = 'Enter Last Name';
    document.getElementById('id_username').placeholder = 'Enter Userame';
    document.getElementById('id_email').placeholder = 'Enter Email';
    document.getElementById('id_password1').placeholder = 'Enter Password';
    document.getElementById('id_password2').placeholder = 'Re-enter Password';

    // .....


    let passField = document.getElementById('regsPassword');
    let passField2 = document.getElementById('regsPassword2');
    let inputPass = document.getElementById('id_password1');
    let inputPass2 = document.getElementById('id_password2');
    
    passField.addEventListener('click', function () {

        if (passField.innerText != "visibility") {

            passField.innerText = "visibility";
            inputPass.type = "text";
        } else {

            passField.innerText = "visibility_off";
            inputPass.type = "password";
        }

    })

    passField2.addEventListener('click', function () {

        if (passField2.innerText != "visibility") {

            passField2.innerText = "visibility";
            inputPass2.type = "text";
        } else {

            passField2.innerText = "visibility_off";
            inputPass2.type = "password";
        }

    })

    document.getElementById('loginBtn').addEventListener('click', function () {
        passField.innerText = "visibility_off";
        inputPass.type = "password";
        passField2.innerText = "visibility_off";
        inputPass2.type = "password";
    });
});