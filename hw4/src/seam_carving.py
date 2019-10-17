import sys

import numpy as np
from imageio import imread, imwrite     # 读取图像的库
from scipy.ndimage.filters import convolve  # numpy之上的高级库
from tqdm import trange # 方便展示进度条

# 为每一个像素计算对应能量值
# 通过计算每个点的偏导绝对值之和-使用sobel滤波器
def calc_energy(img):
    filter_du = np.array([
        [1.0, 2.0, 1.0],
        [0.0, 0.0, 0.0],
        [-1.0, -2.0, -1.0],
    ])
    # 将2D滤波器->3D滤波器
    # 对应RGB三个通道
    filter_du = np.stack([filter_du] * 3, axis= 2)

    # 第二个滤波器
    filter_dv = np.array([
        [1.0, 0.0, -1.0],
        [2.0, 0.0, -2.0],
        [1.0, 0.0, -1.0],
    ])
    filter_dv = np.stack([filter_dv] * 3, axis=2)

    img = img.astype('float32')
    convolved = np.absolute(convolve(img, filter_du)) + np.absolute(convolve(img, filter_dv))   # 计算相邻单元的能量值

    # 将RGB中的能量相加
    energy_map = convolved.sum(axis=2)

    return energy_map


def min_seam(img):
    r, c, _ = img.shape
    energy_map = calc_energy(img)

    M = energy_map.copy()   # dp数组
    backtrack = np.zeros_like(M, dtype=np.int) # 记录回溯路径

    for i in range(1, r):
        for j in (0, c):
            # 单独处理图像的左边界，防止越界
            if j == 0:
                idx = np.argmin(M[i - 1, j:j + 2])  # 平铺返回最小值的下标
                backtrack[i, j] = idx + j           # barktrack记录上一层的j坐标
                min_energy = M[i-1, idx+j]
            else:
                idx = np.argmin(M[i-1, j-1 : j+2])
                backtrack[i, j] = idx + j - 1         # barktrack记录上一层的j坐标
                min_energy = M[i-1, idx + j - 1]

            M[i][j] += min_energy

    return M, backtrack
