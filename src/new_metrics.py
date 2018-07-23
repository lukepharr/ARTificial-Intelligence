import numpy as np

import skimage

from skimage import io
from skimage import feature
from skimage.util import invert
from skimage.measure import perimeter, find_contours, shannon_entropy
from skimage.measure._regionprops import (regionprops as regionprops_default, perimeter)
from skimage.exposure import is_low_contrast
from skimage.color import rgb2gray

import functools

"""
Metrics used in model:
  shannon_entropy
  mean_colors
  luminance
  contrast
  contour
"""

# Open the image and start the metrics chain
def open_and_get_metrics(img_path):
    img = io.imread(img_path)
    flat_image = flatten(img)

    # Treats the image as a matrix - replace with dot product
    for col in img:
        for row in col:
            flat_image.append(row)

    entropy = shannon_entropy(img, base=2)
    mean_colors = get_mean_colors(flat_image)
    luminance = (0.2126 * mean_colors[0] + 0.7152 * mean_colors[1] + 0.0722 * mean_colors[2])
    contrast = get_contrast(luminance)
    contour = get_contour(img)

    image_data = {
        'file_name': img_path,
        'year': img_path.split('/')[-1].split('.')[0],
        'shannon_entropy': entropy,
        'mean_color_r': mean_colors[0],
        'luminance': luminance,
        'contrast': contrast,
        'contour': contour
    }

    return image_data


# For operations that require a flattened image
def flatten(img):
    flat_image = []

    for row in img:
        for pixel in row:
            flat_image.append(pixel)
    
    return flat_image


########################################
# Metrics getter functions
########################################

# Get mean rgb values for the image and return as a list
def get_mean_colors(flat_image):    
    mean_red = np.array([row[0] for row in flat_image]).mean()
    mean_green = np.array([row[1] for row in flat_image]).mean()
    mean_blue = np.array([row[2] for row in flat_image]).mean()
    
    mean_colors = [mean_red, mean_green, mean_blue]

    return mean_colors

# Extract contrast from luminance
def get_contrast(luminance):
    lmin = np.min(luminance)
    lmax = np.max(luminance)

    return (lmax - lmin) / (lmax + lmin)

# Extract image contours from the inverted grayscale image
def get_contour(img):
    img = invert(rgb2gray(img))
    contours = skimage.measure.find_contours(img, 0.8)

    return len(contours) / img.size