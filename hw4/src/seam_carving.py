import sys

import numpy as np
from imageio import imread, imwrite     # 读取图像的库
from scipy.ndimage.filters import convolve  # numpy之上的高级库
from tqdm import trange # 方便展示进度条
import getopt   # 处理命令行参数

# TODO shape维度
# TODO 可视化删掉的红线
# TODO 动态的展示删除的效果
# TODO 注释规范
# TODO 旋转+命令行参数化

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

# 寻找需要删除的缝
def min_seam(img):
    r, c, _ = img.shape
    energy_map = calc_energy(img)

    M = energy_map.copy()   # dp数组
    backtrack = np.zeros_like(M, dtype=np.int) # 记录回溯路径

    for i in range(1, r):
        for j in range(0, c):    # TODO 这里需要处理右边界
            # 单独处理图像的左边界，防止越界
            if j == 0:
                idx = np.argmin(M[i - 1, j : j + 2])  # 平铺返回最小值的下标
                backtrack[i, j] = idx + j           # barktrack记录上一层的j坐标
                min_energy = M[i - 1, idx + j]
            # elif j == c - 1:
            #     idx = np.argmin(M[i - 1, j - 1 : j + 1])  # 处理右边界
            #     backtrack[i, j] = idx + j - 1        
            #     min_energy = M[i - 1, idx + j - 1]
            else:
                idx = np.argmin(M[i - 1, j - 1 : j + 2])
                backtrack[i, j] = idx + j - 1         # barktrack记录上一层的j坐标
                min_energy = M[i - 1, idx + j - 1]

            M[i][j] += min_energy

    return M, backtrack

# 删除从上到下的一条缝
def carve_column(img):
    r, c, _ = img.shape

    M, backtrack = min_seam(img)

    # (r, c)的矩阵，默认值为True,随后删除所有值为false的像素
    mask = np.ones((r, c), dtype=np.bool)

    # 回溯寻找要删除的线
    j = np.argmin(M[-1])    # 图片最下面一行能量的最小值

    for i in reversed(range(r)):    # 从下往上搜索
        mask[i, j] = False
        j = backtrack[i][j]

    # RGB三个通道
    mask = np.stack([mask] * 3, axis=2)

    img = img[mask].reshape((r, c - 1, 3))  # 删除false的值

    return img

# 按列删除
def crop_c(img, scale_c):
    _, c, _ = img.shape
    new_c = int(c * scale_c)

    for _ in trange(c - new_c): # trange可以显示进度条
        img = carve_column(img)

    return img

# 按行删除
def crop_r(img, scale_r):
    img = np.rot90(img, 1, (0, 1))  # 将数组旋转90度
    img = crop_c(img, scale_r)
    img = np.rot90(img, 3, (0, 1))  # 将数组旋转270度转回去

    return img

def main():
    # scale = float(sys.argv[1])
    # in_filename = sys.argv[2]
    # out_filename = sys.argv[3]

    # img = imread(in_filename)
    # print(img.shape)
    # out = crop_c(img, scale)
    # imwrite(out_filename, out)

    column_rate = 0.5
    row_rate = 0.5
    inputfile = ''
    outfile = ''

    # 读取命令行参数
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hi:o:r:c:", ["help", "ifile=", "ofile=", "row_rate=", "column_rate="])
    except getopt.GetoptError:
        print('Error: seam_carving.py -i <inputfile> -o <outputfile> -r <row_rate> -c <column_rate>')
        print('   or: seam_carving.py --ifile=<inputfile> --ofile=<outputfile> --row_rate=<row_rate> --column_rate=<column_rate>')
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print('Help: seam_carving.py -i <inputfile> -o <outputfile> -r <row_rate> -c <column_rate>')
            print('   or: seam_carving.py --ifile=<inputfile> --ofile=<outputfile> --row_rate=<row_rate> --column_rate=<column_rate>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outfile = arg
        elif opt in ("-r", "--row_rate"):
            row_rate = float(arg)
        elif opt in ("-c", "--column_rate"):
            column_rate = float(arg)  

    img = imread(inputfile)
    temp = crop_c(img, column_rate)
    out = crop_r(temp, row_rate)
    imwrite(outfile, out)

if __name__ == '__main__':
    main()

