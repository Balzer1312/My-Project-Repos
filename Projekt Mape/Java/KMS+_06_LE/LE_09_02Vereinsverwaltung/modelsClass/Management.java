package modelsClass;

import java.time.LocalDate;

public class Management extends Member{
    private String administrationBody;

    public Management(int memberID, String firstname, String lastname, String birth, LocalDate entryDate, String administrationBody) {
        super(memberID, firstname, lastname, birth, entryDate);
        this.administrationBody = administrationBody;
    }

    public String getAdministrationBody() {
        return administrationBody;
    }

    public void setAdministrationBody(String administrationBody) {
        this.administrationBody = administrationBody;
    }

    @Override
    public String toString() {
        return administrationBody +":\n"+super.toString();
    }
}
