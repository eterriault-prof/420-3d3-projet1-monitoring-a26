from abc import ABC

class Observateur(ABC):

    @abstractmethod
    def actualiser(self, sujet) -> None:
        pass 