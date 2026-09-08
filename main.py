from models.metrics import MetriquesSysteme
from observers.cpu_display import AffichageCPU
from observers.disk_display import AffichageDisk
from observers.ram_display import AffichageRam
import tkinter as tk

metriques = MetriquesSysteme()
root = tk.Tk()
cpu = AffichageCPU(root)
disk = AffichageDisk(root)
ram = AffichageRam(root)


metriques.abonner(cpu)
metriques.abonner(disk)
metriques.abonner(ram)


def rafraichir():
    metriques.actualiser_metriques()
    root.after(2000, rafraichir)

rafraichir()
root.mainloop()