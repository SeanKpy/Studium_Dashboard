import json
import tkinter as tk


def lade_daten(pfad):
    with open(pfad, "r", encoding="utf-8") as datei:
        return json.load(datei)


daten = lade_daten("studiendaten.json")

regelstudienzeit = daten["regelstudienzeitMonate"]
vergangene_monate = daten["vergangeneMonate"]
gesamt_module = daten["gesamtModule"]
abgeschlossene_module = daten["abgeschlosseneModule"]
ziel_note = daten["notendurchschnittZiel"]
aktuelle_note = daten["aktuellerNotendurchschnitt"]
bachelorarbeit = daten["bachelorarbeitAngefangen"]

laufzeit_prozent = vergangene_monate / regelstudienzeit
modul_prozent = abgeschlossene_module / gesamt_module

ist_in_der_zeit = modul_prozent >= laufzeit_prozent

farbe = "green" if ist_in_der_zeit else "red"
status_text = "Du bist in der Zeit" if ist_in_der_zeit else "Du bist im Verzug"

fenster = tk.Tk()
fenster.title("Studium Dashboard")
fenster.geometry("800x500")

titel = tk.Label(
    fenster,
    text="Studium Dashboard",
    font=("Arial", 28, "bold")
)
titel.pack(pady=20)

frame = tk.Frame(fenster)
frame.pack(fill="both", expand=True, padx=20, pady=20)

links = tk.Frame(frame)
links.pack(side="left", fill="both", expand=True)

laufzeit_label = tk.Label(
    links,
    text="Laufzeit",
    font=("Arial", 18)
)
laufzeit_label.pack(pady=10)

canvas = tk.Canvas(links, width=220, height=230)
canvas.pack()

canvas.create_oval(20, 20, 200, 200, outline="black")

# Kreisanteil dynamisch zeichnen
winkel = laufzeit_prozent * 360
canvas.create_arc(
    20, 20, 200, 200,
    start=90,
    extent=-winkel,
    fill=farbe,
    outline="black"
)

canvas.create_text(
    110,
    110,
    text=f"{int(laufzeit_prozent * 100)}%",
    font=("Arial", 20)
)

monate_label = tk.Label(
    links,
    text=f"{vergangene_monate} Monate von {regelstudienzeit}",
    font=("Arial", 14)
)
monate_label.pack(pady=10)

rechts = tk.Frame(frame)
rechts.pack(side="right", fill="both", expand=True)

bachelor_text = "Ja" if bachelorarbeit else "Nein"

infos = [
    f"Notendurchschnittziel: {ziel_note}",
    "",
    f"Aktueller Notendurchschnitt: {aktuelle_note}",
    "",
    f"{abgeschlossene_module} abgeschlossene Module von {gesamt_module}",
    "",
    f"Bachelorarbeit angefangen? {bachelor_text}"
]

for text in infos:
    label = tk.Label(
        rechts,
        text=text,
        font=("Arial", 16),
        anchor="w"
    )
    label.pack(pady=8)

status = tk.Label(
    fenster,
    text=status_text,
    font=("Arial", 18),
    fg=farbe
)
status.pack(pady=20)

fenster.mainloop()