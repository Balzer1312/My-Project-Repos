import java.util.Scanner;

public class IPv4Convert {
    public static void main(String [] args){
        Scanner input = new Scanner(System.in);

        String binary,octal,hex,ip;
        int value;
        String[] octets;
        String ipv4Pattern = "^((25[0-5]|2[0-4][0-9]|1?[0-9][0-9]?)\\.){3}(25[0-5]|2[0-4][0-9]|1?[0-9][0-9]?)$";

        while (true) {
            System.out.print("Geben Sie eine IPv4-Adresse ein (z.B.: 192.168.0.1): ");
            ip = input.nextLine().trim();

            if (!ip.matches(ipv4Pattern)) {
                System.out.println("\nFehler: Ungültige IPv4-Adresse!\n");
                continue;
            }

            break;
        }
        input.close();
        octets = ip.split("\\.");


        System.out.println("\nIPv4-Adresse: " + ip);
        System.out.printf("%-10s | %-10s | %-8s | %-8s\n", "Dezimal", "Binär", "Oktal", "Hexadezimal");
        System.out.println("-".repeat(40));

        for (String octet : octets) {
            value = Integer.parseInt(octet);

            binary = Integer.toBinaryString(value);
            octal = Integer.toOctalString(value);
            hex = Integer.toHexString(value).toUpperCase();

            System.out.printf("%-10d | %-10s | %-8s | %-8s\n", value, binary, octal, hex);
        }

    }
}
