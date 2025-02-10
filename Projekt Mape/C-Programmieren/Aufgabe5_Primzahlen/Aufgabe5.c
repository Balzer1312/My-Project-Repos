#include<stdio.h>



void main() {

	int term = 2;
	int rounds;

	printf("\nDas sind deine Primzahlen:");
	printf("\n\nGeben sie in der naechsten Zeile an wie viel Primzahlen sie von \"2\" weg anzeigen moechten:");
	scanf_s("%d", &rounds);
	printf("\nPrimzahlen:\n");
	rounds--;

	for (int i = 0; i <= rounds; i++) {

		if (term == 2 || term == 3 || term == 5 || term == 7) {
             printf("\n%d\n", term);
			 term ++;
		}
		else if (term % 2 == 0 || term % 3 == 0 || term % 5 == 0 || term % 7 == 0) {
             i--;
			 term++;
		}
		else{
			printf("\n%d\n", term);
			term++;
		}
	}
	printf("\nDas sind ihre primzahlen !\n\n");
}
