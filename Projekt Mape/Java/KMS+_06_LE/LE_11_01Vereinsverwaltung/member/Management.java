package member;



public class Management extends Member {
    private final String administrationBody;

    public Management(int MID, String firstname, String lastname, String birth, String address, String mail, String entryDate, String unit, int experience, String administrationBody) {
        super(MID, firstname, lastname, birth, address, mail, entryDate, unit, experience);
        this.administrationBody = administrationBody;
    }

    public String getAdministrationBody() {
        return administrationBody;
    }

    @Override
    public String toString() {
        return super.toString()
                +String.format("║ %-20s ║ %-25s ║\n"
                ,"Verwaltungskörper:",administrationBody);
    }
}


