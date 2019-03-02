import matplotlib.pyplot as plt
import numpy as np
import sys

from decimal import  *
def main():
    # arr1 = np.arange(0, 10, 1)
    # arr2 = np.arange(10, 20, 1)
    # plt.plot(arr1, arr2)
    # plt.show()
    # arr_x = [8.38, 2.31, 0.54, 1.19, 8.52, 5.75, 6.0, 0.02, 4.08, 7.08]
    # arr_y = [9.15, 7.06, 2.98, 8.82, 7.75, 7.25, 0.03, 6.27, 3.95, 0.77]
    # for i in range(len(sys.argv[1])):
    #
    #     arr_x.append(float(sys.argv[1][i]))
    #     arr_y.append(float(sys.argv[2][i]))
    diagram_frequency()
    # diagram_frequency()



def diagram_frequency():
    arr_x = sys.argv[1].split("|")

    arr_x = [float(i) for i in arr_x if i != ""]
    arr_y = sys.argv[2].split("|")
    # arr_y.remove(" ")
    arr_y = [float(i) for i in arr_y if i != ""]

    # print(arr_x, arr_y)
    for i in range(len(arr_x)):
        plt.plot([arr_x[i], arr_x[i]], [0.0, arr_y[i]])
    plt.xticks(rotation=90)
    plt.xticks(arr_x)
    plt.yticks(arr_y)

    plt.grid(True)
    plt.tight_layout()
    plt.show()



main()
