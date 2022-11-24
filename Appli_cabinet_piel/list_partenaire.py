import tkinter as tk
from tkinter import ttk

root = tk.Tk()

labelchoix = tk.Label(root, text="Veuillez choisir un partenaire")  # Label pour le choix du partenaire
labelchoix.pack()

ListePartenaire = ["Crédit Agricole", "Crédit Mutuel", "LCL", "Caisse d'épargne", "Société Générale", "CIC", "BRED"]

listeComboPartenaire = ttk.Combobox(root, values=ListePartenaire)  # Création de la liste de choix des partenaires disponibles


listeComboPartenaire.current(0)  # Choix par défaut du premier élément de la liste

listeComboPartenaire.pack()
