import java.util.Scanner;
import java.util.Random;

public class LottoStatistic {
    public static void main(String[] args){
        Scanner input= new Scanner(System.in);
        Random randomGenerator = new Random();

        int lotteryDrawings,randomNumb,indexPos;
        int[][] drawingList;
        int[] frequency=new int[45];
        boolean alreadyExists;
        double percentage;

        //Valedierung
        while (true) {
            System.out.println("Geben Sie die Anzahl der Lottoziehungen an:");
            if (input.hasNextInt()) {
                lotteryDrawings = input.nextInt();
                drawingList = new int[lotteryDrawings][6];
                break;
            }else{
                input.nextLine();
                System.out.print("\nEingabe ungültig,Bitte eine ganze Zahl eingeben!!\n");
            }
        }


        for (int i=0;i<lotteryDrawings;i++){
            indexPos=0;

            while (indexPos<6) {
                randomNumb = randomGenerator.nextInt(45) + 1;

                alreadyExists=false;
                for (int j=0;j<indexPos;j++){
                    if (drawingList[i][j]==randomNumb){     // Prüfung, ob die generierte zahl schon in der aktuellen Ziehung existiert
                        alreadyExists=true;
                        break;
                    }
                }

                if(!alreadyExists){
                    drawingList[i][indexPos]=randomNumb;   //Die Zahl existiert nicht in der aktuellen Ziehung und wird daher in den aktuellen index gespeichert.
                    frequency[randomNumb-1]++;             // Häufigkeits Zähler
                    indexPos++;

                }
            }
        }

        System.out.println("\nHäufigkeit des Vorkommens von Zahlen:");
        for (int i = 0; i < frequency.length; i++) {
            percentage = (frequency[i] / (double) (lotteryDrawings * 6)) * 100;  //Prozent rechnung

            if (percentage>0){
            System.out.printf("Zahl %d: %d-mal (%.2f%%)%n", i + 1, frequency[i], percentage);
            }
        }System.out.print("\nDie Zahlen die nicht vorgekommen sind, werden nicht Angezeigt\n");


        // Ausgabe der Lottoziehungen
        System.out.println("\nAlle Lottoziehungen: \n");
        for(int i=0; i < lotteryDrawings;i++){
            System.out.print("\nZiehung " +(i+1)+": ");
            for(int j=0; j<6;j++){
                System.out.print(drawingList[i][j]);
            }
        }
    input.close();
    }
}
