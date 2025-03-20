package member;

public class Team {
    private final int teamID;
    private final String teamName;
    private final String group;

    public Team(int teamID, String teamName, String group) {
        this.teamID = teamID;
        this.teamName = teamName;
        this.group = group;
    }

    public int getTeamID() {
        return teamID;
    }

    public String getTeamName() {
        return teamName;
    }

    public String getGroup() {
        return group;
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