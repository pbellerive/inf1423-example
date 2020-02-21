import cv2 as cv
import numpy as np
from build_histogram import buildHistogrammeRGB

WHITE = 255

# lire l'image de référence
skinSourceImage = cv.imread('images/bush.jpg')

# select d'un echantillon de peau. Une fois votre rectangle fait appuyer sur ESPACE
# Ref:  https://docs.opencv.org/master/d7/dfc/group__highgui.html#ga8daf4730d3adf7035b6de9be4c469af5
roi = cv.selectROI('SELECTION DE ZONE REPRESENTANT DE LA PEAU', skinSourceImage)
skinImage = skinSourceImage[int(roi[1]):int(roi[1]+roi[3]), int(roi[0]):int(roi[0] + roi[2])]
skinHistogramProb = buildHistogrammeRGB(skinImage)

#select de ce qui n'est pas de la peau . Une fois votre rectangle fait appuyer sur ESPACE
roi = cv.selectROI('SELECTION DE ZONE QUI NEST PAS DE LA PEAU', skinSourceImage)
skinImage = skinSourceImage[int(roi[1]):int(roi[1]+roi[3]), int(roi[0]):int(roi[0] + roi[2])]
notSkinHistogramProb = buildHistogrammeRGB(skinImage)

#Détection de peau
imgToDetect = cv.imread('images/bush3.jpg')
# division par 4 pour avoir un étendu de couleur de 64 plutot que 256 .
imgToDetect = np.floor_divide(imgToDetect, 4)

cv.imshow('Image original', imgToDetect)
shape = imgToDetect.shape

for i in range(1, shape[0]):
    for j in range(1, shape[1]):
        pixel = imgToDetect[i][j]
        pR = pixel[0]
        pG = pixel[1]
        pB = pixel[2]
        # Si la probabilité dans l'histogramme peau est plus élevé que dans celui non peau
        # on considère que cest de la peau. On affiche en blanc.
        if skinHistogramProb[pR, pG, pB] > notSkinHistogramProb[pR, pG, pB]:
            imgToDetect[i, j, 0] = WHITE
            imgToDetect[i, j, 1] = WHITE
            imgToDetect[i, j, 2] = WHITE

cv.imshow('Image avec détection', imgToDetect)
cv.waitKey(0)
