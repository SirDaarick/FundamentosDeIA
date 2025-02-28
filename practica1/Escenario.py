import pygame
import sys
import random
from pygame.locals import *
from Agente import Agente  # Importar la clase Agente desde el archivo Agente.py

class Escenario:
    def __init__(self):
        pygame.init()
        self.dim = 15
        self.cell_size = 50
        self.width = self.dim * self.cell_size + 35
        self.height = self.dim * self.cell_size + 85
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Agentes")
        self.clock = pygame.time.Clock()
        self.background = pygame.image.load("imagenes/surface.jpg")
        self.background = pygame.transform.scale(self.background, (self.width, self.height))
        self.tablero = [[None for _ in range(self.dim)] for _ in range(self.dim)]
        self.matrix = [[0 for _ in range(self.dim)] for _ in range(self.dim)]
        self.robot1 = pygame.image.load("imagenes/wall-e.png")
        self.robot1 = pygame.transform.scale(self.robot1, (self.cell_size, self.cell_size))
        self.robot2 = pygame.image.load("imagenes/eva.png")
        self.robot2 = pygame.transform.scale(self.robot2, (self.cell_size, self.cell_size))
        self.obstacleIcon = pygame.image.load("imagenes/brick.png")
        self.obstacleIcon = pygame.transform.scale(self.obstacleIcon, (self.cell_size, self.cell_size))
        self.sampleIcon = pygame.image.load("imagenes/sample.png")
        self.sampleIcon = pygame.transform.scale(self.sampleIcon, (self.cell_size, self.cell_size))
        self.motherIcon = pygame.image.load("imagenes/mothership.png")
        self.motherIcon = pygame.transform.scale(self.motherIcon, (self.cell_size, self.cell_size))
        self.actualIcon = None
        self.wallE = Agente("Wall-E", self.robot1, self.matrix, self.tablero)
        self.eva = Agente("Eva", self.robot2, self.matrix, self.tablero)
        self.run()

    def run(self):
        while True:
            self.screen.blit(self.background, (0, 0))
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.goodBye()
                elif event.type == MOUSEBUTTONDOWN:
                    self.insertaObjeto(event.pos)
            self.draw_grid()
            self.wallE.update()
            self.eva.update()
            pygame.display.flip()
            self.clock.tick(30)

    def draw_grid(self):
        for i in range(self.dim):
            for j in range(self.dim):
                rect = pygame.Rect(j * self.cell_size + 10, i * self.cell_size + 10, self.cell_size, self.cell_size)
                pygame.draw.rect(self.screen, (255, 255, 255), rect, 1)
                if self.tablero[i][j]:
                    self.screen.blit(self.tablero[i][j], rect.topleft)

    def insertaObjeto(self, pos):
        x, y = pos
        i = (y - 10) // self.cell_size
        j = (x - 10) // self.cell_size
        if 0 <= i < self.dim and 0 <= j < self.dim and self.actualIcon:
            self.tablero[i][j] = self.actualIcon

    def goodBye(self):
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    escenario = Escenario()