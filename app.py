import tkinter as tk
from tkinter import *
from pynput.mouse import Button, Controller

import networkx as nx
import matplotlib.pyplot as plt

from main_menu import MainMenu
from user_input import UserInput

class Application(tk.Frame):
	def __init__(self, master=None):
		super().__init__(master)
		self.master = master
		
		menu = MainMenu.main_menu(self)
	
	def exitProgram(self):
		exit()

root = tk.Tk()
root.geometry("750x750+200+300")
root.title("Wireless Sensor Network")

app = Application(master=root)
app.mainloop()
