import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

import matplotlib.pyplot as plt
import matplotlib.image

def text2image(text, pos = (20,20), font = "arial.ttf", fontsize = 60, width = 400, height =300):
	im = Image.new('L', (width , height ))
	d = ImageDraw.Draw(im)
	tf = ImageFont.truetype(font, fontsize)
	# d.rectangle([0,0, width-1, height-1], outline='red')
	d.text(pos, text, font = tf, fill = (255))

	# plt.imshow(im)
	# plt.show()
	return im

def get_border(im):
	return im.filter(ImageFilter.CONTOUR)

def get_points(im):
	a = np.array(im)
	# grayscale
	pts = []
	for j in range(1, a.shape[1]-1):
		for i in range(1, a.shape[0] -1):
			if a[i,j] == 0:
				add = True
				for p in pts:
					d = np.linalg.norm(np.array([p[0] - j, p[1] - i]),2)
					if d <= 4.0:
						add = False
						break
				if add:
					pts.append((j,i))
	return pts
def text2points(text, pos = (20,20), font = "arial.ttf", fontsize = 60, width = 400, height =300):
	im = text2image(text, pos, font , fontsize , width , height)
	im = get_border(im)
	return get_points(im)

