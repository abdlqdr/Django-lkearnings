console.log('drag n drop')

const imgBox = document.querySelector('.imgBox');

const whiteBoxes = document.getElementsByClassName('whiteBox');

// Dragable event listener for imgBox
imgBox.addEventListener('dragstart', (e)=>{
    console.log('dragStart triggered');
    e.target.className += ' hold'
    setTimeout(() => {
        e.target.className = 'hide'
    }, 0);
});
imgBox.addEventListener('dragend', (e)=>{
    console.log('dragEnd triggered');
    e.target.className = 'imgBox';
});

for (whiteBox of whiteBoxes){
    whiteBox.addEventListener('dragover', (e)=>{
        e.preventDefault();
        console.log('dragOver triggered');
    });
    whiteBox.addEventListener('dragenter', (e)=>{
        console.log('dragEnter triggered');
        e.target.className += ' dashed'
    });
    whiteBox.addEventListener('dragleave', (e)=>{
        console.log('dragLeave triggered');
        e.target.className = 'whiteBox'
    });
    whiteBox.addEventListener('drop', (e)=>{
        console.log('drop triggered');
        e.target.append(imgBox);
    });
}