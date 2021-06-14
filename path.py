import matplotlib.pyplot as plt
import networkx as nx

G = nx.path_graph(18)
nx.draw(G)
plt.show()

class Path:
	active = False
	weight = [1, 10] #weight of the path
	length = [0, 10]
	
	def __init__(self, weight, length, active):
		print(weight)
		print(length)
		pass
	
	def is_active(self):
	    return active
	pass
	
test_path = Path([1, 20], 50, True)
	
