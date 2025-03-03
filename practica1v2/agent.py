import threading
import random
import time
import tkinter as tk

class Agent(threading.Thread):
    
    def __init__(self, name, icon, matrix, grid_labels):
        super().__init__()
        self.name = name
        self.icon = icon
        self.matrix = matrix
        self.grid_labels = grid_labels
        
        # Inicializar posicion aleatoria
        self.i = random.randint(0, len(matrix) - 1)
        self.j = random.randint(0, len(matrix) - 1)
        
        # Colocar el icono en la posición inicial
        self.grid_labels[self.i][self.j].config(image=self.icon)
        self.grid_labels[self.i][self.j].image = self.icon  # Mantener referencia para evitar recolección de basura
        
        self.previous_cell = self.grid_labels[self.i][self.j]
        self.daemon = True  # El hilo terminará cuando el programa principal finalice
    
    def is_valid_cell(self, i, j):
        """Verifica si la celda (i, j) es válida (está dentro de los límites y no tiene un obstáculo)."""
        return (0 <= i < len(self.matrix)) and (0 <= j < len(self.matrix)) and (self.matrix[i][j] != 1)
    
    def get_valid_directions(self):
        """Obtiene todas las direcciones válidas."""
        directions = [
            (1, 0),   # Abajo
            (-1, 0),  # Arriba
            (0, 1),   # Derecha
            (0, -1),  # Izquierda
        ]
        
        valid_directions = []
        for dir_row, dir_col in directions:
            next_i = self.i + dir_row
            next_j = self.j + dir_col
            if self.is_valid_cell(next_i, next_j):
                valid_directions.append((dir_row, dir_col))
        
        return valid_directions

    def choose_valid_direction(self):
        """Elige una dirección válida aleatoriamente."""
        valid_directions = self.get_valid_directions()
        if valid_directions:
            return random.choice(valid_directions)
        else:
            return None  # No hay direcciones válidas

    def run(self):
        """Función principal del hilo que mueve el agente por la cuadrícula."""
        dir_row = 1
        dir_col = 1

        while True:
            self.previous_cell = self.grid_labels[self.i][self.j]

            next_move = random.random()

            if 0.25 > next_move >= 0:
                dir_row = 1
                if not self.is_valid_cell(self.i + dir_row, self.j):
                    dir_row = -1
                self.i = self.i + dir_row

            elif 0.5 > next_move >= 0.25:
                dir_row = -1
                if not self.is_valid_cell(self.i + dir_row, self.j):
                    dir_row = 1
                self.i = self.i + dir_row

            elif 0.75 > next_move >= 0.5:
                dir_col = 1
                if not self.is_valid_cell(self.i, self.j + dir_col):
                    dir_col = -1
                self.j = self.j + dir_col

            elif 1 > next_move >= 0.75:
                dir_col = -1
                if not self.is_valid_cell(self.i, self.j + dir_col):
                    dir_col = 1
                self.j = self.j + dir_col

            self.update_position()
            time.sleep((100 + random.randint(0, 100)) / 1000)
    
    def update_position(self):
        with threading.Lock():
            self.previous_cell.config(image="")
            self.grid_labels[self.i][self.j].config(image=self.icon)
            self.grid_labels[self.i][self.j].image = self.icon  
            print(f"{self.name} en -> Fila: {self.i}, Columna: {self.j}")
