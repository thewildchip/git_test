from fahrzeug import Fahrzeug

class Auto(Fahrzeug):

    def __init__(self, GEWICHT_AUTO, max_pasagiere, max_geschwindigkeit, marke, anzahl_tueren =4, anzahl_raeder=4):
        super().__init__(GEWICHT_AUTO, max_pasagiere, max_geschwindigkeit, marke)
        self.anzahl_tueren = anzahl_tueren
        self.anzahl_raeder = anzahl_raeder
        self.gewicht_zusatz = 0
        self.gewicht_gesamt = GEWICHT_AUTO
        self.sports_mode = False

    def schalte_sports_mode(self):
        if self.motor_zustand:
            if self.sports_mode:
                self.sports_mode = False
            else:
                self.sports_mode = True

    def gewicht_zusatz_beladen(self, gewicht: int):
        self.gewicht_zusatz += gewicht
        self.gewicht_gesamt += self.gewicht_zusatz

    def gib_gewicht_zusatz(self) -> int:
        return self.gewicht_zusatz
