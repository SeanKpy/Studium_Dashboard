from enum import Enum


class Pruefungsart(Enum):
    KLAUSUR = "Klausur"
    WORKBOOK = "Workbook"
    PORTFOLIO = "Portfolio"
    PROJEKTARBEIT = "Projektarbeit"
    BACHELORARBEIT = "Bachelorarbeit"


class Pruefungsleistung:
    def __init__(self, pruefungsart, note, pruefungsdatum):
        self.pruefungsart = pruefungsart
        self.note = note
        self.pruefungsdatum = pruefungsdatum

    @property
    def bestanden(self):
        return self.note <= 4.0


pruefung = Pruefungsleistung(
    Pruefungsart.PORTFOLIO,
    2.3,
    "2026-01-15"
)

print(pruefung.pruefungsart.value)
print(pruefung.note)
print("Prüfung bestanden:", pruefung.bestanden)