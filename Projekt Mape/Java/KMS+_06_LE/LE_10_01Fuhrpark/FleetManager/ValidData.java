package FleetManager;

import DisplayOut.ShowDataToDisplay;
import Rental.RentInfo;
import Vehicles.Employee;
import Vehicles.Vehicle;
import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.time.format.DateTimeParseException;
import java.util.List;
import java.util.Scanner;

public class ValidData {
    private final ShowDataToDisplay showDataToDisplay;
    private final DateTimeFormatter dateFormat;

    public ValidData() {
        this.showDataToDisplay = new ShowDataToDisplay();
        this.dateFormat = DateTimeFormatter.ofPattern("dd.MM.yyyy");
    }


    public int getExistVehicleID(Scanner scanner, String prompt, List<Vehicle> vehicles){
        while (true) {
            showDataToDisplay.showMessage(prompt);
            int inputId;
            try {
                inputId = Integer.parseInt(scanner.nextLine().trim());
            } catch (NumberFormatException e) {
                showDataToDisplay.showMessage("Bitte eine gültige Zahl eingeben.");
                continue;
            }

            boolean found = false;
            for (Vehicle v : vehicles) {
                if (v.getVehicleId() == inputId) {
                    found = true;
                    break;
                }
            }
            if (found) {

                return inputId;
            } else {
                showDataToDisplay.showMessage("Es existiert kein Fahrzeug mit der ID " + inputId + ". Bitte erneut versuchen.");
            }
        }

    }

    public int getExistEmployeeID(Scanner scanner, String prompt, List<Employee> employees){
        while (true) {
            showDataToDisplay.showMessage(prompt);

            int inputId;
            try {
                inputId = Integer.parseInt(scanner.nextLine().trim());
            } catch (NumberFormatException e) {
                showDataToDisplay.showMessage("Bitte eine gültige Zahl eingeben.");
                continue;
            }

            boolean found = false;
            for (Employee e : employees) {
                if (e.getEmployeeId() == inputId) {
                    found = true;
                    break;
                }
            }
            if (found) {

                return inputId;
            } else {
                showDataToDisplay.showMessage("Es existiert kein Fahrzeug mit der ID " + inputId + ". Bitte erneut versuchen.");
            }
        }
    }

    public int getExistingAktivRentalID(Scanner scanner, String prompt, List<RentInfo>rentInfos){
        while (true) {
            showDataToDisplay.showMessage(prompt);

            int inputId;
            try {
                inputId = Integer.parseInt(scanner.nextLine().trim());
            } catch (NumberFormatException e) {
                showDataToDisplay.showMessage("Bitte eine gültige Zahl eingeben.");
                continue;
            }

            boolean found = false;

            for (RentInfo ri : rentInfos) {
                if (ri.getRentalId() == inputId && ri.getDateTo() == null) {
                    found = true;
                    break;
                }
            }
            if (found) {

                return inputId;
            } else {
                showDataToDisplay.showMessage("Es existiert kein Leihvorgang mit der ID oder das Fahrzeug wurde schon zurück gebracht.\n Bitte erneut versuchen.");
            }
        }
    }

    public int getExistingRentalData(Scanner scanner, String prompt,List<RentInfo> rentInfos){
        while (true) {
            showDataToDisplay.showMessage(prompt);

            int inputId;
            try {
                inputId = Integer.parseInt(scanner.nextLine().trim());
            } catch (NumberFormatException e) {
                showDataToDisplay.showMessage("Bitte eine gültige Zahl eingeben.");
                continue;
            }

            boolean found = false;

            for (RentInfo ri : rentInfos) {
                if (ri.getRentalId() == inputId) {
                    found = true;
                    break;
                }
            }
            if (found) {

                return inputId;
            } else {
                showDataToDisplay.showMessage("Es existiert kein Leihvorgang mit der ID: "+inputId);
            }
        }
    }

    public String getfuelType(Scanner scanner){

        int choice;

        showDataToDisplay.showFuelType();

        while (true){
            choice=getInt(scanner,"Wähle eine Option (1-3): ");
            if (choice >= 1 && choice <= 3) {
                break;
            }else {
               showDataToDisplay.showError("\nUngültige Eingabe!");
            }
        }

        return switch (choice) {
            case 1 -> "Benzin";
            case 2 -> "Diesel";
            case 3 -> "Strom";
            default -> null;
        };

    }

    public String getDateForm(Scanner scanner,String prompt){
        //"Geburtsdatum (DD.MM.YYYY) eingeben: "
        LocalDate date;
        while (true) {
            showDataToDisplay.showMessage(prompt);
            try {
                date = LocalDate.parse(scanner.nextLine(),dateFormat);
                break;
            } catch (DateTimeParseException e) {
                showDataToDisplay.showError("Ungültiges Format! Bitte im Format DD.MM.YYYY eingeben.");
            }
        }
        return date.toString();
    }

    public String getString(Scanner scanner, String prompt){
        String data;
        showDataToDisplay.showMessage(prompt);
        data = scanner.nextLine();

        return data;
    }

    public int getInt(Scanner scanner,String prompt){

        while (true) {
            try {
                showDataToDisplay.showMessage(prompt);
                return Integer.parseInt(scanner.nextLine().trim());
            } catch (NumberFormatException e) {
                showDataToDisplay.showError("\nUngültige Eingabe! Bitte eine Zahl eingeben.");
            }
        }
    }

    public double getDouble(Scanner scanner,String prompt) {
        while (true) {
            System.out.print(prompt);
            try {
                return Double.parseDouble(scanner.nextLine().trim());
            } catch (NumberFormatException e) {
                System.out.println("\nUngültige Eingabe! Bitte eine Kommazahl eingeben.");
            }
        }
    }

    public String isValidName(Scanner scanner,String prompt) {
        String name;
        while (true) {
            showDataToDisplay.showMessage(prompt);
            name = scanner.nextLine().trim();
            if (name.matches("[a-zA-ZäöüÄÖÜß\\-']+") ) {
                break;
            }else{
                showDataToDisplay.showError("Ungültiger Name! Bitte nur Buchstaben verwenden.");
            }
        }
        return name;
    }

    public Vehicle findVehicleById(int searchId, List<Vehicle> vehicles) {
        for (Vehicle v : vehicles) {
            if (v.getVehicleId() == searchId) {
                return v;
            }
        }

        return null;
    }

    public RentInfo findRentalInfoByID(int searchId,List<RentInfo> rentInfos){
        for(RentInfo ri : rentInfos){
            if(ri.getRentalId()==searchId){
                return ri;            }
        }
        return null;
    }


}
