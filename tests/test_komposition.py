class Semester:
    def __init__(self, nummer):
        self.nummer = nummer
        self.module = []

    def modul_hinzufuegen(self, modul):
        self.module.append(modul)


semester = Semester(1)

semester.modul_hinzufuegen("Einführung in Python")
semester.modul_hinzufuegen("Mathematik")

print("Semester:", semester.nummer)
print("Module:", semester.module)