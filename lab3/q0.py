def pay(wage, hours):
    '''
    (Number, Number) -> Number
    Calculates employees pay (includes overtime)
    Precondition: wage and hours are positive integers
    '''

    if hours <= 40:
        return hours*wage
    if(40 < hours <= 60):
        return 40 * wage + (hours-40) * wage*1.5
    if(hours > 60):
        regular = 40*wage
        overtime = 20*wage*1.5
        superovertime = (hours-60)*wage*2
        print(regular, overtime, superovertime)
        return regular + overtime + superovertime


def rps(player1, player2):
    '''(string, string) -> Number
    Returns 0 if player1 and player2 tied, -1 if player1 won, and 1 if player2 won in the game of rock paper scissors
    Precondition: both paramaters is one of the following strings (R,S,P)
    '''
    if(player1 == player2):
        return 0
    if(player1 == 'R' and player2 == 'S' or player1 == 'S' and player2 == 'P' or player1 == 'P' and player2 == 'R'):
        return -1
    return 1


def is_divisible(n, m):
    '''(number, number) -> boolean
    Returns True if paramater1 is divisible by paramater2 and false if it's not
    Precondition: paramater1 and paramater2 are both integers
    '''
    return n % m == 0


def is_divisible23n8(value):
    '''(number) -> string
    Returns yes if the paramater is divisible by 3 and 2 but not 8 (if the opposite it returns "no")
    Precondition: the paramater is an integer
    '''
    if(is_divisible(value, 3) and is_divisible(value, 2) and not(is_divisible(value, 8))):
        return "yes"
    return "no"


def a3():
    n = input("Enter 1st integer: ")
    m = input("Enter 2nd integer: ")
    if(is_divisible(int(n), int(m))):
        print(n + " is divisible by " + m)
    else:
        print(n + " is not divisible by " + m)


def b3():
    n = input("Enter an integer: ")
    if(is_divisible23n8(int(n)) == "yes"):
        print(n + " is divisible by 2 or 3 but no 8")
    else:
        print("It is not true that " + n + " is divisible by 2 or 3 but no 8")


if __name__ == "__main__":
    # a3()
    b3()
