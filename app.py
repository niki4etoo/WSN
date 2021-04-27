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
checker_node = IntVar()

check_btn_active_node = Checkbutton(root, text="Is Active", variable=checker_node, \
									onvalue = 1, offvalue = 0, height = 5, width = 20)
check_btn_active_node.pack()

app = Application(master=root)
app.mainloop()
