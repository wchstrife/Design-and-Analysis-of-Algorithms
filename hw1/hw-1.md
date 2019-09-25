# Homework-1

## 1. Prove $2n + \Theta(n^2) =  \Theta(n^2)$

即证
 $$ \exists c_1, c_2, n_0 \in \mathbb{R}^+, \forall n \geq n_0, 0 \leq c_1n^2\leq 2n + \Theta(n^2) \leq c_2n^2 $$

 即

 $$ \exists c_1, c_2, n_0 \in \mathbb{R}^+, \forall n \geq n_0, 0 \leq c_1n^2 - 2n\leq  \Theta(n^2) \leq c_2n^2 - 2n$$

 由$\Theta(n^2)$的定义可知上式成立

## 2. Prove $\Theta(g(n)) \cap\  o(g(n)) = \phi$

反证法：

假设 $f(n) = \Theta(g(n)) \cap\  o(g(n))$

$$ \exists c_1, c_2, n_0 \in \mathbb{R}^+, \forall n \geq n_0, 0 \leq c_1g(n)\leq f(n) \leq c_2g(n) $$

$$ \forall c_3, \exists n_0\geq0,  \forall n \geq n_0,  0 \leq f(n)  < c_3g(n)  $$

当$c_1 = c_3$时，
$$ c_1g(n)\leq f(n) < c_1g(n)$$

此式不成立，因此假设不存在，即：

$$\Theta(g(n)) \cap\  o(g(n)) = \phi$$

## 3. Prove $\Theta(g(n)) \cup\  o(g(n)) \neq\ O(g(n))$

## 4. Prove $\max(f(n),g(n)) = \Theta(f(n)+g(n))$

即证

$$ \exists c_1, c_2, n_0 \in \mathbb{R}^+, \forall n \geq n_0, 0 \leq c_1(f(n) + g(n))\leq max(f(n), g(n)) \leq c_2(f(n) + g(n)) $$

当$c_1 = 0.5, c_2 = 1$时，不等式成立

即:

 $$\max(f(n),g(n)) = \Theta(f(n)+g(n))$$

## 5. Solve the recurrence $\ T(n) = 2T (\sqrt{n}) + 1$

令 $m = lgn$

则：

$$T(2^m) = 2T(2^\tfrac{m}{2}) + 1$$

令 $S(m) = T(2^m)$

则：

$$S(m) = 2T(2^m) + 1$$

根据主方法得

$$S(m) = \Theta(m) = \Theta(lgn)$$

## 6. Solve the recurrence $\ nT(n) = (n-2)T(n-1) +2$

## 7. CLRS, Page 35, 3-3

### a.

$$ \begin{array}{ll} 2^{2^{n + 1}} & \\ 2^{2^n} & \\ (n + 1)! & \\ n! & \\ e^n & \\ n\cdot 2^n & \\ 2^n & \\ (3 / 2)^n & \\ (\lg n)^{\lg n} = n^{\lg\lg n} & \\ (\lg n)! & \\ n^3 & \\ n^2 = 4^{\lg n} & \\ n\lg n \text{ and } \lg(n!) & \\ n = 2^{\lg n} & \\ (\sqrt 2)^{\lg n}(= \sqrt n) & \\ 2^{\sqrt{2\lg n}} & \\ \lg^2 n & \\ \ln n & \\ \sqrt{\lg n} & \\ \ln\ln n & \\ 2^{\lg^*n} & \\ \lg^*n \text{ and } \lg^*(\lg n) & \\ \lg(\lg^*)n & \\ n^{1 / \lg n}(= 2) \text{ and } 1 & \end{array} $$

### b.

选取震荡型的函数，例如：
$$2^{2^{\sin n}}$$