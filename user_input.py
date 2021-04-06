import tkinter as tk
from tkinter import *

class UserInput():
	def __init__(self, master=None):
		self.master = master
		self.user_input()

	def user_input():
		entry = Entry()
		entry.pack()
