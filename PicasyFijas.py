def validarTipado(user):
    try:
        int(user)
    except:
        print("El numero digitado no es un valor numerico, por favor ingrese un valor numerico \n")
        return -1
    return 0

def validarLongitud(user):
    if len(user) > 4:
        print("El numero digitado tiene más de 4 digitos \n")
        return -1
    else:
        return 0
    
def solicitudValorInicialPlayer1():
    numPlayer1 = input("Digite los 4 digitos del picas y fijas para el jugador 1:       ")
    validacionTipado1 = validarTipado(numPlayer1)
    validacionLongitud1 = validarLongitud(numPlayer1)
    if validacionTipado1 == -1 or validacionLongitud1 == -1:
        solicitudValorInicialPlayer1()
    else:
        return numPlayer1
    
def solicitudValorInicialPlayer2():
    numPlayer2 = input("Digite los 4 digitos del picas y fijas para el jugador 2:       ")
    validacionTipado2 = validarTipado(numPlayer2)
    validacionLongitud2 = validarLongitud(numPlayer2)

    if validacionTipado2 == -1 or validacionLongitud2 == -1:
        solicitudValorInicialPlayer2()
    else:
        return numPlayer2
    
def valorJuegoPlayer1(valorPlayer2):
    numAdivinadoP1 = input("Digite el valor que cree que posee el jugador 2:        ")
    validacionTipado1 = validarTipado(numAdivinadoP1)
    validacionLongitud1 = validarLongitud(numAdivinadoP1)
    contadorFijas = 0
    contadorPicas = 0
    turno = 0
    if validacionTipado1 == -1 or validacionLongitud1 == -1:
        valorJuegoPlayer1(valorPlayer2)
    else:
        for i in range(4):
            if numAdivinadoP1[i] == valorPlayer2[i]:
                contadorFijas+=1
                print(f"Tienes {contadorFijas} fijas")
            if i == 0:
                if numAdivinadoP1[i] == valorPlayer2[i+1] or numAdivinadoP1[i] == valorPlayer2[i+2] or numAdivinadoP1 == valorPlayer2[i+3]:
                    contadorPicas+=1
                    print(f"Tienes {contadorPicas} picas")
            elif i == 1:
                if numAdivinadoP1[i] == valorPlayer2[i-1] or numAdivinadoP1[i] == valorPlayer2[i+1] or numAdivinadoP1[i] == valorPlayer2[i+2]:
                    contadorPicas+=1
                    print(f"Tienes {contadorPicas} picas")
            elif i == 2:
                if numAdivinadoP1[i] == valorPlayer2[i-2] or numAdivinadoP1[i] == valorPlayer2[i-1] or numAdivinadoP1[i] == valorPlayer2[i+1]:
                    contadorPicas+=1
                    print(f"Tienes {contadorPicas} picas")
            elif i == 3:
                if numAdivinadoP1[i] == valorPlayer2[i-3] or numAdivinadoP1[i] == valorPlayer2[i-2] or numAdivinadoP1[i] == valorPlayer2[i-1]:
                    contadorPicas+=1
                    print(f"Tienes {contadorPicas} picas")
        if contadorFijas < 4:
            print("En else", contadorFijas)
            valorJuegoPlayer2(valorPlayer1)
        else:
            print("Se ganoxd player 1")

def valorJuegoPlayer2(valorPlayer1):
    numAdivinadoP2 = input("Digite el valor que cree que posee el jugador 1:        ")
    validacionTipado2 = validarTipado(numAdivinadoP2)
    validacionLongitud2 = validarLongitud(numAdivinadoP2)
    contadorFijas = 0
    contadorPicas = 0
    turno = 0
    if validacionTipado2 == -1 or validacionLongitud2 == -1:
        valorJuegoPlayer2(valorPlayer1)
    else:
        for i in range(4):
            if numAdivinadoP2[i] == valorPlayer1[i]:
                contadorFijas+=1
                print(f"Tienes {contadorFijas} fijas")
            if i == 0:
                if numAdivinadoP2[i] == valorPlayer1[i+1] or numAdivinadoP2[i] == valorPlayer1[i+2] or numAdivinadoP2[i] == valorPlayer1[i+3]:
                    contadorPicas+=1
                    print(f"Tienes {contadorPicas} picas")
            elif i == 1:
                if numAdivinadoP2[i] == valorPlayer1[i-1] or numAdivinadoP2[i] == valorPlayer1[i+1] or numAdivinadoP2[i] == valorPlayer1[i+2]:
                    contadorPicas+=1
                    print(f"Tienes {contadorPicas} picas")
            elif i == 2:
                if numAdivinadoP2[i] == valorPlayer1[i-2] or numAdivinadoP2[i] == valorPlayer1[i-1] or numAdivinadoP2[i] == valorPlayer1[i+1]:
                    contadorPicas+=1
                    print(f"Tienes {contadorPicas} picas")
            elif i == 3:
                if numAdivinadoP2[i] == valorPlayer1[i-3] or numAdivinadoP2[i] == valorPlayer1[i-2] or numAdivinadoP2[i] == valorPlayer1[i-1]:
                    contadorPicas+=1
                    print(f"Tienes {contadorPicas} picas")
        if contadorFijas < 4:
            print("En else", contadorFijas)
            valorJuegoPlayer1(valorPlayer2)
        else:
            print("Se ganoxd player 2")
    
valorPlayer1 = solicitudValorInicialPlayer1()
valorPlayer2 = solicitudValorInicialPlayer2()
valorJuegoPlayer1(valorPlayer2)

