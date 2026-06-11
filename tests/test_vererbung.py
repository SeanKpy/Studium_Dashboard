from abc import ABC, abstractmethod
from enum import Enum


class ModulStatus(Enum):
    OFFEN = "offen"
    IN_BEARBEITUNG = "in Bearbeitung"
    ABGESCHLOSSEN = "abgeschlossen"


class Modul(ABC):
    def __init__(self, name, ects, status):
        self.name = name
        self.ects = ects
        self.status = status

    @abstractmethod
    def beschreibung(self):
        pass


class KursModul(Modul):
    def __init__(self, name, ects, status, kurscode):
        super().__init__(name, ects, status)
        self.kurscode = kurscode

    def beschreibung(self):
        return f"{self.name} ({self.kurscode})"


class BachelorModul(Modul):
    def __init__(self, name, ects, status, thema, abgabe_datum):
        super().__init__(name, ects, status)
        self.thema = thema
        self.abgabe_datum = abgabe_datum

    def beschreibung(self):
        return f"{self.name}: {self.thema}"


kurs = KursModul(
    "Objektorientierte Programmierung",
    5,
    ModulStatus.IN_BEARBEITUNG,
    "DLBDSOOFPP01"
)

bachelor = BachelorModul(
    "Bachelorarbeit",
    10,
    ModulStatus.OFFEN,
    "Studien-Dashboard mit Python",
    "2027-06-30"
)

print(kurs.beschreibung())
print(bachelor.beschreibung())