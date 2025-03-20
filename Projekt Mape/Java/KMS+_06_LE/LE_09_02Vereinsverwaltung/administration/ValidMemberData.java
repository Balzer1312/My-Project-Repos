package administration;

import modelsClass.*;
import java.time.LocalDate;
import java.time.format.*;
import java.util.ArrayList;
import java.util.List;
import java.util.Locale;
import java.util.Scanner;

public class ValidMemberData {
    private final List<Member> members;
    private final List<Team>teams;
    private final DisplayShow toDisplay;
    private final DateTimeFormatter dateFormat;

    public ValidMemberData() {
        this.members = new ArrayList<>();
        this.teams= new ArrayList<>();
        this.toDisplay= new DisplayShow();
        this.dateFormat = DateTimeFormatter.ofPattern("dd.MM.yyyy");
    }


    public Member createMember(Scanner scanner){
        int memberID,memberType,playerNumber,experience;
        String firstname,lastname,financeArea,competence,group,trainingKind,pos;
        LocalDate birth, entryDate;
        Member newMember=null;

        while (true) {
            toDisplay.showMessage("Mitglieds-ID eingeben: ");
            memberID = readInt(scanner);
            if (!isMemberIdExists(memberID)) {
                break;
            }
            toDisplay.showError("Diese Mitglieds-ID existiert bereits! Bitte eine andere ID eingeben.");
        }

        while (true) {
            toDisplay.showMessage("Vorname eingeben: ");
            firstname = scanner.nextLine();
            if (!isValidName(firstname)) {
                toDisplay.showError("Ungültiger Name! Bitte nur Buchstaben verwenden.");
            }else{
                break;
            }
        }

        // Nachname validieren (keine Zahlen oder Sonderzeichen erlaubt)
        while (true) {
            toDisplay.showMessage("Nachname eingeben: ");
            lastname = scanner.nextLine();
            if (!isValidName(lastname)) {
                toDisplay.showError("Ungültiger Nachname! Bitte nur Buchstaben verwenden.");
            }else{
                break;
            }
        }

        while (true) {
            toDisplay.showMessage("Geburtsdatum (DD.MM.YYYY) eingeben: ");
            try {
                birth = LocalDate.parse(scanner.nextLine(),dateFormat);
                break;
            } catch (DateTimeParseException e) {
                toDisplay.showError("Ungültiges Format! Bitte im Format DD.MM.YYYY eingeben.");
            }
        }

        while (true) {
            toDisplay.showMessage("Eintrittsdatum (DD.MM.YYYY) eingeben: ");
            try {
                entryDate = LocalDate.parse(scanner.nextLine(), dateFormat);
                break;
            } catch (DateTimeParseException e) {
                toDisplay.showError("Ungültiges Format! Bitte im Format DD.MM.YYYY eingeben.");
            }
        }
        while (true){
            toDisplay.showMemberType();
            memberType = readInt(scanner);
            if (memberType >= 1 && memberType <= 4) {
                break;
            }
            toDisplay.showError("Ungültige Auswahl! Bitte eine Zahl zwischen 1 und 4 eingeben.");
        }

        switch (memberType) {
            case 1:
                toDisplay.showMessage("Kompetenzbereich eingeben: ");
                competence = scanner.nextLine();
                newMember = new Manager(memberID, firstname, lastname, birth.toString(), entryDate, "Manager", competence);
                break;
            case 2:
                toDisplay.showMessage("Finanzbereich eingeben: ");
                financeArea = scanner.nextLine();
                newMember = new Treasurer(memberID, firstname, lastname, birth.toString(), entryDate,"Kassenwart" ,financeArea);
                break;
            case 3:
                while (true) {
                    toDisplay.showMessage("Erfahrung in Jahren: ");
                    experience = readInt(scanner);
                    if (experience >= 0) {
                        break;
                    }
                    toDisplay.showMessage("Erfahrung kann nicht negativ sein.");
                }
                toDisplay.showMessage("Trainingsart: ");
                trainingKind = scanner.nextLine();
                while (true) {
                    toDisplay.showMessage("Team-Gruppe eingeben (ein einzelner Großbuchstabe): ");
                    group = scanner.nextLine().toUpperCase();
                    if (group.matches("[A-Z]")&& isGroupExist(group)) {
                        break;
                    }
                    toDisplay.showError("Ungültige Gruppe! Bitte nur einen Großbuchstaben eingeben.");
                }
                newMember = new Trainer(memberID, firstname, lastname, birth.toString(), entryDate, group, experience, trainingKind);
                break;
            case 4:
                while (true) {
                    toDisplay.showMessage("Spielernummer eingeben (maximal 2-stellig): ");
                    playerNumber = readInt(scanner);
                    if (playerNumber >= 0 && playerNumber <= 99) {
                        break;
                    }
                    toDisplay.showError("Ungültige Spielernummer! Nur 1- bis 2-stellige Zahlen erlaubt.");
                }
                while (true) {
                    toDisplay.showMessage("Team-Gruppe eingeben (ein einzelner Großbuchstabe): ");
                    group = scanner.nextLine().toUpperCase();
                    if (group.matches("[A-Z]") && isGroupExist(group)) {
                        break;
                    }
                    toDisplay.showError("Ungültige Gruppe! Bitte nur einen Großbuchstaben eingeben.");
                }
                toDisplay.showMessage("Position eingeben: ");
                pos = scanner.nextLine();
                newMember = new Player(memberID, firstname, lastname, birth.toString(), entryDate, group, playerNumber, pos);
                break;
        }


        members.add(newMember);
        toDisplay.showMessage("\nMitglied erfolgreich erstellt!");
        return newMember;
    }

