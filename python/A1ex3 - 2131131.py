"""
David Wang
420-LCU-sec. 3
W2023
Prof. Jason Gullifer
Assignment #1, no 3
"""

var=input("Type a positive integer above 0, or 'q' to quit: ")
while var!='q':
#If we input 'q' here, the loop condition is completed and it exits.
    if var.isdigit()==False or var=="0":
        #To check if our input is valid.
        #This also stops us from inputting negative numbers since hyphens, used to represent negatives, "-" are not digits.
            #This means that negative numbers will complete the var.isdigit == False condition.
        var=input("ERROR: Enter a positive integer above 0, or 'q' to quit: ")
        continue
        #In summary, if the input is invalid, it forces us to try again by inputting again.
        #The continue statement then forcefully restarts the loop from line 2 and the variable value is checked again against the .isdigit and var==0. 
        #This is more efficient than having to add "while" loops.
    n = int(var)
    #If the input is valid, the code converts the string into an integer. This yields no errors since it will be that var.isdigit()==True.
    x = n
    tot = 0

    while x!=1:
        if n%x==0:
            tot+=x
        x-=1 
    #Brute forcing: program goes from maximum value (the input) until 1, we stop at 1 since we cannot divide by 0.
    #Along the way, it will check for proper divisors through the modulo.
    tot = tot - n + 1
    #This is the sum of all proper divisors.
    #The way it check for divisors does not exclude the input itself and does not add 1 since the while loop stops at 1.
    #Therefore, the code has to substract the input and add a 1.

    if tot==n:
        print(n, 'is perfect')

    else:
        if tot>n:
            print(n, 'is abundant')
        if tot<n:
            print(n, 'is deficient')
    var=input("Type a positive integer above 0, or 'q' to quit: ")
    #Loop restarts here by asking for an input until we get a 'q'.
    
print("Au revoir")
