import tkinter as tk
from tkinter import *
import UI.main_menu

class Grid:
	
	#Input fields for a new file and nodes count 
	
	global entry_label_nodes_count
	global entry_nodes_count
	global entry_label_file_name
	global entry_file_name
	
	#Members for error messages
	global error_messages_frame
	global error_message_low_nodes
	
	nodes_count = 0
	
	# Nodes set of name, weight and state ( 1 - source 2 - target 0 - common )
	nodesSet = []
	
	#Windows
	global grid_window
	
	#Buttons 
	global button_add
	
	def __init__(self):
		pass
		
	def createNew(self):
		self.entry_label_nodes_count = Label(text="Брой възли:")
		self.entry_nodes_count = Entry(bg="white", fg="black", border=3)
		
		self.entry_label_file_name = Label(text="Име на файл: ")
		self.entry_file_name = Entry(bg="white", fg="black", border=3)
		
		# Add button
		self.button_add = Button(text="Добави", command=lambda: self.newGrid(int(self.entry_nodes_count.get()), str(self.entry_file_name.get())))
		
		# Layout for the adding new file
		self.entry_label_file_name.grid(row=1, column=0, padx=10, pady=10)
		self.entry_file_name.grid(row=1, column=1, padx=10, pady=10)
		self.entry_label_nodes_count.grid(row=2, column=0, padx=10, pady=10)
		self.entry_nodes_count.grid(row=2, column=1, padx=10, pady=10)
		self.button_add.grid(row=3, column=1, padx=10, pady=10)
	pass
	
	def newGrid(self, nodes_count, filename):
	
		# Frame for network parameters
		network_parameters_frame = LabelFrame(text="Параметри", padx=10, pady=10)
		if nodes_count > 3:
			if filename != "":
				# Creating new project file
				new_file = open(filename + ".prjwsn", "w")
			
			global nodes_count_label
			network_parameters_frame.grid(row=1, column=1, sticky=E, padx=10, pady=10)
			nodes_count_label = Label(network_parameters_frame, text="Брой Възли: " + str(nodes_count))
			nodes_count_label.grid(row=0, column=2)
			
			# Clear user input for nodes
			self.button_add.grid_forget()
			self.entry_nodes_count.grid_forget()
			self.entry_label_nodes_count.grid_forget()
			self.entry_file_name.grid_forget()
			self.entry_label_file_name.grid_forget()
			if hasattr(self, 'error_messages_frame'):
				self.error_messages_frame.grid_forget()
			
			global node_state
			node_state = IntVar()
			i = 0
			nodes_frame = LabelFrame(text="Възел " + str(i+1))

			node_name_entry_label = Label(nodes_frame, text="Име: ")
			node_name_entry = Entry(nodes_frame, bg="white", fg="black", border=3)
			node_weight_entry_label = Label(nodes_frame, text="Тежест: ")
			node_weight_entry = Entry(nodes_frame, bg="white", fg="black", border=3)
			node_start_radiobutton = Radiobutton(nodes_frame, text="Начален", variable=node_state, value="1")
			node_end_radiobutton = Radiobutton(nodes_frame, text="Краен", variable=node_state, value="2")
			node_button_add = Button(nodes_frame, text="Добави", command=lambda: self.grid(i+1, nodes_count, str(node_name_entry.get()), int(node_weight_entry.get()), node_state.get()))
			
			nodes_frame.grid(row=1, column=0, padx=30, pady=10)
			node_name_entry_label.grid(row=1, column=0, sticky=E)
			node_name_entry.grid(row=1, column=1, padx=10)
			node_weight_entry_label.grid(row=2, column=0, sticky=E)
			node_weight_entry.grid(row=2, column=1, padx=10)
			node_start_radiobutton.grid(row=3, column=0)
			node_end_radiobutton.grid(row=3, column=1)
			node_button_add.grid(row=4, column=1, columnspan=2)
			
		elif nodes_count <= 3:
			self.error_messages_frame = LabelFrame(padx=10, pady=10)
			self.error_message_low_nodes = Label(self.error_messages_frame, text="Броят възли е по-малък от 3. Моля добавете повече от три възела")
			print(self.error_messages_frame)
			self.error_messages_frame.grid(row=0, column=0)
			self.error_message_low_nodes.grid(row=0, column=0)
	pass
	
	def show(self, nodes):
		grid_window = Tk()
		grid_window.title("Информация за сензорната мрежа")
		grid_window.geometry("400x250")
		grid_label = Label(show_grid_window, text="Име: " + str(nodes[0]) + " Тежест: " + str(nodes[1]))
		grid_label.grid(row=0, column=1, padx=10, pady=10)
	pass
		
	
	def grid(self, i, nodes_count, name, weight, node_state):
		self.nodes_count = nodes_count
		self.nodesSet.append(name)
		self.nodesSet.append(weight)
		self.nodesSet.append(node_state)
		
		print(self.nodesSet)
		# User Input
		nodes_frame = LabelFrame(text="Възел " + str(i+1))
		node_name_entry_label = Label(nodes_frame, text="Име: ")
		node_name_entry = Entry(nodes_frame, bg="white", fg="black", border=3)
		node_weight_entry_label = Label(nodes_frame, text="Тежест: ")
		node_weight_entry = Entry(nodes_frame, bg="white", fg="black", border=3)
		node_state = IntVar()
		node_start_radiobutton = Radiobutton(nodes_frame, text="Начален", variable=node_state, value="1")
		node_end_radiobutton = Radiobutton(nodes_frame, text="Краен", variable=node_state, value="2")	
		
		if i == nodes_count:
			node_button_add = Button(nodes_frame, text="Добави", state=DISABLED)
			show_nodes = Button(nodes_frame, text="Покажи", command=lambda: show_grid(nodes))
			show_nodes.grid(row=6, column=0)
		else:
			node_button_add = Button(nodes_frame, text="Добави", command=lambda: self.grid(i+1, nodes_count, str(node_name_entry.get()), int(node_weight_entry.get()), node_state.get()))
		
		nodes_frame.grid(row=1, column=0, padx=20, pady=10)
		node_name_entry_label.grid(row=1, column=0, sticky=E)
		node_name_entry.grid(row=1, column=1, padx=10)
		node_weight_entry_label.grid(row=2, column=0, sticky=E)
		node_weight_entry.grid(row=2, column=1, padx=10)
		
		node_start_radiobutton.grid(row=3, column=0)
		node_end_radiobutton.grid(row=3, column=1)
		node_button_add.grid(row=4, column=1, columnspan=2)
