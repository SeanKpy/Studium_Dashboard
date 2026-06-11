import tkinter as tk
from tkinter import messagebox, ttk

from model.studiengang import Studiengang

# Stellt die grafische Benutzeroberfläche des Studien-Dashboards bereit.
class DashboardGUI:

    def __init__(self, controller):
        self.controller = controller
        self.eingabefelder = {}
        self.bachelorarbeit_var = None
        self.dashboard_fenster = None

    # Startet zuerst das Eingabefenster.
    def starte_gui(self) -> None:
        self.zeige_eingabeformular()

    # Zeigt ein separates Fenster zur Eingabe der Studiendaten.
    def zeige_eingabeformular(self) -> None:
        eingabe_fenster = tk.Tk()
        eingabe_fenster.title("Studiendaten eingeben")
        eingabe_fenster.geometry("430x480")

        titel = tk.Label(
            eingabe_fenster,
            text="Bitte Studiendaten eingeben",
            font=("Arial", 16, "bold")
        )
        titel.pack(pady=20)

        formular = tk.Frame(eingabe_fenster)
        formular.pack(pady=10)

        studiendaten = self.controller.lade_studiendaten()

        felder = [
            ("Studiengang:", "name"),
            ("Regelstudienzeit (Monate):", "regelstudienzeit_monate"),
            ("Vergangene Monate:", "vergangene_monate"),
            ("Gesamtmodule:", "gesamt_module"),
            ("Abgeschlossene Module:", "abgeschlossene_module"),
            ("Aktueller Notendurchschnitt:", "aktueller_notendurchschnitt"),
            ("Ziel-Notendurchschnitt:", "ziel_notendurchschnitt")
        ]

        for zeile, (label_text, attribut) in enumerate(felder):
            label = tk.Label(formular, text=label_text, font=("Arial", 11))
            label.grid(row=zeile, column=0, sticky="w", padx=10, pady=7)

            eingabe = tk.Entry(formular, width=25, font=("Arial", 11))
            eingabe.grid(row=zeile, column=1, padx=10, pady=7)
            eingabe.insert(0, str(getattr(studiendaten, attribut)))

            self.eingabefelder[attribut] = eingabe

        label = tk.Label(formular, text="Bachelorarbeit angefangen?:", font=("Arial", 11))
        label.grid(row=len(felder), column=0, sticky="w", padx=10, pady=7)

        self.bachelorarbeit_var = tk.StringVar(value="Nein")
        bachelor_dropdown = ttk.Combobox(
            formular,
            textvariable=self.bachelorarbeit_var,
            values=["Ja", "Nein"],
            state="readonly",
            width=22,
            font=("Arial", 11)
        )
        bachelor_dropdown.grid(row=len(felder), column=1, padx=10, pady=7)

        ok_button = tk.Button(
            eingabe_fenster,
            text="OK",
            width=14,
            command=lambda: self.speichere_eingaben_und_oeffne_dashboard(eingabe_fenster)
        )
        ok_button.pack(pady=20)

        eingabe_fenster.mainloop()

    # Speichert die Eingaben und öffnet danach das Dashboard.
    def speichere_eingaben_und_oeffne_dashboard(self, eingabe_fenster) -> None:
        try:
            studiengang = Studiengang(
                self.eingabefelder["name"].get(),
                int(self.eingabefelder["regelstudienzeit_monate"].get()),
                int(self.eingabefelder["vergangene_monate"].get()),
                int(self.eingabefelder["gesamt_module"].get()),
                int(self.eingabefelder["abgeschlossene_module"].get()),
                float(self.eingabefelder["aktueller_notendurchschnitt"].get()),
                float(self.eingabefelder["ziel_notendurchschnitt"].get())
            )

            self.controller.speichere_studiendaten(studiengang)

            eingabe_fenster.destroy()
            self.zeige_dashboard()

        except ValueError:
            messagebox.showerror(
                "Fehler",
                "Bitte gültige Zahlenwerte eingeben."
            )

    # Zeigt das Dashboard-Fenster nach der Eingabe.
    def zeige_dashboard(self) -> None:
        self.dashboard_fenster = tk.Tk()
        self.dashboard_fenster.title("Studium Dashboard")
        self.dashboard_fenster.geometry("950x700")

        self.aktualisiere_anzeige()

        self.dashboard_fenster.mainloop()

    # Aktualisiert die gesamte Dashboard-Anzeige.
    def aktualisiere_anzeige(self) -> None:
        for widget in self.dashboard_fenster.winfo_children():
            widget.destroy()

        studiengang = self.controller.lade_studiendaten()
        dashboard_daten = self.controller.lade_dashboarddaten()

        haupt_frame = tk.Frame(self.dashboard_fenster, bd=2, relief="solid")
        haupt_frame.pack(fill="both", expand=True, padx=20, pady=20)

        titel = tk.Label(
            haupt_frame,
            text="Studium Dashboard",
            font=("Arial", 28, "bold")
        )
        titel.pack(pady=25)

        inhalt_frame = tk.Frame(haupt_frame, bd=1, relief="solid")
        inhalt_frame.pack(fill="both", expand=True)

        links = tk.Frame(inhalt_frame, bd=1, relief="solid")
        links.pack(side="left", fill="both", expand=True)

        rechts = tk.Frame(inhalt_frame, bd=1, relief="solid")
        rechts.pack(side="right", fill="both", expand=True)

        laufzeit_label = tk.Label(
            links,
            text="Laufzeit",
            font=("Arial", 18)
        )
        laufzeit_label.pack(pady=25)

        canvas = tk.Canvas(links, width=260, height=260)
        canvas.pack(pady=10)

        laufzeit_prozent = dashboard_daten.laufzeitfortschritt
        winkel = (laufzeit_prozent / 100) * 360

        canvas.create_oval(30, 30, 230, 230, outline="black", width=2, fill="#eeeeee")
        canvas.create_arc(
            30, 30, 230, 230,
            start=90,
            extent=-winkel,
            fill=dashboard_daten.status_farbe,
            outline="black"
        )
        canvas.create_text(
            130, 130,
            text=f"{int(laufzeit_prozent)}%",
            font=("Arial", 22, "bold")
        )

        monate_text = tk.Label(
            links,
            text=f"{studiengang.vergangene_monate} Monate von {studiengang.regelstudienzeit_monate}",
            font=("Arial", 16)
        )
        monate_text.pack(pady=20)

        werte = [
            f"Notendurchschnittziel: {studiengang.ziel_notendurchschnitt}",
            f"Aktueller Notendurchschnitt: {dashboard_daten.notendurchschnitt}",
            f"{studiengang.abgeschlossene_module} Abgeschlossene Module von {studiengang.gesamt_module}",
            f"Bachelorarbeit angefangen? {self.bachelorarbeit_var.get()}"
        ]

        for index, text in enumerate(werte):
            label = tk.Label(
                rechts,
                text=text,
                font=("Arial", 17)
            )
            label.pack(pady=35 if index == 0 else 30)

        status_frame = tk.Frame(haupt_frame, bd=1, relief="solid")
        status_frame.pack(fill="x")

        status_label = tk.Label(
            status_frame,
            text=dashboard_daten.status_text,
            font=("Arial", 22),
            fg=dashboard_daten.status_farbe
        )
        status_label.pack(pady=20)