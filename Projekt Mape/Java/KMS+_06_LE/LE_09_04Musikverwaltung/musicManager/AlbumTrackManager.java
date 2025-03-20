package musicManager;

import DBUtilis.DBHandler;
import musicClass.Album;
import musicClass.Track;
import interfaceGUI.ShowDashboard;
import java.util.*;
import java.util.stream.Collectors;

public class AlbumTrackManager {
    private final ShowDashboard showDashboard;
    private final ValdiDataMusic valdiDataMusic;
    private final DBHandler dbHandler;
    private final Map<Album, List<Track>> albumTracks;

    public AlbumTrackManager() {
        this.valdiDataMusic=new ValdiDataMusic();
        this.showDashboard = new ShowDashboard();
        this.dbHandler = new DBHandler();
        this.albumTracks = dbHandler.loadAlbumsFromDB();
    }

    public void createAlbum(Scanner scanner){

        showDashboard.showMessage("\nGeben Sie die Album-Details ein:");
        try {

            String publisher = valdiDataMusic.getString(scanner, "Album Verlag: ");
            String title = valdiDataMusic.getString(scanner, "Titel des Albums: ");
            String genre = valdiDataMusic.getString(scanner, "Genre des Albums: ");

            dbHandler.addAlbumToDB(publisher, title, genre);
            refreshAlbums();
        }catch (Exception e){
            showDashboard.showError("Fehler beim Speichern der Daten: " + e.getMessage());
        }
    }

    public void crateTrack(Scanner scanner){

        showDashboard.showMessage("\nGeben Sie die Track-Details ein:");
        try{
            String title = valdiDataMusic.getString(scanner, "Titel des Tracks: ");
            String interpreter = valdiDataMusic.getString(scanner, "Name des Interpreten: ");
            String genre = valdiDataMusic.getString(scanner, "Genre des Tracks: ");
            int length = valdiDataMusic.getInt(scanner, "Länge des Tracks in Sekunden: ");


            showDashboard.showMessage("\nWählen Sie ein Album für den Track:");

            for (Map.Entry<Album, List<Track>> entry : albumTracks.entrySet()) {
                Album album = entry.getKey();
                showDashboard.showMessage("ID: " + album.getAlbumID() + ". Titel: " + album.getTitle());
            }

            int albumId = valdiDataMusic.getInt(scanner, "Album-ID eingeben: ");
            dbHandler.addTrackToDB(title, interpreter, genre, length, albumId);
            refreshAlbums();

        }catch (Exception e){
            showDashboard.showError("Fehler beim Speichern der Daten: " + e.getMessage());
        }
    }

    public void assignTrackToAlbum(Scanner scanner){
        try {
            // IDs aus der vorhandenen Map extrahieren
            Set<Integer> albumIds = albumTracks.keySet().stream().map(Album::getAlbumID).collect(Collectors.toSet());
            Set<Integer> trackIds = albumTracks.values().stream()
                    .flatMap(List::stream)
                    .map(Track::getTrackID)
                    .collect(Collectors.toSet());


            showDashboard.showMessage("\nVerfügbare Alben:");
            for (Album album : albumTracks.keySet()) {
                showDashboard.showMessage("ID: " + album.getAlbumID() + " | Titel: " + album.getTitle());
            }

            int albumId = valdiDataMusic.idCheck(scanner, "Geben Sie eine gültige Album-ID ein: ", albumIds);

            showDashboard.showMessage("\nVerfügbare Tracks:");
            for (List<Track> trackList : albumTracks.values()) {
                for (Track track : trackList) {
                    showDashboard.showMessage("ID: " + track.getTrackID() + " | Titel: " + track.getTitle());
                }
            }

            int trackId = valdiDataMusic.idCheck(scanner, "Geben Sie eine gültige Track-ID ein: ", trackIds);
            dbHandler.assignTrackToAlbum(albumId, trackId);
            refreshAlbums();

        } catch (Exception e) {
            showDashboard.showError("Fehler beim Zuweisen des Tracks: " + e.getMessage());
        }
    }

    public void deleteAlbum(Scanner scanner){

        showDashboard.showMessage("\nAlbum löschen:");

        try {

            Set<Integer> albumIds = albumTracks.keySet().stream().map(Album::getAlbumID).collect(Collectors.toSet());
            for (Map.Entry<Album, List<Track>> entry : albumTracks.entrySet()) {
                Album album = entry.getKey();
                showDashboard.showMessage("ID: " + album.getAlbumID() + ". Titel: " + album.getTitle());
            }

            int albumId = valdiDataMusic.idCheck(scanner, "Geben Sie eine gültige Album-ID ein: ", albumIds);
            dbHandler.deleteAlbum(albumId);
            refreshAlbums();

        }catch (Exception e){
            showDashboard.showError("Fehler beim Speichern der Daten: " + e.getMessage());
        }


    }

