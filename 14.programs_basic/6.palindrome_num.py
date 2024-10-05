# Program for a palindrome number

def pali_num(number):

    number = str(number)
    rev_str = ''
    for i in number:
        rev_str = i + rev_str
    if number == rev_str:
        return True
    return False

print(pali_num(123321))