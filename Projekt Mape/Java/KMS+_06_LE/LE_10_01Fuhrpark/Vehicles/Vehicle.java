package Vehicles;

public abstract class Vehicle {
    protected int vehicleId;
    protected String brand;
    protected String model;
    protected String color;
    protected boolean status;
    public static int vehicleCount = 0;



    public Vehicle(int vehicleId, String brand, String model, String color, boolean status) {
        this.vehicleId = vehicleId;
        this.brand = brand;
        this.model = model;
        this.color = color;
        this.status = status;
        vehicleCount++;
    }

    public int getVehicleId() {
        return vehicleId;
    }

    public String getBrand() {
        return brand;
    }

    public String getModel() {
        return model;
    }

    public String getColor() {
        return color;
    }

    public boolean getRentStatus() {
        return status;
    }

    @Override
    public String toString() {
        return "Seriennummer: " + vehicleId + "\n"
                +"Marke: " + brand +  "\n"
                +"Modell: " + model + "\n"
                +"Farbe: " + color + "\n"
                +"Status: " + (status ? "Frei" : "Geliehen")+"\n";

    }
}

