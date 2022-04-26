from tkinter import Tk, Menu

# Creo la ventana principal
root = Tk()
root.title('Calculadora')

# Creo el menu de navegacion
menu_navegacion = Menu(root)
root.config(menu=menu_navegacion)

# Creo un archivo para el menu
archivo_menu = Menu(menu_navegacion)

# Agrego un elemento al menu
archivo_menu.add_command(label='Salir',command=root.destroy)

# Agrgar el menu a la barra de menu
menu_navegacion.add_cascade(label='Archivo',menu=archivo_menu,underline=0)

root.mainloop()
