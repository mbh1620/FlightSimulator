from wireframe import *
import pygame
import numpy as np
import math
from camera import *
import time
from HUD import HeadsUpDisplay

class ProjectionViewer:

	''' Displays 3D Objects on a Pygame Screen '''

	def __init__(self, width, height, center_point):
		self.width = width
		self.height = height
		self.screen = pygame.display.set_mode((width, height))
		pygame.display.set_caption('Wireframe Display')
		self.background = (10,10,50)
		self.throttle = 0

	

		#Setup camera
		self.camera = Camera([-1200,-1000,0],0,0)
		self.center_point = center_point


		self.wireframes = {}
		self.displayNodes = False
		self.displayEdges = True
		self.nodeColour = (255,255,255)
		self.edgeColour = (200,200,200)
		self.nodeRadius = 4

		self.hud = HeadsUpDisplay(self.screen)

		pygame.init()

	def run(self):

		key_to_function = {
	
 		pygame.K_w: (lambda x: x.rotateAll('X', 0.01*self.throttle/10)),
 		pygame.K_s: (lambda x: x.rotateAll('X', -0.01*self.throttle/10)),
 		pygame.K_a: (lambda x: x.rotate_about_camera('Z', -0.01*self.throttle/10)),
 		pygame.K_d: (lambda x: x.rotate_about_camera('Z', 0.01*self.throttle/10)),
 		pygame.K_UP: (lambda x: x.increaseThrottle(1)),
 		pygame.K_DOWN: (lambda x: x.decreaseThrottle(1)),

		}


		running = True
		flag = False

		while running:

			keys = pygame.key.get_pressed()

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					running = False

				
				
			if keys[pygame.K_LEFT]:
				key_to_function[pygame.K_LEFT](self)
			if keys[pygame.K_RIGHT]:
				key_to_function[pygame.K_RIGHT](self)
			if keys[pygame.K_DOWN]:
				key_to_function[pygame.K_DOWN](self)
			if keys[pygame.K_UP]:
				key_to_function[pygame.K_UP](self)
			if keys[pygame.K_EQUALS]:
				key_to_function[pygame.K_EQUALS](self)
			if keys[pygame.K_MINUS]:
				key_to_function[pygame.K_MINUS](self)
			if keys[pygame.K_LEFT]:
				key_to_function[pygame.K_LEFT](self)
			if keys[pygame.K_q]:
				key_to_function[pygame.K_q](self)
			if keys[pygame.K_w]:
				key_to_function[pygame.K_w](self)
			if keys[pygame.K_a]:
				key_to_function[pygame.K_a](self)
			if keys[pygame.K_s]:
				key_to_function[pygame.K_s](self)
			if keys[pygame.K_z]:
				key_to_function[pygame.K_z](self)
			if keys[pygame.K_x]:
				key_to_function[pygame.K_x](self)
			if keys[pygame.K_t]:
				key_to_function[pygame.K_t](self)
			if keys[pygame.K_d]:
				key_to_function[pygame.K_d](self)

			if keys[pygame.K_u]:
				key_to_function[pygame.K_u](self)
			if keys[pygame.K_h]:
				key_to_function[pygame.K_h](self)
			if keys[pygame.K_j]:
				key_to_function[pygame.K_j](self)
			if keys[pygame.K_k]:
				key_to_function[pygame.K_k](self)
			if keys[pygame.K_y]:
				key_to_function[pygame.K_y](self)
			if keys[pygame.K_i]:
				key_to_function[pygame.K_i](self)

			if keys[pygame.K_o]:
				key_to_function[pygame.K_o](self)
			if keys[pygame.K_p]:
				key_to_function[pygame.K_p](self)
			if keys[pygame.K_m]:
				key_to_function[pygame.K_m](self)


			self.display()
			self.hud.draw(self.throttle)
			self.move_cam_forward(self.throttle)
			pygame.display.flip()
			

	def addWireframe(self, name, wireframe):
		self.wireframes[name] = wireframe
		#translate to center
		wf = Wireframe()
		matrix = wf.translationMatrix(-self.width/2,-self.height/2,0)

		for wireframe in self.wireframes.values():
			wireframe.transform(matrix)

		

		wf = Wireframe()
		matrix = wf.translationMatrix(self.width,self.height,0)

		for wireframe in self.wireframes.values():
			wireframe.transform(matrix)


		

	def display(self):

		self.screen.fill(self.background)

		for wireframe in self.wireframes.values():
			wireframe.transform_for_perspective((self.width/2, self.height/2), self.camera.fov, self.camera.zoom)	

			if self.displayNodes == True:
				for node in wireframe.perspective_nodes:
					if node[2] > 0 and node[2] < 10000 and node[0] > 0 and node[0] < 1199:
						pygame.draw.circle(self.screen, self.nodeColour, (int(node[0]), int(node[1])), self.nodeRadius, 0)
			else:
				pass
			if self.displayEdges:
				for n1, n2 in wireframe.edges:
					if wireframe.perspective_nodes[n1][2] > 0 and wireframe.perspective_nodes[n2][2] > 0 and wireframe.perspective_nodes[n1][2] < 10000 and wireframe.perspective_nodes[n1][0] > 0 and wireframe.perspective_nodes[n1][0] < 1199 :
						pygame.draw.aaline(self.screen, self.edgeColour, wireframe.perspective_nodes[n1][:2], wireframe.perspective_nodes[n2][:2], 1)



	def translateAll(self, vector):
		''' Translate all wireframes along a given axis by d units '''
		wf = Wireframe()
		matrix = wf.translationMatrix(*vector)
		for wireframe in self.wireframes.values():
			wireframe.transform(matrix)

	def scaleAll(self, vector):
		wf = Wireframe()
		matrix = wf.scaleMatrix(*vector)

		for wireframe in self.wireframes.values():
			wireframe.transform(matrix)

	def rotateAll(self, axis, theta):

		wf = Wireframe()
		if axis == 'X':
			matrix = wf.rotateXMatrix(theta)
		elif axis == 'Y':
			matrix = wf.rotateYMatrix(theta)
		elif axis == 'Z':
			matrix = wf.rotateZMatrix(theta)

		for wireframe in self.wireframes.values():
			wireframe.transform(matrix)
			#wireframe.transform_for_perspective()


	def rotate_about_Center(self, Axis, theta):

		#First translate Centre of screen to 0,0

		wf = Wireframe()
		matrix = wf.translationMatrix(-self.width/2,-self.height/2,0)

		for wireframe in self.wireframes.values():
			wireframe.transform(matrix)

		#Do Rotation
		wf = Wireframe()
		if Axis == 'X':
			matrix = wf.rotateXMatrix(theta)
		elif Axis == 'Y':
			matrix = wf.rotateYMatrix(theta)
		elif Axis == 'Z':
			matrix = wf.rotateZMatrix(theta)

		for wireframe in self.wireframes.values():
			wireframe.transform(matrix)
		

		#Translate back to centre of screen

		wf = Wireframe()
		matrix = wf.translationMatrix(self.width/2,self.height/2,0)

		for wireframe in self.wireframes.values():
			wireframe.transform(matrix)

	def rotate_about_camera(self, Axis, theta):

		wf = Wireframe()

		matrix = wf.translationMatrix(-self.width/2, -self.height/2,0)

		for wireframe in self.wireframes.values():
			wireframe.transform(matrix)

		#Do Rotation
		wf = Wireframe()
		if Axis == 'X':
			matrix = wf.rotateXMatrix(theta)
		elif Axis == 'Y':
			matrix = wf.rotateYMatrix(theta)
		elif Axis == 'Z':
			matrix = wf.rotateZMatrix(theta)

		for wireframe in self.wireframes.values():
			wireframe.transform(matrix)
		

		#Translate back to original position

		wf = Wireframe()
		matrix = wf.translationMatrix(self.width/2,self.height/2,0)

		for wireframe in self.wireframes.values():
			wireframe.transform(matrix)


		

		if self.camera.hor_angle >= 2*math.pi:
			self.camera.hor_angle -= 2*math.pi
		elif self.camera.hor_angle < -2*math.pi:
			self.camera.hor_angle += 2*math.pi

		self.camera.define_render_space()
		self.camera.hor_angle += theta
		self.camera.set_position(self.center_point)
		print(self.camera.pos)

		#Update the position of the drone here!

		# a = (self.camera.pos[0] - self.drone.pos[0])**2
		# b = (self.camera.pos[2] - self.drone.pos[2])**2
		# r = math.sqrt(a+b)

		# self.drone.pos[0] = r*math.cos(self.camera.hor_angle)
		# self.drone.pos[2] = r*math.sin(self.camera.hor_angle)
		
		


	def scale_centre(self, vector):

		#Transform center of screen to origin

		wf = Wireframe()
		matrix = wf.translationMatrix(-self.width/2,-self.height/2,0)

		for wireframe in self.wireframes.values():
			wireframe.transform(matrix)

		#Scale the origin by vector

		wf = Wireframe()
		matrix = wf.scaleMatrix(*vector)

		for wireframe in self.wireframes.values():
			wireframe.transform(matrix)

		wf = Wireframe()
		matrix = wf.translationMatrix(self.width/2,self.height/2,0)

		for wireframe in self.wireframes.values():
			wireframe.transform(matrix)

	def move_cam_forward(self, amount):
		#Moving the camera forward will be a positive translation in the z axis for every other object.
		
		self.camera.define_render_space()
		self.translateAll([0,0,-amount])
		self.camera.set_position(self.center_point)
		print("Camera position: ")
		print(self.camera.pos)

	def move_cam_backward(self, amount):
		
		self.camera.define_render_space()
		self.translateAll([0,0,amount])
		self.camera.set_position(self.center_point)
		print("Camera position: ")
		print(self.camera.pos)

	def move_cam_left(self, amount):
		
		self.camera.define_render_space()
		self.translateAll([-amount,0,0])
		self.camera.set_position(self.center_point)
		print("Camera position: ")
		print(self.camera.pos)

	def move_cam_right(self, amount):
		
		self.camera.define_render_space()
		self.translateAll([amount,0,0])
		self.camera.set_position(self.center_point)
		print("Camera position: ")
		print(self.camera.pos)

	def move_cam_up(self, amount):
		
		self.camera.define_render_space()
		self.translateAll([0,-amount,0])
		self.camera.set_position(self.center_point)

	def move_cam_down(self, amount):
		
		self.camera.define_render_space()
		self.translateAll([0,amount,0])
		self.camera.set_position(self.center_point)

	def increaseThrottle(self, amount):
		self.throttle += amount

	def decreaseThrottle(self, amount):
		if(self.throttle > 0):
			self.throttle -= amount

	def Toggle_Nodes(self):
		if self.displayNodes == True:
			self.displayNodes = False
		else:
			self.displayNodes = True

	








