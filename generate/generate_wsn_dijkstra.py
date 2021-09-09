import networkx as nx
import matplotlib.pyplot as plt

# Dijkstra wsn example

G = nx.Graph()

color_map = ["green", "blue", "blue", "blue", "red", "blue", "blue", "yellow", "blue"]

#Displaying Graph
G_nodes = [ 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I' ]
G_edges = [['A', 'B', {'weight': 1}], ['A', 'C', {'weight': 1}], ['B', 'D', {'weight': 1}],
 ['B', 'E', {'weight': 2}], ['C', 'F', {'weight': 1}], ['C', 'G', {'weight': 1}], ['D', 'H', {'weight': 1}],
  ['E', 'H', {'weight': 2}], ['E', 'F', {'weight': 1}], ['F', 'I', {'weight': 1}], ['G', 'I', {'weight': 1}]]
G.add_nodes_from(G_nodes)
G.add_edges_from(G_edges)
pos = nx.spring_layout(G)

sp = nx.shortest_path(G, source=G_nodes[0], target=G_nodes[7], method="dijkstra")

#create a list of shortest-path edges:
sp_edges = [(sp[i],sp[i+1]) for i in range(len(sp)-1)]

edge_color_list = ["grey"]*len(G.edges)
#replace the color in edge_color_list with red if the edge belongs to the shortest path:
for i, edge in enumerate(G.edges()):
    if edge in sp_edges or (edge[1],edge[0]) in sp_edges:
        edge_color_list[i] = 'red'

plt.figure()
nx.draw(G, with_labels=True, font_weight='bold', node_color=color_map, edge_color=edge_color_list, node_size=800)
plt.show()
