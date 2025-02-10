#include<stdio.h>



void main() {

	int rounds;
	int term = 1;

	printf("\nWie oft soll ich die zahl verdoppeln ?");
	scanf_s("%d", &rounds);

	for (int i = 0; i <= rounds; i++) {

		printf("\n%d\n", term);
		term *= 2;
	}
	printf("\nDas war das verdoppeln ! ^^\n\n");
}