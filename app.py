import tkinter as tk
from tkinter import *

class Application(tk.Frame):
	def __init__(self, master=None):
		super().__init__(master)
		self.master = master
		
		menu = Menu(self.master)
		self.master.config(menu=menu)
		
		fileMenu = Menu(menu)
		fileMenu.add_command(label="Item")
		fileMenu.add_command(label="Exit", command=self.exitProgram)
		menu.add_cascade(label="File", menu=fileMenu)
		
		editMenu = Menu(menu)
		editMenu.add_command(label="Undo")
		editMenu.add_command(label="Redo")
		menu.add_cascade(label="Edit", menu=editMenu)
		
		self.pack()
		self.create_widgets()
		
		
			
	def create_widgets(self):
		self.hi_there = tk.Button(self)
		self.hi_there["text"] = "WSN"
		self.hi_there["command"] = self.say_hi
		self.hi_there.pack(side="top")
		
		self.quit = tk.Button(self, text="Quit", fg="red",
							  command=self.master.destroy)
		self.quit.pack(side="bottom")
	
	def exitProgram(self):
		exit()
	
	def say_hi(self):
		print("hi there, everyone!")
		
root = tk.Tk()

frame = tk.Frame(root, width=250, height=150, background="bisque")
frame.pack(fill=None, expand=False)
app = Application(master=root)
app.mainloop()
