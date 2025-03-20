package modelsClass;

import java.time.LocalDate;

public class Manager extends Management{
    private String competence;


    public Manager(int memberID, String firstname, String lastname, String birth, LocalDate entryDate, String administrationBody,String competence) {
        super(memberID, firstname, lastname, birth, entryDate, administrationBody);
        this.competence = competence;
    }

    public String getCompetence() {
        return competence;
    }

    public void setCompetence(String competence) {
        this.competence = competence;
    }

    @Override
    public String toString() {
        return super.toString()+"Zuständigkeit: "+competence+"\n\n";
    }
}
