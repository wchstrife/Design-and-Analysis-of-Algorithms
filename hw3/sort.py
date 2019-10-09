# -*- coding: utf-8 -*-

import time
import random
import sys

# 插入排序
def insertionsort(data):
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

# 归并排序
def mergesort(data, left, right):
    if right - left < 2:
        return 
    mid = int(round((left + right)/2))
    mergesort(data, left, mid)
    mergesort(data, mid, right)

    mergeCombine(data, left, right)

    return data

def mergeCombine(data, left, right):
    mid = int(round((left + right)/2))
    temp = []
    i = left
    j = mid
    while i < mid and j < right:
        if data[i] < data[j]:
            temp.append(data[i])
            i+=1
        else:
            temp.append(data[j])
            j+=1
    if i < mid:
        for k in range(i, mid):
            temp.append(data[k])
    if j < right:
        for k in range(mid, right):
            temp.append(data[k])

    for k in range(left, right):
        data[k] = temp[k - left]

    return data

# 希尔排序
def shellsort(data):
    # gap取Hibbard增量序列
    gap = 1
    while gap < len(data) / 3:
        gap = gap * 3 + 1

    while gap > 0:
        for i in range(gap, len(data)):     # 插入排序
            temp = data[i]
            j = i - gap
            while j >= 0 and data[j] > temp:
                data[j+gap] = data[j]
                j -= gap
            data[j + gap] = temp
        gap = int(round(gap / 3))

    return data

# 基数排序
# 先比较低位
def radixsort(data, n):
    for k in range(n):
        bucket = [[] for i in range(10)] # 表示10位数

        for i in data:
            t = round(i // (10 ** k) % 10)
            bucket[t].append(i)
        
        # 对桶中的元素进行组合
        j = 0
        for i in range(10): 
            if  len(bucket[i]) != 0:
                for x in bucket[i]:
                    data[j] = x
                    j+=1

    return data

def write2file(time, number, al_type):
    file = open('./data/data.txt', 'a', encoding='utf-8')
    file.write(str(number) + ' ')
    file.write(al_type + ' ')
    file.write(str(time) + ' ')
    file.write('\n')
    file.close()


if __name__ == "__main__":
    MAX = 2**32 - 1

    # 构造测试数量级
    for iter in range(10, 11):
        if iter == 9:
            data_number = 2 * 10**(iter - 1 )
        elif iter == 10:    
            data_number = 10**(iter - 1 )
        else:
            data_number = 10**(iter)

        print('*******************************')
        print('num of data: {}'.format(data_number))

        # 生成测试数据
        data = []
        for i in range(0, data_number):
            data.append(random.randint(0, MAX))

        ## 注意：在相同的数据规模下，对于不同算法的测试集应该是一样的
        # 快排测试
        start = time.perf_counter()
        data = quicksort(data, 0, len(data))
        end = time.perf_counter()
        print('quicksort: {}'.format(end - start))
        write2file(end-start, data_number, 'quicksort')
        #print(data)

        # 归并排序
        start = time.perf_counter()
        data = mergesort(data, 0, len(data))
        end = time.perf_counter()
        print('mergesort: {}'.format(end - start))
        write2file(end-start, data_number, 'mergesort')

        # 希尔排序
        start = time.perf_counter()
        data = shellsort(data)
        end = time.perf_counter()
        print('shellsort: {}'.format(end - start))
        write2file(end-start, data_number, 'shellsort')

        # 基数排序
        start = time.perf_counter()
        radixsort(data, iter)
        end = time.perf_counter()
        print('radixsort: {}'.format(end - start))
        write2file(end-start, data_number, 'radixsort')

        # 插入排序
        if iter <= 5:
            start = time.perf_counter()
            insertionsort(data)
            end = time.perf_counter()
            print('insertionsort: {}'.format(end - start))     
            write2file(end-start, data_number, 'insertionsort') 


        
            
            