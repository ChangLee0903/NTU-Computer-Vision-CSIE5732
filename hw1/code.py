from PIL import Image
import numpy as np

# read lena.bmp
sample_img = Image.open('lena.bmp')
sample_arr = np.array(sample_img)

# Part1. Write a program to do the following requirement.

# (a) upside-down lena.bmp
reverse_idx = np.arange(511, -1, -1)
upside_down = np.zeros(sample_arr.shape)
upside_down[reverse_idx] = sample_arr[:]
PIL_image = Image.fromarray(upside_down.astype('uint8'))
PIL_image.save('UpsideDown.bmp')

# (b) right-side-left lena.bmp
reverse_idx = np.arange(511, -1, -1)
right_side_left = np.zeros(sample_arr.shape)
right_side_left[:, reverse_idx] = sample_arr[:, :]
PIL_image = Image.fromarray(right_side_left.astype('uint8'))
PIL_image.save('RightSideLeft.bmp')

# (c) diagonally flip lena.bmp
diagonally_flip = np.zeros(sample_arr.shape)
for i in range(diagonally_flip.shape[0]):
    for j in range(diagonally_flip.shape[1]):
        diagonally_flip[i, j] = sample_arr[j, i]
PIL_image = Image.fromarray(diagonally_flip.astype('uint8'))
PIL_image.save('DiagonallyFlip.bmp')


# Part2. Write a program or use software to do the following requirement.

# (d) rotate lena.bmp 45 degrees clockwise
def get_rotate_coords(x, y, theta, ox, oy):
    s, c = np.sin(theta), np.cos(theta)
    x, y = np.asarray(x) - ox, np.asarray(y) - oy
    return x * c - y * s + ox, x * s + y * c + oy


def rotate_image(src, angle, fill=255):
    theta = angle * np.pi / 180
    ox, oy = src.shape[0]//2, src.shape[1]//2

    sh, sw = src.shape
    cx, cy = get_rotate_coords([0, sw, sw, 0], [0, 0, sh, sh], theta, ox, oy)

    dw, dh = (int(np.ceil(c.max() - c.min())) for c in (cx, cy))
    dx, dy = np.meshgrid(np.arange(dw), np.arange(dh))

    sx, sy = get_rotate_coords(dx + cx.min(), dy + cy.min(), -theta, ox, oy)
    sx, sy = sx.round().astype(int), sy.round().astype(int)

    mask = (0 <= sx) & (sx < sw) & (0 <= sy) & (sy < sh)
    dest = np.ones(shape=(dh, dw), dtype=src.dtype) * fill
    dest[dy[mask], dx[mask]] = src[sy[mask], sx[mask]]

    return dest


rotate_45 = rotate_image(sample_arr, 45)
Ch, Cw = rotate_45.shape[0]//2, rotate_45.shape[1]//2
H, W = sample_arr.shape[0]//2, sample_arr.shape[1]//2
rotate_45 = rotate_45[Ch-H:Ch+H, Cw-W:Cw+W]
PIL_image = Image.fromarray(rotate_45.astype('uint8'))
PIL_image.save('Rotate45Clockwise.bmp')

# (e) shrink lena.bmp in half
width, height = sample_arr.shape[0]//2, sample_arr.shape[1]//2
shrink_half = np.ones(sample_arr.shape) * 255

for i in range(width):
    for j in range(height):
        new_width = int(i * sample_arr.shape[0] / width)
        new_height = int(j * sample_arr.shape[1] / height)
        shrink_half[i, j] = sample_arr[new_width][new_height]

PIL_image = Image.fromarray(shrink_half.astype('uint8'))
PIL_image.save('ShrinkInHalf.bmp')

# (f) binarize lena.bmp at 128 to get a binary image
binarize = np.zeros(sample_arr.shape)
binarize[sample_arr > 128] = 255
PIL_image = Image.fromarray(binarize.astype('uint8'))
PIL_image.save('BinarizeAt128.bmp')