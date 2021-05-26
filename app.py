import tkinter as tk
from tkinter import *
from pynput.mouse import Button, Controller
from main_menu import MainMenu
from user_input import UserInput

mouse = Controller()

print('The current pointer position is {0}'.format(mouse.position))

mouse.position = (10, 20)
print('Now we have moved it to {0}'.format(mouse.position))

mouse.move(5, -5)

class Application(tk.Frame):
	def __init__(self, master=None):
		super().__init__(master)
		self.master = master
		
		menu = MainMenu.main_menu(self)
		entry = UserInput.user_input(self)		
	
	def exitProgram(self):
		exit()

root = tk.Tk()
root.geometry("750x750+200+300")
root.title("Wireless Sensor Network")
checker_node = IntVar()

check_btn_active_node = Checkbutton(root, text="Is Active", variable=checker_node, \
									onvalue = 1, offvalue = 0, height = 1, width = 10)

check_btn_active_node.pack()

app = Application(master=root)
app.mainloop()
