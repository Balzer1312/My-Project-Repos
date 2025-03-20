package musicManager;
import java.util.Scanner;
import java.util.Set;
import interfaceGUI.ShowDashboard;

public class ValdiDataMusic {
    private final ShowDashboard showDashboard;

    public ValdiDataMusic() {
        this.showDashboard = new ShowDashboard();
    }

    public String getString(Scanner scanner, String prompt){
        String data;
        showDashboard.showMessage(prompt);
        data = scanner.nextLine();

        return data;
    }

    public int getInt(Scanner scanner,String prompt){

        while (true) {
            try {
                showDashboard.showMessage(prompt);
                return Integer.parseInt(scanner.nextLine().trim());
            } catch (NumberFormatException e) {
                showDashboard.showError("\nUngültige Eingabe! Bitte eine Zahl eingeben.");
            }
        }
    }

    public int idCheck(Scanner scanner, String prompt, Set<Integer> validIds) {
        int id;

        while (true) {
            try {
                id = getInt(scanner, prompt);
                if (validIds.contains(id)) {
                    return id;
                } else {
                    showDashboard.showError("Diese ID existiert nicht. Bitte erneut eingeben.");
                }
            } catch (Exception e) {
                showDashboard.showError("Ungültige Eingabe! Bitte eine Zahl eingeben.");
                scanner.nextLine();
            }
        }
    }
}
