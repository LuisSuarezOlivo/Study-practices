def run():
    # for contador in range(1000):
    #     if contador % 2 != 0:
    #         continue
    #     print (contador)

    # for i in range (10000):
    #     print (i)
    #     if i == 5678:
    #         break

    texto = input(" Escribe un texto:")
    for letra in texto:
        if letra == "o" :
            break
        print (texto)

if __name__ == "__main__" :
    run()