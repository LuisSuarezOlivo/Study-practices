var numero = 1 ;
switch (numero){
    case 1:
        console.log("Soy uno!");
        break;
    case 10:
        console.log("Soy un 10!");
        break;
    case 100:
        console.log("Soy un 100!")
        break;
    default:
        console.log("No soy nada")
}

var op1 = "Piedra";
var op2 = "Tijera";
var op3 = "Papel";

var resultado = function(usuario , cpu){
    
    switch (true){
        case( usuario == op1 && cpu == op2):
            console.log ("usuario win with " + op1);
            break;
        case(usuario == op2 && cpu == op3):
            console.log ("usuario win with " + op2);
            break;
        case(usuario == op3 && cpu ==op1):
            console.log("usuario win with "+ op3);
            break;
        case(usuario === cpu):
            console.log ("TENEMOS UN EMPATE");
            break;
        default:
            console.log("WIN CPU YOU ARE A LOSER");
   }
}
resultado (op1,op2)