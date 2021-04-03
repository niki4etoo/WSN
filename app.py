import tkinter as tk
from tkinter import *
from main_menu import MainMenu

class Application(tk.Frame):
	def __init__(self, master=None):
		super().__init__(master)
		self.master = master
		
		menu = MainMenu.main_menu(self)
	
	def exitProgram(self):
		exit()

root = tk.Tk()
root.geometry("500x500+100+100")
root.title("Wireless Sensor Network")

frame = tk.Frame(root, width=500, height=500, background="white")
frame.pack()
	
app = Application(master=root)
app.mainloop()
