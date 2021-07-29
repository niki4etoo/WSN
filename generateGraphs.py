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
plt.show()

#To do
starEdges = [['EP1', 'G'], ['EP2', 'G'], ['EP3', 'G'], ['EP4', 'G'], ['EP5', 'G']]
starGraph.add_edges_from(starEdges)
pos = nx.spring_layout(starGraph)
plt.figure()
nx.draw(starGraph, with_labels=True, font_weight='bold', node_size=800)
plt.show()

testGraph = nx.Graph()
testGraph.add_nodes_from([0, 10])
testGraph.add_edge(1, 5)
testGraph.add_edge(2, 5)
testGraph.add_edge(3, 5)
testGraph.add_edge(4, 5)
testGraph.add_edge(6, 5)
testGraph.add_edge(7, 5)
testGraph.add_edge(8, 5)
testGraph.add_edge(9, 5)
testGraph.add_edge(0, 5)
testGraph.add_edge(10, 5)
weights = [ 1, 5, 3, 6, 8, 10, 13, 18, 20, 12 ]
nx.set_edge_attributes(testGraph, values = weights, name = 'weights')
testGraph.edges(data = True)
nx.draw_networkx_edge_labels(testGraph, nx.spring_layout(testGraph),edge_labels={(1,5):1,\
(2,5):5,(3,5):3},font_color='red')
#Star graph
nx.draw(testGraph, with_labels=True, font_weight='bold')
plt.axis('off')
plt.show()
