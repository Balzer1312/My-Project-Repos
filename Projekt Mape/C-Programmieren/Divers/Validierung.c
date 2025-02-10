#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include<string.h>


int isValied(char UserInput[]) {

    char LocalPart[65] = { '\0' };
    int LenLocal = 0;
    char DomainPart[254] = { '\0' };
    int LenDomain = 0;
    int atCount = 0;
    int DotCount = 0;
    int lenMail = strlen(UserInput);

    // Teilung des Strings in den Localen und Domain teil  

    for (int i = 0; i < lenMail; i++) {
        if (UserInput[i] == '@' && atCount == 0) {
            atCount++;
            LenLocal = i;
        }
        else if (atCount == 1) {
            DomainPart[LenDomain] = UserInput[i];
            LenDomain++;
            if (UserInput[i] == '.') {
                DotCount++;
            }
        }
        else {
            LocalPart[i] = UserInput[i];
        }
    }

    if (atCount != 1) {
        return 0;
    }


    // Validierungs Prüfung für den Localen teil

    for (int j = 0; j < LenLocal; j++) {


        if (LocalPart[j] == ' ' || LocalPart[0] == '$' || LocalPart[0] == '/' || LocalPart[0] == '#' || LocalPart[0] == '!' || LocalPart[0] == '@' || LocalPart[LenLocal] == ' '
            || LocalPart[0] == '.' || LocalPart[0] == '-' || LocalPart[LenLocal] == '.' || LocalPart[LenLocal] == '-'
            || (LocalPart[j] == '.' && LocalPart[j + 1] == '.') || (LocalPart[j] == '-' && LocalPart[j + 1] == '-')) // || (LocalPart[..]== '%'.......) 
        {
            return 0;
        }

    }
    // Validierungs Prüfung für den Domain teil

    for (int k = 0; k < LenDomain; k++) {

        if (DomainPart[k] == ' ' || DomainPart[k] == '"' || DomainPart[k] == '&' || DomainPart[k] == '_' || DomainPart[k] == '!' || DotCount < 1
            || DomainPart[k] == '§' || DomainPart[k] == '!' || DomainPart[k] == '#' || DomainPart[k] == '&' || DomainPart[k] == ':'
            || DomainPart[0] == '.' || DomainPart[0] == '-' || DomainPart[LenDomain] == '.' || DomainPart[LenDomain] == '-'
            || (DomainPart[k] == '.' && DomainPart[k + 1] == '.') || (DomainPart[k] == '-' && DomainPart[k + 1] == '-')) // || (DomainPart[..]=='$'........)i
        {
            return 0;
        }


    }


    return 1;

}

void main(void) {

    char mail[256];


    printf("\nUm die Validierung zu beenden geben sie \"n\"ein!");

    while (mail[0] != 'n') {

        printf("\nGeben sie eine E-Mail Adresse ein: ");
        fgets(mail, 256, stdin);
        mail[strcspn(mail, "\n")] = '\0';



        if(mail[0]!= 'n' && strlen(mail)>1){
            isValied(mail);

            if (isValied(mail)) {
                 printf("\nE-mail ist Valide!\n");
            }
            else
                 printf("\nE-mail ist nicht Valide!\n");
        }
    }

    printf("\nDas war die Validierung !\n");
}