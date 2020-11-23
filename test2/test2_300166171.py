'''
I understand the importance of professional integrity in my education and future career
in engineering or computer science. I hereby certify that I have done and will do all work
on this examination entirely by myself, without outside assistance or the use of unauthorized
information sources. Furthermore, I will not provide assistance to others.
'''

# READ THE ABOVE STATEMENT
#
# ADAM JASNIEWICZ
# 300166171
#
# By putting your name here you are signing the statement above and
# agreeing to the TEST 2 (integrity rules) listed on the first page of the test


def list_work(l): # 10 points
    '''(list of int)->list of int

     The function returns a new list where for every pair of consecutive elements in l
     if both are odd or both are even then the sum of the two elements is added to the new list
     otherwise zero is added to the new list. For example, in a list l=[1, 7, 5, 4, 12],
     1 and 7 are both odd, so we add their sum, 8, to the new list
     7 and 5 are both odd, so we add their sum, 12, to the list
     5 and 4 are neither both odd nor both even, so we add zero to the list
     4 and 12 are both even, so we add their sum, 16,  to the list.
     Thus the function returns the list [8, 12, 0, 16]
     
     If l has at most 1 element, then a copy of list l is returned

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


               
          

# main
print("Enter A or B to choose one of the following two options:\n")        
print("A: Would work with numbers?")
print("B: Would like to replace a pattern with stars?\n") 

answer = input("Enter A or B (lower or upper case accepted): ")

# 5 points
# You should code here a part where your program keeps on asking
# the user for "A" or "B" until the user finally enters it. Your solution
# should accept lower case and upper case A or B and it should
# should remove any extra white space. See test2_Runs.txt for example runs


# YOUR CODE GOES HERE:
answer = answer.lower().strip()

while answer != 'a' and answer != 'b':
    print("Invalid Input")
    answer = input("Enter A or B (lower or upper case accepted): ")

    answer = answer.lower().strip()



if answer=="a":
    rawl=input("Enter a sequence of integers separated by either one space or a comma then one space.\n")
    print("You entered:", rawl)
    givenl=get_list_ofint(rawl)
    print("The given list of ints is", givenl)
    print("The list produced after prescribed work is", list_work(givenl))

        
else:
    s=input("Enter a string: ").lower()
    p=input("Enter a non-empty pattern string: ").lower()
    print("Here is a result of replacing pattern", p, "in", s, "with some stars:")
    print(pattern_to_stars(s,p))


