import java.util.Scanner;


public class InputValid {
    public static void main(String[] args){

        Scanner scanner= new Scanner(System.in);

        String product;
        double price;
        String input;
        int productID;


        while (true) {
            System.out.print("Geben Sie die Produkt Bezeichnung ein: ");
            product = scanner.nextLine();

            if (product.matches("[a-zA-Z0-9\\s]+")) {
                break;
            } else {
                System.out.println("Fehler: Die Bezeichnung darf nur Buchstaben enthalten!");
            }
        }

        while (true) {
            System.out.print("Geben Sie die Produkt ID ein: ");
            if (scanner.hasNextInt()) {
                productID = scanner.nextInt();
                scanner.nextLine();
                break;
            } else {
                System.out.println("Fehler: Bitte eine gültige ganze Zahl eingeben!");
                scanner.nextLine();
            }
        }

        while(true){
            System.out.print("Geben Sie den Preis des Produkts ein: ");
            input = scanner.nextLine();
            input = input.replace(",",".");

            if (input.matches("\\d+")){

                input = input+".00";
                price= Double.parseDouble(input);
                break;
            }
            else if(input.matches("\\d+(\\.\\d{1,2})")){

                price= Double.parseDouble(input);
                break;
            }else{
                System.out.print("Fehler: Bitte eine Zahl mit 2 kommastellen angeben!\n ");
            }
        }

    System.out.println("\nDas Produkt \"" + product + "\" wurde hinzugefügt.");
    System.out.println("Produkt ID: "+ productID);
    System.out.printf("Der Preis für das Produkt: %.2f€\n",price);
    }
}
