import json

from model.studiengang import Studiengang
from repository.studien_repository import StudienRepository


# Speichert und lädt Studiendaten aus einer JSON-Datei.
class JSONStudienRepository(StudienRepository):

    def __init__(self, dateipfad: str):
        self.dateipfad = dateipfad

    # Lädt die Daten eines Studiengangs.
    def lade_studiengang(self) -> Studiengang:
        with open(self.dateipfad, "r", encoding="utf-8") as datei:
            daten = json.load(datei)

        return Studiengang(
            daten["name"],
            daten["regelstudienzeit_monate"],
            daten["vergangene_monate"],
            daten["gesamt_module"],
            daten["abgeschlossene_module"],
            daten["aktueller_notendurchschnitt"],
            daten["ziel_notendurchschnitt"]
        )

    # Speichert die Daten eines Studiengangs.
    def speichere_studiengang(self, studiengang: Studiengang) -> None:
        daten = {
            "name": studiengang.name,
            "regelstudienzeit_monate": studiengang.regelstudienzeit_monate,
            "vergangene_monate": studiengang.vergangene_monate,
            "gesamt_module": studiengang.gesamt_module,
            "abgeschlossene_module": studiengang.abgeschlossene_module,
            "aktueller_notendurchschnitt": studiengang.aktueller_notendurchschnitt,
            "ziel_notendurchschnitt": studiengang.ziel_notendurchschnitt
        }

        with open(self.dateipfad, "w", encoding="utf-8") as datei:
            json.dump(daten, datei, indent=4, ensure_ascii=False)