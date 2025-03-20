package administration;
import modelsClass.Member;

import java.util.ArrayList;
import java.util.List;

public class DisplayShow {

    public void showMainMenu() {
        System.out.println("\n==============================");
        System.out.println("Vereins Verwaltung");
        System.out.println("==============================");
        System.out.println("1. Mitglied Hinzufügen");
        System.out.println("2. Mitglied Entfernen");
        System.out.println("3. Team Erstellen");
        System.out.println("4. Team Auflösen");
        System.out.println("5. Mitglieder anzeigen");
        System.out.println("6. Programm beenden");
        System.out.print("Wähle eine Option: ");
    }

    public void showMemberType(){
        System.out.println("\nWelchen Typ von Mitglied möchten Sie erstellen?");
        System.out.println("1. Manager");
        System.out.println("2. Schatzmeister");
        System.out.println("3. Trainer");
        System.out.println("4. Spieler");
    }

    public void showMessage(String message) {
        System.out.println(message);
    }

    public void showError(String errorMessage) {
        System.err.println(errorMessage);
    }

}
