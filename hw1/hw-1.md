# Homework-1

## **1. Prove $2n + \Theta(n^2) =  \Theta(n^2)$**

即证
 $$ \exists c_1, c_2, n_1 \in \mathbb{R}^+, \forall n \geq n_1, 0 \leq c_1n^2\leq 2n + \Theta(n^2) \leq c_2n^2 $$

根据$\Theta(n^2)$的定义可知：

 $$ \exists c_3, c_4, n_2 \in \mathbb{R}^+, \forall n \geq n_2, 0 \leq c_3n^2 \leq  f(n) \leq c_4n^2 $$

 进一步放缩：

  $$ \exists c_3, c_4, n_2 \in \mathbb{R}^+, \forall n \geq n_0, 0 \leq c_3n^2 \leq c_3n^2 + 2n \leq  f(n) + 2n\leq c_4n^2 + 2n \leq (c_4 + 2)n^2 $$

 取$n_0 = max(n_1, n_2)， \forall n \geq n_0$， 当$c_1 = c_3$， $c_2 = c_4 + 2$时

 $$ \exists c_1, c_2, n_0 \in \mathbb{R}^+, \forall n \geq n_0, 0 \leq c_1n^2\leq 2n + \Theta(n^2) \leq c_2n^2 $$

 即：

 $$2n + \Theta(n^2) =  \Theta(n^2)$$

 &nbsp;
 &nbsp;

## **2. Prove $\Theta(g(n)) \cap\  o(g(n)) = \phi$**

反证法：

假设 $f(n) = \Theta(g(n)) \cap\  o(g(n))$, 则$f(n)同时满足$：

$$ \exists c_1, c_2, n_0 \in \mathbb{R}^+, \forall n \geq n_1, 0 \leq c_1g(n)\leq f(n) \leq c_2g(n) $$

$$ \forall c_3, \exists n_0\geq0,  \forall n \geq n_2,  0 \leq f(n)  < c_3g(n)  $$

取$n_0 = max(n_1, n_2)， \forall n \geq n_0$， 当$c_1 = c_3$时
$$ c_1g(n)\leq f(n) < c_1g(n)$$

此式不成立，因此假设不存在，即：

$$\Theta(g(n)) \cap\  o(g(n)) = \phi$$

 &nbsp;
 &nbsp;

## **3. Prove $\Theta(g(n)) \cup\  o(g(n)) \neq\ O(g(n))$**

反证法：

假设$\Theta(g(n)) \cup\  o(g(n)) = O(g(n))$

对于$f(n) = n^2\left| cos(n)  \right|$

$$  \exists c_1, n_0 \in \mathbb{R}^+, \forall n \geq n_0, 0 \leq  n^2\left| cos(n)  \right| \leq c_1n^2 $$

当$c_1=1$时，上式成立，所以$f(n) = O(n^2)$

同理可证$f(n) \neq\ \Theta(n^2)$ 且 $f(n) \neq\ o(n^2)$

因此假设不成立，即：

$$\Theta(g(n)) \cup\  o(g(n)) \neq\ O(g(n))$$

 &nbsp;
 &nbsp;

## **4. Prove $\max(f(n),g(n)) = \Theta(f(n)+g(n))$**

即证

$$ \exists c_1, c_2, n_0 \in \mathbb{R}^+, \forall n \geq n_0, 0 \leq c_1(f(n) + g(n))\leq max(f(n), g(n)) \leq c_2(f(n) + g(n)) $$

取 $c_1 = 0.5, c_2 = 1$时，不等式成立

即:

 $$\max(f(n),g(n)) = \Theta(f(n)+g(n))$$

&nbsp;
&nbsp;

## **5. Solve the recurrence $\ T(n) = 2T (\sqrt{n}) + 1$**

令 $m = lgn$

则：

$$T(2^m) = 2T(2^\tfrac{m}{2}) + 1$$

令 $S(m) = T(2^m)$

则：

$$S(m) = 2T(m/2) + 1$$

根据主方法得：

$$S(m) = \Theta(m) = \Theta(lgn)$$

 &nbsp;
 &nbsp;

## **6. Solve the recurrence $\ nT(n) = (n-2)T(n-1) +2$**

等式两边同乘 $n-1$ 得:

 $$\ n(n-1)T(n) = (n-2)(n-1)T(n-1) + 2(n-1)$$

 设$S(n) = n(n-1)T(n)$, 上式则可以写成：

 $$S(n) = S(n-1) + 2(n-1)$$

 由累加递推式可得：$S(n) = n(n-1)$

 所以$T(n) = 1$, 即 $T(n) = \Theta(1)$

 &nbsp;
 &nbsp;

## **7. CLRS, Page 35, 3-3**

### a.

阶从高到底排列，同行为一等价类：

$$ \begin{array}{ll} 2^{2^{n + 1}} & \\ 2^{2^n} & \\ (n + 1)! & \\ n! & \\ e^n & \\ n\cdot 2^n & \\ 2^n & \\ (3 / 2)^n & \\ (\lg n)^{\lg n} \text{ and } n^{\lg\lg n} & \\ (\lg n)! & \\ n^3 & \\ n^2 \text{ and } 4^{\lg n} & \\ n\lg n \text{ and } \lg(n!) & \\ n \text{ and } 2^{\lg n} & \\ (\sqrt 2)^{\lg n} & \\ 2^{\sqrt{2\lg n}} & \\ \lg^2 n & \\ \ln n & \\ \sqrt{\lg n} & \\ \ln\ln n & \\ 2^{\lg^*n} & \\ \lg^*n \text{ and } \lg^*(\lg n) & \\ \lg(\lg^*)n & \\ n^{1 / \lg n} \text{ and } 1 & \end{array} $$

### b.

要满足$f(n)既不是O(g_i(n)) 也不是 \Omega(g_i(n))$, 

可以使$f(n)$的上临界大于$O(g_i(n))$的最大值，下邻界小于$\Omega(g_i(n))$的最小值,

根据这个思路可以设计以下函数：

$$ y=\begin{cases}
2^{2^{n+2}},\quad x \% 2 == 0 \\
0,  \quad x \% 2 == 1
\end{cases} $$