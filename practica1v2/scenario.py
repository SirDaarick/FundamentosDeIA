# scenario.py
import tkinter as tk
from tkinter import messagebox
import threading
from PIL import Image, ImageTk
import pygame  
import os
import sys
from background_panel import BackgroundPanel 
from agent import Agent

class Scenario(tk.Tk):

    
    def __init__(self):
        super().__init__()
        
        self.dim = 15  # dimensiones de la cuadricula
        
        # iniciar matriz para la logica y la cuadricula
        self.grid_labels = [[None for _ in range(self.dim)] for _ in range(self.dim)]
        self.matrix = [[0 for _ in range(self.dim)] for _ in range(self.dim)]
        
        #declarar las imagenes
        self.robot1 = None
        self.robot2 = None
        self.obstacle_icon = None
        self.sample_icon = None
        self.mother_icon = None
        self.actual_icon = None
        
        #declarar los agentes
        self.wall_e = None
        self.eva = None
        
        # Configuracion de la ventana
        self.title("Agents")
        self.geometry(f"{self.dim*50+35}x{self.dim*50+85}+50+50")
        self.protocol("WM_DELETE_WINDOW", self.good_bye)
        
        # Panel de fondo
        try:
            self.background_panel = BackgroundPanel(self, "imagenes/surface.jpg")
            self.background_panel.pack(fill="both", expand=True)
        except Exception as e:
            print(f"Error creating background panel: {e}")
            self.background_panel = tk.Frame(self, bg="gray")
            self.background_panel.pack(fill="both", expand=True)
        
        self.init_components()
        
        self.play_audio()
    
    def init_components(self):
        # Barra de menu superior
        self.menu_bar = tk.Menu(self)
        self.config(menu=self.menu_bar)
        
        #menu file
        file_menu = tk.Menu(self.menu_bar, tearoff=0)
        file_menu.add_command(label="Run", command=self.handle_run)
        file_menu.add_command(label="Exit", command=self.good_bye)
        self.menu_bar.add_cascade(label="File", menu=file_menu)
        
        # menu settings
        self.settings_menu = tk.Menu(self.menu_bar, tearoff=0)
        
        # opciones del menu settings
        self.selected_option = tk.StringVar()
        self.settings_menu.add_radiobutton(label="Obstacle", variable=self.selected_option, 
                                           value="obstacle", command=self.handle_obstacle)
        self.settings_menu.add_radiobutton(label="Sample", variable=self.selected_option, 
                                           value="sample", command=self.handle_sample)
        self.settings_menu.add_radiobutton(label="MotherShip", variable=self.selected_option, 
                                           value="mothership", command=self.handle_mothership)
        self.menu_bar.add_cascade(label="Settings", menu=self.settings_menu)
        
        # cargar las imagenes
        self.load_images()
        
        # crear la cuadricula
        self.create_grid()
        
        # crear agentes
        self.wall_e = Agent("Wall-E", self.robot1, self.matrix, self.grid_labels)
        self.eva = Agent("Eva", self.robot2, self.matrix, self.grid_labels)
    
    def load_images(self):
        try:
            #carga robot1 
            image = Image.open("imagenes/wall-e.png")
            image = image.resize((50, 50), Image.LANCZOS)
            self.robot1 = ImageTk.PhotoImage(image)
            
            #carga robot2
            image = Image.open("imagenes/eva.png")
            image = image.resize((50, 50), Image.LANCZOS)
            self.robot2 = ImageTk.PhotoImage(image)
            
            #carga los obstaculos
            image = Image.open("imagenes/brick.png")
            image = image.resize((50, 50), Image.LANCZOS)
            self.obstacle_icon = ImageTk.PhotoImage(image)
            
            #carga las muestras (los objetivos que recoge el agente)
            image = Image.open("imagenes/sample.png")
            image = image.resize((50, 50), Image.LANCZOS)
            self.sample_icon = ImageTk.PhotoImage(image)
            
            # carga la nave nodriza
            image = Image.open("imagenes/mothership.png")
            image = image.resize((50, 50), Image.LANCZOS)
            self.mother_icon = ImageTk.PhotoImage(image)
        except Exception as e:
            print(f"Error loading images: {e}")
            self.robot1 = tk.PhotoImage(width=50, height=50)
            self.robot2 = tk.PhotoImage(width=50, height=50)
            self.obstacle_icon = tk.PhotoImage(width=50, height=50)
            self.sample_icon = tk.PhotoImage(width=50, height=50)
            self.mother_icon = tk.PhotoImage(width=50, height=50)
    
    def create_grid(self):
        frame = tk.Frame(self.background_panel)
        frame.place(x=10, y=10, width=self.dim*50, height=self.dim*50)
        
        for i in range(self.dim):
            for j in range(self.dim):
                self.matrix[i][j] = 0
                
                label = tk.Label(frame, borderwidth=1, relief="solid")
                label.place(x=j*50, y=i*50, width=50, height=50)
                
                self.grid_labels[i][j] = label
                #Configura el click para seleccionar una cuadricula
                label.bind("<Button-1>", self.insert_object)
                label.bind("<B1-Motion>", self.insert_object)
    
    def insert_object(self, event):
        if self.actual_icon is not None:
            #Encuentra la cuadricula que fue clickeada
            widget = event.widget
            widget.config(image=self.actual_icon)
            widget.image = self.actual_icon
    
    def handle_obstacle(self):
 
        if self.selected_option.get() == "obstacle":
            self.actual_icon = self.obstacle_icon
        else:
            self.actual_icon = None
    
    def handle_sample(self):
        if self.selected_option.get() == "sample":
            self.actual_icon = self.sample_icon
        else:
            self.actual_icon = None
    
    def handle_mothership(self):

        if self.selected_option.get() == "mothership":
            self.actual_icon = self.mother_icon
        else:
            self.actual_icon = None
    
    def handle_run(self):
        if not self.wall_e.is_alive():
            self.wall_e.start()
        if not self.eva.is_alive():
            self.eva.start()
        
        self.menu_bar.entryconfig("Settings", state="disabled")
    
    def play_audio(self):
        try:
            pygame.mixer.init()
            pygame.mixer.music.load("audio/audio.aiff")
            pygame.mixer.music.play(-1) 
        except Exception as ex:
            print(f"Error playing audio: {ex}")
    
    def good_bye(self):
        response = messagebox.askquestion("Exit", "Do you want to exit?", icon='warning')
        if response == 'yes':
            try:
                pygame.mixer.music.stop()  
            except:
                pass
            self.destroy()  