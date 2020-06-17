#!/usr/bin/python3
import funciones as f
from calculador import Aproximador
import json
import os


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
        self.aproximar(base, peso)

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

    def aproximar(self, base, peso):
        os.system("clear")
        datos = {
            'base': base,
            'peso': peso
            }
        with open('conjuntos_puntos.json', 'r') as file:
            for elem in file:
                puntos = json.loads(elem)
        datos.update(puntos)

        aprox = Aproximador(datos)
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
        while True:
            valor = input('x = ')
            if valor == 'exit':
                break
            try:
                fx = aprox.aprox_funtion(float(valor))
            except():
                raise Exception('Ingreso erroneo')
            print(('f*({x}) = {f}').format(x=valor, f=fx))


if __name__ == "__main__":
    m = Menu()
    m.main()
    exit()
