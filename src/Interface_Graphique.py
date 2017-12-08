#!/usr/bin/env python3

# ------- Grenoble INP - ESISAR -------
# -- PX504 : AutoGarden ---
# ---- Author : Loc Phi ----
# -- Date : 08/12/2017 --

from tkinter import *
from PlantsDict import PlantsDict
from Plant import Plant
from Records import *
import datetime
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import matplotlib.dates as mdates

matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
from threading import RLock

my_font = "{courier new} 25"

root = Tk()

root.geometry('800x480')

# All the frame that depend on the main window
f1 = Frame(root)
f2 = Frame(root)
f3 = Frame(root)
f4 = Frame(root)
f5 = Frame(root)
f6 = Frame(root)
f7 = Frame(root)
f8 = Frame(root)
f9 = Frame(root)

graph = Canvas(f2)
graph2 = Canvas(f4)
graph3 = Canvas(f6)
graph4 = Canvas(f8)

a = PlantsDict()


def confirmPlant(listeOfPlant, frame):
    selection = listeOfPlant.curselection()
    if (selection):
        nameOfPlant = listeOfPlant.get(selection[0])
        selectedPlant = a.findPlant(nameOfPlant)
        if frame == f3:
            potListe[0].currentPlant = selectedPlant
            raise_frame(frame, f2)
        elif frame == f5:
            potListe[1].currentPlant = selectedPlant
            raise_frame(frame, f4)
        elif frame == f7:
            potListe[2].currentPlant = selectedPlant
            raise_frame(frame, f6)
        elif frame == f9:
            potListe[3].currentPlant = selectedPlant
            raise_frame(frame, f8)


def plothum(pot, masterFrame):
    fig = Figure(figsize=(6, 4), dpi=102)
    ax = fig.add_subplot(111)
    rec = Records()
    with lock:
        rec.loadFromFile(pot.pathToFile)
    humidity = []
    date = []
    for time, releve in rec.records.items():
        humidity.append(releve.humidity)
        date.append(time)
    ax.plot(date, humidity, "o")
    ax.set_ylim(0, 100)
    fig.autofmt_xdate()
    myFmt = mdates.DateFormatter('%D')
    ax.xaxis.set_major_formatter(myFmt)
    ax.set_title("Mesure d'humidite sur la plante")
    ax.set_xlabel("date")
    ax.set_ylabel("humidité")
    graphique = FigureCanvasTkAgg(fig, master=masterFrame)
    canvas = graphique.get_tk_widget()
    canvas.grid(row=0, column=0)
    fig.tight_layout()


def plottemp(pot, masterFrame):
    print(pot.currentPlant)
    fig = Figure(figsize=(6, 4), dpi=102)
    ax = fig.add_subplot(111)
    rec = Records()
    with lock:
        rec.loadFromFile(pot.pathToFile)
    temperature = []
    date = []
    for time, releve in rec.records.items():
        temperature.append(releve.temperature)
        date.append(time)
    ax.plot(date, temperature, "o")
    ax.set_ylim(10, 50)
    fig.autofmt_xdate()
    myFmt = mdates.DateFormatter('%D')
    ax.xaxis.set_major_formatter(myFmt)
    ax.set_title("Mesure de temperature sur la plante")
    ax.set_xlabel("date")
    ax.set_ylabel("temperature")
    graphique = FigureCanvasTkAgg(fig, master=masterFrame)
    canvas = graphique.get_tk_widget()
    canvas.grid(row=0, column=0)
    fig.tight_layout()


def plotlum(pot, masterFrame):
    fig = Figure(figsize=(6, 4), dpi=102)
    ax = fig.add_subplot(111)
    rec = Records()
    with lock:
        rec.loadFromFile(pot.pathToFile)
    luminosity = []
    date = []
    for time, releve in rec.records.items():
        luminosity.append(releve.luminosity)
        date.append(time)
    ax.plot(date, luminosity, "o")
    ax.set_ylim(0, 100)
    fig.autofmt_xdate()
    myFmt = mdates.DateFormatter('%D')
    ax.xaxis.set_major_formatter(myFmt)
    ax.set_title("Mesure de luminosité dans la pièce")
    ax.set_xlabel("date")
    ax.set_ylabel("luminosité")
    graphique = FigureCanvasTkAgg(fig, master=masterFrame)
    canvas = graphique.get_tk_widget()
    canvas.grid(row=0, column=0)
    fig.tight_layout()


def raise_frame(frameFrom, frameTo):
    if frameTo in (f2, f4, f6, f8):
        frameTo = create_graph_frame(frameTo)
    if frameTo in (f3, f5, f7, f9):
        frameTo = create_chose_frame(frameTo)
    frameTo.tkraise()


