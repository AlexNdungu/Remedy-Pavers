/* Product Slider */
const prodMain = document.querySelector('.prSl');
const prods = document.querySelectorAll('.thePr')


const next = document.querySelector('.next');
const prev = document.querySelector('.prev');

let counter = 1;
const size = prods[0].clientWidth;

prodMain.style.transform = 'translateX(' + (-size * counter) + 'px)';

next.addEventListener('click', () => {
    if(counter >= prods.length - 1 )return;
    prodMain.style.transition = 'transform .4s ease-in-out';
    counter++;
    prodMain.style.transform = 'translateX(' + (-size * counter) + 'px)'; 
})

prev.addEventListener('click', () => {
    if(counter<=0)return;
    prodMain.style.transition = 'transform .4s ease-in-out';
    counter--;
    prodMain.style.transform = 'translateX(' + (-size * counter) + 'px)'; 
})

prodMain.addEventListener('transitionend', () =>{
    console.log(prods[counter])
    if(prods[counter].id === "lastClone"){
        prodMain.style.transition = 'none';
        counter = prods.length - 2;
        prodMain.style.transform = 'translateX(' + (-size * counter) + 'px)';
    }
    if(prods[counter].id === "firstClone"){
        prodMain.style.transition = 'none';
        counter = prods.length - counter;
        prodMain.style.transform = 'translateX(' + (-size * counter) + 'px)';
    }
})




window.onload = function(){
    /* ELEGANCE SLIDER */
/* Image Product Hover Slider */

let many = document.getElementsByClassName('many')

let activeImages = document.getElementsByClassName('active')

for (var i=0; i < many.length; i++){

    many[i].addEventListener('mouseover', function(){
        console.log(activeImages)
        
        if (activeImages.length > 0){
            activeImages[0].classList.remove('active')
        }
        

        this.classList.add('active')
        document.getElementById('thePs').src = this.src
    })
}


/* ARROW HEAD SLIDER */

let arrows = document.getElementsByClassName('arrows')

let activeImagesA = document.getElementsByClassName('activeA')

for (var i=0; i < arrows.length; i++){

    arrows[i].addEventListener('mouseover', function(){
        console.log(activeImagesA)
        
        if (activeImagesA.length > 0){
            activeImagesA[0].classList.remove('activeA')
        }
        

        this.classList.add('activeA')
        document.getElementById('arrow').src = this.src
    })
}

/*DAZZLE SHAPE*/

let dazzles = document.getElementsByClassName('dazzles')

let activeImagesDz = document.getElementsByClassName('activeDz')

for (var i=0; i < arrows.length; i++){

    dazzles[i].addEventListener('mouseover', function(){
        console.log(activeImagesDz)
        
        if (activeImagesDz.length > 0){
            activeImagesDz[0].classList.remove('activeDz')
        }
        

        this.classList.add('activeDz')
        document.getElementById('dazzle').src = this.src
    })
}

/* LILy SHAPE */

let lilys = document.getElementsByClassName('lilys')

let activeImagesly = document.getElementsByClassName('activeLy')

for (var i=0; i < lilys.length; i++){

    lilys[i].addEventListener('mouseover', function(){
        console.log(activeImagesly)
        
        if (activeImagesly.length > 0){
            activeImagesly[0].classList.remove('activeLy')
        }
        

        this.classList.add('activeLy')
        document.getElementById('lile').src = this.src
    })
}


/* DENE SHAPE */

let denes = document.getElementsByClassName('denes')

let activeImagesDen = document.getElementsByClassName('activeDen')

for (var i=0; i < denes.length; i++){

    denes[i].addEventListener('mouseover', function(){
        console.log(activeImagesDen)
        
        if (activeImagesDen.length > 0){
            activeImagesDen[0].classList.remove('activeDen')
        }
        

        this.classList.add('activeDen')
        document.getElementById('deny').src = this.src
    })
}

/* ZIGZAG SHAPE */

let zigs = document.getElementsByClassName('zigs')

let activeImagezig = document.getElementsByClassName('activezig')

for (var i=0; i < zigs.length; i++){

    zigs[i].addEventListener('mouseover', function(){
        console.log(activeImagezig)
        
        if (activeImagezig.length > 0){
            activeImagezig[0].classList.remove('activezig')
        }
        

        this.classList.add('activezig')
        document.getElementById('zig').src = this.src
    })
}


}

