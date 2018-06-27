import skimage
from skimage import data
from skimage import io
import numpy as np

def mode_color(img):
	img=io.imread('Rothko_AI/'+img)
	flat_img=[]
	for x in img:
	    for y in x:
	        flat_img.append(y)
	flat_img=[str(x) for x in flat_img]
	counts = {}
	for i in flat_img:
	    if i in counts:
	        counts[i] += 1
	    else:
	        counts[i] = 1
	key_max = max(counts.keys(), key=(lambda k: counts[k]))
	key_max=key_max.split('[')[1].split(']')[0]
	rgb=np.fromstring(key_max, dtype=int, sep=' ')
	return rgb

def mean_color(img):
	img=io.imread('Rothko_AI/'+img)
	flat_img=[]
	for x in img:
	    for y in x:
	        flat_img.append(y)
	r = np.array([x[0] for x in flat_img]).mean()
	g = np.array([x[1] for x in flat_img]).mean()
	b = np.array([x[2] for x in flat_img]).mean()
	rgb=[r,g,b]
	return rgb

def shannon_entropy(img):
	entropy = skimage.measure.shannon_entropy(io.imread('Rothko_AI/'+img), base=2)
	return entropy