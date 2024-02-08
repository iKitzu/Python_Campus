#REALIZAR UN PROGRAMA QUE USE UN DICCIONARIO PARA GESTIONAR LOS PRODUCTOS
#Y PRECIOS DE LA TABLA, DONDE SE LE PREGUNTE AL USUARIO POR UN PRODUCTO
#Y LA CANTIDAD. AL FINALIZAR MOSTRAR EN LA CONSOLA EL PRECIO TOTAL. SI
#EL PRODUCTO NO ESTA DEBE MOSTRAR UN MENSAJE INFORMANDO SOBRE ELLO

#Tienda de mortadelas 

productos={"mortadela":3200,
           "mortadela de pollo":4300,
           "mortadela de pavo":8000}
print("================================")
print("====Estos son los productos====")
print("================================")

for i in productos:
    print(i)
print("================================")

while True:
    producto=input("Porfavor ingrese el nombre del producto (o si quiere finalizar escriba fin): ")

    if producto=="fin":
        break
    if producto in productos:
        cantidad=int(input("Escriba la cantidad que desea llevr de su producto: "))
        TotalPagar= productos[producto]*cantidad
    else:
        print("El producto que escribio no se encuentra")


print("Su total a pagar es: ",TotalPagar)