import tkinter as tk
import math
import random
import time

import matplotlib
import matplotlib.pyplot as plt
from matplotlib.pylab import mpl
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg,NavigationToolbar2Tk #NavigationToolbar2TkAgg

import numpy as np
import sys


root = tk.Tk()
root.title('求最近点对')
root.geometry("800x600")
App(root)

Label(root, text='输入随机数点对个数').grid(row=1, column=0)
Label(root, text='最近距离').grid(row=1,column=01)


root.mainloop()


class App:
    def __init__(self, master):
        self.master = master
        self.initWidgets()

    def initWidgets(self):
        
        Label(self.master, text='输入随机数点对个数').pack(side=TOP,fill=X, expand=YES)
        Label(fm1, text='输出').pack(side=TOP,fill=X, expand=YES)

        self.entryInput = tk.Entry(self.master)
        self.entryInput.pack(side=TOP,fill=Y, expand=YES)

        self.entryOutput = tk.Entry(self.master)
        self.entryOutput.grid(row=1, column = 1)
    

        buttonQuit = tk.Button(self.master, text='Quit', command=self.master.quit)
        buttonQuit.grid(row=2, column=0, padx=5, pady=5)

        buttonRun = tk.Button(self.master, text='Run', command=self.runSolution)
        buttonRun.grid(row=2, column=1, padx=5, pady=5)

        self.cv = tk.Canvas(self.master, width = 400, height = 200)
        self.cv.grid(row=3)

        self.canvas=tk.Canvas()              #创建一块显示图形的画布
        self.figure=self.create_matplotlib() #返回matplotlib所画图形的figure对象
        self.create_form(self.figure)        #将figure显示在tkinter窗体上面

    def runSolution(self):
        num = self.entryInput.get()
        AX, AY = randomPairs(num)
        minpair, mindist = Solution(int(num), AX, AY)
        self.entryOutput.insert(0, mindist)
        self.cv.create_line(minpair[0][0], minpair[0][1], minpair[1][0], minpair[1][1])

    def create_matplotlib(self, AX, AY, ):
        


def randomPairs(pairNumbers):
    AX = []
    AY = []
    for i in range(1, pairNumbers):
        AX.append(random.randint(0, 200))
        AY.append(random.randint(0, 200))
    return AX, AY 

def Solution(pairNumbers, AX, AY):

    PairPointA = list(zip(AX, AY))  #一维数组到二维数组
    #print(list(PairPointA)) 

    # 暴力法求解
    #minpair, mindist = BruteSolution(PairPointA)

    # 分治法Y求解
    SortedA_X = sorted(PairPointA, key = lambda point: point[0]) 
    SortedA_Y = sorted(PairPointA, key = lambda point: point[1]) 
    # print("分治法\n", SortedA_X, '\n', SortedA_X)

    minpair, mindist = RecursiveSolution(SortedA_X, SortedA_Y)

    # fig = plt.figure()
    # ax = fig.add_subplot(111)
    # ax.scatter(AX, AY)
    # ax.scatter(minpair[0][0], minpair[0][1], color = 'red')
    # ax.scatter(minpair[1][0], minpair[1][1], color = 'green')
    # plt.show()

    print(mindist)
    return minpair, mindist


# 暴力法求最近点对, 时间复杂度O(n^2)
def BruteSolution(PairPointA):
    Alen = len(PairPointA)
    #初始化 mindist, minpair
    mindist = GetDistance(PairPointA[0], PairPointA[1])
    minpair = (PairPointA[0], PairPointA[1])
    #遍历 
    for i in range(0, Alen-2):
        for j in range(i+1, Alen-1):
            dist = GetDistance(PairPointA[i], PairPointA[j])
            if mindist > dist:
                mindist = dist
                minpair = (PairPointA[i], PairPointA[j])
    return minpair, mindist


# 分治法求最近点对，时间复杂度O(nlogn)
def RecursiveSolution(SortedA_X, SortedA_Y):
    SortedA_len = len(SortedA_X)
    if SortedA_len <= 3:   # 递归出口：小于3时采用暴力法
        minpair, mindist = BruteSolution(SortedA_X)
        return minpair, mindist
    else:
        midx = SortedA_len // 2   # 整数除法，求分治中点
        # 划分分治的左右区间按x排列的点对
        SortedA_XL = SortedA_X[0: midx]
        SortedA_XR = SortedA_X[midx:]
        SortedA_YL = []
        SortedA_YR = []
        # 划分左右区间按y排列的点对
        midX_value = SortedA_X[midx][0]
        for point in SortedA_Y:
            if point[0] < midX_value:
                SortedA_YL.append(point)
            else:
                SortedA_YR.append(point)
        # 递归
        minpair_L, mindist_L = RecursiveSolution(SortedA_XL, SortedA_YL)
        minpair_R, mindist_R = RecursiveSolution(SortedA_XR, SortedA_YR)
        # 合并
        if mindist_L < mindist_R:
            minpair = minpair_L
            mindist = mindist_L
        else:
            minpair = minpair_R
            mindist = mindist_R
        
        # 判断区域内的最小值
        minpair_M, mindist_M = MidAreaMin(SortedA_X, SortedA_Y, mindist)

        if mindist_M < mindist:
            minpair = minpair_M
            mindist = mindist_M

    return minpair, mindist


# 求区域内的点的距离最小值
def MidAreaMin(SortedA_X, SortedA_Y, delta):
    # 获得x坐标在[mid-delta, mid+delta]的点，并按y坐标排序
    SortedA_len = len(SortedA_X)
    midX_value = SortedA_X[SortedA_len // 2][0]
    SortedA_Y_delta = []
    # 判断按Y排序的点对中，X是否在范围内,复杂度O(n)
    for point in SortedA_Y:
        if midX_value - delta <= point[0] and point[0] <= midX_value + delta:
            SortedA_Y_delta.append(point)

    SortedA_Y_len = len(SortedA_Y_delta)

    if SortedA_Y_len <= 1:  # 处理过的y数组可能只有一个元素，需要单独处理
        return ((0,0), (0, 0)) , (delta +1) # 返回一个大于delta的距离，来忽略这类情况
    mindist = GetDistance(SortedA_Y_delta[0], SortedA_Y_delta[1])
    minpair = (SortedA_Y_delta[0], SortedA_Y_delta[1])

    for i in range(0, SortedA_Y_len - 2):
        for j in range(i +1, min(i + 5, SortedA_Y_len - 1)): # 只需要判断每隔点后面5个点即可
            dist = GetDistance(SortedA_Y_delta[i], SortedA_Y_delta[j])
            if dist < mindist:
                mindist = dist
                minpair = (SortedA_Y_delta[i], SortedA_Y_delta[j])

    return minpair, mindist


# 计算两点的距离
def GetDistance(point1, point2):
    # distc = sqrt( (x1-x2)**2 + (y1 - y2)**2 )
    return math.sqrt( (point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)
    #return (point1[0] - point2[0])**2 + (point1[1] - point2[1])**2  # 比较距离的时候不开平方







