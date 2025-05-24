def conversor(moneda_de_cambio, valor_dolar, valor_euro):
    moneda = input("¿ Cuantos" + moneda_de_cambio + " tienes?: ")
    moneda = float(moneda)
    dolares = moneda * valor_dolar * valor_euro
    dolares = round (dolares, 2)
    dolares = str(dolares)
    print(" Tienes  "  + dolares + "  $ dolares")

def dolares_a_euros():
    dolares1 =input("¿ Cuantos dolares tienes?: ")
    dolares1 = float(dolares1)  
    valor_euro = 0.88
    euros = dolares1 * valor_euro
    euros = round(euros, 2)
    euros = str(euros)
    print(" Tienes € "  + euros + " Euros")


menu = """
Bienvenido al conversor de monedas 💰

1 - Euros a dolares
2 - Pesos mexicanos
3 - Yen
4 - Dolares a Euros

Elige una opcion: """

opcion = int(input(menu))

if opcion == 1:
    conversor(" Euros", 1.13, 1)
elif opcion == 2:
    conversor(" Peso Mexicano", 0.049, 1)
elif opcion == 3:
    conversor(" Yen", 0.0087, 1)
elif opcion == 4:
    dolares_a_euros()

else:
    print ("ingresa una opcion correcta por favor")
    """  """

