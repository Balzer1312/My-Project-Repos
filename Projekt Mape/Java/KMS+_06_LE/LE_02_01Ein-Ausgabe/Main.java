import java.util.Scanner;

public class Main {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);

        System.out.print("Bitte geben sie ihren Vornamen ein: ");
        String firstname = scanner.nextLine();
        System.out.print("Bitte geben sie die erste Zahl ein: ");
        int numb1 = scanner.nextInt();

        System.out.print("Bitte geben sie Ihren Nachnamen ein ");
        String lastname = scanner.nextLine();
        System.out.print("Bitte geben sie die zweite Zahl ein: ");
        int numb2 = scanner.nextInt();

        System.out.println("Die Add");

        System.out.println("Willkommen, "+ firstname+" "+ lastname+" bei Java!!!");
        }
}
