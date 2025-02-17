import java.util.Scanner;

public class ExtractInfo {
    public static void main(String [] args){
        Scanner input = new Scanner(System.in);

        String artikelPart= "derArtikel[";
        String orderPart="]wurdebestelltvon[";
        String artikelInput,orderInput,text;
        String [] parts;


        while (true) {
            System.out.print("Geben Sie den Artikel ein: ");
            artikelInput = input.nextLine();
            System.out.print("Geben Sie den Kunden ein: ");
            orderInput = input.nextLine();

            text = artikelPart + artikelInput + orderPart + orderInput + "]";//(Format: derArtikel[Artikel]wurdebestelltvon[Besteller]):


            // Zeichenkette anhand der eckigen Klammern [ ] splitten
            parts = text.split("[\\[\\]]");

            if (parts.length == 4 && !parts[1].isEmpty() && !parts[3].isEmpty()) {
                System.out.println("\nErfolgreich extrahiert:");
                System.out.println("Artikelbezeichnung: " + parts[1]);
                System.out.println("Besteller: " + parts[3]);
                break;
            } else {
                System.out.println("Fehler: Die Eingabe entspricht nicht dem erwarteten Format!");
            }
        }
        input.close();
    }
}
