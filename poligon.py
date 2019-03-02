import matplotlib.pyplot as plt
import numpy as np
import sys


def poligon_frequency():
    arr_x = sys.argv[1].split("|")

    arr_x = [float(i) for i in arr_x if i != ""]
    arr_y = sys.argv[2].split("|")
    # arr_y.remove(" ")
    arr_y = [float(i) for i in arr_y if i != ""]
    plt.plot(arr_x, arr_y)
    plt.show()


poligon_frequency()
