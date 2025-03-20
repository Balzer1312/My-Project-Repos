package manager;

import java.util.List;
import models.*;
import java.util.Scanner;


public class ValidFleetData {

    // Fahrzeug Objekt wird erstellt
   public Vehicle createVehicle(Scanner scanner,List<Vehicle> vehicles){
       int serialID;
       String brand,model,color,fuelType;
       boolean status = true;

       System.out.println("\nNeues Fahrzeug hinzufügen:");

       int typeChoice;
       while (true) {
           System.out.println("Bitte wählen Sie einen Fahrzeugtyp:");
           System.out.println("1. Car");
           System.out.println("2. Truck");
           System.out.println("3. Motorcycle");
           System.out.println("4. Bicycle");
           System.out.print("Ihre Auswahl: ");

           typeChoice = readInt("",scanner);  // Methode validiert die Eingabe
           if (typeChoice >= 1 && typeChoice <= 4) {
               break;
           }
           System.out.println("\nUngültige Auswahl! Bitte 1-4 wählen.");
       }

       while (true) {
           serialID = readInt("\nSerien Nummer: ", scanner);
           if (idCheck(serialID, vehicles)) {
               break;
           } else {
               System.out.println("\nDiese Serien Nummer existiert bereits! Bitte eine andere eingeben.");
           }
       }

       brand = readString("Marke: ",scanner);
       model = readString("Modell: ",scanner);
       color = readString("Farbe: ",scanner);

       return switch (typeChoice) {
           case 1 ->{
               fuelType = selectFuelType(scanner);
              yield  new Car(serialID, brand, model, color, status,fuelType,
                   readString("Kennzeichen: ",scanner),
                   readDouble("Verbrauch (l/100km): ",scanner),
                   readInt("Kilometerstand: ",scanner),readInt("Türen: ",scanner));
           }

           case 2 ->{
               fuelType = selectFuelType(scanner);
               yield  new Truck(serialID, brand, model, color, status,fuelType,
                   readString("Kennzeichen: ",scanner),
                   readDouble("Verbrauch (l/100km): ",scanner),
                   readInt("Kilometerstand: ",scanner),readInt("Ladekapazität (kg): ",scanner));
           }

           case 3 ->{
               fuelType = selectFuelType(scanner);
               yield  new Motorcycle(serialID, brand, model, color, status,fuelType,
                   readString("Kennzeichen: ",scanner),
                   readDouble("Verbrauch (l/100km): ",scanner),
                   readInt("Kilometerstand: ",scanner),readInt("Motorgröße (cc): ",scanner));
           }

           case 4 -> new Bicycle(serialID, brand, model, color, status,readInt("Radgröße: ",scanner));


           default -> null;
       };
   }


   //##################### Eingabe Valedierungen und id Check ########################################
    public int readInt(String prompt,Scanner scanner) {
        while (true) {
            System.out.print(prompt);
            try {
                return Integer.parseInt(scanner.nextLine().trim());
            } catch (NumberFormatException e) {
                System.out.println("\nUngültige Eingabe! Bitte eine Zahl eingeben.");
            }
        }
    }

    private double readDouble(String prompt,Scanner scanner) {
        while (true) {
            System.out.print(prompt);
            try {
                return Double.parseDouble(scanner.nextLine().trim());
            } catch (NumberFormatException e) {
                System.out.println("\nUngültige Eingabe! Bitte eine Kommazahl eingeben.");
            }
        }
    }

    private String readString(String prompt,Scanner scanner) {
        System.out.print(prompt);
        return scanner.nextLine().trim();
    }

    public boolean idCheck(int id ,List<Vehicle> vehicles){
        for (Vehicle v : vehicles) {
            if (v.getSerialID() == id) {
                return false;
            }
        }
        return true;
    }

    private String selectFuelType(Scanner scanner) {
        while (true) {
            System.out.println("\nBitte wählen Sie eine Treibstoffart:");
            System.out.println("1. Benzin");
            System.out.println("2. Diesel");
            System.out.println("3. Strom");
            System.out.print("Ihre Auswahl: ");

            int choice;
            try {
                choice = Integer.parseInt(scanner.nextLine().trim());
            } catch (NumberFormatException e) {
                System.out.println("\nUngültige Eingabe! Bitte eine Zahl von 1 bis 3 wählen.");
                continue;
            }

            switch (choice) {
                case 1 -> { return "Benzin"; }
                case 2 -> { return "Diesel"; }
                case 3 -> { return "Strom"; }
                default -> System.out.println("\nUngültige Auswahl! Bitte erneut versuchen.");
            }
        }
    }

}



