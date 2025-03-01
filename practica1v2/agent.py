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
    
    def run(self):
        """Función principal del hilo que mueve el agente por la cuadrícula."""
        dir_row = 1
        dir_col = 1
        
        while True:
            self.previous_cell = self.grid_labels[self.i][self.j]
            
            # Cambia la direccion si se acerca a los bordes
            if self.i > len(self.matrix) - 2 and dir_row == 1:
                dir_row = -1
            if self.i < 1 and dir_row == -1:
                dir_row = 1
                
            if self.j > len(self.matrix) - 2 and dir_col == 1:
                dir_col = -1
            if self.j < 1 and dir_col == -1:
                dir_col = 1
            
            # Actualizar posicion
            self.i = self.i + dir_row
            self.j = self.j + dir_col
            
            # Actualizar posicion en la cuadrícula
            self.update_position()
            
            #Logica del tiempo
            try:
                time.sleep((100 + random.randint(0, 100)) / 1000)  # Convertir a segundos
            except InterruptedError as ex:
                print(ex)
    
    def update_position(self):
        with threading.Lock():
            self.previous_cell.config(image="")
            self.grid_labels[self.i][self.j].config(image=self.icon)
            self.grid_labels[self.i][self.j].image = self.icon  
            print(f"{self.name} en -> Fila: {self.i}, Columna: {self.j}")
