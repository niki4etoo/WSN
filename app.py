import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image

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
root.geometry("450x450+200+300")
root.title("Симулатор на безжична сензорна мрежа")
root.wm_iconbitmap('@gear.xbm')

app = Application(master=root)
app.mainloop()
