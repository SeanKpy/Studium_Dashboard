from datetime import date
from model.modul import Modul

# Repräsentiert ein Semester eines Studiengangs.
class Semester:

    def __init__(self,nummer: int,start_datum: date,end_datum: date):
        self.nummer = nummer
        self.start_datum = start_datum
        self.end_datum = end_datum
        self.module = []

    # Fügt dem Semester ein Modul hinzu.
    def modul_hinzufuegen(self, modul: Modul) -> None:
        self.module.append(modul)