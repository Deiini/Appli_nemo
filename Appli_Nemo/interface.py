import tkinter as tk
from tkinter.ttk import Treeview


class Interface:
    def __init__(self, master):
        self.master = master
        self.title = master.title("Interface")
        self.master.geometry("900x600")
        self.frame = tk.Frame(self.master)
        self.frame.pack()
        self.bouton_achat = tk.Button(self.frame, text="Achat", command=self.achat)
        self.bouton_achat.pack(side=tk.LEFT)
        self.bouton_ventes = tk.Button(self.frame, text="Ventes", command=self.Ventes)
        self.bouton_ventes.pack(side=tk.LEFT)

    def achat(self):
        # Création d'un tableau pour enregistrer les achats
        tableau = Treeview(self.master, columns=("Nom", "Quantité", "Prix", "Total"))
        tableau.heading("Nom", text="Nom")
        tableau.heading("Quantité", text="Quantité")
        tableau.heading("Prix", text="Prix")
        tableau.heading("Total", text="Total")
        tableau['show'] = 'headings'
        tableau.pack()

        # Création d'un formulaire pour enregistrer les achats
        formulaire = tk.Frame(self.master)
        formulaire.pack()
        nom = tk.Label(formulaire, text="Nom de la matière première :")
        nom.grid(row=0, column=0)
        nom = tk.Entry(formulaire)
        nom.grid(row=0, column=1)
        quantite = tk.Label(formulaire, text="Quantité de la matière première :")
        quantite.grid(row=1, column=0)
        quantite = tk.Entry(formulaire)
        quantite.grid(row=1, column=1)
        prix = tk.Label(formulaire, text="Prix de la matière première :")
        prix.grid(row=2, column=0)
        prix = tk.Entry(formulaire)
        prix.grid(row=2, column=1)
        total = tk.Label(formulaire, text="Total de la matière première :")
        total.grid(row=3, column=0)
        total = tk.Entry(formulaire)
        total.grid(row=3, column=1)
        enregistrer = tk.Button(formulaire, text="Enregistrer")
        enregistrer.grid(row=4, column=0)
        quitter = tk.Button(formulaire, text="Quitter", command=self.master.quit)
        quitter.grid(row=4, column=1)

    def Ventes(self):
        print("Voici l'interface de vente")