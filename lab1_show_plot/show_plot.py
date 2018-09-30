import getopt
import os
import sys

import matplotlib.pyplot as plt
import numpy as np


def main(a, b, d):
    print("a =", a)
    print("b =", b)
    print("d =", d)

    # Data for plotting
    x_array = np.arange(a, b, d)
    y_array = 1 * x_array ** 3 + 2 * x_array ** 2 + 2 * x_array - 9 - 45 * np.sin(5 * x_array)

    # print("X: ", x_array)
    # print("Y: ", y_array)
    # print("Coordinates: ", list(zip(x_array, y_array)))

    roots = x_array[y_array == 0.0]
    print("Roots: ", roots)

    fig, ax = plt.subplots()

    major_ticks = np.arange(a, b, 0.5)
    minor_ticks = np.arange(a, b, 0.1)

    ax.set_xticks(major_ticks)
    ax.set_xticks(minor_ticks, minor=True)

    ax.plot(x_array, y_array, 'r-')

    ax.set(xlabel='x', ylabel='y',
           title='my function')

    ax.grid(which='minor', alpha=0.1)
    ax.grid(which='major', alpha=0.5)

    # fig.savefig("test.png")
    plt.show()


def parse_main_args_and_call_main(argv):
    a = 0.0
    b = 10.0
    d = 0.01

    try:
        opts, args = getopt.getopt(argv, "a:b:d:")
    except getopt.GetoptError:
        print(os.path.basename(__file__) + ' -a <left bound> -b <right bound> -d <tabulation>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-a':
            a = float(arg)
        elif opt == '-b':
            b = float(arg)
        elif opt == '-d':
            d = float(arg)

    main(a, b, d)


if __name__ == '__main__':
    parse_main_args_and_call_main(sys.argv[1:])
