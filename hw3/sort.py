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
    if right - left < 2:
        return
    pos = partition(data, left, right)
    quicksort(data, left, pos)
    quicksort(data, pos, right)

    return data
    

def partition(data, left, right):
    piovt = random.randint(left, right-1)


if __name__ == "__main__":
    data = [5, 4, 3, 2, 1]
    print(insertsort(data))