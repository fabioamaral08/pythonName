import numpy as np

class Point(object):
	def __init__(self, x,y,xt, yt):
		self.r = 1
		self.pos  = np.array([x,y], dtype = np.float64)
		self.alvo = np.array([xt,yt], dtype = np.float64	)
		self.vel  = (np.random.rand(2) -.5) * 2
		self.acel = np.array([0,0], np.float64)
		self.removed = False
		self.maxspeed = 10

	def update(self):
		self.pos += self.vel
		self.vel += self.acel
		self.acel *= 0

	def show(self, C):
		C.create_circle(self.pos[0], self.pos[1], self.r, fill = 'white', outline = '')

	def behaviors(self, target):
		seek = self.seek()
		self.aply_force(seek)
		flee = self.flee(target)
		self.aply_force(flee)

	def aply_force(self, force):
		self.acel += force

	def seek(self):
		vet = self.alvo - self.pos
		
		d = max(np.abs(vet)) #distancia
		if d > 0:
			vet = vet/d
		else:
			return self.vel

		if d > 100:
			 vet = vet * self.maxspeed
		else:
			vet *= d * self.maxspeed/100

		return vet - self.vel

	def flee(self, target):
		vet = target - self.pos

		d = max(np.abs(vet)) #distancia
		if d > 0.0:
			vet = vet/d
		if d < 50:
			vet *= d * self.maxspeed/50
		else:
			vet *= 0

		return (-vet - self.vel)