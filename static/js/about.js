/* Click View */

const view = document.querySelector('.ind1');

/* Links */
const story = document.querySelector('#St');
const product = document.querySelector('#Pr');
const people = document.querySelector('#Pe');
const tests = document.querySelector('#Te');

story.addEventListener('click', ()=>{
    view.style.left = '0';
})

product.addEventListener('click', ()=>{
    view.style.left = '25%';
})

people.addEventListener('click', ()=>{
    view.style.left = '50%';
})

tests.addEventListener('click', ()=>{
    view.style.left = '75%';
})