import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

G.add_node(1)
G.add_nodes_from([2, 3])
G.add_nodes_from([
		(4, {"color": "red"}),
		(5, {"color": "green"}),
])

H = nx.path_graph(10)
G.add_nodes_from(H)

#Displaying Graph

# Display Star graph
starGraph = nx.Graph()

starEdges = [['EP1', 'G'], ['EP2', 'G'], ['EP3', 'G'], ['EP4', 'G'], ['EP5', 'G']]
starGraph.add_edges_from(starEdges)
pos = nx.spring_layout(starGraph)
plt.figure()
nx.draw(starGraph, with_labels=True, font_weight='bold', node_size=800)
#plt.show()

#To do
starEdges = [['EP1', 'G'], ['EP2', 'G'], ['EP3', 'G'], ['EP4', 'G'], ['EP5', 'G']]
starGraph.add_edges_from(starEdges)
pos = nx.spring_layout(starGraph)
plt.figure()
nx.draw(starGraph, with_labels=True, font_weight='bold', node_size=800)
plt.show()
