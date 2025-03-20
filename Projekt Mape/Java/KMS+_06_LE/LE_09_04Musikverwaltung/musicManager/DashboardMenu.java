package musicManager;

import interfaceGUI.ShowDashboard;
import java.util.Scanner;

public class DashboardMenu {
    private final ShowDashboard showDashboard;
    private final AlbumTrackManager manager;

    public DashboardMenu() {
        this.showDashboard = new ShowDashboard();
        this.manager = new AlbumTrackManager();
    }

    public void startMenu() {

        Scanner scanner = new Scanner(System.in);
        boolean running = true;
        int choice;

        while (running) {

            showDashboard.showMenu();

            try {
                choice = Integer.parseInt(scanner.nextLine());
            } catch (NumberFormatException e) {
                showDashboard.showError("\nUngültige Eingabe! Bitte eine Zahl eingeben.");
                continue;
            }

            switch (choice) {
                case 1:
                    manager.createAlbum(scanner);
                    break;
                case 2:
                    manager.crateTrack(scanner);
                    break;
                case 3:
                    manager.assignTrackToAlbum(scanner);
                    break;
                case 4:
                    manager.deleteAlbum(scanner);
                    break;
                case 5:
                    manager.deleteTrackFromAlbum(scanner);
                    break;
                case 6:
                    manager.deleteTrack(scanner);
                    break;
                case 7:
                    manager.showAlbumOnDisplay();
                    break;
                case 8:
                    manager.showChoiceAlbum(scanner);
                    break;
                case 9:
                    running = false;
                    showDashboard.showMessage("\nProgramm wird beendet. Auf Wiedersehen!");
                    break;
                default:
                    showDashboard.showError("\ngültige Option! Bitte 1-8 wählen.");
            }
        }
        scanner.close();
    }
}
