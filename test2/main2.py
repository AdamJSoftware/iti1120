def get_list_ofint(s): # 5 points
    '''(str)->list of int
     Precondition: s string that looks like a sequence in integers where
     every pair of consecutive integers is separated by a comma followed by a space or a space

     More preconditions: s has at least one substring that looks like an integer
     
     Returns a list of integers from s
     
     >>> get_list_ofint("10 22, 7 0 -5, 1")
     [10, 22, 7, 0, -5, 1]
     >>> get_list_ofint("231, -5, 12")
     [231, -5, 12]
     >>> get_list_ofint("231 -5 -7")
     [231, -5, -7]
     >>> get_list_ofint("-7,")
     [-7]
    '''

    a = s.split(' ')
    index  = 0
    for item in a:
        if ',' in item:
            new_number = ''
            for string in item:
                if string == ',':
                    pass
                else:
                    new_number = new_number + string
            a[index] = int(new_number)
        else:
            a[index] = int(item)
                
        index = index + 1
    
    return a

def list_work(l): 
    '''
    >>> list_work([1, 7, 5, 4, 12, -33, 6])
     [8, 12, 0, 16, 0, 0]
     >>> list_work([1])
     [1]
     >>> list_work([])
     []
     >>> list_work([1,2,3,4,5])
     [0, 0, 0, 0]
     >>> list_work([100,20,30])
     [120, 50]
    '''
    last_number = None
    new_list = []
    if len(l) > 1:
        for item in l:
            if last_number != None:
                if (item%2 == 0 and last_number%2 == 0) or (item%2 != 0 and last_number%2 != 0):
                    new_list.append(item + last_number)
                else:
                    new_list.append(0)
            last_number = item
        return new_list
    return l


def pattern_to_stars(s, p): # 10 points
    '''(str, str)->str

     Precondition: p is not an empty string and all letters are lower-case

     Given a string s and another string p the function returns a new string where
     the first occurrence of p in s is replaced with one star, the second occurrence with two stars
     and so on. 
     
     You may assume that no two patterns p in s overlap in s. Example:
     p="aa" s="aaab" cannot happen since "aa" pattern in the first two positions
     overlaps with "aa" pattern in the next two positions in s

     You CANNOT use the replace method from str module.
     Using that method will result in receiving zero for this function.

     Hints:
     - slicing may be helpful in this question
     - it may be easier to solve this problem with a while loop
     
     >>> pattern_to_stars("trabsabtt", "ab")
     'tr*s**tt'
     >>> pattern_to_stars("today123is123nice123d", '123')
     'today*is**nice***d'
     >>> pattern_to_stars("1a2b3", '123')
     '1a2b3'
     >>> pattern_to_stars("chipchip", 'chip')
     '***'
     >>> pattern_to_stars('', 'chip')
     ''
    '''
    occurence = 1
    new_string = ''
    skip = 0
    for item in range(0, len(s)):
        if skip == 0:
            value = s[item: item + len(p)]
            if(value == p):
                new_string = new_string + '*'*occurence
                occurence = occurence + 1
                skip = len(p) - 1
            else:
                new_string = new_string + s[item]
        else:
            skip = skip - 1
    return new_string



print(get_list_ofint("10 22, 7 0 -5, 1"))
print(get_list_ofint("231, -5, 12"))
print(get_list_ofint("231 -5 -7"))
print(get_list_ofint("-7,"))

print('*************')

print(list_work([1, 7, 5, 4, 12, -33, 6]))
print(list_work([1]))
print(list_work([]))
print(list_work([1,2,3,4,5]))
print(list_work([100,20,30]))

print('*************')


print(pattern_to_stars("trabsabtt", "ab"))
print(pattern_to_stars("today123is123nice123d", "123"))
print(pattern_to_stars("1a2b3", "123"))
print(pattern_to_stars("chipchip", "chip"))
print(pattern_to_stars("", "chip"))
