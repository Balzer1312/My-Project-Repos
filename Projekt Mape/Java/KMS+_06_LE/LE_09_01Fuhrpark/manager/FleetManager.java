package manager;

import models.*;
import java.util.*;

public class FleetManager {
    private final List<Vehicle> vehicles;
    private final ShowDataToDisplay showDisplay;
    private final Scanner scanner;

    public FleetManager() {
        this.vehicles = new ArrayList<>();
        this.showDisplay = new ShowDataToDisplay();
        this.scanner = new Scanner(System.in);

    }
    public void startMenu() {
        boolean running = true;

        while (running) {
            // Menü anzeigen
            showDisplay.showMainMenu();


            int choice;
            try {
                choice = Integer.parseInt(scanner.nextLine());
            } catch (NumberFormatException e) {
                showDisplay.showError("\nUngültige Eingabe! Bitte eine Zahl eingeben.");
                continue;
            }

            switch (choice) {
                case 1:
                    addVehicle();
                    break;
                case 2:
                    removeVehicle();
                    break;
                case 3:
                    showDisplay.showFleetData(getVehicles());
                    break;
                case 4:
                    refuelVehicle();
                    break;
                case 5:
                    rentVehicle();
                    break;
                case 6:
                    updateMileage();
                    break;
                case 7:
                    running = false;
                    showDisplay.showMessage("\nProgramm wird beendet. Auf Wiedersehen!");
                    break;
                default:
                    showDisplay.showError("\ngültige Option! Bitte 1-7 wählen.");
            }
        }
        scanner.close();
    }

    // Fahrzeug Hinzufügen
    public void addVehicle() {
        ValidFleetData dataInput = new ValidFleetData();
        Vehicle newVehicle = dataInput.createVehicle(scanner,getVehicles());

        if (newVehicle != null) {
            vehicles.add(newVehicle);
            showDisplay.showMessage("\nFahrzeug erfolgreich zur Flotte hinzugefügt!");
        } else {
            showDisplay.showError("\nFahrzeug konnte nicht erstellt werden.");
        }
    }

    // Fahrzeug entfernen
    public void removeVehicle(){
        ValidFleetData dataInput = new ValidFleetData();
        int removeID;
        boolean existID;

        removeID = dataInput.readInt("\nBitte geben sie die Fahrzeug Serien Nummer ein oder :  ",scanner);
        existID= dataInput.idCheck(removeID,getVehicles());

       if (existID){
           showDisplay.showError("\nFahrzeug ID exestiert nicht!");
       }else {
           for (Vehicle v : vehicles){
               if (v.getSerialID()==removeID){
                   vehicles.remove(v);
                   showDisplay.showMessage("\nFahrzeug wurde erfolgreich gelöscht!");
                   break;
               }
           }
       }
    }

    // Fahrzeug Tanken
    public void refuelVehicle() {
        String fuelType;
        int serialID;
        double amount;

        if (vehicles.isEmpty()) {
            showDisplay.showMessage("\nDer Fuhrpark ist leer. Kein Fahrzeug zum Tanken verfügbar.");
            return;
        }

        showDisplay.showMessage("\nBitte Seriennummer des zu tankenden Fahrzeugs eingeben:");
        try {
            serialID = Integer.parseInt(scanner.nextLine().trim());
        } catch (NumberFormatException e) {
            showDisplay.showError("\nUngültige Seriennummer! Bitte eine Zahl eingeben.");
            return;
        }

        // Fahrzeug mit passender Seriennummer suchen
        for (Vehicle v : vehicles) {
            if (v.getSerialID() == serialID) {
                if (v instanceof Motorized motorizedVehicle) {
                    fuelType = motorizedVehicle.getFuelType();
                    showDisplay.showMessage("\nGeben Sie die Menge an Treibstoff ein:");
                    try {
                        amount = Double.parseDouble(scanner.nextLine().trim());
                    } catch (NumberFormatException e) {
                        showDisplay.showError("\nUngültige Menge! Bitte eine Zahl eingeben.");
                        return;
                    }

                    motorizedVehicle.refuel(amount,fuelType);
                } else {
                    showDisplay.showError("\nDieses Fahrzeug ist nicht motorisiert und kann nicht betankt werden!");
                }
                return;
            }
        }
        showDisplay.showError("\nKein Fahrzeug mit dieser Seriennummer gefunden!");
    }

    // Fahrzeug status änderen
    public void rentVehicle() {
        boolean currentStatus;
        String statusText;
        int serialID;

        if (vehicles.isEmpty()) {
            showDisplay.showMessage("\nDer Fuhrpark ist leer. Kein Fahrzeug zum Verleihen verfügbar.");
            return;
        }

        showDisplay.showMessage("\nBitte Seriennummer des zu verleihenden Fahrzeugs eingeben:");
        try {
            serialID = Integer.parseInt(scanner.nextLine().trim());
        } catch (NumberFormatException e) {
            showDisplay.showError("\nUngültige Seriennummer! Bitte eine Zahl eingeben.");
            return;
        }

        // Fahrzeug mit passender Seriennummer suchen
        for (Vehicle v : vehicles) {
            if (v.getSerialID() == serialID) {
                currentStatus = v.isStatus();
                v.setStatus(!currentStatus); // ✅ Status umkehren (verfügbar ↔ verliehen)

                statusText = v.isStatus() ? "\nVerfügbar" : "Verliehen";
                showDisplay.showMessage("Fahrzeugstatus geändert: " + statusText);
                return;
            }
        }

        showDisplay.showError("\nKein Fahrzeug mit dieser Seriennummer gefunden!");
    }

    // Aktualisieren des Kilometerstands
    public void updateMileage() {
        int newMileage,serialID;

        if (vehicles.isEmpty()) {
            showDisplay.showMessage("\nDer Fuhrpark ist leer. Kein Fahrzeug zum Aktualisieren des Kilometerstands verfügbar.");
            return;
        }

        showDisplay.showMessage("\nBitte Seriennummer des Fahrzeugs eingeben, dessen Kilometerstand aktualisiert werden soll:");
        try {
            serialID = Integer.parseInt(scanner.nextLine().trim());
        } catch (NumberFormatException e) {
            showDisplay.showError("\nUngültige Seriennummer! Bitte eine Zahl eingeben.");
            return;
        }

        // Fahrzeug mit passender Seriennummer suchen
        for (Vehicle v : vehicles) {
            if (v.getSerialID() == serialID) {
                if (v instanceof Motorized motorizedVehicle) {
                    showDisplay.showMessage("\nAktueller Kilometerstand: " + motorizedVehicle.getMileage());
                    showDisplay.showMessage("Neuen Kilometerstand eingeben:");
                    try {
                        newMileage = Integer.parseInt(scanner.nextLine().trim());
                    } catch (NumberFormatException e) {
                        showDisplay.showError("\nUngültige Eingabe! Bitte eine Zahl eingeben.");
                        return;
                    }

                    motorizedVehicle.setMileage(newMileage);
                    showDisplay.showMessage("\nKilometerstand erfolgreich aktualisiert!");
                } else {
                    showDisplay.showError("\nDieses Fahrzeug ist nicht motorisiert und hat keinen Kilometerstand.");
                }
                return;
            }
        }

        showDisplay.showError("\nKein Fahrzeug mit dieser Seriennummer gefunden!");
    }

    //Referenz auf die Liste ohne sie bearbeiten zu können.
    public List<Vehicle> getVehicles() {
        return vehicles;
    }

}
