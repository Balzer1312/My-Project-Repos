package DBUtils;

import DisplayOut.ShowDataToDisplay;

import java.io.IOException;
import java.io.InputStream;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.util.Properties;


public class DBConfig {
    private final ShowDataToDisplay showDashboard = new ShowDataToDisplay();
    private static DBConfig instance; // Singleton-Instanz
    private String dbUrl;
    private String user;
    private String password;

    private DBConfig() {
        loadConfig();
    }

    public static DBConfig getInstance() {
        if (instance == null) {
            instance = new DBConfig();
        }
        return instance;
    }

    private void loadConfig() {
        Properties props = new Properties();
        try (InputStream input = getClass().getClassLoader().getResourceAsStream("DBUtils/config.properties")) {
            props.load(input);
            dbUrl = props.getProperty("db.url", "jdbc:mysql://localhost:3306/carpool");
            user = props.getProperty("db.user", "root");
            password = props.getProperty("db.password", "");

            showDashboard.showMessage("DB-Konfiguration erfolgreich geladen.");
        } catch (IOException e) {
            showDashboard.showError("Fehler beim Laden der DB-Konfiguration: " + e.getMessage());
        }
    }

    public Connection getConnection() throws SQLException {
        return DriverManager.getConnection(dbUrl, user, password);
    }
}


