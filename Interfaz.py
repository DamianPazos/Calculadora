from tkinter import *

expresion = ''

def limpiar():
    global expresion
    expresion = ''
    eq.set(expresion)
    return

def click(numero):
    global expresion
    expresion = expresion + str(numero)
    eq.set(expresion)
    return

def calcular():
    global expresion
    total = str(eval(expresion))
    eq.set(total)
    
    expresion = total
    return

def agregar_botones(gui):
    # Fila N°1 - Columna N°1 - Boton Limpiar
    boton_clear = Button(gui,text="C",fg='black',bg='gray',command=lambda: limpiar(),height=2,width=4)
    boton_clear.grid(row=1,column=0)
    
    # Fila N°1 - Columna N°3 - Boton Dividir
    boton_division = Button(gui,text="/",fg='white',bg='orange',command=lambda: click('/'),height=2,width=4)
    boton_division.grid(row=1,column=3)
    
    # Fila N°2 - Columna N°1 - Boton Siete
    boton_siete = Button(gui,text="7",fg='black',bg='gray',command=lambda: click(7),height=2,width=4)
    boton_siete.grid(row=2,column=0)
    
    # Fila N°2 - Columna N°2 - Boton Ocho
    boton_ocho = Button(gui,text="8",fg='black',bg='gray',command=lambda: click(8),height=2,width=4)
    boton_ocho.grid(row=2,column=1)
    
    # Fila N°2 - Columna N°3 - Boton Nueve
    boton_nueve = Button(gui,text="9",fg='black',bg='gray',command=lambda: click(9),height=2,width=4)
    boton_nueve.grid(row=2,column=2)
    
    # Fila N°2 - Columna N°4 - Boton Multiplicacion
    boton_multiplicar = Button(gui,text="x",fg='white',bg='orange',command=lambda: click('*'),height=2,width=4)
    boton_multiplicar.grid(row=2,column=3)
    
    # Fila N°3 - Columna N°1 - Boton
    boton_cuatro = Button(gui,text="4",fg='black',bg='gray',command=lambda: click(4),height=2,width=4)
    boton_cuatro.grid(row=3,column=0)
    
    # Fila N°1
    boton_nueve = Button(gui,text="5",fg='black',bg='gray',command=lambda: click(5),height=2,width=4)
    boton_nueve.grid(row=3,column=1)
    
    # Fila N°2
    boton_uno = Button(gui,text="6",fg='black',bg='gray',command=lambda: click(6),height=2,width=4)
    boton_uno.grid(row=3,column=2)
    
    # Fila N°2
    boton_resta = Button(gui,text="-",fg='white',bg='orange',command=lambda: click('-'),height=2,width=4)
    boton_resta.grid(row=3,column=3)
    
    # Fila N°2
    boton_tres = Button(gui,text="3",fg='black',bg='gray',command=lambda: click(3),height=2,width=4)
    boton_tres.grid(row=4,column=0)
    
    # Fila N°2
    boton_dos = Button(gui,text="2",fg='black',bg='gray',command=lambda: click(2),height=2,width=4)
    boton_dos.grid(row=4,column=1)
    
    # Fila N°2
    boton_uno = Button(gui,text="1",fg='black',bg='gray',command=lambda: click(1),height=2,width=4)
    boton_uno.grid(row=4,column=2)
    
    # Fila N°2
    boton_suma = Button(gui,text="+",fg='white',bg='orange',command=lambda: click('+'),height=2,width=4)
    boton_suma.grid(row=4,column=3)
    
    # Fila N°2
    boton_cero = Button(gui,text="0",fg='black',bg='gray',command=lambda: click(0),height=2,width=9)
    boton_cero.grid(row=5,column=0, columnspan=2)
    
    # Fila N°2
    boton_decimal = Button(gui,text=".",fg='black',bg='gray',command=lambda: click('.'),height=2,width=4)
    boton_decimal.grid(row=5,column=2)
    
    # Fila N°2
    boton_igual = Button(gui,text="=",fg='white',bg='orange',command=lambda: calcular(),height=2,width=4)
    boton_igual.grid(row=5,column=3)
    


gui = Tk() # Se crea la ventana principal
gui.configure(background='light gray') # Fondo
gui.title('Calculadora')
gui.geometry('180x350')

eq = StringVar()

campo_expresion = Entry(gui, textvariable=eq)
campo_expresion.grid(columnspan=3)

agregar_botones(gui)
gui.mainloop()
