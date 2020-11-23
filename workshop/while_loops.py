def while1():
    while True:
        print('THIS WILL PRINT FOREVER')

def while2():
    user_input = input("Please put in your input: ")
    while user_input != 'exit':
        print('Running while loop')
        user_input = input("Please put in your input: ")

def for1():
    a  = ['item1', 'item2', 'item3', 'item4']
    for item in a:
        print(item)


def for2():
    a  = ['item1', 'item2', 'item3', 'item4']
    for item in a:
        print(item)
        for char in item:
            print(char)


def squarefree(s):
    # We store a length to make sure that we pick the longest square free pair
    stored_length = 0
    # To increase speed (big O), the length of one of the pairs can only be up to half the length of the string
    #range -> iterates of the length of the string / 2
    #this actualy keeps track of the length
    for length in range((len(s)//2)):
        #now we actually want to go through the entire string
        for position in range(len(s)):
            # we slice the string so that we get it's current position to the length of the string
            value =s[position:position+length+1]
            # now we check if the sliced string is found twice throughout the entire string
            if s.count(value) == 2:
                #this is uncessarary 
                # if(length+1>stored_length):
                # now we check if the value we found is behind or in front of the value (next to it)
                if(value == s[position+length+1: position+length+1+length+1] or value == s[position-length-1: position]):
                    return False

def main():
    pass

if __name__ == "__main__":
    main()