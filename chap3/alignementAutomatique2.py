import cv2 as cv
import numpy as np
from sklearn.decomposition import PCA
from PIL import Image

originalImage = Image.open('images/imageINF1423.png')
# (h, w) = originalImage.shape[:2]

# oriImageCenter = (w / 2, h / 2)

angle35 = 35
angle90 = 90
angle180 = 180
angle270 = 270

scale = 1.0
#on simule une image avec une rotation
rotatedImage = originalImage.rotate(angle35)
data = np.array(list(rotatedImage.getdata()))
indices = np.argwhere(data >= 1)

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

fixedImage = rotatedImage.rotate(angleDeg)

# cv.line(rotatedImage, (int(xBar), int(yBar)), (int(premierAxe[0]), int(premierAxe[1])), 175, 3)
# cv.line(rotatedImage, (int(xBar), int(yBar)), (int(deuxiemeAxe[0]), int(deuxiemeAxe[1])), 125, 3)
# cv.imshow('Rotate', rotatedImage)

rotatedImage.show()
fixedImage.show()
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