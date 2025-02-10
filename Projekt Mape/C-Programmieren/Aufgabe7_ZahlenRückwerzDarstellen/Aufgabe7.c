#include<stdio.h>



void main() {

    int numb; 
    int reverse = 0;

    printf("Zeit ihre eingebene Zahl Umgekert darstellen zu lassen! :)\n\n");
    printf("Geben Sie eine ganze Zahl ein: ");
    scanf_s("%d", &numb);

    while (numb != 0) {
        reverse = reverse * 10 + (numb % 10);
        numb = numb / 10;
    }
    printf("Die Zahl in umgekehrter Reihenfolge ist: %d\n", reverse);

}