package bankManager;

import bankClass.BankAccount;
import dashboardGUI.ShowDisplay;

import java.math.RoundingMode;
import java.math.BigDecimal;
import java.time.LocalDate;
import java.util.*;
import java.time.format.*;


public class ValidDataClass {
    private final ShowDisplay toDisplay;
    private final DateTimeFormatter dateFormat;

    public ValidDataClass() {
        this.toDisplay= new ShowDisplay();
        this.dateFormat= DateTimeFormatter.ofPattern("dd.MM.yyyy");
    }

    // Id überprüfung für Existierende Konten
    public int newAccountIDCheck(Scanner scanner, List<BankAccount> accounts) {

        while (true) {
            toDisplay.showMessage("\nKonto-ID eingeben: ");
            try {

                int id = Integer.parseInt(scanner.nextLine().trim());
                boolean exists = accounts.stream().anyMatch(a -> a.getAccountID() == id);
                if (exists) {
                    toDisplay.showError("Diese Konto-ID existiert bereits! Bitte eine andere ID eingeben.");
                } else {
                    return id;
                }
            } catch (NumberFormatException e) {
                toDisplay.showError("\nUngültige Eingabe! Bitte eine Zahl eingeben.");
            }
        }
    }


    // IBAN Generieren
    public String ibanGenerator(List<BankAccount> accounts) {
        Random random = new Random();
        String numberPart;
        boolean exists;

        while (true) {
            numberPart = String.format(
                    "%04d %04d %04d %04d",
                    random.nextInt(10000),
                    random.nextInt(10000),
                    random.nextInt(10000),
                    random.nextInt(10000)
            );

            String iban = "AT" + String.format("%02d", random.nextInt(100)) + " " + numberPart;
            // Überprüfen, ob der IBAN bereits existiert
            exists = accounts.stream().anyMatch(a -> a.getIban().equals(iban));
            if (!exists || accounts.isEmpty()) {
                return iban;
            }
        }
    }


    // Datumsformat überprüfen
    public LocalDate dateCheck(Scanner scanner, String prompt){
        LocalDate birth;
        while (true) {
            toDisplay.showMessage(prompt);
            try {
                birth = LocalDate.parse(scanner.nextLine(),dateFormat);
                break;
            } catch (DateTimeParseException e) {
                toDisplay.showError("Ungültiges Format! Bitte im Format DD.MM.YYYY eingeben.");
            }
        }
        return birth;
    }


    // Namens Validierung
    public String isValidName(Scanner scanner,String prompt) {
        String name;
        while (true) {
            toDisplay.showMessage(prompt);
            name = scanner.nextLine().trim();
            if (name.matches("[a-zA-ZäöüÄÖÜß\\-']+") ) {
                break;
            }else{
                toDisplay.showError("Ungültiger Name! Bitte nur Buchstaben verwenden.");
            }
        }
        return name;
    }


    // Adresse Validierung
    public String addressCheck(Scanner scanner,String prompt){
        String address;
        while (true) {
            toDisplay.showMessage(prompt); // Zeigt die Aufforderung an
            address = scanner.nextLine().trim(); // Entfernt überflüssige Leerzeichen

            // Prüft, ob die Eingabe leer oder nur aus Leerzeichen besteht
            if (!address.isEmpty() && address.matches("^[A-Za-z0-9äöüÄÖÜß\\s,.-]+$")) {
                return address;
            }

            toDisplay.showError("Ungültige Adresse! Bitte eine gültige Adresse eingeben.");
        }
    }


    // Überprüfung ob Bankkonto existiert
    public int accountExistCheck(Scanner scanner,List<BankAccount> accounts,String prompt){


        while (true) {
            toDisplay.showMessage(prompt);
            try {

                int accountID = Integer.parseInt(scanner.nextLine().trim());
                if (accounts.stream().anyMatch(a->a.getAccountID()== accountID) || accounts.isEmpty()) {
                    return accountID;
                } else {
                    toDisplay.showError("Die eingegebene Account-ID existiert nicht. Bitte erneut eingeben.");
                }

            } catch (NumberFormatException e) {
                toDisplay.showError("Ungültige Eingabe! Bitte geben Sie eine gültige Zahl ein.");
            }
        }
    }


   // Bankkonto Kontostand Betrag abfrage und überprüfung
    public BigDecimal transferAmountCheck(Scanner scanner, int sourceAccountID, List<BankAccount> accounts) {
        BigDecimal amount;
        BankAccount sourceAccount = null;

        while (true) {
            try {
                amount = readBigDecimal(scanner,"Bitte geben sie den zu überweißenden Betrag ein: ");

                // Suche nach dem entsprechenden Bankkonto
                for (BankAccount account : accounts) {
                    if (account.getAccountID() == sourceAccountID) {
                        sourceAccount = account;
                        break;
                    }
                }

                // Prüfen, ob genügend Guthaben vorhanden ist
                if (sourceAccount.getValue().compareTo(amount)<0) {
                    toDisplay.showError("Nicht genügend Guthaben! Verfügbar: " + sourceAccount.getValue() + " €");
                    continue;
                }

                return amount; // Betrag ist gültig, also zurückgeben
            } catch (NumberFormatException e) {
                toDisplay.showError("Ungültige Eingabe! Bitte geben Sie eine gültige Zahl ein.");
            }
        }
    }


