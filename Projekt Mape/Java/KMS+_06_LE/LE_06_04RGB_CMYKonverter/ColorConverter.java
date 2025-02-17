

public class ColorConverter {
    public static double[] rgbToCmy(int red, int green, int blue) {
        double cyan, magenta, yellow;

        cyan = (255 - red) / 255.0 * 100;
        magenta = (255 - green) / 255.0 * 100;
        yellow = (255 - blue) / 255.0 * 100;

        return new double[]{                          // Kommastellen Umwandlung
                Math.round(cyan * 100.0) / 100.0,
                Math.round(magenta * 100.0) / 100.0,
                Math.round(yellow * 100.0) / 100.0
        };
    }

    public static int[] hexToRgb(String hex) {
        int red, green, blue;

        hex = hex.replace("#", "");

        if (hex.length() == 3) {
            red = Integer.parseInt(hex.substring(0, 1) + hex.substring(0, 1), 16);
            green = Integer.parseInt(hex.substring(1, 2) + hex.substring(1, 2), 16);
            blue = Integer.parseInt(hex.substring(2, 3) + hex.substring(2, 3), 16);

        } else if (hex.length() == 6) {
            red = Integer.parseInt(hex.substring(0, 2), 16);
            green = Integer.parseInt(hex.substring(2, 4), 16);
            blue = Integer.parseInt(hex.substring(4, 6), 16);

        } else {
            System.out.println("\nUngültiges Hex-Farbformat!");
            return new int[]{0, 0, 0};
        }

        return new int[]{red, green, blue};
    }
}
