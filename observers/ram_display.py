import tkinter as tk
from observers.observer import Observateur

class AffichageRam(Observateur):

    def __init__(self, parent: tk.Frame):
        self.frame_ram = tk.LabelFrame(parent, text="ram", padx=10, pady=10)
        self.frame_ram.pack(fill=tk.X, padx=10, pady=5)
        self.label_ram = tk.Label(self.frame_ram, text="0%", font=("Arial", 24, "bold"))
        self.label_ram.pack()
        self.canvas_ram = tk.Canvas(self.frame_ram, width=300, height=20, bg="white")
        self.canvas_ram.pack()
        self.label_80_ram = tk.Label(self.frame_ram, text = "avertissement 80%!", font=("arial", 12, "bold"))
        self.label_80_ram.pack()
        
    def actualiser(self, sujet) -> None:
        donnees = sujet.get_donnees()
        valeur = donnees["ram"]
        self.label_80_ram.config(text=f"{valeur:.1f}%")
        self._dessiner_barre(valeur)

    def _dessiner_barre(self, valeur: float) -> None:
        self.canvas_ram.delete("all")

        largeur = 300 * valeur / 100

        if valeur < 50:
            couleur = "green"
        elif valeur < 80:
            couleur = "orange"
        else:
            couleur = "red"
        self.canvas_ram.create_rectangle(0, 0, largeur, 20, fill=couleur, outline="")
            