from abc import ABC, abstractmethod

from model.enums import ModulStatus

"""
Abstrakte Basisklasse für alle Module.
"""
class Modul(ABC):
    def __init__(self,name: str,ects: int,status: ModulStatus):
        self.name = name
        self.ects = ects
        self.status = status
        self.pruefungsleistungen = []

    # Fügt dem Modul eine Prüfungsleistung hinzu.
    def pruefungsleistung_hinzufuegen(self, pruefungsleistung):
        self.pruefungsleistungen.append(pruefungsleistung)


    # Gibt eine Beschreibung des Moduls zurück.
    @abstractmethod
    def beschreibung(self) -> str:
        pass