    public void deleteMember(Scanner scanner) {
        int memberID;
        boolean removed;

        toDisplay.showMessage("Mitglieds-ID zum Löschen eingeben: ");
        memberID = readInt(scanner);

        removed= members.removeIf(m -> m.getMemberID()==memberID );
        if (removed) {
            toDisplay.showMessage("Mitglied mit ID " + memberID + " wurde erfolgreich gelöscht.");
        } else {
            toDisplay.showError("Kein Mitglied mit dieser ID gefunden.");
        }

    }

    public Team createTeam(Scanner scanner){
        Team newTeam=null;
        int teamID;
        String teamName,group;

        while (true) {
            toDisplay.showMessage("Team-ID eingeben: ");
            teamID = readInt(scanner);
            if (!isTeamIdExists(teamID)) {
                break;
            }
            toDisplay.showError("Diese Team-ID existiert bereits! Bitte eine andere ID eingeben.");
        }

        while (true){
            toDisplay.showMessage("Team-Gruppe eingeben (ein einzelner Großbuchstabe): ");
            group = scanner.nextLine().toUpperCase();
            if (group.matches("[A-Z]") && isGroupExist(group)) {
                break;
            }
            toDisplay.showError("Ungültige Gruppe! Bitte nur einen Großbuchstaben eingeben.");
        }
        toDisplay.showMessage("Wie wollen sie das Team benennen: ");
        teamName= scanner.nextLine();

        newTeam= new Team(teamID, teamName,group);
        return newTeam;
    }

    public void deleteTeam(Scanner scanner){
        int teamID;
        boolean removed;

        toDisplay.showMessage("Mitglieds-ID zum Löschen eingeben: ");
        teamID = readInt(scanner);

        removed= teams.removeIf(t -> t.getTeamID()==teamID);
        if (removed) {
            toDisplay.showMessage("Mitglied mit ID " + teamID + " wurde erfolgreich gelöscht.");
        } else {
            toDisplay.showError("Kein Mitglied mit dieser ID gefunden.");
        }

    }

    public void displayMembers() {
        if (members.isEmpty()) {
            toDisplay.showMessage("Keine Mitglieder gefunden.");
            return;
        }
        toDisplay.showMessage("\n--- Mitgliederliste ---");
        for (Member m : members) {
            toDisplay.showMessage(m.toString());
        }
    }

    private boolean isTeamIdExists(int id){
        for (Team t : teams) {
            if (t.getTeamID() == id) {
                return true;
            }
        }
        return false;
    }


    private boolean isMemberIdExists(int id) {
        for (Member m : members) {
            if (m.getMemberID() == id) {
                return true;
            }
        }
        return false;
    }

    private boolean isGroupExist(String group){

        if (teams == null || teams.isEmpty()) {
            return true;
        }

        for (Team t : teams){
            if(t.getGroup().equals(group)){
                return true;
            }
        }
        return false;
    }

    private int readInt(Scanner scanner) {
        while (true) {
            try {
                return Integer.parseInt(scanner.nextLine().trim());
            } catch (NumberFormatException e) {
                toDisplay.showError("\nUngültige Eingabe! Bitte eine Zahl eingeben.");
            }
        }
    }

    private boolean isValidName(String name) {
        return name.matches("[a-zA-ZäöüÄÖÜß\\-']+");
    }
}
