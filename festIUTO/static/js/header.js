var prevScrollPos = window.pageYOffset;

window.onscroll = function() {
    var currentScrollPos = window.pageYOffset;
    if (prevScrollPos > currentScrollPos) {
        // Faire apparaître la barre de navigation lorsque l'utilisateur fait défiler vers le haut
        document.querySelector("nav").style.top = "0";
        if (currentScrollPos == 0) {
            document.querySelector("nav").style.backgroundColor = "rgba(255, 255, 255, 0.3)";
        }
    } else {
        // Cacher la barre de navigation lorsque l'utilisateur fait défiler vers le bas
        document.querySelector("nav").style.top = "-100px"; 
        document.querySelector("nav").style.backgroundColor = "transparent";
    }
    prevScrollPos = currentScrollPos;
}