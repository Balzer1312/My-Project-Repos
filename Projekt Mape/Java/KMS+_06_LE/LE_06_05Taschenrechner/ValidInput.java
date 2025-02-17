import java.util.Scanner;


public class ValidInput {

    public static String validateInput(Scanner input, String message) {
        String value;

        while (true) {
            System.out.print(message);
            value = input.next().trim();


            if (value.matches("-?\\d+(\\.\\d+)?")) {
                return value;
            } else {
                System.out.println("Bitte geben Sie eine gültige Nummer ein.");
            }
        }
    }

    public static boolean isInteger(String value) {
        return value.matches("-?\\d+");
    }

    public static char validateOperator(Scanner input) {
        String value;

        while (true) {
            System.out.print("Wählen Sie eine Operation (+, -, *, /): ");
            value = input.next().trim();


            if (value.matches("[+\\-*/]") && value.length() == 1) {
                return value.charAt(0);
            } else {
                System.out.println("Bitte geben Sie einen gültigen Operator ein (+, -, *, /).");
            }
        }
    }
}
