var estudiantes = ["Maria","Sergio","Rosa","Daniel"];

function saludarEstudiantes(estudiantes){
    console.log(`Hola, ${estudiantes}`);
}

for (var i= 0; i < estudiantes.length; i++){
saludarEstudiantes(estudiantes[i])
}


var estudiantes = ["Maria","Sergio","Rosa","Daniel"];

function saludarEstudiantes(estudiantes){
    console.log(`Hola, ${estudiantes}`);
}

for (var estudiante of estudiantes){
saludarEstudiantes(estudiante);
}


var estudiantes = ["Maria","Sergio","Rosa","Daniel"];

function saludarEstudiantes(estudiantes){
    console.log(`Hola, ${estudiantes}`);
}

while(estudiantes.length>0){
    console.log(estudiantes)
    var estudiante  = estudiantes.shift();
    saludarEstudiantes(estudiante);
}