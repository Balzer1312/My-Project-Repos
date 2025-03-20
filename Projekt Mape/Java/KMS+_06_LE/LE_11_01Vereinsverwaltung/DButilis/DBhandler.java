package DButilis;

import GUI.DataToDisplay;
import member.*;
import java.sql.*;
import java.util.ArrayList;
import java.util.List;


public class DBhandler {
    private final DataToDisplay showDashboard = new DataToDisplay();
    private final DBConfig dbConfig;

    public DBhandler() {
        this.dbConfig = DBConfig.getInstance();
    }
//##################################### Daten von der DB laden #######################################

    public List<Member> getMemberDataDB(){
        List<Member> members = new ArrayList<>();
        String administrationBody;
        String query = "SELECT * FROM member";

        try (Connection conn = dbConfig.getConnection();
             Statement stmt = conn.createStatement();
             ResultSet rs = stmt.executeQuery(query)) {

            while (rs.next()) {
                int mid = rs.getInt("MID");
                String firstname = rs.getString("firstname");
                String lastname = rs.getString("lastname");
                String birth = rs.getString("birth");
                String address = rs.getString("address");
                String mail = rs.getString("mail");
                String entryDate = rs.getString("entryDate");
                String unit = rs.getString("unit");
                int experience = rs.getInt("Experience");

                String teamGroup = rs.getString("TeamGroup");

                switch (unit) {
                    case "Player":
                        int playerNumb = rs.getInt("playerNumb");
                        String playerPos = rs.getString("playerPos");
                        members.add(new Player(mid, firstname, lastname, birth, address, mail, entryDate, unit, experience, teamGroup, playerNumb, playerPos));
                        break;
                    case "Trainer":
                        String trainingTypes = rs.getString("trainingTypes");
                        members.add(new Trainer(mid, firstname, lastname, birth, address, mail, entryDate, unit, teamGroup ,experience, trainingTypes));
                        break;
                    case "Manager":
                        administrationBody = rs.getString("administrationBody");
                        String competence = rs.getString("competence");
                        members.add(new Manager(mid, firstname, lastname, birth, address, mail, entryDate, unit, experience, administrationBody ,competence));
                        break;
                    case "Treasurer":
                        administrationBody = rs.getString("administrationBody");
                        String financeArea = rs.getString("financeArea");
                        members.add(new Treasurer(mid, firstname, lastname, birth, address, mail, entryDate, unit, experience, administrationBody,financeArea));
                        break;

                }
            }

        } catch (SQLException e) {
            showDashboard.showError("Fehler beim Laden der Daten: " + e.getMessage());
        }

        return members;
    }

    public List<Team> getAllTeams() {
        List<Team> teamList = new ArrayList<>();
        String sql = "SELECT * FROM Team";

        try (Connection conn = dbConfig.getConnection();
             Statement stmt = conn.createStatement();
             ResultSet rs = stmt.executeQuery(sql)) {

            while (rs.next()) {
                int id = rs.getInt("TID");
                String name = rs.getString("teamName");
                String group = rs.getString("TeamGroup");

                teamList.add(new Team(id, name, group));
            }

            System.out.println("Teams erfolgreich aus der DB geladen!");

        } catch (SQLException e) {
            System.err.println("Fehler beim Laden der Teams: " + e.getMessage());
        }

        return teamList;
    }


    public void addMemberToDB(Member newMember){

        // Standardwerte für optionale Felder
        String playerPos = null, trainingTypes = null, competence = null, administrationBody = null, financeArea = null;
        Integer playerNumb = null;

        String sql = "{CALL addMember(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)}";

        try (Connection conn = dbConfig.getConnection();
             CallableStatement stmt = conn.prepareCall(sql)) {

            // Pflichtfelder setzen (dürfen nicht NULL sein)
            stmt.setString(1, newMember.getFirstname());
            stmt.setString(2, newMember.getLastname());
            stmt.setString(3, newMember.getBirth());
            stmt.setString(4, newMember.getAddress());
            stmt.setString(5, newMember.getMail());
            stmt.setString(6, newMember.getEntryDate());
            stmt.setString(7, newMember.getUnit());
            stmt.setNull(10, Types.VARCHAR);
            stmt.setInt(11, newMember.getExperience()); // Experience ist jetzt Pflicht!

            // Typ des Objekts bestimmen und passende Felder setzen
            switch (newMember) {
                case Player p -> {
                    playerPos = p.getPlayerPos();
                    playerNumb = p.getPlayerNumb();

                }
                case Trainer t -> {
                    trainingTypes = t.getTrainingTypes();
                }

                case Manager m -> {
                    competence = m.getCompetence();
                    administrationBody = m.getAdministrationBody();
                }
                case Treasurer tr -> {
                    financeArea = tr.getFinanceArea();
                    administrationBody = tr.getAdministrationBody();
                }
                default -> {
                }
            }

            if (playerPos != null) stmt.setString(8, playerPos);
            else stmt.setNull(8, Types.VARCHAR);

            if (playerNumb != null) stmt.setInt(9, playerNumb);
            else stmt.setNull(9, Types.INTEGER);

            if (trainingTypes != null) stmt.setString(12, trainingTypes);
            else stmt.setNull(12, Types.VARCHAR);

            stmt.setNull(13, Types.VARCHAR);

            if (competence != null) stmt.setString(14, competence);
            else stmt.setNull(14, Types.VARCHAR);

            if (administrationBody != null) stmt.setString(15, administrationBody);
            else stmt.setNull(15, Types.VARCHAR);

            if (financeArea != null) stmt.setString(16, financeArea);
            else stmt.setNull(16, Types.VARCHAR);

            stmt.setNull(17, Types.INTEGER);
            stmt.execute();

            showDashboard.showMessage("Mitglied erfolgreich in die DB eingefügt!");

        } catch (SQLException e) {
            showDashboard.showError("Fehler beim Einfügen des Mitglieds: " + e.getMessage());
        }

    }

