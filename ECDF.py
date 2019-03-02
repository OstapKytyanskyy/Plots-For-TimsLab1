import matplotlib.pyplot as plt
from decimal import *
from matplotlib import axes
import numpy as np
import sys


def ecdf():
    arr_x = sys.argv[1].split("|")

    arr_x = [float(i) for i in arr_x if i != ""]
    # arr_y = sys.argv[2].split("|")
    #
    # arr_y = [float(i) for i in arr_y if i != ""]

    ecdf = sys.argv[3].split("|")
    ecdf = [float(i) for i in ecdf if i != ""]
    # arr_x = [0.1, 0.2, 0.3, 0.5, 1.6, 1.8, 3.8, 3.9, 4.3,4.3]
    # arr_x1 = [0.1, 0.2, 0.3, 0.5, 1.6, 1.8, 3.8, 3.9, 4.3]
    # ecdf = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 1]
    lines = []
    riznuzya = []
    j = 0
    for i in range(len(arr_x)):
        if i == len(arr_x) - 1:
            break
        j += 1
        lines.append([arr_x[i], arr_x[j]])
    j = 0
    getcontext().prec = 2
    for i in range(len(arr_x)):
        if i == len(arr_x) - 1:
            break
        j += 1
        riznuzya.append(Decimal(arr_x[j]) - Decimal(arr_x[i]))
    riznuzya.append(1)
    print(riznuzya)

    plt.arrow(1, arr_x[-1], 2, 0, head_width=0.03,
              head_length=0.05, fc='k',
              ec='k')
    for i in range(len(arr_x) - 1):
        # plt.plot([lines[i][0], lines[i][1]], [ecdf[i], ecdf[i]])
        plt.arrow(arr_x[i], ecdf[i], float(riznuzya[i] - Decimal(0.05)), 0, head_width=0.03, head_length=0.05, fc='k',
                  ec='k')
    plt.xticks(arr_x)
    plt.yticks(ecdf)
    plt.grid(True)
    plt.tight_layout()
    plt.xticks(rotation=90)
    # plt.plot([0.1, 0.5], [0.1, 0.1])

    # plt.plot([0.1, 0.1], [0.2, 0.1])
    # plt.plot([1,2], [2,2])
    # print(lines)

    plt.show()


ecdf()
