import tkinter as tk
import tkFont
from sys import exit
from add import ADD
from search import SEARCH

class FACE:
 def __init__(self):
	self.root1 = tk.Tk()
	self.root1.minsize(500, 200)
	self.root1.title("Abdulrahman")
	#columnconfigure make column resizable
	self.root1.columnconfigure((5,9), weight = 1)
	self.root1.rowconfigure((3,7), weight =1)
	self.font1 = tkFont.Font(size = 20, weight = 'bold')

	self.label1 = tk.Label(self.root1, text = 'Welcome to Awlad Elsheikh',
				 font = self.font1)
	self.label1.grid(row = 3,column =5,
				 columnspan = 10, sticky = tk.E + tk.W)
	self.button1 = tk.Button(self.root1, text = "Search",
				 font =self.font1, command = self.searchFun)
	self.button1.grid(row = 7,column = 5,
				 columnspan = 3, sticky = tk.EW + tk.NS)
	self.button2 = tk.Button(self.root1, text = "Add",
				 font = self.font1, command = self.addFun)
	self.button2.grid(row = 7,column = 9,
				 columnspan = 3, sticky = tk.EW + tk.NS)
	self.root1.mainloop()


 def searchFun(self):
	obj = SEARCH()

 def addFun(self):
	obj = ADD()