def create_graph_frame(frameToCreate):
    back = Button(frameToCreate, text="<-", command=lambda: raise_frame(frameToCreate, f1))
    if frameToCreate == f2:
        numFrame = 0
        chose = Button(frameToCreate, text="Chose Plant", command=lambda: raise_frame(frameToCreate, f3))
        temp = Button(frameToCreate, text="Temperature", command=lambda: plottemp(potListe[numFrame], graph))
        hum = Button(frameToCreate, text="Humidity", command=lambda: plothum(potListe[numFrame], graph))
        lum = Button(frameToCreate, text="Luminosity", command=lambda: plotlum(potListe[numFrame], graph))
        if potListe[0].currentPlant is None:
            current = Button(f2, text="Current Plant : None")
        else:
            current = Button(f2, text="Current Plant : {}".format(potListe[numFrame].currentPlant.name))
    elif frameToCreate == f4:
        numFrame = 1
        chose = Button(frameToCreate, text="Chose Plant", command=lambda: raise_frame(frameToCreate, f5))
        temp = Button(frameToCreate, text="Temperature", command=lambda: plottemp(potListe[numFrame], graph2))
        hum = Button(frameToCreate, text="Humidity", command=lambda: plothum(potListe[numFrame], graph2))
        lum = Button(frameToCreate, text="Luminosity", command=lambda: plotlum(potListe[numFrame], graph2))
        if potListe[1].currentPlant is None:
            current = Button(f4, text="Current Plant : None")
        else:
            current = Button(f4, text="Current Plant : {}".format(potListe[numFrame].currentPlant.name))
    elif frameToCreate == f6:
        numFrame = 2
        chose = Button(frameToCreate, text="Chose Plant", command=lambda: raise_frame(frameToCreate, f7))
        temp = Button(frameToCreate, text="Temperature", command=lambda: plottemp(potListe[numFrame], graph3))
        hum = Button(frameToCreate, text="Humidity", command=lambda: plothum(potListe[numFrame], graph3))
        lum = Button(frameToCreate, text="Luminosity", command=lambda: plotlum(potListe[numFrame], graph3))
        if potListe[2].currentPlant is None:
            current = Button(f6, text="Current Plant : None")
        else:
            current = Button(f6, text="Current Plant : {}".format(potListe[numFrame].currentPlant.name))
    elif frameToCreate == f8:
        numFrame = 3
        chose = Button(frameToCreate, text="Chose Plant", command=lambda: raise_frame(frameToCreate, f9))
        temp = Button(frameToCreate, text="Temperature", command=lambda: plottemp(potListe[numFrame], graph4))
        hum = Button(frameToCreate, text="Humidity", command=lambda: plothum(potListe[numFrame], graph4))
        lum = Button(frameToCreate, text="Luminosity", command=lambda: plotlum(potListe[numFrame], graph4))
        if potListe[3].currentPlant is None:
            current = Button(f8, text="Current Plant : None")
        else:
            current = Button(f8, text="Current Plant : {}".format(potListe[numFrame].currentPlant.name))

    back.grid(column=0, row=0, columnspan=1, sticky="news", padx=5, pady=5)
    chose.grid(column=0, row=2, columnspan=2, sticky="news", padx=5, pady=5)
    temp.grid(column=1, row=3, columnspan=1, sticky="news", padx=5, pady=5)
    hum.grid(column=1, row=4, columnspan=1, sticky="news", padx=5, pady=5)
    lum.grid(column=1, row=5, columnspan=1, sticky="news", padx=5, pady=5)
    current.grid(column=2, row=0, columnspan=2, sticky="news", padx=5, pady=5)

    if frameToCreate == f2:
        graph.grid(column=2, row=2, columnspan=2, rowspan=4, sticky="news", padx=5, pady=5)
    elif frameToCreate == f4:
        graph2.grid(column=2, row=2, columnspan=2, rowspan=4, sticky="news", padx=5, pady=5)
    elif frameToCreate == f6:
        graph3.grid(column=2, row=2, columnspan=2, rowspan=4, sticky="news", padx=5, pady=5)
    elif frameToCreate == f8:
        graph4.grid(column=2, row=2, columnspan=2, rowspan=4, sticky="news", padx=5, pady=5)

    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)

    frameToCreate.grid_rowconfigure(0, weight=1)
    frameToCreate.grid_rowconfigure(1, weight=1)
    frameToCreate.grid_rowconfigure(2, weight=1)
    frameToCreate.grid_rowconfigure(3, weight=1)
    frameToCreate.grid_rowconfigure(4, weight=1)
    frameToCreate.grid_rowconfigure(5, weight=1)

    frameToCreate.grid_columnconfigure(0, weight=1)
    frameToCreate.grid_columnconfigure(1, weight=1)
    frameToCreate.grid_columnconfigure(2, weight=1)
    frameToCreate.grid_columnconfigure(3, weight=1)
    frameToCreate.grid_columnconfigure(4, weight=1)

    return frameToCreate


