#include<stdio.h>



void main() {

	int numb;
	int min = 0;
	int max = 0;



	printf("\nWillkomen zum Zahlen Einlesen!");
	printf("\nWenn Sie das Einlesen beenden möchten, dann geben sie \"0\" ein\n");
	printf("\nBitte geben sie eine beliebige positive Zahl ein: ");
	scanf_s("%d", &numb);
	min = numb;
	printf("\n\n Los geht`s !!\n\n");


	do {
		if (numb < 0) {
			break;
		}
		else if (numb > min) {
			max = numb;
		}
		else if (numb < min) {
			min = numb;
		}

		printf("\nBitte geben sie eine beliebige positive Zahl ein: ");
		scanf_s("%d", &numb);

	} while (numb != 0);

	if (numb < 0) {
		printf("\nEs sind keine negativen Zahlen erlaubt !!\n\n\n");
	}
	else {
		printf("\n\nDein \"Maximum\" liegt bei: %d und dein \"Minimum\" bei: %d !!\n\n", max, min);
		printf("\n\nDann bis zum nächsten mal !\n\n");
	}
}
