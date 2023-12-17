'''
the requirements, though, are:

In plates.py, implement a program that prompts the user for a vanity plate and then output Valid if meets all of the requirements or
Invalid if it does not. Assume that any letters in the user’s input will be uppercase. Structure your program per the below, wherein is_valid
returns True if s meets all requirements and False if it does not. Assume that s will be a str. You’re welcome to implement additional functions for is_valid
to call (e.g., one function per requirement).
'''

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if (not startsWithTwoLetters(s)):
        return False
    if (not goodLength(s)):
        return False
    if (not endingNums(s)):
        return False
    if (not validChars(s)):
        return False
    return True

#“All vanity plates must start with at least two letters.”
def startsWithTwoLetters(s):
    i = 0
    for c in s:
        if (i == 0 or i == 1):
            if (not c.isalpha()):
                return False
            i += 1
    return True

# “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
def goodLength(s):
    if (len(s) < 2 or len(s) > 6):
        return False
    return True

# “Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable …
    #vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
def endingNums(s):
    firstNum = False
    for c in s:
        if (not firstNum):
            if (c.isnumeric()):
                firstNum = True
            if (c == '0'):
                return False
        else:
            if (c.isalpha()):
                return False
    return True

#“No periods, spaces, or punctuation marks are allowed.”
def validChars(s):
    for c in s:
        if (not (c.isalpha() or c.isnumeric())):
            return False
    return True

main()
