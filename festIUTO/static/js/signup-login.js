const login = document.getElementById("login-box");
const signup = document.getElementById("signup-box");

const boutonLogin = document.getElementById("boutonlogin");
const boutonSignup = document.getElementById("boutonsignup");

boutonLogin.addEventListener("click", function () {
    login.style.display = 'none';
    signup.style.display = 'block';
    console.log("login");
});

boutonSignup.addEventListener("click", function () {
    signup.style.display = 'none';
    login.style.display = 'block';
    console.log("signup");
});



document.addEventListener("DOMContentLoaded", function () {
    // Récupérez l'élément du formulaire de connexion par sa classe
    const formulaireConnexion = document.getElementById('login-container');
        
    // Récupérez l'élément du message de bienvenue par sa classe
    const bienvenueMessage = document.querySelector('.bienvenue-message');
        
     // Vérifiez si l'utilisateur est connecté (par exemple, en vérifiant la présence de l'ID de l'utilisateur dans la session)
    let estConnecte = document.getElementById('user_id').value;
    console.log(estConnecte)
    // Affichez le formulaire de connexion ou le message de bienvenue en fonction de l'état de connexion
    if (estConnecte != "") {
        // Utilisateur connecté, affichez le message de bienvenue
        bienvenueMessage.style.display = 'block';
        formulaireConnexion.style.display = 'none';
    } else {
        // Utilisateur non connecté, affichez le formulaire de connexion
        bienvenueMessage.style.display = 'none';
        formulaireConnexion.style.display = 'flex';
    }
});




