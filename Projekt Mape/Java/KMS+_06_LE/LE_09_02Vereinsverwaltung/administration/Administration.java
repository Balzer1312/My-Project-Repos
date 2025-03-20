package administration;

import java.util.*;
import modelsClass.*;


public class Administration {
    private final DisplayShow showDisplay;
    private final ValidMemberData validData;

    public Administration() {
        this.showDisplay= new DisplayShow();
        this.validData = new ValidMemberData();
    }

    public void startMenu() {
        Scanner scanner = new Scanner(System.in);
        boolean running = true;
        int choice;

        while (running) {
            // Menü anzeigen
            showDisplay.showMainMenu();



            try {
                choice = Integer.parseInt(scanner.nextLine());
            } catch (NumberFormatException e) {
                showDisplay.showError("\nUngültige Eingabe! Bitte eine Zahl eingeben.");
                continue;
            }

            switch (choice) {
                case 1:
                    validData.createMember(scanner);
                    break;
                case 2:
                    validData.deleteMember(scanner);
                    break;
                case 3:
                    validData.createTeam(scanner);
                    break;
                case 4:
                    validData.deleteTeam(scanner);
                    break;
                case 5:
                    validData.displayMembers();
                    break;
                case 6:
                    running = false;
                    showDisplay.showMessage("\nProgramm wird beendet. Auf Wiedersehen!");
                    break;
                default:
                    showDisplay.showError("\ngültige Option! Bitte 1-7 wählen.");
            }
        }
        scanner.close();
    }
}

