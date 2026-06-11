from enum import Enum


class ModulStatus(Enum):
    """
    Mögliche Bearbeitungszustände eines Moduls.
    """

    OFFEN = "offen"
    IN_BEARBEITUNG = "in Bearbeitung"
    ABGESCHLOSSEN = "abgeschlossen"


class Pruefungsart(Enum):
    """
    Definiert die möglichen Arten von Prüfungsleistungen.
    """

    KLAUSUR = "Klausur"
    WORKBOOK = "Workbook"
    PORTFOLIO = "Portfolio"
    PROJEKTARBEIT = "Projektarbeit"
    BACHELORARBEIT = "Bachelorarbeit"


class PraesentationsStatus(Enum):
    """
    Status einer Präsentation.
    """

    OFFEN = "offen"
    BESTANDEN = "bestanden"
    NICHT_BESTANDEN = "nicht bestanden"