import tkinter as tk
from tkinter.ttk import Treeview
from database import connect


class InterfaceAchat:
    def __init__(self, master):
        self.master = master
        self.master.title("Interface d'Achat")
        self.master.geometry("900x600")

        self.tableau = Treeview(self.master, columns=("Nom", "Quantité", "Prix", "Total"))
        self.tableau.heading("Nom", text="Nom")
        self.tableau.heading("Quantité", text="Quantité")
        self.tableau.heading("Prix", text="Prix")
        self.tableau.heading("Total", text="Total")
        self.tableau['show'] = 'headings'
        self.tableau.pack()

        self.formulaire = tk.Frame(self.master)
        self.formulaire.pack()

        self.nom_label = tk.Label(self.formulaire, text="Nom de la matière première :")
        self.nom_label.grid(row=0, column=0)
        self.nom_entry = tk.Entry(self.formulaire)
        self.nom_entry.grid(row=0, column=1)

        self.quantite_label = tk.Label(self.formulaire, text="Quantité de la matière première :")
        self.quantite_label.grid(row=1, column=0)
        self.quantite_entry = tk.Entry(self.formulaire)
        self.quantite_entry.grid(row=1, column=1)

        self.prix_label = tk.Label(self.formulaire, text="Prix de la matière première :")
        self.prix_label.grid(row=2, column=0)
        self.prix_entry = tk.Entry(self.formulaire)
        self.prix_entry.grid(row=2, column=1)



        self.enregistrer = tk.Button(self.formulaire, text="Enregistrer", command=self.enregistrer_achat)
        self.enregistrer.grid(row=4, column=0)

        self.afficher_donnees()

    def enregistrer_achat(self):
        matiere_premieres = self.nom_entry.get()
        quantite = self.quantite_entry.get()
        prix = self.prix_entry.get()

        connect.enregistrer_achat(matiere_premieres, quantite, prix)

        self.afficher_donnees()

    def afficher_donnees(self):
        self.tableau.delete(*self.tableau.get_children())

        rows = connect.consultation_database()
        for row in rows:
            self.tableau.insert("", "end", values=row)
