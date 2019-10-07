import math
import numpy as np   
import random
#-------------------------------------------------------------------------------------------
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.pylab import mpl
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg,NavigationToolbar2Tk #NavigationToolbar2TkAgg
#------------------------------------------------------------------------------------------
from tkinter import *
import tkinter as tk
#------------------------------------------------------------------------------------------
 
 
mpl.rcParams['font.sans-serif'] = ['SimHei']  #中文显示
mpl.rcParams['axes.unicode_minus']=False      #负号显示
 
class From:
    def __init__(self): 
        self.root=tk.Tk()                    #创建主窗体
        self.canvas=tk.Canvas()              #创建一块显示图形的画布

        labelInput = tk.Label(self.root, text="input")
        labelInput.pack(side=TOP, fill=X, expand=YES)

        self.entryInput = tk.Entry(self.root)
        self.entryInput.pack(side=TOP, fill=Y, expand=YES)
        self.entryInput.insert(0, 5) # 默认三个点

        labelOutput = tk.Label(self.root, text="output")
        labelOutput.pack(side=TOP, fill=X, expand=YES)

        self.entryOutput = tk.Entry(self.root)
        self.entryOutput.pack(side=TOP, fill=Y, expand=YES)

        buttonQuit = tk.Button(self.root, text='Quit', command=self.root.quit)
        buttonQuit.pack()

        buttonRun = tk.Button(self.root, text='Run', command=self.drawPic)
        buttonRun.pack()

        self.figure=self.create_matplotlib() #返回matplotlib所画图形的figure对象
        self.create_form(self.figure)        #将figure显示在tkinter窗体上面

        self.root.mainloop()

    def drawPic(self):
        self.figure.clf()
        self.figure = self.create_matplotlib()
        self.create_form(self.figure)
 
    def create_matplotlib(self):
        #创建绘图对象f
        f=plt.figure(num=2,figsize=(8,6),dpi=80,facecolor="white",edgecolor='green',frameon=True)
        #创建一副子图
        fig1=plt.subplot(1,1,1)

        nums = int(self.entryInput.get())

        AX, AY = randomPairs(nums)
        
        fig1.scatter(AX,AY,color='green')    #画第一条线

        minpair, mindist = Solution(int(nums), AX, AY)
        
        fig1.scatter(minpair[0][0], minpair[0][1], color = 'red')
        fig1.scatter(minpair[1][0], minpair[1][1], color = 'red')

        self.entryOutput.insert(0, mindist)
        
        return f
 
    def create_form(self,figure):
        #把绘制的图形显示到tkinter窗口上
        self.canvas=FigureCanvasTkAgg(figure,self.root)
        self.canvas.draw()  #以前的版本使用show()方法，matplotlib 2.2之后不再推荐show（）用draw代替，但是用show不会报错，会显示警告
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
 
        #把matplotlib绘制图形的导航工具栏显示到tkinter窗口上
        toolbar =NavigationToolbar2Tk(self.canvas, self.root) #matplotlib 2.2版本之后推荐使用NavigationToolbar2Tk，若使用NavigationToolbar2TkAgg会警告
        toolbar.update()
        self.canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)


def randomPairs(pairNumbers):
    AX = []
    AY = []
    for i in range(0, pairNumbers):
        AX.append(random.randint(0, 200))
        AY.append(random.randint(0, 200))

    return AX, AY 

def Solution(pairNumbers, AX, AY):

    PairPointA = list(zip(AX, AY))  #一维数组到二维数组
    print(list(PairPointA)) 

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

if __name__=="__main__":
    form=From()