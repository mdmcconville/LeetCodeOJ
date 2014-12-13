"""
My solution for Leetcode OJ.
"""

class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        # Make the string into a list
        lst = s.split()
        lst.reverse()
        # Make the reversed list into a string
        return ' '.join(lst)

# Testing
def main():
    sol = Solution()
    print(sol.reverseWords("blue is sky the"))
    print(sol.reverseWords("10 9 8 7 6 5 4 3 2 1"))
    print(sol.reverseWords("    blue    is  \tsky the"))

main()
