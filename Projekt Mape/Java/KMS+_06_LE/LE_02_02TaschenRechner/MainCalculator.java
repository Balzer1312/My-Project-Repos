import java.util.Scanner;

public class MainCalculator {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);

        System.out.print("Bitte geben sie die erste Zahl ein: ");
        int numb1 = scanner.nextInt();

        System.out.print("Bitte geben sie die zweite Zahl ein: ");
        int numb2 = scanner.nextInt();

        int sum = numb1+numb2;
        System.out.println("\nAddieren: "+ numb1 + "+" + numb2 + "= " + sum);

        sum= numb1 - numb2;
        System.out.println("\nSubtrahiert: "+ numb1 + "-" + numb2 + "= " + sum);

        sum= numb1 / numb2;
        System.out.println("\nDivision: "+ numb1 + "/" + numb2 + "= " + sum);

        sum= numb1*numb2;
        System.out.println("\nMultiplikation: "+ numb1 + "*" + numb2 + "= " + sum);
    }
}
