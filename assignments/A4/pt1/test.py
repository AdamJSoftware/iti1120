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



def main(s):
    new_s = ''
    for item in s:
        new_s = new_s + clean_word(item.lower())
    new_s = new_s.split()
    new_s.sort()
    print('here')
    print(new_s)
    
    new_new_s = []
    for item in new_s:
        if new_new_s.count(item.lower()) >= 1:
            pass
        else:
            new_new_s.append(item.lower())
    return new_new_s

def count_anagrams(l):
    wordbook=open("english_wordbook.txt").read().lower().split()
    list(set(wordbook)).sort()
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
        anagrams.append(count -1)
    return anagrams

# def make_anagrams(s):

#     wordbook=open("english_wordbook.txt").read().lower().split()
#     list(set(wordbook)).sort()


def max_anagram(l = ["listen","care", "item", "year", "race", "ear"], r = count_anagrams(["listen","care", "item", "year", "race", "ear"])):
    '''(list of str, list of int) -> list of str
    - l is a list of words (with no words duplicated)
    - anagcount is a list of integers where i-th integer in the list
    represents the number of anagrams in wordbook of the i-th word in l.

    The function returns a (lexicographicaly sorted) list of all the words
    in l with maximum number of anagrams (in wordbook as recorded in anagcount)
    
    >>> max_anagram(["listen","care", "item", "year", "race", "ear"], [3, 2, 3, 0, 2, 2])
    ['item', 'listen']
    '''
    print(l)
    # r.sort()
    # print(max(r))
    # l.sort()
    index = 0
    max_array = []
    for item in r:
        if item == max(r):
            print(l[index])
            max_array.append(l[index])
        index +=1
    
    #YOUR CODE GOES HERE
    max_array.sort()
    return max_array

def zero_anagram(l = ["listen","care", "item", "year", "race", "ear"], r = count_anagrams(["listen","care", "item", "year", "race", "ear"])):
    index = 0
    max_array = []
    for item in r:
        if item == 0:
            print(l[index])
            max_array.append(l[index])
        index +=1
    
    #YOUR CODE GOES HERE
    max_array.sort()
    return max_array


def k_anagram(l = ["listen","care", "item", "year", "race", "ear"], r = count_anagrams(["listen","care", "item", "year", "race", "ear"]), k=2):
    index = 0
    max_array = []
    for item in r:
        if item == k:
            print(l[index])
            max_array.append(l[index])
        index +=1
    
    #YOUR CODE GOES HERE
    max_array.sort()
    return max_array



def word_anagrams(word):
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
       
    #YOUR CODE GOES HERE
    wordbook=open("english_wordbook.txt").read().lower().split()
    list(set(wordbook)).sort()
    anagrams = []
    for string2 in wordbook:
        if(len(string2) == len(word)):
            for char in word:
                string1_occurence = word.count(char)
                string2_occurence = string2.count(char)
                if string1_occurence != string2_occurence:
                    skip = True
            if skip== False:
                anagrams.append(string2)
            else:
                skip=False
    # anagrams.append(count -1)
    anagrams.remove(word)
    anagrams.sort()
    return anagrams


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
    if(len(w1) == len(w2)):
        for char in w1:
            string1_occurence = w1.count(char)
            string2_occurence = w2.count(char)
            if string1_occurence != string2_occurence:
                return False
    return True


# print(make_anagrams(["listen","care", "item", "year", "race", "ear"]))
# print(clean_word())
# main('able "acre bale beyond" binary boat brainy care cat cater crate lawn\nlist race react cat sheet silt slit trace boat cat crate.\n')

print(test_letters("teen", "need"))