ficha = {
    "nombre": input("Ingrese su nombre: "),
    "telefono": input("Ingrese su telefono: "),
    "gmail": input("Ingrese su gmail: "),
    "edad": input("Ingrese su edad: "),
}

while True:

    print("---MENU---")
    print("1- Ver ficha")
    print("2- Editar dato")
    print("3- Salir")

    opc = int(input("que opcion vas a elegir "))

    if opc == 1:
        print(ficha)

    if opc == 2:
        campo = input("Que dato quieres editar? ")

        if campo in ficha:
            nuevo_valor = input("Nuevo valor: ")
            ficha[campo] = nuevo_valor
            print("Dato actualizado")
        else:
            print("Ese campo no existe")

    if opc == 3:
        print("saliendo del programa...")
        break