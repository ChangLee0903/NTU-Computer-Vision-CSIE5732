import numpy as np
from PIL import Image
import numpy as np

# read lena.bmp
sample_img = Image.open('lena.bmp')
sample_arr = np.array(sample_img)

kernel = np.array([[-2, -1], [-2, 0], [-2, 1],
                   [-1, -2], [-1, -1], [-1, 0], [-1, 1], [-1, 2],
                   [0, -2], [0, -1], [0, 0], [0, 1], [0, 2],
                   [1, -2], [1, -1], [1, 0], [1, 1], [1, 2],
                   [2, -1], [2, 0], [2, 1]])
# (a) Dilation
def dilation(sample_arr, kernel):
    img_dil = np.zeros(sample_arr.shape).astype(int)
    for i in range(sample_arr.shape[0]):
        for j in range(sample_arr.shape[1]):
            if sample_arr[i, j] > 0:
                max_val = 0
                for (p, q) in kernel:
                    i_dil, j_dil = i + p, j + q
                    if i_dil >= 0 and j_dil >= 0 and \
                            i_dil <= (sample_arr.shape[0] - 1) and j_dil <= (sample_arr.shape[1] - 1):
                        max_val = max(max_val, sample_arr[i_dil, j_dil])
                        
                for (p, q) in kernel:
                    i_dil, j_dil = i + p, j + q
                    if i_dil >= 0 and j_dil >= 0 and \
                            i_dil <= (sample_arr.shape[0] - 1) and j_dil <= (sample_arr.shape[1] - 1):
                        img_dil[i_dil, j_dil] = max_val
    return img_dil
img_dil = dilation(sample_arr, kernel)
PIL_image = Image.fromarray(img_dil.astype('uint8'))
PIL_image.save('results/Dilation.bmp')


# (b) Erosion
def erosion(sample_arr, kernel):
    img_ero = np.zeros(sample_arr.shape).astype(int)
    for i in range(sample_arr.shape[0]):
        for j in range(sample_arr.shape[1]):
            Isdraw = True
            min_val = 255
            for (p, q) in kernel:
                i_dil, j_dil = i + p, j + q
                if not(i_dil >= 0 and j_dil >= 0 and
                       i_dil <= (
                           sample_arr.shape[0] - 1) and j_dil <= (sample_arr.shape[1] - 1)
                       and sample_arr[i_dil, j_dil] > 0):
                    Isdraw = False
                    break
                min_val = min(min_val, sample_arr[i_dil, j_dil])
            if Isdraw:
                for (p, q) in kernel:
                    i_dil, j_dil = i + p, j + q
                    if i_dil >= 0 and j_dil >= 0 and i_dil <= (
                            sample_arr.shape[0] - 1) and j_dil <= (sample_arr.shape[1] - 1) \
                            and sample_arr[i_dil, j_dil] > 0:
                        img_ero[i, j] = min_val
    return img_ero
img_ero = erosion(sample_arr, kernel)
PIL_image = Image.fromarray(img_ero.astype('uint8'))
PIL_image.save('results/Erosion.bmp')


# (c) Opening
img_opn = dilation(erosion(sample_arr, kernel), kernel)
PIL_image = Image.fromarray(img_opn.astype('uint8'))
PIL_image.save('results/Opening.bmp')


# (d) Closing
img_cls = erosion(dilation(sample_arr, kernel), kernel)
PIL_image = Image.fromarray(img_cls.astype('uint8'))
PIL_image.save('results/Closing.bmp')