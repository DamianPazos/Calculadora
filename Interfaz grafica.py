from tkinter import Tk, Menu, ttk, Text, Button, Frame, END

# Creo la ventana principal
root = Tk()
root.title('Calculadora')
# Dimension de la ventana principal
ventana_ancho = 400
ventana_alto = 500
# Tomo las dimensiones de la Pantalla
pantalla_ancho = root.winfo_screenwidth()
pantalla_alto = root.winfo_screenheight()
# Busco el centro de la pantalla principal
centro_eje_x = int(pantalla_ancho/2 - ventana_ancho/2)
centro_eje_y = int(pantalla_alto/2 - ventana_alto/2)
# Posiciono la ventana del programa
root.geometry(f'{ventana_ancho}x{ventana_alto}+{centro_eje_x}+{centro_eje_y}')
# Creo el menu de navegacion
menu_navegacion = Menu(root)
root.config(menu=menu_navegacion)
# Creo una opcion del navegador 
operaciones_menu = Menu(menu_navegacion,tearoff=False)
# Agrego un elemento al menu
operaciones_menu.add_command(label='Calculadora Basica')
operaciones_menu.add_command(label='Calculadora Cientifica')
operaciones_menu.add_command(label='Conversiones')
operaciones_menu.add_command(label='Formula Resolvente') 
operaciones_menu.add_separator()
operaciones_menu.add_command(label='Salir',command=root.destroy)
# Agregar el menu a la barra de menu
menu_navegacion.add_cascade(label='Operaciones',menu=operaciones_menu,underline=0)
# Crear un Frame principal
frame_main = Frame(root)
frame_main.pack(expand=True, fill='both')
frame_main.config(bg='Cyan')



def calculadora_basica(frame):
    frame_calculadora = Frame(frame)
    
    # Botones
    boton_1 = crearBoton(frame_calculadora,1)
    boton_2 = crearBoton(frame_calculadora,2)
    boton_3 = crearBoton(frame_calculadora,3)
    boton_4 = crearBoton(frame_calculadora,4)
    boton_5 = crearBoton(frame_calculadora,5)
    boton_6 = crearBoton(frame_calculadora,6)
    boton_7 = crearBoton(frame_calculadora,7)
    boton_8 = crearBoton(frame_calculadora,8)
    boton_9 = crearBoton(frame_calculadora,9)
    boton_0 = crearBoton(frame_calculadora,0)
    boton_suma = crearBoton(frame_calculadora,'+')
    boton_resta = crearBoton(frame_calculadora,'-')
    boton_multiplicacion = crearBoton(frame_calculadora,'*')
    boton_division = crearBoton(frame_calculadora,'/')
    boton_igual = crearBoton('=',escribir=False)
    boton_decimal = crearBoton(frame_calculadora,'.')
    boton_borrar = crearBoton(frame_calculadora,'C',escribir=False)
    
    # Ubicacion de Botones
    botones = [boton_1,boton_2,boton_3,boton_suma,boton_4,boton_5,boton_6,boton_resta,boton_7,boton_8,boton_9,boton_multiplicacion,boton_0,boton_decimal,boton_igual,boton_division,boton_borrar]
    contador = 0
    for fila in range(1,5):
        for columna in range (4):
            botones[contador].grid(row=fila,column=columna)
            contador +=1
                
    botones[-1].grid(row=5,column=1)
    
    def crearBoton(frame,valor,escribir=True,ancho=9,alto=1):
        return Button(frame,text=valor,width=ancho,height=alto,font=('Arial',15),command=lambda:click(valor,escribir))
    
    # Accion de click
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
    
    # Limpieza de pantalla
    def limpiarPantalla(self):
        self.pantalla.configure(state='normal')
        self.pantalla.delete('1.0',END)
        self.pantalla.configure(state='disabled')
        return
        
# Pantalla de la calculadora
#frame_main.pantalla = Text(ventana,state='disabled',width='30',height='5', background='light cyan',foreground='black',font=('Arial',17))
# Ubicar la pantalla en la ventana
#frame_main.pantalla.grid(row=0,column=0,columnspan=4,padx=5,pady=5)
#Inicializar la operacion mostrada en pantalla como un string vacio
#frame_main.operacion =''
calculadora_basica(frame_main)
# Inicio la ventana
root.mainloop()
