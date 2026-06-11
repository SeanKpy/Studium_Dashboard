
# Repräsentiert die zentralen Studiendaten des Dashboards.
class Studiengang:

    def __init__(self,name: str,regelstudienzeit_monate: int,vergangene_monate: int,gesamt_module: int,abgeschlossene_module: int,
            aktueller_notendurchschnitt: float,
            ziel_notendurchschnitt: float
    ):

        self.name = name
        self.regelstudienzeit_monate = regelstudienzeit_monate
        self.vergangene_monate = vergangene_monate
        self.gesamt_module = gesamt_module
        self.abgeschlossene_module = abgeschlossene_module
        self.aktueller_notendurchschnitt = aktueller_notendurchschnitt
        self.ziel_notendurchschnitt = ziel_notendurchschnitt