from node import Node

class Nodes(Node):
	
	count = 0
	nodes_type = ""
	nodes = []
	
	def __init__(self, nodes):
		super.__init__(self, name, grid, posX, posY, active)
		self.nodes = nodes #To do
		pass
		
	def add(self, index, item):
		self.nodes.insert(index, item)
		pass
		
	def insert(self, position):
		#To do
		pass
		
	def remove(self, nodes):
		#To Do
		pass
		
	def update(self, nodes):
		#To do
		pass
		
