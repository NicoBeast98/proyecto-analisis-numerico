import numpy as np


def unidad(x):
    unidad.__name__ = '1'
    return 1.0


def inden(x):
    inden.__name__ = 'x'
    return float(x)


def x_pow(p=1):
    x_pow.__name__ = 'x^'+str(p)
    return lambda x: x**p


def sen(x):
    sen.__name__ = 'sen(x)'
    return float(np.sin(x))


def cos(x):
    cos.__name__ = 'cos(x)'
    return float(np.cos(x))


def exp(n=False):
    if n:
        return lambda x: float(np.exp(-x))
    else:
        return lambda x: float(np.exp(x))


def ln(x):
    ln.__name__ = 'ln(x)'
    return float(np.log(x))
