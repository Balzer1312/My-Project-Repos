package modelsClass;

import java.time.LocalDate;

public class Treasurer extends Management{
    private String financeArea;

    public Treasurer(int memberID, String firstname, String lastname, String birth, LocalDate entryDate, String administrationBody, String financeArea) {
        super(memberID, firstname, lastname, birth, entryDate, administrationBody);
        this.financeArea = financeArea;
    }

    public String getFinanceArea() {
        return financeArea;
    }

    public void setFinanceArea(String financeArea) {
        this.financeArea = financeArea;
    }

    @Override
    public String toString() {
        return super.toString()+"Finanzbereich: " +financeArea +"\n";

    }
}
