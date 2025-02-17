

public class DetectMinMax {
    public static int findMin(int[][] matrixData ){
        int min = matrixData[0][0];

        for (int[] row:matrixData){                //
            for (int num:row){
                if(min>num){
                    min=num;
                }
            }
        }
        return min;
    }

    public static int findMax(int [][]matrixData){
        int max = matrixData[0][0];
        for (int[] row: matrixData){
            for (int num :row){
                if(num>max){
                    max=num;
                }
            }
        }
        return max;
    }
}
