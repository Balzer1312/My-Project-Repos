import java.util.Random;


public class ValueGenerator {
    public static int[][] generateMatrix(int rows,int cols){
        Random randomValue= new Random();
        int[][] matrixTable =new int[rows][cols];

        for (int i=0; i <rows;i++){
            for (int j=0;j<cols;j++){
                matrixTable[i][j]=randomValue.nextInt(Integer.MAX_VALUE)+1;
            }
        }

        return matrixTable;
    }
}
