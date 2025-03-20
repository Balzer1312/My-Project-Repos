package manager;

import models.Vehicle;
import java.util.List;

public class ShowDataToDisplay {

    public void showMainMenu() {
        System.out.println("\n==============================");
        System.out.println("Fuhrpark Manager");
        System.out.println("==============================");
        System.out.println("1. Fahrzeug hinzufügen");
        System.out.println("2. Fahrzeug entfernen");
        System.out.println("3. Fahrzeuge anzeigen");
        System.out.println("4. Fahrzeug Tanken");
        System.out.println("5. Fahrzeug Verlei");
        System.out.println("6. Kilometerstand");
        System.out.println("7. Programm beenden");
        System.out.print("Wähle eine Option: ");
    }
    public void showMessage(String message) {
        System.out.println(message);
    }

    public void showError(String errorMessage) {
        System.err.println(errorMessage);
    }

    public void showFleetData(List<Vehicle> vehicles) {
        if (vehicles.isEmpty()) {
            showMessage("Der Fuhrpark ist aktuell leer.");
            return;
        }
        System.out.println("\nFuhrpark:");
        System.out.println("Gesamt Zahl der Fahrzeuge: "+Vehicle.vehicleCount);
        for (Vehicle v : vehicles) {
            System.out.println(v);;
        }
    }
}

