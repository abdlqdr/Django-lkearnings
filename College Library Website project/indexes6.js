class Book {
  constructor(name, author, type) {
    this.name = name;
    this.author = author;
    this.type = type;
  }
}

class Display {
  add(book) {
    console.log("add to ui");
    let tableBody = document.getElementById("tableBody");
    let uiSrting = `<tr>
                              <td>${book.name}</td>
                              <td>${book.author}</td>
                              <td>@${book.type}</td>
                          </tr>`;
    tableBody.innerHTML += uiSrting;
  }

  clear() {
    let libraryForm = document.getElementById("libraryForm");
    libraryForm.reset();
  }

  validate(book) {
    if (book.name.length < 2 || book.author.length < 2) {
      return false;
    } else {
      return true;
    }
  };

  show(type, displayMessage) {
    let message = document.getElementById("message");
    let boldText;
    if (type === 'Success'){
        boldText = 'Sucess';
    }
    else{
        boldText = 'Error';
    }
    message.innerHTML = ` <div class="alert alert-${type} alert-dismissible fade show" role="alert">
                              <strong>${boldText}:</strong>${displayMessage}
                              <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
                              <span aria-hidden='true'>&times;</span>
                          </div>`;
      setTimeout(function() {
          message.innerHTML = '';
      }, 5000);               
  };
}

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
  let type;

  if (Fiction.checked) {
    type = Fiction.value;
  } else if (Programming.checked) {
    type = Programming.value;
  } else if (Cooking.checked) {
    type = Cooking.value;
  }


  let book = new Book(name, author, type);
  console.log(book);

  let display = new Display();

  if (display.validate(book)) {
    display.add(book);
    display.clear();
    display.show('Success', ' Your book is successfully added');
  } else {
    // show error to the user
    display.show('danger', ' Sorry you cannot add this book');
  }

  e.preventDefault();
}

