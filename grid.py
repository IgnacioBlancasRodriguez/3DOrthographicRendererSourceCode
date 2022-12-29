import pygame as pg

class Grid():
	def __init__ (self, w, w_size, dist, tr):
		self.w = w
		self.w_size = w_size
		self.tr = tr
		self.dist = dist
	def update(self, tr):
		tr
		for i in range(0, int(self.w_size[0]/self.dist)):
			pg.draw.aaline(self.w, pg.Color(0,100,150), (tr.dot([i*self.dist-self.w_size[0]/2,-self.w_size[1]/2,0])[0] + self.w_size[0]/2,
			tr.dot([i*self.dist-self.w_size[0]/2,-self.w_size[1]/2,0])[1] + self.w_size[1]/2),
			 (tr.dot([i*self.dist-self.w_size[0]/2, self.w_size[1]/2,0])[0] + self.w_size[0]/2,
			 tr.dot([i*self.dist-self.w_size[0]/2, self.w_size[1]/2,0])[1] + self.w_size[1]/2),1)
			pg.draw.aaline(self.w, pg.Color(0,100,150), (tr.dot([-self.w_size[0]/2, i*self.dist-self.w_size[1]/2,0])[0] + self.w_size[0]/2,
			tr.dot([-self.w_size[0]/2, i*self.dist-self.w_size[1]/2,0])[1] + self.w_size[1]/2),
			(tr.dot([self.w_size[0]/2, i*self.dist-self.w_size[1]/2,0])[0] + self.w_size[0]/2,
			tr.dot([self.w_size[0]/2, i*self.dist-self.w_size[1]/2,0])[1] + self.w_size[1]/2),1)
		pg.draw.aaline(self.w, pg.Color(0,0,200), (tr.dot([-self.w_size[0]/2, 0,0])[0] + self.w_size[0]/2,
		tr.dot([-self.w_size[0]/2, 0,0])[1] + self.w_size[1]/2),
		(tr.dot([self.w_size[0]/2, 0,0])[0] + self.w_size[0]/2,
		tr.dot([self.w_size[0]/2, 0,0])[1] + self.w_size[1]/2),1)		#Abscissa
		pg.draw.aaline(self.w, pg.Color(200,0,0), (tr.dot([0, -self.w_size[1]/2,0])[0] + self.w_size[0]/2,
		tr.dot([0, -self.w_size[1]/2,0])[1] + self.w_size[1]/2),
		(tr.dot([0, self.w_size[1]/2,0])[0] + self.w_size[0]/2,
		tr.dot([0, self.w_size[1]/2,0])[1] + self.w_size[1]/2),1)		#Ordinates