from tkinter import messagebox
import webbrowser




class Author:
	def __init__(self, fname, lname):
		self.fname = fname
		self.lname = lname
		result_answer = messagebox.askyesno(message="Относно автора: Името ми е Николай Нанев.", title="Относно")
		if result_answer == 1:
			self.opengithub()
		else:
			print("Авторът на приложението е " + str(self.fname) + " " + str(self.lname))
	pass
	
	new = 1
	url = "https://www.github.com/niki4etoo/"

	def opengithub(self):
		webbrowser.open(self.url,new=self.new)
