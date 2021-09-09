let searchBtn = document.querySelector('#search-btn');
let searchBar = document.querySelector('.search-bar-container');
let formBtn = document.querySelector('#login-btn');
let loginForm = document.querySelector('.login-form-container');
let formClose = document.querySelector('#form-close');
let formregBtn = document.querySelector('#register-btn');
let registerForm = document.querySelector('.register-form-container');
let formregClose = document.querySelector('#regform-close');
let imageBtn = document.querySelectorAll('.img-btn');


// const one = $('.first');
// const two = $('.second');
// const three = $('.third');
// const four = $('.forth');
// const five= $('.five');

// console.log('id:',one)

// const handleSelect = (selection) => {
//     switch(selection){
//         case 'first': {
//             one.classList.add('checked')
//             two.classList.remove('checked')
//             three.classList.remove('checked')
//             four.classList.remove('checked')
//             five.classList.remove('checked')
//         }
//     }
// }
// const arr = [one, two, three, four, five]

// arr.forEach(item=> {
//     item.on('click',(event)=>{
//     handleSelect(event.target.id)
// })
// })


window.onscroll = () =>{
    searchBtn.classList.remove('fa-times');
    searchBar.classList.remove('active');
}

searchBtn.addEventListener('click', () =>{
    searchBtn.classList.toggle('fa-times');
    searchBar.classList.toggle('active');
});
formBtn.addEventListener('click', () =>{
    loginForm.classList.add('active');
});

formClose.addEventListener('click', () =>{
    loginForm.classList.remove('active');
});
formregBtn.addEventListener('click', () =>{
    registerForm.classList.add('active');
});

formregClose.addEventListener('click', () =>{
    registerForm.classList.remove('active');
});

imageBtn.forEach(btn => {
    btn.addEventListener('click', ()=>{
        document.querySelector('.controls .active').classList.remove('active');
        btn.classList.add('active');
        let src = btn.getAttribute('data-src');
        document.querySelector('#image-slider').src= src;
    });
});



function scrollUp() {
    const scrollUp =document.getElementById('scroll-up');

    if(this.scrollY >= 200) scrollUp.classList.add('show-scroll'); else scrollUp.classList.remove('show-scroll');
    
}
window.addEventListener('scroll', scrollUp)
