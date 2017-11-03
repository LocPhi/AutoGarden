from tkinter import *

fenetre = Tk()

champ_label = Label(fenetre, text = "test test test test test")
bouton_quitter = Button(fenetre, text ="Quitter", command=fenetre.quit)
var_choix = StringVar()
var_case = IntVar()

case = Checkbutton(fenetre, text="Ne plus poser cette question", variable=var_case)

choix_rouge = Radiobutton(fenetre, text="Rouge", variable=var_choix, value="rouge")
choix_vert = Radiobutton(fenetre, text="Vert", variable=var_choix, value="vert")
choix_bleu = Radiobutton(fenetre, text="Bleu", variable=var_choix, value="bleu")

choix_rouge.pack()
choix_vert.pack()
choix_bleu.pack()

champ_label.pack()
bouton_quitter.pack()

case.pack()

fenetre.mainloop()

