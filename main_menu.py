import tkinter as tk
from tkinter import *
from tkinter.messagebox import showinfo


def newGridWithNodes(nodes_count):
	if nodes_count >= 3:
		print("Работеща мрежа")
	elif nodes_count < 2:
		print("Броят възли е по-малък от 2. Моля добавете повече от два възела")

def numberOfCells():
	entry_label_node_id = Label(text="Брой възли:")
	entry_node_id = Entry(bg="white", fg="black", border=3)
	
	# Add button
	button_add = Button(text="Добави", command=lambda: newGridWithNodes(int(entry_node_id.get())))
	
	entry_label_node_id.pack(side=TOP, fill=BOTH)
	entry_node_id.pack(side=TOP, fill=BOTH)
	button_add.pack(side=TOP, fill=BOTH)
	pass

def createNewGrid():
	numberOfCells()
	rows, cols = (32, 32)
	arr = [[0]*cols]*rows
	print(arr)
		

class MainMenu():
	def __init__(self, master=None):
		self.master = master
		self.main_menu()
		
	def main_menu(self):
		menu = Menu(self.master)
		self.master.config(menu=menu)
		
		fileMenu = Menu(menu)
		fileMenu.add_command(label="Нов", command=createNewGrid)
		fileMenu.add_command(label="Отвори")
		fileMenu.add_command(label="Запази")
		fileMenu.add_command(label="Запази като")
		fileMenu.add_separator()
		fileMenu.add_command(label="Вмъкни ...")
		fileMenu.add_command(label="Извади ...")
		fileMenu.add_separator()
		fileMenu.add_command(label="Изход", command=self.exitProgram)
		menu.add_cascade(label="Файл", menu=fileMenu)
		
		editMenu = Menu(menu)
		editMenu.add_command(label="Назад")
		editMenu.add_command(label="Напред")
		editMenu.add_separator()
		editMenu.add_command(label="Увеличи")
		editMenu.add_command(label="Намали")
		
		menu.add_cascade(label="Редактиране", menu=editMenu)
		
		nodeMenu = Menu(menu)
		nodeMenu.add_command(label="Създай нов")
		nodeMenu.add_command(label="Избери")
		nodeMenu.add_command(label="Премести")
		nodeMenu.add_command(label="Преименувай")
		nodeMenu.add_command(label="Изтрий")
		
		menu.add_cascade(label="Възел", menu=nodeMenu)
		
		aboutMenu = Menu(menu)
		aboutMenu.add_command(label="Помощ")
		aboutMenu.add_command(label="Документация")
		aboutMenu.add_command(label="Преводи")
		aboutMenu.add_command(label="Английски")
		aboutMenu.add_command(label="Български")
		
		menu.add_cascade(label="Относно", menu=aboutMenu)
		
		gridMenu = Menu(menu)
		gridMenu.add_command(label="Нов")
		gridMenu.add_command(label="Запази")
		gridMenu.add_command(label="Запази като")
		gridMenu.add_separator()
		gridMenu.add_command(label="Опции")
		
		menu.add_cascade(label="Мрежа", menu=gridMenu)
		
		settingsMenu = Menu(menu)
		settingsMenu.add_command(label="Прозорец")
		settingsMenu.add_command(label="Шаблон на работната среда")
		settingsMenu.add_command(label="Стилове")
		settingsMenu.add_separator()
		settingsMenu.add_command(label="Върни по подразбиране")
		
		menu.add_cascade(label="Настройки", menu=settingsMenu)
		
		self.pack()
