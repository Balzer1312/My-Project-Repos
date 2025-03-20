package Vehicles;

public class Car extends Motorized {
    private final int seatNumb;

    public Car(int vehicleId, String brand, String model, String color, boolean status,
               String fuelType, double tanked ,double consumption, int mileage, int seatNumb) {
        super(vehicleId, brand, model, color, status, fuelType,tanked,consumption, mileage);
        this.seatNumb = seatNumb;
    }

    @Override
    public String toString() {
        return  " PKW: \n"
                + super.toString()
                +"doors=" + seatNumb +"\n"
                +"----------------------------------";

    }
}