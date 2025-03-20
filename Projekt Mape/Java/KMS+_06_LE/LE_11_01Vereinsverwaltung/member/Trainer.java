package member;

public class Trainer extends Member {
    private final String group;
    private final String trainingTypes;

    public Trainer(int MID, String firstname, String lastname, String birth, String address, String mail, String entryDate, String unit, String group, int experience, String trainingTypes) {
        super(MID, firstname, lastname, birth, address, mail, entryDate, unit, experience);
        this.group = group;
        this.trainingTypes = trainingTypes;
    }

    public String getGroup() {
        return group;
    }

    public String getTrainingTypes() {
        return trainingTypes;
    }

    @Override
    public String toString() {
        return super.toString()
                +String.format(
                 "║ %-20s ║ %-25s ║\n"
                +"║ %-20s ║ %-25s ║\n"
                +"╚══════════════════════╩═══════════════════════════╝\n"
                ,"Team Gruppe:" ,group
                ,"Training Art:" ,trainingTypes);



    }
}
