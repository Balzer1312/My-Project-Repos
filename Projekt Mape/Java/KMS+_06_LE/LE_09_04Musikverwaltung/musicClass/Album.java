package musicClass;

public class Album {
    private int albumID;
    private String publisher;
    private String title;
    private String genre;
    public static int albumCount;

    public Album(int albumID, String publisher,String title, String genre) {
        this.albumID = albumID;
        this.publisher=publisher;
        this.title = title;
        this.genre = genre;
        albumCount++;
    }

    public static int getAlbumcount() {
        return albumCount;
    }

    public int getAlbumID() {
        return albumID;
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    @Override
    public String toString() {
        return "Album: " +"\n" +
                "Titel: " + title + "\n" +
                "Künstler: " + genre + "\n";
    }
}
