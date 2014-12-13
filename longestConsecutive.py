"""
Longest Consecutive Sequence

Solution to the "Longest Consecutive Sequence" problem on LeetCode OJ. Given a
list of integers, the longest sequence length is returned. So [1, 2, 3, 6, 7]
would return 3.

precondition: num is a list of ints
postcondition: returns an int
"""

def longestConsecutive(num):
    # Make a list of lists
    lst = [0]
    count = 1
    keepGoing = True
    # Sort the list of ints
    num.sort()
    for i in range(len(num)):
        if i != len(num) - 1:
            # Keep searching if next number is the same or one greater
            if num[i] == num[i+1] - 1:
                count += 1
            elif num[i] != num[i+1]:
                keepGoing = False
        else:
            keepGoing = False
        if (keepGoing == False):
            lst.append(count)
            count = 1
            keepGoing = True

    return max(lst)

