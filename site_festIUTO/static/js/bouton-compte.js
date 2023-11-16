// Sélectionnez le bouton par son ID
var button = document.getElementById('icon-user');

// Ajoutez un gestionnaire d'événements au clic sur le bouton
button.addEventListener('click', function() {
    // Redirigez l'utilisateur vers la page 2 en utilisant JavaScript
    window.location.href = 'compte';
});