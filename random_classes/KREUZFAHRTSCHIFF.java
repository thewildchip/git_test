public class AUTO extends FAHRZEUGE
{
   // Variabeln explizit nur für Autos
   private int anzahlTueren;
   private int kofferRaum; // in Kubikmeter
   
   public AUTO(int anzahlTueren1, int kofferRaum1,
   
               int gewicht1, int pasagiere1,int bauJahr1,
               int maxGeschwindigkeit1, int leistung1)
   {
       super(gewicht1, pasagiere1, bauJahr1, maxGeschwindigkeit1, leistung1, 4, 5);
       
       anzahlTueren = anzahlTueren1;
       kofferRaum = kofferRaum1;
   }
   
   public void sitzeUpdate(int sitze) {
       anzahlSitze += sitze; // anzahlSitze = anzahlSitze + sitze;
   }
   
   public String schalteSportsModeAn() {
       if (zustand == "An" && currentGeschwindigkeit >= 100)
       {
           currentGeschwindigkeit = 2*(currentGeschwindigkeit); 
           zustand = "Sport";
           return "Sports-Mode wurde erfolgreich Aktiviert";
       }
       
       else {
           return 
           "Sports-Mode konnte nicht aktiviert werden. Überprüfen Sie zustand bzw. currentGeschwindigkeit.";
       }
   }
   public String schalteSportsModeAus() {
       if (zustand == "Sport")
       {
           currentGeschwindigkeit = currentGeschwindigkeit/2; 
           zustand = "An";
           return "Sports-Mode wurde erfolgreich deaktiviert";
       }
       
       else {
           return 
           "Sports-Mode konnte nicht deaktiviert werden.";
       }
   }
}
