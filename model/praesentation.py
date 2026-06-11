from datetime import date
from model.enums import PraesentationsStatus

# Repräsentiert die Präsentation zur Bachelorarbeit.
class Praesentation:

    def __init__(self,datum: date,status: PraesentationsStatus):
        self.datum = datum
        self.status = status