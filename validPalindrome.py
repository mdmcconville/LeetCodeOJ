import string

"""
This determines whether a given string is a palindrome regardless of case,
punctuation, or whitespace.
"""

class Solution:
    """
    Precondition: s is a string
    Postcondition: returns a boolean
    """
    def isPalindrome(self, s):
        # Case: string is empty
        if not s:
            return True
        else:
            # Remove whitespace and punctuation and make all lower-case
            s = ''.join(i for i in s if i not in(string.punctuation +
                                                 string.whitespace)).lower()
            
            # Return whether the reversed string equals the original
            return s == s[::-1]

