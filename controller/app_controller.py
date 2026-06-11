from repository.json_studien_repository import JSONStudienRepository
from service.studien_service import StudienService
# Vermittelt zwischen GUI, Fachlogik und Datenspeicherung.
class AppController:

    def __init__(self, repository: JSONStudienRepository):
        self.repository = repository
        self.service = StudienService()

    # Lädt die Studiendaten.
    def lade_studiendaten(self):
        return self.repository.lade_studiengang()

    # Speichert die Studiendaten.
    def speichere_studiendaten(self, studiengang):
        self.repository.speichere_studiengang(studiengang)

    # Erstellt die Dashboard-Daten für die GUI.
    def lade_dashboarddaten(self):
        studiengang = self.repository.lade_studiengang()
        return self.service.erstelle_dashboard_dto(studiengang)