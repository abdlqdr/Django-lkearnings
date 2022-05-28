// Data is an array of objects which contains information about the candidates
const data = [
  {
    name: "Rohan Das",
    age: 18,
    city: "kolkata",
    language: "python",
    framework: "Django",
    image: "https://randomuser.me/api/portraits/men/65.jpg",
  },
  {
    name: "Rohit Sharma",
    age: 24,
    city: "Ranchi",
    language: "Go",
    framework: "go framework",
    image: "https://randomuser.me/api/portraits/men/66.jpg",
  },
  {
    name: "Shubham Kumar",
    age: 26,
    city: "mumbai",
    language: "JavaScript",
    framework: "Angular",
    image: "https://randomuser.me/api/portraits/men/67.jpg",
  },
  {
    name: "Ragini Patel",
    age: 25,
    city: "Ahemdabad",
    language: "java",
    framework: "Django",
    image: "https://randomuser.me/api/portraits/women/65.jpg",
  },
  {
    name: "Rohan kumar",
    age: 38,
    city: "kolkata",
    language: "python",
    framework: "Django",
    image: "https://randomuser.me/api/portraits/men/85.jpg",
  },
  {
    name: "Katrina Singh",
    age: 32,
    city: "Pune",
    language: "javaScript",
    framework: "Nodejs",
    image: "https://randomuser.me/api/portraits/women/33.jpg",
  },
];

// CV Iterator
function cvIterator(profiles) {
    let nextIndex = 0;
    return {
        next: function () {
            return nextIndex < profiles.length
            ? { value: profiles[nextIndex++], done: false }
            : { done: true };
        },
    };
}
const candidates = cvIterator(data);
nextCV();

let next = document.getElementById('next');
next.addEventListener('click', nextCV);

function nextCV(){
    
    const currentCandidate = candidates.next().value;

    let image = document.getElementById('image');
    let profile = document.getElementById('profile');

    if(currentCandidate != undefined){
    image.innerHTML= `<img src='${currentCandidate.image}'>`;
    profile.innerHTML = `<ul class="list-group">
                            <li class="list-group-item">${currentCandidate.name}</li>
                            <li class="list-group-item">${currentCandidate.age} years old</li>
                            <li class="list-group-item">Lives in ${currentCandidate.city}</li>
                            <li class="list-group-item">Primarily works on ${currentCandidate.language} </li>
                            <li class="list-group-item">Uses ${currentCandidate.framework} framework</li>
                        </ul>`;
    }
    else{
        alert('End of Candidate Application');
        window.location.reload();
    }
}