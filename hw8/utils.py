import numpy as np


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


def opening(bin_img, kernel):
    return dilation(erosion(bin_img, kernel), kernel)


def closing(bin_img, kernel):
    return erosion(dilation(bin_img, kernel), kernel)
