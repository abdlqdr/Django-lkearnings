console.log("project");


// Constructor
function Book(name, author, type) {
  this.name = name;
  this.author = author;
  this.type = type;
}

// Display Constructor
function Display() {}

// Add method to display prototype
Display.prototype.add = function (book) {
  let tableData = localStorage.getItem("tableData"); //assigning key name in the storage
  if (tableData == null) {
    bookObj = []; //empty array  if nothing inserted
  } else {
    bookObj = JSON.parse(tableData); //this is the element of array
  }
  console.log("add to ui");
  let tableBody = document.getElementById("tableBody");
  let uiSrting = "";
  bookObj.forEach(function (book) {
    uiSrting += `<tr>
                          <td>${book.name}</td>
                          <td>${book.author}</td>
                          <td>${book.type}</td>
                          <td><button  class="btn btn-primary">X</button></td>
                      </tr>`;
  });

  // tableBody.innerHTML += uiSrting;

  if (tableBody.length != 0) {
    tableBody.innerHTML = uiSrting;
  }
  
};

// Implementing clear function
Display.prototype.clear = function () {
  let libraryForm = document.getElementById("libraryForm");
  libraryForm.reset();
};

// Implementing validate function
Display.prototype.validate = function (book) {
  if (book.name.length < 2 || book.author.length < 2) {
    return false;
  } else {
    return true;
  }
};

Display.prototype.show = function (type, displayMessage) {
  let message = document.getElementById("message");
  let boldText;
  if (type === "Success") {
    boldText = "Sucess";
  } else {
    boldText = "Error";
  }
  message.innerHTML = ` <div class="alert alert-${type} alert-dismissible fade show" role="alert">
                              <strong>${boldText}:</strong>${displayMessage}
                              <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
                              <span aria-hidden='true'>&times;</span>
                          </div>`;
  setTimeout(function () {
    message.innerHTML = "";
  }, 2000);
};

// // Add submit event listener to libraryForm
let libraryForm = document.getElementById("libraryForm");
libraryForm.addEventListener("submit", libraryFormSubmit);

function libraryFormSubmit(e) {
  console.log("you have submitted library form");
  let name = document.getElementById("bookName").value;
  let author = document.getElementById("author").value;

  let Fiction = document.getElementById("Fiction");
  let Programming = document.getElementById("Programming");
  let Cooking = document.getElementById("Cooking");
  let type = document.getElementsByName("type").value;

  if (Fiction.checked) {
    type = Fiction.value;
  } else if (Programming.checked) {
    type = Programming.value;
  } else if (Cooking.checked) {
    type = Cooking.value;
  }

  let tableData = localStorage.getItem("tableData"); //assigning key name in the storage
  if (tableData == null) {
    bookObj = []; //empty array  if nothing inserted
  } else {
    bookObj = JSON.parse(tableData); //this is the element of array
  }
  let myObj = {
    name: name,
    author: author,
    type: type,
  };
  bookObj.push(myObj); // it is used to push words in notesObj(array element) from text area to local storage
  localStorage.setItem("tableData", JSON.stringify(bookObj));

  let book = new Book(name, author, type);
  console.log(book);

  let display = new Display();

  if (display.validate(book)) {
    display.add(book);
    display.clear();
    display.show("Success", " Your book is successfully added");
  } else {
    // show error to the user
    display.show("Danger", " sorry you cannot add this book");
  }

  e.preventDefault();
}
