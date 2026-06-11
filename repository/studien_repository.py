from abc import ABC, abstractmethod
from model.studiengang import Studiengang


# Definiert die Schnittstelle zum Laden und Speichern von Studiendaten.
class StudienRepository(ABC):

    # Lädt einen Studiengang aus der Datenquelle.
    @abstractmethod
    def lade_studiengang(self) -> Studiengang:
        pass

    # Speichert einen Studiengang in der Datenquelle.
    @abstractmethod
    def speichere_studiengang(self, studiengang: Studiengang) -> None:
        pass