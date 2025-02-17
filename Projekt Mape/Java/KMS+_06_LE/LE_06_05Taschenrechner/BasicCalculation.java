
public class BasicCalculation {

    // Methodenüberladung ist in Java möglich, Die Metoden können den gleichen Namen besitzen solage die Parameter unterschiedlich sind.

    // Methodenüberladung für Addieren
    public static int add(int a, int b) {
        return a + b;
    }

    public static double add(double a, double b) {
        return a + b;
    }

    // Methodenüberladung für Subtrahieren
    public static int subtract(int a, int b) {
        return a - b;
    }

    public static double subtract(double a, double b) {
        return a - b;
    }

    // Methodenüberladung für Multiplizieren
    public static int multiply(int a, int b) {
        return a * b;
    }

    public static double multiply(double a, double b) {
        return a * b;
    }

    // Methodenüberladung für Dividieren
    public static int divide(int a, int b) {
        if (b == 0) {
            System.out.println("Division durch Null ist nicht erlaubt.");
            return 0;
        }
        return a / b;
    }

    public static double divide(double a, double b) {
        if (b == 0) {
            System.out.println("Division durch Null ist nicht erlaubt.");
            return 0.0;
        }
        return a / b;
    }

    // Methodenüberladung für Berechnung und rückgabe des Ergebnisses
    public static int calculate(int a, int b, char operator) {
        return switch (operator) {
            case '+' -> add(a, b);
            case '-' -> subtract(a, b);
            case '*' -> multiply(a, b);
            case '/' -> divide(a, b);
            default -> {
                System.out.println("Fehler: Ungültige Operation!");
                yield 0;
            }
        };
    }

    public static double calculate(double a, double b, char operator) {
        return switch (operator) {
            case '+' -> add(a, b);
            case '-' -> subtract(a, b);
            case '*' -> multiply(a, b);
            case '/' -> divide(a, b);
            default -> {
                System.out.println("Fehler: Ungültige Operation!");
                yield 0.0;
            }
        };
    }
}

