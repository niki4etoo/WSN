import tkinter as tk
from tkinter import *
from tkinter.messagebox import showinfo

def openInfoBox():
		showinfo(title="Short Description about the author",
				 message="Hi, nice user! My name is Nikolay Nanev!")

def optionsWindow():
	showinfo(title="Options for the WSN Simulator v1.0",
			message="To DO")

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
		
		menu.add_cascade(label="Edit", menu=editMenu)
		
		nodeMenu = Menu(menu)
		nodeMenu.add_command(label="Create New")
		nodeMenu.add_command(label="Select")
		nodeMenu.add_command(label="Move")
		nodeMenu.add_command(label="Rename")
		nodeMenu.add_command(label="Delete")
		nodeMenu.add_separator()
		nodeMenu.add_command(label="Options", command=optionsWindow)
		
		menu.add_cascade(label="Node", menu=nodeMenu)
		
		aboutMenu = Menu(menu)
		aboutMenu.add_command(label="Help")
		aboutMenu.add_command(label="Documentation")
		aboutMenu.add_command(label="Translations")
		aboutMenu.add_separator()
		aboutMenu.add_command(label="Info", command=openInfoBox)
		
		menu.add_cascade(label="About", menu=aboutMenu)
		
		gridMenu = Menu(menu)
		gridMenu.add_command(label="New")
		gridMenu.add_command(label="Save")
		gridMenu.add_command(label="Save As")
		gridMenu.add_separator()
		gridMenu.add_command(label="Options")
		
		menu.add_cascade(label="Grid", menu=gridMenu)
		
		settingsMenu = Menu(menu)
		settingsMenu.add_command(label="Window")
		settingsMenu.add_command(label="Workflow layout")
		settingsMenu.add_command(label="Styles")
		settingsMenu.add_separator()
		settingsMenu.add_command(label="Restore Default")
		
		menu.add_cascade(label="Settings", menu=settingsMenu)
		
		self.pack()
