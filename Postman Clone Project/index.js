console.log("project script");

// Utility functions;
//1. Utility function to get DOM element from string
function getElementFromString(string) {
  let div = document.createElement("div");
  div.innerHTML = string;
  return div.firstElementChild;
}

// Initialize no. of parameters
let addedParamsCount = 0;

// Hiding paramereters box initially
let parametersBox = document.getElementById("parametersBox");
parametersBox.style.display = "none";

// If the user clicks on params box, hide the json box
let paramsRadio = document.getElementById("paramsRadio");
paramsRadio.addEventListener("click", () => {
  document.getElementById("parametersBox").style.display = "block";
  document.getElementById("requestJsonBox").style.display = "none";
});

// If the user clicks on json box, hide the params box
let jsonRadio = document.getElementById("jsonRadio");
jsonRadio.addEventListener("click", () => {
  document.getElementById("requestJsonBox").style.display = "block";
  document.getElementById("parametersBox").style.display = "none";
});

// If the user click on + button, add more parameters
let addParams = document.getElementById("addParams");
addParams.addEventListener("click", () => {
  let params = document.getElementById("params");
  let string = `  <div class="form-row my-2">
                        <legend class="col-form-label col-sm-2 pt-0">Parameter ${
                          addedParamsCount + 2
                        }</legend>
                        <div class="col-md-4">
                        <input
                            type="text"
                            class="form-control"
                            id="parameterKey${addedParamsCount + 2}"
                            placeholder="Enter Parameter ${
                              addedParamsCount + 2
                            } key"
                        />
                        </div>
                        <div class="col-md-4">
                        <input
                            type="text"
                            class="form-control"
                            id="parameterValue${addedParamsCount + 2}"
                            placeholder="Enter Parameter ${
                              addedParamsCount + 2
                            } value"
                        />
                        </div>
                        <button  id="addParams" class="btn btn-primary mx-3 deleteParam"> - </button>
                    </div>`;
  // Convert the element string to DOM node
  let paramElement = getElementFromString(string);
  params.appendChild(paramElement);

  // Add an event listener to remove the parameter on clicking '-' button
  let deleteParam = document.getElementsByClassName("deleteParam");
  for (item of deleteParam) {
    item.addEventListener("click", (e) => {
      let result = confirm("Are you sure to delete?");
      if (result == true){
        e.target.parentElement.remove();
      }
    });
  }
  
  addedParamsCount++;
});

// If user clicks on sbmit button
let submit = document.getElementById("submit");
submit.addEventListener("click", () => {
  // show please wait in the response box to request patience from the user
  document.getElementById("responsePrism").innerHTML = "please wait... fetching response...";

  // Fetch all the values user has entered
  let url = document.getElementById("url").value;
  let requestType = document.querySelector(
    "input[name='requestType']:checked"
  ).value;
  let contentType = document.querySelector(
    "input[name='contentType']:checked"
  ).value;

  // If user has used params option  instead of json, collect all the parameters in an object
  if (contentType == "params") {
    data = {};
    for (i = 0; i < addedParamsCount + 1; i++) {
      if (document.getElementById("parameterKey" + (i + 1)) != undefined) {
        let key = document.getElementById("parameterKey" + (i + 1)).value;
        let value = document.getElementById("parameterValue" + (i + 1)).value;
        data[key] = value;
      }
    }
    data = JSON.stringify(data);
  } else {
    data = document.getElementById("requestJsonText").value;
  }
  // for debugging
  console.log("URL is", url);
  console.log("requestType is", requestType);
  console.log("contentType is", contentType);
  console.log("data is", data);

  // If the request type is get, invoke fetch api to create a post request
  if (requestType == "GET") {
    fetch(url, {
      method: "GET",
    })
      .then((response) => response.text())
      .then((text) => {
        // document.getElementById("responseJsonText").value = text;
        document.getElementById("responsePrism").innerHTML = text;
        Prism.highlightAll();

      });
  } else {
    fetch(url, {
      method: "POST",
      body: data,
      headers: {
        "Content-type": "application/json; charset=UTF-8",
      },
    })
      .then((response) => response.text())
      .then((text) => {
        // document.getElementById("responseJsonText").value = text;
        document.getElementById("responsePrism").innerHTML = text;
        Prism.highlightAll();
      });
  }
});
