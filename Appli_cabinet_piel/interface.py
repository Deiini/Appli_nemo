from importlib.resources import Package
from optparse import Values
from tkinter import *
from tkinter import ttk
import tkinter
from typing import List
from xml.dom import NoModificationAllowedErr



class App(tkinter.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("Super appli")
        self.geometry('500x500')
        # self.tk.eval("""
        # set base_theme_dir F:/projet/statElo/awthemes-10.4.0

        # package ifneeded awthemes 10.4.0 \
        #     [list source [file join $base_theme_dir awthemes.tcl]]
        # package ifneeded colorutils 4.8 \
        #     [list source [file join $base_theme_dir colorutils.tcl]]
        # package ifneeded awdark 7.12 \
        #     [list source [file join $base_theme_dir awdark.tcl]]
        # package ifneeded awbreezedark 1.0.1 \
        #     [list source [file join $base_theme_dir awbreezedark.tcl]]
        # package ifneeded awlight 7.6 \
        #     [list source [file join $base_theme_dir awlight.tcl]]
        # """)
        # self.tk.call("lappend", "auto_path", 'F:/projet/statElo/awthemes-10.4.0')
        # self.tk.call("package", "require", 'awdark')
        # self.tk.call("package", "require", 'awlight')
        # self.tk.call("package", "require", 'awbreezedark')
        self.style = ttk.Style(self)
        print(self.style.theme_names())
        # self.style.theme_use("awlight")
        self.tailleLabel = 25

            # Nom
            # Prenom
            # Dated de naissance
            # Propriétaire ou locataire
            # Trésorerie
            # Montant du pret
            # Honoraire
            # Pourcentage : calculer par l'appli
            # Département
            # Enseigne
            # Lieux
            # Financé ou pas

        # gestion des onglet
        ongletControl = ttk.Notebook(self)
        
        ongletSaisie = ttk.Frame(ongletControl)
        ongletStat = ttk.Frame(ongletControl)

        ongletControl.add(ongletSaisie, text ='Saisie client')
        ongletControl.add(ongletStat, text ='Statistique')
        ongletControl.pack(expand = 1, fill ="both")

        # Paned vertical principal
        saisie = PanedWindow(ongletSaisie, orient=VERTICAL)
        saisie.pack(side=TOP, expand=Y, fill=BOTH,pady=2,padx=2)

        # Paned de nom
        nom = PanedWindow(saisie, orient=HORIZONTAL,)
        nom.pack(side=TOP, expand=Y, fill=BOTH,pady=2,padx=2)
        saisie.add(nom)
        nom.add(ttk.Label(nom, text="Nom :", width=self.tailleLabel))
        valNom = Entry(nom)
        nom.add(valNom)

        # Paned de Prenom
        prenom = PanedWindow(saisie, orient=HORIZONTAL)
        prenom.pack(side=TOP, expand=Y, fill=BOTH,pady=2,padx=2)
        saisie.add(prenom)
        prenom.add(ttk.Label(prenom, text="Prénom :", width=self.tailleLabel))
        valPrenom = ttk.Entry(prenom)
        prenom.add(valPrenom)

        # Paned Date de naissance
        naissance = PanedWindow(saisie, orient=HORIZONTAL)
        naissance.pack(side=TOP, expand=Y, fill=BOTH,pady=2,padx=2)
        saisie.add(naissance)
        naissance.add(ttk.Label(naissance, text="Date de naissance :", width=self.tailleLabel))
        valNaissance = ttk.Entry(naissance)
        naissance.add(valNaissance)

        # Paned propriétaire ou locataire
        habitation = PanedWindow(saisie, orient=HORIZONTAL)
        habitation.pack(side=TOP, expand=Y, fill=BOTH,pady=2,padx=2)
        saisie.add(habitation)
        habitation.add(ttk.Label(habitation, text="Statue d'habitation :",width=self.tailleLabel))
        listeHabitation = ["Locataire","Propriétaire"]
        valHabitation = ttk.Combobox(habitation,values=listeHabitation)
        habitation.add(valHabitation)

        # Paned de Trésorerie
        tresorerie = PanedWindow(saisie, orient=HORIZONTAL)
        tresorerie.pack(side=TOP, expand=Y, fill=BOTH,pady=2,padx=2)
        saisie.add(tresorerie)
        tresorerie.add(ttk.Label(tresorerie, text="Trésorerie :",width=self.tailleLabel))
        valTresorerie = ttk.Entry(tresorerie)
        tresorerie.add(valTresorerie)

        # Paned de pret
        pret = PanedWindow(saisie, orient=HORIZONTAL)
        pret.pack(side=TOP, expand=Y, fill=BOTH,pady=2,padx=2)
        saisie.add(pret)
        pret.add(ttk.Label(pret, text="Prêt :",width=self.tailleLabel))
        valPret = ttk.Entry(pret)
        pret.add(valPret)

        # Paned de honoraire
        honoraire = PanedWindow(saisie, orient=HORIZONTAL)
        honoraire.pack(side=TOP, expand=Y, fill=BOTH,pady=2,padx=2)
        saisie.add(honoraire)
        honoraire.add(ttk.Label(honoraire, text="Honoraire :",width=self.tailleLabel))
        valHonoraire = ttk.Entry(honoraire)
        honoraire.add(valHonoraire)

        # Paned de pourcentage
        pourcentage = PanedWindow(saisie, orient=HORIZONTAL)
        pourcentage.pack(side=TOP, expand=Y, fill=BOTH,pady=2,padx=2)
        saisie.add(pourcentage)
        pourcentage.add(ttk.Label(pourcentage, text="Pourcentage :",width=self.tailleLabel))
        valPourcentage = ""
        pourcentage.add(ttk.Label(pourcentage, text=valPourcentage))

        # Paned departement
        departement = PanedWindow(saisie, orient=HORIZONTAL)
        departement.pack(side=TOP, expand=Y, fill=BOTH,pady=2,padx=2)
        saisie.add(departement)
        departement.add(ttk.Label(departement, text="Departement :",width=self.tailleLabel))
        listeDepartement = [14,50,61]
        valDepartement = ttk.Combobox(departement, values=listeDepartement)
        departement.add(valDepartement)

        # Paned enseigne
        enseigne = PanedWindow(saisie, orient=HORIZONTAL)
        enseigne.pack(side=TOP, expand=Y, fill=BOTH,pady=2,padx=2)
        saisie.add(enseigne)
        enseigne.add(ttk.Label(enseigne, text="Enseigne :", width=self.tailleLabel))
        listeEnseigne = ["CA","CIC","Autre"]
        valEnseigne = ttk.Combobox(enseigne, values=listeEnseigne)
        enseigne.add(valEnseigne)

        # Paned de lieux
        lieux = PanedWindow(saisie, orient=HORIZONTAL)
        lieux.pack(side=TOP, expand=Y, fill=BOTH,pady=2,padx=2)
        saisie.add(lieux)
        lieux.add(ttk.Label(lieux, text="Lieux :",width=self.tailleLabel))
        valLieux = ttk.Entry(lieux)
        lieux.add(valLieux)

        # Paned propriétaire ou locataire
        financement = PanedWindow(saisie, orient=HORIZONTAL)
        financement.pack(side=TOP, expand=Y, fill=BOTH,pady=2,padx=2)
        saisie.add(financement)
        financement.add(ttk.Label(financement, text="Statue du Financement :",width=self.tailleLabel))
        listeFinancement = ["Financé", "Non financé"]
        valFinancement = ttk.Combobox(financement, values=listeFinancement)
        financement.add(valFinancement)


        # Bouton de validation
        validate = PanedWindow(saisie, orient=HORIZONTAL)
        validate.pack(side=TOP, expand=Y, fill=BOTH,pady=2,padx=2)
        saisie.add(validate)
        validate.add(ttk.Button(saisie, text="Ajouter", command=self.quit))



if __name__ == "__main__":
    app = App()
    app.mainloop()