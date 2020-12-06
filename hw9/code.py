import numpy as np
from PIL import Image
import os
from scipy import signal

# read lena.bmp
sample_img = Image.open('lena.bmp')
sample_arr = np.array(sample_img).astype(int)

# build output directory
if not os.path.exists('results'):
    os.mkdir('results')

# define function


def binarize(img, thr):
    img_bin = np.zeros(img.shape)
    img_bin[img <= thr] = 255
    return img_bin


def magnitude(Gx, Gy):
    return np.sqrt(Gx ** 2 + Gy ** 2)


def roberts_operator(img):
    k1 = np.array([
        [1, 0],
        [0, -1]
    ])
    k2 = np.array([
        [0, 1],
        [-1, 0]
    ])
    return magnitude(signal.convolve2d(img, k1), signal.convolve2d(img, k2))


def prewitts_edge_detector(img):
    k1 = np.array([
        [-1, 0, 1],
        [-1, 0, 1],
        [-1, 0, 1]
    ])
    k2 = np.array([
        [-1, -1, -1],
        [0, 0, 0],
        [1, 1, 1]
    ])
    return magnitude(signal.convolve2d(img, k1), signal.convolve2d(img, k2))


def sobels_edge_detector(img):
    k1 = np.array([
        [-1, 0, 1],
        [-2, 0, 2],
        [-1, 0, 1]
    ])
    k2 = np.array([
        [-1, -2, -1],
        [0, 0, 0],
        [1, 2, 1]
    ])
    return magnitude(signal.convolve2d(img, k1), signal.convolve2d(img, k2))


def frei_and_chens_gradient_operator(img):
    k1 = np.array([
        [-1, -np.sqrt(2), -1],
        [0, 0, 0],
        [1, np.sqrt(2), 1]
    ])
    k2 = np.array([
        [-1, 0, 1],
        [-np.sqrt(2), 0, np.sqrt(2)],
        [-1, 0, 1]
    ])
    return magnitude(signal.convolve2d(img, k1), signal.convolve2d(img, k2))


def kirschs_compass_operator(img):
    k0 = np.array([
        [-3, -3, 5],
        [-3, 0, 5],
        [-3, -3, 5]
    ])
    k1 = np.array([
        [-3, 5, 5],
        [-3, 0, 5],
        [-3, -3, -3]
    ])
    k2 = np.array([
        [5, 5, 5],
        [-3, 0, -3],
        [-3, -3, -3]
    ])
    k3 = np.array([
        [5, 5, -3],
        [5, 0, -3],
        [-3, -3, -3]
    ])
    k4 = np.array([
        [5, -3, -3],
        [5, 0, -3],
        [5, -3, -3]
    ])
    k5 = np.array([
        [-3, -3, -3],
        [5, 0, -3],
        [5, 5, -3]
    ])
    k6 = np.array([
        [-3, -3, -3],
        [-3, 0, -3],
        [5, 5, 5]
    ])
    k7 = np.array([
        [-3, -3, -3],
        [-3, 0, 5],
        [-3, 5, 5]
    ])
    return np.max(np.array(
        [signal.convolve2d(img, k0),
         signal.convolve2d(img, k1),
         signal.convolve2d(img, k2),
         signal.convolve2d(img, k3),
         signal.convolve2d(img, k4),
         signal.convolve2d(img, k5),
         signal.convolve2d(img, k6),
         signal.convolve2d(img, k7)]), axis=0)


def robinsons_compass_operator(img):
    k0 = np.array([
        [-1, 0, 1],
        [-2, 0, 2],
        [-1, 0, 1]
    ])
    k1 = np.array([
        [0, 1, 2],
        [-1, 0, 1],
        [-2, -1, 0]
    ])
    k2 = np.array([
        [1, 2, 1],
        [0, 0, 0],
        [-1, -2, -1]
    ])
    k3 = np.array([
        [2, 1, 0],
        [1, 0, -1],
        [0, -1, -2]
    ])
    k4 = np.array([
        [1, 0, -1],
        [2, 0, -2],
        [1, 0, -1]
    ])
    k5 = np.array([
        [0, -1, -2],
        [1, 0, -1],
        [2, 1, 0]
    ])
    k6 = np.array([
        [-1, -2, -1],
        [0, 0, 0],
        [1, 2, 1]
    ])
    k7 = np.array([
        [-2, -1, 0],
        [-1, 0, 1],
        [0, 1, 2]
    ])
    return np.max(np.array(
        [signal.convolve2d(img, k0),
         signal.convolve2d(img, k1),
         signal.convolve2d(img, k2),
         signal.convolve2d(img, k3),
         signal.convolve2d(img, k4),
         signal.convolve2d(img, k5),
         signal.convolve2d(img, k6),
         signal.convolve2d(img, k7)]), axis=0)


