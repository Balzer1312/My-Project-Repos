package musicClass;

public class Track {
    private final int trackID;
    private String title;
    private String interpreter;
    private String genre;
    private int length;
    public static int trackCounter;



    public Track(int trackID, String title, String interpreter, String genre , int length) {
        this.trackID = trackID;
        this.title = title;
        this.interpreter = interpreter;
        this.genre=genre;
        this.length = length;
        trackCounter++;
    }

    public static int getTrackCounter() {
        return trackCounter;
    }

    public int getTrackID() {
        return trackID;
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public int getLength() {
        return length;
    }

    public void setLength(int length) {
        this.length = length;
    }

    @Override
    public String toString() {
        return "Track:" +
                "\nTrack ID." + trackID +
                "\nTitel: " + title + '\'' +
                "\nInterpreter: " + interpreter + "  " +
                "\nGenre: " + genre + "  " +
                "\nLänge : " + length + "sec";
    }
}
