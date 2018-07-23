import skimage
from skimage import data
from skimage import io
import numpy as np
import os

from skimage.util import invert
from skimage.measure import perimeter
from skimage.measure import find_contours

from skimage.measure._regionprops import (regionprops as regionprops_default,
                                          PROPS, perimeter, _parse_docs)
import functools
regionprops = functools.partial(regionprops_default, coordinates='rc')

from skimage import feature

from skimage.exposure import is_low_contrast


def mode_color(img):
    #read in image
    img = io.imread(img)
    #flatten image
    flat_img = []
    for x in img:
        for y in x:
            flat_img.append(y)
    #convert pixels to strings
    flat_img = [str(x) for x in flat_img]
    #create dictionary with pixel color counts
    counts = {}
    for i in flat_img:
        if i in counts:
            counts[i] += 1
        else:
            counts[i] = 1
    #find maximum value and convert to numpy array
    key_max = max(counts.keys(), key=(lambda k: counts[k]))
    key_max = key_max.split('[')[1].split(']')[0]
    rgb = np.fromstring(key_max, dtype=int, sep=' ')
    rgb = [rgb[0],rgb[1],rgb[2]]
    return rgb

def mean_color(img):
    #read in image
    img = io.imread(img)
    #flatten image
    flat_img = []
    for x in img:
        for y in x:
            flat_img.append(y)
    #calculate mean red, green and blue
    r = np.array([x[0] for x in flat_img]).mean()
    g = np.array([x[1] for x in flat_img]).mean()
    b = np.array([x[2] for x in flat_img]).mean()
    #combine into one array
    rgb = [r, g, b]
    return rgb

def shannon_entropy(img):
    #ready-made method
    entropy = skimage.measure.shannon_entropy(io.imread(img), base=2)
    return entropy

def perimeter_(img):
    return perimeter(invert(io.imread(img, as_gray=True)), neighbourhood=8)
    
def find_contours(img):
    img = io.imread(img, as_gray=True)
    img = invert(img)
    contours = skimage.measure.find_contours(img, 0.8)
    return len(contours) / img.size

def solidity(img):
    return regionprops(io.imread(img).astype(int))[0].solidity

# This function takes an image and calculates the shape_index of the image which is an array
# It then returns the average of squares of the shape_index array
# from skimage import feature will be needed
def get_shape_index(img):
    img = io.imread(img, as_gray=True)
    shape_index = feature.shape_index(img)
    shape_index_1D = np.ravel(shape_index)
    avg_squares_shape_index = np.average(np.square(shape_index_1D))
    return avg_squares_shape_index

def low_contrast(img):
    img = io.imread(img)
    lowcontrast = is_low_contrast(img)
    return lowcontrast

def getImageContrast(img_file_path):
    img = io.imread(img_file_path)
    flat_img = []

    for x in img:
        for y in x:
            flat_img.append(y)

    lum = []
    for rgb in flat_img:
        luminance = (0.2126*rgb[0] + 0.7152*rgb[1] + 0.0722*rgb[2])
        lum.append(luminance)
    lmin = np.min(lum)
    lmax = np.max(lum)
    return (lmax-lmin)/(lmax + lmin)

def get_image_data(filename):
    data_ = {'file_name':[], 'year':[], 'mean_color':[], 'mean_color_r':[], 'mean_color_g':[], 'mean_color_b':[],\
         'shannon_entropy':[], 'luminance':[],\
         'contour':[], 'solidity':[],\
         'shape_index':[], 'contrast':[]}

    data_['file_name'].append(filename)
    data_['year'].append(filename.split('/')[-1].split('.')[0])
    rgb = mean_color(filename)    
    luminance = (0.2126*rgb[0] + 0.7152*rgb[1] + 0.0722*rgb[2])
    data_['mean_color'].append(rgb)
    data_['mean_color_r'].append(rgb[0])
    data_['mean_color_g'].append(rgb[1])
    data_['mean_color_b'].append(rgb[2])
    data_['luminance'].append(luminance)            
    data_['shannon_entropy'].append(shannon_entropy(filename))
    data_['contour'].append(find_contours(filename))
    data_['shape_index'].append(get_shape_index(filename))
    try:
        data_['solidity'].append(solidity(filename))
    except: 
        data_['solidity'].append('Null')
    data_['contrast'].append(getImageContrast(filename))

    return data_