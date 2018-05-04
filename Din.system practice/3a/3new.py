import matplotlib.pyplot as plt
import numpy as np

def logistic_map(x0, a, b):
    return a - b*x0 + x0**3

def final_point(x0, a, b, additional_points=100, N=1000):
    for i in range(N-additional_points):
        x0 = logistic_map(x0, a, b)

    x0_additional_points = []
    for i in range(additional_points):
        x0 = logistic_map(x0, a, b)
        x0_additional_points.append(x0)

    return x0_additional_points


def make_array(x0, a, b, ap):
    a = np.arange(*a, dtype=np.float64)
    b = np.arange(*b, dtype=np.float64)
    abmap = [ [final_point(x0, i, j, ap) for j in b] for i in a]
    return np.array(abmap) #.shape((a.__len__(), b.__len__(), -1))

def interpret_map(abmap):
    colormap = [[len(set(j)) for j in i] for i in abmap]
    #abmap = [set(j, 4) for j in for i in abmap] # remove duplicates
    #colormap = len()
    return colormap

#TODO read how to make color map, please (matplotlib)

if __name__=="__main__":
    a = (-0.6, 0.6, 0.1)
    b = (0.8, 2.5, 0.1)
    abmap = make_array(0, a, b, ap=10)
    colormap = interpret_map(abmap)
    print(colormap)