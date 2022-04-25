# Iniciamos el menu

bandera_menu = True

while (bandera_menu):
    print("Elige la opcion desesada: ")
    print("1. Suma")
    print("2. Salir")
    opcion_menu = input("Ingrese el numero de la opcion: ")
    
    # Opcion N°1: Suma
    if (opcion_menu == "1"):
        numero_a = float(input('Ingrese el primer valor a sumar: '))
        numero_b = float(input('Ingrese el segundo valor a sumar: '))
        numero_total = numero_a + numero_b
        print(f'La suma es {numero_total}')
    elif (opcion_menu == "2"):
        print('Eligio salir de la calculadora')
        bandera_menu = False
