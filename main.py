import tkinter as tk
from interface import Interface

if __name__ == "__main__":
    root = tk.Tk()
    app = Interface(master=root)
    root.mainloop()
