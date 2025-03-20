package modelsClass;

import java.time.LocalDate;

public class Trainer extends Member{
    private String group;
    private int experience;
    private String trainingTypes;

    public Trainer(int memberID, String firstname, String lastname, String birth, LocalDate entryDate, String group, int experience, String trainingTypes) {
        super(memberID, firstname, lastname, birth, entryDate);
        this.group=group;
        this.experience = experience;
        this.trainingTypes = trainingTypes;
    }

    public int getExperience() {
        return experience;
    }

    public void setExperience(int experience) {
        this.experience = experience;
    }

    public String getTrainingTypes() {
        return trainingTypes;
    }

    public void setTrainingTypes(String trainingTypes) {
        this.trainingTypes = trainingTypes;
    }

    @Override
    public String toString() {
        return "Trainer: \n"+super.toString()+
                "Gruppe: " +"Team-" +group +"\n"+
                "Erfahrung: "+ experience +" Jahre"+ "\n"+
                "Training art: " + trainingTypes+"\n\n";
    }
}
