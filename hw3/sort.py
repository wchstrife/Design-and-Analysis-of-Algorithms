# -*- coding: utf-8 -*-

import time
import random

# 插入排序
def insertsort(data):
    for i in range(0, len(data)):
        temp = data[i]
        j = i - 1
        while j >= 0 and temp < data[j]:
            data[j+1] = data[j]
            data[j] = temp
            j -= 1

    return data

# 快速排序
def quicksort(data, left, right):   
    if right - left < 2:    # 左闭右开，一个元素时已经有序
        return
    pos = partition(data, left, right)
    quicksort(data, left, pos)
    quicksort(data, pos + 1, right)

    return data
    

def partition(data, left, right):
    piovt = random.randint(left, right-1) # 随机选择轴点，注意randint()是闭区间
    # 将随机选择的点放到末尾
    temp = data[piovt]
    data[piovt] = data[right - 1]
    data[right - 1] = temp

    i = left - 1    # i前的点表明是小于pivot的，i之后的表明是大于pivot的
    for j in range(left, right - 1):
        if data[j] <= data[piovt]: # 说明j指的元素小于pivot 要放在i+1的位置
            i += 1
            temp = data[i]
            data[i] = data[j]
            data[j] = temp
    # 将pivot放在i+1后面
    temp = data[i+1]
    data[i+1] = data[right - 1]
    data[right - 1] = temp

    return i + 1


if __name__ == "__main__":
    data = [5, 4]
    print(quicksort(data, 0, len(data)))