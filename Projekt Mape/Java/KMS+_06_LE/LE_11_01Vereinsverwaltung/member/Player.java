package member;

public class Player extends Member {
    private final String teamGroup;
    private final int playerNumb;
    private final String playerPos;

    public Player(int MID, String firstname, String lastname, String birth, String address, String mail, String entryDate, String unit,int  experience , String teamGroup, int playerNumb, String playerPos) {
        super(MID, firstname, lastname, birth, address, mail, entryDate, unit, experience);
        this.playerPos= playerPos;
        this.teamGroup= teamGroup;
        this.playerNumb = playerNumb;
    }

    public String getTeamGroup() {
        return teamGroup;
    }

    public int getPlayerNumb() {
        return playerNumb;
    }

    public String getPlayerPos() {
        return playerPos;
    }

    @Override
    public String toString() {
        return super.toString()
                +String.format(
                 "║ %-20s ║ %-25s ║\n"
                +"║ %-20s ║ %-25d ║\n"
                +"║ %-20s ║ %-25s ║\n"
                +"╚══════════════════════╩═══════════════════════════╝\n"
                ,"Team Gruppe: ", teamGroup
                ,"Spieler Nummer: ", playerNumb
                ,"Spieler Position: " ,playerPos);


    }
}
