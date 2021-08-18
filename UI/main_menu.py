import tkinter as tk
from tkinter import *
from tkinter.messagebox import showinfo
from tkinter import filedialog
from grid import Grid
from author import Author
from help import Help

#Each node parameters
global node_name
global node_weight
global node_pos_x
global node_pos_y

global nodes
nodes = []

def createNewGrid():
	grid = Grid("name")
	grid.createNew()

def add_nodes(i, nodes_count, name, weight, pos_x, pos_y, node_state):
	node_name = name
	node_weight = weight
	node_pos_x = pos_x
	node_pos_y = pos_y
	
	nodes.append(node_name)
	nodes.append(node_weight)
	nodes.append(node_pos_x)
	nodes.append(node_pos_y)
	nodes.append(node_state)
	
	grid = Grid("New Grid 1", 100, 100)
	grid.grid(i, node_pos_x, node_pos_y, nodes_count, nodes)
		
def openFile():
	filedialog.askopenfilename(initialdir="files", title="Select a file", filetypes=(("pdf files", "*.pdf"),("project files", "*.prjwsn")))

def dijkstra_algorithm():
	# Python program for Dijkstra's single
	# source shortest path algorithm. The program is
	# for adjacency matrix representation of the graph
	 
	# Library for INT_MAX
	import sys
	 
	class Graph():
	 
		def __init__(self, vertices):
			self.V = vertices
			self.graph = [[0 for column in range(vertices)]
						  for row in range(vertices)]
	 
		def printSolution(self, dist):
			print("Vertex tDistance from Source")
			for node in range(self.V):
				print(node, "t", dist[node])
	 
		# A utility function to find the vertex with
		# minimum distance value, from the set of vertices
		# not yet included in shortest path tree
		def minDistance(self, dist, sptSet):
	 
			# Initialize minimum distance for next node
			min = sys.maxsize
	 
			# Search not nearest vertex not in the
			# shortest path tree
			for v in range(self.V):
				if dist[v] < min and sptSet[v] == False:
					min = dist[v]
					min_index = v
	 
			return min_index
	 
		# Funtion that implements Dijkstra's single source
		# shortest path algorithm for a graph represented
		# using adjacency matrix representation
		def dijkstra(self, src):
	 
			dist = [sys.maxsize] * self.V
			dist[src] = 0
			sptSet = [False] * self.V
	 
			for cout in range(self.V):
	 
				# Pick the minimum distance vertex from
				# the set of vertices not yet processed.
				# u is always equal to src in first iteration
				u = self.minDistance(dist, sptSet)
	 
				# Put the minimum distance vertex in the
				# shortest path tree
				sptSet[u] = True
	 
				# Update dist value of the adjacent vertices
				# of the picked vertex only if the current
				# distance is greater than new distance and
				# the vertex in not in the shortest path tree
				for v in range(self.V):
					if self.graph[u][v] > 0 and sptSet[v] == False and dist[v] > dist[u] + self.graph[u][v]:
						dist[v] = dist[u] + self.graph[u][v]
			self.printSolution(dist)
	 
	 
	# Driver program
	g = Graph(9)
	g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
			   [4, 0, 8, 0, 0, 0, 0, 11, 0],
			   [0, 8, 0, 7, 0, 4, 0, 0, 2],
			   [0, 0, 7, 0, 9, 14, 0, 0, 0],
			   [0, 0, 0, 9, 0, 10, 0, 0, 0],
			   [0, 0, 4, 14, 10, 0, 2, 0, 0],
			   [0, 0, 0, 0, 0, 2, 0, 1, 6],
			   [8, 11, 0, 0, 0, 0, 1, 0, 7],
			   [0, 0, 2, 0, 0, 0, 6, 7, 0]
			   ]
	 
	g.dijkstra(0)
	
	pass

def help_box():
	help = Help()
	pass

def author():
	author = Author("Николай", "Нанев")
	pass

def createNewNode():
	name = "по подразбиране"
	print("Създаване на нов възел с име " + name)
	pass

def generateGrid():
	print("Generating a grid using the matlibplot")
	pass

def generateTable():
	print("Generating a table with nodes parameters")
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
		fileMenu.add_command(label="Отвори", command=openFile)
		fileMenu.add_command(label="Запази", command=saveNewGrid)
		fileMenu.add_command(label="Запази като", command=saveAsNewGrid)
		fileMenu.add_separator()
		fileMenu.add_command(label="Изход", command=self.exitProgram)
		menu.add_cascade(label="Файл", menu=fileMenu)
		
		nodeMenu = Menu(menu)
		nodeMenu.add_command(label="Създай нов", command=createNewNode)
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
		
		generateGrid = Menu(menu)
		generateGrid.add_command(label="Мрежа", command=generateGrid)
		generateGrid.add_command(label="Таблица", command=generateTable)
		menu.add_cascade(label="Генерирай", menu=generateGrid, command=print("Generate a plot with the newly created nodes"))
		
		self.grid(row=0, column=0)
