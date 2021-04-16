import tkinter as tk
from tkinter import *

class UserInput():
	def __init__(self, master=None):
		self.master = master
		self.user_input()

	def user_input():
		#Entries
		entry_label_node_id = Label(text="ID:")
		entry_node_id = Entry(bg="black", fg="white")
		entry_label_node_name = Label(text="Name:")
		entry_node_name = Entry(bg="black", fg="white")
		entry_label_node_position = Label(text="Position:")
		entry_node_position = Entry(bg="black", fg="white")
		#Buttons
		
		btn_add = Button(text="Add")
		btn_edit = Button(text="Edit")
		btn_remove = Button(text="Remove")
		
		#To do
		entry_label_node_id.pack(side=LEFT)
		entry_node_id.pack(side=LEFT)
		btn_remove.pack(side=RIGHT)
		btn_edit.pack(side=RIGHT)
		btn_add.pack(side=RIGHT)
		
		entry_label_node_name.pack(side=LEFT)
		entry_node_name.pack(side=LEFT)
		entry_label_node_position.pack(side=LEFT)
		entry_node_position.pack(side=LEFT)
		
		
		
		
