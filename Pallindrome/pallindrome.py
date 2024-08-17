import re
def isPalindrome(string):
    string = string.lower()
    string = re.sub(r'[^a-zA-Z0-9]', '', string)
    if string == string[::-1]:
        return "palindrome"
    else:
        return "not palindrome."

string = input("Enter string: ")
print(isPalindrome(string))
