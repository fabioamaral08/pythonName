import tkinter as tk
from Point import Point
import Text2Point
import numpy as np
from Grafo import Grafo


#setup

root = tk.Tk() #criar janela

WIDTH = 500
HEIGHT = 300

canvas = tk.Canvas(root, bg = '#383838', width = WIDTH, height = HEIGHT)

def create_circle(self, x, y, r, **kwargs):
	self.create_oval(x-r, y-r, x+r, y+r, kwargs)
	return

PONTOS = []
if __name__ == '__main__':
	setattr(type(canvas), 'create_circle', create_circle)
	pts = Text2Point.text2points("SECOMPP", pos = (100, 30), fontsize = 80, font = 'cs.ttf', width = WIDTH, height = HEIGHT)
	i = 0
	for p in pts:
		i += 1
		# if i % 2 == 0:
		# 	continue
		x = np.random.randint(0,WIDTH)
		y = np.random.randint(0,HEIGHT)

		pt = Point(x,y, p[0], p[1])
		PONTOS.append(pt)



	# PONTOS2 = []
	# for i in range(len(PONTOS)):
	# 	if PONTOS[i].removed:
	# 		continue
	# 	for j in range(i+1, len(PONTOS)):
	# 		d = np.linalg.norm(PONTOS[i].alvo - PONTOS[j].alvo)
	# 		# print(d)
	# 		if d <= 4.0:
	# 			if not PONTOS[i].removed :
	# 				x = np.random.randint(0,WIDTH)
	# 				y = np.random.randint(0,HEIGHT)
	# 				PONTOS[i].removed = True
	# 				PONTOS[j].removed = True
	# 				PONTOS2.append(Point(x,y, PONTOS[i].alvo[0], PONTOS[i].alvo[1]))
	# 			else:
	# 				PONTOS[j].removed = True
				
	# print(len(PONTOS2))
	# PONTOS = PONTOS2
	# myPt = [(10,10), (100,10), (100,100), (10,100), (50,50),( 200,300)]
	# PONTOS = []
	# for t  in myPt:
	# 	print(t)
	# 	PONTOS.append(Point(t[0], t[1], t[0], t[1]))
	g = Grafo(PONTOS)



	## Draw loop
	while True:
		canvas.delete('all')
		

		x = canvas.winfo_pointerx() - canvas.winfo_rootx()
		y = canvas.winfo_pointery() - canvas.winfo_rooty()

		canvas.create_circle(x,y,2,fill='red')
		canvas.create_text(x, y+5, text = f'({x},{y})', fill = 'white' )

		for p in PONTOS:
			p.behaviors(np.array([x,y], dtype = np.float64))
			p.update()
			p.show(canvas)
		PONTOS[0].show(canvas, True)
		g.drawAGM(canvas)
		canvas.pack()
		canvas.update_idletasks()
		root.update()