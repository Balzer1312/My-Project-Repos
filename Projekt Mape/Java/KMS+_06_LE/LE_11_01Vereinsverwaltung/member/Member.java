package member;

public abstract class Member {
    protected int MID;
    protected String firstname;
    protected String lastname;
    protected String birth;
    protected String address;
    protected String mail;
    protected String entryDate;
    protected String unit;
    protected int experience;

    public Member(int MID, String firstname, String lastname, String birth, String address, String mail, String entryDate, String unit, int experience) {
        this.MID = MID;
        this.firstname = firstname;
        this.lastname = lastname;
        this.birth = birth;
        this.address = address;
        this.mail = mail;
        this.entryDate = entryDate;
        this.unit = unit;
        this.experience= experience;
    }

    public int getMID() {
        return MID;
    }

    public String getFirstname() {
        return firstname;
    }

    public String getLastname() {
        return lastname;
    }

    public String getBirth() {
        return birth;
    }

    public String getAddress() {
        return address;
    }

    public String getMail() {
        return mail;
    }

    public String getEntryDate() {
        return entryDate;
    }

    public String getUnit() {
        return unit;
    }

    public int getExperience() {
        return experience;
    }

    @Override
    public String toString() {
        return String.format(
                "\n╔══════════════════════════════════════════════════╗\n"
                  +"║ %-48s ║\n"
                  +"╠══════════════════════╦═══════════════════════════╣\n"
                  +"║ %-20s ║ %-25d ║\n"
                  +"║ %-20s ║ %-25s ║\n"
                  +"║ %-20s ║ %-25s ║\n"
                  +"║ %-20s ║ %-25s ║\n"
                  +"║ %-20s ║ %-25s ║\n"
                  +"║ %-20s ║ %-25s ║\n"
                  +"║ %-20s ║ %-25s ║\n"
                  +"║ %-20s ║ %-25s ║\n"
                  +"║ %-20s ║ %-25d ║\n",
                "MITGLIEDSDETAILS",
                "ID:", MID,
                "Vorname:", firstname,
                "Nachname:", lastname,
                "Geburtsdatum:", birth,
                "Adresse:", address,
                "E-Mail:", mail,
                "Eintrittsdatum:", entryDate,
                "Mitgliedstyp:", unit,
                "Erfahrung (Jahre):", experience
        );
    }
}
