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

#Display Mesh graph
meshGraph = nx.Graph()
meshEdges = [['EP1', 'G'], ['EP2', 'G'], ['EP3', 'G'], ['EP4', 'G'], ['EP5', 'G'],
			 ['EP1', 'EP2'], ['EP2', 'EP3'], ['EP3', 'EP4'], ['EP4', 'EP5'], ['EP5', 'EP1']]
meshGraph.add_edges_from(meshEdges)
pos = nx.spring_layout(meshGraph)
#plt.figure()
#nx.draw(meshGraph, with_labels=True, font_weight='bold', node_size=800)
#plt.show()

#Display Star-Mesh Graph
starMeshGraph = nx.Graph()
starMeshEdges = [['EP1', 'G'], ['EP2', 'G'], ['EP3', 'G'], ['EP4', 'G'], ['EP5', 'G'],
			 ['EP1', 'EP2'], ['EP2', 'EP3'], ['EP3', 'EP4'], ['EP4', 'EP5'], ['EP5', 'EP1'],
			 ['EP1', 'E'], ['EP2', 'E'], ['EP5', 'M'], ['EP1', 'M'], ['EP3', 'T'], ['EP4', 'T']]
starMeshGraph.add_edges_from(starMeshEdges)
pos = nx.spring_layout(starMeshGraph)
plt.figure()
nx.draw(starMeshGraph, with_labels=True, font_weight='bold', node_size=800)
plt.show()

#Display example 1 of adjecancy matrix graph
starMeshGraph = nx.Graph()
starMeshEdges = [['1', '2'], ['1', '3'], ['2', '3'], ['2', '4'], ['4', '3'], ['4', '5'], ['5', '2'], ['5', '3']]
starMeshGraph.add_edges_from(starMeshEdges)
pos = nx.spring_layout(starMeshGraph)
plt.figure()
nx.draw(starMeshGraph, with_labels=True, font_weight='bold', node_size=800)
plt.show()

#Display example 2 of adjecancy matrix graph (to do )
starMeshGraph = nx.Graph()
starMeshEdges = [['1', '1'], ['1', '2'], ['1', '5'], ['2', '5'], ['2', '3'], ['3', '4'], ['4', '5'], ['4', '6']]
starMeshGraph.add_edges_from(starMeshEdges)
pos = nx.spring_layout(starMeshGraph)
plt.figure()
nx.draw(starMeshGraph, with_labels=True, font_weight='bold', node_size=800)
plt.show()
