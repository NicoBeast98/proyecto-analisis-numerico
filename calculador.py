import numpy as np
import funciones as f


class Aproximador():

    def __init__(self, puntos_x, puntos_y, base, peso):
        self.puntos_x = puntos_x  # Intervalo de x
        self.puntos_y = puntos_y  # Intervalo de f(x)
        self.base = base    # Base por la que me aproximo
        self.peso = peso    # Funcion peso
        self.coef = []
        self.sel

    def producto_escalar(self, f1, f2):
        producto = 0
        for x in self.puntos_x:
            producto += f1(x)*f2(x)*self.peso(x)
        return producto

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

    def prod_esc_y(self, i):
        prod = 0
        for j in range(len(self.puntos_y)):
            prod += self.puntos_y[j]*self.base[i](self.puntos_x[j])
        return prod

    def aprox_funtion(self, x):
        n_f = 0
        for i in range(len(self.base)):
            n_f += self.base[i](x)*self.coef[i]
        return n_f

    def error(self):
        f_2 = 0
        coefs = 0
        for i in range(len(self.puntos_x)):
            f_2 += self.puntos_y[i]**2
        for j in range(len(self.coef)):
            coefs += self.coef[j]*self.prod_esc_y(j)
        err = (f_2 - coefs)**0.5
        return err
    # WIP (Imprimir nueva funcion)
    # def get_n_fun(self):
    #     fun = 'f*(x) = '
    #     for i in range(len(self.coef)):
    #         fname = ''
    #         if self.base[i].__name__ == '<lambda>':
    #             if self.base[i].__qualname__.find('exp') != -1:
    #                 if self.base[i](1) < 1:
    #                     fname = 'e^-x'
    #                 else:
    #                     fname = 'e^x'
    #         if self.base[i].__qualname__.find('x_pow') != -1:
    #             print(self.base[i]
    #         else:
    #             fname = self.base[i].__name__
    #         fun += str(self.coef[i])+'*'+fname+' + '
    #     fun = fun.rstrip(' + ')
    #     return fun


if __name__ == "__main__":
    aprox = Aproximador(
        [1.0, 1.2, 1.4, 1.6, 1.8],
        [0.242, 0.1942, 0.1497, 0.1109, 0.079],
        [f.ln, f.x_pow(2)], f.unidad)
    print(aprox.get_n_fun())
