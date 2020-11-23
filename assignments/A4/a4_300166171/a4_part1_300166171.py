# ITI1120 Assignment 4 - PT 1
# Adam Jasniewicz 300166171


def is_valid_file_name():
    '''()->str or None'''
    file_name = None
    try:
        file_name=input("Enter the name of the file: ").strip()
        f=open(file_name)
        f.close()
    except FileNotFoundError:
        print("There is no file with that name. Try again.")
        file_name=None
    return file_name 

def get_file_name():
    file_name=None
    while file_name==None:
        file_name=is_valid_file_name()
    return file_name

def clean_word(word):
    '''(str)->str
    Returns a new string which is lowercase version of the given word
    with special characters and digits removed

    The returned word should not have any of the following characters:
    ! . ? : , ' " - _ \ ( ) [ ] { } % 0 1 2 3 4 5 6 7 8 9 tab character and new-line character

    >>> clean_word("co-operate.")
    'cooperate'
    >>> clean_word("Anti-viral drug remdesivir has little to no effect on Covid patients' chances of survival, a study from the World Health Organization (WHO) has found.")
    'antiviral drug remdesivir has little to no effect on covid patients chances of survival a study from the world health organization who has found'
    >>> clean_word("1982")
    ''
    >>> clean_word("born_y1982_m08\n")
    'bornym'

    '''
    new_s = ''
    for char in word:
        if char in "!.?:,'\"-_\()[]{}%0123456789\n\t":
            if char == "\n":
                new_s = new_s + " "
            pass
        else:
            new_s = new_s + char
    return new_s


def test_letters(w1, w2):
    '''(str,str)->bool
    Given two strings w1 and w2 representing two words,
    the function returns True if w1 and w2 have exactlly the same letters,
    and False otherwise

    >>> test_letters("listen", "enlist")
    True
    >>> test_letters("eekn", "knee")
    True
    >>> test_letters("teen", "need")
    False
    '''
    
    #YOUR CODE GOES HERE
    if(len(w1) == len(w2)):
        for char in w1:
            string1_occurence = w1.count(char)
            string2_occurence = w2.count(char)
            if string1_occurence != string2_occurence:
                return False
    else:
        return False
    return True
    
def create_clean_sorted_nodupicates_list(s):
    '''(str)->list of str
    Given a string s representing a text, the function returns the list of words with the following properties:
    - each word in the list is cleaned-up (no special characters nor numbers)
    - there are no duplicated words in the list, and
    - the list is sorted lexicographicaly (you can use python's .sort() list method or sorted() function.)

    This function must call clean_word function.

    You may find it helpful to first call s.split() to get a list version of s split on white space.
    
    >>> create_clean_sorted_nodupicates_list('able "acre bale beyond" binary boat brainy care cat cater crate lawn\nlist race react cat sheet silt slit trace boat cat crate.\n')
    ['able', 'acre', 'bale', 'beyond', 'binary', 'boat', 'brainy', 'care', 'cat', 'cater', 'crate', 'lawn', 'list', 'race', 'react', 'sheet', 'silt', 'slit', 'trace']

    >>> create_clean_sorted_nodupicates_list('Across Europe, infection rates are rising, with Russia reporting a record 14,321 daily cases on Wednesday and a further 239 deaths.')
    ['', 'a', 'across', 'and', 'are', 'cases', 'daily', 'deaths', 'europe', 'further', 'infection', 'on', 'rates', 'record', 'reporting', 'rising', 'russia', 'wednesday', 'with']
    '''
    
    #YOUR CODE GOES HERE
    new_s = ''
    for item in s:
        new_s = new_s + clean_word(item.lower())
    new_s = new_s.split()
    new_s.sort()
    
    new_new_s = []
    for item in new_s:
        if new_new_s.count(item.lower()) >= 1:
            pass
        else:
            new_new_s.append(item.lower())
    return new_new_s

def word_anagrams(word, wordbook):
    '''(str, list of str) -> list of str
    - a string (representing a word)
    - wordbook is a list of words (with no words duplicated)

    This function should call test_letters function.

    The function returs a (lexicographicaly sorted) list of anagrams of the given word in wordbook
    >>> word_anagrams("listen", wordbook)
    ['enlist', 'silent', 'tinsel']
    >>> word_anagrams("race", wordbook)
    ['acre', 'care']
    >>> word_anagrams("care", wordbook)
    ['acre', 'race']
    >>> word_anagrams("year", wordbook)
    []
    >>> word_anagrams("ear", wordbook)
    ['are', 'era']
    '''

    anagrams = []
    for string2 in wordbook:
        if test_letters(word,string2):
            anagrams.append(string2)

    if(anagrams.count(word) != 0):
        anagrams.remove(word)
        anagrams.sort()
    return anagrams

def word_anagrams_without_remove(word, wordbook):
    '''
    (str, list of str) -> list of str
    - a string (representing a word)
    - wordbook is a list of words (with no words duplicated)

    The function returs a (lexicographicaly sorted) list of anagrams of the given word in wordbook without removing the initial word
    '''
    anagrams = []
    for string2 in wordbook:
        if test_letters(word,string2):
            anagrams.append(string2)
    return anagrams
        

