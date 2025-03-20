package FleetManager;

import Rental.RentInfo;
import DisplayOut.ShowDataToDisplay;
import Vehicles.*;
import DBUtils.DBHandler;
import java.util.List;
import java.util.Scanner;

public class FleetDataManager {
    private final ValidData validData;
    private final ShowDataToDisplay showDataToDisplay;
    private final DBHandler dbHandler;
    private List<Vehicle>vehicleListFromDB;
    private List<Employee>employees;
   private List<RentInfo>rentalData;


    public FleetDataManager() {
        this.validData = new ValidData();
        this.showDataToDisplay = new ShowDataToDisplay();
        this.dbHandler = new DBHandler();
        this.vehicleListFromDB = dbHandler.getVehicleData();
        this.employees=dbHandler.getEmployeeData();
       this.rentalData=dbHandler.getRentalData();
    }

    public void addVehicle(Scanner scanner){
        int choice;
        Integer mileage = null;
        Integer loadCapacity = null;
        Integer engineCapacity = null;
        Integer seatNumb = null;
        Integer wheelSize = null;
        String fuelType = null;
        String type;
        Double consumption=null;
        Double tanked=null;
        boolean status=true;

        try {
        showDataToDisplay.showVehicleType();

            while (true) {
                choice = validData.getInt(scanner, "Bitte wählen Sie 1-5: ");
                if (choice >= 1 && choice <= 5) {
                    if (choice == 5) return;
                    break;
                } else {
                    showDataToDisplay.showError("Ungültige Eingabe (1-5)!");
                }
            }


            String brand = validData.getString(scanner, "Marke eingeben: ");
            String model = validData.getString(scanner, "Modell eingeben: ");
            String color = validData.getString(scanner, "Farbe eingeben: ");

            switch (choice) {
                case 1: //PKW
                    type = "Car";
                    mileage = validData.getInt(scanner, "Kilometerstand: ");
                    fuelType = validData.getfuelType(scanner);
                    tanked = validData.getDouble(scanner, "Bisher getankt (in Litern): ");
                    consumption = validData.getDouble(scanner, "Verbrauch (L/100km): ");
                    seatNumb = validData.getInt(scanner, "Anzahl der Sitze: ");
                    break;

                case 2: // LKW
                    type = "Truck";
                    // Motorisierte Felder
                    mileage = validData.getInt(scanner, "Kilometerstand: ");
                    fuelType = validData.getfuelType(scanner);
                    tanked = validData.getDouble(scanner, "Bisher getankt (in Litern): ");
                    consumption = validData.getDouble(scanner, "Verbrauch (L/100km): ");
                    loadCapacity = validData.getInt(scanner, "Ladekapazität (in Tonnen): ");
                    break;

                case 3: // Motorrad
                    type = "Motorcycle";
                    // Motorisierte Felder
                    mileage = validData.getInt(scanner, "Kilometerstand: ");
                    fuelType = validData.getfuelType(scanner);
                    tanked = validData.getDouble(scanner, "Bisher getankt (in Litern): ");
                    consumption = validData.getDouble(scanner, "Verbrauch (L/100km): ");
                    engineCapacity = validData.getInt(scanner, "Hubraum (ccm): ");
                    break;

                case 4: // Fahrrad
                    type = "Bicycle";
                    wheelSize = validData.getInt(scanner, "Radgröße (Zoll): ");
                    break;

                default:
                    System.out.println("Ungültige Auswahl!");
                    return;
            }

            // Jetzt rufen wir eine einzige DB-Methode auf
            dbHandler.insertVehicle(
                    brand, model, color, type, status,
                    mileage, fuelType, tanked, consumption,
                    loadCapacity, engineCapacity, seatNumb, wheelSize
            );
            showDataToDisplay.showMessage("Fahrzeug wurde erfolgreich angelegt!");
            refreshVehicleList();


        }catch (Exception e){
                showDataToDisplay.showError("Fehler beim Hinzufügen des Fahrzeugs:" +e.getMessage());
        }

    }

    public void addEmployee(Scanner scanner){

        try{
            String firstname= validData.isValidName(scanner,"Vorname eingeben: ");
            String lastname= validData.isValidName(scanner,"Nachnamen eingeben :");
            String department = validData.getString(scanner,"In welcher Abteilung arbeiten sie: ");
            dbHandler.insertEmployee(firstname,lastname,department);
            refreshEmployeeList();

        } catch (Exception e) {
            throw new RuntimeException(e);

        }
    }

