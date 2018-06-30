import skimage
from skimage import data
from skimage import io
import numpy as np

def mode_color(img):
	#read in image
	img=io.imread('Rothko_AI/'+img)
	#flatten image
	flat_img=[]
	for x in img:
	    for y in x:
	        flat_img.append(y)
	#convert pixels to strings
	flat_img=[str(x) for x in flat_img]
	#create dictionary with pixel color counts
	counts = {}
	for i in flat_img:
	    if i in counts:
	        counts[i] += 1
	    else:
	        counts[i] = 1
	#find maximum value and convert to numpy array
	key_max = max(counts.keys(), key=(lambda k: counts[k]))
	key_max=key_max.split('[')[1].split(']')[0]
	rgb=np.fromstring(key_max, dtype=int, sep=' ')
	return rgb

def mean_color(img):
	#read in image
	img=io.imread('Rothko_AI/'+img)
	#flatten image
	flat_img=[]
	for x in img:
	    for y in x:
	        flat_img.append(y)
	#calculate mean red, green and blue
	r = np.array([x[0] for x in flat_img]).mean()
	g = np.array([x[1] for x in flat_img]).mean()
	b = np.array([x[2] for x in flat_img]).mean()
	#combine into one array
	rgb=[r,g,b]
	return rgb

def shannon_entropy(img):
	#ready-made method
	entropy = skimage.measure.shannon_entropy(io.imread('Rothko_AI/'+img), base=2)
	return entropy