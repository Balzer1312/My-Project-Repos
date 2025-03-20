package bankClass;

import java.math.BigDecimal;
import java.time.LocalDate;

public class BankAccount {
    private int accountID;
    private String firstname;
    private String lastname;
    private LocalDate birth;
    private String address;
    private String iban;
    private BigDecimal value;
    public static int accountCount;



    public BankAccount(int accountID, String firstname, String lastname, LocalDate birth, String address, String iban, BigDecimal value) {
        this.accountID = accountID;
        this.firstname = firstname;
        this.lastname = lastname;
        this.birth = birth;
        this.address = address;
        this.iban = iban;
        this.value = value;
        accountCount++;
    }

    public int getAccountID() {
        return accountID;
    }

    public void setAccountID(int accountID) {
        this.accountID = accountID;
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

    public LocalDate getBirth() {
        return birth;
    }

    public void setBirth(LocalDate birth) {
        this.birth = birth;
    }

    public String getAdress() {
        return address;
    }

    public void setAdress(String adress) {
        this.address = adress;
    }

    public String getIban() {
        return iban;
    }

    public void setIban(String iban) {
        this.iban = iban;
    }

    public BigDecimal getValue() {
        return value;
    }

    public void setValue(BigDecimal value) {
        this.value = value;
    }

    public int getAccountCount() {
        return accountCount;
    }

    public void setAccountCount(int accountCount) {
        this.accountCount = accountCount;
    }

    @Override
    public String toString() {
        return "\nBankAccountMain:\n" +
                "Account ID: " + accountID + "\n"+
                "Name: " + firstname + " " + lastname + "\n"+
                "Geb.: " + birth +"\n"+
                "Adresse: " + address + "\n" +
                "IBAN: " + iban +"\n"+
                "Kontostand: " + value +"\n";
    }

}
