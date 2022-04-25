from re import T
import matplotlib.pyplot as plt
import numpy as np
from tkinter import Tk, Text, Button, END, re
class Interfaz:
    def __init__(self,ventana):
        # Inicializo la ventana con su nombre
        self.ventana = ventana
        self.ventana.title('Calculadora')
        
        # Pantalla de la calculadora
        self.pantalla = Text(ventana,state='disabled',width='30',height='5', background='light cyan',foreground='black',font=('Arial',17))
        
        # Ubicar la pantalla en la ventana
        self.pantalla.grid(row=0,column=0,columnspan=4,padx=5,pady=5)
        
        #Inicializar la operacion mostrada en pantalla como un string vacio
        self.operacion =''
        
        # Botones
        boton_1 = self.crearBoton(1)
        boton_2 = self.crearBoton(2)
        boton_3 = self.crearBoton(3)
        boton_4 = self.crearBoton(4)
        boton_5 = self.crearBoton(5)
        boton_6 = self.crearBoton(6)
        boton_7 = self.crearBoton(7)
        boton_8 = self.crearBoton(8)
        boton_9 = self.crearBoton(9)
        boton_0 = self.crearBoton(0)
        boton_suma = self.crearBoton('+')
        boton_resta = self.crearBoton('-')
        boton_multiplicacion = self.crearBoton('*')
        boton_division = self.crearBoton('/')
        boton_igual = self.crearBoton('=',escribir=False)
        boton_decimal = self.crearBoton('.')
        boton_borrar = self.crearBoton('C',escribir=False)
        
        # Ubicacion de Botones
        
        botones = [boton_1,boton_2,boton_3,boton_suma,boton_4,boton_5,boton_6,boton_resta,boton_7,boton_8,boton_9,boton_multiplicacion,boton_0,boton_decimal,boton_igual,boton_division,boton_borrar]
        contador = 0
        for fila in range(1,5):
            for columna in range (4):
                botones[contador].grid(row=fila,column=columna)
                contador +=1
                
        botones[-1].grid(row=5,column=1)
                
    def crearBoton(self,valor,escribir=True,ancho=9,alto=1):
        return Button(self.ventana,text=valor,width=ancho,height=alto,font=('Arial',15),command=lambda:self.click(valor,escribir))
        
    def click(self,texto,escribir):
        if not escribir:
            if texto == '=' and self.operacion!='':
                resultado =str(eval(self.operacion))
                self.operacion=''
                self.limpiarPantalla()
                self.mostrarEnPantalla(resultado)
            elif texto == 'C':
                self.operacion=''
                self.limpiarPantalla()
        # Mostrar texto
        else:
            self.operacion+=str(texto)
            self.mostrarEnPantalla(texto)     
        return
    
    def limpiarPantalla(self):
        self.pantalla.configure(state='normal')
        self.pantalla.delete('1.0',END)
        self.pantalla.configure(state='disabled')
        return
    
    def mostrarEnPantalla(self, valor):
        self.pantalla.configure(state='normal')
        self.pantalla.insert(END,valor)
        self.pantalla.configure(state='disable')
        return
    
root = Tk()
calculadora = Interfaz(root)
root.mainloop()


#Funcion para la suma
def suma(a,b):
    total = a + b
    return total
# Funcion para la resta
def resta(a,b):
    total = a - b
    return total
# Funcion para la multiplicacion
def multiplicar(a,b):
    total = a * b
    return total
# Funcion para la division
def division(a,b):
    total = a / b
    return total
# Funcion para ingreso de un numero
def ingreso_numero():
    numero = float(input('Ingrese el valor: '))
    return numero
# Iniciamos una bandera para el menu
bandera_menu = True
# Iniciamos el menu
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
        numero_a = ingreso_numero()
        numero_b = ingreso_numero()
        numero_total = suma(numero_a,numero_b)
        print(f'La suma es {numero_total}')
    # Opcion N°2: Resta
    elif (opcion_menu == "2"):
        numero_a = ingreso_numero()
        numero_b = ingreso_numero()
        numero_total = resta(numero_a,numero_b)
        print(f'La resta es {numero_total}')
    # Opcion N°3: Multiplicacion
    elif (opcion_menu == "3"):
        numero_a = ingreso_numero()
        numero_b = ingreso_numero()
        numero_total = multiplicar(numero_a,numero_b)
        print(f'La multiplicacion es {numero_total}')
    # Opcion N°4: Division
    elif (opcion_menu == "4"):
        numero_a = ingreso_numero()
        numero_b = ingreso_numero()
        numero_total = division(numero_a,numero_b)
        print(f'La division es {numero_total}')
    elif (opcion_menu == "5"):
        print('Eligio salir de la calculadora')
        bandera_menu = False
