package bankManager;

import dashboardGUI.ShowDisplay;

import java.util.Scanner;

public class Dashboard {
    private final ShowDisplay showDisplay;
    private final BankManager bankManager;

    public Dashboard(){
        this.showDisplay = new ShowDisplay();
        this.bankManager = new BankManager();
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
                    bankManager.createAccount(scanner);
                    break;
                case 2:
                    bankManager.deleteAccount(scanner);
                    break;
                case 3:
                    bankManager.transferMoney(scanner);
                    break;
                case 4:
                    bankManager.accountWithdraw(scanner);
                    break;
                case 5:
                    bankManager.accountDeposit(scanner);
                    break;
                case 6:
                    bankManager.displayAllAccounts();
                    break;
                case 7:
                    bankManager.displayAccount(scanner);
                    break;
                case 8:
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

