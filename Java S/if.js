var edad = 18;
if (edad === 18 ){
    console.log("you can vote, that wild your firs votecion");
    } else if(edad > 18){
        console.log("you can again vote");
    } else {
        console.log ("you can't vote")

    }

    condition ? true : false;

    var numero =1;

    var resultado = numero === 1 ? "yes, i am an one" : "No, i am not  an one";

var op1 = "Piedra";
var op2 = "Tijera";
var op3 = "Papel";

var resultado = function(usuario , cpu){
    if (usuario != cpu ){
        if ( usuario == op1 && cpu == op2){
            console.log ("usuario win with " + op1);
        }else if (usuario == op2 && cpu == op3){
            console.log ("usuario win with " + op2);
        }else if (usuario == op3 && cpu ==op1){
            console.log("usuario win with "+ op3);
        }else{
            console.log ("WIN CPU YOU ARE A LOSER ");
         }
    }else if (usuario === cpu){
        console.log ("Empate");
    }
    
};

resultado (op1, op1)