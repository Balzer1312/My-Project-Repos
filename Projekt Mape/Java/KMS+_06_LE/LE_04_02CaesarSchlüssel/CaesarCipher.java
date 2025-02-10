import java.util.Scanner;


public class CaesarCipher {
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        char character,cryptedChar;
        String text;
        int offset;


        System.out.println("Geben Sie den Text ein, der verschlüsselt werden soll:");
        text = input.nextLine();

        // Schlüssel Verschiebungswert
        while (true) {
            System.out.println("Geben Sie den Verschiebewert ein:");
            if (input.hasNextInt()) {
                offset = input.nextInt();
                break;
            }else{
                input.nextLine();
                System.out.print("\nEingabe ungültig,Bitte eine ganze Zahl eingeben!!\n");
            }
        }

        System.out.println("Verschlüsselter Text:");

        for (int i = 0; i < text.length(); i++) {
            character = text.charAt(i);


            if (character >= 65 && character <= 90) {        // Der Buchstabe groß "A" hat den ASCII Wert 65 und "Z" den Wert 90
                cryptedChar = (char) (((character - 65 + offset) % 26) + 65);  // Modulo 26 bezieht sich auf die Anzahl der Buchstaben des Alphapets
                System.out.print(cryptedChar);
            }

            else if (character >= 97 && character <= 122) {  // Der Buchstabe klein "a" hat den ASCII Wert 97 und "z" den Wert 122
                cryptedChar = (char) (((character - 97 + offset) % 26) + 97);
                System.out.print(cryptedChar);
            }

            else {
                System.out.print(character);
            }
        }
        System.out.println();
        input.close();

    }
}
