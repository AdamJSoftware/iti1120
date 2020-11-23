# Family name: Adam Jasniewicz
# Student number:  300166171
# Course: ITI 1120
# Assignment Number 3.1
# year 2020

########################
# Question 1.1
########################

def is_up_monotone(X, d):
    '''
    (String, string) -> None or Number
    Description: prints the different divisions of x using d with commans and afterwards return if the sequence is up-monotone
    Preconditions: String x is can be converted to a positive integer and the number of digits in x can be divided by 
    '''

    d = int(d)
    for i in range(0, len(X), int(d)):
        if i != len(X) - d:
            print(str(X[i:int(d)+i]), end=", ")
        else:
            print(str(X[i:int(d)+i]))
    if(int(X) > 0 and len(X)%d == 0):
        a = 0
        for i in range(0, len(X), d):
            if(a < int(X[i:d+i])):
                a = int(X[i:d+i])
            else: 
                return False
        return True
    return False




print("""
*******************************************
*                                         *
* __Welcome to up-monotone inquiry__      *
*                                         *
*******************************************
""")

name = input("What is your name?  ")
name = name.strip()
print('*'*72 + len(name)*'*')
print('*', ' '*67, len(name)*' ', '*')
print("*  __" + name +", welcome to my quiz-generator for elementary school students.__  *")
print('*', ' '*67, len(name)*' ', '*')
print('*'*72 + len(name)*'*')

flag=True
while flag:
    question=input(name+", would you like to test if a number admits an up-monotone split of given size? ")
    question=(question.strip()).lower()
    if question=='no':
        flag=False
    elif question != 'yes' and question != 'no':
        print("Please enter yes or no. Try again.")
    else:
        print("Good choice!")
        X = input("Enter a positive integer: ")
        X = X.strip()
        if('-' in X):
            print("The input has to be a positive integer.Try again.")
        elif(X.isdigit() == False):
            print("The input can only contain digits. Try again.")
        elif(X == "0"):
            print("The input has to be a positive integer.Try again.")

        else:
            d = input("Input the split. The split has to divide the length of " + X + " i.e. " + str(len(X)) +" ")
            d = d.strip()
            if(d.isdigit() == False or len(X)%int(d) != 0):
                if(len(X)%int(d) != 0):
                    print(d + " does not divide " + str(len(X)) +". Try again.")
                else:
                    print("The split can only contain digits. Try again.")
            else:
                if(is_up_monotone(X,d)):
                    print("The sequence is up-monotone")
                else:
                    print("The sequence is not up-monotone")
print('*'*22 + len(name)*'*')
print('*', ' '*17, len(name)*' ', '*')
print("*  __Good bye " + name +" !__   *")
print('*', ' '*17, len(name)*' ', '*')
print('*'*22 + len(name)*'*')

