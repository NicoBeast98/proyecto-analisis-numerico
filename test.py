import funciones as f
from calculador import Aproximador
import os
import matplotlib.pyplot as plt
import numpy as np

datos = {
    'base': [f.unidad, f.inden, f.exp(True)],
    'peso': f.inden,
    }
puntos = {"puntos_x":[1.0, 1.2, 1.4, 1.6, 1.8],"puntos_y":[0.242, 0.1942, 0.1497, 0.1109, 0.079]}
datos.update(puntos)
aprox = Aproximador(datos)

x = np.linspace(aprox.puntos_x[0],aprox.puntos_x[len(aprox.puntos_x)-1], 10, dtype=list)
plt.plot(x, aprox.aprox_funtion(x))
plt.title('Funcion aproximada')
plt.xlabel('x')
plt.ylabel('f*(x)')
plt.grid()
plt.show()