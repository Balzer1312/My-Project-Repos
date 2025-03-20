package ClubAdminsitration;

import DButilis.*;
import member.*;
import GUI.DataToDisplay;
import java.util.*;


public class MemberAdministration {
    private final DataToDisplay dataToDisplay;
    private final ValidData validData;
    private final DBhandler dbHandler;
    private List<Member>membersList;
    private List<Team> teamsList;

    public MemberAdministration() {
        this.dbHandler = new DBhandler();
        this.dataToDisplay = new DataToDisplay();
        this.validData = new ValidData();
        membersList = dbHandler.getMemberDataDB();
        teamsList = dbHandler.getAllTeams();
    }

    public void addMember(Scanner scanner){
        int dummyId =0;
        String teamGroup,administrationBody;
        try{

            while (true) {
                int choice;
                dataToDisplay.showMemberType();
                while (true) {
                    choice = validData.getInt(scanner, "Bitte wählen Sie eine Option (1-5):");
                    if (choice >= 1 && choice <= 5) {
                        break;
                    }
                    dataToDisplay.showError("Ungültige Eingabe! Bitte eine Zahl zwischen 1 und 5 eingeben.");
                }

                if (choice == 5) {
                    dataToDisplay.showMessage("Vorgang abgebrochen.");
                    return;
                }


                String firstname = validData.isValidName(scanner, "Vorname: ");
                String lastname = validData.isValidName(scanner, "Nachname: ");
                String birth = validData.getDateForm(scanner, "Geburtsdatum (MM.DD.YYYY): ");
                String address = validData.getString(scanner, "Adresse: ");
                String mail = validData.isEmailValid(scanner);
                String entryDate = validData.getDateForm(scanner, "Eintrittsdatum (MM.DD.YYYY): ");
                int experience = validData.getInt(scanner, "Erfahrung (Jahre): ");

                switch (choice) {
                    case 1: // Spieler
                        String playerPos = validData.getString(scanner, "Spielerposition: ");
                        int playerNumb = validData.getInt(scanner, "Rückennummer: ");
                        Member newMember = new Player(dummyId, firstname, lastname, birth, address, mail, entryDate, "Player", experience, null, playerNumb, playerPos);
                        dbHandler.addMemberToDB(newMember);
                        refreshMemberList();
                        dataToDisplay.showMessage("Liste wurde aktualisiert!");
                        break;

                    case 2: // Trainer
                        String trainingTypes = validData.getString(scanner, "Trainingstypen: ");
                        newMember = new Trainer(dummyId, firstname, lastname, birth, address, mail, entryDate, "Trainer", null, experience, trainingTypes);
                        dbHandler.addMemberToDB(newMember);
                        refreshMemberList();
                        dataToDisplay.showMessage("Liste wurde aktualisiert!");
                        break;

                    case 3: // Manager
                        String competence = validData.getString(scanner, "Kompetenz: ");
                        administrationBody = validData.getString(scanner, "Wessen Verwaltungskörper gehören Sie an: ");
                        newMember = new Manager(dummyId, firstname, lastname, birth, address, mail, entryDate, "Manager", experience, administrationBody, competence);
                        dbHandler.addMemberToDB(newMember);
                        refreshMemberList();
                        dataToDisplay.showMessage("Liste wurde aktualisiert!");
                        break;

                    case 4: // Schatzmeister
                        String financeArea = validData.getString(scanner, "Finanzbereich: ");
                        administrationBody = validData.getString(scanner, "Wessen Verwaltungskörper gehören Sie an: ");
                        newMember = new Treasurer(dummyId, firstname, lastname, birth, address, mail, entryDate, "Treasurer", experience, administrationBody, financeArea);
                        dbHandler.addMemberToDB(newMember);
                        refreshMemberList();
                        dataToDisplay.showMessage("Liste wurde aktualisiert!");
                        break;
                }
            }


        } catch (Exception e) {
            throw new RuntimeException(e);
        }
    }

    public void deleteMember(Scanner scanner){

        if (membersList.isEmpty()){
            dataToDisplay.showMessage("Es gibt noch keine Mitglieder!");
            return;
        }

        int memberID;
        dataToDisplay.showMessage("Mitglieder Löschen ");
        memberID=validData.getExistMemberID(scanner,"Bitte Mitglieds ID für Löschen eingeben: ", membersList);
        dbHandler.deleteMemberInDB(memberID);
        refreshMemberList();
        dataToDisplay.showMessage("Liste wurde aktualisiert!");
    }

