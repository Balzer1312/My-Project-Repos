package Vehicles;

public class Employee {
    protected int employeeId;
    protected String firstname;
    protected String lastname;
    protected String department;

    public Employee(int employeeId,String firstname, String lastname, String department) {
        this.employeeId = employeeId;
        this.firstname = firstname;
        this.lastname = lastname;
        this.department = department;
    }

    public int getEmployeeId() {
        return employeeId;
    }

    public String getFirstname() {
        return firstname;
    }

    public String getLastname() {
        return lastname;
    }

    @Override
    public String toString() {
        return "Mitarbeiter: \n"
                +"Name: " + firstname +" " +lastname + "\n"
                +"Abteilung: "+ department;
    }
}
