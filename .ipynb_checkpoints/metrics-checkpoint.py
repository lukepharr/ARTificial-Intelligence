import skimage
from skimage import data
from skimage import io
from skimage.measure import perimeter
from skimage.util import invert

import numpy as np
import pandas as pd
import os

def mode_color(img):
	#read in image
	img = io.imread('Rothko_AI/'+img)

	img = io.imread('../Rothko_AI/'+img)
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
	key_max=key_max.split('[')[1].split(']')[0]
	rgb=np.fromstring(key_max, dtype=int, sep=' ')
	rgb=[rgb[0],rgb[1],rgb[2]]

	return rgb

def mean_color(img):
	#read in image
	img = io.imread('Rothko_AI/'+img)
	img=io.imread('../Rothko_AI/'+img)
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
	rgb = [r,g,b]
	return rgb

def shannon_entropy(img):
	#ready-made method

	entropy = skimage.measure.shannon_entropy(io.imread('Rothko_AI/'+img), base=2)
	return entropy

def get_perimeter(img):
    """
    1. Import the image:
        "as_gray=True" is needed to reshape the original 3D array to a 2D array.
    The perimeter function only accepts 2D arrays.
    
    2. Invert the grayscale. I did this because the standard grayscale image 
    gave me a value of 0.0
    """
    img = io.imread('Rothko_AI/'+img, as_gray=True)
    img = invert(img)
    
    return perimeter(img, neighbourhood=4)

	# entropy = skimage.measure.shannon_entropy(io.imread('../Rothko_AI/'+img), base=2)
	# return entropy

data_ = {'file_name':[], 'mode_color':[], 'mean_color':[], 'shannon_entropy':[]}
for filename in os.listdir('../Rothko_AI'):
    if '.jpg' in filename:
        data_['file_name'].append(filename)
        data_['mode_color'].append(mode_color(filename))
        data_['mean_color'].append(mean_color(filename))
        data_['shannon_entropy'].append(shannon_entropy(filename))
df=pd.DataFrame(data_)
df.to_csv('../data/data.csv')