    public void deleteVehicle(Scanner scanner){

        try{
            showDataToDisplay.showVehiclesInfos(vehicleListFromDB);
            int deleteOnID=validData.getExistVehicleID(scanner,"Bitte geben die die Fahrzeugs ID ein: ",vehicleListFromDB);
            dbHandler.deleteVehicle(deleteOnID);
            refreshVehicleList();



        }catch (Exception e){
            showDataToDisplay.showError("Fehler beim Löschen des Fahrzeugs:" +e.getMessage());
        }

    }

    public void rentVehicle(Scanner scanner){
        int vehicleId, employeeId;
        String dateFromStr;
        try {
            showDataToDisplay.showVehiclesAvailableRent(vehicleListFromDB);
            vehicleId = validData.getInt(scanner, "Fahrzeug ID: ");

           showDataToDisplay.showMessage("Bitte geben Sie die Mitarbeiter ID ein");
           employeeId= validData.getExistEmployeeID(scanner,"Mitarbeiter ID: ",employees);
           dateFromStr=validData.getDateForm(scanner,"Ab wann wird das Fahrzeug ausgeliehen? (Format: DD.MM.YYYY)");
            dbHandler.rentVehicle(employeeId, vehicleId, dateFromStr);
            refreshRentInfoList();
            refreshVehicleList();

        }catch (Exception e){
            showDataToDisplay.showError("Fehler :" +e.getMessage());
        }

    }

    public void vehicleReturned(Scanner scanner){
        int rentalID, drivenKm;
        double tanked;
        String dateToStr;
        try {
            showDataToDisplay.showCurrentRentalVehicle(rentalData);
            rentalID=validData.getExistingAktivRentalID(scanner,"Bitte geben Sie die Vorgangs ID ein: ",rentalData);
            drivenKm = validData.getInt(scanner, "Gefahrene Kilometer: ");
            tanked = validData.getDouble(scanner, "Getankt (Liter): ");
            dateToStr = validData.getDateForm(scanner, "Rückgabedatum (Format: DD.MM.YYYY): ");

            dbHandler.vehicleReturned(rentalID, drivenKm, tanked, dateToStr);
            showDataToDisplay.showMessage("\nFahrzeug wurde zurück gebracht!\n");


        } catch (Exception e) {
            showDataToDisplay.showError("Fehler :" +e.getMessage());
        }

    }

    public void showVehicleToDisplay(){
        showDataToDisplay.showFleetData(vehicleListFromDB);
    }

    public void showIndividualVehicleData(Scanner scanner){
        try {
            showDataToDisplay.showVehiclesInfos(vehicleListFromDB);
            int idToShow= validData.getExistVehicleID(scanner,"Bitte geben die die Fahrzeugs ID ein: ",vehicleListFromDB);
            Vehicle vehicleData = validData.findVehicleById(idToShow,vehicleListFromDB);
            showDataToDisplay.showMessage(vehicleData.toString());

        } catch (Exception e) {
            showDataToDisplay.showError("Fehler :" +e.getMessage());

        }
    }

    public void showRentalData(){
        showDataToDisplay.showTotalRentalData(rentalData);
    }

    public void showIndividualRentData(Scanner scanner){
        try {
            showDataToDisplay.showRentalInfos(rentalData);
            int idToShow= validData.getExistingRentalData(scanner,"Bitte geben die die Fahrzeugs ID ein: ",rentalData);
            RentInfo rentInfo = validData.findRentalInfoByID(idToShow,rentalData);
            showDataToDisplay.showMessage(rentInfo.toString());

        } catch (Exception e) {
            showDataToDisplay.showError("Fehler :" +e.getMessage());

        }
    }

    private void refreshVehicleList(){
        vehicleListFromDB.clear();
        vehicleListFromDB=dbHandler.getVehicleData();
        showDataToDisplay.showMessage("Liste wurde aktualisiert!");
    }

    private void refreshEmployeeList(){
        employees.clear();
        employees=dbHandler.getEmployeeData();
        showDataToDisplay.showMessage("Liste wurde aktualisiert!");

    }

    private void refreshRentInfoList(){
        rentalData.clear();
        rentalData= dbHandler.getRentalData();
        refreshVehicleList();
    }


}
