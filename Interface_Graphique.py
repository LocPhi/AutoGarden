# from tkinter import *
#
#
# class Interface(Frame):
#     """Notre fenêtre principale.
#     Tous les widgets sont stockés comme attributs de cette fenêtre."""
#
#     def __init__(self, fenetre, **kwargs):
#         Frame.__init__(self, fenetre, width=768, height=576, **kwargs)
#         self.pack(fill=BOTH)
#         self.nb_clic = 0
#
#         # Création de nos widgets
#         self.message = Label(self, text="Vous n'avez pas cliqué sur le bouton.")
#         self.message.pack()
#
#         self.bouton_quitter = Button(self, text="Quitter", command=self.quit)
#         self.bouton_quitter.pack(side="left")
#
#         self.bouton_cliquer = Button(self, text="Cliquez ici", fg="red",
#                                      command=self.cliquer)
#         self.bouton_cliquer.pack(side="right")
#
#     def cliquer(self):
#         """Il y a eu un clic sur le bouton.
#
#         On change la valeur du label message."""
#
#         self.nb_clic += 1
#         self.message["text"] = "Vous avez cliqué {} fois.".format(self.nb_clic)
#
# fenetre = Tk()
# interface = Interface(fenetre)
#
# interface.mainloop()
# interface.destroy()

# from tkinter import *
#
#
# def faireApparaitreLeToplevel():
#     top = Toplevel(root)
#     lab = Label(top, text="Ce soir je vais manger des frites")
#     lab.pack()
#
#
# root = Tk()
# go = Button(root, text="lancer", command=faireApparaitreLeToplevel)
# go.pack()
# root.mainloop()

# import tkinter as tk
#
# class Demo1:
#     def __init__(self, master):
#         self.master = master
#         self.frame = tk.Frame(self.master)
#         self.button1 = tk.Button(self.frame, text = 'New Window', width = 25, command = self.new_window)
#         self.button1.pack()
#         self.frame.pack()
#
#     def new_window(self):
#         self.newWindow = tk.Toplevel(self.master)
#         self.app = Demo2(self.newWindow)
#
# class Demo2:
#     def __init__(self, master):
#         self.master = master
#         self.frame = tk.Frame(self.master)
#         self.quitButton = tk.Button(self.frame, text = 'Quit', width = 25, command = self.close_windows)
#         self.quitButton.pack()
#         self.frame.pack()
#
#     def close_windows(self):
#         self.master.destroy()
#
# def main():
#     root = tk.Tk()
#     app = Demo1(root)
#     root.mainloop()
#
# if __name__ == '__main__':
#     main()

from tkinter import *

def raise_frame(frame):
    frame.tkraise()

root = Tk()

f1 = Frame(root)
f2 = Frame(root)
f3 = Frame(root)
f4 = Frame(root)

for frame in (f1, f2, f3, f4):
    frame.grid(row=0, column=0, sticky='news')


l = LabelFrame(f1, text="My plants", padx=200, pady=150)
l.pack(fill="both", expand="yes")

b1=Button(l, text='Go to frame 2', command=lambda:raise_frame(f2))
b1.pack()

b2 = Button(l, text='Go to frame 2', command=lambda:raise_frame(f2)).pack()
b3 = Button(l, text='Go to frame 2', command=lambda:raise_frame(f2)).pack()
b4 = Button(l, text='Go to frame 2', command=lambda:raise_frame(f2)).pack()


Label(f2, text='FRAME 2').pack()
Button(f2, text='Go to frame 3', command=lambda:raise_frame(f3)).pack()

Label(f3, text='FRAME 3').pack(side='left')
Button(f3, text='Go to frame 4', command=lambda:raise_frame(f4)).pack(side='left')

Label(f4, text='FRAME 4').pack()
Button(f4, text='Goto to frame 1', command=lambda:raise_frame(f1)).pack()

raise_frame(f1)
root.mainloop()
