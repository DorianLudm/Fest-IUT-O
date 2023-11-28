let cacher = false;

function actionLoupe(){
    if(!cacher){
        cacherElements();
    }
    else{
        reafficherElements();
    }
}

// Fonction pour masquer les éléments
function cacherElements() {
    console.log("cache");
    // Parcourir les éléments et changer leur style "display" en "none"
    for(let i=1; i<=6; i++){
        const elem = document.getElementById('element-a-cacher'+i);
        elem.style.display = 'none';
    }
    const recherche = document.getElementById('barre-recherche');
    recherche.style.display = 'flex';
    // const filtre = document.getElementById('icon-filtre');
    // filtre.style.display = 'block';
    cacher = true;
}

// Fonction pour réafficher les éléments
function reafficherElements() {
    console.log("affiche");
    const recherche = document.getElementById('barre-recherche');
    recherche.style.display = 'none';
    // const filtre = document.getElementById('icon-filtre');
    // filtre.style.display = 'none';
    for(let i=1; i<=6; i++){
        const elem = document.getElementById('element-a-cacher'+i);
        elem.style.display = 'flex';
    }
    cacher = false;
}

// Ajouter un écouteur d'événement au bouton pour masquer les éléments
var boutonCacher = document.getElementById('icon-loupe-white');
boutonCacher.addEventListener('click', actionLoupe);