    public void deleteTrack(Scanner scanner){
        Set<Integer> displayedTracks = new HashSet<>();

        try {
            Set<Integer> trackIds = albumTracks.values().stream().flatMap(List::stream) .map(Track::getTrackID).collect(Collectors.toSet());
            for (Map.Entry<Album, List<Track>> entry : albumTracks.entrySet()) {
                List<Track> tracks = entry.getValue();
                for (Track track : tracks) {
                    if (!displayedTracks.contains(track.getTrackID())) { // Prüfen, ob Track schon angezeigt wurde
                        showDashboard.showMessage("  Track-ID: " + track.getTrackID() + " | Titel: " + track.getTitle());
                        displayedTracks.add(track.getTrackID());  // Track-ID speichern für anzeige
                    }
                }
            }

            int trackId = valdiDataMusic.idCheck(scanner, "Geben Sie eine gültige Track-ID ein: ", trackIds);
            dbHandler.deleteTrack(trackId);
            refreshAlbums();

        }catch (Exception e){
            showDashboard.showError("Fehler beim Speichern der Daten: " + e.getMessage());
        }

    }

    public void deleteTrackFromAlbum(Scanner scanner){

        try {

            for (Map.Entry<Album, List<Track>> entry : albumTracks.entrySet()) {
                Album album = entry.getKey();
                showDashboard.showMessage("Album ID: " + album.getAlbumID() + " - Titel: " + album.getTitle());
                for (Track track : entry.getValue()) {
                    showDashboard.showMessage("   ➤ Track ID: " + track.getTrackID() + " - " + track.getTitle());
                }
            }
            int albumId = valdiDataMusic.idCheck(scanner, "Geben Sie eine gültige Album-ID ein:",
                    albumTracks.keySet().stream().map(Album::getAlbumID).collect(Collectors.toSet()));

            List<Track> tracks = albumTracks.entrySet().stream()
                    .filter(e -> e.getKey().getAlbumID() == albumId)
                    .flatMap(e -> e.getValue().stream())
                    .toList();

            if (tracks.isEmpty()) {
                showDashboard.showError("Dieses Album enthält keine Tracks.");
                return;
            }

            int trackId = valdiDataMusic.idCheck(scanner, "Geben Sie eine gültige Track-ID aus dem Album ein:",
                    tracks.stream().map(Track::getTrackID).collect(Collectors.toSet()));

            dbHandler.removeTrackFromAlbum(albumId, trackId);
            refreshAlbums();

        } catch (Exception e) {
            showDashboard.showError("Fehler beim Entfernen des Tracks aus dem Album: " + e.getMessage());
        }
    }

    public void showAlbumOnDisplay(){
        try {
            int totalLength;
            if (albumTracks.isEmpty()) {
                showDashboard.showMessage("Keine Alben verfügbar.");
                return;
            }

            showDashboard.showMessage("\nAlbum Übersicht");

            for (Map.Entry<Album, List<Track>> entry : albumTracks.entrySet()) {
                Album album = entry.getKey();
                List<Track> tracks = entry.getValue();
                totalLength = tracks.stream().mapToInt(Track::getLength).sum();

                showDashboard.showMessage(album.toString());
                showDashboard.showMessage("Gesamtlänge :" + totalLength / 60 + "min " + totalLength % 60 + "sec");

                if (tracks.isEmpty()) {
                    showDashboard.showMessage("Keine Tracks verfügbar.");
                } else {
                    for (Track track : tracks) {
                        showDashboard.showMessage(track.toString()+"\n");
                    }
                }
                showDashboard.showMessage("--------------------------------------");
            }
        }catch (Exception e){
            showDashboard.showError("Fehler beim Anzeigen des Albums: " + e.getMessage());
        }

    }

    public void showChoiceAlbum(Scanner scanner){
        try {
            int totalLength;
            showDashboard.showMessage("\nVerfügbare Alben:");
            showDashboard.showMessage("\nAlle Alben: "+Album.getAlbumcount());
            showDashboard.showMessage("\nVerfügbare Alben:"+ Track.getTrackCounter()+"\n");





            for (Album album : albumTracks.keySet()) {
                showDashboard.showMessage("ID: " + album.getAlbumID() + " | Titel: " + album.getTitle());
            }

            Set<Integer> albumIds = albumTracks.keySet().stream().map(Album::getAlbumID).collect(Collectors.toSet());

            int albumId = valdiDataMusic.idCheck(scanner, "Geben Sie die gewünschte Album-ID ein: ", albumIds);

            Album selectedAlbum = albumTracks.keySet().stream()
                    .filter(a -> a.getAlbumID() == albumId)
                    .findFirst()
                    .orElse(null);

            if (selectedAlbum != null) {

                showDashboard.showMessage("\nAlbum Details:");
                showDashboard.showMessage(selectedAlbum.toString());

                List<Track> tracks = albumTracks.get(selectedAlbum);

                totalLength = tracks.stream().mapToInt(Track::getLength).sum();
                showDashboard.showMessage("Gesamtlänge : "+ totalLength/60+"min "+ totalLength %60+"sec");

                if (!tracks.isEmpty()) {
                    showDashboard.showMessage("\nEnthaltene Tracks:");
                    for (Track track : tracks) {
                        showDashboard.showMessage(track.toString());
                    }
                } else {
                    showDashboard.showMessage("\nKeine Tracks in diesem Album gefunden.");
                }
            }

        } catch (Exception e) {
            showDashboard.showError("Fehler beim Anzeigen des Albums: " + e.getMessage());
        }

    }

    private void refreshAlbums() {
        albumTracks.clear();
        albumTracks.putAll(dbHandler.loadAlbumsFromDB());
        showDashboard.showMessage("Liste wurde aktualisiert!");
    }
}



