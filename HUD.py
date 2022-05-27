import pygame


class HeadsUpDisplay:

	def __init__(self, screen):

		self.screen = screen
		self.draw(0)

	def draw(self, throttle):
		pygame.draw.aaline(self.screen, (255,255,255), (600, 500), (610, 510), 1)
		pygame.draw.aaline(self.screen, (255,255,255), (600, 500), (590, 510), 1)
		pygame.draw.aaline(self.screen, (255,255,255), (580, 510), (590, 510), 1)
		pygame.draw.aaline(self.screen, (255,255,255), (620, 510), (610, 510), 1)
		
		pygame.draw.aaline(self.screen, (0,255,0), (800, 510), (610, 510), 1)
		pygame.draw.aaline(self.screen, (0,255,0), (400, 510), (590, 510), 1)
		pygame.draw.aaline(self.screen, (0,255,0), (380, 400), (380, 610), 1)
		pygame.draw.aaline(self.screen, (0,255,0), (820, 400), (820, 610), 1)

		pygame.draw.aaline(self.screen, (255,0,0), (850, 610-(throttle*5)), (820, 610-(throttle*5)), 1)


		

		pygame.draw.aaline(self.screen, (0,255,0), (820, 400), (860, 400), 1)
		pygame.draw.aaline(self.screen, (0,255,0), (380, 400), (340, 400), 1)
		pygame.draw.aaline(self.screen, (0,255,0), (380, 420), (370, 420), 1)
		pygame.draw.aaline(self.screen, (0,255,0), (380, 440), (370, 440), 1)
		pygame.draw.aaline(self.screen, (0,255,0), (380, 460), (370, 460), 1)
		pygame.draw.aaline(self.screen, (0,255,0), (380, 480), (370, 480), 1)
		pygame.draw.aaline(self.screen, (0,255,0), (380, 500), (370, 500), 1)
		pygame.draw.aaline(self.screen, (0,255,0), (380, 520), (370, 520), 1)
		pygame.draw.aaline(self.screen, (0,255,0), (380, 540), (370, 540), 1)
		pygame.draw.aaline(self.screen, (0,255,0), (380, 560), (370, 560), 1)
		pygame.draw.aaline(self.screen, (0,255,0), (380, 580), (370, 580), 1)
		pygame.draw.aaline(self.screen, (0,255,0), (380, 610), (360, 610), 1)









		pygame.draw.circle(self.screen, (0, 255, 180), (1000, 800), 100, 1)
		pygame.draw.circle(self.screen, (0, 255, 180), (200, 800), 100, 1)
		# pygame.draw.circle(self.screen, (0, 0, 180), (200, 800), 80,)
		# pygame.draw.circle(self.screen, (0, 0, 180), (1000, 800), 80,)

		pygame.draw.line(self.screen, (255, 255, 255), (1100, 800), (900, 800), 1)

	
