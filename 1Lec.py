import argparse
from matplotlib import pyplot as plt
from skimage.io import imshow, show
from skimage.io import imread, imsave
from skimage import data, exposure, img_as_float
from skimage.exposure import histogram

parser = argparse.ArgumentParser()
parser.add_argument('-p', '--path', type=str)
parser.add_argument('-r', '--result', type=str)
parser.add_argument('-gm', '--gamma', type=float)
parser.add_argument('-gn', '--gain', type=float)

args = parser.parse_args()
path = args.path
img = imread(path)

image = img_as_float(img)
gamma_corrected = exposure.adjust_gamma(image, args.gamma, args.gain)
imsave(args.result, gamma_corrected)

fig = plt.figure(figsize=(10, 5))
fig.add_subplot(2, 2, 1)
imshow(img)
fig.add_subplot(2, 2, 2)
imshow(gamma_corrected)

hist_red, bins_red = histogram(img[500:600, 300:400,2])
hist_green, bins_green = histogram(img[500:600,300:400,1])
hist_blue, bins_blue = histogram(img[500:600,300:400,0])

fig.add_subplot(2,2,3)
plt.plot(bins_green,hist_green, color='green', linestyle = '-', linewidth=1)
plt.plot(bins_red,hist_red, color='red', linestyle = '-', linewidth=1)
plt.plot(bins_blue,hist_blue, color='blue', linestyle = '-', linewidth=1)

hist_red, bins_red = histogram(gamma_corrected[500:600,300:400,2])
hist_green, bins_green = histogram(gamma_corrected[500:600,300:400,1])
hist_blue, bins_blue = histogram(gamma_corrected[500:600,300:400,0])

fig.add_subplot(2,2,4)
plt.plot(bins_green,hist_green, color='green', linestyle = '-', linewidth=1)
plt.plot(bins_red,hist_red, color='red', linestyle = '-', linewidth=1)
plt.plot(bins_blue,hist_blue, color='blue', linestyle = '-', linewidth=1)
show()


#C:\Users\stron\Pictures\hkD1XISx644.jpg