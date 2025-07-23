public class FAHRZEUGE
{
   // Um für die Subklassen zugänglich zu machen, müssen die Variablen protected oder public sein, nicht private.
   int gewicht; // in Tonnen
   int pasagiere;
   int bauJahr;
   
   int maxGeschwindigkeit;
   int leistung;
   int anzahlRaeder;
   
   int anzahlSitze;
   
   
   int currentGeschwindigkeit;
   String zustand;
   
   //     FAHRZEUGE(Gewicht,     Pasagiere,      bauJahr,      maximale Geschwindigkeit,   leistung,    Anzahl der Räder,    Anzahl der Sitze,  Markenname)
   public FAHRZEUGE(int gewicht1, int pasagiere1, int bauJahr1, 
                   int maxGeschwindigkeit1, int leistung1, int anzahlRaeder1, 
                   int anzahlSitze1)
   {
       currentGeschwindigkeit = 0;
       zustand = "Aus";
       gewicht = gewicht1;
       pasagiere = pasagiere1;
       bauJahr = bauJahr1;
       maxGeschwindigkeit = maxGeschwindigkeit1;
       leistung = leistung1;
       anzahlRaeder = anzahlRaeder1;
       anzahlSitze = anzahlSitze1;
   }
   
   public void geschwindigkeitAendern(int zielGeschwindigkeit){
       if (zustand == "An") {
           currentGeschwindigkeit = zielGeschwindigkeit;
       }
       else {
           return;
       }
   }
   
   public String startUndAusKnopf() {
       if (zustand == "Aus") {
           zustand = "An";
           return "Der Motor ist An";
       }
       else {
           zustand = "Aus";
           currentGeschwindigkeit = 0;
           return "Der Motor ist Aus.";
       }
   }
   
   public int gibCurrentGeschwindigkeit() {
       return currentGeschwindigkeit;
   }
   
}
