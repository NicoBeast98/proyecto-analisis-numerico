import numpy as np


def unidad(x):
    unidad.__name__ = '1'
    return np.float64(1)


def inden(x):
    inden.__name__ = 'x'
    return np.float64(x)


def x_pow(p=1):
    x_pow.__name__ = 'x^'+str(p)
    return lambda x: np.float64(x**p)


def sen(x):
    sen.__name__ = 'sen(x)'
    return np.sin(x)


def cos(x):
    cos.__name__ = 'cos(x)'
    return np.cos(x)


def exp(n=False):
    if n:
        return lambda x: np.exp(-x)
    else:
        return lambda x: np.exp(x)


def ln(x):
    ln.__name__ = 'ln(x)'
    return np.log(x)
