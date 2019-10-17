import sys
from PIL import Image
import numpy as np
import sys, getopt


def choose_min_j(dp, i, js, n):
    mini = sys.maxsize
    pre = -1
    for x in js:
        if 1 <= x <= n and dp[i][x] < mini:
            mini = dp[i][x]
            pre = x
    return mini, pre


def choose_min_i(dp, j, i_s, m):
    mini = sys.maxsize
    pre = -1
    for x in i_s:
        if 1 <= x <= m and dp[x][j] < mini:
            mini = dp[x][j]
            pre = x
    return mini, pre


def seam_carving(d, axis=0):
    m = len(d)
    n = len(d[0])
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    pre_path = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    answer = sys.maxsize
    if axis == 0:
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j], pre = choose_min_j(dp, i - 1, [j - 1, j, j + 1], n)
                dp[i][j] += d[i - 1][j - 1]
                pre_path[i][j] = pre
        pre = -1
        for j in range(1, n + 1):
            if dp[m][j] < answer:
                answer = dp[m][j]
                pre = j
        path = [0 for _ in range(m)]
        for i in range(m - 1, -1, -1):
            path[i] = pre - 1
            pre = pre_path[i][pre]
    else:
        for j in range(1, n + 1):
            for i in range(1, m + 1):
                dp[i][j], pre = choose_min_i(dp, j - 1, [i - 1, i, i + 1], m)
                dp[i][j] += d[i - 1][j - 1]
                pre_path[i][j] = pre
        pre = -1
        for i in range(1, m + 1):
            if dp[i][n] < answer:
                answer = dp[i][n]
                pre = i
        path = [0 for _ in range(n)]
        for j in range(n - 1, -1, -1):
            path[j] = pre - 1
            pre = pre_path[pre][j]
    return answer, path


def cal_energy(im_array):
    height = len(im_array)
    width = len(im_array[0])
    answer = [[0 for _ in range(width)] for _ in range(height)]
    for i in range(height):
        for j in range(width):
            if i == 0:
                vertical = im_array[i + 1][j]
            elif i == height - 1:
                vertical = im_array[i - 1][j]
            else:
                vertical = abs(im_array[i + 1][j] - im_array[i - 1][j])

            if j == 0:
                horizon = im_array[i][j + 1]
            elif j == width - 1:
                horizon = im_array[i][j - 1]
            else:
                horizon = abs(im_array[i][j + 1] - im_array[i][j - 1])
            answer[i][j] = vertical + horizon
    return answer


def remove(image, path, axis=0):
    m = len(image)
    n = len(image[0])
    if axis == 0:
        new_image = np.zeros(shape=[m, n - 1, 3], dtype=np.uint8)
        for i in range(m):
            k = 0
            for j in range(n):
                if j != path[i]:
                    new_image[i][k][0] = image[i][j][0]
                    new_image[i][k][1] = image[i][j][1]
                    new_image[i][k][2] = image[i][j][2]
                    k += 1
    else:
        new_image = np.zeros(shape=[m - 1, n, 3], dtype=np.uint8)
        for j in range(n):
            k = 0
            for i in range(m):
                if i != path[j]:
                    new_image[k][j][0] = image[i][j][0]
                    new_image[k][j][1] = image[i][j][1]
                    new_image[k][j][2] = image[i][j][2]
                    k += 1
    return new_image


def for_one_carving(image, axis):
    im_array = np.array(image)
    gray = image.convert('L')
    gray_array = np.array(gray, np.int32)
    energy = cal_energy(gray_array)
    _, path = seam_carving(energy, axis=axis)
    new_arrary = remove(im_array, path, axis=axis)
    return Image.fromarray(new_arrary)


def show_one_seam(image):
    im_array = np.array(image)
    gray = image.convert('L')
    gray_array = np.array(gray, np.int32)
    energy = cal_energy(gray_array)
    _, path = seam_carving(energy, axis=0)
    for i in range(len(path)):
        im_array[i][path[i]][0] = 255
        im_array[i][path[i]][1] = 0
        im_array[i][path[i]][2] = 0
    return Image.fromarray(im_array)


if __name__ == '__main__':
    inputfile = ''
    outputfile = ''
    row_rate = 100
    column_rate = 100
    if_show_one_seam = False
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hi:o:r:c:s", ["help", "ifile=", "ofile=", "row_rate=", "column_rate="])
    except getopt.GetoptError:
        print('CLRS_15-8.py -i <inputfile> -o <outputfile> -r <row_rate> -c <column_rate> [s]')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('CLRS_15-8.py -i <inputfile> -o <outputfile> -r <row_rate> -c <column_rate> [s]')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
        elif opt in ("-r", "--row_rate"):
            row_rate = int(arg)
        elif opt in ("-c", "--column_rate"):
            column_rate = int(arg)
        elif opt in ("-s", "--s"):
            if_show_one_seam = True

    im = Image.open(inputfile)
    m, n = im.size
    if if_show_one_seam:
        temp = show_one_seam(im)
        temp.show()
    for _ in range(int(m - (m * (column_rate / 100)))):
        im = for_one_carving(im, axis=0)
    for _ in range(int(n - (n * (row_rate / 100)))):
        im = for_one_carving(im, axis=1)
    im.save(outputfile)
