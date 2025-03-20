package DBUtils;

import Rental.RentInfo;
import DisplayOut.ShowDataToDisplay;
import Vehicles.*;

import java.math.BigDecimal;
import java.sql.*;
import java.util.ArrayList;
import java.util.List;


public class DBHandler {
    private final ShowDataToDisplay showDashboard = new ShowDataToDisplay();
    private final DBUtils.DBConfig dbConfig;

    public DBHandler() {
        this.dbConfig = DBConfig.getInstance();
    }
//##################################### Daten von der DB laden #######################################

    public List<Vehicle> getVehicleData() {
        List<Vehicle> vehicles = new ArrayList<>();

        String sql = "SELECT * FROM Vehicles";

        try (Connection conn = dbConfig.getConnection();
        Statement stmt = conn.createStatement();
        ResultSet rs = stmt.executeQuery(sql)) {

            while (rs.next()) {
                int vehicleId = rs.getInt("vehicle_id");
                String brand = rs.getString("brand");
                String model = rs.getString("model");
                String color = rs.getString("color");
                boolean status = rs.getBoolean("status");
                String type = rs.getString("type");


                int mileage = rs.getInt("mileage");
                String fuelType = rs.getString("fuelType");
                double tanked = rs.getDouble("tanked");
                double consumption = rs.getDouble("consumption");


                int loadCapacity  = rs.getInt("loadCapacity");
                int engineCapacity = rs.getInt("engineCapacity");
                int seatNumb = rs.getInt("seatNumb");
                int wheelSize = rs.getInt("weehlSize");

                Vehicle v = null;

                switch (type) {
                    case "Car":
                        v = new Car(vehicleId, brand, model, color, status,fuelType ,tanked ,consumption, mileage, seatNumb);
                        break;
                    case "Truck":
                        v = new Truck(vehicleId, brand, model, color, status,fuelType ,tanked ,consumption, mileage, loadCapacity);
                        break;
                    case "Motorcycle":
                        v = new Motorcycle(vehicleId, brand, model, color, status,fuelType ,tanked ,consumption, mileage, engineCapacity);
                        break;
                    case "Bicycle":
                        v = new Bicycle(vehicleId, brand, model, color, status, wheelSize);
                        break;
                    default:
                        showDashboard.showError("Unbekannter Fahrzeugtyp: " + type);
                        break;
                }

                if (v != null) {
                    vehicles.add(v);
                }
            }

        } catch (SQLException e) {
                showDashboard.showError("Fehler beim Laden der Daten: " + e.getMessage());
        }
        return vehicles;
    }

    public List<Employee> getEmployeeData(){
        List<Employee> employees = new ArrayList<>();
        String sql = "SELECT * FROM Employees";

        try (Connection conn = dbConfig.getConnection();
             Statement stmt = conn.createStatement();
             ResultSet rs = stmt.executeQuery(sql)) {

            Employee e;
            while (rs.next()) {
                // Lies die Werte aus dem ResultSet
                int employeeId = rs.getInt("employee_id");
                String firstname = rs.getString("first_name");
                String lastname = rs.getString("last_name");
                String department = rs.getString("department");
                e = new Employee(employeeId, firstname, lastname, department);
                employees.add(e);

            }

        } catch(SQLException e){
            showDashboard.showError("Fehler beim Laden der Daten: " + e.getMessage());
        }
        return employees;
    }

    public List<RentInfo> getRentalData(){
        List<RentInfo> rentals = new ArrayList<>();
        String sql = "SELECT * FROM view_rental_info";

        try (Connection conn = dbConfig.getConnection();
             Statement stmt = conn.createStatement();
             ResultSet rs = stmt.executeQuery(sql)) {

            while (rs.next()) {

                int rentalId = rs.getInt("rental_id");
                int employeeId = rs.getInt("employee_id");
                String firstName = rs.getString("first_name");
                String lastName = rs.getString("last_name");
                int vehicleId = rs.getInt("vehicle_id");
                String brand = rs.getString("brand");
                String model = rs.getString("model");
                String type = rs.getString("type");
                String dateFrom  = rs.getString("date_from");
                String dateTo = rs.getString("date_to");
                Integer drivenKm = (Integer) rs.getObject("driven_km");
                BigDecimal tankedValue = rs.getBigDecimal("tanked");
                Double tanked = (tankedValue != null) ? tankedValue.doubleValue() : null;


                RentInfo rentInfo = new RentInfo(rentalId, employeeId, firstName, lastName,vehicleId,
                        brand, model, type, dateFrom, dateTo, drivenKm, tanked);

                rentals.add(rentInfo);
            }



        } catch(SQLException e){
            showDashboard.showError("Fehler beim Laden der Daten: " + e.getMessage());
        }
        return rentals;
    }

//#################################### Fahrzeug zur DB übertragen ##############################################

