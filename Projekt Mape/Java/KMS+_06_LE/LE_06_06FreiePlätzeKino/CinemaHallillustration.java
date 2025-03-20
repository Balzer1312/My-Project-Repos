
public class CinemaHallillustration {
    public static void showSeatsPlan(boolean[][] seats){


        System.out.println("\nKinosaal Sitzplan: ");
        System.out.println("▣ = Plätze besetzt ");
        System.out.println("▢ = Plätze frei\n");

        for (boolean[] seat : seats) {
            for (boolean isOccupied : seat) {
                System.out.print(isOccupied ? "▣" : "▢");
            }
            System.out.println();
        }
    }
}
