"""
program that prompts the user for a vanity plate and then
- output Valid if meets all of the requirements
- or Invalid if it does not.
"""

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    """
    Returns True if s meets all requirements
    and False if it does not.
    """

    if not (len(s) >= 2 and len(s) <= 6):
        return False
    elif not s[:2].isalpha():
        return False
    elif has_punc(s):
        return False
    elif not numbers(s):
        return False
    else:
        return True

def numbers(s):
    """
    Returns True if
    - numbers are not in the middle CS50P
    - number doesn't start with '0' CS05
    else return False
    """
    first_digit = True
    for i in s:
        if i.isdigit() and first_digit:
            first_digit = False
            if i == "0":
                return False

    for i in range(len(s)):
        if s[i].isdigit():
            if not (s[i:].isdigit()):
                return False

    return True


def has_punc(s):
    """ 
    Returns True if the string has punctuation
    else return False
    """

    punc = "'.,\";:?!"
    for i in s:
        if i in punc:
            return True
    return False 


main()