    // Geld übertragen Logik
    public boolean transferMoney(int sourceAccountID, int targetAccountID, BigDecimal amount,List<BankAccount> accounts) {
        BankAccount sourceAccount = null;
        BankAccount targetAccount = null;

        // Prüfen, dass es nicht dasselbe Konto ist
        if (sourceAccountID == targetAccountID) {
            toDisplay.showError("Sie können kein Geld an Ihr eigenes Konto überweisen!");
            return false;
        }

        for (BankAccount account : accounts) {
            if (account.getAccountID() == sourceAccountID) {
                sourceAccount = account;
            } else if (account.getAccountID() == targetAccountID) {
                targetAccount = account;
            }
        }

        // Geld transferieren
        sourceAccount.setValue(sourceAccount.getValue().subtract(amount));
        targetAccount.setValue(targetAccount.getValue().add(amount));


        // 5️⃣ Erfolgsmeldung
        toDisplay.showMessage("Überweisung erfolgreich: " + amount + " € von Konto " + sourceAccountID + " an Konto " + targetAccountID + " transferiert.");
        return true;
    }


    // Auszahlungslogik
    public void withdraw(Scanner scanner,List<BankAccount> accounts){
        BankAccount currentAccount = null;
        int accountID;
        BigDecimal value=  readBigDecimal(scanner,"Bitte Auszahlungsbetrag eingeben: ");

        try{

            accountID = accountExistCheck(scanner,accounts,"Bitte ihre Account-ID eingeben: ");
            for (BankAccount account : accounts) {
                if (account.getAccountID() == accountID) {
                    currentAccount = account;
                    if (currentAccount.getValue().compareTo(value)<0){
                        toDisplay.showMessage("Nicht genug Guthaben!");
                        return;
                    }
                }
            }
            currentAccount.setValue(currentAccount.getValue().subtract(value));

        }catch (NumberFormatException e){
            toDisplay.showError("Auszahlung fehlgeschlagen");
            return;
        }
        toDisplay.showMessage("Erfolg! Der Betrag "+value+"€ wurden ausgezahlt");
    }


    // Einzahlungslogik
    public void deposit (Scanner scanner,List<BankAccount> accounts){
        BankAccount currentAccount = null;
        int accountID;
        BigDecimal value;

        while (true) {
            try {

                toDisplay.showMessage("\nBitte Einzahlungsbetrag eingeben oder 0 für Beenden: \n");
                value = new BigDecimal(scanner.nextLine().trim());

                // Falls der Nutzer 0 eingibt, sofort beenden
                if (value.compareTo(BigDecimal.ZERO) == 0) {
                    toDisplay.showMessage("Einzahlung abgebrochen.");
                    return;
                }

                // Falls der Betrag negativ ist, Fehlermeldung und neue Eingabe fordern
                if (value.compareTo(BigDecimal.ZERO) < 0) {
                    toDisplay.showError("Ungültiger Betrag! Betrag muss größer als 0 sein.");
                    continue;
                }

                // **Nachkommastellen auf exakt 2 begrenzen, ohne zu runden**
                value = value.setScale(2, RoundingMode.DOWN);
                break;

            } catch (NumberFormatException e) {
                toDisplay.showError("Ungültige Eingabe! Bitte geben Sie eine gültige Zahl ein.");
            }

        }
        accountID = accountExistCheck(scanner, accounts, "Bitte Ihre Account-ID eingeben: ");

        for (BankAccount account : accounts) {
            if (account.getAccountID() == accountID) {
                currentAccount = account;
                break;
            }
        }
        currentAccount.setValue(currentAccount.getValue().add(value));
        toDisplay.showMessage("Erfolg! Der Betrag "+value+"€ wurden eingezahlt");
    }


    // BigDecimal Einlesen
    public BigDecimal readBigDecimal(Scanner scanner, String prompt){
        while (true) {
            toDisplay.showMessage(prompt);
            try {
                BigDecimal value = new BigDecimal(scanner.nextLine().trim());
                if (value.compareTo(BigDecimal.ZERO) > 0) {
                    return value;
                } else {
                    toDisplay.showError("Der Betrag muss größer als 0 sein.");
                }
            } catch (NumberFormatException e) {
                toDisplay.showError("Ungültige Eingabe! Bitte geben Sie eine gültige Zahl ein.");
            }
        }
    }


    // int Einlesen
    public int readInt(Scanner scanner,String prompt) {
        while (true) {
            try {
                toDisplay.showMessage(prompt);
                return Integer.parseInt(scanner.nextLine().trim());
            } catch (NumberFormatException e) {
                toDisplay.showError("\nUngültige Eingabe! Bitte eine Zahl eingeben.");
            }
        }
    }





























}
