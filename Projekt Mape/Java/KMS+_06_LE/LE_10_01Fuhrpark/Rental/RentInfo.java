package Rental;

public class RentInfo {
    private final int rentalId;
    private final int employeeId;
    private final String firstName;
    private final String lastName;
    private final int vehicleId;
    private final String brand;
    private final String model;
    private final String type;
    private final String dateFrom;
    private final String dateTo;
    private final Integer drivenKm;
    private final Double tanked;

    public RentInfo(int rentalId, int employeeId, String firstName, String lastName,
                    int vehicleId, String brand, String model, String type,
                    String dateFrom, String dateTo, Integer drivenKm, Double tanked) {
        this.rentalId = rentalId;
        this.employeeId = employeeId;
        this.firstName = firstName;
        this.lastName = lastName;
        this.vehicleId = vehicleId;
        this.brand = brand;
        this.model = model;
        this.type = type;
        this.dateFrom = dateFrom;
        this.dateTo = dateTo;
        this.drivenKm = drivenKm;
        this.tanked = tanked;
    }

    public int getRentalId() {
        return rentalId;
    }

    public int getVehicleId() {
        return vehicleId;
    }

    public String getBrand() {
        return brand;
    }

    public String getModel() {
        return model;
    }

    public String getDateTo() {
        return dateTo;
    }

    // Falls es Null Werte gibt, wird ein Text übergeben
    private String fallback(Object value) {
        return (value == null)? "Noch nicht Angegeben": value.toString();
    }


    @Override
    public String toString() {
        return "Verleih Info:\n"
                + "-------------------------------------------------\n"
                + "Vorgangs ID : " + rentalId + "\n"
                + "Mitarbeiter ID: " + employeeId + "\n"
                + "Mitarbeiter Name: " + firstName + " " + lastName + "\n"
                + "Fahrzeug ID: " + vehicleId + "\n"
                + "Marke: " + brand + "\n"
                + "Modell: " + model + "\n"
                + "Fahrzeugtyp: " + type + "\n"
                + "Auslesebeginn: " + dateFrom + "\n"
                + "Rückgabedatum : " + fallback(dateTo) + "\n"
                + "Gefahrene Kilometer: " + fallback(drivenKm)+ "\n"
                + "Getankt: " +(tanked != null? fallback(tanked) +" l": fallback(tanked)) +"\n"
                + "-------------------------------------------------\n";
    }
}