    public void updateMemberData(Scanner scanner){

        if (membersList.isEmpty()){
            dataToDisplay.showMessage("Es gibt noch keine Mitglieder!");
            return;
        }
        try {
            dataToDisplay.showMessage("\n\nMitgliedsdaten aktualisieren");
            dataToDisplay.outputAllMember(membersList);

            // Mitglied anhand der ID holen
            int memberID = validData.getExistMemberID(scanner, "Bitte Mitglieds-ID zum Bearbeiten eingeben: ", membersList);
            Member member = membersList.stream().filter(m -> m.getMID() == memberID).findFirst().orElse(null);
            dataToDisplay.showMessage(member.getUnit()+":\n"+"ID: "+member.getMID()+"\n"+"Name: "+ member.getFirstname()+" "+member.getLastname()+"\n"+"Geb.: "+member.getBirth()+"\n");

            String memberType = member.getUnit();
            LinkedHashMap<Integer, String> options = new LinkedHashMap<>();
            Map<Integer, Integer> sqlFieldMapping = new HashMap<>();

            // Basisfelder
            options.put(1, "Vorname");
            options.put(2, "Nachname");
            options.put(3, "Adresse");
            options.put(4, "E-Mail");
            options.put(5, "Erfahrung");

            sqlFieldMapping.put(1, 2);
            sqlFieldMapping.put(2, 3);
            sqlFieldMapping.put(3, 4);
            sqlFieldMapping.put(4, 5);
            sqlFieldMapping.put(5, 11);

            // Zusatzfelder je nach Typ
            switch (memberType) {
                case "Player" -> {
                    options.put(6, "Spielerposition");
                    options.put(7, "Team-Gruppe");
                    sqlFieldMapping.put(6, 6);
                    sqlFieldMapping.put(7, 7);
                }
                case "Trainer" -> {
                    options.put(6, "Trainingstypen");
                    options.put(7, "Team-Gruppe");
                    sqlFieldMapping.put(6, 8);
                    sqlFieldMapping.put(7, 7);
                }
                case "Manager" -> {
                    options.put(6, "Kompetenz");
                    sqlFieldMapping.put(6, 9);
                }
                case "Treasurer" -> {
                    options.put(6, "Finanzbereich");
                    sqlFieldMapping.put(6, 10);
                }
            }



            // Auswahl anzeigen
            dataToDisplay.showMessage("\nWählen Sie ein Feld zum Bearbeiten:\n");
            options.forEach((key, value) -> dataToDisplay.showMessage(key + ". " + value));
            dataToDisplay.showMessage("12 oder mehr für Abbrechen\n");

            // Nutzerauswahl
            int choice = validData.getInt(scanner, "Bitte Option wählen: ");
            if (choice >= 12) {
                dataToDisplay.showMessage("Vorgang abgebrochen.");
                return;
            }

            if (!options.containsKey(choice)) {
                dataToDisplay.showMessage("Ungültige Auswahl!");
                return;
            }

            // Neuer Feldwert abrufen
            Object newValue;
            if (choice == 1 || choice == 2) {
                newValue = validData.isValidName(scanner, "Bitte neuen " + options.get(choice) + " eingeben:");
            } else if (choice == 4) {
                newValue = validData.isEmailValid(scanner);
            } else if (choice == 5) {
                newValue = validData.getInt(scanner, "Neue Erfahrung (Jahre) eingeben: ");
            } else {
                newValue = validData.getString(scanner, "Geben Sie den neuen Wert für " + options.get(choice) + " ein: ");
            }


            int sqlIndex = sqlFieldMapping.get(choice);
            dbHandler.updateMember(memberID, sqlIndex, newValue);
            refreshMemberList();
            dataToDisplay.showMessage("Mitgliedsdaten erfolgreich aktualisiert!");


        } catch (Exception e) {
            throw new RuntimeException(e);
        }

    }

    public void showOneMember(Scanner scanner){

        if (membersList.isEmpty()){
            dataToDisplay.showMessage("Es gibt noch keine Mitglieder!");
            return;
        }
        dataToDisplay.outputAllMember(membersList);
        int memberID=validData.getExistMemberID(scanner,"Bitte Mitglied-ID für das Anzeigen eingeben: ",membersList);
        dataToDisplay.outputOneMember(memberID,membersList);
    }

    public void createNewTeam(Scanner scanner){

        String newTeamName = validData.getString(scanner,"Bitte geben sie den Namen des Teams ein: ");
        String group= validData.getGroupLetter(scanner,"Bitte Team Gruppen kürzel eingeben (A,B,....): ",teamsList);
        dbHandler.newTeamToDB(newTeamName,group);
        refreshTeamList();
        dataToDisplay.showMessage("Liste wurde aktualisiert!");
    }

    public void deleteTeam(Scanner scanner){

        if (teamsList.isEmpty()){
            dataToDisplay.showMessage("Es gibt noch keine Teams!");
            return;
        }
        dataToDisplay.showMessage("Team Löschen");
        int teamID = validData.getExistTeamID(scanner,"Bitte geben sie die TeamID ein um es löschen: ",teamsList);
        dbHandler.deleteTeam(teamID);
        refreshMemberList();
        refreshTeamList();
        dataToDisplay.showMessage("Liste wurde aktualisiert!");
    }

    public void assignMemberToTeam(Scanner scanner){
        if (membersList.isEmpty() || teamsList.isEmpty()) {
            dataToDisplay.showMessage("Keine Mitglieder oder Teams vorhanden!");
            return;
        }
        int memberID= validData.getPlayerOrTrainerID(scanner,"Bitte geben sie die ID ein:",membersList);
        int teamID= validData.getExistTeamID(scanner,"Bitte Team ID eingeben: ",teamsList);
        if (memberID==-1){
            dataToDisplay.showMessage("Keine Spieler und Trainer in Vorhanden.");
            return;
        }

        dbHandler.assignMemberToTeamDB(memberID,teamID);
        refreshMemberList();
        refreshTeamList();
        dataToDisplay.showMessage("Liste wurde aktualisiert!");


    }

    public void showAllMember(){
        dataToDisplay.outputAllMember(membersList);

    }

    public void showTeam(){
        dataToDisplay.showTeams(membersList,teamsList);
    }

    private void refreshTeamList(){
        teamsList.clear();
        teamsList = dbHandler.getAllTeams();
    }

    private void refreshMemberList(){
        membersList.clear();
        membersList = dbHandler.getMemberDataDB();
    }
}
