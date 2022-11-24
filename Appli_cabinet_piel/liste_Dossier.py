import tkinter as tk
from tkinter import ttk

root = tk.Tk()


labelchoix = tk.Label(root, text="Veuillez choisir un type de dossier")  # Label pour le choix du partenaire
labelchoix.pack()

TypeDossier = ["LS1", "LS2", "SGAR"]

listeComboDossier = ttk.Combobox(root, values=TypeDossier)  # Création de la liste de choix des types de dossier disponibles
listeComboDossier.current(0)  # Choix par défaut du premier élément de la liste

listeComboDossier.pack()


root.mainloop()