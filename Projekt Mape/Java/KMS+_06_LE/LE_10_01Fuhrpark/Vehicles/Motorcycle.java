package Vehicles;

public class Motorcycle extends Motorized {
    private final int engineCapacity;

    public Motorcycle(int vehicleId, String brand, String model, String color, boolean status,
                      String fuelType, double tanked,double consumption, int mileage, int engineCapacity) {
        super(vehicleId, brand, model, color, status, fuelType, tanked,consumption, mileage);
        this.engineCapacity = engineCapacity;
    }

    @Override
    public String toString() {
        return " Motorrad: "
                +super.toString()
                +"Hubraum: " + engineCapacity+"cm³\n"
                +"----------------------------------";

    }
}