"""
String Reversal

My solution to the "Reverse Words in a String" problem on LeetCode OJ. Reverses
an input string. For example, "See Spot run" would be "run Spot See" reversed.
"""

def reverseIt(string):
    # Make the string into a list
    lst = string.split()
    lst.reverse()
    # Make the reversed list into a string
    return ' '.join(lst)
