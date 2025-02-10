#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h> 
#include<time.h>

// Die Funktion Game() ist die Logik für das spiel. Die Parameter werden in der main() in die Game() Funktion übertagen  
void Game(int DiffValue,int choice){

	int randomValue;    //Die randomValue Variable wird von rand() initialisiert 
	int guessValue;     //Diese Variable ist für den Input für den schätzwert des users 
	int trys = 0;       //Die Zähler Variable für die Anzahl der Versuche 
	int score;          //Jeder Schwierichkeitsgrads hat ihre eigenen Punkte die je nach versuch abgezogen werden bis 0

	while (DiffValue){
	    
		// Die Bedingungen werden für das trennen der Ausgaben und das initialisieren der Punkte für jeden Schwierigkeitsgrad genutzt
		if (choice==1){
		    printf("\nRaten sie eine Zahl zwischen 1-10:");
			score = 100;
        }
		else if (choice== 2) {
			printf("\nRaten sie eine Zahl zwischen 1-100:");
			score = 1000;
		}
		else if (choice==3) {
			printf("\nRaten sie eine Zahl zwischen 1-1000:");
			score = 10000;
		}
		else{
			printf("\nRaten sie eine Zahl zwischen 1-10000:");
			score = 100000;
		}
		scanf_s("%d", &guessValue); // Der Userinput für den Schätzwert 
		srand(time(NULL));          // srand(...) initialisiert den Seed basierend auf der zeit des Betriebsystems im hintergrund
		randomValue = rand() % DiffValue + 1;  // rand() holt sich den seed und generiert eine zufällige zahl, Der Modulo operater teil die Zahl durch 10 um den rest +1 als zufallszahl zu initialisieren

		
		if (guessValue >= 1 && guessValue <= DiffValue) { // Diese bedingung dinnt zu überprüfung ob die eingabe korrekt ist 

			trys++;

			if (randomValue != guessValue) {

				if (guessValue < randomValue) {     //Prüft ob der Schätzwert des Useres kleiner ist als die Zufalls Zahl 
					printf("\nLeider ist deine Zahl kleiner !\n");
					score -= 5;
					if (score < 0) {     // Wenn der score ins (-) geht. Wird er wieder 0 gesetzt um negative zahlen zu vermeiden 
						score = 0;
					}
				}
				else {                              //Prüft ob der Schätzwert des Useres Größer ist als die Zufalls Zahl
					printf("\nLeider ist deine Zahl Groeßer !\n");
					score -= 5;
					if (score < 0) {
						score = 0;
					}
				}
			}
			else {         
				printf("\nGlueckwunsch!! Sie haben die richtige Zahl eratten !\n");
				printf("\nSie haben %d versuche gebraucht!\n\n", trys);  // Ausgabe der versuche die mann gebraucht hat 
				if (score == 0) {
					printf("\nSie haben leider zu viele Versuche gebraucht! :(\nDaher haben sie %d Punkte.", score);  // Ausgabe der Punkte wenn die punkte auf 0 fallen 
				}
				else {
					printf("Sie Haben %u Punkte erreicht\n", score);   //Ausgabe der Punkte
				}
				return 0;    //Das Spiel wird nach eratten der zahl beendet
			}
		}
		else if(choice==1) {
			printf("\nBitte geben sie eine Gueltige zahl von 1-10 ein!\n\n");
		}
		else if (choice == 2) {
			printf("\nBitte geben sie eine Gueltige zahl von 1-100 ein!\n\n");
		}
		else if (choice == 3) {
			printf("\nBitte geben sie eine Gueltige zahl von 1-1000 ein!\n\n");
		}
		else{
			printf("\nBitte geben sie eine Gueltige zahl von 1-10000 ein!\n\n");
		}
	}

}


void main(void) {
	
	unsigned int StartGame = 1;  //Variable für die Bedingung zum starten der while schleife
	unsigned int diffchoice;     //Variable für die wahl des Schwierichkeitsgrades 


	printf("\nWillkommen zum Zahlen rate spiel\n");
	printf("\nWählen sie einen schwierigkeit grad aus:\n1.fuer leicht\n2.fuer Medium\n3.fuer Schwer\n4.fuer sehr Schwer\n");

	// Der start der main Funktion mit dem start wert 1 
	while (StartGame==1){

		printf("Waehlen sie einen Schwierichkeitgrad aus:");
		scanf_s("%d", &diffchoice); // Der User kann zwischen 4 Schwierigkeitsgrade entscheiden
		if (diffchoice > 4) {       // Falls der User was anderes eingibt als 1,2,3,4 wird die main() Funktion erneut aufgerufen um die eingabe zu wiederholen 
			printf("\n\nBitte waehlen sie einen Schwierichkeitgrad von 1-4 !!!\n\n\n\n");
			main();
		}
		
		// Das switch case dinnt zur trennung der schwierichkeitsgrade damit die richtigen Parameter an in die Funktion übergeben werden  
		switch (diffchoice) {

		case 1:   
			printf("\nSie haben sich fuer den Schwierigkeitsgrad Leich entschieden!\n");
			Game(10, 1);   // Das aufrufen der Game() Funktion mit den zugehörigen parameter für das Spiel    
			break;         // Switch Case wird beendet 
		case 2:
			printf("\nSie haben sich fuer den Schwierigkeitsgrad Medium entschieden!\n");
			Game(100, 2);
			break;

		case 3:
			printf("\nSie haben sich fuer den Schwierigkeitsgrad Schwer entschieden!\n");
			Game(1000, 3);
			break;

		case 4:
			printf("\nSie haben sich fuer den Schwierigkeitsgrad sehr Schwer entschieden!\n");
			Game(10000, 4);
			break;

		}
		// Die abfrage ob man das spiel wiederholen will oder nicht
		printf("\nWollen Sie nochmal spielen ?\n\n1.Fuer Ja\n0. und groesser als 1.fuer nein\nIhre eingabe:");
		scanf_s("%d", &StartGame); 
		if (StartGame > 1) { //Dinnt für den fall, falls der User eine falsche eingabe macht das die Variable Startgame auf 0 setzt um das spiel zu beenden   
			StartGame = 0;
		}
	}
	printf("\nDas war das Zahlenrate spiel.\n\n");

}