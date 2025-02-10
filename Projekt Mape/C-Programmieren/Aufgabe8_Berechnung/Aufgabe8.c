#include<stdio.h>



void main() {

	int sum =0;
	int userValue = 0;

	printf("\nDie Summe der Zahlen die groesser sind als 10\n");
	printf("Um das Einlesen zu beenden, Geben sie die zahl 0 ein!\n");
	

	while (userValue != 0) {

		printf("\nBitte geben sie eine Zahl ein:");
		scanf_s("%d", &userValue);

		if (userValue > 10) {

			sum += userValue;
			printf("\nZahl eingeben:");
			scanf_s("%d", &userValue);
		}
	}
	printf("\n\nDeine Summe der eingegeben Zahlen die Groesser als 10 sind ergibt: \"%d\"\n\n", sum);
}
