package DBUtilis;

import interfaceGUI.ShowDashboard;
import musicClass.*;
import java.sql.*;
import java.util.*;

public class DBHandler {
    private final ShowDashboard showDashboard = new ShowDashboard();
    private final DBConfig dbConfig;

    public DBHandler() {
        this.dbConfig = DBConfig.getInstance();
    }

    public Map<Album, List<Track>> loadAlbumsFromDB() {
        Map<Album, List<Track>> albumTracks = new HashMap<>();
        String sql = "SELECT * FROM album_tracks_view";

        try (Connection conn = dbConfig.getConnection()) {

            try (PreparedStatement stmt = conn.prepareStatement(sql);
                 ResultSet rs = stmt.executeQuery()) {

                while (rs.next()) {
                    // Album erstellen
                    Album album = new Album(
                            rs.getInt("album_id"),
                            rs.getString("publisher"),
                            rs.getString("album_title"),
                            rs.getString("album_genre")
                    );
                    albumTracks.put(album, new ArrayList<>());

                    // Falls Tracks vorhanden sind
                    String trackIds = rs.getString("track_ids");
                    if (trackIds != null && !trackIds.equalsIgnoreCase("NULL")) {
                        String[] ids = trackIds.split("\\|");
                        String[] titles = rs.getString("track_titles").split("\\|");
                        String[] interpreters = rs.getString("interpreters").split("\\|");
                        String[] genres = rs.getString("track_genres").split("\\|");
                        String[] lengths = rs.getString("track_lengths").split("\\|");

                        for (int i = 0; i < ids.length; i++) {
                            albumTracks.get(album).add(new Track(
                                    Integer.parseInt(ids[i]),
                                    titles[i],
                                    interpreters[i],
                                    genres[i],
                                    Integer.parseInt(lengths[i])
                            ));


                        }
                    }
                }
            }

            showDashboard.showMessage("Alben & Tracks erfolgreich aus der DB geladen.");

        } catch (SQLException e) {
            showDashboard.showError("Fehler beim Laden der Daten: " + e.getMessage());
        }

        return albumTracks;
    }

    // Album der DB übertragen (Call Anweisung ist für das Aufrufen einer SQL PROCEDURE)
    public void addAlbumToDB(String publisher, String title,String genre){
        String sql = "CALL add_album(?, ?, ?)";

        try (Connection conn = dbConfig.getConnection();
             PreparedStatement stmt = conn.prepareStatement(sql)) {

            stmt.setString(1, publisher);
            stmt.setString(2, title);
            stmt.setString(3, genre);
            stmt.executeUpdate();

            showDashboard.showMessage("Album erfolgreich erstellt: " + title + " (Publisher: " + publisher + ")\n");

        } catch (SQLException e) {
            showDashboard.showError("Fehler beim Erstellen des Albums: " + e.getMessage());
        }
    }


    public void addTrackToDB(String title, String interpreter, String genre, int length, int albumId){
        String sql = "CALL add_track(?, ?, ?, ?, ?)"; // Aufruf der gespeicherten Prozedur

        try (Connection conn = dbConfig.getConnection();
             PreparedStatement stmt = conn.prepareStatement(sql)) {

            stmt.setString(1, title);
            stmt.setString(2, interpreter);
            stmt.setString(3, genre);
            stmt.setInt(4, length);
            stmt.setInt(5, albumId);
            stmt.executeUpdate();

            showDashboard.showMessage("Track erfolgreich hinzugefügt: " + title+"\n");

        } catch (SQLException e) {
            showDashboard.showError("Fehler beim Hinzufügen des Tracks: " + e.getMessage());
        }
    }


    public void deleteAlbum(int albumId) {
        String sql = "CALL delete_album(?)";

        try (Connection conn = dbConfig.getConnection();
             PreparedStatement stmt = conn.prepareStatement(sql)) {

            stmt.setInt(1, albumId);
            stmt.executeUpdate();

            showDashboard.showMessage("Album erfolgreich gelöscht: ID " + albumId+"\n");

        } catch (SQLException e) {
            showDashboard.showError("Fehler beim Löschen des Albums: " + e.getMessage());
        }
    }
    
    
    public void deleteTrack(int trackId){

        String sql = "CALL delete_track(?)";

        try (Connection conn = dbConfig.getConnection();
             PreparedStatement stmt = conn.prepareStatement(sql)) {

            stmt.setInt(1, trackId);
            stmt.executeUpdate();

            showDashboard.showMessage("Album erfolgreich gelöscht: ID " + trackId+"\n");

        } catch (SQLException e) {
            showDashboard.showError("Fehler beim Löschen des Albums: " + e.getMessage());
        }
        
    }

    public void removeTrackFromAlbum(int albumId, int trackId) {
        String sql = "CALL remove_track_from_album(?, ?)";

        try (Connection conn = dbConfig.getConnection();
             PreparedStatement stmt = conn.prepareStatement(sql)) {

            stmt.setInt(1, albumId);
            stmt.setInt(2, trackId);
            stmt.executeUpdate();

            showDashboard.showMessage("Track erfolgreich aus dem Album entfernt!\n");

        } catch (SQLException e) {
            showDashboard.showError("Fehler beim Entfernen des Tracks aus dem Album: " + e.getMessage());
        }
    }

    public void assignTrackToAlbum(int albumId, int trackId) {
        String sql = "CALL assign_track_to_album(?, ?)";

        try (Connection conn = dbConfig.getConnection();
             PreparedStatement stmt = conn.prepareStatement(sql)) {

            stmt.setInt(1, albumId);
            stmt.setInt(2, trackId);
            stmt.executeUpdate();

            showDashboard.showMessage("Track ID " + trackId + " wurde erfolgreich dem Album zugewiesen!\n");

        } catch (SQLException e) {
            showDashboard.showError("Fehler beim Zuweisen des Tracks: " + e.getMessage());
        }
    }
    
}


