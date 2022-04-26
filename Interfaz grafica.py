from tkinter import Tk, Menu, ttk, Text, Button

class VentanaPrincipal:
    
    def __init__(self,ventana):
        
        self.ventana = ventana
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
        # Pantalla de la calculadora
        self.pantalla = Text(ventana,state='disabled',width='30',height='5', background='light cyan',foreground='black',font=('Arial',17))
        # Ubicar la pantalla en la ventana
        self.pantalla.grid(row=0,column=0,columnspan=4,padx=5,pady=5)
        #Inicializar la operacion mostrada en pantalla como un string vacio
        self.operacion =''
        
# Creo la ventana principal
root = Tk()
calculadora_basica = VentanaPrincipal(root)

# Inicio la ventana
root.mainloop()
