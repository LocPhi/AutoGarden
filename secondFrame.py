from tkinter import *

def raise_frame(frame):
    frame.tkraise()

# Main Window
root = Tk()
root.geometry('800x480')

fe = Frame(root)
fe.grid(row=0, column=0, sticky='news')

graph = Canvas(fe, bg='ivory')

back = Button(fe, text="<-")
chose = Button(fe, text="Chose Plant")
current = Button(fe, text="Current Plant : ")
temp = Button(fe, text="Temperature")
hum = Button(fe, text="Humidity")
lum = Button(fe, text="Luminosity")

back.grid(column=0, row=0, columnspan=1, sticky="news", padx=5, pady=5)
chose.grid(column=0, row=2, columnspan=2, sticky="news", padx=5, pady=5)
temp.grid(column=1, row=3, columnspan=1, sticky="news", padx=5, pady=5)
hum.grid(column=1, row=4, columnspan=1, sticky="news", padx=5, pady=5)
lum.grid(column=1, row=5, columnspan=1, sticky="news", padx=5, pady=5)
current.grid(column=2, row=0, columnspan=2, sticky="news", padx=5, pady=5)
graph.grid(column=2, row=2, columnspan=2, rowspan=4, sticky="news", padx=5, pady=5)

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

fe.grid_rowconfigure(0, weight=1)
fe.grid_rowconfigure(1, weight=1)
fe.grid_rowconfigure(2, weight=1)
fe.grid_rowconfigure(3, weight=1)
fe.grid_rowconfigure(4, weight=1)
fe.grid_rowconfigure(5, weight=1)

fe.grid_columnconfigure(0, weight=1)
fe.grid_columnconfigure(1, weight=1)
fe.grid_columnconfigure(2, weight=1)
fe.grid_columnconfigure(3, weight=1)
fe.grid_columnconfigure(4, weight=1)

root.mainloop()