from datetime import date

from model.modul import Modul
from model.enums import ModulStatus

# Repräsentiert die Bachelorarbeit.
class BachelorModul(Modul):

    def __init__(self,name: str,ects: int,status: ModulStatus,thema: str,abgabe_datum: date):
        super().__init__(name, ects, status)

        self.thema = thema
        self.abgabe_datum = abgabe_datum

    def beschreibung(self) -> str:
        return f"{self.name}: {self.thema}"