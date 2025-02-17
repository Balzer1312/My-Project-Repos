import java.util.Arrays;

public class SalesVolumeMain {
    public static void main(String[] args){

        int row=100,cols=1,max,min;
        int[][] matrixData= ValueGenerator.generateMatrix(row,cols);

        min=DetectMinMax.findMin(matrixData);
        max= DetectMinMax.findMax(matrixData);

        System.out.print("Umsatzzahlen: \n");
        for (int [] line: matrixData){
            for(int numb:line){
                System.out.printf("%d. : %15d €",  Arrays.asList(matrixData).indexOf(line)+1,numb);
            }
            System.out.println();
        }
        System.out.println("\nKleinster Umsatzwert: " + min +"€");
        System.out.println("Größter Umsatzwert: " + max+"€");
    }
}
