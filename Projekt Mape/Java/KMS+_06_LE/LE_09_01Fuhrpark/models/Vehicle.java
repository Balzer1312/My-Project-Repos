package models;

public class Vehicle {
    protected int serialID;
    protected String brand;
    protected String model;
    protected String color;
    protected boolean status;
    public static int vehicleCount = 0;

    public Vehicle(int serialID, String brand, String model, String color, boolean status) {
        this.serialID = serialID;
        this.brand = brand;
        this.model = model;
        this.color = color;
        this.status = status;
        vehicleCount++;
    }

    public int getSerialID() {
        return serialID;
    }

    public void setSerialID(int serialID) {
        this.serialID = serialID;
    }

    public String getBrand() {
        return brand;
    }

    public void setBrand(String brand) {
        this.brand = brand;
    }

    public String getModel() {
        return model;
    }

    public void setModel(String model) {
        this.model = model;
    }

    public String getColor() {
        return color;
    }

    public void setColor(String color) {
        this.color = color;
    }

    public boolean isStatus() {
        return status;
    }

    public void setStatus(boolean status) {
        this.status = status;
    }

    @Override
    public String toString() {
        return "Seriennummer: " + serialID + "\n"+
                "Marke: " + brand +  "\n"+
                "Modell: " + model + "\n" +
                "Farbe: " + color + "\n" +
                "Status: " + (status ? "Frei" : "Geliehen")+"\n";

    }
}