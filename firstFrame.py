from tkinter import *

root = Tk()
root.title('Example')
#root.geometry('300x300')

content=Frame(root)

myButtons=LabelFrame(content, text="My Buttons", padx=5, pady=5)

one = Button(myButtons, text="Button 1")
two = Button(myButtons, text="Button 2")
three = Button(myButtons, text="Button 3")
four = Button(myButtons, text="Button 4")

content.grid(column=0, row=0, sticky="nsew")
myButtons.grid(column=0, row=0, sticky="nsew")

one.grid(column=0, row=0, columnspan=1, sticky="nsew")
two.grid(column=1, row=0, columnspan=1, sticky="nsew")
three.grid(column=0, row=1, columnspan=1, sticky="nsew")
four.grid(column=1, row=1, columnspan=1, sticky="nsew")

root.grid_rowconfigure(0,weight=1)
root.grid_columnconfigure(0,weight=1)

content.grid_rowconfigure(0, weight=1)
content.grid_columnconfigure(0, weight=1)

myButtons.grid_rowconfigure(0, weight=1)
myButtons.grid_rowconfigure(1, weight=1)
myButtons.grid_columnconfigure(0, weight=1)
myButtons.grid_columnconfigure(1, weight=1)

root.mainloop()
