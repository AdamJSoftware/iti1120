# Name: Adam Jasniewicz
# Student number:  300166171
# Course: IT1 1120
# Test Number 1
# year 2020


########################
# Question 1
########################


def atlantic(sn):
    '''
    (number) -> (string)
    '''
    if(len(sn) >= 9):
        return 'new'
    return 'old'


########################
# Question 2
########################


def southern(n):
    '''
    (number) -> (none)
    '''
    if(n == 1):
        pounds = input("Enter a number of the weight in pounds: ")
        ounces = input("Enter a number of the weight in ounces: ")
        kg = (float(pounds)*16+float(ounces))*0.02835
        print(str(pounds) + " pounds and " + str(ounces) +
              " ounces is (approximately) " + str(kg) + " kilograms")
    else:
        name = input("What is your name? ")
        snum = input("What is your student number? ")
        print(name + " you have " + atlantic(snum) + " student number")


########################
# Question 3
########################


def pacific(g1, g2, g3):
    '''
    (number, number, number) -> (boolean)
    '''
    condition1 = (g1 >= 50) and (g2 >= 50) and (g3 >= 50)
    condition2 = (g1 >= 80) or (g2 >= 80) or (g3 >= 80)
    return condition1 and condition2


########################
# Question 4
########################


def arctic(n):
    '''
    (number) -> (boolean)
    '''
    if(n/1000 < 10):
        num1 = n//1000
        num2 = (n//100) % 10
        num3 = n % 100//10
        num4 = n % 10
        return (num1 == num4) and (num2 == num3)
    else:
        num1 = n//100000
        num2 = (n//10000) % 10
        num3 = n % 10000//1000
        num4 = n % 1000//100
        num5 = n % 100//10
        num6 = n % 10
        return (num1 == num6) and (num2 == num5) and (num3 == num4)
