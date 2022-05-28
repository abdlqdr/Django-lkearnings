console.log("abhi tak news");

// Initializing the news api parameters
source = "the-times-of-india";
let apikey = "771456111ba149f288b976ada436749a";

// Grab the news container
let newsAccordian = document.getElementById("newsAccordian");

// Create a ajax GET request
const xhr = new XMLHttpRequest();
xhr.open(
  "GET",
  `https://newsapi.org/v2/top-headlines?sources=${source}&apiKey=${apikey}`,
  true
);

xhr.onload = function () {
  if (this.status === 200) {
    let json = JSON.parse(this.responseText);
    let articles = json.articles;
    console.log(articles);
    let newsHtml = "";
    articles.forEach(function (element, index) {
      let news = `  <div class="accordion-item">
                        <h2 class="accordion-header" id="heading${index}">
                            <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapse${index}" aria-expanded="true" aria-controls="collapse${index}">
                            <strong>Aaj ki Taaza Khabar ${index+1}:-${element.title}</strong>
                            </button>
                        </h2>

                        <div id="collapse${index}" class="accordion-collapse collapse" aria-labelledby="heading${index}" data-bs-parent="#newsAccordian">
                            <div class="accordion-body">${element['description']}. <a href="${element.url}" target="_blank">Click here to read more</a></div>
                        </div>
                    </div>`;
      newsHtml += news;
    });
    newsAccordian.innerHTML = newsHtml;
  } else {
    console.log("Some error occured");
  }
};

xhr.send();
