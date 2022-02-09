import argparse
from skimage.io import imread, imsave
parser = argparse.ArgumentParser()
parser.add_argument('-p', '--path', type=str)
parser.add_argument('-r', '--result', type=str)
parser.add_argument('-gm', '--gamma', type=float)
parser.add_argument('-gn', '--gain', type=float)
args = parser.parse_args()
path = args.path
img = imread(path)
print('Image shape: ', img.shape)

