var frutas = ["Manzana", "cereza","Platano","Fresa"];

console.log (frutas);

console.log(frutas.length);
// con este podemos ver la longitud del arrays//

console.log(frutas[0]);
// En java comenzamos desde 0 en cualquier momento, lo cual el primer elemento regresado seria el primero escrito.//

var masFrutas = frutas.push("uvas")
//Esto es para colocarle mas elementos a mi arrays //

var ultimo = frutas.pop("Uvas")
// con este metodo es para quitarle un elemento al arrays//

var nuevaLongitud = frutas.unshift("Naranjas")
// Con este metodo es para colocar de primero de tu arrays el nuevo elemento que estas agregando//

var borraFruta = frutas.shift("Naranjas")
// Este metodo ayuda a eliminar el elemento que esta en el principio//

var posicion = frutas.indexOf("cereza")
// te dice la posicion de la fruta que escoges 