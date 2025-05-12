/* Commençons avec une version simplifiée du jeu.
Nous imposerons la combinaison à deviner. Elle doit être composée de 2 pions de couleurs différentes.
Le joueur a donc 12 essais pour trouver la bonne combinaison.
4 choix de couleurs possibles.
Vous devez écrire au moins 3 fonctions pour gérer :
    Si la proposition est bien composée uniquement des 4 couleurs possibles et rien d’autre
    Une fonction qui retourne true ou false si la bonne combinaison est trouvée ou non
    Une fonction qui gère la partie (continuer tant que/fin si gagné)
*/

let secretCode = ['blue', 'yellow'];
let possibleColors = ['blue', 'red', 'green', 'yellow'];
// let playerChoice = document.querySelector("input");
let playerChoice = 'green yellow';
let playerColors = playerChoice.split(" ");

function isplayerChoiceAColor(choice, colors) {
    let i = 0;
    while (choice[0]!== colors[i] && i<=colors.length){
        console.log(colors[i]);
        i++
    }  
}

isplayerChoiceAColor(playerColors, possibleColors);

/** .every
.includes */