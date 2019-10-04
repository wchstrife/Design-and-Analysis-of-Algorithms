import numpy as np
import time

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

    trials = 10 # 10次取平均值
    MAX = 100

    for i in range(1, MAX):
        totalTime = 0
        
        for j in range(trials):
            Tstart = time.time()
            fib_matrix(i)
            Tfinish = time.time()
            totalTime += Tfinish - Tstart
        file = open('matrix-V1.txt', 'a', encoding='utf-8')
        file.write(str(i) + ' ')
        file.write(str(totalTime / trials * 1000))
        file.write('\n')
        file.close()