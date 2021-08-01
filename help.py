from tkinter import messagebox
import webbrowser

class Help:
	new = 1
	url = "https://www.github.com/niki4etoo/WSN/"
	
	def __init__(self):
		webbrowser.open(self.url,new=self.new)
		print("There is a github repository with the WSN Simulator Docs")
		
