package interfaceGUI;

public class ShowDashboard {

    public void showMenu(){

        String[] menuOptions = {
                "1. Album Hinzufügen",
                "2. Track Hinzufügen",
                "3. Track einem Album zuweisen",
                "4. Album Löschen",
                "5. Track aus Album entfernen",
                "6. Track aus gesamter DB löschen",
                "7. Alben Anzeigen lassen",
                "8. Ein Album Anzeigen lassen",
                "9. Programm Beenden",
                "==============================\n"

        };

        System.out.println("\n==============================");
        System.out.println("Album Verwaltung");
        System.out.println("==============================");

        for (String option : menuOptions) {
            System.out.println(option);
        }
        System.out.print("Wähle eine Option: ");
    }

    public void showMessage(String message) {
        System.out.println(message);
    }

    public void showError(String errorMessage) {
        System.err.println(errorMessage);
    }
}

