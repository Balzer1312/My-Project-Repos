package Vehicles;

public class Bicycle extends Vehicle {
    private final int weehlSize;

    public Bicycle(int vehicleId, String brand, String model, String color, boolean status, int weehlSize) {
        super(vehicleId, brand, model, color, status);
        this.weehlSize = weehlSize;
    }



    @Override
    public String toString() {
        return  "Fahrrad: \n"
                + super.toString()
                + "Radgröße :" + weehlSize + "\n"
                +"----------------------------------";
    }
}