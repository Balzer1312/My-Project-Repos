#include<stdio.h>



void main(){


	int term1 = 0;
	int term2 = 1;
	int term_next = term1 + term2;
	int max;

	printf("\nWillkommen zu meiner Fibonacci-Zahlenreihe\n\n");
	printf("Bitte geben sie die Hoechsgrenze der Zahlenreihe an: ");
	scanf_s("%d", &max);
	printf("Ihre Grenze liegt bei %d.",max);

	if (max < 0) {
		printf("\n\nEs sind keine Negativen Zahlen erlaubt !!\n\n");
	}
	else{
	    for (int i = 0; i <= max; i++) {

		    if (i==0 && max > 0){

			     printf("\n%d\n", term_next);
		    }
		    else{
		         printf("\n%d\n", term_next);
		         term1 = term2;
		         term2 = term_next;
		         term_next = term1 + term2;
            }

	    }
    }
	printf("\n\nDas ist die Fibonacci-Zahlenreihe!\n\n");

}
