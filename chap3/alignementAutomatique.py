import cv2 as cv
import numpy as np
from sklearn.decomposition import PCA


originalImage = cv.imread('images/imageINF1423.png', flags=cv.IMREAD_GRAYSCALE)

(h, w) = originalImage.shape
oriImageCenter = (w / 2, h / 2)

angle35 = 35
angle90 = 90
angle180 = 180
angle270 = 270

scale = 1
#on simule une image avec une rotation
rotationMatrix = cv.getRotationMatrix2D(oriImageCenter, angle35, scale)
abs_cos = abs(rotationMatrix[0,0])
abs_sin = abs(rotationMatrix[0,1])
bound_w = int(h * abs_sin + w * abs_cos)
bound_h = int(h * abs_cos + w * abs_sin)

rotationMatrix[0, 2] += bound_w/2 - oriImageCenter[0]
rotationMatrix[1, 2] += bound_h/2 - oriImageCenter[1]

rotatedImage = cv.warpAffine(originalImage, rotationMatrix, (bound_w, bound_h), flags=cv.INTER_LINEAR)


indices = np.argwhere(rotatedImage >= 1)
y = indices[:, 0]
x = indices[:, 1]

xBar = np.mean(x)
yBar = np.mean(y)

D = [x-xBar, y-yBar]

pca = PCA()
principalComponents = pca.fit_transform(D)
premierAxe = principalComponents[:, 0]
deuxiemeAxe = principalComponents[:, 1]
breakpoint()
print(principalComponents)
angleRad = np.arctan2(premierAxe[1], premierAxe[0])
angleDeg = np.rad2deg(angleRad)
print(angleDeg)

cv.line(rotatedImage, (int(xBar), int(yBar)), (int(premierAxe[0]), int(premierAxe[1])), 125, 3)
cv.line(rotatedImage, (int(xBar), int(yBar)), (int(deuxiemeAxe[0]), int(deuxiemeAxe[1])), 225, 3)
cv.imshow('Rotate', rotatedImage)

rotationMatrix = cv.getRotationMatrix2D(oriImageCenter, angleDeg, scale)
replacedImage = cv.warpAffine(rotatedImage, rotationMatrix, (bound_w, bound_h))

cv.imshow('Replaced', replacedImage)
cv.waitKey()

# I = imread('imageINF1423.png');
# I = imrotate(I,35,'bilinear','crop');

# % calculer les axes principaux
# [y x] = find(I);
# xbar = mean(x);
# ybar = mean(y);
# D = [x - xbar, y - ybar];
# axesPrincipaux = princomp(D);
# premierAxe = axesPrincipaux(:, 1);
# deuxiemeAxe = axesPrincipaux(:, 2);

# % estimer l'angle de rotation
# angleEstime = atan2(premierAxe(2), premierAxe(1));
# % convertir l'angle en degré
# angleEstime = rad2deg(angleEstime);

# imshow(I);
# hold on

# % afficher le premier axe
# quiver(xbar, ybar, premierAxe(1), premierAxe(2), 'LineWidth', 3, 'Color', 'g', 'MaxHeadSize', 2, 'AutoScaleFactor', 100);
# % afficher le deuxième axe
# quiver(xbar, ybar, deuxiemeAxe(1), deuxiemeAxe(2), 'LineWidth', 3, 'Color', 'b', 'MaxHeadSize', 2, 'AutoScaleFactor', 100);
# % afficher le barycentre
# plot(xbar, ybar, 'Marker', '.','MarkerSize', 25, 'Color', 'r');

# % aligner I avec l'angle estimé
# J =imrotate(I, angleEstime, 'bilinear', 'crop');
# figure
# imshow(J)