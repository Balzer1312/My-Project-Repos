import java.util.Scanner;
import java.util.InputMismatchException;

public class Numbering {
    public static void main(String [] args){
        Scanner scanner= new Scanner(System.in);

        int startNum;
        int endNum;
        int counter;

        System.out.print("Geben Sie für die Nummerierung die Parameter ein.\n");

        // Valedierung mit try/catch
        while (true) {
            System.out.print("Start Wert: ");
            try {
                startNum = scanner.nextInt();
                break;
            } catch (Exception e) {
                System.out.println("Ungültige Eingabe! Bitte geben Sie eine ganze Zahl ein.");
                scanner.nextLine();
            }
        }


        while (true) {
            System.out.print("End Wert: ");
            try {
                endNum = scanner.nextInt();
                break;
            } catch (Exception e) {
                System.out.println("Ungültige Eingabe! Bitte geben Sie eine ganze Zahl ein.");
                scanner.nextLine();
            }
        }

        while (true) {
            System.out.print("Zähler: ");
            try {
                counter = scanner.nextInt();
                if (counter > 0) {
                    break;
                } else {
                    System.out.println("Der Zähler muss größer als 0 sein.");
                }
            } catch (Exception e) {
                System.out.println("Ungültige Eingabe! Bitte geben Sie eine ganze Zahl ein.");
                scanner.nextLine();
            }
        }

        for(int i =startNum; i <= endNum ; i += counter ){

            System.out.println(i);
        }


    }
}
