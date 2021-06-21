class Grid:
	nodesCount = 0
	
	def __init__(self, name, width, height):
		self.name = name
		self.width = width
		self.height = height
		pass
		
	def grid(self, width, height, nodesCount):
		self.width = width
		self.height = height
		self.nodesCount = nodesCount
		
	def description(self, title, text):
		self.title = title
		self.text = text
