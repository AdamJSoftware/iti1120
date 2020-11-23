def main():
    if True:
        print('if is here')
    elif True:
        print('elif is here')
    else:
        print('if all else failse this will print')
    # IT WILL ONLY HIT ONE STATEMENT

    print('NEXT IF BRANCH')

    if False:
        # as this statement is false, it will not print
        print('if is here')
    elif True:
        # this is the next statement, thus this will run, but the one under it will not 
        print('elif is here')
    else:
        print('if all else failse this will print')


    print('NEXT IF BRANCH')

    if False:
        # as this statement is false, it will not print
        print('if is here')
    elif False:
        # this is the next statement, thus this will run, but the one under it will not 
        print('elif is here')
    else:
        #as all else failed, this is the final part of the if branch and this will print, there is no check for a true statement
        print('if all else failse this will print')
    
    print('NEXT IF BRANCH')
    if True:
        print('this if branch')
    print('NEXT IF BRANCH')
    if True:
        print('and this if branch are seperate')
    else:
        print('this is branch will not print')
    print('NEXT IF BRANCH')
    if False:
        print('and this if branch are seperate')
    else:
        print('this is branch will not print')



if __name__ == "__main__":
    main()