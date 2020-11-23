# ITI1120 Assignment 4 - PT 2 -2
# Adam Jasniewicz 300166171

def longest_run(array):
    '''
    array -> array of floats

    Returns the length of the longest run
    '''
    last_run = None;
    run_lengths = []
    same_run = False
    if len(array) != 0:
        for run in array:
            if run == last_run:
                if same_run:
                    run_lengths[-1] = run_lengths[-1] + 1
                else:
                    same_run = True
                    run_lengths.append(2)
            else:
                run_lengths.append(1)
                same_run = False
            last_run = run
        return max(run_lengths)
    return 0


raw_input = input("Please input a list of numbers separated by space: ").strip().split()
number_input = []
for string in raw_input:
    number_input.append(float(string))
print(longest_run(number_input))
