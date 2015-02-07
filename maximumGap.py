"""
Given an un-sorted list, determine the maximum gap between sucessive values.
"""

class Solution:
    """
    Precondition: num is an unsorted list of ints
    Postcondition: returns an int
    """
    def maximumGap(self, num):
        # List to store gaps between successive values
        gaps = []
        if len(num) < 2:
            return 0
        else:
            # Sort the list
            num.sort()
            for i in range(len(num)-1):
                gaps.append(num[i+1]-num[i])
            # Return the largest gap
            return max(gaps)
