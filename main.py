import math
import pygame as pg
from grid import Grid
import Primitives as pr
import numpy as np

pg.init()

w_size = [1000, 1000]

w = pg.display.set_mode(w_size)
pg.display.set_caption("3D Orthographic Renderer")

tr = np.array([[1,0,0],
	[0,1,0]])											#Initialize the projection Matrix

grid = Grid(w, w_size, 20, tr)							#Initialize the grid
cube = pr.Cube(w, 40, 40, 40, [0,0,0], w_size, pg.Color(255, 255, 255))		#Initialize the cube

def main():
	alpha = beta = 0
	
	m_pos = m_pos_back = m_pos_new = (0,0)				#Initialize the mouse position buffers
	clock = pg.time.Clock()								
	clock.tick(144)										#Adujust the frame rate

	z = 1												#Level of zoom
	t = 0												#Initialize time counter

	while True:
		for event in pg.event.get():					#Handel user events
			if event.type == pg.QUIT:
				quit()
			if event.type == pg.KEYDOWN:
				if event.key == pg.K_LEFT:
					beta -= math.pi/100
				if event.key == pg.K_RIGHT:
					beta += math.pi/100
				if event.key == pg.K_UP:
					alpha -= math.pi/100
				if event.key == pg.K_DOWN:
					alpha += math.pi/100
				if event.key == pg.K_KP_PLUS and pg.key.get_mods() & pg.KMOD_CTRL:
					z += 0.1
				if event.key == pg.K_KP_MINUS and pg.key.get_mods() & pg.KMOD_CTRL:
					z -= 0.1	
		if pg.mouse.get_pressed()[0]:
			if m_pos_new[0] != -1:
				m_pos_back = m_pos_new
				m_pos_new = pg.mouse.get_pos()
				m_pos = (m_pos_back[0] - m_pos_new[0], m_pos_new[1] - m_pos_back[1])
			else:
				m_pos_new = pg.mouse.get_pos()
				m_pos = (0,0)
		else:
			m_pos_new = (-1,-1)
		m_pos = ((m_pos[1]*(math.pi/1.5))/w_size[1], (m_pos[0]*(math.pi/1.5))/w_size[0])

		alpha += m_pos[0]								#Update alpha according to the mouse movement
		beta += m_pos[1]								#Update beta according to the mouse movement

		tr = np.array([[math.cos(beta), math.cos(beta + math.pi/2)*math.cos(alpha + math.pi/2), math.cos(beta + math.pi/2)*math.cos(alpha + math.pi)],
		[0, math.sin(alpha + math.pi/2), math.sin(alpha + math.pi)]])	#Update the projection matrix
		tr = tr*z										#Zoom in or out

		w.fill(pg.Color(0,0,0))							#Make the backround with black
		
		grid.update(tr)									#Update the grid with the projection matrix
		
		cube.center = [100*math.cos(0.01*t), 0, 0]		#Moves the cube's center in harmonic movement
		cube.update(tr)									#Update the cube with the projection matrix
		pg.display.update()
		t += 1											#Update time counter with

if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		quit()