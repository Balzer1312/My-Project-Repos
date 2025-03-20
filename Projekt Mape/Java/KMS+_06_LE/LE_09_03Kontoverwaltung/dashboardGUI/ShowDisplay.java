package dashboardGUI;

public class ShowDisplay {

    public void showMainMenu() {
        String[] menuOptions = {
                "1. Bankkonto erstellen",
                "2. Bankkonto Löschen",
                "3. Überweisung",
                "4. Auszahlung",
                "5. Einzahlung",
                "6. Bankkonten Ausgeben",
                "7. Ein Bankkonto Ausgeben",
                "8. Programm Beenden"
        };

        System.out.println("\n==============================");
        System.out.println("Bankkonto verwaltung");
        System.out.println("==============================");

        for (String option: menuOptions){
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
