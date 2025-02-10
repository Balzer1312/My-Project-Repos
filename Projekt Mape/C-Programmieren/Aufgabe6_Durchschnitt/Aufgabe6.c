#include<stdio.h>



void main() {

	int randomNumb = 0;
	int sum =0;
	int count = 0;

	printf("Berechnen wir den durchschnitt von deinen eingegebenen Ganzen Zahlen. :)\n");
	printf("\nWenn sie das Einlesen von zahlen beenden moechten, dann geben sie eine negative Zahl ein.\n");


	while (randomNumb >= 0) {

		printf("\nBitte geben sie ein Ganze zahl ein die groesser ist als 0: ");
		scanf_s("%d", &randomNumb);

		if (randomNumb > 0) {
			sum += randomNumb;
			count++;
		}

	}
	randomNumb = sum / count;
	printf("\n\nSie haben %d Zahlen eingegeben!\n", count);
	printf("\nDer Durchschnitt von ihren eingegeben Zahlen liegt bei: %d \n\n", randomNumb);

}
