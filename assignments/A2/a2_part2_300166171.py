# Family name: Adam Jasniewicz
# Student number:  300166171
# Course: ITI 1120
# Assignment Number 2
# year 2020


########################
# Question 2.1
########################


def min_enclosing_rectangle(radius, x, y):
    '''
    (Number, Number, Number) -> (Number, Number)
    Description: Calculates the x and y-coordinates of the bottom left corner of the smallest axis-aligned rectangle that could contain the circle
    Preconditions: All 3 numbers are real numbers (if radius is negative function will return none)
    '''
    if radius < 0:
        return None
    return (x-radius, y-radius)


########################
# Question 2.2
########################


def vote_percentage(results):
    '''
    (string) -> Number
    Description: Calculates the percentage of yes in the paramater results among all other substrings (yes, no and abastained (abstained does not count towards the percentage, it is ignored)
    Preconditions: Results only contains yes,no or abstained and at least one yes or no
    '''
    if(results.count('no') == 0):
        return 1
    if(results.count('yes') == 0):
        return 0
    yes = results.count('yes')
    no = results.count('no')
    return yes/(yes+no)


########################
# Question 2.3
########################

def vote():
    '''
    (None) -> None
    Description: Invokes the user to enter a string of yes', no's and abastained's, after it prints if the vote is unanimous, a super majority, simple majority or if it fails
    Preconditions: Input contains only yes', no's and abastains
    '''
    result = vote_percentage(
        input("Enter the yes, no, abstained votes one by one and then press enter: "))
    if result == 1:
        print("proposal passes unanimously")
    elif result >= 2/3:
        print("proposal passes with super majority")
    elif result >= .5:
        print("proposal passes with simple majority")
    else:
        print("proposal fails")
