import tkinter as tk
from tkinter import *
import UI.main_menu

class Grid:
	global button_add
	global entry_label_node_id
	global entry_node_id
	global entry_label_file_name
	global entry_file_name
	
	nodes_count = 0
	title = ""
	text = ""
	
	#Windows
	global grid_window
	
	#Buttons 
	
	
	def __init__(self, name):
		self.name = name
		pass
		
	def createNew():	
		entry_label_node_id = Label(text="Брой възли:")
		entry_node_id = Entry(bg="white", fg="black", border=3)
		
		entry_label_file_name = Label(text="Име на файл: ")
		entry_file_name = Entry(bg="white", fg="black", border=3)
		
		# Add button
		button_add = Button(text="Добави", command=lambda: newGridWithNodesCount(int(entry_node_id.get()), str(entry_file_name.get())))
		
		entry_label_file_name.grid(row=0, column=0, padx=10, pady=10)
		entry_file_name.grid(row=0, column=1, padx=10, pady=10)
		entry_label_node_id.grid(row=1, column=0, padx=10, pady=10)
		entry_node_id.grid(row=1, column=1, padx=10, pady=10)
		button_add.grid(row=2, column=1, padx=10, pady=10)
	pass
	
	def show(self, nodes):
		grid_window = Tk()
		grid_window.title("Информация за сензорната мрежа")
		grid_window.geometry("400x250")
		grid_label = Label(show_grid_window, text="Име: " + str(nodes[0]) + " Тежест: " + str(nodes[1]))
		grid_label.grid(row=0, column=1, padx=10, pady=10)
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
		
		node_start_radiobutton.grid(row=5, column=0)
		node_end_radiobutton.grid(row=5, column=1)
		node_button_add.grid(row=6, column=1, columnspan=2)
