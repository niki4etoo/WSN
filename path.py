import matplotlib.pyplot as plt
import networkx as nx

G = nx.path_graph(18)
nx.draw(G)
plt.show()

class Path:
	active = False
	weight = [1, 10] #weight of the path
	length = [0, 10]
	visited = False
	
	def __init__(self, weight, length, active):
		print(weight)
		print(length)
		pass
	
	def isActive(self):
	    return active
	pass
	
	def isVisited(self):
		return visited
	pass
	
	def getLength(self):
		return length
	pass
	
test_path = Path([1, 20], 50, True)
	
