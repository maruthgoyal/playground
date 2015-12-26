Implements 3 different ways to check the number of palindromes in a given string S.

Procedure #1: (Absolute Brute force)
1. Check every possible substring for being a palindrome
2. Increment counter if a palindrome.

3. return counter

Procedure #2: (Optimized Brute force)
1. For every substring, if the first character is equal to the last character, then check it for being a palindrome.
2. Increment counter if a palindrome

3. return counter

Procedure #3: (Optimization using Hashing) [original idea]
1. Create a dictionary, D.
2. For every character in S, if it is not in D, add it to D and map it to a list which contains its index
          If it is in D, Check the substring from current index to all the indices in the list for being a palindrome
          If it is a palindrome, increment the counter.
          Add, the current index to the list
3. return counter
