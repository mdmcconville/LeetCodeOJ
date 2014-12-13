"""
String Reversal

My solution to the "Reverse Words in a String" problem on LeetCode OJ. Reverses
an input string. For example, "See Spot run" would be "run Spot See" reversed.
"""

def reverseIt(string):
    # Make the string into a list, reverse it, and back to string
    return ' '.join(reversed(string.split()))

