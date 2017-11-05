from tkinter import *

root = Tk()
root.title('Example')

content=Frame(root)
myButtons=LabelFrame(content, text="My Buttons", padx=7, pady=7)

one = Button(myButtons, text="Button 1")
two = Button(myButtons, text="Button 2")
three = Button(myButtons, text="Button 3")
four = Button(myButtons, text="Button 4")

content.grid(column=0, row=0)
myButtons.grid(column=0, row=0)

one.grid(column=0, row=0)
two.grid(column=1, row=0)
three.grid(column=0, row=1)
four.grid(column=1, row=1)

root.grid_columnconfigure(0,weight=1)
root.grid_columnconfigure(1,weight=1)
root.grid_rowconfigure(0,weight=1)
root.grid_rowconfigure(1,weight=1)

root.mainloop()