    public void insertVehicle(String brand, String model, String color, String type, boolean status,
                              Integer mileage, String fuelType, Double tanked, Double consumption,
                              Integer loadCapacity, Integer engineCapacity, Integer seatNumb, Integer wheelSize) {
        String sql = "{CALL insertVehicle(?,?,?,?,?,?,?,?,?,?,?,?,?)}"; // 13 Parameter

        try (Connection conn = dbConfig.getConnection();
             CallableStatement cstmt = conn.prepareCall(sql)) {

            cstmt.setString(1, brand);
            cstmt.setString(2, model);
            cstmt.setString(3, color);
            cstmt.setString(4, type);
            cstmt.setBoolean(5, status);

            // mileage
            if (mileage == null) cstmt.setNull(6, Types.INTEGER);
            else cstmt.setInt(6, mileage);

            // fuelType
            if (fuelType == null) cstmt.setNull(7, Types.VARCHAR);
            else cstmt.setString(7, fuelType);

            // tanked
            if (tanked == null) cstmt.setNull(8, Types.DECIMAL);
            else cstmt.setDouble(8, tanked);

            // consumption
            if (consumption == null) cstmt.setNull(9, Types.DECIMAL);
            else cstmt.setDouble(9, consumption);

            // loadCapacity
            if (loadCapacity == null) cstmt.setNull(10, Types.INTEGER);
            else cstmt.setInt(10, loadCapacity);

            // engineCapacity
            if (engineCapacity == null) cstmt.setNull(11, Types.INTEGER);
            else cstmt.setInt(11, engineCapacity);

            // seatNumb
            if (seatNumb == null) cstmt.setNull(12, Types.INTEGER);
            else cstmt.setInt(12, seatNumb);

            // wheelSize
            if (wheelSize == null) cstmt.setNull(13, Types.INTEGER);
            else cstmt.setInt(13, wheelSize);

            cstmt.execute();



        } catch (SQLException e) {
            showDashboard.showError("Fehler beim Übertragen der Daten: " + e.getMessage());
        }
    }

//########################################## Fahrzeug aus DB Löschen ##########################################################

    public void deleteVehicle (int vehicleId){


        String sql = "{CALL deleteVehicle(?)}";

        try (Connection conn = dbConfig.getConnection();
             CallableStatement cstmt = conn.prepareCall(sql)) {

            cstmt.setInt(1, vehicleId);
            cstmt.execute();

        } catch (SQLException e) {
            showDashboard.showError("Fehler beim Laden der Daten: " + e.getMessage());
        }
    }

    public void insertEmployee (String firstName, String lastName, String department){
        String sql = "{CALL insertEmployee(?,?,?)}";

        try (Connection conn = dbConfig.getConnection();
             CallableStatement cstmt = conn.prepareCall(sql)) {

            cstmt.setString(1, firstName);
            cstmt.setString(2, lastName);
            cstmt.setString(3, department);

            cstmt.execute();

        } catch (SQLException e) {
            showDashboard.showError("Fehler beim Übertragen der Daten: " + e.getMessage());

        }
    }

    public void rentVehicle(int employeeId, int vehicleId, String dateFromStr) {

        String sql = "{CALL rentVehicle(?,?,?)}";

        try (Connection conn = dbConfig.getConnection();
             CallableStatement cstmt = conn.prepareCall(sql)) {

            cstmt.setInt(1, employeeId);
            cstmt.setInt(2, vehicleId);
            cstmt.setString(3, dateFromStr);
            cstmt.execute();

        } catch (SQLException e) {
            showDashboard.showError("Fehler beim Übertragen der Daten: " + e.getMessage());
        }
    }

    public void vehicleReturned(int rentalId, int drivenKm, double tanked, String dateToStr) {
        String sql = "{CALL vehicleReturned(?,?,?,?)}";

        try (Connection conn = dbConfig.getConnection();
             CallableStatement cstmt = conn.prepareCall(sql)) {

            cstmt.setInt(1, rentalId);
            cstmt.setInt(2, drivenKm);
            cstmt.setDouble(3, tanked);
            cstmt.setString(4, dateToStr);
            cstmt.execute();


        } catch (SQLException e) {
            showDashboard.showError("Fehler beim Übertragen der Daten: " + e.getMessage());
        }
    }
}




