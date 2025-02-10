import java.util.Scanner;

public class CalculateVolume {
    public static void main(String[] args){
        Scanner scanner= new Scanner(System.in);

        boolean runMenu = true;

        while (runMenu){

            System.out.print("\nBitte, Wählen Sie eine Grundfläche aus: \n1 für Rechteck \n2 für Gleichseitiges Dreieck\n3 für Kreis\n4 für Beenden\nIhre Auswahl: ");
            int choice = scanner.nextInt();

            double area = 0;
            double volume = 0;
            double length = 0;
            double width = 0;
            double height = 0;
            double radius = 0;


            if (choice < 1 || choice > 4) {
                System.out.println("Ungültige Auswahl. Bitte starten Sie das Programm neu.");
                return;

            } else if (choice == 4) {
                    runMenu= false;
                    System.out.print("\nDann bis zum nächsten mal.\n");
                    break;
            }

            switch (choice) {

                case 1:
                    System.out.print("Bitte geben Sie die Seitenlänge des Rechtecks ein: ");
                    length = scanner.nextDouble();

                    System.out.print("Bitte geben Sie die Seitenbreite des Rechtecks ein: ");
                    width = scanner.nextDouble();
                    area = length * width;

                    System.out.print("Bitte geben Sie die Höhe des Rechtecks ein: ");
                    height = scanner.nextDouble();
                    volume = area * height;
                    break;

                case 2:
                    System.out.print("Geben Sie die Seitenlänge des Dreiecks ein: ");
                    length = scanner.nextDouble();
                    area = (Math.sqrt(3) / 4) * (length * length);

                    System.out.print("Geben Sie die Höhe des Prismas ein: ");
                    height = scanner.nextDouble();
                    volume = area * height;
                    break;

                case 3:
                    System.out.print("Geben Sie den Radius des Kreises ein: ");
                    radius = scanner.nextDouble();
                    area = Math.PI * (radius * radius);

                    System.out.print("Geben Sie die Höhe des Zylinders ein: ");
                    height = scanner.nextDouble();
                    volume = area * height;
                    break;
            }

            System.out.println("Die berechnete Grundfläche beträgt: " + area + " m².");
            System.out.println("Das berechnete Volumen beträgt: " + volume + " m³.");
        }
    }
}

