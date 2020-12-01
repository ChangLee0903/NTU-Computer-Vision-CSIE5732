import numpy as np


def dilation(sample_arr, kernel):
    img_dil = np.zeros(sample_arr.shape).astype(int)
    for i in range(sample_arr.shape[0]):
        for j in range(sample_arr.shape[1]):
            val = []
            for (p, q) in kernel:
                i_dil, j_dil = min(max(
                    i + p, 0), sample_arr.shape[0] - 1), min(max(j + q, 0), sample_arr.shape[1] - 1)
                val.append(min(max(0, sample_arr[i_dil, j_dil]), 255))
            img_dil[i, j] = max(val)
    return img_dil


def erosion(sample_arr, kernel):
    img_ero = np.zeros(sample_arr.shape).astype(int)
    for i in range(sample_arr.shape[0]):
        for j in range(sample_arr.shape[1]):
            val = []
            for (p, q) in kernel:
                i_dil, j_dil = min(max(
                    i + p, 0), sample_arr.shape[0] - 1), min(max(j + q, 0), sample_arr.shape[1] - 1)
                val.append(min(max(0, sample_arr[i_dil, j_dil]), 255))
            img_ero[i, j] = min(val)
    return img_ero


def opening(bin_img, kernel):
    return dilation(erosion(bin_img, kernel), kernel)


def closing(bin_img, kernel):
    return erosion(dilation(bin_img, kernel), kernel)


def opening_closing(bin_img, kernel):
    return closing(opening(bin_img, kernel), kernel)


def closing_opening(bin_img, kernel):
    return opening(closing(bin_img, kernel), kernel)
