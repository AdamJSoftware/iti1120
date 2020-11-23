# Family name: Adam Jasniewicz
# Student number:  300166171
# Course: ITI 1120
# Assignment Number 3.2
# year 2020

import math

########################
# Question 2.1
########################

def sum_odd_divisors(n):
    '''
    (Number) -> None or Number
    Description: returns the sum of all positive divisors of n (if n is not zero)
    Preconditions: n is an integer
    '''
    if(n==0):
        return None
    x = 0

    for i in range(abs(n) + 1):
        if(i%2 != 0):
            if(abs(n)%i == 0):
                x = x+i

    return x

########################
# Question 2.2
########################
    
def series_sum():
    '''
    (None) -> None or Number
    Description: if the user inputs a positive integer, it returns the sum of a series (1000+1/n**2)
    Preconditions: none
    '''
    n = input("Number: ")

    if(n.isdigit()):
        n = int(n)

        x = 1000
        for i in range(n):
            i = i+1
            x = x + 1/i**2
        return x
    return None
########################
# Question 2.3
########################

def pell(n):
    '''
    (None) -> None or Number
    Description: if the user inputs a positive integer, it returns the sum of a series (1000+1/n**2)
    Preconditions: none
    '''
    if(n<0):
        return None
    if(n==0):
        return 0
    if(n==1):
        return 1
    if(n==2):
        return 2
    val1 = 1
    val2 = 2

    n = n+1
    final_value = 2

    for i in range(3, n) : 
        final_value = final_value+val1+val2
        temp_val2 = val2
        val2 = final_value
        val1= temp_val2
    return final_value

########################
# Question 2.4
########################

def countMembers(s):
    '''
    (String) -> Number
    Description: counts the amount of times an extraordinar character appears
    Preconditions: s is a string
    '''
    x = 0
    for i in s:
        if i in "\\efghijFGHIJKLMNOPQRSTUVWX!23456,":
            x = x +1
    return(x)

########################
# Question 2.5
########################
    
def casual_number(s):
    '''
    (String) -> None or int
    Description: If s is a proper financial value, it will return the financial value as an integer
    Preconditions: s is a string containing only numbers with probably positioned commas
    '''
    s = s.replace(',', '')
    flag = False
    if(s[0] == '-'):
        flag = True
        s = s[1:]
    if(s.isdigit()):
        s = int(s)
        if(flag):
            s = s *-1
            return s
        return s
    return None

########################
# Question 2.6
########################

def alienNumbers(s):
    '''
    (String) -> int
    Description: Returns the the value of the alien symbols
    Preconditions: s is a string
    '''
    return s.count("T")*1024 + s.count("y")*598 + s.count("!")*121 + s.count("a")*42 + s.count("N")*6 + s.count("U")*1

########################
# Question 2.7
########################

def alienNumbersAgain(s):
    '''
    (String) -> int
    Description: Returns the the value of the alien symbols (without string methods)
    Preconditions: s is a string
    '''
    x = 0
    for i in s:
        if i == "T":
            x = x +1024
        if i == "y":
            x = x +598
        if i == "!":
            x = x +121
        if i == "a":
            x = x +42
        if i == "N":
            x = x +6
        if i == "U":
            x = x +1
    return x

########################
# Question 2.8
########################

def encrypt(s):
    '''
    (String) -> String
    Description: Returns the encrypted string
    Preconditions: s is a string
    '''
    newS = ''
    for i in range(len(s)):
        newS = newS + s[len(s)-(i+1)]
    new_new_s = ''
    for i in range(0,len(newS)):
        if((i%2==0)):
            new_new_s = new_new_s + newS[i//2]
        else:
            new_new_s = new_new_s + newS[-((i+1)//2)]

    return new_new_s

########################
# Question 2.9
########################

def waveop(s):
    '''
    (String) -> String
    Description: Returns a string with lowercase or capitalized o's and p's (depending on the capitalization of the pair of characters) in between pairs of characters
    Preconditions: s is a string
    '''
    last_value = ''
    new_s = ''
    for i in range(len(s)):
        if(i==0):
            new_s = new_s + s[i]
        else:
            if s[i].isalpha() and last_value.isalpha():
                if last_value.isupper():
                    new_s = new_s + "O"
                else:
                    new_s = new_s + "o"
                if s[i].isupper():
                    new_s = new_s + "P"
                else:
                    new_s = new_s + "p"
            new_s = new_s + s[i]
        last_value = s[i]
        
    return new_s

########################
# Question 2.10
########################

def squarefree(s):
    '''
    (String) -> Boolean
    Description: Returns if a string is square free
    Preconditions: s is a string
    '''
    stored_length = 0
    for length in range((len(s)//2)):
        for position in range(len(s)):
            value =s[position:position+length+1]
            if s.count(value) == 2:
                if(length+1>stored_length):
                    if(value == s[position+length+1: position+length+1+length+1] or value == s[position-length-1: position]):
                        return False
    return True
