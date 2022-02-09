from skimage.io import imread, imsave
path = input('Введите путь:\n')
img = imread(path)
print('Image shape: ', img.shape)

