# ITI1120 Assignment 4 - PT 2 -2
# Adam Jasniewicz 300166171


def two_length_run(array):
    '''
    array -> array of floats

    Returns True if the give list has at least one run (of length at least two)
    '''
    last_run = None;
    for run in array:
        if run == last_run:
            return True
        last_run = run
    return False


raw_input = input("Please input a list of numbers separated by space: ").strip().split()
number_input = []
for string in raw_input:
    number_input.append(float(string))
print(two_length_run(number_input))