def create_chose_frame(frameToCreate):
    # Create 4 plant for the list

    a.loadPlantsFromFile()

    # Window configuration

    if frameToCreate == f3:
        back = Button(f3, text="<-", command=lambda: raise_frame(frameToCreate, f2))
        confirm = Button(f3, text="Confirm", command=lambda: confirmPlant(listeOfPlant, f3))
        listeOfPlant = Listbox(f3, bg='ivory', height=4, font=my_font)
    elif frameToCreate == f5:
        back = Button(f5, text="<-", command=lambda: raise_frame(frameToCreate, f4))
        confirm = Button(f5, text="Confirm", command=lambda: confirmPlant(listeOfPlant, f5))
        listeOfPlant = Listbox(f5, bg='ivory', height=4, font=my_font)
    elif frameToCreate == f7:
        back = Button(f7, text="<-", command=lambda: raise_frame(frameToCreate, f6))
        confirm = Button(f7, text="Confirm", command=lambda: confirmPlant(listeOfPlant, f7))
        listeOfPlant = Listbox(f7, bg='ivory', height=4, font=my_font)
    elif frameToCreate == f9:
        back = Button(f9, text="<-", command=lambda: raise_frame(frameToCreate, f8))
        confirm = Button(f9, text="Confirm", command=lambda: confirmPlant(listeOfPlant, f9))
        listeOfPlant = Listbox(f9, bg='ivory', height=4, font=my_font)

    listeOfPlant.insert(END, "No Plants")

    for p in a.plants:
        listeOfPlant.insert(END, p)

    back.grid(column=0, row=0, columnspan=1, sticky="news", padx=5, pady=5)
    confirm.grid(column=0, row=3, columnspan=2, sticky="news", padx=5, pady=5)
    listeOfPlant.grid(column=2, row=0, columnspan=3, rowspan=4, sticky="news", padx=5, pady=5)

    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)

    frameToCreate.grid_rowconfigure(0, weight=1)
    frameToCreate.grid_rowconfigure(1, weight=1)
    frameToCreate.grid_rowconfigure(2, weight=1)
    frameToCreate.grid_rowconfigure(3, weight=1)
    frameToCreate.grid_rowconfigure(4, weight=1)
    frameToCreate.grid_rowconfigure(5, weight=1)

    frameToCreate.grid_columnconfigure(0, weight=1)
    frameToCreate.grid_columnconfigure(1, weight=1)
    frameToCreate.grid_columnconfigure(2, weight=1)
    frameToCreate.grid_columnconfigure(3, weight=1)
    frameToCreate.grid_columnconfigure(4, weight=1)

    return frameToCreate


def main(rlock, Liste):
    global potListe
    global lock
    lock = rlock
    potListe = Liste

    # Place the frame with a grid method
    for frame in (f1, f2, f3, f4, f5, f6, f7, f8, f9):
        frame.grid(row=0, column=0, sticky='news')

    # ------------- MAIN FRAME WINDOW -------------

    # LabelFrame "My Plant" to group all my Button
    myButtons = LabelFrame(f1, text="My Plants", padx=5, pady=5)

    # Four buttons to access plants graph
    one = Button(myButtons, text="PLANT 1", command=lambda: raise_frame(f1, f2))
    two = Button(myButtons, text="PLANT 2", command=lambda: raise_frame(f1, f4))
    three = Button(myButtons, text="PLANT 3", command=lambda: raise_frame(f1, f6))
    four = Button(myButtons, text="PLANT 4", command=lambda: raise_frame(f1, f8))

    f1.grid(column=0, row=0, sticky="nsew")
    myButtons.grid(column=0, row=0, sticky="nsew")

    one.grid(column=0, row=0, columnspan=1, sticky="nsew")
    two.grid(column=1, row=0, columnspan=1, sticky="nsew")
    three.grid(column=0, row=1, columnspan=1, sticky="nsew")
    four.grid(column=1, row=1, columnspan=1, sticky="nsew")

    # Configure the weight to allow the content to expand with the window
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)

    f1.grid_rowconfigure(0, weight=1)
    f1.grid_columnconfigure(0, weight=1)

    myButtons.grid_rowconfigure(0, weight=1)
    myButtons.grid_rowconfigure(1, weight=1)
    myButtons.grid_columnconfigure(0, weight=1)
    myButtons.grid_columnconfigure(1, weight=1)

    # ------------- PLANT FRAME WINDOW -------------


    # ------------- CHOSE PLANT WINDOW -------------


    f1.tkraise()
    root.mainloop()