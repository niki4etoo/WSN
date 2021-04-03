import tkinter as tk
from tkinter import *

class MainMenu():
	def __init__(self, master=None):
		self.master = master
		self.main_menu()
		
	def main_menu(self):
		menu = Menu(self.master)
		self.master.config(menu=menu)
		
		fileMenu = Menu(menu)
		fileMenu.add_command(label="New")
		fileMenu.add_command(label="Open")
		fileMenu.add_command(label="Save")
		fileMenu.add_command(label="Save As")
		fileMenu.add_separator()
		fileMenu.add_command(label="Import ...")
		fileMenu.add_command(label="Export ...")
		fileMenu.add_separator()
		fileMenu.add_command(label="Exit", command=self.exitProgram)
		menu.add_cascade(label="File", menu=fileMenu)
		
		editMenu = Menu(menu)
		editMenu.add_command(label="Undo")
		editMenu.add_command(label="Redo")
		editMenu.add_separator()
		editMenu.add_command(label="Scale Up")
		editMenu.add_command(label="Scale Down")
		editMenu.add_separator()
		editMenu.add_command(label="Node")
		
		menu.add_cascade(label="Edit", menu=editMenu)
		
		self.pack()
