let navBar = document.querySelector('.nav');
let slideNavigation = document.querySelector('.slideNav');
let navList = document.querySelector('.listNav')
let barX = false;

navBar.addEventListener('click', () => {
    if(!barX){
        navBar.classList.remove('open')
        slideNavigation.style.width = '0px';
        navList.style.display = 'none'
        barX = true;
    }
    else {
        navBar.classList.add('open')
        slideNavigation.style.width = '100%';
        navList.style.display = 'flex'
        barX = false;
    }

});



/* MOUSE CURSOR */

let mouseCursor = document.querySelector('.cursor');
let links = document.querySelectorAll('a');
let nav = document.querySelector('.nav');

window.addEventListener('mousemove', cursor);

function cursor(e){
    mouseCursor.style.top = e.pageY + 'px';
    mouseCursor.style.left = e.pageX + 'px';
}

links.forEach(link => {
    link.addEventListener('mouseover', () => {
        mouseCursor.classList.add('link-grow');
        links.classList.add('hover-link');
    });
    link.addEventListener('mouseleave', () => {
        mouseCursor.classList.remove('link-grow');
        links.classList.remove('hover-link');
    });

    nav.addEventListener('mouseover', () => {
        mouseCursor.classList.add('link-grow');
        links.classList.add('hover-link');
    });
    nav.addEventListener('mouseleave', () => {
        mouseCursor.classList.remove('link-grow');
        links.classList.remove('hover-link');
    });
});


/* LOADING ANIMATION */

//ingerit page
const logo = document.querySelector('.logo-side');
const imgSide = document.querySelector('.image-side');
//index page
const bannerA = document.querySelector('.banner');

const tl = new TimelineMax();

tl.fromTo(logo, 1, {opacity: 0, y: -90}, {opacity: 1, y: 0})
.fromTo(imgSide, 1, {opacity: 0, y: -90}, {opacity: 1, y: 0}, "-=1")
.fromTo(bannerA, 1, {opacity: 0, x: -120}, {opacity: 1, x: 0}, "-=1")

/* LOADING ANIMATION */
