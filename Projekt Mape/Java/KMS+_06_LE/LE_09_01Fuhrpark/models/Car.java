package models;

public class Car extends Motorized {
    private int doors;

    public Car(int serialID, String brand, String model, String color, boolean status,
               String fuelType, String mark, double consumption, int mileage, int doors) {
        super(serialID, brand, model, color, status, fuelType, mark, consumption, mileage);
        this.doors = doors;
    }

    public int getDoors() {
        return doors;
    }

    public void setDoors(int doors) {
        this.doors = doors;
    }

    @Override
    public String toString() {
        return  " PKW:\n" + super.toString() +"doors=" + doors +"\n";

    }
}