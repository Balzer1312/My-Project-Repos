import java.util.Scanner;

public class ColorCodeConverterMain {
    public static void main(String[] args) {

        Scanner input= new Scanner(System.in);
        String choice,rgbInput,hexInput;
        String[] rgbValues;
        int red,green,blue;
        int[] rgb;
        double[] cmy;



        System.out.println("Willkommen zum Farbkonverter!");

        while (true) {
            System.out.println("\nWählen Sie den Farbmodus: RGB oder HEX (oder 'STOP' zum Beenden): ");
            choice = input.nextLine().trim().toUpperCase();

            switch (choice) {
                case "RGB":
                    System.out.println("\nGeben Sie die RGB-Werte ein (Format: R,G,B, z.B. 255,110,74): ");
                    rgbInput = input.nextLine().trim();

                    if (!ColorValidator.isValidRgb(rgbInput)) {
                        System.out.println("\n\nUngültige RGB-Eingabe! Werte müssen zwischen 0 und 255 liegen.");
                        continue;
                    }

                    rgbValues = rgbInput.split("[,.]");
                    red = Integer.parseInt(rgbValues[0]);
                    green = Integer.parseInt(rgbValues[1]);
                    blue = Integer.parseInt(rgbValues[2]);

                    cmy = ColorConverter.rgbToCmy(red, green, blue);
                    System.out.println("\nRGB-Werte: R=" + red + ", G=" + green + ", B=" + blue);
                    System.out.println("CMY-Werte: C=" + cmy[0] + "%, M=" + cmy[1] + "%, Y=" + cmy[2] + "%\n\n");
                    break;

                case "HEX":
                    System.out.println("\nGeben Sie den Hex-Farbcode ein (z.B. #80FF40): ");
                    hexInput = input.nextLine().trim();

                    if (!ColorValidator.isValidHex(hexInput)) {
                        System.out.println("\nUngültige Hex-Farbe! Bitte ein korrektes Format (#RGB oder #RRGGBB) eingeben.");
                        continue;
                    }

                    rgb = ColorConverter.hexToRgb(hexInput);
                    cmy = ColorConverter.rgbToCmy(rgb[0], rgb[1], rgb[2]);

                    System.out.println("\nRGB-Werte: R=" + rgb[0] + ", G=" + rgb[1] + ", B=" + rgb[2]);
                    System.out.println("CMY-Werte: C=" + cmy[0] + "%, M=" + cmy[1] + "%, Y=" + cmy[2] + "%\n\n");
                    break;

                case "STOP":
                    System.out.println("Programm wird beendet");
                    input.close();
                    return;

                default:
                    System.out.println("\n\nUngültiger Modus! Bitte wählen Sie 'RGB', 'HEX' oder 'EXIT'.");
            }
        }
    }
}
