import numpy as np
def diff():
    S = [] #Creating an empty list for the original sequence.
    delta = [] #Creating an empty list for the list of difference sequences.
#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Inputting the terms of the sequence ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
    inp = input("Enter the first term of the sequence: ")
    while inp != "DONE":
        try:
            int(inp) #Making sure the user is inputting a number.
        except:
            print("Input must be an integer.")
            return
        else:
            if "." in inp: #Making sure the user is inputting an integer.
                print("Input must be an integer.")
                return
            else:
                S.append(int(inp))
                inp = input("Enter the next term of the sequence, or DONE if done: ")
#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Finding the delta sequences ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
    else:
        delta.append(S) #Adding S to the delta list, i.e. making S the delta-0 sequence.
        for deltanum in list(range(len(S))): #deltanum is the order of the difference (like 3 in the delta-3 sequence).
            #                                 we loop through each delta sequence until we get all zeroes or we onkly have one term left.
            templist = [] #Creating a "dummy" temporary list to use to create the delta sequences.
            sum = 0 #Using a sum variable to sum the absolute value of the terms of the delta list.
            #        If the sum is 0, the delta sequence before was constant.
            for element in list(range(len(delta[deltanum]) - 1)): #Looping through each pair of sequential terms in the previous delta sequence.
                templist.append(delta[deltanum][element + 1] - delta[deltanum][element]) #We add the difference of each pair to the templist, in order.
            delta.append(templist) #Then we add this list as the next delta sequence, to the "master" delta list of all delta sequences.
            if deltanum == 0: #Printing a unique message for the original sequence (delta-0 sequence sounds odd out of context)
                print("The original sequence:", delta[deltanum])
            else:
                print("The delta-" + str(deltanum) + " sequence:", delta[deltanum]) #Printing the difference sequences.
#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Checking for delta-constancy ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
            for entry in list(range(len(delta[deltanum]))): #Finding the sum of of the absolute value of the current delta sequence.
                sum += abs(delta[deltanum][entry])
            if sum == 0: #The sum will be 0 if and only if all terms are 0, if and only if the previous sequence was constant.
                print("From the number of terms given, your sequence appears to be delta-" + str(deltanum - 1) + " constant.") #Print the order of constancy.
                deg = deltanum - 1
                if deg > len(S): #I don't think at this point it's actually possible for the program to run into a constant sequence with not enough terms
                    #             to find a closed form, but this check is in here just in case. It doesn't add much to the computing power or computation time.
                    print("There are not enough terms in the sequence to find a closed form.")
                    return
                else: #If there are enough terms to find a closed form, let's find the closed form!
#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Finding a closed form ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
                    Alist = [] #We'll find a closed form using linear algebra.
                    Blist = [] #We need matrices, so we'll create lists for the matrices A and B for python stuff and then turn them into matrices later.
                    for i in list(range(deg + 1)):
                        Blist.append(S[i]) #Creating B.
                        Arow = [] #Creating a "dummy" list for each row of A.
                        for j in list(range(deg + 1)):
                            a = (i + 1)**(deg - j) #Creating a "dummy" variable for each entry of A.
                            Arow.append(a) #Adding that to the row of A.
                        Alist.append(Arow) #Adding that row to A. This completes one row, and will loop through to the next one.
                    A = np.array(Alist) #Turn the lists into matrices.
                    B = np.array(Blist)
                    print("A is:")
                    print(A)
                    print("B is")
                    print(B)
                    coefficients = np.linalg.solve(A, B) #Generate the coefficients of the closed form (like a,b,c,d in an^3 + bn^2 + cn + d).
                    print("And the coefficients are, in order of descending powers of n,", coefficients) #Print the coefficients in list form. 
                return
diff()