import tkinter as tk
from tkinter import *
from main_menu import MainMenu
from user_input import UserInput

class Application(tk.Frame):
	def __init__(self, master=None):
		super().__init__(master)
		self.master = master
		
		menu = MainMenu.main_menu(self)
		entry = UserInput.user_input()		
	
	def exitProgram(self):
		exit()

root = tk.Tk()
root.geometry("750x750+200+300")
root.title("Wireless Sensor Network")
	
app = Application(master=root)
app.mainloop()
