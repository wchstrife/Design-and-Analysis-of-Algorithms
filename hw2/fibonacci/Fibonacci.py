#!/usr/bin/env python3
#-*- coding: utf-8 -*-
#made by wchstrife
#2019-10-3

import numpy as np

# 递归法
def fib_recur(n):
    if n <= 1:
        return n
    return fib_recur(n - 1) + fib_recur(n - 2)

# 递推法
def fib_loop(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a

# 矩阵法
def fib_matrix_tool(n):
    Matrix = np.matrix("1 1;1 0", dtype=np.int64)
    return pow(Matrix, n)

def fib_matrix(n):
    result = []
    for i in range(0, n):
        result.append(np.array(fib_matrix_tool(i))[0][0])
    return result[-1]

if __name__ == "__main__":
    #print(fib_recur(30))
    print(fib_loop(10))
    #print(fib_matrix(93))
    #print(2**64 - fib_loop(90))
    for i in range(10):
        print(fib_loop(i), " ")



