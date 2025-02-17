import java.util.Arrays;

public class OutputFormatter {
    public static void printResults(int[] dataArray, int[] checkSequence, boolean sequenceFound) {
        System.out.println("\nÜbertragene Daten: " + Arrays.toString(dataArray));
        System.out.println("Prüfsequenz: " + Arrays.toString(checkSequence));
        System.out.println("Ergebnis: " + (sequenceFound ? "Sequenz gefunden!" : "Sequenz nicht gefunden."));
    }
}
