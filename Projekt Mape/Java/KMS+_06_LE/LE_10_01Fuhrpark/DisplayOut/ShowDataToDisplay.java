package DisplayOut;
import Rental.RentInfo;
import Vehicles.*;

import java.util.List;

public class ShowDataToDisplay {

    public void showMainMenu() {

        String[] menuOptions ={
                "1. Fahrzeug hinzufügen",
                "2. Fahrzeug entfernen",
                "3. Fahrzeuge anzeigen",
                "4. Einzelne Fahrzuge Anzeigen",
                "5. Mitarbeiter Hinzufügen",
                "6. Fahrzeug Verleih",
                "7. Fahrzeug zurück gebracht",
                "8. Geliehene Fahrzeuge Anzeigen",
                "9. Fahrzeug Leih daten",
                "10. Programm beenden",
        };

        System.out.println("\n==============================");
        System.out.println("Fuhrpark Manager");
        System.out.println("==============================");

        for (String option: menuOptions){
            System.out.println(option);
        }

        System.out.print("Wähle eine Option: ");
    }

    public void showVehicleType(){
        String[] menuOptions ={
                "1. PKW",
                "2. LKW",
                "3. Motorrad",
                "4. Fahrrad",
                "5. Vorgang abbrechen",
        };

        System.out.println("\n==============================");
        System.out.println("Neue Fahrzeuge Eintragen");
        System.out.println("==============================\n");
        System.out.println("Um welches Fahrzeug Handelt es sich: \n");

        for (String option: menuOptions){
            System.out.println(option);
        }

        System.out.print("Wähle eine Option: ");
    }

    public void showFuelType(){
        String[]fuelTypeOption= {
                "1. Benzin",
                "2. Diesel",
                "3. Strom",
        };

        for (String option: fuelTypeOption){
            System.out.println(option);
        }
        System.out.print("Wähle eine Option: ");
    }

    public void showMessage(String message) {
        System.out.println(message);
    }

    public void showError(String errorMessage) {
        showMessage(errorMessage);
    }

    public void showFleetData(List<Vehicle> vehicles) {
        if (vehicles.isEmpty()) {
            System.out.println("Der Fuhrpark ist aktuell leer.");
            return;
        }
        System.out.println("\nFuhrpark:");
        System.out.println("Gesamt Zahl der Fahrzeuge: "+Vehicle.vehicleCount);
        for (Vehicle v : vehicles) {
            System.out.println(v);
        }
    }

    public void showCurrentRentalVehicle(List<RentInfo>rentInfos){
        if (rentInfos.isEmpty()) {
            System.out.println("Der Fuhrpark ist aktuell leer.");
            return;
        }
        System.out.println("\nGeliehene Fahrzeuge:\n");
        for (RentInfo ri : rentInfos) {
            if (ri.getDateTo()==null){
                System.out.println("Vorgangs ID"+ri.getRentalId() +"\n" +"Fahrzeug ID: "+ri.getVehicleId()+"\n"+"Marke: "+ri.getBrand()+"\n"+"Modell: "+ri.getModel()+"\n");
            }
        }
    }

    public void showVehiclesInfos(List<Vehicle> vehicles){
        if (vehicles.isEmpty()) {
            System.out.println("Der Fuhrpark ist aktuell leer.");
            return;
        }
        System.out.println("\nFuhrpark:");
        System.out.println("Gesamt Zahl der Fahrzeuge: "+Vehicle.vehicleCount);
        for (Vehicle v : vehicles) {
            System.out.println("Fahrzeug ID: "+v.getVehicleId()+"\n"+"Marke: "+v.getBrand()+"\n"+"Modell: "+v.getModel()+"\n");
        }
    }

    public void showRentalInfos(List<RentInfo> rentInfos){
        if (rentInfos.isEmpty()) {
            System.out.println("Der Fuhrpark ist aktuell leer.");
            return;
        }
        System.out.println("\nGeliehene Fahrzeuge:\n");
        for (RentInfo ri : rentInfos) {
            System.out.println("Vorgangs ID: "+ri.getRentalId() +"\n" +"Fahrzeug ID: "+ri.getVehicleId()+"\n"+"Marke: "+ri.getBrand()+"\n"+"Modell: "+ri.getModel()+"\n");
        }
    }

    public void showTotalRentalData(List<RentInfo>rentInfos){
        if (rentInfos.isEmpty()) {
            System.out.println("Keine Daten von Verleih vorhanden.");
            return;
        }
        System.out.println("\nGeliehene Fahrzeuge:");
        for (RentInfo ri : rentInfos) {
            System.out.println(ri);
        }
    }

    public void showVehiclesAvailableRent(List<Vehicle> vehicles){
        if (vehicles.isEmpty()) {
            System.out.println("Der Fuhrpark ist aktuell leer.");
            return;
        }
        System.out.println("\nVerfügbare Fahrzeuge:\n");
        for (Vehicle v : vehicles) {
            if (v.getRentStatus()){
            System.out.println("Fahrzeug ID: "+v.getVehicleId()+"\n"+"Marke: "+v.getBrand()+"\n"+"Modell: "+v.getModel()+"\n");
            }
        }
    }
}

