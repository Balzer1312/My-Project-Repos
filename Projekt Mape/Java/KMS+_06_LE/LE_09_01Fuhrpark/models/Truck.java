package models;

public class Truck extends Motorized {
    private int loadCapacity;

    public Truck(int serialID, String brand, String model, String color, boolean status,
                 String fuelType, String mark, double consumption, int mileage, int loadCapacity) {
        super(serialID, brand, model, color, status, fuelType, mark, consumption, mileage);
        this.loadCapacity = loadCapacity;
    }

    public int getLoadCapacity() {
        return loadCapacity;
    }

    public void setLoadCapacity(int loadCapacity) {
        this.loadCapacity = loadCapacity;
    }

    @Override
    public String toString() {
        return  " LKW:\n" + super.toString() +"Tragelast:" + loadCapacity + " kg\n";


    }
}