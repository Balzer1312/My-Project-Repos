package models;

public class Motorcycle extends Motorized {
    private int engineCapacity;

    public Motorcycle(int serialID, String brand, String model, String color, boolean status,
                      String fuelType, String mark, double consumption, int mileage, int engineCapacity) {
        super(serialID, brand, model, color, status, fuelType, mark, consumption, mileage);
        this.engineCapacity = engineCapacity;
    }

    public int getEngineCapacity() {
        return engineCapacity;
    }

    public void setEngineCapacity(int engineCapacity) {
        this.engineCapacity = engineCapacity;
    }

    @Override
    public String toString() {
        return " Motorrad: "+super.toString()+"Hubraum: " + engineCapacity+"cm³\n";

    }
}