# Family name: Adam Jasniewicz
# Student number:  300166171
# Course: IT1 1120
# Assignment Number 1
# year 2020


import math
import turtle
s = turtle.Screen()
t = turtle.Turtle(shape='turtle')


########################
# Question 1
########################


def f_to_k(t):
    '''(number,number)->number
    Returns the area of a triangle with a given base and height
    Precondition: base and height are non-negative numbers
    '''
    return round((t-32)*(5/9)+273.15, 2)

#######################
# Question 2
#######################


def poem_generator():
    '''(None)->None
    Prints a poem based on inputed name and city
    Precondition: None
    '''
    name = input("What is your name: ")
    city = input("What is your city: ")
    print("There was a small boy of " + city)
    print("Who was buried in snow to his neck")
    print("When they said, 'Are you " + name + "?'")
    print("He replied, 'Yes, I is —")
    print("But we don’t call this cold in " + city + "'")

#######################
# Question 3
#######################


def impl2loz(w):
    '''(number)-> (number,number)
    Returns a pair of numbers that resolves w(parameter) = l + o/16. l is an integer and o is a non-negative number smaller than 16
    Precondition: w (parameter) is a non-negative number
    '''
    l = int(w)
    o = w % 1*16
    return (l, o)

#######################
# Question 4
#######################


def pale(n):
    '''(number)-> boolean
    Returns if number is pale
    Precondition: n (parameter) positive 4 digit integer
    '''
    num1 = n//1000
    num2 = (n//100) % 10
    num3 = n % 100//10
    num4 = n % 10
    consecutive = (num1 == 3 and num2 == 3) or (
        num2 == 3 and num3 == 3) or (num3 == 3 and num4 == 3)
    return not(consecutive or num4 % 4 == 0)

#######################
# Question 5
#######################


def bibformat(author, title, city, publisher, year):
    '''(string, string, string, string, string)-> string
    Returns bibliographical format of provided author, title, city, publisher and year
    Precondition: author, title, city, publisher and year are strings
    '''
    return author + " ("+str(year) + "). " + title + ". " + city + ": " + publisher + "."

#######################
# Question 6
#######################


def bibformat_display():
    '''(None)-> None
    Prompts user for the the book title, author, year publisher and city and prints bibliographical fromat
    Precondition: none
    '''
    title = input("Enter the title of a book: ")
    author = input("Enter the name of the author? ")
    year = input("What year was the book published? ")
    publisher = input("Enter the name of the publisher: ")
    city = input("In what city are the headquarters of the publisher? ")
    print(bibformat(author, title, city, publisher, year))


#######################
# Question 7
#######################

def compound(x, y, z):
    '''(number, number, number)-> boolean
    Returns true only if x (paramter 1) is the only even number among all 3 paramaters and if any pair of the 3 paramaters add up to a number greater than 100
    Precondition: x, y and z are integers
    '''
    condition1 = x % 2 == 0
    condition2 = (y % 2 == 0 or z % 2 == 0) == False
    condition3 = x + y > 100 or x + z > 100 or y + z > 100
    return condition1 and condition2 and condition3

#######################
# Question 8
#######################


def funct(p):
    '''(number)-> none
    Prints a sentenced with the resolved value of r of the following equation ((5**r)**2)-p+10=0 base on paramater p
    Precondition: p (paramater) is an integer greater or equal to 11
    '''
    print("The solution is " + str(math.sqrt(math.log(p-10)/math.log(5))))

#######################
# Question 9
#######################


def gol(n):
    '''(number)-> number
    Returns the minimum number of times that n (paramater) needs to be divided by 2 in order to get a number equal or smaller than 1
    Precondition: n (paramater) is greater or equal to 1
    '''
    return math.ceil(math.log2(n))

#######################
# Question 10
#######################


def draw_rocket():
    '''(none)-> none
    Draws a rocket using turtle graphics
    Precondition: turtle package is installed
    '''
    t.up()
    t.goto(0, -150)
    t.down()
    t.seth(-45)
    t.circle(20, 90)
    t.circle(300, 90)
    t.circle(20, 90)
    t.circle(300, 90)
    t.penup()

    t.goto(0, 50)
    t.pendown()

    t.circle(20)
    t.penup()

    t.goto(0, 100)
    t.pendown()

    t.circle(20)
    t.penup()

    t.goto(0, 150)
    t.pendown()

    t.circle(20)
    t.penup()

    t.goto(-65, -50)
    t.pendown()
    t.goto(-130, -100)
    t.goto(-110, -200)
    t.goto(-90, -190)
    t.goto(-90, -130)
    t.goto(-40, -90)

    t.penup()

    t.goto(65+25, -50)
    t.pendown()
    t.goto(130+25, -100)
    t.goto(110+25, -200)
    t.goto(90+25, -190)
    t.goto(90+25, -130)
    t.goto(40+25, -90)

    t.penup()
    t.goto(-20, -120)
    t.pendown()
    t.seth(90)

    t.circle(200, -45)
    t.up()
    t.right(45)
    t.pendown()
    t.forward(180)
    t.seth(270)

    t.penup()
    t.goto(50, -120)
    t.pendown()
    t.seth(270)

    t.circle(200, 45)

    turtle.Screen().exitonclick()


#######################
# Question 11
#######################


def cad_cashier(price, payment):
    '''(number, number)-> number
    Returns the difference between the payment and the price using canadian currency (5 cents is the lowest valid currency)
    Precondition: price (paramater 1) and payment (paramater 2) are two real non-negative numbers withtwo decimal places. payment >= price and the second decimal in payment is 0 or 5
    '''
    decimal = (round((round(payment-price, 2)*100 % 10)/5)*5)
    return round(math.floor((payment-price)*10)/10 + decimal * 0.01, 2)


#######################
# Question 12
#######################


def min_CAD_coins(price, payment):
    '''(number, number)-> number
    Returns 5 numbers that represent (toonies, loonies, quarters, dimes and nickles) based on the difference between payment and price using canadian currency
    Precondition: price (paramater 1) and payment (paramater 2) are two real non-negative numbers withtwo decimal places. payment >= price and the second decimal in payment is 0 or 5
    '''
    final = round(cad_cashier(price, payment) * 100)
    toonies = math.floor(final/200)
    final = final - toonies*200
    loonies = math.floor(final/100)
    final = final - loonies * 100
    quarters = math.floor(final/25)
    final = final - quarters * 25
    dimes = math.floor(final/10)
    final = final - dimes * 10
    nickles = math.floor(final/5)
    final = final - nickles * 5
    return (toonies, loonies, quarters, dimes, nickles)
