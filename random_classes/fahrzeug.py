class Fahrzeug():
    alle_marken = ["BMW","Volkswagen","Audi", "Mercedes Benz"]

    def __init__(self, gewicht: int, max_pasagiere: int, max_geschwindigkeit: int, marke: str):
        self.gewicht = gewicht
        self.max_pasagiere = max_pasagiere
        self.max_geschwindigkeit = max_geschwindigkeit
        self.marke = marke
        if self.marke not in Fahrzeug.alle_marken:
            Fahrzeug.alle_marken.append(self.marke)
            Fahrzeug.alle_marken.sort()
        self.motor_zustand = False
        self.geschwindigkeit = 0
    
    def geschwindigkeit_aendern(self, geschwindigkeit=10):
        if self.motor_zustand:
            self.geschwindigkeit += geschwindigkeit
        else:
            return "Der Motor ist Aus."
        
    def gib_geschwindigkeit(self):
        return self.geschwindigkeit
    
    def motor_schalten(self):
        if self.motor_zustand:
            self.motor_zustand = False
        else:
            self.motor_zustand = True
    
    def gib_motor_zustand(self):
        return self.motor_zustand()
    
    def neue_marke_deklarieren(neue_marke: str):
        Fahrzeug.alle_marken.append(neue_marke)

    '''
    def gib_alle_marken():
        for marke in Fahrzeug.alle_marken():
            print(marke)
    '''
        