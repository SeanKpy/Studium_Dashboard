from dto.dashboard_dto import DashboardDTO
from model.studiengang import Studiengang


# Enthält die Fachlogik des Studien-Dashboards.
class StudienService:

    # Gibt den aktuellen Notendurchschnitt zurück.
    def berechne_notendurchschnitt(self, studiengang: Studiengang) -> float:
        return studiengang.aktueller_notendurchschnitt

    # Berechnet den prozentualen Fortschritt der abgeschlossenen Module.
    def berechne_modulfortschritt(self, studiengang: Studiengang) -> float:
        if studiengang.gesamt_module == 0:
            return 0.0

        return round((studiengang.abgeschlossene_module / studiengang.gesamt_module) * 100, 2)

    # Berechnet den prozentualen Fortschritt der vergangenen Studienzeit.
    def berechne_laufzeitfortschritt(self, studiengang: Studiengang) -> float:
        if studiengang.regelstudienzeit_monate == 0:
            return 0.0

        return round((studiengang.vergangene_monate / studiengang.regelstudienzeit_monate) * 100, 2)

    # Prüft, ob der Modulfortschritt mindestens dem Laufzeitfortschritt entspricht.
    def pruefe_zeitplan(self, studiengang: Studiengang) -> bool:
        modulfortschritt = self.berechne_modulfortschritt(studiengang)
        laufzeitfortschritt = self.berechne_laufzeitfortschritt(studiengang)

        return modulfortschritt >= laufzeitfortschritt

    # Legt die Farbe für die Statusanzeige fest.
    def bestimme_status_farbe(self, studiengang: Studiengang) -> str:
        if self.pruefe_zeitplan(studiengang):
            return "green"

        return "red"

    # Erstellt alle Daten, die im Dashboard angezeigt werden.
    def erstelle_dashboard_dto(self, studiengang: Studiengang) -> DashboardDTO:
        zeitplan_eingehalten = self.pruefe_zeitplan(studiengang)

        status_text = "Du bist in der Zeit" if zeitplan_eingehalten else "Du bist im Verzug"
        status_farbe = self.bestimme_status_farbe(studiengang)

        return DashboardDTO(
            self.berechne_notendurchschnitt(studiengang),
            self.berechne_modulfortschritt(studiengang),
            self.berechne_laufzeitfortschritt(studiengang),
            zeitplan_eingehalten,
            status_text,
            status_farbe
        )