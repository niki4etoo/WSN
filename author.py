from tkinter import messagebox
import webbrowser

class Author:
	new = 1
	url = "https://www.github.com/niki4etoo/"
	
	def __init__(self, fname, lname):
		self.fname = fname
		self.lname = lname
		result_answer = messagebox.askyesno(message="Автор: Николай Нанев - Повече информация за мен в моят github профил. Желаете ли да го посетите?", title="Относно")
		if result_answer == 1:
			self.opengithub()
		else:
			print("Авторът на приложението е " + str(self.fname) + " " + str(self.lname))
	pass

	def opengithub(self):
		webbrowser.open(self.url,new=self.new)
