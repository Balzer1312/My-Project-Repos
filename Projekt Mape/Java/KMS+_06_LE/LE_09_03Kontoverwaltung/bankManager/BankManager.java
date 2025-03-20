package bankManager;


import java.math.BigDecimal;
import java.time.LocalDate;
import java.util.*;
import bankClass.BankAccount;
import dashboardGUI.ShowDisplay;


public class BankManager {
    private final List<BankAccount> accounts;
    private final ShowDisplay toDisplay;
    private final ValidDataClass validData;

    public BankManager() {
        this.accounts = new ArrayList<>();
        this.toDisplay = new ShowDisplay();
        this.validData = new ValidDataClass();
    }

    // Account erstellen
    public void createAccount(Scanner scanner){
        BankAccount newAccount;

        int accountID = validData.newAccountIDCheck(scanner,accounts);
        String firstname= validData.isValidName(scanner,"Vorname eingeben: ");
        String lastname= validData.isValidName(scanner,"Nachnamen eingeben :");
        String iban= validData.ibanGenerator(accounts);
        LocalDate birth= validData.dateCheck(scanner,"Geburtsdatum (DD.MM.YYYY) eingeben: ");
        String address= validData.addressCheck(scanner,"Bitte Adresse angeben:");
        BigDecimal value= BigDecimal.valueOf(0.00);

        newAccount=new BankAccount(accountID,firstname,lastname,birth,address,iban,value);

        accounts.add(newAccount);
    }


    // Account Löschen
    public void deleteAccount(Scanner scanner){

        int accountID = validData.readInt(scanner,"Account-ID zum Löschen eingeben: ");
        boolean removed= accounts.removeIf(t -> t.getAccountID()==accountID);
        if (removed) {
            toDisplay.showMessage("Mitglied mit ID " + accountID + " wurde erfolgreich gelöscht.");
            BankAccount.accountCount--;
        } else {
            toDisplay.showError("Kein Mitglied mit dieser ID gefunden.");
        }

    }


    // Bank Transfer
    public void transferMoney(Scanner scanner) {

        if (accounts.size() < 2) {
            toDisplay.showError("Es gibt noch zu wenig Konten!");
            return;
        }

        int sourceAccountID = validData.accountExistCheck(scanner, accounts,"\nÜberweißung:\n\nBitte ihre Account-ID eingeben: ");
        int targetAccountID = validData.accountExistCheck(scanner, accounts,"Empfänger-ID eingeben: ");
        BigDecimal amount = validData.transferAmountCheck(scanner,sourceAccountID,accounts);

        toDisplay.showMessage("Wollen Sie die Überweisung fortsetzen?\n1. Nein\nBeliebige Eingabe für Ja: ");
        if (scanner.hasNextInt() && scanner.nextInt() == 1) {
            toDisplay.showMessage("Überweisung abgebrochen.");
            return;
        }
        scanner.nextLine();

        // Überweisung durchführen
        if (validData.transferMoney(sourceAccountID, targetAccountID, amount, accounts)) {
            toDisplay.showMessage("Überweisung erfolgreich! " + amount + "€ von Konto "
                    + sourceAccountID + " zu Konto " + targetAccountID + " überwiesen.");
        } else {
            toDisplay.showError("Überweisung fehlgeschlagen!");
        }
    }


    // Geld Abheben
    public void accountWithdraw(Scanner scanner){
        validData.withdraw(scanner,accounts);
    }


    // Geld Einzahlen
    public void accountDeposit(Scanner scanner){
        validData.deposit(scanner,accounts);
    }


    // Alle Konten Anzeigen
    public void displayAllAccounts() {
        if (accounts.isEmpty()) {
            toDisplay.showMessage("Es gibt noch keine Bankkonten.");
            return;
        }

        toDisplay.showMessage("\n📜 Liste aller Bankkonten:\n");
        toDisplay.showMessage("Anzahl der Bankkonten: " + BankAccount.accountCount + "\n");
        for (BankAccount account : accounts) {
            toDisplay.showMessage(account.toString());
        }
    }


    // Einzelnes Konto Anzeigen
    public void displayAccount(Scanner scanner) {
        if(accounts.isEmpty()){
            toDisplay.showError("Es gibt keine Konten!");
        }

        int accountID= validData.accountExistCheck(scanner,accounts,"Bitte geben Sie die Account-ID ein: ");

        for (BankAccount account : accounts) {
            if (account.getAccountID() == accountID) {
                toDisplay.showMessage("\nBankkonto-Details:\n" + account);
            }
        }
    }
}
