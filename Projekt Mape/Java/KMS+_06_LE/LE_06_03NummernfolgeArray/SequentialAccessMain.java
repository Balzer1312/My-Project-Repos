import java.util.Scanner;

public class SequentialAccessMain {
    public static void main(String[] args) {
        Scanner input= new Scanner(System.in);
        int[]numbSequenceArray,sequenceNumb;
        boolean containsSequence;

        numbSequenceArray=ArrayGenerator.generateRandomArray(50,1,9);
        sequenceNumb=UserInputValidator.getUserSequence(input,4);

        containsSequence=DetectSequence.containsSequence(numbSequenceArray,sequenceNumb);
        OutputFormatter.printResults(numbSequenceArray,sequenceNumb,containsSequence);

        input.close();

    }
}
