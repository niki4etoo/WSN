import tkinter as tk
from tkinter import *
from tkinter.messagebox import showinfo

def openInfoBox():
		showinfo(title="Кратка информация за мен",
				 message="Здравей, потребителю! Името ми е Николай Нанев. Създадох това приложение с целта да обезпеча търсенето на най-кратък път между два възела в една безжична мрежа.")

def optionsWindow():
	showinfo(title="Опции за БСМ Симулатор в1.0",
			message="Предстои разработка")

def createNewGrid():
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
		nodeMenu.add_separator()
		nodeMenu.add_command(label="Опции", command=optionsWindow)
		
		menu.add_cascade(label="Възел", menu=nodeMenu)
		
		aboutMenu = Menu(menu)
		aboutMenu.add_command(label="Помощ")
		aboutMenu.add_command(label="Документация")
		aboutMenu.add_command(label="Преводи")
		aboutMenu.add_command(label="Английски")
		aboutMenu.add_command(label="Български")
		aboutMenu.add_separator()
		aboutMenu.add_command(label="Информация", command=openInfoBox)
		
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
