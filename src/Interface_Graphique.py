#!/usr/bin/env python3

# ------- Grenoble INP - ESISAR -------
# -- PX504 : AutoGarden ---
# ---- Author : Loc Phi ----
# -- Date : 13/10/2017 --

from tkinter import *
from PlantsDict import PlantsDict
from Plant import Plant
from Records import *

import datetime
import numpy as np
import matplotlib.pyplot as plt

import matplotlib

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

graph = Canvas(f2)


def plothum(rlock):
    fig = Figure(figsize=(6, 4), dpi=102)
    ax = fig.add_subplot(111)
    rec = Records()
    # with verrou
    rec.loadFromFile("../data/pot1")
    humidity = []
    date = []
    for time, releve in rec.records.items():
        humidity.append(releve.humidity)
        date.append(time)
    print(humidity)
    print(date)
    print(len(date))
    print(len(humidity))
    ax.plot(date, humidity, "o")
    ax.set_ylim(0,100)
    # ax.gcf().autofmt_xdate()
    # myFmt = mdates.DateFormatter('%H:%M')
    # plt.gca().xaxis.set_major_formatter(myFmt)
    ax.set_title("Mesure d'humidite sur la plante")
    ax.set_xlabel("date")
    ax.set_ylabel("humidité")
    graphique = FigureCanvasTkAgg(fig, master=graph)
    canvas = graphique.get_tk_widget()
    canvas.grid(row=0, column=0)
    fig.tight_layout()


def plottemp(rlock):
    fig = Figure(figsize=(6, 4), dpi=102)
    ax = fig.add_subplot(111)
    rec = Records()
    rec.loadFromFile("../data/pot1")
    temperature = []
    date = []
    for time, releve in rec.records.items():
        temperature.append(releve.temperature)
        date.append(time)
    print(temperature)
    print(date)
    print(len(date))
    print(len(temperature))
    ax.plot(date, temperature, "o")
    ax.set_ylim(10,50)
    # ax.gcf().autofmt_xdate()
    # myFmt = mdates.DateFormatter('%H:%M')
    # plt.gca().xaxis.set_major_formatter(myFmt)
    ax.set_title("Mesure de temperature sur la plante")
    ax.set_xlabel("date")
    ax.set_ylabel("temperature")
    graphique = FigureCanvasTkAgg(fig, master=graph)
    canvas = graphique.get_tk_widget()
    canvas.grid(row=0, column=0)
    fig.tight_layout()


def plotlum(rlock):
    fig = Figure(figsize=(6, 4), dpi=102)
    ax = fig.add_subplot(111)
    rec = Records()
    rec.loadFromFile("../data/pot1")
    luminosity = []
    date = []
    for time, releve in rec.records.items():
        luminosity.append(releve.luminosity)
        date.append(time)
    print(luminosity)
    print(date)
    print(len(date))
    print(len(luminosity))
    ax.plot(date, luminosity, "o")
    ax.set_ylim(0,100)
    # ax.gcf().autofmt_xdate()
    # myFmt = mdates.DateFormatter('%H:%M')
    # plt.gca().xaxis.set_major_formatter(myFmt)
    ax.set_title("Mesure de luminosité dans la pièce")
    ax.set_xlabel("date")
    ax.set_ylabel("luminosité")
    graphique = FigureCanvasTkAgg(fig, master=graph)
    canvas = graphique.get_tk_widget()
    canvas.grid(row=0, column=0)
    fig.tight_layout()


def raise_frame(frame):
    frame.tkraise()


def main(rlock):

    # Place the frame with a grid method
    for frame in (f1, f2, f3, f4, f5):
        frame.grid(row=0, column=0, sticky='news')

    # ------------- MAIN FRAME WINDOW -------------

    # LabelFrame "My Plant" to group all my Button
    myButtons = LabelFrame(f1, text="My Plants", padx=5, pady=5)

    # Four buttons to access plants graph
    one = Button(myButtons, text="PLANT 1", command=lambda: raise_frame(f2))
    two = Button(myButtons, text="PLANT 2", command=lambda: raise_frame(f3))
    three = Button(myButtons, text="PLANT 3", command=lambda: raise_frame(f4))
    four = Button(myButtons, text="PLANT 4", command=lambda: raise_frame(f5))

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

    # graph = Canvas(f2)

    back = Button(f2, text="<-", command=lambda: raise_frame(f1))
    chose = Button(f2, text="Chose Plant", command=lambda: raise_frame(f3))
    current = Button(f2, text="Current Plant : ")
    temp = Button(f2, text="Temperature", command=lambda: plottemp(rlock))
    hum = Button(f2, text="Humidity", command=lambda: plothum(rlock))
    lum = Button(f2, text="Luminosity", command=lambda: plotlum(rlock))

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

    # Create 4 plant for the list
    a = PlantsDict()
    a.loadPlantsFromFile()

    plant1 = Plant('Menthe', 10.0, 10, 10)
    plant2 = Plant('Coriandre', 10.0, 10, 10)
    plant3 = Plant('Radis', 10.0, 10, 10)
    plant4 = Plant('Carotte', 10.0, 10, 10)

    a.addPlant(plant1)
    a.addPlant(plant2)
    a.addPlant(plant3)
    a.addPlant(plant4)
    a.saveInFile()
    print(a.plants)

    # Window configuration
    # listeOfPlant = Canvas(f3, bg='ivory')

    listeOfPlant = Listbox(f3, bg='ivory', height=4, font=my_font)
    listeOfPlant.insert(END, plant1.name)
    listeOfPlant.insert(END, plant2.name)
    listeOfPlant.insert(END, plant3.name)
    listeOfPlant.insert(END, plant4.name)

    back = Button(f3, text="<-", command=lambda: raise_frame(f2))
    confirm = Button(f3, text="Confirm", command=lambda: raise_frame(f2))

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

# For testing

#blabla = RLock()

#main(blabla)