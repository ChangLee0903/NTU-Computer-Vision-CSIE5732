import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

# read lena.bmp
sample_img = Image.open('lena.bmp')
sample_arr = np.array(sample_img)

# define function
def get_hist(img):
    counter = np.zeros(256).astype(int)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            counter[int(img[i, j])] += 1
    return counter


def write_hist(hist, name=None):
    fig = plt.figure()
    plt.bar(np.arange(256), hist, color=(0.4, 0.6, 1))
    if name is not None:
        plt.title(name)
        plt.savefig(f'results/{name}.png')


# (a) original image and its histogram
org_hist = get_hist(sample_arr)
np.savetxt('results/OriginalHist.csv', org_hist, fmt='%d', delimiter=",")
write_hist(org_hist, 'OriginalHist')
PIL_image = Image.fromarray(sample_arr.astype('uint8'))
PIL_image.save('results/Original.bmp')

# (b) image with intensity divided by 3 and its histogram
div_by_3 = sample_arr / 3
div_by_3_hist = get_hist(div_by_3)
np.savetxt('results/DividedBy3Hist.csv',
           div_by_3_hist, fmt='%d', delimiter=",")
write_hist(div_by_3_hist, 'DividedBy3Hist')
PIL_image = Image.fromarray(div_by_3.astype('uint8'))
PIL_image.save('results/DividedBy3.bmp')

# (c) image after applying histogram equalization to (b) and its histogram
CMF = np.zeros(256).astype(int)
CMF[0] = div_by_3_hist[0]
for i in range(1, 256):
    CMF[i] = CMF[i - 1] + div_by_3_hist[i]

CMF = CMF * 255 / div_by_3_hist.sum()
hist_equal = np.zeros(div_by_3.shape).astype(int)
for i in range(div_by_3.shape[0]):
    for j in range(div_by_3.shape[1]):
        hist_equal[i, j] = CMF[int(div_by_3[i, j])]

hist_equal_hist = get_hist(hist_equal)
np.savetxt('results/HistogramEqualizationHist.csv', hist_equal_hist, fmt='%d', delimiter=",")
write_hist(hist_equal_hist, 'HistogramEqualizationHist')
PIL_image = Image.fromarray(hist_equal.astype('uint8'))
PIL_image.save('results/HistogramEqualization.bmp')
