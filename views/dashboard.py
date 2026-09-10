import tkinter as tk
from models.metrics import MetriquesSysteme
from observers.cpu_display import AffichageCPU
from observers.ram_display import AffichageRAM
from observers.disk_display import AffichageDisque
from observers.logger import Logger  # Modifiez en LoggerFichier si c'est le nom dans votre fichier
 
class Dashboard(tk.Tk):
 
    INTERVALLE_MS = 2000
 
    def __init__(self, metriques: MetriquesSysteme):
        super().__init__()
        self.title("Monitoring système")
        self._metriques = metriques
 
        # 1. Création des observateurs
        self._creer_observateurs()

        # 2. Abonnement au sujet
        self._abonner_observateurs()

        # 3. Démarrage du rafraîchissement automatique
        self._rafraichir()
 
    def _creer_observateurs(self) -> None:
        self.cpu = AffichageCPU(self)
        self.ram = AffichageRAM(self)
        self.disk = AffichageDisque(self)
        self.logger = Logger()
 
    def _abonner_observateurs(self) -> None:
        self._metriques.abonner(self.cpu)
        self._metriques.abonner(self.ram)
        self._metriques.abonner(self.disk)
        self._metriques.abonner(self.logger)
 
    def _rafraichir(self) -> None:
        self._metriques.actualiser_metriques()
        self.after(self.INTERVALLE_MS, self._rafraichir)
