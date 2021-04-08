/* MOUSE CURSOR */

let mouseCursor = document.querySelector('.cursor');
let links = document.querySelectorAll('a');

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
});