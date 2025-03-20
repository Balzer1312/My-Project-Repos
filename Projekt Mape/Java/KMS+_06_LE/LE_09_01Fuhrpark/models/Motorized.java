package models;

public class Motorized extends Vehicle {
    protected String fuelType;
    protected String mark;
    protected double consumption;
    protected int mileage;

    private static double totalPetrol= 0;
    private static double totalDiesel=0;
    private static double totalPower=0;

    public Motorized(int serialID, String brand, String model, String color, boolean status,
                     String fuelType, String mark, double consumption, int mileage) {
        super(serialID, brand, model, color, status);
        this.fuelType = fuelType;
        this.mark = mark;
        this.consumption = consumption;
        this.mileage = mileage;
    }

    public String getFuelType() {
        return fuelType;
    }

    public void setFuelType(String fuelType) {
        this.fuelType = fuelType;
    }

    public String getMark() {
        return mark;
    }

    public void setMark(String mark) {
        this.mark = mark;
    }

    public double getConsumption() {
        return consumption;
    }

    public void setConsumption(double consumption) {
        this.consumption = consumption;
    }

    public int getMileage() {
        return mileage;
    }

    public void setMileage(int mileage) {
        this.mileage = mileage;
    }

    @Override
    public String toString() {
        return super.toString() +
                "Treibstoff: " + fuelType + "\n" +
                "Kennzeichen: " + mark + "\n" +
                "Verbrauch: " + consumption + " l\\100km\n"+
                "Kilometerstand: " + mileage + "km\n";

    }

    public void refuel(double amount,String fuelType) {
        if (amount <= 0) {
            System.out.println("\nUngültige Menge! Geben Sie eine positive Zahl ein.");
            return;
        }

        // Gesamtverbrauch pro Treibstoffart erhöhen
        switch (fuelType.toLowerCase()) {
            case "benzin" -> totalPetrol += amount;
            case "diesel" -> totalDiesel += amount;
            case "strom"  -> totalPower += amount;
            default -> System.out.println("Unbekannter Treibstofftyp: " + fuelType);
        }

        System.out.println("Erfolgreich " + amount + "L " + fuelType + " getankt.");
    }

}
