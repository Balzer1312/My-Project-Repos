package ClubAdminsitration;

import GUI.DataToDisplay;
import java.util.Scanner;


public class Menu {
    private final DataToDisplay showDisplay;
    private final Scanner scanner;
    private final MemberAdministration administration;

    public Menu() {
        this.showDisplay = new DataToDisplay();
        this.scanner = new Scanner(System.in);
        this.administration = new MemberAdministration();
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
                    administration.addMember(scanner);
                    break;
                case 2:
                    administration.deleteMember(scanner);
                    break;
                case 3:
                    administration.updateMemberData(scanner);
                    break;
                case 4:
                    administration.showAllMember();
                    break;
                case 5:
                    administration.showOneMember(scanner);
                    break;
                case 6:
                    administration.createNewTeam(scanner);
                    break;
                case 7:
                    administration.deleteTeam(scanner);
                    break;
                case 8:
                    administration.assignMemberToTeam(scanner);
                    break;
                case 9:
                    administration.showTeam();
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
