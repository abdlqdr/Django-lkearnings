console.log("how are you");

showNotes();
// if user adds a note, add it to the localStorage
let addBtn = document.getElementById("addBtn");
addBtn.addEventListener("click", function (e) {
  let addTxt = document.getElementById("addTxt");   // targetting note text area in a variable
  let addTitle = document.getElementById("addTitle");   // targetting title text area in a variable
  let notes = localStorage.getItem("notes");    //assigning key name in the storage
  if (notes == null) {
    notesObj = [];  //empty array  if nothing inserted
  } else {
    notesObj = JSON.parse(notes); //this is the element of array
  }
  let myObj = {
    title: addTitle.value,
    text: addTxt.value
  }
  notesObj.push(myObj);    // it is used to push words in notesObj(array element) from text area to local storage
  localStorage.setItem("notes", JSON.stringify(notesObj));  //defining value to insert items in notesObj(array element) 
  addTxt.value = "";    // to set note text area empty after adding note  
  addTitle.value = "";     // to set title text area empty after adding note
  showNotes();    // it displays the added notes
});

//Function to show elements from localStorage
function showNotes() {
  let notes = localStorage.getItem("notes");    //assigning key name in the storage
  if (notes == null) {
    notesObj = [];
  } else {
    notesObj = JSON.parse(notes);
  }
  let html = "";    // defining an empty html
  notesObj.forEach(function (element, index) {              //inserting dynamic html 
    html += `<div class="noteCard my-2 mx-2 card" style="width: 18rem;">
                <div class="card-body">
                    <h5 class="card-title">${element.title}</h5>
                    <p class="card-text">${element.text}</p>
                    <button id="${index}" onclick="deleteNote(this.id)" class="btn btn-primary">Delete Note</button>
                </div>
            </div>`;
  });

  // To display notes if any inserted 
  let notesElem = document.getElementById('notes');
  if(notesObj.length != 0){
      notesElem.innerHTML = html;
  }
  else{
      notesElem.innerHTML = `Nothinfg to show! Use "Add a Note" section above to add notes`;
  }
}

//Function to delete a note
function deleteNote(index) {
    let notes = localStorage.getItem('notes');
    if (notes == null){
        notesObj = [];
    }
    else{
        notesObj = JSON.parse(notes);
    }
    notesObj.splice(index, 1);    // to delete a particular note
    localStorage.setItem('notes', JSON.stringify(notesObj));
    showNotes();
}

// code for serach area

let search = document.getElementById('searchTxt');   // targetting search text area
search.addEventListener('input', function () {              //input event is used to insert a word for search
    
    let inputVal = search.value.toLowerCase();      // assigning search value to a variable
    
    let noteCards = document.getElementsByClassName('noteCard');
    Array.from(noteCards).forEach(function(element) {           //  \Treating notecards as an array so all element in it will be array element
        let cardTxt = element.getElementsByTagName('P')[0].innerText;   // Targetting p tag text for writing a text in search box
        
       
        if((cardTxt).includes(inputVal)){           
          element.style.display = 'block';   // if input matches note display
        }
        else{
          
          element.style.display = 'none' ;     // if input not matches nothing display
        }
      
    });
});