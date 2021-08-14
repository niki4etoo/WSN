import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image

from UI.main_menu import MainMenu

class Application(tk.Frame):
	def __init__(self, master=None):
		super().__init__(master)
		self.master = master
		menu = MainMenu.main_menu(self)
		
		
		
	def exitProgram(self):
		exit()

root = tk.Tk()
root.geometry("450x450+150+150")
root.title("Симулатор на безжична сензорна мрежа")
root.wm_iconbitmap('@gear.xbm')

app = Application(master=root)
app.mainloop()
