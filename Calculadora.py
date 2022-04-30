class Calculadora():
    
    def __init__(self):
        
        self.string_expresion = ''
        self.resultado = 0

    def identificar_expresion(self):
        if '+' in self.string_expresion:
            return '+'
        elif '*' in self.string_expresion:
            return '*'
        elif '-'in self.string_expresion:
            return '-'
        elif '/' in self.string_expresion:
            return '/'
    
    def ingresar_expresion(self):
        self.string_expresion = input('Ingrese el calculo a realizar: ')

    def separar_expresion(self):
        operacion = self.identificar_expresion()
        numeros = self.string_expresion.split(operacion)
        return numeros
        
    def suma(self, lista_numeros):
        self.resultado = float(lista_numeros[0]) + float(lista_numeros[1])
        
    def multiplicacion(self, lista_numeros):
        self.resultado = float(lista_numeros[0]) * float(lista_numeros[1])
        
    def resta(self, lista_numeros):
        self.resultado = float(lista_numeros[0]) - float(lista_numeros[1])
        
    def division(self, lista_numeros):
        self.resultado = float(lista_numeros[0]) / float(lista_numeros[1])

calcular = Calculadora()
bandera_menu = True
while bandera_menu:
    calcular.ingresar_expresion()
    operacion = calcular.identificar_expresion()
    numeros = calcular.separar_expresion()
    if operacion == '+':
        calcular.suma(numeros)
    elif operacion == '*':
        calcular.multiplicacion(numeros)
    elif operacion == '-':
        calcular.resta(numeros)
    elif operacion == '/':
        calcular.division(numeros)
    
    print(f'El resultado es: {calcular.resultado}')
    opcion_seguir = input('Desea seguir Y/N?: ')
    if opcion_seguir == 'N' or opcion_seguir == 'n':
        bandera_menu = False
    else:
        bandera_menu = True
