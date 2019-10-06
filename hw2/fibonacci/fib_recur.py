import time

# 递归法
def fib_recur(n):
    if n <= 1:
        return n
    return fib_recur(n - 1) + fib_recur(n - 2)

if __name__ == "__main__":

    trials = 10 # 10次取平均值
    MAX = 100

    for i in range(MAX):
        totalTime = 0
        
        for j in range(trials):
            Tstart = time.time()
            fib_recur(i)
            Tfinish = time.time()
            totalTime += Tfinish - Tstart
        file = open('./data/recur-V1.txt', 'a', encoding='utf-8')
        file.write(str(i) + ' ')
        file.write(str(totalTime / trials * 1000))
        file.write('\n')
        file.close()