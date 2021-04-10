import tkinter as tk
from tkinter import *
from main_menu import MainMenu
from user_input import UserInput

class Application(tk.Frame):
	def __init__(self, master=None):
		super().__init__(master)
		self.master = master
		
		entry = UserInput.user_input()
		menu = MainMenu.main_menu(self)
		
	
	def exitProgram(self):
		exit()

root = tk.Tk()
root.geometry("750x750+200+300")
root.title("Wireless Sensor Network")

frame = tk.Frame(root, width=500, height=500, background="white")
frame.pack()
	
app = Application(master=root)
app.mainloop()
