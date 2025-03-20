package ClubAdminsitration;

import GUI.DataToDisplay;
import member.Member;
import member.Team;

import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.time.format.DateTimeParseException;
import java.util.List;
import java.util.Scanner;
import java.util.regex.*;


public class ValidData {
    private final DataToDisplay dataToDisplay;
    private final DateTimeFormatter dateFormat;

    public ValidData(){
        this.dataToDisplay = new DataToDisplay();
        this.dateFormat = DateTimeFormatter.ofPattern("dd.MM.yyyy");
    }

    public String getGroupLetter(Scanner scanner, String prompt, List<Team> teams){

        while (true) {
            dataToDisplay.showMessage(prompt);
            String input = scanner.nextLine().trim();

            if (!input.matches("[A-Z]")) {
                dataToDisplay.showMessage("Ungültige Eingabe! Bitte nur einen Großbuchstaben (A-Z) eingeben.");
                continue;
            }

            boolean exists = teams.stream().anyMatch(team -> team.getGroup().equals(input));

            if (exists) {
                dataToDisplay.showMessage("Team-Gruppe '" + input + "' existiert bereits! Bitte einen anderen Buchstaben wählen.");
                continue;
            }

            return input;
        }
    }

    public int getExistTeamID(Scanner scanner,String prompt,List<Team>teams){

        while (true) {
            dataToDisplay.showMessage(prompt);
            try {
                int teamID = Integer.parseInt(scanner.nextLine().trim());
                boolean exists = teams.stream().anyMatch(team -> team.getTeamID() == teamID);

                if (exists) {
                    return teamID;
                } else {
                    dataToDisplay.showMessage("Fehler: Team mit ID " + teamID + " existiert nicht! Bitte erneut eingeben.");
                }
            } catch (NumberFormatException e) {
                dataToDisplay.showError("Ungültige Eingabe! Bitte eine gültige Zahl eingeben.");
            }
        }

    }

    public int getExistMemberID(Scanner scanner,String prompt,List<Member> members){

        while (true) {
            try {
                dataToDisplay.showMessage(prompt);
               int memberID = Integer.parseInt(scanner.nextLine().trim());

                boolean exists = members.stream().anyMatch(m -> m.getMID() == memberID);
                if (exists) {
                    return memberID;
                } else {
                    dataToDisplay.showMessage("Die Mitglieds-ID " + memberID + " existiert nicht. Bitte eine gültige ID eingeben.");
                }

            } catch (NumberFormatException e) {
                dataToDisplay.showError("Ungültige Eingabe! Bitte eine gültige Zahl eingeben.");
            }
        }

    }

    public int getPlayerOrTrainerID(Scanner scanner,String prompt,List<Member>members){


        List<Member> validMembers = members.stream()
                .filter(m -> m.getUnit().equals("Player") || m.getUnit().equals("Trainer"))
                .toList();

        if (validMembers.isEmpty()) {
            System.out.println("Es gibt keine Spieler oder Trainer in der Liste!");
            return -1;
        }

        dataToDisplay.showMessage("Wähle einen Spieler oder Trainer:");
        validMembers.forEach(m ->
                dataToDisplay.showMessage(m.getMID() + " - " + m.getFirstname() + " " + m.getLastname() + " (" + m.getUnit() + ")"));


        while (true) {
            dataToDisplay.showMessage(prompt);
            String input = scanner.nextLine().trim();
            int memberID;
            try {
                memberID = Integer.parseInt(input);
                if (validMembers.stream().anyMatch(m -> m.getMID() == memberID)) {
                    return memberID;
                } else {
                    dataToDisplay.showMessage("Ungültige ID! Bitte eine gültige Spieler- oder Trainer-ID eingeben.");
                }
            } catch (NumberFormatException e) {
                dataToDisplay.showMessage("Ungültige Eingabe! Bitte eine Zahl eingeben.");
            }
        }

    }

    public String getDateForm(Scanner scanner, String prompt){

        String date;
        while (true) {
            dataToDisplay.showMessage(prompt);
            try {
                date = LocalDate.parse(scanner.nextLine(),dateFormat).toString();
                break;
            } catch (DateTimeParseException e) {
                dataToDisplay.showError("Ungültiges Format! Bitte im Format DD.MM.YYYY eingeben.");
            }
        }
        return date;
    }

    public String getString(Scanner scanner, String prompt){
        String data;
        dataToDisplay.showMessage(prompt);
        data = scanner.nextLine();

        return data;
    }

    public int getInt(Scanner scanner,String prompt){

        while (true) {
            try {
                dataToDisplay.showMessage(prompt);
                return Integer.parseInt(scanner.nextLine().trim());
            } catch (NumberFormatException e) {
                dataToDisplay.showError("\nUngültige Eingabe! Bitte eine Zahl eingeben.");
            }
        }
    }

    public String isValidName(Scanner scanner,String prompt) {
        String name;
        while (true) {
            dataToDisplay.showMessage(prompt);
            name = scanner.nextLine().trim();
            if (name.matches("[a-zA-ZäöüÄÖÜß\\-']+") ) {
                break;
            }else{
                dataToDisplay.showError("Ungültiger Name! Bitte nur Buchstaben verwenden.");
            }
        }
        return name;
    }

    public String isEmailValid(Scanner scanner){

        String emailRegex = "^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$";
        String newEmail;
        Pattern pattern = Pattern.compile(emailRegex);

        while (true) {  // Endlosschleife, bis eine gültige E-Mail eingegeben wird
            System.out.print("Bitte eine gültige E-Mail-Adresse eingeben: ");
            newEmail = scanner.nextLine().trim();  // Benutzer-Eingabe lesen und Leerzeichen entfernen

            Matcher matcher = pattern.matcher(newEmail);

            if (matcher.matches()) {  // Falls die Eingabe korrekt ist, brechen wir die Schleife ab
                break;
            } else {
                System.out.println("⚠ Ungültige E-Mail-Adresse. Bitte erneut eingeben.");
            }
        }

        return newEmail;  // Zurückgeben der gültigen E-Mail-Adresse
    }

}
