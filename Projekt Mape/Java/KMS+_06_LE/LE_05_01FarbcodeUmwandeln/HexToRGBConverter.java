import java.util.Scanner;

public class HexToRGBConverter {
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);

        int red,green,blue;
        String hexCode;

        while (true) {

            System.out.print("Geben Sie einen Hexadezimalen Farbcode ein (z.B.: #AB3556): ");
            hexCode = input.nextLine().trim();

            if (hexCode.matches("^#[0-9A-Fa-f]{6}$")) {
                red = Integer.parseInt(hexCode.substring(1, 3), 16);
                green = Integer.parseInt(hexCode.substring(3, 5), 16);
                blue = Integer.parseInt(hexCode.substring(5, 7), 16);

                System.out.println("\nDie RGB Werte für den Farbcode " + hexCode + " sind:");
                System.out.println("Rot (R): " + red);
                System.out.println("Grün (G): " + green);
                System.out.println("Blau (B): " + blue);
                break;
            } else {
                System.out.println("Ungültiger Hexadezimaler Farbcode.");
            }

        }
        input.close();

    }
}
