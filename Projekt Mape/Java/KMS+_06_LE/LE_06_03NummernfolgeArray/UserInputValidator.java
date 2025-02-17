import java.util.Scanner;

public class UserInputValidator {
    public static int[] getUserSequence(Scanner input, int length) {
        int[] sequence = new int[length];
        boolean validInput = false;
        String sequenceData;
        String[] inputNumbers;

        while (!validInput) {
            System.out.println("Geben Sie " + length + " Prüfsequenz-Zahlen ein und es soll getrennt durch Leerzeichen sein: ");
            sequenceData = input.nextLine();
            inputNumbers = sequenceData.split("\\s+");

            if (inputNumbers.length == length) {
                try {
                    for (int i = 0; i < length; i++) {
                        sequence[i] = Integer.parseInt(inputNumbers[i]);
                    }
                    validInput = true; // Eingabe korrekt
                } catch (NumberFormatException e) {
                    System.out.println("Ungültige Eingabe! Bitte geben Sie nur ganze Zahlen ein.");
                }
            } else {
                System.out.println("Bitte genau " + length + " Zahlen eingeben!");
            }
        }
        return sequence;
    }
}
