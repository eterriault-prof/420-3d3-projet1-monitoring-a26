from datetime import datetime
from observers.observer import Observateur

class Logger(Observateur):
    def __init__(self, filename="log.txt"):
        self.filename = filename
        
    def actualiser(self, sujet):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        donnees = sujet.get_donnees()
        cpu = donnees.get('cpu', 0.0)
        ram = donnees.get('ram', 0.0)
        disk = donnees.get('disque', 0.0)
        
        log_entry = f"{timestamp} | CPU: {cpu:.1f}% | RAM: {ram:.1f}% | Disque: {disk:.1f}%\n"

        with open(self.filename, "a", encoding="utf-8") as file:
            file.write(log_entry)