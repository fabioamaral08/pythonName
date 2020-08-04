import numpy as np
import tkinter as tk

class Node():
	def __init__(self, p,c1,c2, c1_ind, c2_ind):
		self.point = p
		self.closest1 = c1
		self.closest2 = c2

		self.c1_ind = c1_ind
		self.c2_ind = c2_ind


class Grafo():
	def __init__(self, points):
		self.num_vert = len(points)
		self.mat = np.zeros((self.num_vert * self.num_vert,))
		self.nodes = np.array(points).flatten()
		self.prox = []
		self.agm = []
		self.topoogic = []

		self.pai = -np.ones(self.nodes.shape)
		for i in range(self.num_vert):
			min0 = np.inf
			min1 = np.inf
			c1= -1
			c2 = -1
			for j in range(self.num_vert):
				if i == j:
					continue
				index_ij = self.calc_index(i,j)
				index_ji = self.calc_index(j,i)
				d =  self.dist(self.nodes[i], self.nodes[j])
				if d < min0:
					min1 = min0
					c2 = c1
					min0 = d
					c1 = j
				elif d < min1:
					min1 = d
					c2 = j

				self.mat[index_ji] = d
				self.mat[index_ij] = d
			self.prox.append(Node(self.nodes[i], self.nodes[c1], self.nodes[c2], c1,c2))
		


	def calc_index(self, i, j):
		return j + i * self.num_vert

	def dist(self, p1, p2):
		x1 = float( p1.alvo[0])
		y1 = float( p1.alvo[1])
		x2 = float( p2.alvo[0])
		y2 = float( p2.alvo[1])
		return np.sqrt((x1 -x2)**2 + (y1 - y2)**2) 


	def prim(self):
		vis = np.zeros(self.nodes.shape, dtype= np.int)
		
		v = 0
		self.pai = -np.ones((self.nodes.shape[0],2), dtype=np.int32)
		Q = np.array((0,v)).reshape((-1,2))

		S = []
		# cont = 0
		while len(Q) > 0:
			# cont +=1
			# if cont == 2: 
			# 	print(Q)
			v, Q = self.remove_min(Q)
			S.append(v)
			vis[v] += 1

			for i in range(self.num_vert):
				if v == i or vis[i] > 1:
					continue
				if vis[i] == 1 and self.pai[i,0] == v:
					continue
				w = self.mat[self.calc_index(v, i)]
				c = self.get_elem(Q,i)
				if c is None or c[0] > w:

					self.pai[i,vis[i]] = v
					Q = self.atualiza(Q,w,i)
					# print(f'-{i}->',Q)
		self.agm = S
		return


	def remove_min(self, Q):
		minv = np.argmin(Q,axis=0)[0]
		# print(">>>>",Q[minv,:])
		v = int(Q[minv,1])
		return v, np.delete(Q,minv,0)

	def atualiza(self, Q, w, i):
		for c in Q:
			if c[1] == i:
				if c[0] > w:
					c[0] = w
					return Q
		return np.append(Q,[[w,i]], axis=0)
	def get_elem(self, Q, i):
		for c in Q:
			if c[1] == i:
				return c
		return None

	def drawAGM(self, C):
		i = 1
		n_ant = self.prox[0]
		n = self.prox[n_ant.c1_ind]
		vis = np.zeros(self.nodes.shape, dtype= np.bool)
		vis[0] = True
		vis[n_ant.c1_ind] = True
		while not vis.all():
			o = n_ant.point
			d0 = n.point
			C.create_line(o.pos[0], o.pos[1], d0.pos[0], d0.pos[1], fill='grey')
			n_ant = n
			if not vis[n.c1_ind]:
				vis[n.c1_ind] = True
				n = self.prox[n.c1_ind]
			elif not vis[n.c2_ind] :
				vis[n.c2_ind] = True
				n = self.prox[n.c2_ind]
			else:
				j = 0
				while vis[j]:
					j +=1
				n = self.prox[j]
				vis[j] = True

			i +=1

		
