const firstButton = document.getElementById("menuToggle");
const secondButton = document.getElementById("croixToggle");
const menuItems = document.getElementById('menuItems');
const menuButton = document.getElementById('menuButton');

const navElem1 = document.getElementById('nav-elem-1');
const navElem2 = document.getElementById('nav-elem-2');
const navElem3 = document.getElementById('nav-elem-3');
const navElem4 = document.getElementById('nav-elem-4');
const navElem5 = document.getElementById('nav-elem-5');
const navElem6 = document.getElementById('nav-elem-6');
const navElem7 = document.getElementById('nav-elem-7');
  
function reset(){
    menuButton.style.display = 'none';
}

reset()

// Ajouter un gestionnaire d'événement pour le clic sur le premier bouton
firstButton.addEventListener("click", function () {
    // Exécute l'animation de disparition
    firstButton.style.animationName = "bouton-disparition"; 
    });
  
// Ajouter un gestionnaire d'événement pour l'animation de disparition du premier bouton
document.addEventListener("animationend", function (event) {
    if (event.target === firstButton && event.animationName === "bouton-disparition") {
        firstButton.style.display = 'none'; 
        secondButton.style.display = 'block';
        secondButton.style.animationName = "bouton-apparition";
        menuButton.style.display = 'block';
        //menuButton.style.animationName = "bouton-apparition";
    }
});

secondButton.addEventListener("click", function () {
    // Exécute l'animation de disparition
    secondButton.style.animationName = "bouton-disparition"; 
});

// Ajouter un gestionnaire d'événement pour l'animation de disparition du second bouton
document.addEventListener("animationend", function (event) {
    if (event.target === secondButton && event.animationName === "bouton-disparition") {
        secondButton.style.display = 'none'; 
        firstButton.style.display = "block";
        firstButton.style.animationName = "bouton-apparition";
        menuButton.style.display = 'none';
        //menuButton.style.animationName = "bouton-apparition";
    }
});

navElem1.addEventListener('click', () => {
    reset();
    secondButton.style.animationName = "bouton-disparition"; 
});

navElem2.addEventListener('click', () => {
    reset();
    secondButton.style.animationName = "bouton-disparition"; 
});

navElem3.addEventListener('click', () => {
    reset();
    secondButton.style.animationName = "bouton-disparition"; 
});

navElem4.addEventListener('click', () => {
    reset();
    secondButton.style.animationName = "bouton-disparition"; 
});

navElem5.addEventListener('click', () => {
    reset();
    secondButton.style.animationName = "bouton-disparition"; 
});

navElem6.addEventListener('click', () => {
    reset();
    secondButton.style.animationName = "bouton-disparition"; 
});

navElem7.addEventListener('click', () => {
    reset();
    secondButton.style.animationName = "bouton-disparition"; 
});

  