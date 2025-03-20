package Vehicles;

public class Truck extends Motorized {
    private final int loadCapacity;

    public Truck(int vehicleId, String brand, String model, String color, boolean status,
                 String fuelType, double tanked ,double consumption, int mileage, int loadCapacity) {
        super(vehicleId, brand, model, color, status, fuelType, tanked ,consumption, mileage);
        this.loadCapacity = loadCapacity;
    }

    @Override
    public String toString() {
        return  " LKW: \n"
                + super.toString()
                +"Tragelast:" + loadCapacity + " t\n"
                +"----------------------------------";


    }
}