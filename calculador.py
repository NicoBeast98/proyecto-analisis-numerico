import numpy as np
# import funciones as f > 'Funciones con las que trabaja el obj'


class Aproximador():

    def __init__(self, datos):
        self.puntos_x = datos['puntos_x']  # Intervalo de x
        self.puntos_y = datos['puntos_y']  # Intervalo de f(x)
        self.base = datos['base']    # Base por la que me aproximo
        self.peso = datos['peso']    # Funcion peso
        self.coef = []
        self.err = 0
        # Calculo todo
        self.sel
        self.error

    # Producto escalar entre los puntos de 'x' y
    # a base dada.
    def producto_escalar(self, f1, f2):
        producto = 0
        for x in self.puntos_x:
            producto += f1(x)*f2(x)*self.peso(x)
        return producto
    # <>

    # Resuelvo el sistema de ecuaciones lineales que
    # contiene los productos escalares.
    @property
    def sel(self):
        rg = len(self.base)
        mat_A = np.empty((rg, rg))
        for i in range(rg):
            for j in range(rg):
                mat_A[i][j] = self.producto_escalar(
                    self.base[i], self.base[j]
                    )
        mat_B = np.empty((rg))
        for i in range(rg):
            mat_B[i] = self.prod_esc_y(i)
        mat_A_inv = np.linalg.inv(mat_A)
        self.coef = np.matmul(mat_A_inv, mat_B)
    # <>

    # Realizar producto escalar entre los valores y de entrada
    # y las funciones de la base.
    def prod_esc_y(self, i):
        prod = 0
        for j in range(len(self.puntos_y)):
            prod += self.puntos_y[j]*self.base[i](self.puntos_x[j])
        return prod
    # <>

    # Mejor aproximacion con la base ingresada.
    def aprox_funtion(self, x):
        n_f = 0
        for i in range(len(self.base)):
            n_f += self.base[i](x)*self.coef[i]
        return n_f
    # <>

    # Calculo de error en el metodo.
    @property
    def error(self):
        f_2 = 0
        coefs = 0
        for i in range(len(self.puntos_x)):
            f_2 += self.puntos_y[i]**2
        for j in range(len(self.coef)):
            coefs += self.coef[j]*self.prod_esc_y(j)
        err = (f_2 - coefs)**0.5
        self.err = err
    # <>

    # Gets de datos
    def get_px(self):
        return self.puntos_x

    def get_py(self):
        return self.puntos_y

    def get_f_peso(self):
        return self.peso

    def get_base(self):
        return self.base

    def get_coef(self):
        return self.coef

    def get_error(self):
        return self.err
    # <>


if __name__ == "__main__":
    pass
