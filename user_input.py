import tkinter as tk
from tkinter import *

def add_message_box(self):
	tk.messagebox.showinfo("Add new node", "You have just added new node")
	node_label_result = Label(text=entry_node_id.get())
	node_label_result.pack(side=RIGHT)
		
def edit_message_box(self):
	tk.messagebox.showinfo("Edit node", "You need to edit this node")
	
def remove_message_box(self):
	tk.messagebox.showinfo("Remove node", "You have just removed the node")

class UserInput():
	def __init__(self, master=None):
		self.master = master
		self.user_input()

	def user_input(self, master=None):
		#Entries
		entry_label_node_id = Label(text="ID:")
		entry_node_id = Entry(bg="black", fg="white")
		entry_label_node_name = Label(text="Name:")
		entry_node_name = Entry(bg="black", fg="white")
		entry_label_node_position = Label(text="Position:")
		entry_node_position = Entry(bg="black", fg="white")
		
		#Buttons
		btn_add = Button(text="Add", command=add_message_box)
		btn_edit = Button(text="Edit", command=edit_message_box)
		btn_remove = Button(text="Remove", command=remove_message_box)
		
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
		
