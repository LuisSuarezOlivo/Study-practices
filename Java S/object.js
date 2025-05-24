var objeto = {};
// esta es la forma tipica de crear un objeto en JS//


var miAuto= {
    marca: "Toyota",
    modelo:"Corolla",
    years: 2020,
    detalleDelAuto: function(){
        console.log(`Auto ${this.modelo} ${this.years}`);
    }
};

miAuto.detalleDelAuto
// este seria un ejemplo de como pedirle a la consola que me traiga un objeto en especifico.

function auto(marca, modelo, years){
    this.marca = marca;
    this.modelo = modelo;
    this.years = years;
}
var autoNuevo = new auto ("Tesla","modelo3",2020)

var autoNuevo2= new auto("Tesla","Model X",2018);
var autoNuevo3 =new auto("toyota","corolla",2020);