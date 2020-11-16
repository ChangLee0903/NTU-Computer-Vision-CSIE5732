import numpy as np
from PIL import Image
import numpy as np

# read lena.bmp
sample_img = Image.open('lena.bmp')
sample_arr = np.array(sample_img)

# downsampling
down_img = np.zeros((64, 64)).astype(int)
for i in range(down_img.shape[0]):
    for j in range(down_img.shape[1]):
        down_img[i, j] = sample_arr[8 * i, 8 * j]

# binarization
bin_img = np.zeros(down_img.shape).astype(int)
bin_img[down_img > 127] = 255

# define function
def h(b, c, d, e):
    if b == c and (d != b or e != b):
        return 'q'
    if b == c and (d == b and e == b):
        return 'r'
    return 's'


def YokoiConnectivityNumber(bin_img, i, j):
    if i == 0:
        if j == 0:
            # top-left
            x7, x2, x6 = 0, 0, 0
            x3, x0, x1 = 0, bin_img[i][j], bin_img[i][j + 1]
            x8, x4, x5 = 0, bin_img[i + 1][j], bin_img[i + 1][j + 1]
        elif j == bin_img.shape[1] - 1:
            # top-right
            x7, x2, x6 = 0, 0, 0
            x3, x0, x1 = bin_img[i][j - 1], bin_img[i][j], 0
            x8, x4, x5 = bin_img[i + 1][j - 1], bin_img[i + 1][j], 0
        else:
            # top-row
            x7, x2, x6 = 0, 0, 0
            x3, x0, x1 = bin_img[i][j - 1], bin_img[i][j], bin_img[i][j + 1]
            x8, x4, x5 = bin_img[i + 1][j -
                                        1], bin_img[i + 1][j], bin_img[i + 1][j + 1]
    elif i == bin_img.shape[0] - 1:
        if j == 0:
            # bottom-left
            x7, x2, x6 = 0, bin_img[i - 1][j], bin_img[i - 1][j + 1]
            x3, x0, x1 = 0, bin_img[i][j], bin_img[i][j + 1]
            x8, x4, x5 = 0, 0, 0
        elif j == bin_img.shape[1] - 1:
            # bottom-right
            x7, x2, x6 = bin_img[i - 1][j - 1], bin_img[i - 1][j], 0
            x3, x0, x1 = bin_img[i][j - 1], bin_img[i][j], 0
            x8, x4, x5 = 0, 0, 0
        else:
            # bottom-row
            x7, x2, x6 = bin_img[i - 1][j -
                                        1], bin_img[i - 1][j], bin_img[i - 1][j + 1]
            x3, x0, x1 = bin_img[i][j - 1], bin_img[i][j], bin_img[i][j + 1]
            x8, x4, x5 = 0, 0, 0
    else:
        if j == 0:
            x7, x2, x6 = 0, bin_img[i - 1][j], bin_img[i - 1][j + 1]
            x3, x0, x1 = 0, bin_img[i][j], bin_img[i][j + 1]
            x8, x4, x5 = 0, bin_img[i + 1][j], bin_img[i + 1][j + 1]
        elif j == bin_img.shape[1] - 1:
            x7, x2, x6 = bin_img[i - 1][j - 1], bin_img[i - 1][j], 0
            x3, x0, x1 = bin_img[i][j - 1], bin_img[i][j], 0
            x8, x4, x5 = bin_img[i + 1][j - 1], bin_img[i + 1][j], 0
        else:
            x7, x2, x6 = bin_img[i - 1][j -
                                        1], bin_img[i - 1][j], bin_img[i - 1][j + 1]
            x3, x0, x1 = bin_img[i][j - 1], bin_img[i][j], bin_img[i][j + 1]
            x8, x4, x5 = bin_img[i + 1][j -
                                        1], bin_img[i + 1][j], bin_img[i + 1][j + 1]

    a1 = h(x0, x1, x6, x2)
    a2 = h(x0, x2, x7, x3)
    a3 = h(x0, x3, x8, x4)
    a4 = h(x0, x4, x5, x1)

    if a1 == 'r' and a2 == 'r' and a3 == 'r' and a4 == 'r':
        return 5
    else:
        return sum(np.array([a1, a2, a3, a4]) == 'q')


output = np.zeros(bin_img.shape).astype(str)

# compute and output Yokoi Connectivity Number ...
for i in range(bin_img.shape[0]):
    for j in range(bin_img.shape[1]):
        if bin_img[i][j] > 127:
            output[i, j] = '%d ' % YokoiConnectivityNumber(bin_img, i, j)
        else:
            output[i, j] = '  '

fp = open("results/YokoiConnectivity.txt", "a")
for line in output:
    fp.writelines(list(line)+['\n'])
fp.close()
