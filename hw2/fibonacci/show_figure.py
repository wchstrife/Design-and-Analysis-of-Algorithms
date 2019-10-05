#!/usr/bin/env python3
#-*- coding: utf-8 -*-
#made by wchstrife
#2019-10-3

import matplotlib
import matplotlib.pyplot as plt

def readFile(input_txt):

    file = open(input_txt, 'r')
    X = []
    Y = []

    for line in file:
        line = line.strip('\n')
        line = line.split(' ')
        X.append(line[0])
        Y.append(line[1])
    
    file.close

    return X, Y


def showFigure(X1, Y1, X2, Y2, X3, Y3):

    plt.subplot(1, 3, 1)
    plt.plot(X1, Y1)
    plt.title('Recurcive Method')
    plt.ylabel('Time(ms)')
    plt.xlabel('N')
    plt.xlim(0, 50)
    plt.xticks(range(0, 50, 5))
    plt.ylim(0, 800001)
    plt.xticks(range(0, 800001, 100000))

    plt.subplot(1, 3, 2)
    plt.plot(X2, Y2)
    plt.title('Matrix Method')
    plt.ylabel('Time(ms)')
    plt.xlabel('N')
    plt.xlim(0, 50)
    plt.xticks(range(0, 50, 5))
    plt.ylim(0, 800001)
    plt.xticks(range(0, 800001, 100000))

    plt.subplot(1, 3, 3)
    plt.plot(X3, Y3)
    plt.title('Loop Method')
    plt.ylabel('Time(ms)')
    plt.xlabel('N')
    plt.xlim(0, 50)
    plt.xticks(range(0, 50, 5))
    plt.ylim(0, 800001)
    plt.xticks(range(0, 800001, 100000))

    plt.show()

if __name__ == "__main__":
    X1 ,Y1 = readFile("recur-V1.txt")
    X2 ,Y2 = readFile("matrix-V1.txt")
    X3 ,Y3 = readFile("loop-V1.txt")
    showFigure(X1, Y1, X2, Y2, X3, Y3)