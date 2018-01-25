import tkinter as tk
import tkFont
class SEARCH:
 def __init__(self):
	self.root2 = tk.Tk()
	self.root2.title('Search')
	self.root2.minsize(1366, 300)
	self.root2.bind('<Return>', self.find)
	self.font2 = tkFont.Font(size = 20)
	self.font4 = tkFont.Font(size = 10)

	self.entry = tk.Entry(self.root2, font = self.font2, width = 150)
	self.entry.grid(row = 0, column = 0, columnspan = 7,
				sticky = tk.EW +tk.NS)
	self.button = tk.Button(self.root2,text = 'Search', width = 10,
			        font = self.font2, command = self.find)
	self.button.grid(row = 0, column = 7, columnspan = 3,
				 sticky = tk.EW + tk.NS)

	self.root2.columnconfigure((0,7,8,9), weight = 1)
	self.text_display()
	self.root2.mainloop()

 def text_display(self):
	lab1 = tk.Label(self.root2, text = "Items", font = self.font2)
	lab2 = tk.Label(self.root2, text = "Price", font = self.font4, width = 3)
	lab3 = tk.Label(self.root2, text = "Quantity", font = self.font4, width = 3)
	lab4 = tk.Label(self.root2, text = "Total Price", font = self.font4, width = 3)
	lab1.grid(row = 1, column =0, columnspan = 7, sticky = tk.EW + tk.NS)
	lab2.grid(row = 1, column =7, sticky = tk.EW + tk.NS)
	lab3.grid(row = 1, column =8, sticky = tk.EW + tk.NS)
	lab4.grid(row = 1, column =9, sticky = tk.EW + tk.NS)

	self.text1 = tk.Text(self.root2,
			takefocus = 0, state = 'disabled', border = 0,
				wrap = 'none',bg = 'khaki', font = self.font4)
	self.text1.grid(row = 2, column =0, columnspan = 7, sticky = tk.EW + tk.NS)
	self.text2 = tk.Text(self.root2,
                        takefocus = 0, state = 'disabled', border = 0,
                                wrap = 'none',bg = 'khaki')
        self.text2.grid(row = 2, column =7, sticky = tk.EW + tk.NS)
        self.text3 = tk.Text(self.root2,
                        takefocus = 0, state = 'disabled', border = 0,
                                wrap = 'none',bg = 'khaki')
        self.text3.grid(row = 2, column =8, sticky = tk.EW + tk.NS)
        self.text4 = tk.Text(self.root2,
                        takefocus = 0, state = 'disabled', border = 0,
                                wrap = 'none',bg = 'khaki')
        self.text4.grid(row = 2, column =9, sticky = tk.EW + tk.NS)

 #here we make function which search in file and if it find items it call display
 def find(self, event = None):
	self.var = 0
	self.clear() #here we clear the value of the last operation
	find_type = self.entry.get() #we get new inserted value
	f = open('file')
	for line in f:		#we search for value in file
	 line_content = line.split('\t')
	 if find_type == line_content[0]:
	     self.display(line_content) # if we found it we display it
	     self.var = 1  #if not we call error function
	self.error()

 def display(self, show):
	self.text1.config(state = 'normal')
	self.text2.config(state = 'normal')
	self.text3.config(state = 'normal')
	self.text4.config(state = 'normal')
	try:
	  show[1] = int(show[1])
	  show[2] = int(show[2])
	  self.text4.insert(1.0, show[1] * show[2])
	except ValueError:
	 self.text1.insert(1.0, 'quantity or price was not inserted')
	 return
	self.text1.insert(1.0, show[0])
        self.text1.insert(1.0, '\n')
        self.text2.insert(1.0, show[1])
        self.text2.insert(1.0, '\n')
        self.text3.insert(1.0, show[2])
        self.text3.insert(1.0, '\n')

	self.text4.insert(1.0, '\n')
	self.text1.config(state = 'disabled')
	self.text2.config(state = 'disabled')
	self.text3.config(state = 'disabled')
	self.text4.config(state = 'disabled')

 def clear(self):
	self.text1.config(state = 'normal')
        self.text2.config(state = 'normal')
        self.text3.config(state = 'normal')
        self.text4.config(state = 'normal')
        self.text1.delete(1.0, tk.END)
        self.text2.delete(1.0, tk.END)
        self.text3.delete(1.0, tk.END)
	self.text4.delete(1.0, tk.END)
        self.text1.config(state = 'disabled')
        self.text2.config(state = 'disabled')
        self.text3.config(state = 'disabled')
        self.text4.config(state = 'disabled')


 def error(self):
	if self.var == 0:
	 self.clear()
	 self.text1.config(state = 'normal')
	 self.text1.insert(1.0,"sorry we didn't find the Item you search for")
	 self.text1.config(state = 'disabled')
