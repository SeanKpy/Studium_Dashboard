from controller.app_controller import AppController
from gui.dashboard_gui import DashboardGUI
from repository.json_studien_repository import JSONStudienRepository


# Startet und verbindet die zentralen Komponenten der Anwendung.
class Application:

    def __init__(self):
        self.repository = JSONStudienRepository("daten/studiengang.json")
        self.controller = AppController(self.repository)
        self.gui = DashboardGUI(self.controller)

    # Startet die grafische Benutzeroberfläche.
    def start(self) -> None:
        self.gui.starte_gui()