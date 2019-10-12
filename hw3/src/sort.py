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
def quicksort(arr,low,high): 
    if low < high: 
  
        pi = partition(arr,low,high) 
  
        quicksort(arr, low, pi-1) 
        quicksort(arr, pi+1, high)

    return arr
    
def partition(arr,low,high): 
    i = ( low-1 )         # 最小元素索引
    pivot = arr[high]     
  
    for j in range(low , high): 
  
        # 当前元素小于或等于 pivot 
        if   arr[j] <= pivot: 
          
            i = i+1 
            arr[i],arr[j] = arr[j],arr[i] 
  
    arr[i+1],arr[high] = arr[high],arr[i+1] 
    return ( i+1 ) 

# 归并排序
def mergesort(data, left, right):
    mid = int( round((left + right) / 2) )
    if right - left > 1:
        mergesort(data, left, mid)
        mergesort(data, mid, right)
    else:
        return
    mergeCombine(data, left, right)

    return data

def mergeCombine(data, left, right):
    mid = int(round((left + right)/2))
    temp = []
    i = left
    j = mid
    while (i < mid and j < right):
        if data[i] <= data[j]:
            temp.append(data[i])
            i+=1
        else:
            temp.append(data[j])
            j+=1
    if i < mid:
        for k in range(i, mid):
            temp.append(data[k])
    if j < right:
        for k in range(j, right):
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
def radixsort(data, digit):
    for k in range(digit):  # 这里k取的取值在后面测试数据当中有点小bug
        bucket = [[] for i in range(10)] # 表示10位数

        for i in data:
            t = round(i // (10 ** k) % 10)
            bucket[t].append(i)
        
        # 对桶中的元素进行组合
        data = [j for i in bucket for j in i]
        # j = 0
        # for i in range(10): 
        #     if  len(bucket[i]) != 0:
        #         for x in bucket[i]:
        #             data[j] = x
        #             j+=1

    return data

def write2file(time, number, al_type):
    file = open('data.txt', 'a', encoding='utf-8')
    file.write(str(number) + ' ')
    file.write(al_type + ' ')
    file.write(str(time) + ' ')
    file.write('\n')
    file.close()


if __name__ == "__main__":
    MAX = 2**32 - 1
    #MAX = 10000

    # 构造测试数量级
    for iter in range(1, 11):
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
        temp = data

        ## 注意：在相同的数据规模下，对于不同算法的测试集应该是一样的
        # 快排测试
        start = time.perf_counter()
        data = quicksort(data, 0, len(data)-1)
        end = time.perf_counter()
        print('quicksort: {}'.format(end - start))
        write2file(end-start, data_number, 'quicksort')
        #print(data)
        data = temp

        # 归并排序
        start = time.perf_counter()
        data = mergesort(data, 0, len(data))
        end = time.perf_counter()
        print('mergesort: {}'.format(end - start))
        write2file(end-start, data_number, 'mergesort')
        #print(data)
        data = temp

        # 希尔排序
        start = time.perf_counter()
        data = shellsort(data)
        end = time.perf_counter()
        print('shellsort: {}'.format(end - start))
        write2file(end-start, data_number, 'shellsort')
        #print(data)
        data = temp
        

        # 基数排序
        start = time.perf_counter()
        radixsort(data, iter)
        end = time.perf_counter()
        print('radixsort: {}'.format(end - start))
        write2file(end-start, data_number, 'radixsort')
        data = temp
        #print(data)

        # 插入排序
        if iter <= 5:
            start = time.perf_counter()
            insertionsort(data)
            end = time.perf_counter()
            print('insertionsort: {}'.format(end - start))     
            write2file(end-start, data_number, 'insertionsort') 
            #print(data)
            


        
            
            