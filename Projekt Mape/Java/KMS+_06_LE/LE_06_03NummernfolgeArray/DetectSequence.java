


public class DetectSequence {
    public static boolean containsSequence(int[] data, int[] sequence) {
        boolean match;

        for (int i = 0; i <= data.length - sequence.length; i++) {
            match=true;
            for (int j = 0; j < sequence.length; j++) {
                if (data[i + j] != sequence[j]) {
                    match = false;
                    break;
                }
            }
            if (match) {
                return true;
            }
        }
        return false;
    }
}
