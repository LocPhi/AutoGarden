from tkinter import *

def raise_frame(frame):
    frame.tkraise()

# Main Window
root = Tk()
root.geometry('800x480')

f3 = Frame(root)
f3.grid(row=0, column=0, sticky='news')

listeOfPlant = Canvas(f3, bg='ivory')

back = Button(f3, text="<-")
confirm = Button(f3, text="Confirm")

back.grid(column=0, row=0, columnspan=1, sticky="news", padx=5, pady=5)
confirm.grid(column=0, row=3, columnspan=2, sticky="news", padx=5, pady=5)
listeOfPlant.grid(column=2, row=0, columnspan=3, rowspan=4, sticky="news", padx=5, pady=5)

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

f3.grid_rowconfigure(0, weight=1)
f3.grid_rowconfigure(1, weight=1)
f3.grid_rowconfigure(2, weight=1)
f3.grid_rowconfigure(3, weight=1)
f3.grid_rowconfigure(4, weight=1)
f3.grid_rowconfigure(5, weight=1)

f3.grid_columnconfigure(0, weight=1)
f3.grid_columnconfigure(1, weight=1)
f3.grid_columnconfigure(2, weight=1)
f3.grid_columnconfigure(3, weight=1)
f3.grid_columnconfigure(4, weight=1)

root.mainloop()