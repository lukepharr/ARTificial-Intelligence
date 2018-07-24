"""Collects the necessary image metrics for the model.

Metrics used in model:
  shannon_entropy
  mean_colors
  luminance
  contrast
  contour

1. open_and_get_metrics() - Essentially the main. Opens the image and calls all the metrics 
retrieval functions.
2. flatten() - Converts the the image to a 1-dimensional array
3. get_contour() - Gets the contours of the image (pixel count of all borders in the image).
4. get_mean_colors() - Gets the mean color value for red, green, and blue.
5. get_contrast() - Gets the contrast value for the image
"""

import numpy as np

import skimage
from skimage import io
from skimage.util import invert
from skimage.measure import perimeter, find_contours, shannon_entropy
from skimage.measure._regionprops import perimeter
from skimage.color import rgb2gray

import functools

# Open the image and start the metrics chain
def open_and_get_metrics(img_path):
    """Open the image from the static folder and retrieve its metrics for classification

    Args:
        img_path: The path of the image within the static folder, or uploads folder.

    Returns:
        image_data: A dictionary of all the collected image metrics
    """
    img = io.imread(img_path)
    flat_image = flatten(img)

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
    """Converts the image to a 1-dimensional array for get_mean_colors().

    Args:
        img: image file opened by open_and_get_metrics().
    
    Returns:
        flat_img: 1-dimensional array of the image data.
    """
    flat_img = []

    for row in img:
        for pixel in row:
            flat_img.append(pixel)
    
    return flat_img


########################################
# Metrics getter functions
########################################

# Extract image contours from the inverted grayscale image
def get_contour(img):
    """Returns the total pixel count of all the borders in the image. It first converts the
    image to grayscale, and then inverts it, making the borders more pronounced.

    Args:
        img: Image file opened by open_and_get_metrics().
    
    Returns:
        len_contours: Length of pixel array returned by find_contours(). (The number of 
    border pixels.)
    """
    img = invert(rgb2gray(img))
    contours = skimage.measure.find_contours(img, 0.8)
    len_contours = len(contours) / img.size

    return len_contours

# Get mean rgb values for the image and return as a list
def get_mean_colors(flat_img):  
    """Gets the mean color values for red, blue, and green.

    Args:
        flat_img: 1-dimensional array from flatten()
    
    Returns:
        mean_colors: List of red, green, and blue values. One value for each.
    """  
    mean_red = np.array([row[0] for row in flat_img]).mean()
    mean_green = np.array([row[1] for row in flat_img]).mean()
    mean_blue = np.array([row[2] for row in flat_img]).mean()
    
    mean_colors = [mean_red, mean_green, mean_blue]

    return mean_colors

# Extract contrast from luminance
def get_contrast(luminance):
    """Gets the contrast value from the min and max luminance values.

    Args:
        luminance: Calculated using the standard luminance formula in open_and_get_metrics().
    
    Returns:
        contrast: Contrast value from the formula for finding contrast from luminance.
    """
    lmin = np.min(luminance)
    lmax = np.max(luminance)
    contrast = (lmax - lmin) / (lmax + lmin)

    return contrast