class Node:
	starting = True
	ending = False
	
	name = ""
	weight = [1, 20]
	active = True
	edge_length = 0
	
	def __init__(self, name, grid, posX, posY, active):
		self.name = name 	 # Name of the node
		self.grid = grid	 # Which grid the node will be placed
		self.posX = posX	 # Position X on the grid
		self.posY = posY 	 # Position Y on the grid
		self.active = active # Is active

	def isEndingNode(self, ending):
		self.ending = ending
		pass
		
	def isStartingNode(self, starting):
		self.starting = starting
		pass

	def description(self):
		pass
		
	
		
