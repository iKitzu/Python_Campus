##---------------------------------
##---- Ejercicio 1 ----
##---------------------------------
##Impresión en consola
print("Hola MundOwO")

## ---- Datos primitivos ----
##String
texto = "Campus"
print(texto)
print(type(texto))
##Int
numeroEntero = 1
print(numeroEntero)
##Float
numeroDecimal = 3.1
print(numeroDecimal)
##Double
numeroDecimalLargo = 3.14167582737283
print(numeroDecimalLargo)
##Boolean
booleano = True
print(booleano)

##---- Entradas parte del usuario ----
entradaUsuario = input("Ingresa tu nombre: ")
print("Tu nombre es:",entradaUsuario)

##---- Entradas parte del usuario con definición de tipo de dato primitivo ----
entradaUsuarioNumero = int(input("Ingresa tu edad: "))
print("Tu edad es:",entradaUsuarioNumero)

##---- Ciclos ----
##Ciclo "for"
for i in range(5,10,2): # For contador in range (Desde,hasta,pasos):
    print(i)

##Ciclo "while"
booleanito = True
while booleanito == True: # While condición a_cumplir :
    print("Sigo vivo")
    booleanito = False

##---- Condicionales ----
texto1 = "Campus"
if texto1 == "Campus":
    print("Soy Campus")
else:
    print("No soy Campus")

## Desarrollado por Kenneth santiago ceballos sierra - 1097095601