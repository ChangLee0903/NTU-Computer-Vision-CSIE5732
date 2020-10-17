import numpy as np
from PIL import Image
import numpy as np

# read lena.bmp
sample_img = Image.open('lena.bmp')
sample_arr = np.array(sample_img)

bin_img = np.zeros(sample_arr.shape).astype(int)
bin_img[sample_arr > 127] = 255

kernel = np.array([[-2, -1], [-2, 0], [-2, 1],
                   [-1, -2], [-1, -1], [-1, 0], [-1, 1], [-1, 2],
                   [0, -2], [0, -1], [0, 0], [0, 1], [0, 2],
                   [1, -2], [1, -1], [1, 0], [1, 1], [1, 2],
                   [2, -1], [2, 0], [2, 1]])
# (a) Dilation
def dilation(bin_img, kernel):
    img_dil = np.zeros(bin_img.shape).astype(int)
    for i in range(bin_img.shape[0]):
        for j in range(bin_img.shape[1]):
            if bin_img[i, j] > 0:
                for (p, q) in kernel:
                    i_dil, j_dil = i + p, j + q
                    if i_dil >= 0 and j_dil >= 0 and \
                            i_dil <= (bin_img.shape[0] - 1) and j_dil <= (bin_img.shape[1] - 1):
                        img_dil[i_dil, j_dil] = 255
    return img_dil
img_dil = dilation(bin_img, kernel)
PIL_image = Image.fromarray(img_dil.astype('uint8'))
PIL_image.save('results/Dilation.bmp')


# (b) Erosion
def erosion(bin_img, kernel):
    img_ero = np.zeros(bin_img.shape).astype(int)
    for i in range(bin_img.shape[0]):
        for j in range(bin_img.shape[1]):
            Isdraw = True
            for (p, q) in kernel:
                i_dil, j_dil = i + p, j + q
                if not(i_dil >= 0 and j_dil >= 0 and
                       i_dil <= (
                           bin_img.shape[0] - 1) and j_dil <= (bin_img.shape[1] - 1)
                       and bin_img[i_dil, j_dil] > 0):
                    Isdraw = False
                    break
            if Isdraw:
                img_ero[i, j] = 255
    return img_ero
img_ero = erosion(bin_img, kernel)
PIL_image = Image.fromarray(img_ero.astype('uint8'))
PIL_image.save('results/Erosion.bmp')


# (c) Opening
img_opn = dilation(erosion(bin_img, kernel), kernel)
PIL_image = Image.fromarray(img_opn.astype('uint8'))
PIL_image.save('results/Opening.bmp')


# (d) Closing
img_cls = erosion(dilation(bin_img, kernel), kernel)
PIL_image = Image.fromarray(img_cls.astype('uint8'))
PIL_image.save('results/Closing.bmp')


# (e) Hit-and-miss transform
J_kernel = [[0, -1], [0, 0], [1, 0]]
K_kernel = [[-1, 0], [-1, 1], [0, 1]]
def hit_and_miss(bin_img, J_kernel, K_kernel):
    img_ham = np.ones(bin_img.shape).astype(int) * 255
    img_ham[np.logical_or(erosion(bin_img, J_kernel) < 128,
                          erosion(-bin_img + 255, K_kernel) < 128)] = 0
    return img_ham
img_ham = hit_and_miss(bin_img, J_kernel, K_kernel)
PIL_image = Image.fromarray(img_ham.astype('uint8'))
PIL_image.save('results/HitAndMiss.bmp')
