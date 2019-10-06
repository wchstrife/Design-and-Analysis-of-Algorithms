import time

# 递推法
def fib_loop(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a


if __name__ == "__main__":

    trials = 10 # 10次取平均值
    MAX = 1000000

    for i in range(1, MAX, 10000):
        totalTime = 0
        
        for j in range(trials):
            Tstart = time.time()
            fib_loop(i)
            Tfinish = time.time()
            totalTime += Tfinish - Tstart
        file = open('./data/loop-V1.txt', 'a', encoding='utf-8')
        file.write(str(i) + ' ')
        file.write(str(totalTime / trials * 1000))
        file.write('\n')
        file.close()