package modelsClass;

import java.time.LocalDate;

public class Player extends Member{
    private String group;
    private int playerNumb;
    private String pos;

    public Player(int memberID, String firstname, String lastname, String birth, LocalDate entryDate, String group, int playerNumb, String pos) {
        super(memberID, firstname, lastname, birth, entryDate);
        this.group = group;
        this.playerNumb = playerNumb;
        this.pos = pos;
    }

    public int getPlayerNumb() {
        return playerNumb;
    }

    public void setPlayerNumb(int playerNumb) {
        this.playerNumb = playerNumb;
    }

    public String getPos() {
        return pos;
    }

    public void setPos(String pos) {
        this.pos = pos;
    }

    @Override
    public String toString() {
        return "Spieler: \n"+super.toString()+
                "Gruppe: " +"Team-" +group +"\n"+
                "Position:"+ pos + "\n"+
                "Spieler Nummer: " + playerNumb+"\n\n";
    }
}
