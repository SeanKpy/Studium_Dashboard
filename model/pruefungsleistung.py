from datetime import date
from model.enums import Pruefungsart


class Pruefungsleistung:
    """
    Repräsentiert eine Prüfungsleistung eines Moduls.
    """

    def __init__(self,pruefungsart: Pruefungsart,note: float,pruefungsdatum: date):
        self.pruefungsart = pruefungsart
        self.note = note
        self.pruefungsdatum = pruefungsdatum

    @property
    def bestanden(self) -> bool:
        """
        Leitet den Bestehensstatus aus der Note ab.
        """
        return self.note <= 4.0