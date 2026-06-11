# Enthält die für das Dashboard benötigten Anzeigedaten.
class DashboardDTO:

    def __init__(self, notendurchschnitt: float, modulfortschritt: float,
                 laufzeitfortschritt: float, zeitplan_eingehalten: bool,status_text: str, status_farbe: str):
        self.notendurchschnitt = notendurchschnitt
        self.modulfortschritt = modulfortschritt
        self.laufzeitfortschritt = laufzeitfortschritt
        self.zeitplan_eingehalten = zeitplan_eingehalten
        self.status_text = status_text
        self.status_farbe = status_farbe