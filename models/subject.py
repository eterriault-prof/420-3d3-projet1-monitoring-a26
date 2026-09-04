from abc import ABC, abstractmethod

class Sujet(ABC):

    def __init__(self):
        self._observateurs = []

    def abonner(self, observateur) -> None:
        self._observateurs.append(observateur)

    def desabonner(self, observateur) -> None:
        self._observateurs.remove(observateur)

    def notifier(self) -> None:
        # À compléter — quelle méthode appelle-t-on sur chaque observateur ?
        for o in self._observateurs:
            o.actualiser(self)

    @abstractmethod
    def get_donnees(self) -> dict:
        pass