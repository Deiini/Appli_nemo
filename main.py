import tkinter as tk
import interface_achat

# Création de la fenêtre principale
class MainInterface:
    def __init__(self, master):
        self.master = master
        self.master.title("Application de gestion de stock")
        self.master.geometry("900x600")
        self.frame = tk.Frame(self.master)
        self.frame.pack()
        # Bouton achat
        self.button_achat = tk.Button(self.frame, text="Achat", command=self.ouvrir_interface_achat)
        self.button_achat.pack(side=tk.LEFT)
        # Bouton vente
        self.bouton_vente = tk.Button(self.frame, text="Vente")
        self.bouton_vente.pack(side=tk.RIGHT)

    def ouvrir_interface_achat(self):

        interface_achat_window = tk.Toplevel(self.master)
        interface_achat.InterfaceAchat(interface_achat_window)


if __name__ == "__main__":
    root = tk.Tk()
    app = MainInterface(master=root)
    root.mainloop()
