


public class SeatReservationMain {
    public static void main(String[] args) {
        boolean[][] seats;
        int seatRow = 10, seatColumns = 15, freeSeats=0;
        double fillingLevel;


        seats= SeatManager.seatPlanGenerator(seatRow,seatColumns);
        CinemaHallillustration.showSeatsPlan(seats);

        System.out.println();
        for (int row = 0; row < seatRow; row++) {
            freeSeats = SeatManager.freeSeatsByRow(seats, row);
            System.out.println(freeSeats + " freie Plätze in Reihe " + (row + 1));
        }

        fillingLevel= SeatManager.hallFillingLevel(seats);
        System.out.printf("\nDer Kinosaal ist zu %.2f%% ausgelastet.%n", fillingLevel);
    }
}
