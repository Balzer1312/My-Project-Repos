import java.util.Scanner;

public class LeapYear {
    public static void main(String[] args){
        Scanner scanner= new Scanner(System.in);

        int year;
        int choice;
        int startYear;
        int endYear;

        while (true) {
            System.out.print("""
                    Schaltjahr filtern\
                    
                    1 für Eingabe auf schaltjahr überprüfen\
                    
                    2 für Schaltjahre filtern\
                    
                    3 für Beenden"""
            );

            System.out.print("\nIhre Eingabe:");
            choice = scanner.nextInt();
            scanner.nextLine();

            if (choice == 3 ){
                break;
            }
            else if(choice < 1 || choice > 4) {
                System.out.println("Ungültige Auswahl. Bitte starten Sie das Programm neu.");
                return;
            }

            switch (choice) {

                case 1:

                    while (true) {
                        System.out.print("\nBitte geben sie das Jahr ein um es zu überprüfen:");
                        year = scanner.nextInt();
                        scanner.nextLine();

                        if (year >= 1000 && year <= 9999) {

                            if ((year % 4 == 0 && year % 100 != 0) || (year % 400 == 0)) {
                                System.out.println("\nDas Jahr " + year + " ist ein Schaltjahr.\n");
                            } else {
                                System.out.println("\nDas Jahr " + year + " ist kein Schaltjahr.\n");
                            }
                            break;
                        } else {
                            System.out.println("Ungültige Eingabe! Bitte geben Sie eine vierstellige Jahreszahl ein.");
                        }
                    }
                    break;

                case 2:

                    while (true){

                        System.out.print("Bitte geben Sie den start und endwert ein," +
                                " um diesen zeitraum auf Schaltjahre zu filtern!" +
                                "\nStartwert: ");
                        startYear=scanner.nextInt();
                        scanner.nextLine();

                        System.out.print("Endwert: ");
                        endYear= scanner.nextInt();
                        scanner.nextLine();

                        if(startYear >= 1000 && startYear <= 9999 && endYear >= 1000 && endYear <= 9999){

                            for (int i = startYear; i <= endYear; i++) {

                                if (i %4 == 0 && i %100 !=0 || i % 400 == 0){
                                    System.out.println(i+ " Ist ein Schaltjahr");
                                }
                            }
                            break;
                        }else{
                            System.out.println("Ungültige Eingabe! Bitte geben Sie eine vierstellige Jahreszahl ein.");
                        }
                    }
                    break;
            }
        }
    }
}

