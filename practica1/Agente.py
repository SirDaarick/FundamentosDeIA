import random
import pygame

class Agente:
    def __init__(self, nombre, icon, matrix, tablero):
        self.nombre = nombre
        self.icon = icon
        self.matrix = matrix
        self.tablero = tablero
        self.i = random.randint(0, len(matrix) - 1)
        self.j = random.randint(0, len(matrix) - 1)
        self.tablero[self.i][self.j] = self.icon
        self.dirRow = 1
        self.dirCol = 1

    def update(self):
        self.casillaAnterior = self.tablero[self.i][self.j]
        if self.i > len(self.matrix) - 2 and self.dirRow == 1:
            self.dirRow = -1
        if self.i < 1 and self.dirRow == -1:
            self.dirRow = 1
        if self.j > len(self.matrix) - 2 and self.dirCol == 1:
            self.dirCol = -1
        if self.j < 1 and self.dirCol == -1:
            self.dirCol = 1
        self.i += self.dirRow
        self.j += self.dirCol
        self.actualizarPosicion()

    def actualizarPosicion(self):
        self.casillaAnterior = None
        self.tablero[self.i][self.j] = self.icon
        print(f"{self.nombre} in -> Row: {self.i} Col: {self.j}")