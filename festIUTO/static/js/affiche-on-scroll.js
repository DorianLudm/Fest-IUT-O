// Fonction pour vérifier si un élément est visible dans la fenêtre
function isElementInViewport(element) {
    const rect = element.getBoundingClientRect();
    return (
        rect.top >= 0 &&
        rect.left >= 0 &&
        rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
        rect.right <= (window.innerWidth || document.documentElement.clientWidth)
    );
}

// Fonction pour faire apparaître les éléments lorsque dans la fenêtre visible
function showElementsOnScroll() {
    const elements = document.querySelectorAll('.element');

    elements.forEach((element) => {
        if (isElementInViewport(element)) {
            element.classList.add('visible');
        }
    });
}

// Écouteur d'événement pour vérifier lors du défilement
window.addEventListener('scroll', showElementsOnScroll);

// Appelez la fonction pour vérifier les éléments au chargement de la page
window.addEventListener('load', showElementsOnScroll);
