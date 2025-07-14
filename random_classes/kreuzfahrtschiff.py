from fahrzeug import Fahrzeug

class Kreuzfahrtschiff(Fahrzeug):

    def __init__(self, gewicht, max_pasagiere, max_geschwindigkeit, marke="Carnival Corporation & plc."):
        super().__init__(gewicht, max_pasagiere, max_geschwindigkeit, marke)

    
alois = Kreuzfahrtschiff(200,200, 100)

for marke in Fahrzeug.alle_marken:
    print(marke)