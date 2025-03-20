package Vehicles;

public class Motorized extends Vehicle {
    protected int mileage;
    protected String fuelType;
    protected double tanked;
    protected double consumption;

    public Motorized(int vehicleId, String brand, String model, String color, boolean status,
                     String fuelType, double tanked ,double consumption, int mileage) {
        super(vehicleId, brand, model, color, status);
        this.fuelType = fuelType;
        this.tanked = tanked;
        this.consumption = consumption;
        this.mileage = mileage;
    }

    public String getFuelType() {
        return fuelType;
    }

    public double getConsumption() {
        return consumption;
    }

    public int getMileage() {
        return mileage;
    }

    @Override
    public String toString() {
        return super.toString()
                +"Treibstoff: " + fuelType + "\n"
                +"Getankte Menge: "+ tanked +"\n"
                +"Verbrauch: " + consumption + " l\\100km\n"
                +"Kilometerstand: " + mileage + "km\n";

    }

}
