#!/usr/bin/python3
import funciones as f
from calculador import Aproximador
import os
import matplotlib.pyplot as plt


class Menu():

    def main(self):
        os.system("clear")
        print('''
\tAproximador Minimos Cuadrados
Ingrese la base por la que aproximar los puntos,
debe ingresar cada funcion como se muestra
las opciones disponibles son:
\t~ Unidad >> 1
\t~ Identidad >> x
\t~ Logaritmo Natural >> ln(x)
\t~ Exponecial Positiva >> e^x
\t~ Exponencial Negativa >> e^-x
\t~ Potencia de x a la 'n'>> x^n
\t~ Coseno >> cos(x)
\t~ Seno >> sen(x)

Cuando termine de ingresar las funciones de la base
ingrese \'done\'
        ''')
        base = self.selecion_funcion()
# Funcion Peso
        print('''
Ahora selecione la funcion peso de las mismas funciones
anteriores:
            ''')
        peso = ''
        while True:
            peso = input('w(x) >> ')
            peso = self.validate(peso)
            if peso == 'bad_input':
                print('Ingreso erroneo, intente otra vez')
            else:
                break
# Puntos de x
        print('''
Ingreso el conjunto de puntos de la funcion a aproximar:
        ''')
        punt = self.input_puntos()
        self.aproximar(base, peso, punt)

    def validate(self, fun):
        if fun == '1':
            return f.unidad
        elif fun == 'x':
            return f.inden
        elif fun == 'ln(x)':
            return f.ln
        elif fun == 'e^x':
            return f.exp(False)
        elif fun == 'e^-x':
            return f.exp(True)
        elif fun.find('x^') != -1:
            div = fun.split('^')
            if div[1].isdecimal():
                return f.x_pow(int(div[1]))
            else:
                return f.x_pow(float(div[1]))
        elif fun == 'cos(x)':
            return f.cos
        elif fun == 'sen(x)':
            return f.sen
        return 'bad_input'

    def selecion_funcion(self):
        temp = ''
        base = []
        while temp != 'done':
            temp = input('f(x) >> ')
            if temp == 'done':
                break
            val = self.validate(temp)
            if val == 'bad_input':
                print('Ingreso erroneo, intente otra vez')
            else:
                print('Ingreso correcto')
                base.append(val)
        return base

    def aproximar(self, base, peso, puntos):
        # os.system("clear")
        datos = {
            'base': base,
            'peso': peso,
            }
        datos.update(puntos)

        aprox = Aproximador(datos)
        aprox
        print('puntos en y =', aprox.puntos_y)
        print(('Intervalo de x = [{i} , {f}]').format(
            i=aprox.puntos_x[0], f=aprox.puntos_x[len(aprox.puntos_x)-1]
        ))
        print('coef = ', aprox.get_coef())
        print('error = ', aprox.get_error())
        print('''
Para usar la funcion aproximada ingrese el valor de x,
para salir ingrese \'exit\'.
        ''')
        self.graph(aprox)
        while True:
            valor = input('x = ')
            if valor == 'exit':
                break
            try:
                fx = aprox.aprox_funtion(float(valor))
            except():
                raise Exception('Ingreso erroneo')
            print(('f*({x}) = {f}').format(x=valor, f=fx))
    
    def input_puntos(self):
        print('Ingrese \'done\' cuando termine')
        dots = int(input('Cuantos pares de puntos? >>'))
        puntos = {'puntos_x':[], 'puntos_y':[]}
        for n in range(0,dots*2):
            if n%2 == 0:
                while True:
                    var = input('x = ')
                    if self.numtype(var):
                        puntos['puntos_x'].append(float(var))
                        break
                    else:
                        print('Ingreso erroneo, intente de nuevo')
            else:
                while True:
                    var = input('y = ')
                    if self.numtype(var):
                        puntos['puntos_y'].append(float(var))
                        break
                    else:
                        print('Ingreso erroneo, intente de nuevo')
        return(puntos)
    
    def numtype(self, num):
        if num.isalpha():
            return False
        elif num.find(' ') != -1:
            return False
        elif num.isdecimal():
            return True
        elif num.find(',') != -1:
            div = num.split(',')
            for val in div:
                if val.isalpha():
                    return False
            return True
        elif num.find('.') != -1:
            div = num.split('.')
            for val in div:
                if val.isalpha():
                    return False
            return True
    
    def graph(self, aprox):
        coefs = aprox.get_coef()
        print(coefs)

if __name__ == "__main__":
    m = Menu()
    m.main()
    exit()
