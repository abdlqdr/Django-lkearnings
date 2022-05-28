let submitAlarm = document.getElementById('submitAlarm');
submitAlarm.addEventListener('click', setAlarm);
var audio = new Audio('https://media.geeksforgeeks.org/wp-content/uploads/20190531135120/beep.mp3');

// function to play alarm tone
function ringBell() {
    audio.play();
};

// This function runs whenever alarm is set from UI.
function setAlarm(e){

    e.preventDefault();
    
    const inputAlarm = document.getElementById('inputAlarm');
    alamDate = new Date(inputAlarm.value);
    console.log(`Setting Alarm for ${alamDate}...`);

    now = new Date();
    let timeToAlarm = alamDate - now;

    console.log(alamDate - now);
    
    if(timeToAlarm >= 0){
        setTimeout(() => {
            ringBell();
        }, timeToAlarm);
    }

    
}

const inputAlarm = document.getElementById('inputAlarm');
inputAlarm.addEventListener("blur", () => {
    console.log("name is blurred");

    //validate name here
    let regex = /^([0-9]){4}\-([0-9]){2}\-([0-9]){2} ([0-9]){2}\:([0-9]){2}\:([0-9]){2}/;
    let str = inputAlarm.value;
    console.log(regex, str);
    
    if (regex.test(str)) {
      console.log("Your inputAlarm is valid");
      inputAlarm.classList.remove("is-invalid");
      validInputAlarm = true;
    } else {
      console.log("Your inputAlarm is invalid");
      inputAlarm.classList.add("is-invalid");
      validInputAlarm = false;
    }

});
