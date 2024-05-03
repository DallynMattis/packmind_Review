const prompt = require("prompt-sync")({sigint:true});

// fonction qui renvoi "pierre" "feuille" ou "ciseaux" aléatoirement
function randomRPS() {
    var rps = ["pierre", "feuille", "ciseaux"];
    var random = Math.floor(Math.random() * 3);
    return rps[random];
}
// fonction qui détermine qui gagne entre le joueur et l'ordinateur

function who_won(player: string, computer: string) {
    if (player === computer) {
        return "Egalité";
    } else if (
        (player === "pierre" && computer === "ciseaux") ||
        (player === "ciseaux" && computer === "feuille") ||
        (player === "feuille" && computer === "pierre")
    ) {
        return "Le joueur a gagné";
    } else {
        return "L'ordinateur a gagné";
    }
}

let computer = randomRPS();
// récupere le choix du joueur
let player = prompt("pierre, feuille ou ciseaux ?");
console.log("L'ordinateur a choisi " + computer);
console.log(who_won(player, computer));
