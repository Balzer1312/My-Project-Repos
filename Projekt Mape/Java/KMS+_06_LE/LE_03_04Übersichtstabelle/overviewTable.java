import java.util.Scanner;


public class overviewTable {
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        double lowerLimit, upperLimit, step, totalPrice,price;

        // Input Kontrolle
        while (true) {
            System.out.print("Geben Sie das untere Preis-Limit ein: ");

            if (input.hasNextDouble()){
                lowerLimit = input.nextDouble();
                break;
            }
            else{
                input.nextLine();
                System.out.print("\nBitte geben sie einen Gültigen Preis ein\n");
            }
        }

        // Input und Preis-Limit Kontrolle
        while (true) {
            System.out.print("Geben Sie das obere Preis-Limit ein: ");

            if (input.hasNextDouble()){
                upperLimit = input.nextDouble();

                if (lowerLimit>upperLimit){
                    System.out.print("\nDer Untere Preis-Limit kann nicht größer als der obere Preis-limit sein!!\n");
                    continue;
                }
                break;
            }
            else{
                input.nextLine();
                System.out.print("\nBitte geben sie einen Gültigen Preis ein\n");
            }
        }

            // Berechnung des Preis Schrittes
            step = (upperLimit - lowerLimit) / 10;

            //Kopf zeile
            System.out.print("\nStück");
            for (int i = 0; i <= 10; i++) {
                price = lowerLimit + (i * step);
                System.out.printf("%10.1f |", price);
            }
            System.out.println(" ");
            System.out.println("-".repeat(140));

            // Tabelle Generieren
            for (int quantity = 10; quantity <= 100; quantity += 10) {
                System.out.printf("%1d |", quantity);

                for (int i = 0; i <= 10; i++) {
                    price = lowerLimit + (i * step);
                    totalPrice = quantity * price;
                    System.out.printf("%10.1f |", totalPrice);
                }
                System.out.println();
                System.out.println("⊸".repeat(140));
            }
            input.close();


        }
}