def nevatia_babu_5x5_operator(img):
    k0 = -np.array([
        [100, 100, 100, 100, 100],
        [100, 100, 100, 100, 100],
        [0, 0, 0, 0, 0],
        [-100, -100, -100, -100, -100],
        [-100, -100, -100, -100, -100],
    ])
    k1 = -np.array([
        [100, 100, 100, 100, 100],
        [100, 100, 100, 78, -32],
        [100, 92, 0, -92, -100],
        [32, -78, -100, -100, -100],
        [-100, -100, -100, -100, -100]
    ])
    k2 = -np.array([
        [100, 100, 100, 32, -100],
        [100, 100, 92, -78, -100],
        [100, 100, 0, -100, -100],
        [100, 78, -92, -100, -100],
        [100, -32, -100, -100, -100]
    ])
    k3 = np.array([
        [-100, -100, 0, 100, 100],
        [-100, -100, 0, 100, 100],
        [-100, -100, 0, 100, 100],
        [-100, -100, 0, 100, 100],
        [-100, -100, 0, 100, 100]
    ])
    k4 = -np.array([
        [-100, 32, 100, 100, 100],
        [-100, -78, 92, 100, 100],
        [-100, -100, 0, 100, 100],
        [-100, -100, -92, 78, 100],
        [-100, -100, -100, -32, 100]
    ])
    k5 = -np.array([
        [100, 100, 100, 100, 100],
        [-32, 78, 100, 100, 100],
        [-100, -92, 0, 92, 100],
        [-100, -100, -100, -78, 32],
        [-100, -100, -100, -100, -100]
    ])
    return np.max(np.array(
        [signal.convolve2d(img, k0),
         signal.convolve2d(img, k1),
         signal.convolve2d(img, k2),
         signal.convolve2d(img, k3),
         signal.convolve2d(img, k4),
         signal.convolve2d(img, k5)]), axis=0)


# (a) Robert's Operator: 12
PIL_image = Image.fromarray(
    binarize(roberts_operator(sample_arr), 12).astype('uint8'))
PIL_image.save('results/RobertsOperator.bmp')

# (b) Prewitt's Edge Detector: 24
PIL_image = Image.fromarray(
    binarize(prewitts_edge_detector(sample_arr), 24).astype('uint8'))
PIL_image.save('results/PrewittsEdgeDetector.bmp')

# (c) Sobel's Edge Detector: 38
PIL_image = Image.fromarray(
    binarize(sobels_edge_detector(sample_arr), 38).astype('uint8'))
PIL_image.save('results/SobelsEdgeDetector.bmp')

# (d) Frei and Chen's Gradient Operator: 30
PIL_image = Image.fromarray(
    binarize(frei_and_chens_gradient_operator(sample_arr), 30).astype('uint8'))
PIL_image.save('results/FreiAndChensGradientOperator.bmp')

# (e) Kirsch's Compass Operator: 135
PIL_image = Image.fromarray(
    binarize(kirschs_compass_operator(sample_arr), 135).astype('uint8'))
PIL_image.save('results/KirschsCompassOperator.bmp')

# (f) Robinson's Compass Operator: 43
PIL_image = Image.fromarray(
    binarize(robinsons_compass_operator(sample_arr), 43).astype('uint8'))
PIL_image.save('results/RobinsonsCompassOperator.bmp')

# (g) Nevatia-Babu 5x5 Operator: 12500
PIL_image = Image.fromarray(
    binarize(nevatia_babu_5x5_operator(sample_arr), 12500).astype('uint8'))
PIL_image.save('results/NevatiaBabuOperator.bmp')
