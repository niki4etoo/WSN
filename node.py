class Node:
	starting = True
	ending = False
	
	name = ""
	weight = [1, 20]
	active = True
	edge_length = 0
	nodes = []
	
	def __init__(self, name, grid, posX, posY, active):
		self.name = name 	 # Name of the node
		self.grid = grid	 # Which grid the node will be placed
		self.posX = posX	 # Position X on the grid
		self.posY = posY 	 # Position Y on the grid
		self.active = active # Is active
		pass
		
	def add(self, newNode):
		#To DO
		self.nodes.append(newNode)
		print("Added new node")
		pass
	
	def remove(self, node):
		#To DO
		self.nodes = []
		print("The node has been removed")		
		pass
	
	def update(self, index, node):
		self.nodes.pop(index)
		self.nodes.insert(index, node)
		print("The node has been updated")
		pass
