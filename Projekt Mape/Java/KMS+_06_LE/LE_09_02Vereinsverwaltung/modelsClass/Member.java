package modelsClass;
import java.time.LocalDate;

public abstract class Member {
    private int memberID;
    private String firstname;
    private String lastname;
    private String birth;
    private LocalDate entryDate;
    private int memberCount = 0;


    public Member(int memberID, String firstname, String lastname, String birth, LocalDate entryDate) {
        this.memberID = memberID;
        this.firstname = firstname;
        this.lastname = lastname;
        this.birth = birth;
        this.entryDate = entryDate;
        this.memberCount++;
    }

    public int getMemberID() {
        return memberID;
    }

    public void setMemberID(int memberID) {
        this.memberID = memberID;
    }

    public String getFirstname() {
        return firstname;
    }

    public void setFirstname(String firstname) {
        this.firstname = firstname;
    }

    public String getLastname() {
        return lastname;
    }

    public void setLastname(String lastname) {
        this.lastname = lastname;
    }

    public String getBirth() {
        return birth;
    }

    public void setBirth(String birth) {
        this.birth = birth;
    }

    public LocalDate getEntryDate() {
        return entryDate;
    }

    public void setEntryDate(LocalDate entryDate) {
        this.entryDate = entryDate;
    }

    public int getMemberCount() {
        return memberCount;
    }

    @Override
    public String toString() {
        return "ID:"+ memberID+"\n"+
                "Name: " + firstname +" " +lastname + "\n"+
                "Geb.: " + birth +  "\n"+
                "Eintrittsdatum: " + entryDate + "\n";
    }
}

