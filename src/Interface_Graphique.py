# ------- Grenoble INP - ESISAR -------
# -- PX504 : AutoGarden ---
# ---- Author : Loc Phi ----
# -- Date : 13/10/2017 --

from tkinter import *

def raise_frame(frame):
    frame.tkraise()

# Main Window
root = Tk()
root.geometry('800x480')

# All the frame that depend on the main window
f1 = Frame(root)
f2 = Frame(root)
f3 = Frame(root)
f4 = Frame(root)
f5 = Frame(root)

# Place the frame with a grid method
for frame in (f1, f2, f3, f4, f5):
    frame.grid(row=0, column=0, sticky='news')

# ------------- MAIN FRAME WINDOW -------------

# LabelFrame "My Plant" to group all my Button
myButtons=LabelFrame(f1, text="My Plants", padx=5, pady=5)

# Four buttons to access plants graph
one = Button(myButtons, text="PLANT 1", command=lambda:raise_frame(f2))
two = Button(myButtons, text="PLANT 2", command=lambda:raise_frame(f3))
three = Button(myButtons, text="PLANT 3", command=lambda:raise_frame(f4))
four = Button(myButtons, text="PLANT 4", command=lambda:raise_frame(f5))

f1.grid(column=0, row=0, sticky="nsew")
myButtons.grid(column=0, row=0, sticky="nsew")

one.grid(column=0, row=0, columnspan=1, sticky="nsew")
two.grid(column=1, row=0, columnspan=1, sticky="nsew")
three.grid(column=0, row=1, columnspan=1, sticky="nsew")
four.grid(column=1, row=1, columnspan=1, sticky="nsew")

# Configure the weight to allow the content to expand with the window
root.grid_rowconfigure(0,weight=1)
root.grid_columnconfigure(0,weight=1)

f1.grid_rowconfigure(0, weight=1)
f1.grid_columnconfigure(0, weight=1)

myButtons.grid_rowconfigure(0, weight=1)
myButtons.grid_rowconfigure(1, weight=1)
myButtons.grid_columnconfigure(0, weight=1)
myButtons.grid_columnconfigure(1, weight=1)

# ------------- PLANT FRAME WINDOW -------------

graph = Canvas(f2, bg='ivory')

back = Button(f2, text="<-", command=lambda:raise_frame(f1))
chose = Button(f2, text="Chose Plant", command=lambda:raise_frame(f3))
current = Button(f2, text="Current Plant : ")
temp = Button(f2, text="Temperature")
hum = Button(f2, text="Humidity")
lum = Button(f2, text="Luminosity")

back.grid(column=0, row=0, columnspan=1, sticky="news", padx=5, pady=5)
chose.grid(column=0, row=2, columnspan=2, sticky="news", padx=5, pady=5)
temp.grid(column=1, row=3, columnspan=1, sticky="news", padx=5, pady=5)
hum.grid(column=1, row=4, columnspan=1, sticky="news", padx=5, pady=5)
lum.grid(column=1, row=5, columnspan=1, sticky="news", padx=5, pady=5)
current.grid(column=2, row=0, columnspan=2, sticky="news", padx=5, pady=5)
graph.grid(column=2, row=2, columnspan=2, rowspan=4, sticky="news", padx=5, pady=5)

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

f2.grid_rowconfigure(0, weight=1)
f2.grid_rowconfigure(1, weight=1)
f2.grid_rowconfigure(2, weight=1)
f2.grid_rowconfigure(3, weight=1)
f2.grid_rowconfigure(4, weight=1)
f2.grid_rowconfigure(5, weight=1)

f2.grid_columnconfigure(0, weight=1)
f2.grid_columnconfigure(1, weight=1)
f2.grid_columnconfigure(2, weight=1)
f2.grid_columnconfigure(3, weight=1)
f2.grid_columnconfigure(4, weight=1)

# ------------- CHOSE PLANT WINDOW -------------

listeOfPlant = Canvas(f3, bg='ivory')

back = Button(f3, text="<-", command=lambda:raise_frame(f2))
confirm = Button(f3, text="Confirm", command=lambda:raise_frame(f2))

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


raise_frame(f1)
root.mainloop()
