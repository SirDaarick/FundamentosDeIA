import tkinter as tk
from PIL import Image, ImageTk

class BackgroundPanel(tk.Frame):
    
    def __init__(self, parent, background_image_path):
        super().__init__(parent)
        
        # Cargar la imagen de fondo
        self.original_image = Image.open(background_image_path)
        self.background_image = ImageTk.PhotoImage(self.original_image)
        
        # Crear un lienzo (canvas) para dibujar el fondo
        self.canvas = tk.Canvas(self)
        self.canvas.pack(fill="both", expand=True)
        
        # Dibujar la imagen en el lienzo
        self.image_id = self.canvas.create_image(0, 0, image=self.background_image, anchor="nw")
        
        #Redimensionar
        self.bind("<Configure>", self.resize_background)
    
    def resize_background(self, event):
        """Redimensiona la imagen de fondo cuando se cambia el tamaño del marco."""
        
        # Obtener las nuevas dimensiones
        width = event.width
        height = event.height
        
        # Redimensionar la imagen
        resized_image = self.original_image.resize((width, height), Image.LANCZOS)
        self.background_image = ImageTk.PhotoImage(resized_image)
        
        # Actualizar la imagen en el lienzo
        self.canvas.itemconfig(self.image_id, image=self.background_image)
