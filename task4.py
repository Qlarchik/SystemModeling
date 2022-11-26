import random
import numpy as np


def func(x):
    return pow(x, 3) + 1


def integrate(a, b):
    exp_nmb = [10 ** n for n in range(4, 8)]
    k = 0
    m = 0
    x_min = a
    x_max = b
    y_min = 0
    y_max = func(b)
    s_par = (x_max - x_min) * (y_max - y_min)
    vector = []

    for exp in exp_nmb:
        while k < exp:
            xp = (x_max - x_min) * random.random() + x_min
            yp = (y_max - y_min) * random.random() + y_min
            if (func(xp)) > yp:
                m += 1
            k += 1
        s = s_par * m / exp
        vector.append(s)

    return vector


if __name__ == '__main__':
    A = 0
    B = 2

    for i in range(1, 4):
        seria = integrate(A, B)
        print(f'SERIA_{i} = {seria}')

        seria = np.array(seria)
        average = np.mean(seria)
        print(f'Average value in SERIA_{i}: {average}')

        standard_deviation = np.std(seria)
        avg_error = standard_deviation / np.sqrt(len(seria))
        print(f'Average error in SERIA_{i}: {avg_error}')
