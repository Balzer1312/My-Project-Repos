import java.util.Random;


public class SeatManager {
    public static boolean[][] seatPlanGenerator(int seatRow,int seatColumns){
        boolean[][]seats= new boolean[seatRow][seatColumns];
        Random rand=new Random();

        for (int i=0;i<seatRow;i++) {
            for (int j = 0; j < seatColumns; j++) {
                seats[i][j] = rand.nextBoolean();
            }
        }
    return seats;
    }

    public static int freeSeatsByRow(boolean[][] seats, int row){
        int freeSeats=0;

        for(boolean seat : seats[row])
            if(!seat){
                freeSeats++;
            }
        return freeSeats;
    }

    public static double hallFillingLevel(boolean[][] seats){
        int occupiedSeats =0;
        int totalSeats=  seats.length * seats[0].length;

        for (boolean[] row : seats) {
            for (boolean seat : row) {
                if (seat) occupiedSeats++;
            }
        }

        return (occupiedSeats / (double) totalSeats) * 100 ;
    }

}
