import tkinter as tk
from tkinter import *
from tkinter.messagebox import showinfo


def newGridWithNodesCount(nodes_count):
	if nodes_count >= 3:
		global nodes_count_label
		
		# Frame for network parameters
		network_parameters_frame = LabelFrame(text="Параметри", padx=10, pady=10)
		
		nodes_count_label = Label(network_parameters_frame, text="Брой Възли: " + str(nodes_count))
		nodes_count_label.grid(row=1, column=0)
		network_parameters_frame.grid(row=2, column=0, sticky=W+E)
	elif nodes_count < 2:
		global error_message_low_nodes
		error_message_low_nodes = Label(network_parameters_frame, text="Броят възли е по-малък от 2. Моля добавете повече от два възела")
		error_message_low_nodes.grid(row=1, column=0)
		network_parameters_frame.grid(row=2, column=0, sticky=W+E)

def createNewGrid():
	entry_label_node_id = Label(text="Брой възли:")
	entry_node_id = Entry(bg="white", fg="black", border=3)
	
	# Add button
	button_add = Button(text="Добави", command=lambda: newGridWithNodesCount(int(entry_node_id.get())))
	
	entry_label_node_id.grid(row=1, column=0)
	entry_node_id.grid(row=1, column=1)
	button_add.grid(row=1, column=2)
	pass
		
def saveNewGrid():
	pass
	
def saveAsNewGrid():
	pass

def dijkstra_algorithm():
	pass

def belman_ford_algorithm():
	pass
	
def a_star_algorithm():
	pass
	
def floyd_warshall_algorithm():
	pass

def help_box():
	pass

def author():
	pass

def main_menu_english():
	pass
	
def main_menu_bulgarian():
	pass

class MainMenu():
	def __init__(self, master=None):
		self.master = master
		self.main_menu()
		
	def main_menu(self):
		menu = Menu(self.master)
		self.master.config(menu=menu)
		
		fileMenu = Menu(menu)
		fileMenu.add_command(label="Нов", command=createNewGrid)
		fileMenu.add_command(label="Отвори")
		fileMenu.add_command(label="Запази", command=saveNewGrid)
		fileMenu.add_command(label="Запази като", command=saveAsNewGrid)
		fileMenu.add_separator()
		fileMenu.add_command(label="Изход", command=self.exitProgram)
		menu.add_cascade(label="Файл", menu=fileMenu)
		
		nodeMenu = Menu(menu)
		nodeMenu.add_command(label="Създай нов")
		nodeMenu.add_command(label="Избери")
		nodeMenu.add_command(label="Премести")
		nodeMenu.add_command(label="Преименувай")
		nodeMenu.add_command(label="Изтрий")
		
		menu.add_cascade(label="Възел", menu=nodeMenu)

		algorithmsMenu = Menu(menu)
		algorithmsMenu.add_command(label="Дейкстра", command=dijkstra_algorithm)
		algorithmsMenu.add_command(label="Белман-Форд", command=belman_ford_algorithm)
		algorithmsMenu.add_command(label="А*", command=a_star_algorithm)
		algorithmsMenu.add_command(label="Флойд-Уоршал", command=floyd_warshall_algorithm)

		menu.add_cascade(label="Алгоритми", menu=algorithmsMenu)
		
		aboutMenu = Menu(menu)
		aboutMenu.add_command(label="Помощ", command=help_box)
		aboutMenu.add_command(label="Автор", command=author)
		aboutMenu.add_command(label="Английски", command=main_menu_english)
		aboutMenu.add_command(label="Български", command=main_menu_bulgarian)
		
		menu.add_cascade(label="Относно", menu=aboutMenu)
		
		self.grid(row=0, column=0)
