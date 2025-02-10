import java.util.Scanner;


public class investigateText {
    public static void main(String[] args){
        Scanner input= new Scanner(System.in);
        String text;
        char currentChar;
        int vowels=0, consonants=0, punctuationMarks=0, spaces=0,textLength;

        System.out.print("Bitte geben Sie einen Text ein: ");
        text=input.nextLine();
        textLength=text.length();

        for (int i = 0; i < textLength; i++) {
            currentChar = text.charAt(i);
            currentChar = Character.toLowerCase(currentChar);

            if (Character.isWhitespace(currentChar)) {
                spaces++;
            } else if ("aeiouäöü".indexOf(currentChar) != -1) { // Überprüfen auf Vokale
                vowels++;
            } else if (Character.isLetter(currentChar)) { // Überprüfen auf Konsonanten
                consonants++;
            } else if (".,;:!?\"".indexOf(currentChar) != -1) { // Überprüfen auf Satzzeichen
                punctuationMarks++;
            }
        }

        System.out.println("Analyse des Textes:");
        System.out.println("Anzahl der Vokale: " + vowels);
        System.out.println("Anzahl der Konsonanten: " + consonants);
        System.out.println("Anzahl der Satzzeichen: " + punctuationMarks);
        System.out.println("Anzahl der Leerzeichen: " + spaces);
        System.out.println("Länge des Textes: " + textLength);

        input.close();

    }
}
