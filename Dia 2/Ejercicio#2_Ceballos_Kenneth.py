# Juego Adivina el numero B)

import random

numAtt=0
numMin=1
nunMax=100

print("Hola! ¿Cual es tu nombre?")
username= input()

numero=random.randint(numMin, nunMax)

print("Bien, "+username + " Estoy pensando en un numero entre el ", str(numMin)+ " y", str(nunMax))
print("¿Puedes adivinar cual es?")


while numAtt < 10:
    print("Adivina: ")
    adivinar= input()
    adivinar=int(adivinar)
    
    numAtt=numAtt+1

    if adivinar<numero:
        print("Tu numero es muy bajo")
    if adivinar>numero:
        print("Tu numero es muy alto")
    if adivinar==numero:
        break

if adivinar==numero:
    numAtt=str(numAtt)
    print("Buen trabajo, ",username)
    print("Haz adivinado mi numero en ", numAtt + " Intentos")
if adivinar!= numero:
    numero= str(numero)
    print("Perdiste, el numero en el que pensaba era " + numero)
    