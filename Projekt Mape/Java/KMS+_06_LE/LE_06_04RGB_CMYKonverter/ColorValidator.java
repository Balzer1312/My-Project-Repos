import java.util.regex.Pattern;
import java.util.regex.Matcher;

public class ColorValidator {
    public static boolean isValidRgb(String input) {
        Pattern pattern;
        Matcher matcher;
        String[] values;
        int num;

        pattern = Pattern.compile("^\\s*\\d{1,3}\\s*[,.]\\s*\\d{1,3}\\s*[,.]\\s*\\d{1,3}\\s*$");
        matcher = pattern.matcher(input);
        if (!matcher.matches()) return false;

        values = input.split("[,.]");
        for (String value : values) {
            num = Integer.parseInt(value);
            if (num < 0 || num > 255) return false;
        }
        return true;
    }

    public static boolean isValidHex(String hex) {
        boolean isValid;
        isValid = hex.matches("^#?[0-9A-Fa-f]{3}$") || hex.matches("^#?[0-9A-Fa-f]{6}$");
        return isValid;
    }
}
