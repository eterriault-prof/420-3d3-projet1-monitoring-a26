import psutil
from models.sujet import Sujet

class MetriquesSysteme(Sujet):

    def __init__(self):
        super().__init__() # Permet d'initialiser la liste des observateurs
        self._cpu = 0.0
        self._ram = 0.0
        self._disque = 0.0

    def actualiser_metriques(self) -> None:
        cpu = psutil.cpu_percent()
        ram = psutil.virtual_memory().percent
        disque = psutil.disk_usage("/").percent

        self.notifier()

    def get_donnees(self) -> dict:
        return {
           'cpu':  psutil.cpu_percent(),
           'ram': psutil.virtual_memory().percent,
           'disque': psutil.disk_usage("/").percent 
        }