# Family name: Adam Jasniewicz
# Student number:  300166171
# Course: ITI 1120
# Assignment Number 2
# year 2020

import math
import random


########################
# Question 1.1
########################


def elementary_school_quiz(flag, n):
    '''
    (Number, Number) -> Number
    Description: This function tests the user with elementary level math. If flag is set to 0, then the function will test the user with 1 or 2
    substraction questions (depending on the value of n). If flag is set to 1, then the function will test the user with 1 or 2
    exponentiation questions (depending on the value of n)
    Preconditions: flag is 0 or 1, n is 1 or 2.
    '''
    total = 0
    if(flag == 0):
        if(n == 1):
            num1 = random.randint(1, 9)
            num2 = random.randint(1, 9)
            print("Question 1:")
            q1 = input("What is the result of " + str(num1)+"-"+str(num2)+"? ")
            if(int(q1) == num1-num2):
                total = total + 1
        else:
            num1 = random.randint(1, 9)
            num2 = random.randint(1, 9)
            print("Question 1:")
            q1 = input("What is the result of " + str(num1)+"-"+str(num2)+"? ")
            if(int(q1) == (num1-num2)):
                total = total + 1

            num3 = random.randint(1, 9)
            num4 = random.randint(1, 9)
            print("Question 2:")
            q2 = input("What is the result of " + str(num3)+"-"+str(num4)+"? ")
            if(int(q2) == (num3-num4)):
                total = total + 1
    else:
        if(n == 1):
            num1 = random.randint(1, 9)
            num2 = random.randint(1, 9)
            print("Question 1:")
            q1 = input("What is the result of " + str(num1)+"^"+str(num2)+"? ")
            if(int(q1) == num1**num2):
                total = total + 1

        else:
            num1 = random.randint(1, 9)
            num2 = random.randint(1, 9)
            print("Question 1:")
            q1 = input("What is the result of " + str(num1)+"^"+str(num2)+"? ")
            if(int(q1) == num1**num2):
                total = total + 1
            num3 = random.randint(1, 9)
            num4 = random.randint(1, 9)
            print("Question 2:")
            q2 = input("What is the result of " + str(num3)+"^"+str(num4)+"? ")
            if(int(q2) == num3**num4):
                total = total + 1

    return total
    # Your code for elementary_school_quiz function goes here (instead of keyword pass)
    # Your code should include  dosctrings and the body of the function
    #
    #


def high_school_quiz(a, b, c):
    '''
    (Number, Number, Number) -> None
    Description: This function prints the quadratic equation and then solves it for the user
    Preconditions: a, b, c are real numbers
    '''
    num_of_real_roots = b**2-4*a*c
    if(a == 0 and b != 0 and c != 0):
        print("The linear equation " + str(b) + "*x + " + str(c) + " = 0")
        print("has the following root/solution: " + str((c*-1)/b))
    elif(a == 0 and b == 0 and c == 0):
        print("The quadratic equation 0*x + 0 = 0\nis satisfied for all numbers x")
    elif (a == 0 and b == 0 and c != 0):
        print("The quadratic equation 0*x + " + str(c) +
              " = 0\nis satisfied for no number x")
    else:
        if(num_of_real_roots > 0):
            sol1 = (b*-1 + math.sqrt(b**2 - 4*a*c))/(2*a)
            sol2 = (b*-1 - math.sqrt(b**2 - 4*a*c))/(2*a)
            print("The quadratic equation " + str(a) +
                  "*x^2 + " + str(b) + "*x + " + str(c) + " = 0")
            print("has the following real roots: ")
            print(sol1, "and", sol2)
        elif(num_of_real_roots == 0):
            sol1 = (-b + math.sqrt(b**2 - 4*a*c))/(2*a)
            print("The quadratic equation " + str(a) +
                  "*x^2 + " + str(b) + "*x + " + str(c) + " = 0")
            print("has only one solution, a real root: ")
            print(sol1)
        else:
            sol1 = -b/(2*a)
            sol2 = math.sqrt(abs(b**2-4*a*c))/(2*a)
            print("The quadratic equation " + str(a) +
                  "*x^2 + " + str(b) + "*x + " + str(c) + " = 0")
            print("has the following two complex roots: ")
            print(sol1, "+ i", sol2, "and", sol1, "- i", sol2)


########################
# Question 1.2
########################


print("""
*******************************************
*                                         *
* __Welcome to my math quiz-generator__   *
*                                         *
*******************************************
    """)

name = input("What is your name?  ")

status = input(
    "Hi "+name+". Are you in?  Enter \n1 for elementary school\n2 for high school or\n3 or other character(s) for none of the above? \n")

if status == '1':
    print('*'*72 + len(name)*'*')
    print('*', ' '*67, len(name)*' ', '*')
    print("*  __" + name +
          ", welcome to my quiz-generator for elementary school students.__  *")
    print('*', ' '*67, len(name)*' ', '*')
    print('*'*72 + len(name)*'*')
    practice = input(
        name + " what would you like to practice? Enter\n0 for subtraction\n1 for exponentiation\n")
    if practice == '0' or practice == '1':
        q = input(
            "How many practice questions would you like to do? Enter 0, 1, or 2: ")
        if(int(q) == 1 or int(q) == 2):
            result = elementary_school_quiz(int(practice), int(q))
            percentage = result / int(q)
            if(percentage == 1):
                print("Congratulations " + name +
                      "! You'll probably get an A tomorrow.")
            elif(percentage == 0.5):
                print("You did ok " + name +
                      ", but I know you can do better.")
            else:
                print("I think you need some more practice " + name + ".")
        elif(int(q) == 0):
            print("Zero questions. OK. Good bye")
        else:
            print(
                "Only 0, 1, or 2 are valid choices for the number of questions.")
    else:
        print("Invalid choice. Only 0 or 1 is accepted.")
elif status == '2':
    print('*'*61 + len(name)*'*')
    print('*', ' '*56, len(name)*' ', '*')

    print("*  __quadratic equation, a·x^2 + b·x + c= 0, solver for " + name + "__  *")
    print('*', ' '*56, len(name)*' ', '*')
    print('*'*61 + len(name)*'*')

    flag = True
    while flag:
        question = input(
            name+", would you like a quadratic equation solved?  ")

        if question.lower() != "yes":
            flag = False
        else:
            print("Good choice!")
            a = input("Enter a number for the coefficient of a: ")
            b = input("Enter a number for the coefficient of b: ")
            c = input("Enter a number for the coefficient of c: ")
            high_school_quiz(float(a), float(b), float(c))
else:
    print(name, "you are not the target audience for this software")

print("Good bye "+name+"!")
