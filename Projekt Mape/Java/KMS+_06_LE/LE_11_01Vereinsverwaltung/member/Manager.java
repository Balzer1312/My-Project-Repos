package member;

public class Manager extends Management {
    private final String competence;

    public Manager(int MID, String firstname, String lastname, String birth, String address, String mail, String entryDate, String unit, int experience, String administrationBody, String competence) {
        super(MID, firstname, lastname, birth, address, mail, entryDate, unit, experience, administrationBody);
        this.competence = competence;
    }

    public String getCompetence() {
        return competence;
    }

    @Override
    public String toString() {
        return super.toString()
                +String.format("║ %-20s ║ %-25s ║\n"
                +"╚══════════════════════╩═══════════════════════════╝\n"
                ,"Kompetenz:",competence);

    }
}
