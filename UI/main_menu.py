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

def main_menu_english():
	pass

def main_menu_bulgarian():
	pass

def saveNewGrid():
	pass

def saveAsNewGrid():
	pass

def createNewGrid():
	grid = Grid()
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

def bellmanford_algorithm():
	pass

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
	author = Author("??????????????", "??????????")
	pass

def createNewNode():
	name = "???? ????????????????????????"
	print("?????????????????? ???? ?????? ?????????? ?? ?????? " + name)
	pass
	
def chooseNode():
	pass

def moveNode():
	pass

def renameNode():
	pass
	
def deleteNode():
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
		fileMenu.add_command(label="??????", command=createNewGrid)
		fileMenu.add_command(label="????????????", command=openFile)
		fileMenu.add_command(label="????????????", command=saveNewGrid)
		fileMenu.add_command(label="???????????? ????????", command=saveAsNewGrid)
		fileMenu.add_separator()
		fileMenu.add_command(label="??????????", command=self.exitProgram)
		menu.add_cascade(label="????????", menu=fileMenu)
		
		nodeMenu = Menu(menu)
		nodeMenu.add_command(label="???????????? ??????", command=createNewNode)
		nodeMenu.add_command(label="????????????", command=chooseNode)
		nodeMenu.add_command(label="????????????????", command=moveNode)
		nodeMenu.add_command(label="??????????????????????", command=renameNode)
		nodeMenu.add_command(label="????????????", command=deleteNode)
		
		menu.add_cascade(label="??????????", menu=nodeMenu)

		algorithmsMenu = Menu(menu)
		algorithmsMenu.add_command(label="????????????????", command=dijkstra_algorithm)
		algorithmsMenu.add_command(label="????????????-????????", command=bellmanford_algorithm)

		menu.add_cascade(label="??????????????????", menu=algorithmsMenu)
		
		aboutMenu = Menu(menu)
		aboutMenu.add_command(label="??????????", command=help_box)
		aboutMenu.add_command(label="??????????", command=author)
		aboutMenu.add_command(label="??????????????????", command=main_menu_english)
		aboutMenu.add_command(label="??????????????????", command=main_menu_bulgarian)
		
		menu.add_cascade(label="??????????????", menu=aboutMenu)
		
		generateGrid = Menu(menu)
		generateGrid.add_command(label="??????????", command=generateGrid)
		generateGrid.add_command(label="??????????????", command=generateTable)
		menu.add_cascade(label="??????????????????", menu=generateGrid, command=print("Generate a plot with the newly created nodes"))
		
		self.grid(row=0, column=0)