def count_anagrams(l, wordbook):
    '''(list of str, list of str) -> list of int

    - l is a list of words (with no words duplicated)
    - wordbook is another list of words (with no words duplicated)

    The function returns a list of integers where i-th integer in the list
    represents the number of anagrams in wordbook of the i-th word in l.
    
    Whenever a word in l is the same as a word in wordbook, that is not counted.

    >>> count_anagrams(["listen","care", "item", "year", "race", "ear"], wordbook)
    [3, 2, 3, 0, 2, 2]

    The above means that "listen" has 3 anagrams in wordbook, that "care" has 2 anagrams in wordbook ...
    Note that wordbook has "care", "race" and "acre" which are all anagrams of each other.
    When we count anagrams of "care" we count "race" and "acre" but not "care" itself.
    '''

    anagrams = []
    for string1 in l:
        count = 0
        skip=False
        for string2 in wordbook:
            if(len(string2) == len(string1)):
                for char in string1:
                    string1_occurence = string1.count(char)
                    string2_occurence = string2.count(char)
                    if string1_occurence != string2_occurence:
                        skip = True
                
                if skip== False:
                    count +=1
                else:
                    skip=False
        if count != 0:
            anagrams.append(count -1)
        else:
            anagrams.append(count)
    return anagrams



def k_anagram(l, anagcount, k):
    '''(list of str, list of int, int) -> list of str

    - l is a list of words (with no words duplicated)
    - anagcount is a list of integers where i-th integer in the list
    represents the number of anagrams in wordbook of the i-th word in l.

    The function returns a  (lexicographicaly sorted) list of all the words
    in l that have exactlly k anagrams (in wordbook as recorded in anagcount)

    k_anagram(["listen","care", "item", "year", "race", "ear"], [3, 2, 3, 0, 2, 2], 2)
    ['care', 'ear', 'race']
    '''
    index = 0
    max_array = []
    for item in anagcount:
        if item == int(k):
            max_array.append(l[index])
        index +=1

    max_array.sort()
    return max_array

def max_anagram(l, anagcount):
    '''(list of str, list of int) -> list of str
    - l is a list of words (with no words duplicated)
    - anagcount is a list of integers where i-th integer in the list
    represents the number of anagrams in wordbook of the i-th word in l.

    The function returns a (lexicographicaly sorted) list of all the words
    in l with maximum number of anagrams (in wordbook as recorded in anagcount)
    
    >>> max_anagram(["listen","care", "item", "year", "race", "ear"], [3, 2, 3, 0, 2, 2])
    ['item', 'listen']
    '''
    
    index = 0
    max_array = []
    for item in anagcount:
        if item == max(anagcount):
            max_array.append(l[index])
        index +=1

    max_array.sort()
    return max_array

def zero_anagram(l, anagcount):
    '''(list of str, list of int) -> list of str
    - l is a list of words (with no words duplicated)
    - anagcount is a list of integers where i-th integer in the list
    represents the number of anagrams in wordbook of the i-th word in l.

    The function returns a (lexicographicaly sorted) list of all the words
    in l with no anagrams
    (in wordbook as recorded in anagcount)
    
    >>> zero_anagram(["listen","care", "item", "year", "race", "ear"], [3, 2, 3, 0, 2, 2])
    ['year']
    '''
    index = 0
    max_array = []
    for item in anagcount:
        if item == 0:
            max_array.append(l[index])
        if item=="asap":
            print(item, "!!!")
        index +=1
    
    max_array.sort()
    return max_array

##############################
# main
##############################
wordbook=open("english_wordbook.txt").read().lower().split()
list(set(wordbook)).sort()

print("Would you like to:")
print("1. Analize anagrams in a text -- given in a file")
print("2. Get small help for Scrabble game")
print("Enter any character other than 1 or 2 to exit: ")
choice=input()

if choice=='1':
    file_name=get_file_name()
    rawtx = open(file_name).read()
    l=create_clean_sorted_nodupicates_list(rawtx)
    anagcount = count_anagrams(l,wordbook)

    print("\nOf all the words in your file, the following words have the most anagrams:")
    maximum_anagrams = max_anagram(l, anagcount)
    print(maximum_anagrams)
    for item in maximum_anagrams:
        print("Anagrams of " + item + " are " + str(word_anagrams(item, wordbook)))
    print('Here are the words in your file that have no anagrams')
    zero_anagrams = zero_anagram(l, anagcount)
    print(zero_anagrams)
    print("Say you are in if there is a word in your file that has exactly k anagrams")
    k=input("Enter an integer for k: ")
    k_words = k_anagram(l,anagcount,k)
    print("Here is a word (words) in your file with exactly 2 anagrams:")
    print(k_words)
    
elif choice=='2':
    w1 = input("Enter the letters that you have, one after another with no space: ")
    while " " in w1:
        print("Error: You entered space(s). ")
        w1 = input("Enter the letters that you have, one after another with no space: ")

    
    print("Would you like help forming a word with\n1. all these letters\n2. all but one of these letter")
    user_input = input("")
    while user_input != str(1) and user_input != str(2):
        print("You must choose 1 or 2. Please try again.")
        print("Would you like help forming a word with\n1. all these letters\n2. all but one of these letter")
        user_input = input("")
    if(user_input == str(1)):
        total_words = word_anagrams_without_remove(w1, wordbook)
        if(len(total_words) == 0):
            print("There is no word compromised of exactly these letters")
        else:
            print("Here are the words that are comprised of exactly these letters: ")
            print(total_words)
    if(user_input == str(2)):
        print("The letters you gave us are: " + w1)
        print("Let's see what we can get if we ommit one of these letters.")
        for position in range(len(w1)):
            new_word = ''
            for char in range(len(w1)):
                if position == char:
                    pass
                else:
                    new_word = new_word + w1[char]
            print("Without the letter in position " + str(position+1) + " we have letters: " + new_word)
            total_words = word_anagrams_without_remove(new_word, wordbook)
            if(len(total_words) == 0):
                print("There is no word compromised of letters " + new_word)
            else:
                print("Here are the words that are comprised of letters: " + new_word)
                print(total_words)


                       
                      
else:
    print("Good bye")


