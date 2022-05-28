console.log("prject 4");

const name = document.getElementById("name");
const email = document.getElementById("email");
const phone = document.getElementById("phone");
let validName = false;
let validEmail = false;
let validPhone = false;
$('#failure').hide();
$('#success').hide();

// console.log(name, email, phone)

name.addEventListener("blur", () => {
  console.log("name is blurred");
  //validate name here
  let regex = /^[a-zA-Z]([0-9a-zA-Z]){2,10}$/;
  let str = name.value;
  console.log(regex, str);
  if (regex.test(str)) {
    console.log("Your name is valid");
    name.classList.remove("is-invalid");
    validName = true;
  } else {
    console.log("Your name is invalid");
    name.classList.add("is-invalid");
    validName = false;
  }
  
});
email.addEventListener("blur", () => {
  console.log("email is blurred");
  //validate email here
  let regex = /^([_\-\.0-9a-zA-z]+)@([_\-\.0-9a-zA-z]+)\.([a-zA-Z]){2,7}$/;
  let str = email.value;
  console.log(regex, str);
  if (regex.test(str)) {
    console.log("Your email is valid");
    email.classList.remove("is-invalid");
    validEmail = true;
  } else {
    console.log("Your email is invalid");
    email.classList.add("is-invalid");
    validEmail = false;
  }

});
phone.addEventListener("blur", () => {
  console.log("phone is blurred");
  //validate phone here
  let regex = /^([0-9]){10}$/;
  let str = phone.value;
  console.log(regex, str);
  if (regex.test(str)) {
    console.log("Your phone is valid");
    phone.classList.remove("is-invalid");
    validPhone = true;
  } else {
    console.log("Your phone is invalid");
    phone.classList.add("is-invalid");
    validPhone = false;
  }
});

let submit = document.getElementById("submit");
submit.addEventListener("click", (e) => {
  e.preventDefault();
  console.log("submit clicked");
  console.log(validName, validEmail, validPhone)

  if (validEmail && validName && validPhone) {
    let failure = document.getElementById("failure");

    console.log("phone, email and user are valid. submitted");
    let success = document.getElementById("success");
    success.classList.add("show");
    // failure.classList.remove("show");
    $('#success').show();
    $('#failure').hide();
  } else {
    console.log("phone, email and user are not valid. not submitting");
    let failure = document.getElementById("failure");
    failure.classList.add("show");
    // success.classList.remove("show");
    $('#failure').show();
    $('#success').hide();
  }
});
