# differencemethod.py
A short program finding the difference sequences of a given sequence and a closed form if any difference is constant. Made by Noah Prentice on 5 October 2022.

To use the program, run it and input the first several terms in any sequence, pressing the enter/return after every term. (If you know your sequence is polynomial (its closed form is a polynomial), input a number of terms equal to the degree of the polynomial, plus 2. Otherwise, it is not clear that the sequence is ever constant.) Then, when you've input all the terms you want, input "DONE" and press the enter/return key. 

The program will output the original sequence, as well as all of the sequences of differences between terms until the first sequence with all zeroes, if one exists. If one exists, then, from the number of terms, given, the sequence appears to be a polynomial sequence, and so the program will find the coefficients of the polynomial sequence using linear algebra. 

It will print the two matrices used in the calculation, and then will output the coefficients of the closed form polynomial, in the order of descending powers of n. So, if the output for the coefficients is [3 5 0 1 2], the closed form will be 3n^4 + 5n^3 + n + 2, where the first term of the sequence corresponds to n = 1.
