package GUI;

import member.*;
import member.Team;

import java.util.List;
import java.util.Objects;

public class DataToDisplay {

    public void showMainMenu() {

        String[] menuOptions ={
                "1. Mitglieder Hinzufügen",
                "2. Mitglied Löschen",
                "3. Mitglied bearbeiten",
                "4. Alle Mitglieder Ausgeben",
                "5. Ein Mitglied Ausgeben",
                "6. Team erstellen",
                "7. Team Löschen",
                "8. Mitglieder zu Team zu weißen",
                "9. Team Ausgeben",
                "10. Programm Beenden"
        };

        System.out.println("\n==============================");
        System.out.println("Vereinsverwaltung");
        System.out.println("==============================");

        for (String option: menuOptions){
            System.out.println(option);
        }

        System.out.print("Wähle eine Option: ");
    }

    public void showMemberType(){

        String[] memberOptions ={
                "1. Spieler",
                "2. Trainer",
                "3. Manager",
                "4. Schatzmeister",
                "5. Vorgang abbrechen",
        };

        System.out.println("\nWas wollen Sie Hinzufügen:\n");

        for (String option: memberOptions){
            System.out.println(option);
        }
    }

    public void showMessage(String message) {
        System.out.println(message);
    }

    public void showError(String errorMessage) {
        showMessage(errorMessage);
    }

    public void outputOneMember(int memberID, List<Member> members){
        if(members.isEmpty()){
            System.out.println("Keine Daten Vorhanden");
            return;
        }
        System.out.println("\nMitglied:\n");
        for (Member m : members) {
            if (m.getMID()==memberID)
                System.out.println(m);
        }

    }

    public void outputAllMember(List<Member>members){

        if(members.isEmpty()){
            System.out.println("Keine Daten Vorhanden");
            return;
        }
        System.out.println("\n=================================================================================================================");
        System.out.println("\nVerfügbare Mitglieder:\n");
        System.out.printf("           |%-15s | %-15s | %-10s | %-25s | %-10s | %-10s%n",
                          "Vorname", "Nachname", "Geb.:", "Email", "Eintritt", "Mitglied-Typ");
        System.out.println("-----------------------------------------------------------------------------------------------------------------");
        for (Member m : members) {
            System.out.printf("ID: %-5d | %-15s | %-15s | %-10s | %-25s | %-10s | %-10s |\n",
                    m.getMID(), m.getFirstname(), m.getLastname(), m.getBirth(),
                    m.getMail(), m.getEntryDate(), m.getUnit());
        }
        System.out.println("-----------------------------------------------------------------------------------------------------------------\n");
    }

    public void showTeams(List<Member>members, List<Team> teams){

        if (teams.isEmpty()) {
            System.out.println("Keine Teams vorhanden!");
            return;
        }

        System.out.println("\nTeams und ihre Gruppen:\n");

        for (Team team : teams) {
            System.out.println("\nTeam: " + team.getTeamName() + " (Gruppe: " + team.getGroup() + ")");

            // Spieler und Trainer suchen, die zu diesem Team gehören
            List<Member> teamMembers = members.stream()
                    .filter(m -> (m instanceof Player && Objects.equals(((Player) m).getTeamGroup(), team.getGroup()))
                                      || (m instanceof Trainer && Objects.equals(((Trainer) m).getGroup(), team.getGroup()))).toList();



            // Falls Team Mitglieder hat, anzeigen
            if (!teamMembers.isEmpty()) {
                System.out.println("Team Mitglieder:");
                for (Member member : teamMembers) {
                    System.out.println("   - " + member.getFirstname() + " " + member.getLastname() + "Gruppe:  (" + member.getUnit() + ")");
                }

            } else {
                System.out.println("Keine Mitglieder in diesem Team.");
            }
        }
    }
}
