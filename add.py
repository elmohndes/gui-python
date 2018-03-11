import tkinter as tk
import tkFont
import time
class ADD:
 def __init__(self):
	self.root3 = tk.Tk()
	self.root3.title("Add")
	self.root3.minsize(1366, 300)
	self.root3.bind('<Return>', self.enter)
	self.font3 = tkFont.Font(size = 20)
	self.font5 = tkFont.Font(size = 30, weight = 'bold')

	self.display()
	self.root3.mainloop()

 def display(self):
	label1 = tk.Label(self.root3, text = "Item", font = self.font3, width = 50)
	label2 = tk.Label(self.root3, text = "Price", font = self.font3, width = 10)
	label3 = tk.Label(self.root3, text = "Quantity", font = self.font3, width = 11)

	label1.grid(row = 2, column = 1, columnspan = 9, sticky = tk.EW)
	label2.grid(row = 2, column = 10, sticky = tk.EW)
	label3.grid(row = 2, column = 11, sticky = tk.EW)

	self.entry1 = tk.Entry(self.root3, font = ('calibri', 20), width = 58)
	self.entry2 = tk.Entry(self.root3, font = ('calibri', 20), width = 10)
	self.entry3 = tk.Entry(self.root3, font = ('calibri', 20), width = 11)

	self.entry1.grid(row = 3, column = 1, columnspan = 9,
				 sticky = tk.EW + tk.NS)
	self.entry2.grid(row = 3, column = 10, sticky = tk.EW + tk.NS)
	self.entry3.grid(row = 3, column = 11, sticky = tk.EW + tk.NS)

	self.button = tk.Button(self.root3, text = "Add", font = self.font5,
				 width = 25, command = self.enter)
	self.button.grid(row = 6, column = 5, columnspan = 5, pady = 100,
				sticky = tk.EW + tk.NS)

#i wanted to make it able to increment and decrement quantity and price
#but i found to do this this i should delete all lines and rewrite them again
#so i will wait until know how to use mysql with python
#i'm sorry but program is not complete and i don't promis that it will be completed soon
 def enter(self, var = None):
	foo = open('file', 'a+')
	foo.write(self.entry1.get())
	foo.write('\t')
        foo.write(self.entry2.get())
        foo.write('\t')
        foo.write(self.entry3.get())
        foo.write('\n')
	foo.close()
	time.sleep(2)
	self.clear()


 def clear(self):
	self.entry1.delete(0, tk.END)
	self.entry2.delete(0, tk.END)
	self.entry3.delete(0, tk.END)
