import numpy as np

def buildHistogrammeRGB(img):
    size = img.shape
    img = np.floor_divide(img, 4)
    histogram = np.zeros((64, 64, 64))

    for i in range(0, size[0]):
        for j in range(0, size[1]):
            r = img[i][j][0]
            g = img[i][j][1]
            b = img[i][j][2]
            histogram[r][g][b] = histogram[r][g][b] + 1
    histogram = histogram / (size[0]*size[1])
    return histogram