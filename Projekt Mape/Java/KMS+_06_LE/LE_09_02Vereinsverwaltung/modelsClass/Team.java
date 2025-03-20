package modelsClass;

import java.time.LocalDate;

public class Team {
    private int teamID;
    private String teamName;
    private String group;

    public Team(int teamID, String teamName,String group) {
        this.teamID=teamID;
        this.teamName=teamName;
        this.group = group;
    }

    public int getTeamID() {
        return teamID;
    }

    public void setTeamID(int teamID) {
        this.teamID = teamID;
    }

    public String getTeamName() {
        return teamName;
    }

    public void setTeamName(String teamName) {
        this.teamName = teamName;
    }

    public String getGroup() {
        return group;
    }

    public void setGroup(String group) {
        this.group = group;
    }

    @Override
    public String toString() {
        return "Team{" +
                "teamID=" + teamID +
                ", teamName='" + teamName + '\'' +
                ", group='" + group + '\'' +
                '}';
    }
}
