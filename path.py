import matplotlib.pyplot as plt
import networkx as nx

G = nx.path_graph(18)
nx.draw(G)
plt.show()

class Path:
	active = False
	weight = [1, 10] #weight of the path
	
	def __init__(self, weight, active):
		print(weight)
		pass
	
	def is_active(self):
	    return active
	pass
	
test_path = Path([1, 20], True)
	
