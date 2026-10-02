import tkinter as tk
from observers.observer import Observateur

class AffichageCPU(Observateur):

    def __init__(self, parent: tk.Frame):
        # À compléter: Créez un LabelFrame "CPU", un Label pour le pourcentage et un Canvas pour la barre de progression
        self.frame_cpu = tk.LabelFrame(parent, text="CPU", padx=10, pady=10)
        self.frame_cpu.pack(fill=tk.X, padx=10, pady=5)
        self.label_cpu = tk.Label(self.frame_cpu, text="0%", font=("Arial", 24, "bold"))
        self.label_cpu.pack()
        self.canvas_cpu = tk.Canvas(self.frame_cpu, width=300, height=20, bg="white")
        self.canvas_cpu.pack()
        
        self.label_cpu_80 = tk.Label(self.frame_cpu, text="", font=("Arial", 10))
        self.label_cpu_80.pack()
        
        self.label_cpu_grand = tk.Label(self.frame_cpu, text="", font=("Arial", 24, "bold"))
        self.label_cpu_grand.pack(padx=20, pady=20)


    def actualiser(self, sujet) -> None:
        # À compléter: Récupérez la valeur CPU depuis sujet.get_donnees()
        donnees_metriques = sujet.get_donnees()
        donnees_cpu = donnees_metriques['cpu']

        # À compléter: Mettez à jour le label et la barre
        self.label_cpu.config(text=f"{donnees_cpu}%")
        self._dessiner_barre(donnees_cpu)

    def _dessiner_barre(self, valeur: float) -> None:
        # À compléter: 
        # Effacez le canvas
        # Calculez la largeur (300 * valeur / 100)
        # Choisissez la couleur : vert < 50%, orange < 80%, rouge sinon
        # Dessinez le rectangle
        self.canvas_cpu.delete("all")
        largeur_cpu = int(300 * valeur / 100)
        if valeur < 50:
            couleur_cpu = "green"
        elif valeur < 80:
            couleur_cpu = "orange"
        else:
            couleur_cpu = "red"
        self.canvas_cpu.create_rectangle(0, 0, largeur_cpu, 20, fill=couleur_cpu, outline="")