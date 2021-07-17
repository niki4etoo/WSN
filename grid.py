import tkinter as tk
from tkinter import *
import main_menu

class Grid:
	nodes_count = 0
	title = ""
	text = ""
	width = 0
	height = 0
	
	def __init__(self, name, width, height):
		self.name = name
		self.width = width
		self.height = height
		pass
		
	def grid(self, i, width, height, nodes_count, nodes):
		self.width = width
		self.height = height
		self.nodes_count = nodes_count
		
		# User Input
		nodes_frame = LabelFrame(text="Възел " + str(i+1))
		node_name_entry_label = Label(nodes_frame, text="Име: ")
		node_name_entry = Entry(nodes_frame, bg="white", fg="black", border=3)
		node_weight_entry_label = Label(nodes_frame, text="Тежест: ")
		node_weight_entry = Entry(nodes_frame, bg="white", fg="black", border=3)
		node_pos_x_entry_label = Label(nodes_frame, text="Позиция по x: ")
		node_pos_x_entry = Entry(nodes_frame, bg="white", fg="black", border=3)
		node_pos_y_entry_label = Label(nodes_frame, text="Позиция по y: ")
		node_pos_y_entry = Entry(nodes_frame, bg="white", fg="black", border=3)
		node_state = IntVar()
		node_start_radiobutton = Radiobutton(nodes_frame, text="Начален", variable=node_state, value="1")
		node_end_radiobutton = Radiobutton(nodes_frame, text="Краен", variable=node_state, value="2")	
		
		if i == nodes_count:
			node_button_add = Button(nodes_frame, text="Добави", state=DISABLED)
			show_nodes = Button(nodes_frame, text="Покажи", command=lambda: show_grid(nodes))
			show_nodes.grid(row=6, column=0)
		else:
			node_button_add = Button(nodes_frame, text="Добави", command=lambda: add_nodes(i+1, nodes_count, str(node_name_entry.get()), int(node_weight_entry.get()), int(node_pos_x_entry.get()), int(node_pos_y_entry.get()), node_state.get()))
		
		nodes_frame.grid(row=1, column=0, padx=20, pady=10)
		node_name_entry_label.grid(row=1, column=0, sticky=E)
		node_name_entry.grid(row=1, column=1, padx=10)
		node_weight_entry_label.grid(row=2, column=0, sticky=E)
		node_weight_entry.grid(row=2, column=1, padx=10)
		node_pos_x_entry_label.grid(row=3, column=0, sticky=E)
		node_pos_x_entry.grid(row=3, column=1, padx=10)
		node_pos_y_entry_label.grid(row=4, column=0, sticky=E)
		node_pos_y_entry.grid(row=4, column=1, padx=10)
		
		print(nodes)
		
		node_start_radiobutton.grid(row=5, column=0)
		node_end_radiobutton.grid(row=5, column=1)
		node_button_add.grid(row=6, column=1, columnspan=2)
		
	def description(self, title, text, description):
		self.title = title
		self.text = text
