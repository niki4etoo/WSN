import tkinter as tk
from tkinter import *
from pynput.mouse import Button, Controller

import networkx as nx
import matplotlib.pyplot as plt

from main_menu import MainMenu
from user_input import UserInput

mouse = Controller()

print('The current pointer position is {0}'.format(mouse.position))

mouse.position = (10, 20)
print('Now we have moved it to {0}'.format(mouse.position))

mouse.move(5, -5)

class Application(tk.Frame):
	def __init__(self, master=None):
		super().__init__(master)
		self.master = master
		
		menu = MainMenu.main_menu(self)
		entry = UserInput.user_input(self)		
	
	def exitProgram(self):
		exit()

root = tk.Tk()
root.geometry("750x750+200+300")
root.title("Wireless Sensor Network")
checker_node = IntVar()

check_btn_active_node = Checkbutton(root, text="Is Active", variable=checker_node, \
									onvalue = 1, offvalue = 0, height = 1, width = 10)

check_btn_active_node.pack()

G = nx.petersen_graph()
plt.subplot(121)
nx.draw(G, with_labels=True, font_weight='bold')
plt.subplot(122)
nx.draw_shell(G, nlist=[range(5, 10), range(5)], with_labels=True, font_weight='bold')
plt.show()

# Other type of graph
G = nx.grid_2d_graph(4, 4)  # 4x4 grid

pos = nx.spring_layout(G, iterations=100)

plt.subplot(221)
nx.draw(G, pos, font_size=8)

plt.subplot(222)
nx.draw(G, pos, node_color="k", node_size=0, with_labels=False)

plt.subplot(223)
nx.draw(G, pos, node_color="g", node_size=250, with_labels=False, width=6)

plt.subplot(224)
H = G.to_directed()
nx.draw(H, pos, node_color="b", node_size=20, with_labels=False)

plt.show()

app = Application(master=root)
app.mainloop()
