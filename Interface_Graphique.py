# ------- Grenoble INP - ESISAR -------
# -- PX504 : AutoGarden ---
# ---- Author : Loc Phi ----
# -- Date : 06/10/2017 --

from tkinter import *

def raise_frame(frame):
    frame.tkraise()

# Main Window
root = Tk()

# All the frame that depend on the main window
f1 = Frame(root)
f2 = Frame(root)
f3 = Frame(root)
f4 = Frame(root)
f5 = Frame(root)

# Place the frame with a grid method
for frame in (f1, f2, f3, f4, f5):
    frame.grid(row=0, column=0, sticky='news')

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

Label(f2, text='FRAME 2').pack()
Button(f2, text='Go to frame 3', command=lambda:raise_frame(f3)).pack()

Label(f3, text='FRAME 3').pack(side='left')
Button(f3, text='Go to frame 4', command=lambda:raise_frame(f4)).pack(side='left')

Label(f4, text='FRAME 4').pack()
Button(f4, text='Goto to frame 1', command=lambda:raise_frame(f1)).pack()

raise_frame(f1)
root.mainloop()
