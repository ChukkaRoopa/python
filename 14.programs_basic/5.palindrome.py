# Find string is a palindrome or not

def pali_str(string):
    rev_str = ''
    for i in string:
        rev_str = i + rev_str
    if rev_str == string:
        return True
    return False
print(pali_str('maddam'))