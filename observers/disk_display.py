import tkinter as tk
from observers.observer import Observateur

class AffichageDisk(Observateur):

    def __init__(self, parent: tk.Frame):
        self.frame_disk = tk.LabelFrame(parent, text="Disk", padx=10, pady=10)
        self.frame_disk.pack(fill=tk.X, padx=10, pady=5)
        self.label_disk = tk.Label(self.frame_disk, text="0%", font=("Arial", 24, "bold"))
        self.label_disk.pack()
        self.canvas_disk = tk.Canvas(self.frame_disk, width=300, height=20, bg="white")
        self.canvas_disk.pack()
        self.label_80_disk = tk.Label(self.frame_disk, text = "avertissement 80%!", font=("arial", 12, "bold"))
        self.label_80_disk.pack()
        
    def actualiser(self, sujet) -> None:
        donnees = sujet.get_donnees()
        valeur = donnees["disque"]
        self.label_80_disk.config(text=f"{valeur:.1f}%")
        self._dessiner_barre(valeur)





    def _dessiner_barre(self, valeur: float) -> None:
        self.canvas_disk.delete("all")

        largeur = 300 * valeur / 100

        if valeur < 50:
            couleur = "green"
        elif valeur < 80:
            couleur = "orange"
        else:
            couleur = "red"
        self.canvas_disk.create_rectangle(0, 0, largeur, 20, fill=couleur, outline="")
    