package FleetManager;

import DisplayOut.ShowDataToDisplay;
import java.util.Scanner;

public class MainMenu {
    private final ShowDataToDisplay showDisplay;
    private final Scanner scanner;
    private final FleetDataManager fleetManager;

    public MainMenu() {
        this.showDisplay = new ShowDataToDisplay();
        this.scanner = new Scanner(System.in);
        this.fleetManager=new FleetDataManager();

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
                    fleetManager.addVehicle(scanner);
                    break;
                case 2:
                    fleetManager.deleteVehicle(scanner);
                    break;
                case 3:
                    fleetManager.showVehicleToDisplay();
                    break;
                case 4:
                    fleetManager.showIndividualVehicleData(scanner);
                    break;
                case 5:
                    fleetManager.addEmployee(scanner);
                    break;
                case 6:
                    fleetManager.rentVehicle(scanner);
                    break;
                case 7:
                    fleetManager.vehicleReturned(scanner);
                    break;
                case 8:
                    fleetManager.showRentalData();
                    break;
                case 9:
                    fleetManager.showIndividualRentData(scanner);
                    break;
                case 10:
                    running = false;
                    showDisplay.showMessage("\nProgramm wird beendet. Auf Wiedersehen!");
                    break;
                default:
                    showDisplay.showError("\ngültige Option! Bitte 1-10 wählen.");
            }
        }
        scanner.close();
    }
}
