package member;



public class Treasurer extends Management {
    private final String financeArea;

    public Treasurer(int MID, String firstname, String lastname, String birth, String address, String mail, String entryDate, String unit, int experience, String administrationBody, String financeArea) {
        super(MID, firstname, lastname, birth, address, mail, entryDate, unit, experience, administrationBody);
        this.financeArea = financeArea;
    }

    public String getFinanceArea() {
        return financeArea;
    }

    @Override
    public String toString() {
        return super.toString()
                +String.format("║ %-20s ║ %-25s ║\n"
                +"╚══════════════════════╩═══════════════════════════╝\n"
                ,"Finanzbereich:", financeArea);

    }
}
