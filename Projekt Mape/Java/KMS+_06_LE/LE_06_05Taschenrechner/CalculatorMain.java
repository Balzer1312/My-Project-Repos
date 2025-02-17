import java.util.Scanner;

public class CalculatorMain {
    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);
        String value1,value2;
        char operator;
        int intResult,numInt1,numInt2;
        double doubleResult,numFloat1,numFloat2;

        System.out.println("Willkommen beim Taschenrechner!");

        // Benutzereingaben validieren
        value1 = ValidInput.validateInput(input, "Geben Sie die erste Zahl ein: ");
        value2 = ValidInput.validateInput(input, "Geben Sie die zweite Zahl ein: ");
        operator = ValidInput.validateOperator(input);

        // Datentyp erkennen und Berechnung durchführen
        if (ValidInput.isInteger(value1) && ValidInput.isInteger(value2)) {
            numInt1 = Integer.parseInt(value1);
            numInt2 = Integer.parseInt(value2);
            intResult = BasicCalculation.calculate(numInt1, numInt2, operator);
            System.out.println("Ergebnis: " + intResult);
        } else {
            numFloat1 = Double.parseDouble(value1);
            numFloat2 = Double.parseDouble(value2);
            doubleResult = BasicCalculation.calculate(numFloat1, numFloat2, operator);
            System.out.println("Ergebnis: " + doubleResult);
        }


        input.close();
    }

}
