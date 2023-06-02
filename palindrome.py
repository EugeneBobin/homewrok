import string

def is_palindrome(s):
    s = s.lower()
    s = ''.join(i for i in s if i not in string.punctuation)
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1

    return True
print(is_palindrome(input("enter the palindrome :")))
