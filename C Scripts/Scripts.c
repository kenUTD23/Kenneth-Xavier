#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <stdbool.h>
#include <string.h>

bool validip() {
    int seg1, seg2, seg3, seg4;
    printf("Enter your IP address here: ");
    int count = scanf("%d.%d.%d.%d", &seg1, &seg2, &seg3, &seg4);

    if (count == 4 && seg1 >= 0 && seg1 <= 255 && 
                   seg2 >= 0 && seg2 <= 255 && 
                   seg3 >= 0 && seg3 <= 255 && 
                   seg4 >= 0 && seg4 <= 255) {
        printf("Your IP Address is valid.\n");
        return true;  
    } else { 
        printf("Your IP Address is not valid.\n");
        return false;  
    }
}

void ascii() {
    int number;  
    char asciiChar;  

    printf("Enter a number (0-127): ");
    scanf("%d", &number);  

    if (number >= 0 && number <= 127) {
        asciiChar = (char)number;  
        printf("The ASCII character for %d is '%c'\n", number, asciiChar);  
    } else {
        printf("Please enter a number between 0 and 127.\n");
    }
}

int generateRandomNumber() {
    int number = (rand() % 6) + 1; 
    printf("Random number between 1 and 6: %d\n", number);
    return number;
}

void concatenateWords() {
    char word1[50];
    char word2[50];
    char result[100]; 

    
    printf("Enter the first word: ");
    scanf("%s", word1); 

    printf("Enter the second word: ");
    scanf("%s", word2); 

   
    strcpy(result, word1); 
    strcat(result, " "); 
    strcat(result, word2); 

    
    printf("Concatenated result: %s\n", result);
}

int main() {
    
    srand(time(0));

    int choice;
    char continueProgram = 'y';

    
    while (continueProgram == 'y' || continueProgram == 'Y') {
        printf("\nChoose an option:\n");
        printf("1. Validate an IP address\n");
        printf("2. Convert a number to ASCII\n");
        printf("3. Generate a random number between 1 and 6\n");
        printf("4. Concatenate two words\n");
        printf("5. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        
        if (choice == 1) {
            validip();
        } else if (choice == 2) {
            ascii();
        } else if (choice == 3) {
            generateRandomNumber();
        } else if (choice == 4) {
            concatenateWords();
        } else if (choice == 5) {
            printf("Exiting...\n");
            break;  
        } else {
            printf("Invalid choice. Please try again.\n");
            continue;
        }

        printf("Do you want to perform another operation? (y/n): ");
        scanf(" %c", &continueProgram);
    }

    printf("Program terminated.\n");
    return 0;
}