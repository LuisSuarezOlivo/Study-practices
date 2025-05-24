import random

def generar_contrasena():
    mayuscula = [ "A","B", "C", "D", "E", "F", "G", "H", "I", "J", "K"," L", "M", "N", "P", "Q", "R", "S", "T", "U","V","W","Y","X","Z" ]
    minuscula = [ "a","b", "c", "d", "e", "f", "g", "h", "i", "j", "k"," l", "m", "n", "p", "q", "r", "s", "t", "u","v","w","y","x","z" ]
    simbolo = ["!","#" , "$","_","&", "/", "?","-"]
    numeros = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0" ]
    
    caracteres = mayuscula + minuscula + simbolo + numeros
    

    contrasena = []

    for i in range(15):
        caracter_radom = random.choice(caracteres)
        contrasena.append(caracter_radom)

    contrasena = "".join(contrasena)
    return contrasena



def run():
    contrasena = generar_contrasena()
    print ("tu nueva contrasena es:" + contrasena)


if __name__ == "__main__":
    run()