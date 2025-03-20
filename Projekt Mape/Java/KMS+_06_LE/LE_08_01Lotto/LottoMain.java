import java.util.Arrays;
import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

public class LottoMain {
    public static void main(String[] args) {
        Set<Integer> currentNumber = new HashSet<>();
        Scanner input = new Scanner(System.in);
        String userNumber;
        int checkNumber;
        int[] LotteryNumbers = new int[6];


        System.out.println("Bitte geben Sie sechs Lottozahlen (1-45) ein:");

        for (int i = 0; i < 6; i++) {
            while (true) {
                System.out.printf("Geben Sie die %d. Zahl ein: ", i + 1);
                userNumber = input.nextLine();

                try {
                    checkNumber = Integer.parseInt(userNumber);

                    if (checkNumber < 1 || checkNumber > 45) {
                        throw new IllegalArgumentException("Die Zahl muss zwischen 1 und 45 liegen. Wiederholen!");
                    }
                    if (currentNumber.contains(checkNumber)) {
                        throw new IllegalArgumentException("Diese Zahl haben Sie schon. Bitte nochmals eingeben!");
                    }

                    LotteryNumbers[i] = checkNumber;
                    currentNumber.add(checkNumber);
                    break;

                } catch (NumberFormatException e) {
                    System.out.println("Das ist keine gültige Zahl! Bitte eine ganze Zahl eingeben.");
                } catch (IllegalArgumentException e) {
                    System.out.println(e.getMessage());
                }
            }
        }

        Arrays.sort(LotteryNumbers);
        System.out.println("Das sind Ihre Lottozahlen: " + Arrays.toString(LotteryNumbers));

        input.close();


    }
}
