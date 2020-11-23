# ITI1120 Assignment 4 - PT 2 -1
# Adam Jasniewicz 300166171


def number_divisible(numbers, divisor):
    '''
    numbers -> list of numbers
    divisor -> number

    returns an integer of all the numbers that can be divided by the divisor
    '''
    i = 0
    for number in numbers:
        if number %divisor == 0:
            i+=1

    return i


raw_input = input("Please input a list of numbers separated by space: ").strip().split()
number_input = []
for string in raw_input:
    number_input.append(int(string))
divisor = input("Please input an integer: ")
print("The number of elements divisible by " + divisor + " is " + str(number_divisible(number_input, int(divisor))))
