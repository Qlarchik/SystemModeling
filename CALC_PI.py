import random
import numpy as np


def calc_pi(x_0, y_0, r_0, n):
    x_max = x_0 + r_0
    x_min = x_0 - r_0

    y_max = y_0 + r_0
    y_min = y_0 - r_0

    n_temp = n
    circle_count = 0
    while n_temp > 0:
        p = random.random()
        xp = (x_max - x_min) * p + x_min

        p = random.random()
        yp = (y_max - y_min) * p + y_min

        if (xp - x_0) ** 2 + (yp - y_0) ** 2 < r_0 ** 2:
            circle_count += 1

        n_temp -= 1

    result = 4 * circle_count / n
    print("PI = " + str(result))
    return result


def calc_vector(x_0, y_0, r_0):
    ExpNmb = [10 ** n for n in range(4, 9)]

    vector = []
    for Exp in ExpNmb:
        print('Number of experiments: ', Exp)
        vector.append(calc_pi(x_0, y_0, r_0, Exp))

    return vector


if __name__ == '__main__':
    x0 = 0
    y0 = 0
    r0 = 5

    for i in range(1, 6):
        seria = calc_vector(x0, y0, r0)
        print(f'SERIA_{i} = {seria}')

        np.array(seria)

        average = np.mean(seria)
        print(f'Average value of pi in SERIA_{i}: {average}')

        standard_deviation = np.std(seria)
        avg_error = standard_deviation / np.sqrt(len(seria))
        print(f'Average error in SERIA_{i}: {avg_error}')
