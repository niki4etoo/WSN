from tkinter import messagebox

class Author:
	def __init__(self, fname, lname):
		self.fname = fname
		self.lname = lname
		messagebox.showinfo(message="Относно автора: Името ми е Николай Нанев.", title="Относно")
		print("Авторът на приложението е " + str(self.fname) + " " + str(self.lname))
	pass
