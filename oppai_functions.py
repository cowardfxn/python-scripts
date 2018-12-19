#!/bin/python3
# encoding: utf-8

import numpy as np
import matplotlib.pyplot as plt
from numpy import cos, sin, pi, square, exp
from matplotlib import gridspec


def plot_1():

    """
    琦玉大学(理学部)
    """

    a, b, c, d, m, n, p = 2.09, 1.31, 1.16, 0.885, 0.036, 0.615, 35.237

    theta = np.linspace(-2, 2, 2000, dtype=np.float64)

    x = a * exp(c * theta) * np.cos(c * theta) + exp(-np.power(theta - n, 2) / (2 * square(m))) / (p * np.sqrt(2 * pi * square(m)))
    y = b * exp(b * theta) * np.sin(d * theta)

    configs = {
        "figsize": (4, 9),
        "xlim": (0, 4),
        "ylim": (-1, 8)
    }

    return x, y, configs


def plot_2():
    """
    明治大学
    """

    t = np.linspace(0, 2*pi, 2000, dtype=np.float64)

    x = 13 * np.power(sin(t), 4)
    y = - 17 * cos(t) + 9 * cos(2 * t) - cos(3 * t) / 10 + cos(4 * t) + cos(5 * t) / 10

    configs = {
        "figsize": (3, 44/16 * 4),
        "xlim": (0, 14),
        "ylim": (-16, 28)
    }

    return x, y, configs


def plot_3():
    """
    广岛大学(理学部)
    """
    theta = np.linspace(-pi/2, pi/2, 2000, dtype=np.float64)

    x = (0.005 / (square(theta - pi / 2)) + 0.2 * exp(-110 * square(theta - 0.1 * pi)) + theta + pi / 2) * cos(theta)
    y = (0.005 / (square(theta - pi / 2)) + 0.2 * exp(-110 * square(theta - 0.1 * pi)) + theta + pi / 2) * sin(theta)

    configs = {
        "figsize": (4, 8),
        "xlim": (0, 4),
        "ylim": (-1, 6.5)
    }

    return x, y, configs


def plot_4():
    """
    东京农业大学
    """
    p = 3.0

    x = np.linspace(0, 6, 2000)
    y = p * square(1 - p / (square(pi) * (1 + pi))) * square(x) / exp((1 - p / np.power(pi, pi)) * x) + \
        square(p) * sin(p * (p/np.power(pi, pi) + x)/square(pi)) / (square(pi) * exp(x)) + \
        (np.power(p, 1/pi) / (2 * square(pi)) + np.power(pi, -3)) * exp(-np.power(pi, square(pi) - p / 2) * np.power(-p/(2*square(pi)) + x - 2 ,4)) + \
        (pi - np.sqrt(p)) / np.power(pi, pi) * exp(-square(pi) * (pi - 1) * square(-p/(2*pi**2) + x - 2)) + \
        p / np.power(pi, 4) * exp(-square(pi**2 * (-p / (2 * pi**2) + x - 2) / p))

    configs = {
        "figsize": (8, 3),
        "xlim": (0, 6.3),
        "ylim": (0, 2)
    }

    return x, y, configs


def plot_5():
    """
    文教大学
    """

    x = np.linspace(-3, 4, 2000)
    y = 4/ 5 * exp(-square(x) / 2) + exp(-square(6.9*x - 8.3)) / 8 + exp(-square(2 * x - 4.17)) / 6 + exp(-square(x - 1.4))

    configs = {
        "figsize": (8, 2),
        "xlim": (-3.2, 4.2),
        "ylim": (0, 1.6)
    }

    return x, y, configs


def plot_6():
    """
    京都大学  bug?
    """
    theta = np.linspace(-pi, 7 / 12 * pi, 2000)
    phi = (np.sqrt(5) - 1) / 2  # golden division
    b = np.log(phi) * 2 / pi
    a = np.arctan((-1 + np.sqrt(1 + square(b))) / b)

    x = exp(-np.power(pi, 4) * square(theta - a)) / square(pi) + cos(theta) * exp(b * theta) + 1
    y = exp(b * theta) * sin(theta) + pi / (1 + exp(-np.power(pi, 3) * (theta - 1.793))) - pi / (1 + exp(pi * (theta + pi)))

    configs = {
        "figsize": (2, 8),
        "xlim": (0, 2.5),
        "ylim": (-2, 4.5)
    }

    return x, y, configs


def plot_7():
    """
    首都大学东京(积分cycle)
    """

    x = np.linspace(-3, 2, 2000)
    y = 0.4 * exp(-0.04 * np.power(x, 8)) + 1.2 * exp(-0.5 * square(x)) + 0.1 * exp(-square(8*x -2)) + \
        0.2 * exp(-7*np.power(x - 0.8, 8)) + 0.4 * exp(-0.04 * np.power(x + 3, 8)) + exp(0.1 * x) - np.power(1.1, x -6) - \
        np.power(1.1, -x) - np.power(1.3, 0.6*x) + 1.2

    configs = {
        "figsize": (8, 3),
        "xlim": (-3, 2),
        "ylim": (-0.5, 1.6)
    }

    return x, y, configs


def plot_8():
    """
    大阪学校
    """
    x = np.linspace(-1, 3, 2000)
    y = (np.sqrt((abs(1-x) -x + 1)/ 2) + 1/4) * exp(-square(1-x)) + (abs(1 - 16 * np.power(5*x - 3, 4)) + abs(1 - 512 * np.power(5*x-3, 4)) - 528 * np.power(5*x-3, 4) + 2) / 40

    configs = {
        "figsize": (8, 2.3),
        "xlim": (-1, 3),
        "ylim": (0, 1)
    }

    return x, y, configs


def plot_9():
    """
    名古屋大学
    """
    y = np.linspace(-2, 3, 2000)
    x = 0.2 * (exp(-square(y+1)) + 1) / (exp(100*(y+1) - 16) + 1) + \
        1.5*exp(-0.62*square(y-0.16)) / (exp(-20*(5*y-1)) + 1) + \
        0.1 / exp(2 * np.power(10*y-1.2, 4)) + \
        (0.8*np.power(y-0.2, 3) + 1.5) / (exp(-(100*(y+1)-16)) + 1) / (exp(20*(5*y-1)) + 1)

    configs = {
        "figsize": (3, 8),
        "xlim": (0, 2),
        "ylim": (-2, 3)
    }

    return x, y, configs


def single_plot(x, y, configs):
    plt.figure(figsize=configs['figsize'])
    plt.xlim(configs['xlim'])
    plt.ylim(configs['ylim'])
    plt.plot(x, y)


def main():
    for i in range(9, 0, -1):
        plt_func = "plot_{}".format(i)
        func = globals().get(plt_func)
        if func:
            x, y, configs = func()
            single_plot(x, y, configs)

    plt.show()


if __name__ == "__main__":
    main()