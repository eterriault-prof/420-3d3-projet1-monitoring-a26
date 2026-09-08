import tkinter as tk
from observers.observer import Observateur

class AffichageCPU(Observateur):

    def __init__(self, parent: tk.Frame):
        self.frame_cpu = tk.LabelFrame(parent, text="CPU", padx=10, pady=10)
        self.frame_cpu.pack(fill=tk.X, padx=10, pady=5)
        self.label_cpu = tk.Label(self.frame_cpu, text="0%", font=("Arial", 24, "bold"))
        self.label_cpu.pack()
        self.canvas_cpu = tk.Canvas(self.frame_cpu, width=300, height=20, bg="white")
        self.canvas_cpu.pack()
        self.label_80_cpu = tk.Label(self.frame_cpu, text = "avertissement 80%!", font=("arial", 12, "bold"))
        self.label_80_cpu.pack()
        
    def actualiser(self, sujet) -> None:
        donnees = sujet.get_donnees()
        valeur = donnees["cpu"]
        self.label_80_cpu.config(text=f"{valeur:.1f}%")
        self._dessiner_barre(valeur)





    def _dessiner_barre(self, valeur: float) -> None:
        self.canvas_cpu.delete("all")

        largeur = 300 * valeur / 100

        if valeur < 50:
            couleur = "green"
        elif valeur < 80:
            couleur = "orange"
        else:
            couleur = "red"
        self.canvas_cpu.create_rectangle(0, 0, largeur, 20, fill=couleur, outline="")
    
     