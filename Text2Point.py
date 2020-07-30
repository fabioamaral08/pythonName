import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

import matplotlib.pyplot as plt
import matplotlib.image

def text2image(text, pos = (20,20), font = "arial.ttf", fontsize = 60, width = 400, height =300):
	im = Image.new('RGB', (width, height))
	d = ImageDraw.Draw(im)
	tf = ImageFont.truetype(font, fontsize)
	d.text(pos, text, font = tf)
	return im

def get_border(im):
	return im.filter(ImageFilter.CONTOUR)

def get_points(im):
	a = np.array(im)
	# grayscale
	a = a.mean(axis=2)
	pts = []
	for i in range(1, a.shape[0]-1):
		for j in range(1, a.shape[1] -1):
			if a[i,j] == 0:
				pts.append((i,j))
	return pts
def text2points(text, pos = (20,20), font = "arial.ttf", fontsize = 60, width = 400, height =300):
	im = text2image(text, pos, font , fontsize , width , height)
	im = get_border(im)
	return get_points(im)

def main():
	pos = (20,115)
	height = 300
	pts = text2points("Hello world", pos, fontsize = 70, height = height)

	# plt.imshow(im)
	for p in pts:
		plt.plot(p[1], height - p[0], '.k')
	print("fim")
	plt.show()

if __name__ == "__main__":
    main()

