import java.util.Scanner;
import java.util.Random;


public class CustomerSurvey {
    public static void main(String [] args){
        Scanner input= new Scanner(System.in);
        Random randomGenerator = new Random();

        int testPersonsNumb, rating,count,averageRating,totalRating=0;
        int[] ratingCounts= new int[3];
        String[] ratingDescription = {
                "Nicht empfehlenswert",
                "Akzeptabel",
                "Hervorragend"
        };


        while (true) {
            System.out.println("Geben Sie die Anzahl der Test Personen ein:");
            if (input.hasNextInt()) {
                testPersonsNumb = input.nextInt();
                break;
            }else{
                input.nextLine();
                System.out.print("\nEingabe ungültig,Bitte eine ganze Zahl eingeben!!\n");
            }
        }

        System.out.print("Umfrageergebnisse:\n");

        for (int i=0;i<testPersonsNumb;i++){
            rating = randomGenerator.nextInt(3); //Begrenzung für die Zählrange von 0-2
            ratingCounts[rating]++;
        }

        for (int i =0;i<ratingCounts.length;i++){
            count= ratingCounts[i];
            totalRating += (i + 1) * count;
            System.out.printf("Bewertung %d (%s): %d Stimmen\n",i + 1, ratingDescription[i], count);

        }
        averageRating= totalRating / testPersonsNumb;
        System.out.printf("\nGesamte Anzahl der Test Personen: %d Personen\n",testPersonsNumb);
        System.out.printf("Durchschnitt der Bewertungen liegt bei:  %d (%s)\n\n", averageRating, ratingDescription[averageRating-1]);
        input.close();
    }
}
