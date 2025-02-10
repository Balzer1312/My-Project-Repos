#include<stdio.h>



void main() {

	unsigned int rounds;
	unsigned int sum = 0;
	unsigned int factor;
	unsigned int NumToMultip;


	printf("Hallo und Wilkommen zu meinem Staffelrechnungs Programm\n");
	printf("\nBitte geben sie mir die Anzahl der Runden fuer die Staffelrechnung an: ");
	scanf_s("%d", &rounds);
	printf("\n\nUnd jetzt geben sie nun den multiplikanden fuer die Staffelrechnung an: ");
	scanf_s("%d", &NumToMultip);
	printf("\n\n Ich braeuchte jetzt nur noch den Multiplikator: ");
	scanf_s("%d", &factor);
	printf("\n\nInitiiere die Rechenopertationen.......\n\n");

	for (int i = 0; i <= rounds; i++) { 

		if (i == 0) {
		    sum = NumToMultip * factor;
			printf("\n%d * %d = %d", NumToMultip, factor, sum);
		}
		else if (i < rounds) {

			NumToMultip = sum;
			sum = sum * factor;
			printf("\n%d * %d = %d", NumToMultip, factor, sum);
		}

		for (int j = 0; j <= rounds && i == rounds; j++) { 

			if (j < rounds) {
				NumToMultip = sum; 
				sum = sum / factor; 
				printf("\n%d / %d = %d", NumToMultip, factor, sum);
			}
		}
	}
	printf("\n\nDas war deine Staffelrechnungs !!! :)\n");
}
