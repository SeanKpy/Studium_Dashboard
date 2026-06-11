from model.modul import Modul
from model.enums import ModulStatus


# Repräsentiert ein reguläres Kursmodul.
class KursModul(Modul):

    def __init__(self,name: str,ects: int,status: ModulStatus,kurs_code: str):
        super().__init__(name, ects, status)
        self.kurs_code = kurs_code

    # Liefert eine Kurzbeschreibung des Moduls.
    def beschreibung(self) -> str:
        return f"{self.name} ({self.kurs_code})"