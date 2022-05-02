import numpy as np
import math
from matplotlib import pyplot as plt
import matplotlib.patches as patches


def plot(x, y, string, number, delta, e, res, s, error):
    plt.figure(number)
    plt.clf()
    fig, ax = plt.subplots()
    ax.plot(x, y, linewidth=2, color="Blue")
    ax.text(-0.1, 0.82, f'countPoints {res} \nintegralSum {round(s, 6)} \nintegralSumNL 2\n'
                       f'errorOfSum {round(abs(s - 2), 6)}\ntheoreticalError {round(error, 6)}\ntheoreticalError {abs(s - 2) < error}\nLessSum',
            fontsize=7, weight="bold")
    for i in range(len(e)):
        ax.add_patch(
            patches.Rectangle(
                (delta * i, 0),
                delta,
                e[i],
                edgecolor='blue',
                facecolor='red',
                fill=True
            ))
    ax.grid(True)
    plt.title(string, fontsize=14, fontweight="bold")
    plt.xlabel('x', fontsize=14)
    plt.ylabel('y', fontsize=14)

    plt.savefig(str(number) + ".png", dpi=500)


def integer(countPoints, typeEquipment):
    # x = [0] * countPoints
    # for i in range(1, countPoints):
    #     x[i] = math.pi * i / (countPoints - 1)
    e = [0] * (countPoints)
    dx = math.pi / (countPoints)
    error = 0
    if 0 <= typeEquipment <= 3:
        if typeEquipment == 0:
            for i in range(countPoints):
                e[i] = i * math.pi / (countPoints)
            error = math.pi ** 2 / (2 * countPoints)
        elif typeEquipment == 1:
            for i in range(countPoints):
                e[i] = (i + 0.5) * math.pi / (countPoints)
            error = math.pi ** 3 / (24 * countPoints ** 2)
        elif typeEquipment == 2:
            for i in range(countPoints):
                e[i] = (i + 1) * math.pi / (countPoints)
            error = math.pi ** 2 / (2 * countPoints)
        s = 0
        matSum = []
        for i in range(countPoints):
            s += math.sin(e[i]) * dx
        for i in range(countPoints):
            matSum.append(math.sin(e[i]))
        a = [i * math.pi / 1000 for i in range(1000)]
        y = [math.sin(i) for i in a]
        plot(a, y, "Integral sum and graph sin(x)", str(typeEquipment) + "_" + str(countPoints), dx, matSum, countPoints, s, error)

    else:
        print("out of range [0, 2] equipment")


print("please input countPoints:")
count = int(input())
print("please input typeEquipment: 0 - left, 1 - middle, 2 - right:")
typ = int(input())
integer(count, typ)


