Implements the game of Cows and Bulls

Procedure:
1. Generate a random n-digit number where each digit is distinct, K
2. User makes a guess, U
3. For each digit D in U, if it is in K in the correct position, increment the number of bulls
4  For each digit D in U, if it is in K in the incorrect position, increment the number of cows
5. Tell the user the number of bulls and cows
6. Exit if number of bulls is n.
7. Else go back to Step #2 
