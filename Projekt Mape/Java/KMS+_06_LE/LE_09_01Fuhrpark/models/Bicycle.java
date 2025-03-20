package models;

public class Bicycle extends Vehicle {
    private int wheelSize;

    public Bicycle(int serialID, String brand, String model, String color, boolean status, int wheelSize) {
        super(serialID, brand, model, color, status);
        this.wheelSize = wheelSize;
    }

    public int getWheelSize() {
        return wheelSize;
    }

    public void setWheelSize(int wheelSize) {
        this.wheelSize = wheelSize;
    }

    @Override
    public String toString() {
        return  "Fahrrad:\n" + super.toString()+ "wheelSize=" + wheelSize + "\n";
    }
}