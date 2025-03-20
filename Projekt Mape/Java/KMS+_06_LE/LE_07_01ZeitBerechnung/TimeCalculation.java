import java.time.LocalDate;
import java.time.LocalTime;
import java.time.Duration;
import java.time.format.DateTimeFormatter;
import java.time.format.DateTimeParseException;
import java.util.Scanner;

public class TimeCalculation {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        DateTimeFormatter timeFormat= DateTimeFormatter.ofPattern("HH:mm");
        DateTimeFormatter dateFormat= DateTimeFormatter.ofPattern("dd.MM.yyyy");

        LocalTime workBeginTime;
        LocalTime endOfWorkTime;
        Duration durationOfWork;
        LocalDate orderDate;
        LocalDate deliveryDate;
        int choice,deliveryTime;


        while (true) {
            System.out.print("""
                    Zeiten berechnen\
                    
                    1 für Arbeitszeit berechnen\
                    
                    2 für Lieferzeit berechnen\
                    
                    3 für Beenden"""
            );

            while (true) {
                System.out.print("\n\nIhre Wahl: ");
                if (input.hasNextInt()) {
                    choice = input.nextInt();
                    input.nextLine();
                    if (choice>3 || choice==0){
                        System.out.println("Ungültige Auswahl!");
                        continue;
                    }
                    break;
                } else {
                    System.out.println("Ungültige Eingabe! Bitte eine Zahl eingeben.");
                    input.nextLine();
                }
            }
            switch(choice) {

                // Arbeitszeit berechnen
                case 1:
                    System.out.print("\nWann haben Sie ihre arbeit begonnen?\n\n");
                    while (true) {
                        try {
                            System.out.print("Bitte geben sie die Uhrzeit für den Arbeitsbeginn ein.\n(Format: HH:mm): ");
                            workBeginTime = LocalTime.parse(input.nextLine(), timeFormat);
                            break;
                        } catch (DateTimeParseException e) {
                            System.out.println("Ungültige Uhrzeit!\n\n");
                        }
                    }

                    while (true) {
                        try {
                            System.out.print("Bitte geben sie die Uhrzeit für das Arbeitsende ein.\n(Format: HH:mm): ");
                            endOfWorkTime = LocalTime.parse(input.nextLine(), timeFormat);
                            break;
                        } catch (DateTimeParseException e) {
                            System.out.println("Ungültige Uhrzeit!\n\n");
                        }
                    }

                    durationOfWork = Duration.between(workBeginTime, endOfWorkTime);
                    System.out.printf("Heutige Arbeitszeit: %d Std und %d min .\n\n", durationOfWork.toHours(), durationOfWork.toMinutesPart());

                    // Lieferzeit berechnen
                case 2:
                    while (true) {
                        try {
                            System.out.print("Bestelldatum (DD.MM.YYYY): ");
                            orderDate = LocalDate.parse(input.nextLine(), dateFormat);
                            break;
                        } catch (DateTimeParseException e) {
                            System.out.println("Ungültiges Datumsformat!");
                        }
                    }
                    while (true) {
                        try {
                            System.out.print("Lieferdatum (DD.MM.YYYY): ");
                            deliveryDate = LocalDate.parse(input.nextLine(), dateFormat);
                            if (deliveryDate.isBefore(orderDate)) {
                                System.out.println("Das Lieferdatum kann nicht vor dem Bestelldatum liegen!");
                                continue;
                            }
                            break;
                        } catch (DateTimeParseException e) {
                            System.out.println("Ungültiges Datumsformat!");
                        }
                    }
                    deliveryTime = (int) java.time.temporal.ChronoUnit.DAYS.between(orderDate, deliveryDate);
                    if (deliveryTime > 0) {
                        System.out.printf("Die Lieferzeit beträgt: %d Tage.%n", deliveryTime);
                    } else {
                        System.out.println("Die Lieferung sollte heute eintreffen!");
                    }

                    //Program beenden
                case 3:
                    System.out.println("Programm wird beendet..");
                    input.close();
                    return;
            }
        }
    }
}
