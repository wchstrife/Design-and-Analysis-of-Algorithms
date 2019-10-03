#!/usr/bin/env python3
#-*- coding: utf-8 -*-
#made by wchstrife
#2019-10-03

import math
import random
import time

import sys

MAX_INT = 1000000    # 最多10万个点
MIN_INT = -1000000   # int的最小值
MAX_NUMBERS = 10000   # 生成最大数量的点对

trials = 10 # 每组做20次实验取平均值

# TODO: 1. 多次循环去平均值 2. 减少计算平方的计算量

def run(pairNumbers):

    totalTime = 0

    # 执行trials次实验取平均值
    for i in range(0, trials):
        Tstart = time.time()
        minpair, mindist = Solution(pairNumbers)
        Tfinish = time.time()
        totalTime += Tfinish - Tstart
        print('%dth experiment  closest pair point is :%s\nthe distance is :%s  TimeUsed: %s s \n' %(i, minpair, mindist, (Tfinish-Tstart)))
    print(MAX_NUMBERS, '规模下， 平均运行时间为：', totalTime / trials)
    file = open('Result-brute.txt', 'a', encoding='utf-8')
    file.write(str(pairNumbers) + ' ')
    file.write(str(totalTime / trials * 1000))
    file.write('\n')
    file.close()

def Solution(pairNumbers):

    # 随机生成测试数据
    AX = []
    AY = []
    for i in range(1, pairNumbers):
        AX.append(random.randint(0, MAX_INT))
        AY.append(random.randint(0, MAX_INT))
    PairPointA = list(zip(AX, AY))  #一维数组到二维数组
    #print(list(PairPointA)) 

    # 暴力法求解
    minpair, mindist = BruteSolution(PairPointA)

    # 分治法Y求解
    # SortedA_X = sorted(PairPointA, key = lambda point: point[0]) 
    # SortedA_Y = sorted(PairPointA, key = lambda point: point[1]) 
    # # print("分治法\n", SortedA_X, '\n', SortedA_X)

    # minpair, mindist = RecursiveSolution(SortedA_X, SortedA_Y)

    # fig = plt.figure()
    # ax = fig.add_subplot(111)
    # ax.scatter(AX, AY)
    # ax.scatter(minpair[0][0], minpair[0][1], color = 'red')
    # ax.scatter(minpair[1][0], minpair[1][1], color = 'green')
    # plt.show()

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


if __name__ == "__main__":
    for i in range(1000, 1001001, 20000):   # 从1000-100W 的规模进行测试
        run(i)
    