# 递归法
def Cut_Rod(p, n):
    if n == 0:
        return 0
    max_value = -1
    for i in range(1, n+1):
        max_value = max(max_value, p[i] + Cut_Rod(p, n-i))

    return max_value

# 动态规划-带备忘的自顶向下方法
def Memoized_Cut_Rod(p, n):
    r = [-1] * (n + 1)
    return(Memoized_Cut_Rod_Aux(p, n, r))

def Memoized_Cut_Rod_Aux(p, n, r):
    if r[n] >= 0:
        return(r[n])
    if n == 0:
        max_value = 0
    else:
        max_value = -1
    for i in range(1, n+1):
        max_value = max(max_value, p[i] + Memoized_Cut_Rod_Aux(p, n-i, r))
    r[n] = max_value    # 记录下n时的最小值
    
    return max_value

# 动态规划-带备忘录的自顶向下方法-记录路径
def Extended_Memoized_Cut_Rod(p, n):
    r = [-1] * (n + 1)
    s = [0] * (n + 1)  # 记录最优解路径
    max_value = Extended_Memoized_Cut_Rod_Aux(p, n, r, s)
    print(r)
    print(s)
    print("最优解：%d" % r[n])
    while n > 0:
        print(s[n])
        n = n - s[n]

def Extended_Memoized_Cut_Rod_Aux(p, n, r, s):
    if r[n] >= 0:
        return (r[n])
    if n == 0:
        max_value = 0
    else:
        max_value = -1
    for i in range(1, n+1):
        temp = Extended_Memoized_Cut_Rod_Aux(p, n-i, r, s)
        if max_value < p[i] + temp:
            max_value = p[i] + temp
            s[n] = i    # 记录最优时切分点的位置
    r[n] = max_value    # 记录下n时的最小值
    
    return max_value


# 动态规划-自底向上
def Buttom_Up_Cut_Rod(p, n):
    r = [-1] * (n + 1)
    r[0] = 0
    for j in range(1, n+1):
        max_value = -1
        for i in range(1, j+1):
            max_value = max(max_value, p[i] + r[j-i])
        r[j] = max_value
    return r[n]

# 动态规划-自底向上-记录路径
def Extended_Buttom_Up_Cut_Rod(p, n):
    r = [-1] * (n + 1)
    r[0] = 0
    s = [0] * (n + 1)  # 记录最优解路径
    for j in range(1, n + 1):
        max_value = -1
        for i in range(1, j + 1):
            if max_value < p[i] + r[j-i]:
                max_value = p[i] + r[j-i]
                s[j] = i    # 记录最优时切分点的位置
        r[j] = max_value
    return r, s

def Print_Cut_Rod_Solution(p ,n):
    r, s = Extended_Buttom_Up_Cut_Rod(p, n)
    print(r)
    print(s)
    print("最优解：%d" % r[n])
    while n > 0:
        print(s[n])
        n = n - s[n]


if __name__ == "__main__":
    p = [0,1,5,8,9,10,17,17,20,24,30]
    # print(Cut_Rod(p, 9))
    # print(Memoized_Cut_Rod(p, 9))
    # print(Buttom_Up_Cut_Rod(p, 9))
    Print_Cut_Rod_Solution(p, 10)
    Extended_Memoized_Cut_Rod(p, 10)