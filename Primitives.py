import pygame as pg

class Cube:
	def __init__(self, w, width, length, height, center, w_size, color):
		self.w = w
		self.width = width
		self.height = height
		self.center = center
		self.length = length
		self.w_size = w_size
		self.color = color
		self.vertices = [
			[[self.length/2 + self.center[0], self.center[1] + self.width/2, self.height/2 + self.center[2]],
			[self.center[0] - self.length/2, self.center[1] + self.width/2, self.height/2 + self.center[2]],
			[self.length/2 + self.center[0], self.center[1] - self.width/2, self.height/2 + self.center[2]],
			[self.center[0] - self.length/2, self.center[1] - self.width/2, self.height/2 + self.center[2]]],
			[[self.length/2 + self.center[0], self.center[1] + self.width/2, self.center[2] - self.height/2],
			[self.center[0] - self.length/2, self.center[1] + self.width/2, self.center[2] - self.height/2],
			[self.length/2 + self.center[0], self.center[1] - self.width/2, self.center[2] - self.height/2],
			[self.center[0] - self.length/2, self.center[1] - self.width/2, self.center[2] - self.height/2]]
		]
	def update(self, tr):
		self.vertices = [
			[[self.length/2 + self.center[0], self.center[1] + self.width/2, self.height/2 + self.center[2]],
			[self.center[0] - self.length/2, self.center[1] + self.width/2, self.height/2 + self.center[2]],
			[self.length/2 + self.center[0], self.center[1] - self.width/2, self.height/2 + self.center[2]],
			[self.center[0] - self.length/2, self.center[1] - self.width/2, self.height/2 + self.center[2]]],
			[[self.length/2 + self.center[0], self.center[1] + self.width/2, self.center[2] - self.height/2],
			[self.center[0] - self.length/2, self.center[1] + self.width/2, self.center[2] - self.height/2],
			[self.length/2 + self.center[0], self.center[1] - self.width/2, self.center[2] - self.height/2],
			[self.center[0] - self.length/2, self.center[1] - self.width/2, self.center[2] - self.height/2]]
		]	
		self.vertices_norm = [
			[
				tr.dot(self.vertices[0][0]),tr.dot(self.vertices[0][1]),tr.dot(self.vertices[0][2]),tr.dot(self.vertices[0][3])
			],
			[
				tr.dot(self.vertices[1][0]),tr.dot(self.vertices[1][1]),tr.dot(self.vertices[1][2]),tr.dot(self.vertices[1][3])
			]
		]
		for i in range(0, len(self.vertices_norm)):
			for k in range(0, len(self.vertices_norm[i])):
				for t in range(0, len(self.vertices_norm[i][k])):
					self.vertices_norm[i][k][t] += self.w_size[t]/2
		
		pg.draw.aaline(self.w, self.color, self.vertices_norm[0][0], self.vertices_norm[0][1], 1)
		pg.draw.aaline(self.w, self.color, self.vertices_norm[0][1], self.vertices_norm[0][3], 1)
		pg.draw.aaline(self.w, self.color, self.vertices_norm[0][2], self.vertices_norm[0][3], 1)
		pg.draw.aaline(self.w, self.color, self.vertices_norm[0][2], self.vertices_norm[0][0], 1)
		pg.draw.aaline(self.w, self.color, self.vertices_norm[1][0], self.vertices_norm[1][1], 1)
		pg.draw.aaline(self.w, self.color, self.vertices_norm[1][1], self.vertices_norm[1][3], 1)
		pg.draw.aaline(self.w, self.color, self.vertices_norm[1][2], self.vertices_norm[1][3], 1)
		pg.draw.aaline(self.w, self.color, self.vertices_norm[1][0], self.vertices_norm[1][2], 1)
		pg.draw.aaline(self.w, self.color, self.vertices_norm[0][0], self.vertices_norm[1][0], 1)
		pg.draw.aaline(self.w, self.color, self.vertices_norm[0][1], self.vertices_norm[1][1], 1)
		pg.draw.aaline(self.w, self.color, self.vertices_norm[0][2], self.vertices_norm[1][2], 1)
		pg.draw.aaline(self.w, self.color, self.vertices_norm[0][3], self.vertices_norm[1][3], 1)