    public void deleteMemberInDB(int deleteOnID){
        String sql = "{CALL deleteMember(?)}";

        try (Connection conn = dbConfig.getConnection();
             CallableStatement stmt = conn.prepareCall(sql)) {

            stmt.setInt(1, deleteOnID);
            stmt.execute();
            showDashboard.showMessage("Mitglied mit MID " + deleteOnID + " wurde erfolgreich gelöscht.");

        } catch (SQLException e) {
            showDashboard.showError("Fehler beim Löschen des Mitglieds: " + e.getMessage());
        }


    }

    public void deleteTeam(int teamID) {
        String sql = "{CALL deleteTeam(?)}";

        try (Connection conn = dbConfig.getConnection();
             CallableStatement stmt = conn.prepareCall(sql)) {

            stmt.setInt(1, teamID);
            stmt.execute();
            showDashboard.showMessage("Team erfolgreich gelöscht!");


        } catch (SQLException e) {
            showDashboard.showError("Fehler beim Löschen des Teams: " + e.getMessage());
        }
    }

    public void updateMember(int memberID, int choice, Object newValue) {
        String sql = "{CALL updateMember(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)}";

        //      1.  IN p_mid INT,
        //      2.  IN p_firstname VARCHAR(50),
        //      3.  IN p_lastname VARCHAR(50),
        //      4.  IN p_address VARCHAR(50),
        //      5.  IN p_mail VARCHAR(50),
        //      6.  IN p_playerPos VARCHAR(10),
        //      7.  IN p_teamGroup VARCHAR(10),
        //      8.  IN p_trainingTypes VARCHAR(25),
        //      9.  IN p_competence VARCHAR(50),
        //     10.  IN p_financeArea VARCHAR(50),
        //     11.  IN p_experience INT

        try (Connection conn = dbConfig.getConnection();
             CallableStatement stmt = conn.prepareCall(sql)) {

            stmt.setInt(1, memberID);

            // Standardwerte für optionale Parameter (auf NULL setzen)
            for (int i = 2; i <= 11; i++) {
                if (i == 11) {
                    stmt.setNull(i, Types.INTEGER);
                } else {
                    stmt.setNull(i, Types.VARCHAR);
                }
            }

            // Neues Feld setzen
            if (newValue instanceof String) {
                stmt.setString(choice, (String) newValue);
            } else if (newValue instanceof Integer) {
                stmt.setInt(choice, (Integer) newValue);
            }



            stmt.execute();
            showDashboard.showMessage("Mitgliedsdaten erfolgreich in der DB aktualisiert!");

        } catch (SQLException e) {
            showDashboard.showError("Fehler beim Aktualisieren des Mitglieds: " + e.getMessage());
        }
    }

    public void newTeamToDB(String teamName, String teamGroup) {
        String sql = "{CALL createNewTeam(?, ?)}";

        try (Connection conn = dbConfig.getConnection();
             CallableStatement stmt = conn.prepareCall(sql)) {

            stmt.setString(1, teamName);
            stmt.setString(2, teamGroup);
            stmt.execute();

            System.out.println("Team erfolgreich erstellt!");

        } catch (SQLException e) {
            System.err.println("Fehler beim Erstellen des Teams: " + e.getMessage());
        }
    }

    public void assignMemberToTeamDB(int memberID, int teamID) {
        String sql = "{CALL assignMemberToTeam(?, ?)}";

        try (Connection conn = dbConfig.getConnection();
             CallableStatement stmt = conn.prepareCall(sql)) {

            stmt.setInt(1, memberID);
            stmt.setInt(2, teamID);
            stmt.execute();

            showDashboard.showMessage("Mitglied erfolgreich dem Team zugewiesen!");


        } catch (SQLException e) {
            showDashboard.showError("Fehler beim Zuweisen des Mitglieds zum Team: " + e.getMessage());
        }
    }

}




