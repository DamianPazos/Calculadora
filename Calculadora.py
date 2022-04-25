# Iniciamos el menu
def suma(a,b):
    total = a + b
    return total

def resta(a,b):
    total = a - b
    return total

def multiplicar(a,b):
    total = a * b
    return total

def division(a,b):
    total = a / b
    return total

bandera_menu = True

while (bandera_menu):
    print("Elige la opcion desesada: ")
    print("1. Suma")
    print('2. Resta')
    print('3. Multiplicacion')
    print('4. Division')
    print("5. Salir")
    opcion_menu = input("Ingrese el numero de la opcion: ")
    
    # Opcion N°1: Suma
    if (opcion_menu == "1"):
        numero_a = float(input('Ingrese el primer valor a sumar: '))
        numero_b = float(input('Ingrese el segundo valor a sumar: '))
        numero_total = suma(numero_a,numero_b)
        print(f'La suma es {numero_total}')
    # Opcion N°2: Resta
    elif (opcion_menu == "2"):
        numero_a = float(input('Ingrese el primer valor a restar: '))
        numero_b = float(input('Ingrese el segundo valor a restar: '))
        numero_total = resta(numero_a,numero_b)
        print(f'La resta es {numero_total}')
    # Opcion N°3: Multiplicacion
    elif (opcion_menu == "3"):
        numero_a = float(input('Ingrese el primer valor a multiplicar: '))
        numero_b = float(input('Ingrese el segundo valor a multiplicar: '))
        numero_total = multiplicar(numero_a,numero_b)
        print(f'La multiplicacion es {numero_total}')
    # Opcion N°4: Division
    elif (opcion_menu == "4"):
        numero_a = float(input('Ingrese el primer valor a dividir: '))
        numero_b = float(input('Ingrese el segundo valor a dividir: '))
        numero_total = division(numero_a,numero_b)
        print(f'La division es {numero_total}')
    elif (opcion_menu == "5"):
        print('Eligio salir de la calculadora')
        bandera_menu = False
