const burgerButton = document.querySelector('.burger-button');
let items = document.getElementById('items');

burgerButton.addEventListener('click', toggle);

function toggle(){
    burgerButton.classList.toggle('open');
    if(burgerButton.classList.value != "burger-button open"){
        items.style.left = "-100%";
    } else{
        items.style.left = "0";
    }
}